import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "registry" / "seo" / "moonn-production-83-schema-snippets.json"
AUDIT = ROOT / "registry" / "seo" / "moonn-production-83-seo-audit.json"
ENTITY_GRAPH = ROOT / "registry" / "seo" / "moonn-authority-entity-graph.json"
OUT = ROOT / "assets" / "moonn-seo-aeo-enhancer.js"


def extract_json_ld(snippet: str) -> dict:
    match = re.search(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', snippet, flags=re.DOTALL)
    if not match:
        raise ValueError("JSON-LD script not found")
    return json.loads(match.group(1))


def path_key(url: str) -> str:
    return re.sub(r"/+$", "", url.replace("https://moonn.ru", "")) or "/"


def uniq(values: list[str]) -> list[str]:
    result = []
    for value in values:
        if value and value not in result:
            result.append(value)
    return result


def enhance_person_schema(schema: dict, entity_graph: dict) -> dict:
    person = entity_graph["person"]
    same_as = entity_graph.get("same_as", [])
    organizations = entity_graph.get("organizations", [])
    for node in schema.get("@graph", []):
        if node.get("@id") != "https://moonn.ru/#tatiana-munn":
            continue
        node["alternateName"] = uniq(list(node.get("alternateName", [])) + person.get("alternate_names", []))
        node["jobTitle"] = uniq(list(node.get("jobTitle", [])) + person.get("job_titles", []))
        node["sameAs"] = uniq(list(node.get("sameAs", [])) + same_as)
        affiliations = []
        for organization in organizations:
            if organization.get("relationship") != "affiliation":
                continue
            affiliations.append({
                "@type": "Organization",
                "name": organization["name"],
                "alternateName": organization.get("alternate_name"),
                "url": organization["url"],
            })
        if affiliations:
            node["affiliation"] = affiliations
        node["subjectOf"] = [
            {"@type": "WebPage", "url": url}
            for url in same_as
            if url != "https://moonn.ru/"
        ]
    return schema


def main() -> int:
    schema_manifest = json.loads(SCHEMA.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    entity_graph = json.loads(ENTITY_GRAPH.read_text(encoding="utf-8"))
    page_meta = {}
    for page in audit["pages"]:
        page_meta[path_key(page["url"])] = {
            "title": page["title"],
            "description": page["description"],
            "alias": page["alias"],
            "url": page["url"],
        }

    schemas = {}
    for item in schema_manifest["snippets"]:
        schema = extract_json_ld(item["snippet"])
        schema = enhance_person_schema(schema, entity_graph)
        schemas[path_key(item["url"])] = {
            "marker": item["marker"],
            "schema": schema,
        }

    payload = {
        "generated_at": "2026-05-02",
        "scope": "moonn-production-83",
        "schemas": schemas,
        "page_meta": page_meta,
        "entity_bridge": {
            "text": entity_graph["person"]["visible_bridge_text"],
            "links": entity_graph["person"]["visible_bridge_links"],
        },
    }

    js = f"""/*
  Moonn production SEO/AEO enhancer.
  Generated from registry/seo/moonn-production-83-schema-snippets.json.
  Purpose: rendered-DOM SEO support for Tilda pages while source-level block cleanup is pending.
*/
(function () {{
  'use strict';
  var PAYLOAD = {json.dumps(payload, ensure_ascii=False, separators=(",", ":"))};

  function normalizedPath() {{
    var path = window.location.pathname || '/';
    path = path.replace(/\\/+$/, '');
    return path || '/';
  }}

  function findPageData() {{
    var path = normalizedPath();
    return PAYLOAD.schemas[path] || PAYLOAD.schemas[path + '/'] || PAYLOAD.schemas['/'];
  }}

  function findPageMeta() {{
    var path = normalizedPath();
    return PAYLOAD.page_meta[path] || PAYLOAD.page_meta[path + '/'] || PAYLOAD.page_meta['/'] || {{}};
  }}

  function ensureMeta(name, content) {{
    if (!content) return;
    var selector = 'meta[name=\"' + name + '\"]';
    var node = document.head.querySelector(selector);
    if (!node) {{
      node = document.createElement('meta');
      node.setAttribute('name', name);
      document.head.appendChild(node);
    }}
    if (!node.getAttribute('content')) {{
      node.setAttribute('content', content);
    }}
  }}

  function injectSchema() {{
    var page = findPageData();
    if (!page || !page.schema || document.getElementById('moonn-rendered-jsonld')) return;
    var script = document.createElement('script');
    script.type = 'application/ld+json';
    script.id = 'moonn-rendered-jsonld';
    script.setAttribute('data-moonn-seo-marker', page.marker);
    script.text = JSON.stringify(page.schema);
    document.head.appendChild(script);
  }}

  function fixLinks() {{
    Array.prototype.forEach.call(document.querySelectorAll('a[href]'), function (link) {{
      var href = link.getAttribute('href') || '';
      var next = href;
      next = next.replace(/^http:\\/\\/wa\\.me\\/79777770303/i, 'https://wa.me/79777770303');
      next = next.replace(/^http:\\/\\/twa\\.me\\/79777770303/i, 'https://wa.me/79777770303');
      next = next.replace(/^http:\\/\\/\\.moonn\\.ru/i, 'https://moonn.ru');
      next = next.replace(/^\\/http:\\/\\/wa\\.me\\/\\+?79777770303/i, 'https://wa.me/79777770303');
      if (next !== href) {{
        link.setAttribute('href', next);
        link.setAttribute('data-moonn-link-fixed', '1');
      }}
      if (/^https:\\/\\/wa\\.me\\//i.test(next)) {{
        link.setAttribute('rel', 'nofollow noopener');
      }}
    }});
  }}

  function improveImages() {{
    var meta = findPageMeta();
    var title = meta.title || document.title || 'Татьяна Мунн, психолог МГУ';
    Array.prototype.forEach.call(document.querySelectorAll('img'), function (img, index) {{
      var alt = (img.getAttribute('alt') || '').trim();
      if (!alt || alt === 'image' || alt === 'photo') {{
        img.setAttribute('alt', title + ' - изображение ' + (index + 1));
        img.setAttribute('data-moonn-alt-fixed', '1');
      }}
      if (!img.getAttribute('loading')) {{
        img.setAttribute('loading', 'lazy');
      }}
      if (!img.getAttribute('decoding')) {{
        img.setAttribute('decoding', 'async');
      }}
    }});
  }}

  function improveHead() {{
    var meta = findPageMeta();
    ensureMeta('author', 'Татьяна Мунн');
    ensureMeta('publisher', 'Татьяна Мунн');
    ensureMeta('robots', 'index, follow, max-image-preview:large');
    ensureMeta('theme-color', '#f4d8ee');
    if (meta.description) ensureMeta('abstract', meta.description);
  }}

  function injectEntityBridge() {{
    if (document.getElementById('moonn-entity-bridge')) return;
    var bridge = PAYLOAD.entity_bridge || {{}};
    if (!bridge.text) return;
    var section = document.createElement('section');
    section.id = 'moonn-entity-bridge';
    section.setAttribute('aria-label', 'Профессиональная связка Татьяны Мунн');
    section.innerHTML = '<p></p><nav aria-label="Профили Татьяны Мунн"></nav>';
    section.querySelector('p').textContent = bridge.text;
    var nav = section.querySelector('nav');
    (bridge.links || []).forEach(function (item, index) {{
      if (index) nav.appendChild(document.createTextNode(' · '));
      var link = document.createElement('a');
      link.href = item.url;
      link.textContent = item.label;
      link.rel = 'me noopener';
      nav.appendChild(link);
    }});
    document.body.appendChild(section);
  }}

  function injectEntityBridgeStyles() {{
    if (document.getElementById('moonn-entity-bridge-style')) return;
    var style = document.createElement('style');
    style.id = 'moonn-entity-bridge-style';
    style.textContent = [
      '#moonn-entity-bridge{{max-width:980px;margin:42px auto 26px;padding:0 20px 10px;font:12px/1.55 Arial,sans-serif;color:rgba(38,32,48,.68);text-align:center;position:relative;z-index:3;}}',
      '#moonn-entity-bridge p{{margin:0 0 8px;}}',
      '#moonn-entity-bridge nav{{font-size:12px;}}',
      '#moonn-entity-bridge a{{color:rgba(88,48,168,.82);text-decoration:none;border-bottom:1px solid rgba(88,48,168,.22);}}',
      '#moonn-entity-bridge a:hover{{color:#5d2ee6;border-bottom-color:rgba(93,46,230,.55);}}',
      '@media (max-width:640px){{#moonn-entity-bridge{{margin:30px auto 18px;font-size:11px;}}}}'
    ].join('');
    document.head.appendChild(style);
  }}

  function run() {{
    injectSchema();
    fixLinks();
    improveImages();
    improveHead();
    injectEntityBridgeStyles();
    injectEntityBridge();
    document.documentElement.setAttribute('data-moonn-seo-aeo-enhanced', PAYLOAD.scope);
  }}

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', run);
  }} else {{
    run();
  }}
}}());
"""
    OUT.write_text(js, encoding="utf-8")
    print(json.dumps({"out": str(OUT.relative_to(ROOT)), "bytes": OUT.stat().st_size}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
