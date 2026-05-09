# 2026-05-09 Fast Restart Handoff — Moonn / Tilda Payment

Use this file to continue the Moonn workstream in a new Codex chat without loading the full old conversation.

## Canonical Workstream

- Project: Moonn / Tilda site.
- Repository: `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site`
- Git branch: `codex/moonn-seo-audit`
- Live page: `https://moonn.ru/podrostkovyy-lager-psihologiya`
- Tilda project: `8326812`
- Tilda page: `140348786`

## Current State

- Payment for `Подростковый лагерь по психологии` is working through native Tilda ST100/T-Bank.
- The custom page CTA `Оплатить участие` is bridged into native Tilda cart functions:
  - `tcart__addProduct`
  - `tcart__reDrawCartIcon`
  - `tcart__openCart`
- Live verification reached real `pay.tbank.ru` card-entry page with amount `30 000 ₽`.
- No real payment was submitted.

## Important Commits

- `b7fc89f` — `Open teen camp checkout via native Tilda cart`
- `6ca1991` — `Point teen camp Tilda head loader to native cart bridge`
- `ebb9b1b` — `Record teen camp payment verification`
- `5ac822d` — `Record Tilda payment learning rule`
- `9448c35` — `Clarify Tilda visual confirmation lesson`

## Key Lesson

Do not trust visual confirmations in Tilda as proof.

The green Tilda "saved" banner is only a UI signal. Treat it as a hypothesis until it survives independent checks:

1. Reopen Tilda HEAD and verify the Ace editor value.
2. Publish the page.
3. Probe live HTML for the expected loader and absence of the old loader.
4. Click the live CTA in Chrome.
5. Verify exactly one cart product and the expected amount.
6. Continue only to provider card-entry screen unless real payment submission is explicitly approved.

## Files To Read First In A New Chat

1. `docs/codex-chat-history.md`
2. `docs/teen-psychology-camp-2026/tilda-page-final.html`
3. `docs/teen-psychology-camp-2026/tilda-head-loader-final.html`
4. Root incident ledger if needed:
   `C:\пайто н тесты\Ано_институт_глаболизация\registry\project-ai\incidents.md`

## Suggested New Chat Startup Prompt

```text
Восстанови рабочий контур Moonn / Tilda site без чтения старого тяжёлого чата.

Репозиторий: C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site
Ветка: codex/moonn-seo-audit
Сначала прочитай:
1. docs/codex-handoffs/2026-05-09-fast-restart-moonn-payment.md
2. docs/codex-chat-history.md только последние записи за 2026-05-09
3. docs/teen-psychology-camp-2026/tilda-page-final.html
4. docs/teen-psychology-camp-2026/tilda-head-loader-final.html

Не перечитывай полный архив чата без причины. Сначала работай от handoff-файла и последних project-memory записей.

Критичное правило: для Tilda не доверять зелёной плашке сохранения. Проверять фактическое состояние через reopened Ace editor, published live HTML и браузерный результат.
```

## Performance Rule

If the current Codex chat becomes slow again, do not change repository or duplicate branch. Create a new chat with the startup prompt above and continue on the same canonical branch unless the next task is a genuinely separate workstream.
