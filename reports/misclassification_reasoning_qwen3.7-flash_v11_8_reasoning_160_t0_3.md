# Misclassification Reasoning — qwen3.7-flash_v11_8_reasoning_160_t0_3

**Overall Accuracy:** 98.7% (157/159)  
**Total Errors:** 2  
**Unique Confused Pairs:** 2

---

## form → presentation (1 errors)

### `test_imagesj_j_e_d_jed71e00_03701993_03702011.tif.png`
**Expected:** `form` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** None visible.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a Bates number "03701993" on the right side.
> **2. Scratchpad procedure:**
> *   **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
    *   Evidence: There is a large black rectangular area (looks like a photographed slide or a dark document). On the left, there is a strip of paper with text "CHART 1", "A", "B", "C", and a column of numbers. At the bottom right, there is a Bates number "03701993".
    *   Wait, let's look closer. The main content is a large dark rectangle (looks like a slide or a dark page) and a strip of paper on the left with "CHART 1", letters A, B, C, and a column of numbers.
    *   Is this a folder tab? No, it looks like a slide or a chart.
    *   Is it an identifier-only page? No, there is "CHART 1", data, and a large dark area.
    *   Wait, look at the layout. It looks like a photograph of a slide or a chart. The large black area is likely a photographic slide or a dark background.
    *   Let's check Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation.
    *   "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation". Here we have a large black block.
    *   Wait, let's look at the left strip. "CHART 1", "A", "B", "C", numbers. "CH..." "USE" "MADE".
    *   This looks like a chart or a data table.
    *   Let's re-evaluate Check 1. "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix...". This page has a table/chart ("CHART 1") and a large image (black block). So not file_folder.
> *   **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
    *   Evidence: The text looks typed (monospaced font for the numbers). The black area is a photo/slide. Not majority handwritten.
> *   **Check 3: FAX TRANSMISSION SHEET -> form**
    *   Evidence: No fax header.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No survey questions.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal header.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: The numbers look like data (1.37, 1.23, etc.), not currency. "CHART 1". Not financial.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: "CHART 1", data. Could be a product rate data chart? "WINSTON KS RATE DATA" is an example. Here we have "CHART 1", "A", "B", "C". The text at the bottom says "CH...", "USE", "MADE". It looks like a statistical process control chart or similar.
    *   Wait, let's look at the black area. It's a large dark rectangle. This is typical of a photographed slide or transparency.
    *   Check 9: "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
    *   Actually, the black area takes up most of the right side. The left side has a strip of paper. This looks like a photograph of a slide mount or a slide itself.
    *   "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder".
    *   "A large heading rotated 90 degrees... is a section divider... but a rotated SHORT FILING LABEL... is file_folder".
    *   Here, the text "CHART 1" is vertical? No, "CHART 1" is horizontal at the top left of the strip. The strip is vertical. The text "A", "B", "C" is vertical. The numbers are vertical.
    *   Wait, the text "03701993" is vertical on the right.
    *   The strip on the left has "CHART 1" at the top, then "A", "B", "C" going down. The numbers are in a column.
    *   This looks like a chart printed on a strip, next to a dark slide.
    *   Let's look at Check 9 again: "Slide/overhead layouts... a photographic slide image (including a blurred or low-quality photo of a slide, chart, or scene)."
    *   The large black area is likely a photographed slide (maybe a chart slide that is dark or just a black slide).
    *   The text "CHART 1" and the data strip look like the content of a slide or a chart associated with a presentation.
    *   Actually, let's look at the layout. It looks like a scan of a slide film strip or a transparency. The black area is the slide mount or the slide itself (which is dark). The strip on the left is the label or the data.
    *   Wait, is this a "standalone chart or table of values alone"?
    *   Check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
    *   BUT, "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
    *   Here we have a large black block (taking up ~70% of the page). The text is on a strip on the left.
    *   This looks exactly like a photographed slide/transparency. The black area is the slide background or the mount. The text is the content.
    *   Let's check the text content: "CHART 1", "A", "B", "C", numbers. "CH...", "USE", "MADE".
    *   This looks like a chart from a presentation.
    *   Let's consider Check 10: ADMINISTRATIVE FORM. "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... is a form only when it holds generic administrative/log data".
    *   If it's a product rate data chart, it's specification (Check 8). "A labeled product/parameter rate-data chart... is a specification".
    *   If it's a generic chart, it's a form.
    *   BUT, the layout is a photographed slide. "Scan-artifact signal... points to a photographed slide/overhead — presentation".
    *   The large black area is the key. It looks like a slide.
    *   Let's look at the text "03701993". It's a Bates number.
    *   The text "CHART 1" is visible.
    *   The text "A", "B", "C" is visible.
    *   The numbers are visible.
    *   This is a chart. Is it a presentation slide?
    *   "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." -> This is a crucial rule.
    *   "Scan-artifact signal... points to a photographed slide/overhead — presentation — even if the sparse text sounds like a research title; don't let a technical-sounding phrase pull this toward scientific_report when the layout itself is sparse and slide-like rather than a prose page. BUT this signal applies only to a photographic image (people, a scene, a slide, a chart-photo) or a designed deck page — it does NOT apply to a photographed file-folder TAB".
    *   So if it's a "chart-photo" (a photo of a chart), it's presentation.
    *   The image shows a large black rectangle (likely a slide or a dark chart) and a strip of data. This looks like a photograph of a slide or a transparency.
    *   The text is sparse. "CHART 1", "A", "B", "C", numbers.
    *   This fits "photographic slide image (including a blurred or low-quality photo of a slide, chart, or scene)".
    *   Therefore, Check 9 (presentation) seems likely.
