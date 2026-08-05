# Prompt Version Changelog

This document tracks the changes between prompt iterations (v11 through v15) for the qwen3.7-flash document classifier.

---

## v11 — Estimate vs Bill Rule

**Baseline prompt for the estimate-vs-bill disambiguation work.**

- **Check 7 (Financial Document):** Restored v9 wording for agency/vendor ESTIMATE documents with unit prices/amounts/totals (invoice), and added concrete bill signals ("EST NO", "REVISES EST", "PRIOR ADJUSTMENTS", "EST AMT LESS C/D", original-vs-present estimate columns, "BILLING TYPE PROGRESSIVE").
- **Budget carve-out narrowed:** A pure planning recap with no billing apparatus (e.g., "OUTDOOR ESTIMATE RECAP" bus-shelter planning) stays budget. Check stubs remain budget even when columns are headed "INVOICE DATE/NO/AMOUNT".
- **Worked examples:** 4th example teaches estimate-change-order → invoice case.

**Rationale:** v10 had routed three agency estimate documents to budget because the invoice bullet was too narrow ("billing document for COMPLETED work...listing ACTUAL billable charges"). v11 restored the broader v9 wording to recover invoice coverage.

---

## v11.5 — Extended Money-Only Records

**Extended clarification for money-only records and periodic customer statements.**

- **Check 7 (invoice):** Added landlord's rent/lease statement for a specific period as invoice (bills one-off service period, not ongoing account).
- **Check 7 (budget):** Clarified campaign-contribution/expenditure requests, contribution-request checklists, grant/contribution requests with recipient and amount as budget (internal money requests). Added campaign-contribution/expenditure statements/disclosures and financial/money-data tables (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures) as budget.
- **Check 10 (form):** Explicitly excluded campaign-contribution requests/checklists/statements and financial or money-data tables from form.

**Rationale:** The model was routing money-only records to form because they had approval blocks or field layouts. v11.5 made explicit that bare money requests (amount + recipient, or financial data tables) are budget, not form.

---

## v11.6 — (Intermediate)

No build script preserved. Likely minor tweaks between v11.5 and v11.7.

---

## v11.7 — Minimal Edit Set D + A + B

**Deliberately minimal 3-edit set (C and E skipped to reduce regression risk).**

- **Edit D (Check 7 voucher vs check-stub):** Voucher is a payment instrument that BILLS a named payee for named goods/services/charges (invoice). Check face/check stub is the DISBURSEMENT instrument (budget), even when stub columns are headed "INVOICE DATE/NO/AMOUNT".
- **Edit A (Check 8 rate-data chart):** A labeled product/parameter rate-data chart (e.g., statistical process-control chart titled with product name plotting measured property against spec limits) is specification even without "shall/must" text.
- **Edit B (Check 10 standalone-chart carve-out):** A standalone labeled chart is form only when it holds generic administrative/log data. A chart of a product's measured parameters against spec limits → specification (check 8). A financial/money chart → budget (check 7). A research-measurement chart → scientific_report (check 13).

**Rationale:** v11 had two 160-set misses: `jow70f00` (form → budget, ambiguous grant payment) and `tqi16e00` (budget → invoice, planning recap with estimate numbers). v11.7 targeted structural disambiguation (voucher vs check-stub) and chart-type routing (product/parameter charts, financial charts) with minimal changes to avoid regressions.

**Result:** 160-set: 156/159 (98.1%). Eval 56-set: 20/56 (35.7%) — best eval yet (v11.5 = 16/56, v11.6 = 17/56).

---

## v11.8 — Fix 1 (Form-vs-Budget Authorization) + Fix 2 (Memo-vs-Letter)

**Two targeted fixes for v11.7's remaining 160-set misses.**

