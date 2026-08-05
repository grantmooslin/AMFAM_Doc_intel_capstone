# Misclassification Reasoning — qwen3.7-flash_v11_reasoning_160

**Overall Accuracy:** 98.7% (156/158)  
**Total Errors:** 2  
**Unique Confused Pairs:** 2

---

## invoice → budget (1 errors)

### `test_imagesj_j_o_w_jow70f00_0011930077.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is a "VOUCHER" header.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a header "VOUCHER" and "BROWN & WILL FARSON TOBACCO CORPORATION".
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a lot of content: a voucher form with fields, dates, amounts, descriptions. It's not just an ID or stamp.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: There is some handwriting ("November 1984", maybe a signature), but the majority is a printed form with typed/printed entries (vendor info, description, amounts).
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
    *   Evidence: No survey questions.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY**
    *   Evidence: No CV/resume content.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE**
    *   Evidence: No journal name, volume, issue, page range.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: The page is titled "VOUCHER". It lists "VENDOR NO. 18119", "The Franklin Institute", "Benjamin Franklin Parkway, Philadelphia, PA 19108".
    *   Item Description: "Final contribution for grant to above institute for basic research".
    *   Item Amount: "$278,000.00".
    *   Pay this amount: "$278,000.00".
    *   Account Name: "Gen, Corp, Contributions- Medical- Other".
    *   This is a payment voucher / check stub / payment request.
    *   Let's look at the definitions in Check 7.
    *   "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..." -> Wait, "payment voucher" is listed under invoice? Let's re-read carefully.
    *   "invoice: an outside vendor, supplier, or agency states charges owed... a payment voucher, a vendor's price... a receipt, a payment request..."
    *   "budget: ... a check face or check stub, a check/payment register... ALSO a provider's periodic customer statement... money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
    *   Wait, let's look closer. "A check face/check stub stays budget even when the detachable stub's columns are headed 'INVOICE DATE'/'INVOICE NO.'/'INVOICE AMOUNT' — a check and its stub record a disbursement from a payment instrument, not a vendor bill for goods or services."
    *   This document is a "VOUCHER" from "BROWN & WILL FARSON TOBACCO CORPORATION".
    *   It says "Final contribution for grant to above institute for basic research". Amount $278,000.00.
    *   It has fields for "MAIL CHECK TO ADDRESS SHOWN", "MAIL CHECK WITH ATTACHMENTS", "PAY THIS AMOUNT".
    *   It has account coding: "Gen, Corp, Contributions- Medical- Other", "665 08-4694".
    *   This looks like an internal payment authorization or a check stub/voucher for a disbursement.
    *   Let's check the definition of "budget" again: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register... ALSO a provider's periodic customer statement... money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
    *   This is a voucher for a contribution/grant. It records a disbursement ($278,000).
    *   Is it an invoice? "an outside vendor... states charges owed". The Franklin Institute is receiving a contribution/grant, not selling goods/services in a typical invoice sense, although it says "Final contribution for grant". It's a payment of a grant.
    *   The document is a "VOUCHER" used internally to authorize payment (Brown & Will Farson Tobacco Corporation). It looks like a check payment voucher or a disbursement record.
    *   "a check face or check stub... is budget".
    *   "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
    *   This document authorizes payment of $278,000 to The Franklin Institute. It has account codes. It looks like an internal financial document tracking disbursement.
    *   Let's look at "invoice" definition again: "a payment voucher... is an invoice". Wait. "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
    *   This is confusing. Let's re-read carefully.
    *   "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
    *   Wait, is a "payment voucher" always an invoice? "a payment voucher" is listed under invoice examples. BUT, "a check face or check stub stays budget".
    *   Let's look at the content. "Final contribution for grant to above institute for basic research". This is a grant payment.
    *   The header says "VOUCHER BROWN & WILL FARSON TOBACCO CORPORATION".
    *   This is an internal voucher to pay a vendor (The Franklin Institute).
    *   Usually, a voucher is an internal document authorizing payment.
    *   Let's look at the "budget" definition: "budget: internal money planning, tracking, or disbursement... a check face or check stub... money-only records: a contribution/expenditure request or approval form whose whole content is an amount".
    *   This document is a contribution/expenditure request/approval form. It has the amount ($278,000). It has account codes. It is for a "contribution for grant".
    *   The "invoice" definition says "an outside vendor... states charges owed". The Franklin Institute is the vendor/payee here, but this document is *from* Brown & Will Farson (the payer). The text "REMITTANCE ADVICE INFO. (15 CHAIR ONLY)" suggests this is the remittance advice or the voucher copy kept by the payer.
    *   Actually, "VOUCHER" usually implies an internal accounting document.
    *   Let's look at the "budget" bullet: "money-only records: a contribution/expenditure request or approval form whose whole content is an amount... is budget". This fits perfectly. It's a form requesting/approving a contribution of $278,000.
    *   Also, "a check face or check stub stays budget". This looks like a check stub or payment voucher.
    *   Let's check "form" (Check 10). "internal authorization/approval forms with an approval signature/date block". This has "PAY THIS AMOUNT", account codes. But Check 7 says "Money function overrides form layout". So if it's financial, it's invoice or budget.
    *   Is it invoice or budget?
    *   Invoice: "outside vendor... states charges owed". Here, the payer (Brown & Will Farson) is recording a payment to a grantee (Franklin Institute). It's not a bill for goods sold. It's a grant contribution.
    *   Budget: "internal money planning, tracking, or disbursement... a check face or check stub... contribution/expenditure request or approval form whose whole content is an amount".
    *   This is a disbursement record / contribution approval. So it's **budget**.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK...**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM**
    *   Evidence: It is a form (voucher), but Check 7 (Financial) overrides it because it's a money document (contribution/grant payment). "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
    *   Result: not this check (because Check 7 applies).
