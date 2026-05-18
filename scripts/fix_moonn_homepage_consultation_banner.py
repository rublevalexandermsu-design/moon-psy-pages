from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "docs" / "consultation-home-banner-2026"

TARGETS = [
    ROOT / "docs" / "tatiana-munn-exam-prep" / "homepage-t123-combined-2026-05-12.html",
    ROOT / "docs" / "tatiana-munn-art-gallery" / "homepage-t123-combined-2026-05-12.html",
    ROOT / "docs" / "tatiana-munn-reviews-home-banner" / "homepage-t123-combined-2026-05-17.html",
]

MARKER = '<section id="moonn-consultation-home-banner"'

PRODUCT_IMAGE = (
    "https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@"
    "85584ecd84fee5511a6fed6b593aaea22c4b22de/assets/timepad/"
    "tatiana-munn-psychological-consultation-msu-online-offline-moscow-timepad-2026.png"
)


COMPACT_BLOCK = f"""<section id="moonn-consultation-home-banner" class="moonn-consultation-home-banner" data-moonn-consultation-compact="2026-05-12" aria-labelledby="moonn-consultation-home-title">
  <style>
    #moonn-consultation-home-banner {{
      --moonn-consult-ink: #2f2450;
      --moonn-consult-violet: #5b2ec4;
      --moonn-consult-magenta: #d93f9a;
      --moonn-consult-sky: #42b8ee;
      margin: 0;
      padding: 46px 20px 54px;
      background: linear-gradient(100deg, #fbf4ff 0%, #f4eeff 48%, #eaf6ff 100%);
      color: var(--moonn-consult-ink);
      font-family: Arial, sans-serif;
      box-sizing: border-box;
      overflow: hidden;
      clear: both;
      position: relative;
      z-index: 1;
    }}
    #moonn-consultation-home-banner *,
    #moonn-consultation-home-banner *::before,
    #moonn-consultation-home-banner *::after {{
      box-sizing: border-box;
      letter-spacing: 0;
    }}
    #moonn-consultation-home-banner .consult-wrap {{
      width: min(100%, 1160px);
      margin: 0 auto;
      display: grid;
      grid-template-columns: minmax(0, 1.08fr) minmax(300px, .92fr);
      gap: 0;
      align-items: stretch;
      min-height: 0;
      border: 1px solid rgba(118, 68, 190, .18);
      border-radius: 28px;
      background: rgba(255, 255, 255, .82);
      box-shadow: 0 22px 56px rgba(97, 66, 160, .16);
      overflow: hidden;
    }}
    #moonn-consultation-home-banner .consult-copy {{
      min-width: 0;
      padding: 38px 38px 38px 42px;
      display: grid;
      align-content: center;
      gap: 16px;
    }}
    #moonn-consultation-home-banner .consult-eyebrow {{
      width: fit-content;
      max-width: 100%;
      padding: 7px 14px;
      border-radius: 999px;
      background: #efe7ff;
      color: var(--moonn-consult-violet);
      font: 700 14px/1 Arial, sans-serif;
      text-transform: uppercase;
    }}
    #moonn-consultation-home-banner h2 {{
      margin: 0;
      max-width: 680px;
      color: var(--moonn-consult-violet);
      font: 900 clamp(31px, 4.2vw, 48px)/.98 Arial, sans-serif;
    }}
    #moonn-consultation-home-banner p {{
      margin: 0;
      max-width: 640px;
      color: #4c435d;
      font: 400 18px/1.5 Arial, sans-serif;
    }}
    #moonn-consultation-home-banner .consult-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 2px 0 0;
      padding: 0;
      list-style: none;
    }}
    #moonn-consultation-home-banner .consult-tags li {{
      min-height: 34px;
      display: inline-flex;
      align-items: center;
      padding: 7px 14px;
      border: 1px solid rgba(91, 46, 196, .18);
      border-radius: 999px;
      background: rgba(255, 255, 255, .72);
      color: #48375f;
      font: 500 14px/1.2 Arial, sans-serif;
      white-space: nowrap;
    }}
    #moonn-consultation-home-banner .consult-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 6px;
    }}
    #moonn-consultation-home-banner .consult-btn {{
      min-height: 48px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 13px 20px;
      border: 0;
      border-radius: 999px;
      background: linear-gradient(100deg, #7e2fe8 0%, #e046a6 52%, #43bce9 100%);
      box-shadow: 0 14px 26px rgba(116, 58, 205, .25);
      color: #fff !important;
      font: 800 15px/1.1 Arial, sans-serif;
      text-decoration: none !important;
      text-align: center;
      cursor: pointer;
      transition: transform .18s ease, box-shadow .18s ease;
    }}
    #moonn-consultation-home-banner .consult-btn:hover {{
      transform: translateY(-1px);
      box-shadow: 0 18px 34px rgba(116, 58, 205, .32);
    }}
    #moonn-consultation-home-banner .consult-btn-secondary {{
      background: rgba(255, 255, 255, .9);
      border: 1px solid rgba(91, 46, 196, .22);
      color: var(--moonn-consult-violet) !important;
      box-shadow: none;
    }}
    #moonn-consultation-home-banner .consult-offer {{
      min-width: 0;
      padding: 34px;
      display: grid;
      align-content: center;
      gap: 16px;
      background:
        radial-gradient(circle at 86% 14%, rgba(217, 63, 154, .18), transparent 34%),
        linear-gradient(135deg, #fff8f2 0%, #fff 52%, #f2fbff 100%);
      border-left: 1px solid rgba(118, 68, 190, .14);
    }}
    #moonn-consultation-home-banner .consult-price-list {{
      display: grid;
      gap: 12px;
    }}
    #moonn-consultation-home-banner .consult-price-row {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      align-items: baseline;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(118, 68, 190, .12);
      color: #3e3150;
      font: 700 19px/1.25 Arial, sans-serif;
    }}
    #moonn-consultation-home-banner .consult-price-row strong {{
      color: #c43382;
      font-size: 25px;
      white-space: nowrap;
    }}
    #moonn-consultation-home-banner .consult-summer {{
      padding: 18px 20px;
      border: 1px solid rgba(217, 63, 154, .18);
      border-radius: 20px;
      background: rgba(255, 255, 255, .76);
    }}
    #moonn-consultation-home-banner .consult-summer strong {{
      display: block;
      color: #c43382;
      font: 900 24px/1.15 Arial, sans-serif;
    }}
    #moonn-consultation-home-banner .consult-summer span {{
      display: block;
      margin-top: 5px;
      color: #6b5870;
      font: 500 15px/1.35 Arial, sans-serif;
    }}
    #moonn-consultation-home-banner .consult-note {{
      display: none;
      color: #5d5267;
      font: 13px/1.35 Arial, sans-serif;
    }}
    @media (min-width: 761px) and (max-width: 980px) {{
      #moonn-consultation-home-banner {{
        padding: 34px 18px 40px;
      }}
      #moonn-consultation-home-banner .consult-wrap {{
        grid-template-columns: minmax(0, 1fr) minmax(285px, .82fr);
        border-radius: 24px;
      }}
      #moonn-consultation-home-banner .consult-copy {{
        padding: 28px 24px 28px 28px;
        gap: 12px;
      }}
      #moonn-consultation-home-banner .consult-offer {{
        padding: 24px;
      }}
      #moonn-consultation-home-banner h2 {{
        font-size: clamp(28px, 4vw, 34px);
      }}
      #moonn-consultation-home-banner p {{
        font-size: 15px;
        line-height: 1.42;
      }}
      #moonn-consultation-home-banner .consult-tags {{
        gap: 8px;
      }}
      #moonn-consultation-home-banner .consult-tags li {{
        min-height: 30px;
        padding: 6px 10px;
        font-size: 12px;
      }}
      #moonn-consultation-home-banner .consult-btn {{
        min-height: 42px;
        padding: 11px 16px;
        font-size: 13px;
      }}
      #moonn-consultation-home-banner .consult-price-row {{
        font-size: 16px;
      }}
      #moonn-consultation-home-banner .consult-price-row strong {{
        font-size: 21px;
      }}
      #moonn-consultation-home-banner .consult-summer {{
        padding: 15px 16px;
      }}
      #moonn-consultation-home-banner .consult-summer strong {{
        font-size: 20px;
      }}
    }}
    @media (max-width: 760px) {{
      #moonn-consultation-home-banner {{
        padding: 34px 16px 42px;
      }}
      #moonn-consultation-home-banner .consult-wrap {{
        grid-template-columns: 1fr;
      }}
      #moonn-consultation-home-banner .consult-offer {{
        border-left: 0;
        border-top: 1px solid rgba(118, 68, 190, .14);
      }}
    }}
    @media (max-width: 640px) {{
      #moonn-consultation-home-banner {{
        padding: 28px 12px 34px;
      }}
      #moonn-consultation-home-banner .consult-wrap {{
        border-radius: 22px;
      }}
      #moonn-consultation-home-banner .consult-copy,
      #moonn-consultation-home-banner .consult-offer {{
        padding: 20px 18px;
      }}
      #moonn-consultation-home-banner h2 {{
        font-size: clamp(26px, 9vw, 34px);
      }}
      #moonn-consultation-home-banner p {{
        font-size: 15px;
        line-height: 1.4;
      }}
      #moonn-consultation-home-banner .consult-eyebrow {{
        font-size: 12px;
      }}
      #moonn-consultation-home-banner .consult-tags {{
        gap: 8px;
      }}
      #moonn-consultation-home-banner .consult-tags li {{
        min-height: 30px;
        padding: 6px 10px;
        font-size: 12px;
      }}
      #moonn-consultation-home-banner .consult-actions {{
        display: grid;
      }}
      #moonn-consultation-home-banner .consult-btn {{
        width: 100%;
        min-height: 42px;
        padding: 11px 14px;
        font-size: 13px;
      }}
      #moonn-consultation-home-banner .consult-price-row {{
        display: grid;
        gap: 4px;
        font-size: 16px;
        padding-bottom: 10px;
      }}
      #moonn-consultation-home-banner .consult-price-row strong {{
        font-size: 21px;
      }}
      #moonn-consultation-home-banner .consult-summer {{
        padding: 14px 16px;
      }}
      #moonn-consultation-home-banner .consult-summer strong {{
        font-size: 20px;
      }}
    }}
  </style>
  <div class="consult-wrap">
    <div class="consult-copy">
      <span class="consult-eyebrow">Онлайн · Татьяна Мунн · Психолог МГУ</span>
      <h2 id="moonn-consultation-home-title">Онлайн-консультации для вас и ваших близких</h2>
      <p>Индивидуальные консультации для себя, подростка, семьи или близких. Можно выбрать одну встречу или пакет из 3 консультаций.</p>
      <ul class="consult-tags" aria-label="Формат консультаций">
        <li>Для себя</li>
        <li>Для подростка</li>
        <li>Для семьи</li>
        <li>Онлайн-формат</li>
      </ul>
      <div class="consult-actions">
        <a class="consult-btn" data-moonn-consult-product="one" href="#order:Онлайн-консультация Татьяны Мунн =8000:::image={PRODUCT_IMAGE}">Оплатить 1 консультацию</a>
        <a class="consult-btn consult-btn-secondary" href="https://moonn.timepad.ru/event/3973843/">Подробнее</a>
      </div>
    </div>
    <div class="consult-offer" aria-label="Стоимость онлайн-консультаций">
      <div class="consult-price-list">
        <div class="consult-price-row"><span>1 консультация</span><strong>8 000 ₽</strong></div>
        <div class="consult-price-row"><span>3 консультации</span><strong>21 000 ₽</strong></div>
      </div>
      <div class="consult-summer">
        <strong>Онлайн-консультации лето 2026</strong>
        <span>Летняя цена - 19 000 ₽</span>
        <span>при оплате до 31 мая</span>
        <span>Дни приёма: среда, четверг, пятница с 9:00 до 23:00</span>
      </div>
      <div class="consult-actions">
        <a class="consult-btn" data-moonn-consult-product="three" href="#order:Пакет 3 онлайн-консультаций Татьяны Мунн =19000:::image={PRODUCT_IMAGE}">Оплатить пакет 3 консультации</a>
      </div>
      <div class="consult-note" data-moonn-consult-payment-note>Оплата открывается в защищенной корзине сайта через T-Bank. Платежные данные вводятся на стороне банка.</div>
    </div>
  </div>
  <script>
    (function() {{
      if (window.__moonnConsultationHomeBannerReady) return;
      window.__moonnConsultationHomeBannerReady = true;

      var productImage = '{PRODUCT_IMAGE}';
      var products = {{
        one: {{
          name: 'Онлайн-консультация Татьяны Мунн',
          price: 8000,
          amount: 8000,
          quantity: 1,
          img: productImage,
          sku: 'moonn-consultation-online-1-2026'
        }},
        three: {{
          name: 'Пакет 3 онлайн-консультаций Татьяны Мунн',
          price: 19000,
          amount: 19000,
          quantity: 1,
          img: productImage,
          sku: 'moonn-consultation-online-3-summer-2026'
        }}
      }};

      function repairTildaCart() {{
        var cartRecord = document.querySelector('[data-record-type="706"][id]');
        if (!cartRecord) return null;
        var cartRoot = cartRecord.querySelector('.t706');
        if (!cartRoot) {{
          cartRoot = document.createElement('div');
          cartRoot.className = 't706';
          cartRecord.appendChild(cartRoot);
        }}
        ['.t706__carticon', '.t706__carticon-wrapper', '.t706__cartwin'].forEach(function(selector) {{
          Array.prototype.slice.call(document.querySelectorAll(selector)).forEach(function(node) {{
            if (node && !cartRoot.contains(node)) cartRoot.appendChild(node);
          }});
        }});
        return cartRoot;
      }}

      function initTildaCart() {{
        var cartRoot = repairTildaCart();
        var cartRecord = document.querySelector('[data-record-type="706"][id]');
        if (!cartRoot || !cartRecord || typeof t_onFuncLoad !== 'function') return;
        t_onFuncLoad('tcart__init', function() {{
          try {{
            tcart__init(cartRecord.id.replace(/^rec/, ''), {{ cssClassName: '' }});
          }} catch (error) {{
            console.warn('Consultation cart init skipped', error);
          }}
        }});
      }}

      function repairTildaOrderFormHandlers() {{
        var cartRecord = document.querySelector('[data-record-type="706"][id]');
        var form = document.querySelector('.t706__cartwin form.js-form-proccess');
        if (!cartRecord || !form) return;
        try {{
          if (window.initForms && cartRecord.id) delete window.initForms[cartRecord.id];
          if (typeof t_forms__initFormFields === 'function') t_forms__initFormFields(cartRecord);
          if (typeof t_forms__addInputItsGood === 'function') t_forms__addInputItsGood(cartRecord);
          if (typeof t_forms__addAttrAction === 'function') t_forms__addAttrAction(cartRecord);
          if (typeof t_forms__onSubmit === 'function') t_forms__onSubmit(cartRecord);
          if (typeof t_forms__onClick === 'function') t_forms__onClick(cartRecord);
          if (typeof t_forms__onRender === 'function') t_forms__onRender(cartRecord);
          if (typeof t_forms__addFocusOnTab === 'function') t_forms__addFocusOnTab(cartRecord);
        }} catch (error) {{
          console.warn('Consultation order form repair skipped', error);
        }}
      }}

      function enhanceTildaPaymentUi() {{
        var cart = document.querySelector('.t706__cartwin, .t706');
        if (!cart) return;
        repairTildaOrderFormHandlers();
        Array.prototype.slice.call(cart.querySelectorAll('.t-submit, button[type="submit"], .t-btnflex_type_submit')).forEach(function(submit) {{
          var submitText = submit.querySelector('.t-btnflex__text, span') || submit;
          if ((submitText.textContent || '').trim() !== 'Перейти к оплате') submitText.textContent = 'Перейти к оплате';
          submit.setAttribute('aria-label', 'Перейти к оплате через T-Bank');
        }});
        var paymentBlock = Array.prototype.slice.call(cart.querySelectorAll('*')).find(function(node) {{
          return (node.textContent || '').trim() === 'Способ оплаты';
        }});
        if (paymentBlock && !cart.querySelector('.moonn-consultation-payment-note')) {{
          var note = document.createElement('div');
          note.className = 'moonn-consultation-payment-note';
          note.textContent = 'После нажатия кнопки откроется защищенная страница T-Bank. Данные карты вводятся на стороне банка.';
          var container = paymentBlock.parentElement || paymentBlock;
          container.appendChild(note);
        }}
      }}

      function clearConsultationCartState() {{
        try {{
          if (window.tcart) {{
            window.tcart.products = [];
            window.tcart.amount = 0;
            window.tcart.total = 0;
          }}
          if (typeof tcart__reDrawCartIcon === 'function') tcart__reDrawCartIcon();
        }} catch (error) {{
          console.warn('Consultation cart cleanup skipped', error);
        }}
      }}

      function openConsultationPayment(productKey) {{
        var product = products[productKey];
        if (!product) return false;
        initTildaCart();
        if (typeof tcart__addProduct !== 'function' || typeof tcart__openCart !== 'function') return false;
        try {{
          clearConsultationCartState();
          tcart__addProduct(product);
          if (typeof tcart__reDrawCartIcon === 'function') tcart__reDrawCartIcon();
          tcart__openCart();
          setTimeout(enhanceTildaPaymentUi, 200);
          setTimeout(enhanceTildaPaymentUi, 900);
          var note = document.querySelector('[data-moonn-consult-payment-note]');
          if (note) note.style.display = 'block';
          return true;
        }} catch (error) {{
          console.warn('Consultation payment open skipped', error);
          return false;
        }}
      }}

      initTildaCart();
      setTimeout(initTildaCart, 300);
      setTimeout(initTildaCart, 1200);
      setTimeout(repairTildaOrderFormHandlers, 1500);
      setInterval(enhanceTildaPaymentUi, 1500);

      document.addEventListener('click', function(event) {{
        var button = event.target && event.target.closest && event.target.closest('[data-moonn-consult-product]');
        if (!button) return;
        var productKey = button.getAttribute('data-moonn-consult-product');
        if (openConsultationPayment(productKey)) {{
          event.preventDefault();
          event.stopPropagation();
        }}
      }}, true);
    }})();
  </script>
</section>"""