- **Fix 1 (Form-vs-budget authorization):** Budget money-only clause narrowed to bare amount-only requests ONLY. A project-funding authorization/approval form that names the work to be funded, carries finance-data/expense-code fields (e.g., budgeted department/expense code), and has an approval block is form (check 10), not budget — even when it states an amount (e.g., "AUTHORIZATION REQUEST" for $690,000 to perform a named study). Caveat explicitly includes AUTHORIZATION REQUEST / project-funding forms.
- **Fix 2 (Memo-vs-letter):** By-name memo rule requires an explicit INTERNAL TITLE/DIVISION in the address line; do not infer internal vs. external from pronoun usage in the prose. A dated note addressed to a bare name with an honorific (e.g., "Mr. T. E. Sandefur:") — no internal title/division, no TO:/FROM:/RE:/SUBJECT: block, no "Dear ..." salutation, and no closing signature — is a letter (external addressee), not a memo.

**Rationale:** v11.7 had three 160-set misses: `yvp54d00` (form → budget, AUTHORIZATION REQUEST $690,000), `cpt85d00` (letter → memo, "Mr. T. E. Sandefur"), `tqi16e00` (budget → invoice). Fix 1 targets the authorization-request form; Fix 2 targets the bare-name external addressee case.

**Result:** 160-set: 157/158 (99.4%) — best ever. All three v11.7 misses fixed. Eval 56-set: 18/56 (32.1%) — regression vs v11.7's 20/56. Two eval rows recovered (`form__0005`, `spec__0019`), but four regressed (`presentation__0001`, `presentation__0011` → budget; `spec__0017` → form; `jed71e00` → presentation).

---

## v11.9 — Narrow Edit B's Financial-Chart→Budget Carve-Out

**Three edits that narrow Edit B so titled/designed deck charts no longer fall into budget.**

- **Edit 1 (Check 10 carve-out narrowed):** A product/parameter rate-data chart → specification. A research/measurement chart → scientific_report. A financial/money chart → budget ONLY when it is a standalone data table used for money planning or tracking (a ledger, budget-vs-actual, price/value table). A financial chart presented as a TITLED, DESIGNED DECK CHART (a chart page styled as a slide with its own title/caption, company logo/date, or chart-per-page deck look, e.g., a "brand shares" pie chart or "performance triggers" table page) → presentation (check 9), not budget.
- **Edit 2 (Check 9 hardened):** A titled/designed deck chart IS a presentation slide; don't route it to budget. The check-10 carve-out routes money charts to budget only when they are standalone planning/tracking data tables, not when they are titled deck charts.
- **Edit 3 (Calibration):** Keep the deck-chart exception visible next to the general chart rule.

**Rationale:** v11.8's Edit B carve-out ("a financial/money chart is budget") was too broad — it routed titled designed deck charts to budget ahead of check 9. The eval set had two presentation→budget regressions (`presentation__0001`, `presentation__0011`) from v11.7 to v11.8. v11.9 narrows the carve-out to standalone planning/tracking tables only.