> Let's re-read Check 9 carefully.
"Slide/overhead layouts... a photographic slide image (including a blurred or low-quality photo of a slide, chart, or scene)."
"Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
Here, the black area is huge, not just a bar. But it looks like a slide mount.
The text "CHART 1" and the data are on a strip.
This looks like a scan of a slide film or a transparency with a label.
Actually, looking closely at the left strip: "CHART 1", "A", "B", "C". The numbers are in a column. At the bottom "11...".
This looks like a data strip from a chart.
The large black area is the chart itself? Or a black slide?
If it's a chart, and it's a "chart-photo" (photo of a chart), it's presentation.
If it's a standalone chart, it's form (Check 10).
The rule says: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
BUT: "Scan-artifact signal... points to a photographed slide/overhead — presentation... it does NOT apply to a photographed file-folder TAB".
Is this a file folder tab? No.
Is this a photographed slide? The large black block looks like a slide. The text is sparse.
The text "03701993" is a Bates number.
The text "CHART 1" suggests it's a chart.
If it's a chart that is photographed (a slide), it's presentation.
"A photographic slide image (including a blurred or low-quality photo of a slide, chart, or scene)." -> This explicitly includes a photo of a chart.
So if this is a photo of a chart (which it looks like, given the black background and the strip of data), it is presentation.
> Let's check Check 8: Specification.
"A labeled product/parameter rate-data chart — e.g. a statistical process-control chart titled with the product name... plotting a measured property over time/subgroup against spec limits... is a specification".
Here we have "CHART 1", "A", "B", "C". No product name like "WINSTON KS". Just "CHART 1".
So it's not clearly a specification chart.
> Let's check Check 10: Form.
"A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data".
If this is a generic chart, it's a form.
BUT, the layout is a photographed slide (black area + sparse text).
The rule for Check 9 says: "Scan-artifact signal... points to a photographed slide/overhead — presentation... even if the sparse text sounds like a research title... don't let a technical-sounding phrase pull this toward scientific_report".
And "A photographic slide image (including a blurred or low-quality photo of a slide, chart, or scene)."
So a photo of a chart is presentation.
The image is clearly a low-quality scan of a slide/transparency (black background, strip of data, Bates number on the side).
This is a "photographic slide image".
So Check 9 (presentation) is the winner.
> Let's double check Check 1: file_folder.
"A page is NOT file_folder if it carries any real content — a photograph or slide image...". This carries a slide image. So not file_folder.
> Let's double check the "folder tab" exception.
"Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number... The black bar is the photographed folder body/tab edge".
Here, the black area is a large rectangle, not a bar. And the text is "CHART 1", not a folder label like "NEWTROL" or "Litigation Content".
So it's not a folder tab.
> Conclusion: It's a photographed slide (presentation). The content is a chart ("CHART 1"), but the format is a slide/overhead (black background, sparse text, scan artifact).
Wait, "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
This is a contradiction.
Let's read carefully:
"Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation — even if the sparse text sounds like a research title... BUT this signal applies only to a photographic image (people, a scene, a slide, a chart-photo) or a designed deck page — it does NOT apply to a photographed file-folder TAB".
And: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> So, if it's a "chart-photo" (photo of a chart), it's presentation.
If it's a "standalone chart" (digital scan of a chart), it's form.
This image looks like a photo of a slide/transparency. The black area is the slide. The text is the content.
The text is "CHART 1", "A", "B", "C", numbers.
This is a "chart-photo".
So it should be presentation.
> Let's look at the text again.
"CHART 1"
"A"
"B"
"C"
Numbers: 1.37, 1.23, 1.25...
"CH..." (maybe "CHART" cut off?)
"USE"
"MADE"
This looks like a data strip from a chart.
The large black area is the rest of the slide.
This is a photographed slide.
Label: presentation.
> Wait, is there any other possibility?
Check 13: scientific_report. "Requires running prose". No prose here.
Check 8: specification. "A labeled product/parameter rate-data chart... is a specification".
If this is a product rate data chart, it could be specification.
But the title is just "CHART 1". No product name.
And the layout is a slide.
Check 9 says: "Scan-artifact signal... points to a photographed slide/overhead — presentation".
The black area is the slide.
So presentation.
> Let's reconsider the "standalone chart" rule.
"A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
This implies that if I see a chart, I should classify it as form, UNLESS it's a "chart-photo" (photographed slide).
How to tell?
The image has a large black block. This is typical of a slide scan (the black is the slide mount or the dark slide).
The text is on a strip.
This is a "photographic slide image".
So presentation.
> Let's look at the Bates number "03701993".
It's on the right edge, vertical.
This is typical of scanned slides/transparencies in this archive.
> Final decision: presentation.
Evidence: Large black area (photographed slide/overhead artifact), sparse text "CHART 1", "A", "B", "C", numbers. Layout matches "photographic slide image" or "scan-artifact signal" for presentation.
> Wait, let's look at the text "CHART 1".
If it's a form, it's a "standalone labeled data chart".
But the layout is a slide.
Check 9: "Slide/overhead layouts... a photographic slide image (including a blurred or low-quality photo of a slide, chart, or scene)."
This is a photo of a chart. So presentation.
> One more check: Check 1 file_folder.
"A page is NOT file_folder if it carries any real content — a photograph or slide image...".
This carries a slide image. So not file_folder.
> So, presentation.
> Wait, is it a "section divider"?
"A near-blank cover or title page... a single-word/short-phrase heading... is a presentation".
Here we have "CHART 1" and data.
It's a chart slide.
So presentation.
> Let's refine the scratchpad.
- file_folder: no — page has real content (chart data, large image), not just ID/stamp.
- handwritten: no — typed text/numbers.
- form: "CHART 1" with data looks like a form/chart, but the layout is a photographed slide (large black area, sparse text, scan artifact). Check 9 overrides for chart-photos.
- presentation: yes — large black block (scan artifact for slide/transparency), sparse text "CHART 1", "A", "B", "C", numbers. Matches "photographic slide image (including... photo of a slide, chart, or scene)" and "scan-artifact signal".
- scientific_report: no — no running prose.
- specification: "CHART 1" is generic, no product name, no "shall/must". Even if it were a spec chart, the slide format makes it presentation? No, Check 8 says "A labeled product/parameter rate-data chart... is a specification". But Check 9 says "photographic slide image... is presentation". Which wins?
Check order: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14.
Check 8 is before Check 9.
If Check 8 matches, we stop.
Check 8: "A labeled product/parameter rate-data chart — e.g. a statistical process-control chart titled with the product name... is a specification".
Here, title is "CHART 1". No product name. "A, B, C".
Is it a product chart? "CHART 1" is generic.
So Check 8 likely doesn't match strongly. "You don't need a code... just clear evidence the table's subject is a product's own composition". Here, no evidence of product subject. Just "CHART 1".
So Check 8 is "not this check".
> Check 9: presentation.
Evidence: Large black area (slide artifact), sparse text "CHART 1", data strip. "photographic slide image (including... photo of a slide, chart, or scene)".
Matches.
> So presentation.
> One detail: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
This rule is in Check 9's text.
"A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
This means if it's JUST a chart (digital), it's form.
But if it's a "photographic slide image" (photo of a chart), it's presentation.
The image is clearly a photo/scan of a physical slide (black background, Bates number on side, strip of paper).
So it's a photo of a chart -> presentation.
> Final label: presentation.