> *   **Check 11: CORRESPONDENCE**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 12: PUBLISHED JOURNALISM**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 14: PROMOTIONAL MATERIAL**
    *   Evidence: No.
    *   Result: not this check.
> **Re-evaluating Check 7 (Invoice vs Budget):**
- The document is a "VOUCHER".
- Vendor: The Franklin Institute.
- Description: "Final contribution for grant to above institute for basic research".
- Amount: $278,000.00.
- Account: "Gen, Corp, Contributions- Medical- Other".
- This is a payment of a grant.
- Definition of **invoice**: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD". A grant contribution is not charges for goods/services sold. It's a contribution.
- Definition of **budget**: "internal money planning, tracking, or disbursement... a check face or check stub... money-only records: a contribution/expenditure request or approval form whose whole content is an amount".
- This fits "contribution/expenditure request or approval form whose whole content is an amount" or "check face or check stub" (it's a voucher for payment).
- Therefore, **budget**.
> Wait, let's look at the "invoice" definition again. "a payment voucher... is an invoice".
"invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
This is tricky. "Payment voucher" is listed under invoice.
BUT, "a check face or check stub stays budget".
And "money-only records: a contribution/expenditure request or approval form whose whole content is an amount... is budget".
This document is a voucher for a contribution.
The text says "Final contribution for grant...".
The account is "Contributions- Medical- Other".
This is an internal accounting document (voucher) for a disbursement (grant payment).
Internal disbursement tracking is budget.
The "payment voucher" in the invoice list likely refers to a vendor's payment voucher (a bill they send you to pay), or maybe a generic term. But the specific bullet "money-only records: a contribution/expenditure request or approval form whose whole content is an amount... is budget" seems to cover this.
Also, the document is from "BROWN & WILL FARSON TOBACCO CORPORATION" (the payer), not the vendor. It's an internal voucher to authorize payment. "REMITTANCE ADVICE INFO...".
So it's an internal financial record. Internal financial records are budget.
> Let's check if there's any other label.
It's a form with fields. Check 10 says "internal authorization/approval forms... is a form". BUT Check 7 says "Money function overrides form layout... money-only forms are budget".
So it's budget.
> Final decision: **budget**.
> Let's double check the "invoice" definition. "an agency/vendor ESTIMATE document... is the agency's BILL for a client job — invoice, not budget". This is not an agency bill.
"A hotel/motel guest bill... is an invoice". Not this.
"provider's periodic customer statement... is budget". Not this.
This is a one-off grant payment voucher.
"money-only records: a contribution/expenditure request or approval form whose whole content is an amount... is budget".
This fits perfectly. It's a form (voucher) whose content is a contribution amount ($278,000).
> So, **budget**.
> One detail: "A check face/check stub stays budget even when the detachable stub's columns are headed 'INVOICE DATE'/'INVOICE NO.'/'INVOICE AMOUNT'". This document has "VOUCHER NO.", "DATE", "DUE DATE". It looks like a check stub or payment voucher.
> Conclusion: budget.
> Wait, is it a form?
Check 10: "administrative form... internal authorization/approval forms with an approval signature/date block".
Check 7: "Money function overrides form layout... money-only forms are budget".
The page is primarily a financial record (voucher for $278,000 contribution).
So budget.
> Let's look at the labels again.
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> The document is a "VOUCHER" for a contribution.
Category: budget.
> Evidence:
- Header: "VOUCHER", "BROWN & WILL FARSON TOBACCO CORPORATION".
- Content: Vendor "The Franklin Institute", Item Description "Final contribution for grant...", Amount "$278,000.00", Account "Gen, Corp, Contributions- Medical- Other".
- Function: Internal disbursement/contribution record.
- Matches Check 7 (budget): "money-only records: a contribution/expenditure request or approval form whose whole content is an amount... is budget" and "a check face or check stub... is budget".
> Runner-up: form. Ruled out because Check 7 (financial) overrides form layout for money records.
Runner-up: invoice. Ruled out because it's not a vendor bill for goods/services sold, but an internal contribution/grant payment record (budget).
> One final check: Is it a "payment request"?
Invoice definition: "a payment request... is an invoice".
But budget definition: "contribution/expenditure request or approval form whose whole content is an amount... is budget".
The distinction is usually: Invoice is from vendor to buyer (charges owed). Budget/Expenditure request is internal (requesting money to be spent).
This document is from Brown & Will Farson (the company) to its own accounting/payroll (implied by "VOUCHER", account codes). It's an internal request/approval to pay a grant. So it's budget.
> The text "REMITTANCE ADVICE INFO. (15 CHAIR ONLY)" suggests this is the copy sent with the check or kept as remittance advice.
"MAIL CHECK TO ADDRESS SHOWN" -> "The Franklin Institute".
This is the payment authorization/voucher.
Internal financial document -> budget.
> Final label: budget.

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
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a table with "PRODUCT", "PERIOD", "GROSS AMOUNT", "GROSS CHANGE", "TOTALS BY PRODUCT/MONTH", "OUTDOOR ESTIMATE RECAP - ODO1(S)". It has real content (a financial table).
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Typed text throughout.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions or transmittal note.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No career history.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name/volume/issue/page number on the page itself.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: "OUTDOOR ESTIMATE RECAP - ODO1(S)". "CLIENT: P.M. INC.", "EST NO: 4155", "DESC: 774A ODP B&H BUS SHELTERS". Table with "PRODUCT", "PERIOD", "GROSS AMOUNT", "GROSS CHANGE", "TOTAL". Total is 330,550.00.
- Let's look at the rules for invoice vs budget.
- "invoice: ... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
- Wait, the rule also says: "Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- Let's re-read carefully: "an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- This document has "EST NO: 4155". It has "GROSS AMOUNT" and "GROSS CHANGE" columns. It has a "TOTAL" of 330,550.00. It is an "ESTIMATE RECAP".
- Wait, the budget bullet says: "an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
- Does this document have "GROSS CHANGE"? Yes. "GROSS AMOUNT" and "GROSS CHANGE". This implies it's comparing original vs revised, or it's a recap of estimates.
- Let's look at the invoice bullet: "when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
- This document has "EST NO: 4155". It has "GROSS AMOUNT" and "GROSS CHANGE". This looks like it compares original vs revised (Gross Amount vs Gross Change). Or maybe it's just a recap.
- Wait, the budget bullet explicitly uses "OUTDOOR ESTIMATE RECAP" as an example of budget: "(e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter)".
- Let's look at the document again. "OUTDOOR ESTIMATE RECAP - ODO1(S)". "PERIOD 01/01/94 TO 12/31/94". "DATE 05/06/94". "CLIENT: P.M. INC.". "EST NO: 4155". "DESC: 774A ODP B&H BUS SHELTERS".
- Table: "TOTALS BY PRODUCT/MONTH SHOWING DATE". "PRODUCT 12- B&H 85'S". "PERIOD JUN 1994 QUARTER 2 ... SEP QUARTER 3 ... OCT DEC QUARTER 4". "GROSS AMOUNT 90,250.00 ... 330,550.00". "GROSS CHANGE 90,250.00 ... 330,550.00".
- The amounts are identical in both columns. This looks like a planning document showing planned gross amounts by future quarter (Jun 1994, Sep 1994, Oct/Dec 1994). The period is 01/01/94 to 12/31/94. The dates in the table are future quarters (Q2, Q3, Q4 of 1994). The date of the document is 05/06/94. So it's planning upcoming placements.
- The budget bullet says: "an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
- Wait, the budget bullet says "no estimate number...". But this document HAS "EST NO: 4155".
- Let's re-read the invoice bullet: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
- This document has "EST NO: 4155". It has "GROSS AMOUNT" and "GROSS CHANGE" columns. Even if the values are the same, it has the structure of comparing original vs revised (or it's just a recap with an estimate number).
- Actually, let's look at the budget bullet again: "Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- The key distinction: "ONLY plans upcoming placements — no estimate number...". This document HAS an estimate number ("EST NO: 4155"). Therefore, it falls under the invoice bullet: "an estimate/recap/change order that names an estimate number... is the agency's bill (invoice)."
- Wait, is it billing completed work? The period is 01/01/94 to 12/31/94. The document date is 05/06/94. The table shows Jun 1994, Sep 1994, Oct/Dec 1994. These are future quarters relative to May 1994. So it's planning future placements.
- But the invoice bullet explicitly says: "when it names an estimate number ("EST NO")... the word "estimate" in the title does NOT make it budget."
- Let's re-read carefully: "Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- The example in the budget bullet is exactly this document type: "an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter". The description matches perfectly: "OUTDOOR ESTIMATE RECAP", "BUS SHELTERS", "planned gross amounts by future quarter" (Jun 1994, Sep 1994, Oct/Dec 1994).
- BUT the budget bullet says this example has "no estimate number". This document HAS "EST NO: 4155".
- The invoice bullet says: "when it names an estimate number ("EST NO")... is the agency's bill (invoice)."
- So because it has "EST NO: 4155", it is an invoice?
- Let's look at the columns: "GROSS AMOUNT" and "GROSS CHANGE". If they are the same, maybe it's just a recap. But the presence of "EST NO" triggers the invoice rule.
- Wait, the budget bullet says: "an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
- The "e.g." is describing the budget case. The invoice case is "an estimate/recap/change order that names an estimate number...".
- Since this document names an estimate number ("EST NO: 4155"), it falls into the invoice category according to the explicit exception: "but see the invoice bullet — an estimate/recap/change order that names an estimate number... is the agency's bill (invoice)."
- Let's check if there's any other evidence. "FORM MO1A REV 04-14-83" at the bottom.
- Is it a form? Check 10: "administrative form". But check 7 says "Money function overrides form layout". So it's either invoice or budget.
- Given "EST NO: 4155", it matches the invoice bullet's condition "names an estimate number ("EST NO")".
- Therefore, invoice.
> Let's double check.
Budget bullet: "an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice"
Invoice bullet: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
> The document has:
- Title: "OUTDOOR ESTIMATE RECAP"
- "EST NO: 4155"
- Columns: "GROSS AMOUNT", "GROSS CHANGE" (comparing original vs present/revised estimate columns)
- Total: 330,550.00
> This perfectly matches the invoice bullet: "names an estimate number ("EST NO")", "compares original vs. present/revised estimate columns" (Gross Amount vs Gross Change). Even if the values are currently the same, the structure is there. And the explicit mention of "EST NO" triggers the invoice rule over the budget rule.
> So the label is invoice.
> Let's quickly check other categories just in case.
- form: "FORM MO1A REV 04-14-83" is at the bottom. But check 7 says money function overrides form layout.
- presentation: no.
- scientific_report: no.
> Final decision: invoice.
Evidence: "EST NO: 4155", "OUTDOOR ESTIMATE RECAP", "GROSS AMOUNT" / "GROSS CHANGE" columns, total amount. Matches invoice bullet for agency estimate/recap that names an estimate number and compares columns.
> Wait, is "GROSS CHANGE" a revision? Yes, "Gross Amount" vs "Gross Change" implies original vs revised.
The text says: "compares original vs. present/revised estimate columns". "GROSS AMOUNT" and "GROSS CHANGE" are exactly that.
So it is invoice.
> Let's write the scratchpad.
file_folder: no — page has a financial table with product, period, amounts, not just an identifier.
handwritten: no — typed text.
form: no — although it has a form number at the bottom ("FORM MO1A REV 04-14-83"), check 7 says money function overrides form layout.
invoice: yes — "OUTDOOR ESTIMATE RECAP" with "EST NO: 4155", "GROSS AMOUNT" and "GROSS CHANGE" columns, and a total of $330,550.00. The invoice bullet explicitly states that an agency estimate/recap that names an estimate number ("EST NO") or compares original vs. present/revised estimate columns is an invoice, not budget.
Runner-up: budget, ruled out because the document names an estimate number ("EST NO: 4155") and has "GROSS AMOUNT" / "GROSS CHANGE" columns, which triggers the invoice exception for agency estimates/recaps that bill a client job, rather than being a pure planning document with no estimate number.

---