**Result:** Eval 56-set: 20/56 (35.7%) — ties v11.7's best, +2 over v11.8's 18/56. Both presentation→budget regressions recovered, plus bonus fix of `jed71e00` (form → presentation, also v11.8's 160-set miss). Cost: `form__0005` (a v11.8 Fix-1 success) regressed to invoice; new `news_article__0008` → memo miss.

---

## v12 — Major Rewrite (Function-Based Invoice vs Budget)

**Complete rewrite of checks 7, 9, 10 with new calibration and worked examples.**

- **Edit A (Check 7 complete rewrite):** DECIDE BY FUNCTION, NOT BY HEADINGS. Invoice: page charges or requests payment for goods SOLD or services PERFORMED. Budget: internal money planning, tracking, or disbursement. Added explicit guidance on purchase orders (invoice when listing line items/quantities/prices/total), vouchers (payment instrument, invoice), hotel/motel bills (invoice), landlord's rent/lease statements (invoice), agency estimates/change orders (invoice when listing actual charges/totals, budget when only projecting future spend), checks/check stubs (budget).
- **Edit B (Check 9 last-sentence rewrite):** A chart-per-page deck exhibit (titled chart, pie chart, flowchart, or data table that is a SINGLE visual on a slide-styled page with descriptive title, corporate branding, footer date/code) IS a slide (presentation), not a form. A dense data-RECORD table (multi-row/multi-column records log, data-capture sheet, chart data table with generic row labels) is form (check 10).
- **Edit C (Check 10 data-table clause):** Covers dense multi-row data-RECORD tables (records logs, data-capture sheets, chart data tables with generic row labels). NOT covered: single-exhibit chart/table on slide-styled page (presentation); titled product-analysis table keyed to product/material (specification).
- **Edit D (Calibration trim):** Updated calibration section with refined rules for form/scientific_report/handwritten/news_article/presentation over/under-prediction.
- **Edit E (Worked examples):** Updated worked examples for agency estimate change order (invoice) vs planning recap (budget).

**Rationale:** v11.5-v11.9 incremental edits had accumulated complexity. v12 rewrites check 7 from scratch with a function-based decision framework (bill vs plan/track/statement), clarifies check 9 for chart-per-page deck exhibits vs dense data-record tables, and streamlines calibration.

---

## v13 — Specialist Periodicals + Scientific Research Records

**Built from v11.9. Extends scientific_publication to specialist periodicals and scientific_report to research records.**

- **Check 6 (Published evidence):** Include a dated, titled science, medical, engineering, or technical periodical page whose own masthead identifies that specialist publication (e.g., a science magazine or medical trade paper), even when it lacks volume/issue/DOI.
- **Check 12 (News article caveat):** Don't use general-news caveat for specialist science, medical, engineering, or technical periodicals. A specialist periodical with its own dated masthead is scientific_publication, not news_article, even if its page uses magazine/news typography or a section title such as "Monitor" or "World Wide Report".
- **Check 10 (Form carve-out):** Generic administrative forms remain form, but a page whose fields, tables, signatures, or handwritten entries document a scientific experiment, laboratory result, compound test, analytical measurement, protocol review, or technical research report → scientific_report (check 13), not form.
- **Check 10 (additional):** It does NOT cover scientific/laboratory research records merely because they use fields, tables, QA sign-offs, or a report cover.

**Rationale:** The model was routing specialist science/medical/technical periodicals (with their own mastheads) to news_article because they used magazine/news typography. It was also routing scientific research records (experiments, lab results, compound tests) to form because they used structured fields/tables. v13 extends scientific_publication to specialist periodicals and scientific_report to research records.

**Result:** v2 160-set: 137/159 (86.2%).

---

## v14 — Production Precedence Rules

**Built from v13. Adds final authority rules for conflicting cues.**

- **Added section:** "v14 production precedence (final authority)" with explicit rules:
  1. **Financial function beats layout:** Invoice for vendor/agency billing specific good/service/job. Budget for internal planning/tracking/recurring statements/checks. Form for single authorization/request with approval fields (even with large dollar amount).
  2. **Generic form is not a technical catch-all:** Form only when primary purpose is administrative data capture/approval and no stronger document function. Page documenting experiment/sample/compound/protocol/measurement/lab result/research study → scientific_report unless clearly product/material documentation.
  3. **Additional precedence rules** (from truncated output): Likely covers other recurring boundary decisions.

**Rationale:** v13 extended scientific_publication and scientific_report, but the model still had edge cases where layout cues (structured fields, approval blocks, dollar amounts) overrode document function. v14 makes the recurring boundary decisions explicit as final authority rules.

**Result:** v2 160-set retry: 136/160 (85.0%).

---

## v15 — Function-First Regression Repair

**Built from the validated v13 base after analyzing the v14 reasoning traces.**

- **Financial boundary:** Requires positive billing evidence for `invoice`; estimate numbers, revisions, agency letterhead, projected periods, and quoted totals alone remain `budget` when the page plans future spend. Purchase orders and authorization requests remain `form` when their function is approval.
- **Letter boundary:** Recognizes recipient-directed prose with a salutation or closing as `letter` without requiring letterhead or a complete street address. Complete handwritten letters remain `letter`; freeform notes and cards remain `handwritten`.
- **Email boundary:** Preserves genuine mail-client evidence requirements so phone-message logs, voicemail records, fax metadata, and generic From/To forms do not become email.
- **Form/questionnaire boundary:** Requires a respondent-facing survey instrument for `questionnaire`; retains `form` for administrative capture and QC sheets.
- **Technical boundary:** Separates normative product requirements (`specification`), filled QC/data-capture sheets (`form`), and study findings/results (`scientific_report`).
- **Presentation/news boundary:** Requires explicit deck or promotional function instead of relying on rotation, scan borders, sparse tables, or isolated mastheads.
- **Output contract:** Requires exactly one parser-safe `<label>...</label>` result.

**Rationale:** v14 fell to 85.0% on `fixed_size_sampled_v2`, with repeated budget/invoice and form-boundary errors. Its final precedence rules over-weighted weak visual or lexical cues and contradicted function-based evidence in the traces.

**Validation assets:** Adds two disjoint 160-image Braintrust slices, `fixed_size_sampled_v3` and `fixed_size_sampled_v4`, sampled primarily from the full Hugging Face `chainyo/rvl-cdip` test split and using the Kaggle test checkout only as a fallback when the Hugging Face source cannot satisfy disjoint quotas.

---

## Summary Table

| Version | Based On | Key Changes | 160-set | 320-set | 480-set | Eval 56 |
|---------|----------|-------------|---------|---------|---------|---------|
| v11 | v10 | Estimate vs bill rule | 156/158 (98.7%) | 266/317 (83.9%) | — | — |
| v11.5 | v11 | Extended money-only records | — | — | — | — |
| v11.6 | v11.5 | (Intermediate) | — | — | — | — |
| v11.7 | v11.6 | Edit D+A/B (voucher/check-stub, rate-data chart, standalone-chart) | 156/159 (98.1%) | — | — | 20/56 (35.7%) |
| v11.8 | v11.7 | Fix 1 (authorization form) + Fix 2 (memo vs letter) | 157/158 (99.4%) | 279/320 (87.2%) | 424/476 (89.1%) | 18/56 (32.1%) |
| v11.9 | v11.8 | Narrow Edit B (titled deck charts → presentation) | — | — | — | 20/56 (35.7%) |
| v12 | v11.6 | Major rewrite (function-based invoice/budget, chart-per-page deck) | — | — | — | — |
| v13 | v11.9 | Specialist periodicals + scientific research records | 137/159 (86.2%) [v2] | — | — | — |
| v14 | v13 | Production precedence rules | 136/160 (85.0%) [v2 retry] | — | — | — |

---

## Best Results by Dataset

| Dataset | Best Version | Accuracy |
|---------|--------------|----------|
| 160-image (original) | v11.8 | 157/158 (99.4%) |
| 320-image | v11.8 | 279/320 (87.2%) |
| 480-image | v11.8 | 424/476 (89.1%) |
| Eval 56 | v11.7 / v11.9 | 20/56 (35.7%) |
| 160-image v2 | v11.9 | 137/159 (86.2%) |

**Note:** v11.8 generalizes best to larger, noisier datasets (320, 480). v11.7 and v11.9 tie on the eval 56-set. v13 and v14 target specialist periodicals and scientific research records but show lower accuracy on the v2 dataset.

---

## v16 — v11.9 + Two Worked Examples (Estimate→Invoice, Handwritten→Letter)

**Appended two worked examples to the v11.9 prompt to target the top confusion pairs from prior evaluations.**

- **Worked example 1:** Estimate vs Invoice — a "DATABASE MARKETING ESTIMATE" with PREVIOUS/CURRENT ESTIMATE columns showing planned agency spending is budget, not invoice (no payment demand).
- **Worked example 2:** Handwritten letter vs handwritten note — a complete handwritten letter with salutation, prose body, and closing remains letter, not handwritten.
- **Prompt length:** 51,753 chars (v11.9 = 50,254).

**Result (multispect on 3 slices):**
| Slice | Accuracy | Failure rate |
|-------|----------|-------------|
| v1 (test_images) | 154/160 (96.2%) | 1 failed row |
| v2 (HF mirror) | 134/160 (83.8%) | 6 failed rows |
| v3 (HF mirror) | 127/160 (79.4%) | 9 failed rows |

**Findings:** Worked examples did not prevent the top confusions (handwritten→letter = 10, budget→invoice = 7 across slices). 16 total failed rows (13 finish_reason=length, 3 provider errors). v2/v3 HF-mirror source is ~15pp harder than v1 test_images source, independent of prompt version.

---

## v17 — Simplified Financial Rules + Handwritten → Letter Override

**Data-driven rebuild of the v11.9 check-7 (financial) rules, eliminating the agency-estimate sub-protocol that caused v11.9–v16's budget→invoice errors. Adds explicit LETTER/MEMO OVERRIDE in check-2 (handwritten) to enforce ordered-checklist precedence.**

Driven by three root causes identified in the v16 multispect evaluation (`reports/v16_multislice_evaluation_report.md`):

1. **Provider failures (16 rows / 3.3%)** — 13 finish_reason=length (qwen3.7-flash exhausts reasoning tokens on the bloated check-7 section) → **Fix:** Trim check-7 from 6,284 chars to ~1,100 chars (simplified invoice=payment-demand, budget=planning, estimate=budget). Reduced reasoning effort to `medium`. Raised MAX_TOKENS_CAP to 32,768. Added 300s HTTP timeout.

2. **Slice source quality gap (~15pp)** — v2/v3 (HF mirror) images are inherently harder than v1 (test_images) → **Mitigation:** Stronger rules should be more robust across sources.

3. **Prompt regression from v11.8's 99.4%** — the agency-estimate sub-protocol caused the model to misclassify budgets (planning estimates) as invoices when "PREVIOUS/CURRENT ESTIMATE" revision columns were present. → **Fix:** Removed the entire agency-estimate sub-protocol. The rule is now simple: "A document titled ESTIMATE is budget — it PLANS spending. Only an explicit payment demand (Amount Due, Pay, Invoice header) makes it invoice."

**Key changes from v11.9/v16:**
- **Check-7 (invoice):** Replaced 2,450-char agency-estimate maze with a 250-char clean rule: payment demand = invoice.
- **Check-7 (budget):** Replaced 3,030-char budget section (including the planning-recap vs agency-bill sub-protocol) with a 700-char clean rule: estimate = budget.
- **Check-2 (handwritten):** Added "LETTER/MEMO OVERRIDE" bullet: if most of the page is handwritten, it IS handwritten — even with complete letter structure (salutation, body, closing) or memo layout (To/From/Re/Date headers). Check 2 fires before check 11; do not evaluate letter/memo for handwritten pages.
- **Prompt length:** 46,277 chars — 3,977 shorter than v11.9, 5,476 shorter than v16.

**Infrastructure:**
- Reasoning effort reduced to `medium` for qwen models (was `high`).
- MAX_TOKENS_CAP raised to 32,768 (was 16,384).
- Failed rows now return ERROR: sentinel output and are scored as a tracked `failed` metric in Braintrust.
- HTTP timeout (300s) on OpenAI client.
- All eval runs now use `--manifest` for resumability.

---

## Cross-model v11.8 Validation Runs (Aug 2026)

The v11.8 prompt was evaluated across additional OpenRouter models on the original 160-image
`fixed_size_sampled` slice, with each model running at its maximum reasoning effort. Temperature
was varied per run (0.1 default, 0.3 for the qwen3.7-flash re-run, 0.2 for gemini-2.5-flash-lite).

| Model | Reasoning effort | Temp | 160-set Accuracy |
|-------|------------------|-----:|------------------|
| qwen3.7-flash (temp 0.1 baseline) | high | 0.1 | 157/158 (99.4%) |
| qwen3.7-flash (temp 0.3) | high | 0.3 | 157/159 (98.7%) |
| qwen3.5-35b-a3b | high | 0.1 | 155/157 (98.7%) |
| kimi-k2.6 | xhigh | 0.1 | aborted mid-run (network outage) |
| gemini-2.5-flash-lite | max | 0.2 | 139/160 (86.9%) |

**Findings so far:**

- qwen3.7-flash at temp 0.3 holds 98.7% but regresses `tqi16e00` (budget → invoice) that was
  fixed at temp 0.1; `jed71e00` (form → presentation) remains the recurring miss across models.
- qwen3.5-35b-a3b matches the qwen3.7-flash accuracy (98.7%) on the 160-set but needs a larger
  max_tokens budget — long reasoning traces capped several rows even after doubling to 16k.
- gemini-2.5-flash-lite at max reasoning scores 86.9% with zero failed rows; it uniquely
  resolves `jed71e00` but over-uses `specification` (memo/form/handwritten/letter pull) and
  still confuses `scientific_publication → scientific_report` and `budget → invoice`.
- On the deliberately hard `qwen_v12_retroactive_eval` slice (52 rows, all v12 misses),
  qwen3.5-35b-a3b scores 30.8% (16/52); expected given the slice only contains known hard cases.
- kimi-k2.6 run aborted ~109/160 due to a transient DNS outage against `api.braintrust.dev`
  that crashed the Braintrust logging thread; the partial experiment is not comparable.

The temperature and reasoning-effort flags added to `braintrust_openrouter_input.py` record both
settings in Braintrust experiment metadata for reproducibility.

---

## v17.1 — Surgical Calibration + Counter-Examples (Aug 2026)

**Data-driven corrections from v16 v2+v3 multi-slice failure analysis (320 images, 81.6% accuracy).**

- **Worked example — handwritten letter → handwritten.** v16's worked example #2 taught the model that "a complete handwritten letter remains letter." This caused 7/44 misclassifications across both slices (35% of the handwritten class). The new worked example applies the LETTER/MEMO OVERRIDE: handwriting wins regardless of letter formatting.
- **Worked example — agency estimate → budget.** v16's worked example #1 failed to prevent budget→invoice confusion (6/44 misclassifications). The new worked example reinforces the simplified check-7 rule: no payment demand = budget.
- **Calibration — scientific_report vs specification.** 2 scientific_report→specification errors and a budget→scientific_report outlier traced to the model misreading technical data tables as product specs. New sentence: "A research study's own experimental data tables belong to scientific_report, not specification — specification requires the page's PRIMARY function to be defining a product's composition."
- **Calibration — news_article vs advertisement.** 3 news_article→advertisement errors where the model fixated on embedded ad imagery. New sentence: "Judge newspaper/magazine pages by editorial intent, not embedded ads — a page with masthead, columns, and bylines is news_article even when it CONTAINS a branded advertisement."

**Token profile:** +2,177 chars (+4.7%). v17.1 total: 48,462 chars vs v16: 51,753 chars. Still significantly lighter than v16 while carrying 2 more worked examples (6 total vs v16's 6, but v16's were actively harmful).

---

## v18 — Monte Carlo Exemplar Appendix (Aug 2026, EXPERIMENTAL)

**Data-driven worked examples mined by `monte_carlo_exemplars.py` from the joint
corpus (4,641 rows / 1,512 images). Four correct traces whose runner-up named
the decoy label for four of the top confusion pairs.**

- **letter vs memo (letter):** OGILVY & MATHER letterhead, external address,
  "Dear John:" salutation, "Yours truly," closing → letter, not memo. Targets
  the #1 confusion pair (letter→memo: 53 corpus errors).
- **MSDS (specification, not form):** "MATERIAL SAFETY DATA SHEET" with
  INGREDIENTS / PHYSICAL DATA / FIRE AND EXPLOSION HAZARD DATA sections → check 8
  precedes check 10. Targets specification→form (41 errors).
- **PHS 398 biographical sketch (resume, not form):** check 5 explicitly covers
  PHS 398 templates — biographical content decides, not the form-page label.
  Targets resume→form (21 errors).
- **Survey instrument (questionnaire, not form):** YES/NO + open-response
  questions → check 4 precedes check 10. Targets questionnaire→form (16 errors).

**Rationale:** The Monte Carlo near-miss analysis found 27.7% of current-line
misses have the correct label as the stated runner-up — the model overrides its
own best evidence. These four exemplars teach the runner-up-vs-final decision on
the highest-frequency pairs. Selected pairs cover 131 of 767 corpus errors (17%).

**Status:** EXPERIMENTAL — NOT the default (default remains v17.2). **Verified
on the exemplar slice (48 images): v18 scored 64.6% vs v17.2's 68.8% (−4.2pp) —
the exemplar appendix did NOT improve accuracy and slightly hurt.** The
measurement shows that adding more worked-example text does not fix the
runner-up-vs-final decision; the follow-up should be a decision-rule change
(e.g. "never override your own stated runner-up without new evidence"), not more
exemplar verbosity. v18 is retained for reference but should not be promoted.

**Token profile:** +1,714 chars vs v17.2 (50,678 → 52,392 chars; +3.4%).

---

## v17.2 — Three-Slice Generalization (Aug 2026)

**Data-driven corrections from v17.1 v1+v2+v3 combined analysis (480 images, 53 failures, ~89% accuracy).**

v17.1 successfully eliminated handwritten→letter (0 misses across all 3 slices) and length errors (4 vs v16's 15). Five clusters survived the v17.1 fix:

- **invoice→budget (6) + budget→invoice (3) + invoice→form (4):** 13 financial document failures in 480 images. The simplified check-7 reduced v16's 20 financial failures but the form-override rule ("money function overrides form layout") wasn't consistently applied when invoices had form-like layouts.
- **news_article→advertisement (3):** The v17.1 calibration sentence wasn't sufficient — the model still fixated on embedded ad imagery within newspaper pages.
- **Form over-prediction (8 instances of form as predicted class):** invoice→form (4), budget→form (2), specification→form (2), scientific_report→form (2), advertisement→form (1). The model defaulted to form when unsure.
- **scientific_publication→scientific_report (3):** Journal reprint boundary still fuzzy.
- **Presentation confusion (4):** presentation→memo (2), →handwritten (1), →budget (1) — the model read slide-style layouts as prose memos.

**Changes:**
- **Calibration — form-is-never-a-default.** "If you are choosing form because no other check clearly matched, you have missed a check — go back through checks 1-14." Addresses the 8 form-overprediction instances.
- **Calibration — presentation vs memo.** "A presentation with slide-style layout is presentation, not memo — memo requires internal organizational context and prose body, not slide typography." Addresses the 2 presentation→memo cases.
- **Worked example — invoice with form layout → invoice.** Shows a vendor bill with labeled fields, amount boxes, and approval blocks being classified as invoice because "money function overrides form layout." Addresses the 4 invoice→form cases.
- **Worked example — newspaper page with embedded ad → news_article.** Shows a newspaper page with masthead, columns, bylines, and an embedded brand ad being classified as news_article because "the page's dominant function is newspaper editorial content." Addresses the 3 news→ad cases.

**Token profile:** +2,216 chars (+4.6% vs v17.1). v17.2 total: 50,678 chars. 8 worked examples total. Still 1,075 chars lighter than v16.

---

## v0 — Function-Not-Subject Baseline (Aug 2026)

**Minimal baseline prompt (915 chars) with no check structure — added to benchmark the value of the check-driven iterations (v11+).**

- **Content:** Only the "judge by FUNCTION, not subject matter" preamble (commit to the first check with concrete on-page evidence; later checks don't override) plus the 16 exact label strings. No checks, no worked examples, no calibration sentences.
- **Purpose:** Isolated control to measure how much of the v17.x accuracy comes from prompt engineering vs. the model's prior knowledge of document types.

**Result:** `fixed_size_sampled_480` slice (30/class × 16 = 480), `qwen/qwen3.7-flash`, reasoning high, max_tokens 8192: **332/480 (69.2%)**, 0 failed rows. Memo 100%; advertisement/email/scientific_publication 93%; file_folder/news_article 80%; form 73%; letter 70%; resume/scientific_report 60%; invoice/questionnaire/specification 57%; handwritten 53%; budget 43%; presentation 37%.
