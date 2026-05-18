const STORAGE_KEY = 'moonn_reviews_v1';
const ADMIN_TOKEN_KEY = 'moonn_reviews_admin_token_v1';
const MAX_REVIEWS = 300;
const MAX_COMMENT_LENGTH = 1200;
const MAX_NAME_LENGTH = 80;
const ALLOWED_ACTIONS = ['health', 'list', 'submit', 'hide', 'bootstrapAdmin'];

function doGet(event) {
  return handleRequest(event);
}

function doPost(event) {
  return handleRequest(event);
}

function handleRequest(event) {
  const params = Object.assign({}, event && event.parameter ? event.parameter : {});
  const action = String(params.action || 'list').trim();

  try {
    if (ALLOWED_ACTIONS.indexOf(action) === -1) {
      return respond(params, { ok: false, error: 'unknown_action' });
    }
    if (action === 'health') return respond(params, { ok: true, service: 'moonn-reviews', version: 1 });
    if (action === 'list') return respond(params, { ok: true, reviews: listPublicReviews() });
    if (action === 'submit') return respond(params, submitReview(params));
    if (action === 'hide') return respond(params, hideReview(params));
    if (action === 'bootstrapAdmin') return respond(params, bootstrapAdmin(params));
  } catch (error) {
    return respond(params, { ok: false, error: 'server_error', message: String(error && error.message || error) });
  }
}

function submitReview(params) {
  if (String(params.website || '').trim()) {
    return { ok: false, error: 'spam_rejected' };
  }

  const consent = ['1', 'true', 'yes', 'on'].indexOf(String(params.consent || '').toLowerCase()) !== -1;
  if (!consent) return { ok: false, error: 'consent_required' };

  const rating = Number(params.rating || 5);
  if (!Number.isFinite(rating) || rating < 1 || rating > 5) {
    return { ok: false, error: 'invalid_rating' };
  }

  const comment = cleanText(params.comment, MAX_COMMENT_LENGTH);
  if (comment.length < 8) return { ok: false, error: 'comment_too_short' };

  const namePublic = cleanText(params.name || params.name_public || 'Анонимно', MAX_NAME_LENGTH) || 'Анонимно';
  const context = cleanText(params.context || 'Отзыв', 80) || 'Отзыв';
  const source = cleanText(params.source || 'moonn_review_funnel', 100) || 'moonn_review_funnel';
  const now = new Date();
  const review = {
    id: Utilities.getUuid(),
    createdAt: now.toISOString(),
    publishedAt: now.toISOString(),
    rating: Math.round(rating),
    context,
    namePublic,
    comment,
    source,
    status: 'published',
    hidden: false,
    isTest: /тест|test/i.test(namePublic + ' ' + comment + ' ' + source)
  };

  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const reviews = readReviews_();
    reviews.unshift(review);
    writeReviews_(reviews.slice(0, MAX_REVIEWS));
  } finally {
    lock.releaseLock();
  }

  return { ok: true, review: publicReview(review), reviews: listPublicReviews() };
}

function hideReview(params) {
  requireAdminToken_(params);
  const id = String(params.id || '').trim();
  if (!id) return { ok: false, error: 'missing_id' };

  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const reviews = readReviews_();
    let found = false;
    reviews.forEach(function (review) {
      if (review.id === id) {
        review.hidden = true;
        review.status = 'hidden';
        review.hiddenAt = new Date().toISOString();
        found = true;
      }
    });
    writeReviews_(reviews);
    return { ok: found, hidden: found, id, reviews: listPublicReviews() };
  } finally {
    lock.releaseLock();
  }
}

function bootstrapAdmin(params) {
  const properties = PropertiesService.getScriptProperties();
  const existing = properties.getProperty(ADMIN_TOKEN_KEY);
  if (existing) return { ok: false, error: 'admin_token_already_configured' };
  const token = String(params.adminToken || '').trim();
  if (token.length < 24) return { ok: false, error: 'token_too_short' };
  properties.setProperty(ADMIN_TOKEN_KEY, token);
  return { ok: true };
}

function listPublicReviews() {
  return readReviews_()
    .filter(function (review) {
      return review && review.status === 'published' && review.hidden !== true;
    })
    .map(publicReview);
}

function publicReview(review) {
  return {
    id: review.id,
    createdAt: review.createdAt,
    publishedAt: review.publishedAt,
    rating: review.rating,
    context: review.context,
    namePublic: review.namePublic,
    comment: review.comment,
    source: review.source,
    isTest: review.isTest === true
  };
}

function readReviews_() {
  const raw = PropertiesService.getScriptProperties().getProperty(STORAGE_KEY);
  if (!raw) return [];
  const parsed = JSON.parse(raw);
  return Array.isArray(parsed) ? parsed : [];
}

function writeReviews_(reviews) {
  PropertiesService.getScriptProperties().setProperty(STORAGE_KEY, JSON.stringify(reviews));
}

function cleanText(value, limit) {
  return String(value || '')
    .replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, ' ')
    .replace(/\s+\n/g, '\n')
    .replace(/[ \t]{2,}/g, ' ')
    .trim()
    .slice(0, limit);
}

function requireAdminToken_(params) {
  const expected = PropertiesService.getScriptProperties().getProperty(ADMIN_TOKEN_KEY);
  if (!expected) throw new Error('admin_token_not_configured');
  const actual = String(params.adminToken || '').trim();
  if (!actual || actual !== expected) throw new Error('admin_token_invalid');
}

function respond(params, payload) {
  const callback = String(params.callback || '').trim();
  const json = JSON.stringify(payload);
  if (/^[A-Za-z_$][0-9A-Za-z_$]*(?:\.[A-Za-z_$][0-9A-Za-z_$]*)?$/.test(callback)) {
    return ContentService
      .createTextOutput(callback + '(' + json + ');')
      .setMimeType(ContentService.MimeType.JAVASCRIPT);
  }
  return ContentService
    .createTextOutput(json)
    .setMimeType(ContentService.MimeType.JSON);
}

function setAdminToken(token) {
  if (!token || String(token).length < 24) throw new Error('token_too_short');
  PropertiesService.getScriptProperties().setProperty(ADMIN_TOKEN_KEY, String(token));
  return { ok: true };
}

function clearAllReviewsForEmergency() {
  PropertiesService.getScriptProperties().deleteProperty(STORAGE_KEY);
  return { ok: true };
}