def replace_consultation_block(html: str) -> str:
    start = html.find(MARKER)
    if start == -1:
        raise ValueError("Consultation marker not found")
    end_marker = "\n</section>"
    end = html.find(end_marker, start)
    if end == -1:
        raise ValueError("Consultation section close not found")
    end += len(end_marker)
    return html[:start].rstrip() + "\n\n" + COMPACT_BLOCK.strip() + html[end:]


def validate(html: str, path: Path) -> None:
    checks = {
        "compact marker": 'data-moonn-consultation-compact="2026-05-12"',
        "section close": "</section>",
        "one product sku": "moonn-consultation-online-1-2026",
        "three product sku": "moonn-consultation-online-3-summer-2026",
        "tilda cart bridge": "tcart__addProduct",
    }
    missing = [name for name, needle in checks.items() if needle not in html]
    if missing:
        raise ValueError(f"{path}: missing {', '.join(missing)}")
    if "moonn-consultation-home-signature" in html:
        raise ValueError(f"{path}: old unbounded consultation signature remained")
    if html.count(MARKER) != 1:
        raise ValueError(f"{path}: expected one consultation marker, got {html.count(MARKER)}")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "tilda-html-block-compact-final.html").write_text(COMPACT_BLOCK.strip() + "\n", encoding="utf-8")

    latest_combined = None
    for target in TARGETS:
        html = target.read_text(encoding="utf-8")
        updated = replace_consultation_block(html)
        validate(updated, target)
        target.write_text(updated, encoding="utf-8")
        if target.name == "homepage-t123-combined-2026-05-12.html" and "tatiana-munn-exam-prep" in target.parts:
            latest_combined = updated

    if latest_combined:
        preview = (
            "<!doctype html><html lang=\"ru\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
            "<title>Moonn homepage consultation compact preview</title></head><body>"
            + latest_combined
            + "</body></html>"
        )
        (OUTPUT_DIR / "homepage-t123-combined-compact-preview.html").write_text(preview, encoding="utf-8")


if __name__ == "__main__":
    main()