---

## budget → invoice (1 errors)

### `test_imagest_t_q_i_tqi16e00_2040855570.tif.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING". This is a company letterhead/header, not a newspaper/magazine masthead or journal running head.
> **Check 1: file_folder**
- Evidence: The page has a table with "PRODUCT", "PERIOD", "GROSS AMOUNT", "GROSS CHANGE", "TOTALS BY PRODUCT/MONTH". It has real content, not just an identifier/stamp.
- Not this check.
> **Check 2: handwritten**
- Evidence: Typed throughout. No majority handwriting.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: Not a survey instrument.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: Not a resume.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name/volume/issue/page number on the page itself.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: "LEO BURNETT U.S.A. ... OUTDOOR ESTIMATE RECAP - ODO1(S)". "EST NO: 4155". "CLIENT: P.M. INC.". "DESC: 774A ODP B&H BUS SHELTERS". Table with "PRODUCT", "PERIOD", "GROSS AMOUNT", "GROSS CHANGE", "TOTAL". Total is 330,550.00.
- Let's look at the invoice vs budget rules for check 7.
- "invoice: ... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
- This page has "EST NO: 4155". It has "GROSS AMOUNT" and "GROSS CHANGE" columns. It is an "ESTIMATE RECAP".
- Wait, let's read the budget bullet: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- This page has "EST NO: 4155". It has "GROSS AMOUNT" and "GROSS CHANGE". It lists amounts for JUN 1994, SEP, OCT, DEC 1994. The period is "01/01/94 TO 12/31/94". Date is "05/06/94".
- Wait, the invoice bullet says: "when it names an estimate number ("EST NO")... the word 'estimate' in the title does NOT make it budget."
- This page has "EST NO: 4155". So it is an invoice.
- Let's re-read carefully: "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
- "an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- This page has "EST NO: 4155", "GROSS AMOUNT", "GROSS CHANGE", "TOTAL 330,550.00". It is an estimate recap for a client job (P.M. INC., 774A ODP B&H BUS SHELTERS). Thus, it is an invoice.
> Let's double check.
"OUTDOOR ESTIMATE RECAP - ODO1(S)"
"EST NO: 4155"
"CLIENT: P.M. INC."
"DESC: 774A ODP B&H BUS SHELTERS"
Table:
PRODUCT: 12- B&H 85'S
PERIOD: JUN 1994 QUARTER 2, SEP QUARTER 3, OCT, DEC QUARTER 4
GROSS AMOUNT: 90,250.00, 90,250.00, 90,250.00, 59,800.00, 150,050.00, TOTAL 330,550.00
GROSS CHANGE: 90,250.00, 90,250.00, 90,250.00, 90,250.00, 59,800.00, 150,050.00, TOTAL 330,550.00
> This matches the invoice bullet: "names an estimate number ("EST NO")... lists charges and totals for a client job is the agency's bill (invoice)."
> Runner-up: budget. Ruled out because the document names an estimate number ("EST NO: 4155") and lists charges/totals for a client job, making it an invoice (agency bill) rather than a pure planning recap.
> Let's check check 10 just in case.
"administrative form -> form"
But check 7 says: "Money function overrides form layout... A payment VOUCHER... is invoice... An agency estimate/recap/change order... is invoice".
So check 7 wins over check 10.
> Final label: invoice.

---