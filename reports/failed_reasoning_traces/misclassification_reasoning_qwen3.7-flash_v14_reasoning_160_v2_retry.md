# Misclassification Reasoning — qwen3.7-flash_v14_reasoning_160_v2_retry

**Overall Accuracy:** 85.0% (136/160)
**Total Errors:** 24
**Unique Confused Pairs:** 19

---

## budget → invoice (3 errors)

### `rvl_cdip__budget__0001.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is a fax-like transmission header? No, just a Bates number "2041838831" on the side. Wait, let's look closer. No fax header.
- **Masthead/Running head:** "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING". This is a company letterhead/logo, not a newspaper/magazine masthead or journal running head.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder.**
    *   Evidence: The page has a lot of content: a table with costs, signatures, headers. Not just an ID or stamp.
    *   Result: not this check.
> *   **Check 2: handwritten.**
    *   Evidence: There are signatures at the bottom ("Theresa Luter", "Kenneth C. ..."), but the majority of the content is typed text and a table.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET.**
    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire.**
    *   Evidence: No survey questions.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume.**
    *   Evidence: No CV content.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication.**
    *   Evidence: No journal name, volume, issue, page range.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget.**
    *   Evidence: The document is titled "DATABASE MARKETING ESTIMATE".
    *   It lists "CLIENT: PHILIP MORRIS-INC", "L B JOB#: WRO149".
    *   It has columns "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE".
    *   It lists costs: "OTHER (SEE NOTES) 20,000.00 45,000.00", "TOTAL COMMISSIONABLE COSTS 20,000.00 45,000.00", "AGENCY COMMISSION 3,000.00 6,750.00", "TRAVEL AND EXPENSES 2,900.00 2,900.00", "DATABASE RESEARCH FEE 35,000.00 35,000.00", "TOTAL GROSS COSTS 61,500.00 90,250.00".
    *   Notes: "ESTIMATE REVISED TO COVER ADDITIONAL DATA PROCESSING FOR THE MERIT SEGMENTATION STUDY."
    *   Signatures at the bottom: CLIENT, BRAND, AGENCY.
    *   Is this an invoice or a budget?
    *   Let's look at the definitions.
    *   **Invoice:** "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher... an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement with unit prices, amounts, and totals... An agency estimate/recap/change order is the agency's BILL for a client job... when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements... or carries a billing designation ("BILLING TYPE PROGRESSIVE")... The word 'estimate' in the title does NOT make it budget."
    *   **Budget:** "internal money planning, tracking, or disbursement... money-only records... A provider's periodic customer statement... is budget... Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job... plans projected spend rather than billing completed work, so it is budget, not invoice".
    *   This document is from "LEO BURNETT U.S.A." (an advertising agency) to "PHILIP MORRIS-INC" (client).
    *   Title: "DATABASE MARKETING ESTIMATE".
    *   It has "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE". This implies a revision.
    *   The note says: "ESTIMATE REVISED TO COVER ADDITIONAL DATA PROCESSING...".
    *   It lists costs like "AGENCY COMMISSION", "TRAVEL AND EXPENSES", "DATABASE RESEARCH FEE".
    *   Wait, is this billing for work done or planning future work?
    *   "DATABASE MARKETING ESTIMATE". Usually an estimate is a quote for future work.
    *   However, let's look at the "invoice" bullet: "An agency/vendor estimate or recap that ONLY plans upcoming placements... is budget... But see the invoice bullet — an agency estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
    *   This document has "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE". It is revising a prior estimate.
    *   It lists specific costs: "OTHER (SEE NOTES) 20,000.00 -> 45,000.00". "TOTAL GROSS COSTS 61,500.00 -> 90,250.00".
    *   The note says "ESTIMATE REVISED TO COVER ADDITIONAL DATA PROCESSING".
    *   This looks like a revised estimate (change order) for a client job.
    *   Wait, let's re-read the budget definition carefully. "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job... plans projected spend rather than billing completed work, so it is budget, not invoice".
    *   This document *does* have a revision line ("PREVIOUS ESTIMATE" vs "CURRENT ESTIMATE"). It is revising a prior estimate.
    *   The invoice bullet says: "an agency estimate/recap/change order that names an estimate number, revises a prior estimate... is the agency's bill (invoice)."
    *   Here we have "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE". This is a revision.
    *   Also, Leo Burnett is an advertising agency. Philip Morris is the client.
    *   This is a document from an agency to a client.
    *   Is it an invoice (billing) or a budget (planning)?
    *   The title is "DATABASE MARKETING ESTIMATE".
    *   Usually, an estimate is a quote. But if it's revised and signed by client and agency, it might be a finalized budget/authorization or a bill.
    *   Let's look at the signatures: "CLIENT", "BRAND", "AGENCY". This looks like an approval block.
    *   Check 10 (Administrative Form): "internal authorization/approval forms with an approval signature/date block."
    *   Check 7 (Financial): "Money function overrides form layout... A payment VOUCHER... is invoice... But an internal expenditure-authorization form... is a form (check 10)...".
    *   Wait, is this an authorization form? "AUTHORIZATION REQUEST... names the work to be funded... and carries an approval signature/date block... is a form".
    *   This document has signatures from Client, Brand, Agency. It looks like an approval of an estimate.
    *   Let's check the budget definition again: "Also covers money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient... is budget... This covers only REQUEST/CHECKLIST/STATEMENT forms; it does NOT cover a project-funding authorization/approval form that names the work to be funded, carries finance-data/expense-code fields... and has an approval block — authorizing a specific funded project is a form (check 10)".
    *   This document names the work ("MERIT SEGMENTATION STUDY"), carries finance data (costs), and has an approval block (signatures).
    *   So it could be a **form** (check 10) or **budget** (check 7) or **invoice** (check 7).
    *   Let's look at the "invoice" bullet again. "An agency/vendor estimate or recap that ONLY plans upcoming placements... is budget... But see the invoice bullet — an agency estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
    *   This document revises a prior estimate ("PREVIOUS ESTIMATE" vs "CURRENT ESTIMATE"). The note says "ESTIMATE REVISED...".
    *   So under the strict reading of the prompt: "an agency estimate/recap/change order that... revises a prior estimate... is the agency's bill (invoice)."
    *   Wait, is it a bill? Or is it a budget/estimate for future work?
    *   "DATABASE MARKETING ESTIMATE". Date: 03/09/93. Start Date: 02/16/93. Fiscal Year: 93.
    *   It lists costs. Total Gross Costs: 61,500.00 (Previous) -> 90,250.00 (Current).
    *   If it's an estimate for future work, it's budget. If it's a bill for work done, it's invoice.
    *   The prompt says: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements... plans projected spend rather than billing completed work, so it is budget, not invoice".
    *   "But see the invoice bullet — an agency estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
    *   This document *revises a prior estimate*. It has "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE".
    *   Therefore, according to the specific instruction: "an agency estimate/recap/change order that... revises a prior estimate... is the agency's bill (invoice)."
    *   Wait, let's look at the signatures. Client, Brand, Agency. This is an approval.
    *   If it's an approval of a budget/estimate, is it a form?
    *   Check 7 caveat: "an internal expenditure-authorization form... is a form (check 10)... But an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
    *   This is an agency (Leo Burnett) document to a client (Philip Morris). It's not internal to Philip Morris. It's an external vendor document.
    *   So it's not an "internal expenditure-authorization form".
    *   It is an agency document.
    *   If it lists charges and totals, it's an invoice.
    *   Does it list "actual charges and totals owed"? It lists an "ESTIMATE".
    *   The note says "ESTIMATE REVISED TO COVER ADDITIONAL DATA PROCESSING".
    *   This is a revised estimate.
    *   The rule says: "an agency estimate/recap/change order that... revises a prior estimate... is the agency's bill (invoice)."
    *   So this should be **invoice**.
>     *   Let's reconsider **budget**.
    *   "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job... plans projected spend rather than billing completed work, so it is budget, not invoice".
    *   This document *has* a revision line ("PREVIOUS ESTIMATE" vs "CURRENT ESTIMATE"). So it falls into the "invoice" category according to the exception: "But see the invoice bullet — an agency estimate/recap/change order that names an estimate number, revises a prior estimate... is the agency's bill (invoice)."
    *   Wait, is "PREVIOUS ESTIMATE" an estimate number? No, it's a column header.
    *   But it is revising a prior estimate.
    *   The text says "ESTIMATE REVISED...".
    *   So it fits the "revises a prior estimate" criterion for invoice.
>     *   Let's look at **form** (Check 10).
    *   "internal authorization/approval forms with an approval signature/date block."
    *   This has signatures. But it's from an agency to a client.
    *   Check 7 says: "Money function overrides form layout... A payment VOUCHER... is invoice... But an internal expenditure-authorization form... is a form".
    *   This is not internal. It's Leo Burnett (agency) to Philip Morris (client).
    *   So Check 7 applies.
    *   Is it Invoice or Budget?
    *   The document is an "ESTIMATE".
    *   Usually estimates are budget (planning).
    *   BUT the rule says: "an agency estimate/recap/change order that... revises a prior estimate... is the agency's bill (invoice)."
    *   This document has "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE". It is a revision.
    *   So it is **invoice**.
>     *   Wait, let's look at the content again.
    *   "DATABASE MARKETING ESTIMATE".
    *   Client: Philip Morris.
    *   Description: Merit Segmentation Study.
    *   Product: 27-Merit.
    *   Costs: Other, Total Commissionable, Agency Commission, Travel, Database Research Fee, Shipping. Total Gross Costs: 90,250.00.
    *   This looks like a quote/estimate for a project.
    *   If it's a quote for future work, it's budget (planning).
    *   The rule: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements... plans projected spend rather than billing completed work, so it is budget, not invoice".
    *   The exception: "an agency estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
    *   This document *revises a prior estimate* (Previous vs Current).
    *   So it falls into the exception -> **invoice**.
>     *   Let's check if there's an "estimate number". "CLIENT ID#: TMR6800-93/SEGM". "L B JOB#: WRO149". These act as identifiers.
    *   "REV #: 01". "REV DATE: 02/16/93". "PREV REV DATE: 03/09/93". Wait, Rev Date is 02/16, Prev Rev Date is 03/09? No, Date is 03/09/93. Rev Date 02/16/93. Prev Rev Date 03/09/93? That's weird. Maybe Prev Rev Date is the date of the previous revision.
    *   Anyway, it has revision history.
    *   It is a revised estimate.
    *   According to the prompt: "an agency estimate/recap/change order that... revises a prior estimate... is the agency's bill (invoice)."
>     *   Wait, is it a **form**?
    *   Check 10: "administrative form... filled or blank fields... internal authorization/approval forms".
    *   This is an external document (Agency to Client).
    *   Check 7: "Money function overrides form layout... an agency/vendor document that lists actual charges and totals owed is an invoice".
    *   Does it list "actual charges and totals owed"? It lists an estimate.
    *   But the rule says a revised estimate is an invoice (bill).
>     *   Let's look at the label **budget**.
    *   "Also covers money-only records... a financial or money-data table... budget-vs-actual".
    *   This is a comparison of Previous Estimate vs Current Estimate.
    *   Is it a budget?
    *   "Money PLANNING for future work is budget... an agency/vendor estimate... that ONLY plans upcoming placements... is budget".
    *   This document *revises* a prior estimate. The rule says revised estimates are invoices.
    *   "But see the invoice bullet — an agency estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
    *   This document has "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE". It is revising.
    *   So it is **invoice**.
>     *   Let's look at the signatures. Client, Brand, Agency.
    *   This is an approval of the estimate.
    *   If it's an approval of a budget/estimate, is it a form?
    *   Check 7 caveat: "an internal expenditure-authorization form... is a form". This is external (Agency to Client).
    *   Check 7: "an agency/vendor document that lists actual charges and totals owed is an invoice".
    *   Even if it's an estimate, if it's revised, it's treated as a bill/invoice in this classification scheme.
>     *   Wait, let's look at the "invoice" definition again.
    *   "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement... An agency estimate/recap/change order is the agency's BILL for a client job... when it names an estimate number... revises a prior estimate... The word 'estimate' in the title does NOT make it budget."
    *   This fits perfectly. Leo Burnett (agency) to Philip Morris (client). Title "DATABASE MARKETING ESTIMATE". It has Previous vs Current (revises prior estimate). It lists charges (Total Gross Costs).
    *   So it is **invoice**.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification.**
    *   Evidence: No MSDS, no product formulation, no "shall/must".
    *   Result: not this check.
> *   **Check 9: SLIDE DECK... -> presentation.**
    *   Evidence: Not a slide deck. It's a document with a table and signatures.
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM -> form.**
    *   Evidence: It has fields and signatures. But Check 7 (Financial) takes precedence if money function is primary.
    *   Check 7 says money function overrides form layout.
    *   Is the money function primary? Yes, it's a cost estimate/bill.
    *   Is it an internal authorization form? No, it's Agency to Client.
    *   So Check 7 applies.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter.**
    *   Evidence: No letterhead with external address + salutation + closing. It has a company logo (Leo Burnett) and a structured table.
    *   Result: not this check.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article.**
    *   Evidence: No masthead, no news typography.
    *   Result: not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report.**
    *   Evidence: No running narrative prose about research.
    *   Result: not this check.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement.**
    *   Evidence: No product imagery, slogans. It's a business document.
    *   Result: not this check.
> **Conclusion:**
The document is a "DATABASE MARKETING ESTIMATE" from Leo Burnett (ad agency) to Philip Morris (client).
It compares "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE".
It lists costs and totals.
It has a note "ESTIMATE REVISED...".
According to Check 7 (Invoice bullet): "an agency estimate/recap/change order that... revises a prior estimate... is the agency's bill (invoice)."
"The word 'estimate' in the title does NOT make it budget."
So it is **invoice**.
> Wait, let's double check **budget**.
"Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job... plans projected spend rather than billing completed work, so it is budget, not invoice".
This document *has* a revision line ("PREVIOUS ESTIMATE" vs "CURRENT ESTIMATE").
So it is NOT "ONLY plans upcoming placements" without revision. It revises a prior estimate.
Therefore, it falls into the **invoice** category.
> Final check: Is it a **form**?
Check 10: "internal authorization/approval forms...". This is external.
Check 7: "Money function overrides form layout".
So **invoice**.
> One detail: "L B JOB#: WRO149". "CLIENT ID#: TMR6800-93/SEGM".
These are identifiers.
The document is a revised estimate (change order) from an agency to a client.
Classification: **invoice**.
> Wait, looking closely at the bottom signatures:
"CLIENT" (Theresa Luter), "BRAND" (Kenneth C...), "AGENCY" (signed).
This is an approval of the estimate.
Does an approved estimate count as an invoice?
The rule says: "an agency estimate/recap/change order that... revises a prior estimate... is the agency's bill (invoice)."
It doesn't say "unapproved". It says the document *is* the bill.
Also, the rule says: "an internal expenditure-authorization form... is a form". This is not internal.
So **invoice** is the best fit.
> Let's re-read the budget definition carefully.
"budget: internal money planning... A provider's periodic customer statement... is budget".
Leo Burnett is a provider. Philip Morris is the customer.
Is this a "periodic customer statement"?
No, it's an "ESTIMATE".
"Also covers money-only records... a financial or money-data table... budget-vs-actual".
This is Previous Estimate vs Current Estimate.
But the invoice bullet is specific: "an agency estimate/recap/change order that... revises a prior estimate... is the agency's bill (invoice)."
This document revises a prior estimate.
So **invoice**.
> One more check: **form**.
Check 10: "administrative form... filled or blank fields...".
This document has fields (Client, Job#, etc.) and is filled.
But Check 7 says: "Money function overrides form layout... a billing or payment page stays financial even when it is printed on a form".
Is this a billing page?
It's an estimate.
"An agency/vendor ESTIMATE document... is an invoice... when it names an estimate number... revises a prior estimate...".
This document revises a prior estimate.
So it is financial (invoice), not form.
> Final decision: **invoice**.
> Wait, is there any chance it's **budget**?
"Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line..."
This document HAS a revision line ("PREVIOUS ESTIMATE" column, "REV #", "REV DATE").
So it is excluded from the "budget" definition of "ONLY plans... no revision".
It falls into the "invoice" definition of "revises a prior estimate".
> So **invoice**.
> One final check on the label string: "invoice".
> Scratchpad summary:
- file_folder: no, has content.
- handwritten: no, mostly typed.
- fax: no.
- questionnaire: no.
- resume: no.
- scientific_publication: no.
- financial (invoice/budget): Yes. It's a "DATABASE MARKETING ESTIMATE" from Leo Burnett (agency) to Philip Morris (client). It lists costs (Total Gross Costs 90,250.00). It compares "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE" (revises prior estimate). Note says "ESTIMATE REVISED".
- Check 7 Invoice bullet: "an agency estimate/recap/change order that... revises a prior estimate... is the agency's bill (invoice)." The word "estimate" in title doesn't make it budget.
- Check 7 Budget bullet: excludes estimates that "revises a prior estimate" (that goes to invoice). Budget is for estimates that "ONLY plans upcoming placements — no... revision/prior-adjustment line". This has revision lines.
- So it is invoice.
- form: Check 7 overrides form layout for money documents. This is not an internal authorization form (it's external agency to client).
- presentation: no.
> Runner-up: budget. Ruled out because the document revises a prior estimate ("PREVIOUS ESTIMATE" vs "CURRENT ESTIMATE", "REV #"), which per the instructions moves it from budget (planning) to invoice (billing/revised estimate). Also ruled out form because money function overrides layout and it's an external agency document, not an internal authorization form.
> Wait, is "PREVIOUS ESTIMATE" a revision line? Yes, it's a column comparing previous and current. And "REV #: 01".
The text says "ESTIMATE REVISED...".
So yes, it revises a prior estimate.
> Final label: invoice.

---
### `rvl_cdip__budget__0004.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is a fax-like transmission header? No, just "LEO BURNETT U.S.A.", "NEWSPAPER ESTIMATE RECAP - PN01", dates, client info. Wait, there's a Bates number "2049423331" at the bottom right. No mail header.
- **Masthead/Running head:** No newspaper masthead. No journal running head. "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING". This is an advertising agency letterhead/header.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder.**
    *   Evidence: The page has a lot of data (table with numbers, product names, dates). It's not just an ID or stamp.
    *   Result: not this check.
> *   **Check 2: handwritten.**
    *   Evidence: Mostly typed text and numbers. There is a signature "John" or similar and a checkmark/line drawn across the page. But the majority is typed data.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET.**
    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
    *   Result: not this check.
> *   **Check 4: QUESTIONNAIRE.**
    *   Evidence: No survey questions.
    *   Result: not this check.
> *   **Check 5: RESUME.**
    *   Evidence: No career history.
    *   Result: not this check.
> *   **Check 6: SCIENTIFIC_PUBLICATION.**
    *   Evidence: No journal name, volume, issue, page range on this page itself.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget.**
    *   Evidence: "LEO BURNETT U.S.A. ADVERTISING". "NEWSPAPER ESTIMATE RECAP - PN01". "CLIENT: P.M. INC.". "EST NO: 8010 REVISES EST DID 10/16/78". "DESC: MARLBORG ROP-703".
    *   Table columns: PRODUCT, PERIOD, GROSS AMOUNT, GROSS CHANGE, GROSS LESS C/C.
    *   Rows: MARLBORO RED, JAN 1978, FEB, MAR, QUARTER 1, APR, MAY, JUN, QUARTER 2, etc. Totals: 4,361,078.18.
    *   Analysis: This is an "ESTIMATE RECAP".
    *   Let's look at the rules for Check 7 (invoice vs budget).
    *   **Invoice:** "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
    *   **Budget:** "Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
    *   This document: "EST NO: 8010 REVISES EST DID 10/16/78". It has an estimate number (8010). It revises a prior estimate ("REVISES EST DID"). It has columns for "GROSS CHANGE" and "GROSS LESS C/C". It lists amounts for specific periods (Jan 1978 - Dec 1978). Wait, the period is 01/01/78 to 12/31/78. The date is 11/13/78. So this is a recap of an estimate for the upcoming year (1978) or current year.
    *   Let's re-read the budget rule carefully: "an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type... is budget".
    *   This document HAS an estimate number ("EST NO: 8010") and says "REVISES EST DID 10/16/78".
    *   Wait, the rule says: "an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line... is budget". This document *has* an estimate number and revision info.
    *   Let's look at the invoice rule: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements...".
    *   This document has "EST NO: 8010 REVISES EST DID 10/16/78". This matches the invoice criteria perfectly. It is a billing document (recap of charges/amounts) for a client job (Marlboro newspaper ads). Even though the period is 1978 and date is 11/13/78, it's a recap of the estimate which likely includes planned spend or actuals. The presence of "EST NO" and "REVISES EST" pushes it to invoice according to the specific text: "the word 'estimate' in the title does NOT make it budget... An agency estimate/recap/change order is the agency's BILL... when it names an estimate number...".
    *   Wait, let's look closer. "TOTALS BY PRODUCT/MONTH". "GROSS AMOUNT", "GROSS CHANGE", "GROSS LESS C/C".
    *   The total is $4,361,078.18.
    *   Is this a bill for goods sold? It's an advertising estimate recap. Advertising agencies bill for media placements.
    *   Let's check the budget definition again: "Also covers money-only records... a provider's periodic customer statement... is budget, not invoice". But this is an "ESTIMATE RECAP".
    *   The rule says: "an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line... is budget". Since this *has* an estimate number and revision line, it falls under the invoice definition: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate...".
    *   So this is an **invoice**.
> *   **Check 8: SPECIFICATION.**
    *   Evidence: No material safety data, no product formulation.
    *   Result: not this check.
> *   **Check 9: PRESENTATION.**
    *   Evidence: Not a slide deck. It's a financial table.
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM.**
    *   Evidence: It has a form number "FORM M-01 EFF. R-73" at the bottom left. It has fields. But Check 7 (Financial) overrides form layout. "Money function overrides form layout".
    *   Result: not this check (because Check 7 matches).
> *   **Check 11: CORRESPONDENCE.**
    *   Evidence: No TO/FROM/RE memo header. No letter structure.
    *   Result: not this check.
> *   **Check 12: NEWS_ARTICLE.**
    *   Evidence: No masthead, no news typography.
    *   Result: not this check.
> *   **Check 13: SCIENTIFIC_REPORT.**
    *   Evidence: No running narrative prose. It's a table.
    *   Result: not this check.
> *   **Check 14: ADVERTISEMENT.**
    *   Evidence: It's from an advertising agency (Leo Burnett), but it's an internal/external financial document (estimate recap), not a promotional ad for a product.
    *   Result: not this check.
> **Re-evaluating Check 7 (Invoice vs Budget):**
The document is "NEWSPAPER ESTIMATE RECAP - PN01".
Header: "EST NO: 8010 REVISES EST DID 10/16/78".
This explicitly matches the condition for **invoice**: "when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")".
The rule states: "the word 'estimate' in the title does NOT make it budget."
So, despite being an "estimate recap", the presence of "EST NO" and "REVISES EST" makes it an invoice (a bill for the client job).
> Wait, let's look at the "Budget" definition again.
"Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type... is budget".
This document HAS an estimate number and revision line. So it is NOT the "ONLY plans upcoming placements" case. It falls into the "invoice" case: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number...".
> Therefore, the label is **invoice**.
> Let's double check.
The document lists "GROSS AMOUNT", "GROSS CHANGE", "GROSS LESS C/C".
Total: 4,361,078.18.
This is a financial document.
It is an estimate recap from Leo Burnett (ad agency) for P.M. Inc. (Philip Morris).
It revises a previous estimate.
According to the prompt: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")..."
This matches perfectly.
> Final check of the label: **invoice**.
> One detail: "FORM M-01 EFF. R-73" is at the bottom. This is a form. But Check 7 says "Money function overrides form layout". And Check 7 is checked before Check 10.
Check 7: Financial document.
Invoice vs Budget.
Evidence for Invoice: "EST NO: 8010", "REVISES EST DID".
Evidence for Budget: It's an estimate for 1978 (future relative to 11/13/78? No, 11/13/78 is late in the year. The period is 01/01/78 to 12/31/78. So it's a recap for the current year, likely a budget or actuals recap).
However, the rule is specific about the *labels* on the document. "names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")". These labels are present. So it is classified as invoice.
> Wait, is there any other check?
Check 10: Administrative form. "A form does NOT have to be blank...". But Check 7 comes first. "Check 7 applies only when financial content IS the page's primary structure...". Yes, the primary structure is a financial table. "Money function overrides form layout". So Check 7 wins over Check 10.
> So the classification is **invoice**.
> Let's look at the "Runner-up" requirement.
Runner-up: budget. Ruled out because the document names an estimate number ("EST NO: 8010") and revises a prior estimate ("REVISES EST DID"), which per the instructions classifies an agency estimate/recap as an invoice (bill for a client job), not a budget (planning document).
> Wait, let's re-read the budget definition carefully.
"Also covers money-only records... a provider's periodic customer statement... is budget, not invoice".
Is this a periodic customer statement? No, it's an "ESTIMATE RECAP".
The rule says: "an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line... is budget".
Since this document HAS an estimate number and revision line, it is excluded from the "budget" definition of planning documents and falls into the "invoice" definition of billing documents.
> Correct label: invoice.
> One final check: Could it be a **form**?
Check 10: "administrative form".
Check 7: "financial document".
Check 7 is checked before Check 10.
"Check 7 applies only when financial content IS the page's primary structure... If the page is otherwise formatted as correspondence... classify it as correspondence... instead".
Here, the page is a financial table. So Check 7 applies.
Under Check 7, we decide between invoice and budget.
It matches invoice criteria.
> So, **invoice**.
> One detail: "DESC: MARLBORG ROP-703". Marlboro.
"CLIENT: P.M. INC." Philip Morris.
This is an ad agency billing/recap for a client.
> Final decision: invoice.

---
### `rvl_cdip__budget__0006.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** No "From/To/Sent/Subject" block. There is a "BILL TO" block, but that's part of an invoice layout.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a company header "Peake Printers, Inc." and a large "INVOICE" title.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a lot of content: an invoice table, billing info, company header. It's not just an ID or stamp.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: There is some handwriting ("otc- ADCAT", "from 1501-5201", "see attached original deposit/invoice", "Invoice: 83829"). But the majority of the page is printed text (invoice details, table, company info).
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. The "SENT BY:" header is not present (though there might be fax metadata, looking closely... no, just standard invoice layout). Wait, looking at the bottom, there's "TIMN 0163588", "CUSTOMER COPY", "FED I.D. #52-0784214". No fax transmission header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
    *   Evidence: No survey questions.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY**
    *   Evidence: No resume/CV.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE**
    *   Evidence: No journal name, volume, issue, DOI.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: The page is titled "INVOICE" in large bold letters at the top right.
    *   Header: "Peake Printers, Inc." (vendor).
    *   "BILL TO": "THE TOBACCO INSTITUTE".
    *   Table columns: DESCRIPTION, QUANTITY, U/M, UNIT PRICE, AMOUNT.
    *   Line item: "TWO SIDED DECAL: 'IT'S THE LAW--UNDER 18' PRINTS 2/2, 5 1/2 x 7 1/2\"", Quantity 5000, Unit Price 5145.000 (wait, 5145.00 total? Ah, unit price is likely per 1000 or similar, or total is 5145.00. Let's look: 5145.000 under Unit Price? No, 5145.00 under Amount. Wait. 5000 quantity. Unit price 5145.000? That's weird. Ah, maybe $1.029 per unit? 5000 * 1.029 = 5145. Let's look at the numbers. 5145.000 under Unit Price column? No, 5145.00 is under Amount. 5145.000 is under Unit Price. Wait. 5000 * 1.029 = 5145. Maybe unit price is 1.029? The text says "5145.000". Let's assume it's a price.
    *   Sub Total: 5145.00. Tax: 308.70. Total Invoice: 5453.70.
    *   "AMT DUE 5453.70". "LESS DEPOSIT (11000.00)". "CREDIT BALANCE $5546.30".
    *   This is clearly a bill from a vendor (Peake Printers) for goods/services (decals).
    *   Check 7 definition: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an 'INVOICE' header with line items and amount due..."
    *   Result: **invoice**.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
    *   Evidence: Not an MSDS or product spec.
    *   Result: not this check (stopped at 7).
> *   **Check 9: SLIDE DECK...**
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM**
    *   Result: not this check (stopped at 7). Financial function overrides form layout.
> *   **Check 11: CORRESPONDENCE**
    *   Result: not this check.
> *   **Check 12: PUBLISHED JOURNALISM**
    *   Result: not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP**
    *   Result: not this check.
> *   **Check 14: PROMOTIONAL MATERIAL**
    *   Result: not this check.
> **Conclusion:**
The page is an invoice from Peake Printers, Inc. to The Tobacco Institute. It has an "INVOICE" header, line items, amounts, tax, total due. It fits Check 7 perfectly.
> Runner-up: form. Ruled out because check 7 (financial document/invoice) takes precedence over form layout when the primary function is billing for goods/services. The page is explicitly titled "INVOICE".
> Let's double check the "budget" vs "invoice" distinction in Check 7.
- Invoice: outside vendor states charges owed. Peake Printers is an outside vendor. They are billing for decals.
- Budget: internal money planning. This is a bill from an outside company.
So it is definitely invoice.
> Final check of the text:
- Top right: "INVOICE"
- Top left: "Peake Printers, Inc." address.
- "BILL TO": The Tobacco Institute.
- Table with Description, Quantity, Unit Price, Amount.
- "TOTAL INVOICE 5453.70".
- "CONFIDENTIAL: MINNESOTA TOBACCO LITIGATION" stamp (legal stamp, ignored per instructions).
- Handwritten note about deposit/invoice.
> Everything points to invoice.

---

## invoice → form (3 errors)

### `rvl_cdip__invoice__0003.png`
**Expected:** `invoice` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow a specific scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: No "From/To/Sent/Subject" mail headers. There is a "REQUISITIONER'S COPY", "PURCHASE ORDER NO.", "DATE", "REQ. NO.". This looks like a purchase order or invoice/requisition form. Wait, let's look closer.
- Masthead/running head: "THE AMERICAN TOBACCO COMPANY" logo at top left. "SIX STAMFORD FORUM...". "REQUISITIONER'S COPY". No newspaper/magazine masthead. No journal running head.
> **Check 1: file_folder**
- Content: Lots of text, tables, addresses, signatures. Not just an ID/stamp.
- Result: not this check.
> **Check 2: handwritten**
- Most content is typed. There is a signature "L. Cannarota" and "By [signature]". Not majority handwritten.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- No "FACSIMILE" or "FAX COVER SHEET" header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Not a survey.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Not a resume.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE**
- No journal name/volume/issue on the page itself.
- Result: not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Let's analyze the financial content.
- Header: "THE AMERICAN TOBACCO COMPANY", "REQUISITIONER'S COPY".
- "PURCHASE ORDER NO. M 13174", "DATE May 27, 1992", "REQ. NO. Auth #R-44".
- "TO: Webcraft Technologies, Inc." (Supplier).
- "SHIP TO: Neil 3rd Class Bulk Rate...".
- Table columns: QUANTITY, CODE NO., DESCRIPTION, PRICE.
- Rows:
    - 400,000 CARLTON Tar Chart "Reward and Shelter" Direct Mail Units ... $787.21/M
    - Plus Prep., Proof, Programming ... $7,600.00
    - 400,000 Advanced Postage - 3rd Class Bulk Rate - Indicia ... ($93,200.00)
    - 3 Non-Standard Ink Charge ... $250.00/ea
- Text: "Costs include 42 basic plates...", "Refund due, if any, for unused advanced postage. Please forward a copy of U.S. Postal Document 3802 with your reconciliation and refund."
- Bottom: "ACCOUNTING CHARGE NO. Marketing Adv. Exp.", checkboxes for "STATE SALES TAX...", "EXEMPTION CERTIFICATE", "DIRECT PAYMENT PERMIT".
- "Please contact on any questions regarding this Purchase Order."
- Signature: "By [signature]".
> Is this an invoice or a budget?
- Check 7 definition:
    - invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an 'INVOICE' header with line items and amount due... A payment VOUCHER... A check face... is the DISBURSEMENT instrument and stays budget".
    - budget: "internal money planning, tracking, or disbursement... a check face or check stub... Also covers money-only records... a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient... is budget, not form".
    - Caveat: "an internal expenditure-authorization form (an 'AUTHORIZATION REQUEST' for funds... purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget".
    - Wait, this document has billable charges? "CARLTON Tar Chart... $787.21/M", "Plus Prep... $7,600.00", "Advanced Postage... ($93,200.00)".
    - But the header says "REQUISITIONER'S COPY" and "PURCHASE ORDER NO.".
    - It looks like a Purchase Order (PO) or a Requisition.
    - Let's re-read Check 7 carefully.
    - "invoice: an outside vendor... states charges owed... A payment VOUCHER... A check face... is budget".
    - "budget: internal money planning... expense reports... a check face or check stub... Also covers money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient... is budget, not form".
    - "Caveat: an internal expenditure-authorization form (an 'AUTHORIZATION REQUEST' for funds, 'ADVERTISING AND SELLING AUTHORIZATION', purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget".
    - Wait, this document *does* have billable charges listed ($787.21/M, $7,600.00, etc.).
    - However, it is titled "REQUISITIONER'S COPY" and has "PURCHASE ORDER NO.".
    - Is it an invoice from Webcraft Technologies? No, it's from American Tobacco Company (logo at top left). It's a requisition/purchase order *to* Webcraft.
    - "BILLING INSTRUCTIONS - MAIL YOUR INVOICES IN DUPLICATE TO CONSIGNEE... MAIL INVOICES TO OUR ADMINISTRATIVE CENTER... GENERAL ACCOUNTING OFFICE...". This is instructions for the vendor (Webcraft) on how to send invoices.
    - So this document is a Purchase Order / Requisition.
    - Let's look at Check 10: ADMINISTRATIVE FORM. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."
    - Wait, Check 7 says: "A payment VOUCHER naming a payee, vendor/item fields, an amount... and a payment date is a payment instrument that BILLS a named payee... invoice".
    - Check 7 also says: "an internal expenditure-authorization form... purchase/requisition approval... is a form (check 10), not budget".
    - This document is a "REQUISITIONER'S COPY" of a Purchase Order. It authorizes the purchase. It lists the items and costs, but it's an internal authorization/requisition document (Purchase Order).
    - Wait, let's look at the structure. It has "PURCHASE ORDER NO.", "DATE", "REQ. NO.". It has "TO: Webcraft Technologies". It has line items with quantities and prices. It has an approval signature at the bottom ("By [signature]").
    - Is it a form? Check 10: "internal authorization/approval forms with an approval signature/date block." Yes.
    - Is it a budget? Check 7: "budget: internal money planning... expense reports...". But the caveat says: "an internal expenditure-authorization form (an 'AUTHORIZATION REQUEST' for funds... purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget".
    - Wait, this document *has* billable charges listed (the line items with prices). Does that make it an invoice?
    - "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD". This document is from American Tobacco Company (the buyer), not the vendor. The vendor is Webcraft. The billing instructions say "MAIL YOUR INVOICES...". So this is NOT an invoice from the vendor. It's a Purchase Order / Requisition from the buyer.
    - So it's not an invoice (check 7).
    - Is it a budget? "budget: internal money planning...". A purchase order is a commitment of funds, but is it a budget document?
    - Check 7 caveat: "an internal expenditure-authorization form... purchase/requisition approval... is a form (check 10), not budget". Even if it has amounts? "but no billable charges". This document has line items with prices.
    - Let's re-read carefully: "an internal expenditure-authorization form (an 'AUTHORIZATION REQUEST' for funds, 'ADVERTISING AND SELLING AUTHORIZATION', purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget".
    - This implies if it *does* have billable charges, maybe it's not a form? Or maybe it's still a form?
    - Actually, a Purchase Order is a form. It's an administrative document to authorize a purchase.
    - Let's look at Check 10: "administrative form... internal authorization/approval forms with an approval signature/date block." This fits perfectly. It's a requisition/purchase order form with an approval signature.
    - Wait, is there a stronger match?
    - Let's look at the financial content again. It's a "REQUISITIONER'S COPY". It's a Purchase Order.
    - Purchase orders are forms.
    - Let's check if it could be an invoice. "an outside vendor... states charges owed". No, this is the buyer's copy ("REQUISITIONER'S COPY"). The vendor is Webcraft. The text says "MAIL YOUR INVOICES...". So this is not the invoice.
    - Is it a budget? "budget: internal money planning...". A PO is a commitment, but usually classified as a form if it's an authorization. The caveat specifically mentions "purchase/requisition approval" as a form (check 10), not budget. Even though this one has line items with prices (which might be considered "billable charges" in a loose sense, but they are estimates/quoted prices for the PO, not an invoice from a vendor). The text says "Costs include...", "Refund due...". This looks like a detailed PO or a requisition with cost breakdown.
    - Actually, looking closely at the bottom: "ACCOUNTING CHARGE NO. Marketing Adv. Exp." "Please contact on any questions regarding this Purchase Order." "By [signature]". This is an approval block.
    - So it's an internal authorization/approval form (Purchase Order/Requisition).
    - Therefore, Check 10 (form) is the best fit.
> Let's re-evaluate Check 7 vs Check 10.
- Check 7 (invoice): "an outside vendor... states charges owed". This is not an outside vendor stating charges. This is the company (American Tobacco) issuing a Purchase Order to a vendor (Webcraft). The billing instructions tell the vendor to send invoices here. So this is NOT an invoice.
- Check 7 (budget): "internal money planning...". But the caveat says "purchase/requisition approval... is a form (check 10), not budget". This document is a requisition/purchase order approval.
- Check 10 (form): "internal authorization/approval forms with an approval signature/date block." This document has "REQUISITIONER'S COPY", "PURCHASE ORDER NO.", approval signature at the bottom. It is a form.
> Wait, is there any other category?
- Check 11: Correspondence. No.
- Check 12: News article. No.
- Check 13: Scientific report. No.
- Check 14: Advertisement. No.
> So it's likely `form`.
> Let's double check the "invoice" definition.
- "invoice: ... A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee for named goods/services/charges — invoice".
- This document has "PURCHASE ORDER NO.", not a payment voucher. It's a requisitioner's copy.
- "A check face/check stub ... is the DISBURSEMENT instrument and stays budget".
- This is a Purchase Order / Requisition.
> Let's look at the structure again.
- Top: American Tobacco Company logo. "REQUISITIONER'S COPY".
- "PURCHASE ORDER NO. M 13174".
- "TO: Webcraft Technologies, Inc." (Supplier).
- Table with Quantity, Code No, Description, Price.
- Bottom: Accounting charge no, checkboxes, signature "By ...".
- This is a standard Purchase Order form (or Requisition converted to PO).
- Function: Administrative data capture / authorization.
- Category: `form`.
> Let's check if it could be `budget`.
- "budget: ... a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking."
- "Also covers money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient ... is budget, not form".
- This document has more than just amount and recipient. It has a detailed breakdown of costs (printing, postage, ink charge). And it has an approval block.
- Caveat: "an internal expenditure-authorization form (an 'AUTHORIZATION REQUEST' for funds, 'ADVERTISING AND SELLING AUTHORIZATION', purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget".
- This caveat implies that if it *does* have billable charges, it might not be a form? Or does it mean "if it has no billable charges, it's a form; if it has billable charges, it's something else"?
- Actually, a Purchase Order *does* have billable charges (the items being ordered). But it's not an invoice from a vendor.
- The text says "MAIL YOUR INVOICES...". This confirms this document is not the invoice. It's the PO.
- A PO is a form. "internal authorization/approval forms".
> Let's consider `invoice` again.
- Could this be an invoice from American Tobacco to someone? No, "TO: Webcraft Technologies". American Tobacco is buying from Webcraft.
- "REQUISITIONER'S COPY" implies this is the copy kept by the person who requisitioned the purchase (internal).
- So it's an internal document authorizing a purchase.
- This fits `form` (Check 10).
> Let's check `specification` (Check 8).
- "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables...".
- This is a purchase order for printing (Carlton Tar Chart). Not a specification.
> Let's check `presentation` (Check 9).
- No.
> So `form` seems correct.
> Wait, is there any chance this is an `invoice`?
- "invoice: ... an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement with unit prices, amounts, and totals."
- This document has unit prices and totals. But it's a "REQUISITIONER'S COPY" of a "PURCHASE ORDER".
- The billing instructions say "MAIL YOUR INVOICES...". So the vendor (Webcraft) will send an invoice later. This document is the PO.
- A PO is a form.
> Final decision: `form`.
> Let's review the scratchpad steps.
1. file_folder: No, has content.
2. handwritten: No, mostly typed.
3. FAX: No.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No.
7. financial:
   - Is it invoice? No, it's a Purchase Order / Requisition from buyer to vendor, not an invoice from vendor to buyer. The text explicitly says "MAIL YOUR INVOICES...".
   - Is it budget? It has financial data, but it's an authorization form (Purchase Order/Requisition) with an approval signature. The caveat says "purchase/requisition approval ... is a form (check 10), not budget". Even though it lists costs, its primary function is authorization/approval of a purchase order. Wait, the caveat says "but no billable charges". This document *does* have line items with prices. Does that disqualify it from being a form under the caveat?
   - "an internal expenditure-authorization form ... that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form". This implies if it *has* billable charges, it might be budget or invoice?
   - But it's not an invoice (not from vendor).
   - Is it budget? "budget: internal money planning...". A PO is a commitment. But usually POs are forms.
   - Let's look at Check 10: "internal authorization/approval forms with an approval signature/date block." This is a very strong match. The document has an approval signature ("By [signature]") and is a requisition/purchase order.
   - The financial data (prices) is part of the form's fields (Quantity, Description, Price columns). It's a filled form (or a pre-filled form for approval).
   - "A form does NOT have to be blank — a filled form recording data is still a form".
   - So `form` is the correct label.
> Runner-up: `invoice`. Ruled out because the document is a "REQUISITIONER'S COPY" of a "PURCHASE ORDER" from the buyer (American Tobacco) to the supplier (Webcraft), with instructions for the supplier to "MAIL YOUR INVOICES". It is not an invoice stating charges owed by the supplier. Also ruled out `budget` because it is an authorization/approval form (PO/Requisition) with a signature block, which falls under Check 10 (form), specifically the "purchase/requisition approval" exception, even though it contains cost estimates/line items. Actually, the caveat says "no billable charges is a form". This has line items. But a PO is fundamentally a form. Let's stick with `form`.
> Wait, could it be `budget`?
- "budget: ... a statement of account ...". No.
- "budget: ... money-only records ...". No, it has descriptions.
> Let's look at the "invoice" definition again.
- "invoice: ... A payment VOUCHER naming a payee, vendor/item fields, an amount ... and a payment date is a payment instrument that BILLS a named payee ... invoice".
- This is not a payment voucher. It's a requisitioner's copy.
> So `form` is the best fit.
> One detail: "REQUISITIONER'S COPY". This is a copy of a Requisition or Purchase Order.
Requisitions and Purchase Orders are administrative forms.
> Final check of the text:
- "THE AMERICAN TOBACCO COMPANY"
- "REQUISITIONER'S COPY"
- "PURCHASE ORDER NO. M 13174"
- "TO: Webcraft Technologies, Inc."
- "BILLING INSTRUCTIONS - MAIL YOUR INVOICES..."
- Table with quantities and prices.
- "ACCOUNTING CHARGE NO."
- Signature line "By ...".
> This is a Purchase Order / Requisition form. Label: `form`.
> One more check: Could it be `invoice`?
- Sometimes internal documents that look like invoices are classified as invoices if they bill someone. But this is "REQUISITIONER'S COPY". The requisitioner is internal. The "TO" is the supplier. The supplier will invoice American Tobacco. So this is not the invoice.
> Could it be `budget`?
- Check 7: "budget: internal money planning...".
- Caveat: "an internal expenditure-authorization form (an 'AUTHORIZATION REQUEST' for funds... purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget".
- This document has billable charges (line items with prices). Does this push it to `budget` or `invoice`?
- If it has billable charges, it's not the "no billable charges" exception.
- But it's not an invoice (not from vendor).
- Is it a budget? "budget: ... expense reports ...".
- Actually, a Purchase Order with line items and prices is often just a form. The "billable charges" in the caveat likely refers to an invoice-like breakdown of costs owed. Here, the breakdown is the scope of work for the PO.
- Check 10: "administrative form ... internal authorization/approval forms with an approval signature/date block." This is the most direct description. The page is a form for authorization.
> I will go with `form`.
> Wait, looking at the table:
- Quantity: 400,000. Description: CARLTON Tar Chart... Price: $787.21/M.
- This is a detailed breakdown of costs for a printing job.
- It looks like a quote or a PO.
- "REQUISITIONER'S COPY" suggests it's an internal document to request/approve the purchase.
- So `form`.
> One final check on `invoice`.
- "invoice: ... an agency/vendor ESTIMATE document... itemized billing statement".
- If this is an estimate from Webcraft? No, it has American Tobacco logo and "REQUISITIONER'S COPY". It's from American Tobacco.
- So it's not an estimate from a vendor.
> Conclusion: `form`.

---
### `rvl_cdip__invoice__0004.png`
**Expected:** `invoice` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** I see "CRC CONTRACT RESEARCH CENTER", "Business Administration", "Geadresseerde/Aдресée:", "TELEFAX", "Kaiser & Kraft", "Bestelling Nr./Commande No.: 1513/94", "Datum/Date: 13 jan. 94". No "From/To/Sent/Subject" mail header. There is a "TELEFAX" label, but it's part of the letterhead/contact info, not a fax transmission header like "SENT BY: ... # 4/7". Wait, let's look closer. "TELEFAX (fax nr. 02/720 00 16)". This is contact info.
- **Masthead/Running head:** No newspaper masthead. No journal running head. There is a company header "CRC CONTRACT RESEARCH CENTER B.V.B.A./S.P.R.L.".
> **2. Scratchpad checks:**
> *   **Check 1: file_folder.**
    *   Evidence: The page has a lot of content: a table with items, prices, totals, delivery terms. It's not just an ID or stamp.
    *   Result: not this check.
> *   **Check 2: handwritten.**
    *   Evidence: Mostly typed text. There is a signature "J. Van den Bulcke" and some handwritten notes like "6459", "OUTGOING MAIL REGISTER", "4424". But the main content is typed.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET.**
    *   Evidence: "TELEFAX" is listed as contact info, but there is no "FACSIMILE TRANSMISSION" header with To/From/Date/Page count fields typical of a fax cover sheet. The "OUTGOING MAIL REGISTER" stamp is an internal filing mark.
    *   Result: not this check.
> *   **Check 4: questionnaire.**
    *   Evidence: No survey questions.
    *   Result: not this check.
> *   **Check 5: resume.**
    *   Evidence: No career history.
    *   Result: not this check.
> *   **Check 6: scientific_publication.**
    *   Evidence: No journal name/volume/issue.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget.**
    *   Evidence:
        *   Header: "CRC CONTRACT RESEARCH CENTER".
        *   Addressed to: "Kaiser & Kraft".
        *   "Bestelling Nr./Commande No.: 1513/94" (Order No.).
        *   Table with columns: "POSITIE/POSITION", "HOEVEELHEID/QUANTITE", "EENHEID/UNITE", "ARTIKELOMSCHRIJVING/DESIGNATION D'ARTICLE", "PRIJS/PRIX (BF)".
        *   Items: "Tafel met blad van zwart epoxylak...", "Sjideframe stoelen...", "transportkosten".
        *   "TOTAAL: 17.520,-".
        *   "Leveringstermijn/Délai de livraison: 4'de week 1994".
        *   "Betalswijze/Mode de paiement: 30 dagen einde maand".
        *   Signature: "J. Van den Bulcke Management Accountant".
    *   Analysis: This is a document from a vendor (CRC Contract Research Center) listing charges for goods (table, chairs, transport) to a customer (Kaiser & Kraft). It lists unit prices (implied by total calculation: 5.680 + 11.040 + 800 = 17.520). Wait, 5.680 + 11.040 + 800 = 17.520. Yes.
    *   Is it an invoice or a budget?
        *   It lists specific charges for goods sold (table, chairs, transport).
        *   It has a total amount due.
        *   It has payment terms ("30 dagen einde maand").
        *   The text says "(Gelieve deze referentie in ieder geval op de factuur te vermelden / veuillez sans exception reproduire cette référence sur la facture)" -> "Please mention this reference in any case on the invoice". This implies this document *is* the invoice or is accompanying an invoice, but looking at the structure, it's a billing statement. Wait, "Bestelling Nr" is Order Number. But the content is a list of items and prices with a total.
        *   Let's check the definition of invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an 'INVOICE' header with line items and amount due...".
        *   Let's check the definition of budget: "internal money planning...". This is external (CRC to Kaiser & Kraft).
        *   The text explicitly mentions "factuur" (invoice). "Gelieve deze referentie in ieder geval op de factuur te vermelden". This suggests this document might be a purchase order or a quote, but let's look closer.
        *   "Bestelling Nr./Commande No.: 1513/94". This is an Order Number.
        *   However, the table lists "PRIJS/PRIX".
        *   Usually, a document listing items, quantities, prices, and a total with payment terms is an invoice or a proforma invoice/quote.
        *   Let's look at the "invoice" bullet: "an outside vendor... states charges owed... a payment voucher... a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document...".
        *   Wait, is this an invoice? The text says "referentie... op de factuur" (reference on the invoice). This implies this is *not* the invoice itself, but perhaps a purchase order or a delivery note?
        *   Actually, let's look at the structure. It looks like a standard European invoice/credit note format. "CRC CONTRACT RESEARCH CENTER". Addressed to "Kaiser & Kraft".
        *   "Bestelling Nr" = Order Number. Often invoices reference the order number.
        *   The content is a list of delivered goods (Table, Chairs, Transport costs) and a total.
        *   "Leveringstermijn" = Delivery deadline.
        *   "Betalswijze" = Payment method.
        *   This is a billing document. It bills for goods.
        *   Let's re-read the invoice definition carefully. "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an 'INVOICE' header with line items and amount due...". It doesn't strictly require the word "INVOICE" in the header, but "a payment voucher... a receipt...".
        *   Wait, is it a "Bestelling" (Order)? "Bestelling Nr. 1513/94". If it's a purchase order, it's a request to buy. But the table has prices and a total. A purchase order usually has prices.
        *   However, the text "(Gelieve deze referentie in ieder geval op de factuur te vermelden...)" strongly suggests this document is *not* the invoice, but a document that accompanies it or is a request for it? Or maybe it's a "factuur" (invoice) and the text is a standard boilerplate saying "please put this order number on the invoice"?
        *   Actually, in many European systems, the "Bestelling" (Order) is the document from the buyer, and the "Factuur" (Invoice) is from the seller. Here, the header is "CRC CONTRACT RESEARCH CENTER" (the seller/vendor). They are addressing "Kaiser & Kraft" (the buyer).
        *   If CRC is the seller, and they are listing items and prices, this is likely an invoice or a proforma invoice.
        *   Let's look at the "invoice" definition again: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
        *   This page is a billing statement. It lists charges (5.680, 11.040, 800) and a total (17.520). It has payment terms (30 days end of month).
        *   Therefore, it is an **invoice**. Even if the header says "Bestelling Nr" (Order No), the content is a bill for goods. Wait, if it's an order, it's a request. But the total is calculated. And "Betalswijze" (Payment method) is listed. You don't usually list payment terms on a purchase order in this way (usually on the invoice). The presence of "Betalswijze: 30 dagen einde maand" (Payment terms: 30 days end of month) is a strong indicator of an invoice/bill.
        *   Also, the signature is "Management Accountant". Accountants sign invoices/payment requests.
        *   So, Check 7 applies. It is financial.
        *   Is it invoice or budget?
        *   Invoice: "outside vendor... states charges owed for goods or services SOLD". CRC is selling a table and chairs to Kaiser & Kraft.
        *   Budget: "internal money planning". This is external.
        *   So it's **invoice**.
> *   **Check 8: specification.**
    *   Evidence: No MSDS, no product formulation. The table describes a table and chairs, but it's a sales list, not a technical spec sheet with tolerances.
    *   Result: not this check.
> *   **Check 9: presentation.**
    *   Evidence: Not a slide deck.
    *   Result: not this check.
> *   **Check 10: form.**
    *   Evidence: It has fields, but the primary function is financial billing (Check 7 overrides). "Money function overrides form layout".
    *   Result: not this check (Check 7 is higher priority and matches). Wait, the checks are ordered 1-14. Check 7 is before Check 10. So if Check 7 matches, we stop.
> *   **Check 11: correspondence.**
    *   Evidence: No letter/memo structure. It's a structured financial document.
    *   Result: not this check.
> *   **Check 12: news_article.**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 13: scientific_report.**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 14: advertisement.**
    *   Evidence: No.
    *   Result: not this check.
> **Re-evaluating Check 7 (Invoice vs Budget vs Form):**
The document is from "CRC CONTRACT RESEARCH CENTER" to "Kaiser & Kraft".
It lists:
1. Tafel (Table) ... 5.680,-
2. Sjideframe stoelen (Chairs) ... 11.040,-
3. transportkosten (Transport costs) ... 800,-
Total: 17.520,-
> This is a bill for goods and services.
The text "Gelieve deze referentie in ieder geval op de factuur te vermelden" means "Please make sure to mention this reference on the invoice". This is slightly confusing. It implies this document *isn't* the invoice, or it's a standard text on a purchase order?
If this is a Purchase Order (Bestelling) from Kaiser & Kraft to CRC?
Header: "CRC CONTRACT RESEARCH CENTER". Usually the header is the sender.
If CRC is the sender, and they are sending a "Bestelling Nr 1513/94" to Kaiser & Kraft... that's weird. Usually the buyer sends the order.
Maybe CRC is the buyer? "Business Administration... Geadresseerde: Kaiser & Kraft".
If CRC is addressing Kaiser & Kraft, CRC is the sender.
If CRC is sending a document with "Bestelling Nr" (Order No), maybe CRC is ordering from Kaiser & Kraft?
"Bestelling Nr./Commande No.: 1513/94".
If CRC is ordering from Kaiser & Kraft:
CRC is the buyer. Kaiser & Kraft is the seller.
The table lists items: Table, Chairs, Transport.
Prices are in BF (Belgian Francs).
Total: 17.520.
"Leveringstermijn" (Delivery deadline): 4th week 1994.
"Betalswijze" (Payment method): 30 days end of month.
Signature: J. Van den Bulcke, Management Accountant.
> If CRC is the buyer (ordering goods), this is a **Purchase Order** or a **Request for Quotation** or a **Budget Request**?
Let's look at the "Budget" definition: "internal money planning... a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient... is budget".
"A project-funding authorization/approval form that names the work to be funded... is a form".
"An internal expenditure-authorization form... is a form".
> Let's look at the "Invoice" definition: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD".
If this document is from CRC (buyer) to Kaiser & Kraft (seller), listing items to be bought...
Wait, "Bestelling" means Order.
If this is a Purchase Order (PO), what category is it?
The categories are: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> Is a Purchase Order a "form"? Or "budget"? Or "invoice"?
Usually, a PO is a form. But let's look at the content.
It lists specific items and a total cost.
If it's a request for money/spending: "budget" or "form"?
Check 7 says: "budget: ... a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient ... is budget".
"A project-funding authorization/approval form that names the work to be funded... is a form (check 10)... not budget".
This document names the work (buying a table and chairs) and has an amount.
Is it an authorization? It has a signature "Management Accountant". This looks like an approval.
"J. Van den Bulcke Management Accountant" signed it.
If this is an internal document from CRC's accountant to authorize a purchase from Kaiser & Kraft...
Then it's an internal expenditure authorization.
Check 7 caveat: "an internal expenditure-authorization form (an 'AUTHORIZATION REQUEST' for funds... purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget".
Wait, this document *does* have charges (prices). "5.680,-", "11.040,-".
But the caveat says: "names the work/project to be funded... and carries an approval signature... but no billable charges is a form". Here there are prices.
However, if this is a Purchase Order (request to buy), it's not a bill *from* a vendor.
If this is a document *from* CRC *to* Kaiser & Kraft saying "We order these items for this price", it's a Purchase Order.
Purchase orders are often classified as **form** (administrative) or **budget** (if it's a request for funds).
> Let's reconsider the sender/receiver.
Header: CRC CONTRACT RESEARCH CENTER.
Addressed to: Kaiser & Kraft.
If CRC is the sender, and they are sending a "Bestelling" (Order) to Kaiser & Kraft...
Actually, in business, a "Bestelling" is an order.
If CRC orders from Kaiser & Kraft, CRC is the buyer.
The document lists what CRC wants to buy and the price (agreed price?).
"Leveringstermijn" (Delivery time).
"Betalswijze" (Payment terms).
This looks like a Purchase Order (PO) or a Purchase Agreement.
> How to classify a Purchase Order?
- Is it an invoice? No, it's not a bill *from* a vendor stating charges owed. It's a request *from* a buyer. (Unless it's a proforma invoice, but "Bestelling" means Order).
- Is it a budget? "internal money planning, tracking, or disbursement". A PO is a commitment of funds. But Check 7 says "budget" covers "internal money planning...". And "A project-funding authorization... is a form".
- Is it a form? Check 10: "Filled or blank fields... for capturing factual data; an application...". A PO is a form.
> Let's look at the text again: "(Gelieve deze referentie in ieder geval op de factuur te vermelden / veuillez sans exception reproduire cette référence sur la facture)".
Translation: "Please mention this reference in any case on the invoice".
This text is usually on a **Purchase Order** (Bestelling). The buyer (CRC) sends a PO to the seller (Kaiser & Kraft) and says "When you send the invoice, please reference our Order No. 1513/94".
So this document is a **Purchase Order** (Bestelling).
> What category is a Purchase Order?
- Not invoice (it's not the bill).
- Not budget (it's not internal planning/tracking primarily, though it involves money. But Check 7 says money records like "contribution request" are budget. A PO is a request to buy).
- Check 7 caveat: "an internal expenditure-authorization form... is a form (check 10), not budget".
- Check 10: "Administrative form... application...". A purchase order is a form.
> Wait, let's look at the "Invoice" definition again.
"invoice: an outside vendor... states charges owed...". This is not that.
"budget: ... internal money planning...".
Is a Purchase Order a form? Yes.
> Let's look at the signature. "J. Van den Bulcke Management Accountant".
This looks like an approval within CRC.
CRC Management Accountant approves the order to Kaiser & Kraft.
So this is an internal approval document for a purchase.
Check 7: "an internal expenditure-authorization form... that names the work/project to be funded and carries an approval signature/date block... is a form (check 10), not budget".
This fits perfectly. It names the items (work/project: buying furniture), has amounts, and has an approval signature (Management Accountant).
So it is a **form**.
> Wait, let's check Check 7 again.
"Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form..." -> This applies to invoices/budgets.
"Caveat: an internal expenditure-authorization form... is a form (check 10), not budget".
This document is an internal authorization (signed by Management Accountant) for a purchase (Bestelling).
The content is the details of the purchase (items, prices, delivery date, payment terms).
This is a standard "Purchase Requisition" or "Purchase Order Approval" form.
So **form** (Check 10) seems correct.
> Let's double check if it could be an **invoice**.
If this document is from Kaiser & Kraft to CRC?
Header: "CRC CONTRACT RESEARCH CENTER". Usually the top header is the letterhead of the sender.
If CRC is the sender, and the text says "Please mention this reference on the invoice", then CRC is the buyer.
Buyer sends "Bestelling" (Order).
So this is a Purchase Order / Purchase Requisition.
Category: **form**.
> Let's check if there's any other label.
Could it be **budget**?
"budget: ... a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient ... is budget".
This has items and amounts.
"A project-funding authorization/approval form that names the work to be funded... is a form".
This names the work (buying table/chairs) and has an approval block. So it's a form.
> Let's check the labels again.
1. file_folder: No.
2. handwritten: No.
3. FAX: No.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No.
7. financial (invoice/budget):
   - Invoice: No, it's a purchase order (Bestelling), not a vendor bill. The text explicitly references an invoice ("op de factuur").
   - Budget: "internal money planning...". A purchase requisition is a request for money/spending. But the caveat says "internal expenditure-authorization form... is a form". This document has an approval signature ("Management Accountant"). It authorizes the expenditure. So it's a form.
8. specification: No.
9. presentation: No.
10. form: "Filled or blank fields... administrative form... internal authorization/approval forms with an approval signature/date block."
    - This page has fields (Bestelling Nr, Datum, items table, Leveringstermijn, Betalswijze).
    - It has an approval signature (J. Van den Bulcke, Management Accountant).
    - It is an authorization for a purchase.
    - So **form** fits Check 10.
> Let's verify the "Invoice" possibility one more time.
Is it possible that this is an invoice from CRC to Kaiser & Kraft?
Header: CRC.
Addressed to: Kaiser & Kraft.
"Bestelling Nr 1513/94". (Order No).
If CRC is selling to Kaiser & Kraft, and this is the invoice...
Why would it say "Bestelling Nr"? Invoices often reference the customer's order number.
"Gelieve deze referentie in ieder geval op de factuur te vermelden".
If this *is* the invoice, why would it say "mention this on the invoice"? That makes no sense.
Unless... the text is on the *back* or it's a standard text on the PO.
Actually, the text is under "Bestelling Nr./Commande No.: 1513/94".
"(Gelieve deze referentie in ieder geval op de factuur te vermelden...)"
This is definitely text on a **Purchase Order** (Bestelling). The buyer (CRC) tells the seller (Kaiser & Kraft): "When you invoice us, use our Order No. 1513/94".
So this document is the Purchase Order.
> Purchase Order classification:
- Not invoice (not a bill).
- Not budget (not internal tracking/planning primarily, though it involves money. But the specific caveat for authorization forms points to form).
- **form** (Check 10). "internal authorization/approval forms with an approval signature/date block". This is an approval for a purchase.
> Wait, is there a chance it's **budget**?
"budget: ... internal money planning...".
If this is a "Bestelling" (Order) from a company, it's a commitment.
But the rule says: "an internal expenditure-authorization form ... is a form (check 10), not budget".
This document has a signature from a Management Accountant. It's an authorization.
So **form**.
> Let's look at the "form" definition (Check 10).
"Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
This document has:
- Fields: Bestelling Nr, Datum, Address, Items table, Leveringstermijn, Betalswijze.
- Approval signature: J. Van den Bulcke, Management Accountant.
- It captures data about a purchase order.
So it is a **form**.
> One detail: "Money function overrides form layout: a billing or payment page stays financial...".
This page is not a billing page (it's a PO). It's not a payment page (it's an order/authorization).
So the override doesn't apply to make it invoice/budget.
The caveat for budget says authorization forms are **form**.
> So the label is **form**.
> Let's check if it could be **invoice** under a different interpretation.
What if "CRC" is the seller, and "Kaiser & Kraft" is the buyer, and this is a "Factuur" (Invoice) but titled "Bestelling" (Order) by mistake? Unlikely.
What if the text "Gelieve deze referentie..." is a standard footer on all documents from CRC?
If CRC is the seller, and they send an invoice...
Invoice usually has "Factuur Nr." (Invoice No). Here it has "Bestelling Nr." (Order No).
And the text says "mention on the invoice". This confirms this is NOT the invoice.
So it's a Purchase Order (from buyer CRC to seller Kaiser & Kraft) OR a Purchase Requisition (internal).
Given the signature "Management Accountant", it looks like an internal approval document (Purchase Requisition/Authorization) that is also sent to the vendor, or just an internal document.
Actually, "Bestelling Nr" is often used by the buyer.
If CRC is the buyer: CRC (Buyer) -> Kaiser & Kraft (Seller).
CRC sends a PO.
The PO is signed by CRC's Management Accountant (internal approval before sending? or just part of the PO?).
Regardless, a Purchase Order / Purchase Requisition is a **form**.
> Final check:
Check 7 (Financial):
- Invoice: No (not a bill from vendor).
- Budget: No (not internal planning/tracking, it's an authorization/request which is a form per caveat).
Check 10 (Form):
- Yes, it has fields, table, and approval signature. It's an administrative document for a purchase order/authorization.
> Label: **form**.
> Wait, let's look at the "budget" definition again.
"budget: ... a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient ... is budget".
This has items and amounts.
"A project-funding authorization/approval form that names the work to be funded... is a form".
This names the work (furniture purchase) and has approval. So **form**.
> One more check: Is it a **specification**?
"Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables... tolerances... 'shall/must'".
No. The table describes a table and chairs for sale, not technical specs.
> So **form** is the best fit.
> Evidence for form (Check 10):
- Structured fields: "Bestelling Nr./Commande No.", "Datum/Date", address fields.
- Table with headers: "POSITIE", "HOEVEELHEID", "EENHEID", "ARTIKELOMSCHRIJVING", "PRIJS".
- Approval block: Signature of "J. Van den Bulcke Management Accountant".
- Function: Purchase order / authorization for expenditure (Check 7 caveat: internal expenditure-authorization form is a form).
> Runner-up: invoice. Ruled out because the document references an invoice ("op de factuur te vermelden") and is titled "Bestelling Nr" (Order No), indicating it is a purchase order/authorization, not a vendor bill. Also, the signature is an internal accountant approval, typical of a requisition/authorization form.
> Wait, is there any chance it's **invoice**?
If the text "Gelieve deze referentie..." is on the invoice? No, that's boilerplate on a PO.
If this is a "Proforma Invoice"?
Even if it's a proforma invoice, it's often classified as a form or invoice.
But the explicit text "mention on the invoice" makes it a PO.
And POs are forms.
> Let's assume the label is **form**.
> One detail: "CRC CONTRACT RESEARCH CENTER".
Maybe this is a report? No.
> Final decision: **form**.
> Wait, looking closely at the image...
The text "Bestelling Nr./Commande No.: 1513/94" is followed by the note about the invoice.
The table has "TOTAAL: 17.520,-".
"Leveringstermijn... 4'de week 1994".
"Betalswijze... 30 dagen einde maand".
This is a Purchase Order (Bestelling).
In the 16 categories, Purchase Order falls under **form** (administrative form for data capture/approval).
> Check 10: "internal authorization/approval forms with an approval signature/date block".
This has "Management Accountant" signature.
So **form**.
> One distinct possibility: Is it a **budget**?
"budget: ... internal money planning...".
If this is a request for budget approval...
But the caveat says: "an internal expenditure-authorization form ... is a form (check 10), not budget".
This is exactly that.
> So **form**.
> <scratchpad>
file_folder: no — page has substantial content (table, addresses, totals), not just an ID.
handwritten: no — mostly typed, only signature and marginal notes.
fax: no — "TELEFAX" is contact info, no fax transmission header block.
questionnaire: no — no survey items.
resume: no.
scientific_publication: no — no journal header.
financial (invoice/budget):
- Invoice: No — text says "Gelieve deze referentie in ieder geval op de factuur te vermelden" (Please mention this reference on the invoice), implying this is not the invoice. It is titled "Bestelling Nr" (Order No). It is a purchase order/authorization.
- Budget: No — Check 7 caveat says "internal expenditure-authorization form... is a form (check 10), not budget". This document has an approval signature ("Management Accountant") authorizing a purchase (work/project: buying table/chairs).
specification: no — table lists commercial items (table, chairs) with prices, not technical specs/tolerances.
presentation: no.
form: yes — Check 10. "Filled or blank fields... internal authorization/approval forms with an approval signature/date block." The page has structured fields (Order No, Date, Address), a data table (items, quantities, prices), delivery terms, payment terms, and an approval signature from a Management Accountant. It is a purchase order/authorization form.
news_article: no.
scientific_report: no.
advertisement: no.
> Runner-up: invoice. Ruled out because the document text explicitly references an invoice ("op de factuur te vermelden") and is titled "Bestelling Nr" (Order No), identifying it as a purchase order or authorization document rather than a vendor bill. The signature of a Management Accountant indicates internal authorization, which Check 7 routes to form.
</scratchpad>
<label>form</label>

---
### `rvl_cdip__invoice__0010.png`
**Expected:** `invoice` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** I see "FedEx. USA Airbill", "Tracking Number 5950842936", "SNA32 Sender's Copy". No "From/To/Sent/Subject" mail headers. There is a "From" and "To" section, but it's part of the FedEx form fields (Sender's Name, Company, Address, etc.). This is a FedEx Airbill.
- **Masthead/Running head:** No newspaper masthead. No journal running head. There is a Bates number "T11717-1860" at the bottom right.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a lot of content (FedEx Airbill form fields, text, checkboxes). It's not just an ID or stamp.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: There is some handwriting (signatures, filled-in fields like names and addresses), but the majority is a printed form template. The handwriting fills the fields of a printed structured form.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE TRANSMISSION" header. It's a FedEx Airbill.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
    *   Evidence: No survey questions.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY**
    *   Evidence: No CV/Resume content.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE**
    *   Evidence: No journal name/volume/issue.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: This is a FedEx USA Airbill.
    *   Let's look at the details.
    *   "FedEx. USA Airbill"
    *   "Sender's Name: DAVID M. HORAZDOVSKY", "Company: THE TOBACCO INSTITUTE".
    *   "Recipient Name: Jeremiah D. Murphy", "Company: BOYCE, MURPHY, MCDOWELL & GREENFIELD".
    *   "Total Packages: 1", "Total Weight: 8 oz", "Total Declared Value: $1.00".
    *   "Payment: [X] Sender".
    *   This is a shipping document / bill of lading / airbill.
    *   Wait, is it an invoice? Or a budget? Or a form?
    *   Let's re-read the definitions.
    *   **Invoice:** "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher... a receipt... a payment request... an agency/vendor ESTIMATE document".
    *   **Budget:** "internal money planning... expense reports... statement of account... check face or check stub... check/payment register". "Also covers money-only records...". "A provider's periodic customer statement... is budget, not invoice".
    *   **Form:** "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
    *   Let's look at the FedEx Airbill. It's a shipping document. It records a shipment.
    *   Is it an invoice? A FedEx airbill is a shipping receipt/contract. It's not a bill for goods sold in the traditional sense, but it is a document used for shipping.
    *   Wait, look at Check 7 again. "invoice: ... a receipt, a payment request...". A FedEx airbill is a shipping document.
    *   Let's look at Check 10: "ADMINISTRATIVE FORM". "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This is definitely a filled form (FedEx Airbill).
    *   Is there a financial category that fits better?
    *   The FedEx Airbill captures shipping data (From, To, Packages, Weight, Payment method).
    *   It's not an invoice for goods sold (though shipping is a service). A FedEx bill (invoice) would come later. This is the "Sender's Copy" of the Airbill, used to initiate the shipment. It's a shipping form.
    *   Let's check the budget definition: "internal money planning... expense reports". This is a record of a shipment.
    *   Let's check the invoice definition: "an outside vendor... states charges owed". This document doesn't state charges owed (except maybe the $1.00 declared value, but payment is "Sender"). It's a shipping instruction/receipt.
    *   So it's likely a **form** (Check 10). It's a filled FedEx Airbill form.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: No MSDS, no product formulation.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK...**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: "FedEx. USA Airbill". Fields for From, To, Company, Address, City, State, Zip. Checkboxes for service type (Express Package, Express Freight, Packaging, Special Handling, Payment). "Total Packages 1", "Total Weight 8 oz". Signature block.
    *   This is a classic administrative form capturing factual data (shipping details).
    *   Result: **form**.
> *   **Check 11: CORRESPONDENCE**
    *   Evidence: No memo/letter structure.
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
> **Re-evaluating Check 7 (Financial) vs Check 10 (Form):**
The document is a FedEx Airbill.
- Is it an invoice? An invoice bills for goods/services. A FedEx Airbill is a shipping contract/receipt. Sometimes FedEx bills are called invoices, but this is the "Sender's Copy" of the Airbill (the shipping label/instruction). It records the shipment. The payment section has "Sender" checked. It doesn't list a charge amount due (except declared value $1.00). It's a shipping form.
- Is it a budget? No.
- Is it a form? Yes. Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This fits perfectly. It's a filled FedEx Airbill.
> Wait, is there any other category?
The document is a "FedEx USA Airbill".
It has fields: From, To, Company, Address, City, State, Zip.
It has checkboxes: Express Package Service, Express Freight Service, Packaging, Special Handling, Payment.
It has data: 1 package, 8 oz, $1.00 declared value.
It has a signature.
This is a shipping form. Shipping forms are administrative forms.
> Let's look at the "invoice" definition again. "a receipt, a payment request". A FedEx airbill is a receipt of the package for shipping. But usually, "invoice" in these datasets refers to a bill for money.
However, look at the budget definition: "check face or check stub... check/payment register".
Look at the form definition: "application... records-management inventory... QA/parameter review sheet... standalone labeled data chart... filled analytical or lab data sheet... internal authorization/approval forms".
The FedEx Airbill is a form used to capture shipping data.
> Let's check if there's a specific "shipping document" category. No.
The categories are: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> If I have to choose between form and invoice/budget.
- Invoice: "an outside vendor... states charges owed". FedEx is a vendor. Does this document state charges owed? "Total Declared Value $1.00". Payment is "Sender". It doesn't show a charge amount like "$15.00 shipping". It's the shipping instruction. The invoice would come later. This is the Airbill (shipping label/contract).
- Form: "Filled or blank fields... for capturing factual data". This is exactly what it is. A filled FedEx Airbill.
> So, **form** is the best fit.
> Let's double check Check 7 caveats.
"A check face/check stub... is the DISBURSEMENT instrument and stays budget". This is not a check.
"A hotel/motel guest bill... is an invoice". This is not a hotel bill.
"landlord's rent/lease statement... is an invoice". No.
"provider's periodic customer statement... is budget". No.
> The FedEx Airbill is a form. Specifically, a shipping form.
Check 10 covers "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
The page is a FedEx Airbill with filled fields (David Horazdovsky, The Tobacco Institute, Jeremiah Murphy, Boyce Murphy..., addresses) and checked boxes (FedEx Standard Overnight, Sender payment).
> Therefore, the label is **form**.
> Wait, let's look at the "invoice" definition again. "a payment voucher... a receipt".
Is a FedEx Airbill a receipt? It's a "Sender's Copy". It serves as a receipt for the sender that the package was handed over.
But functionally, in document classification, a filled-out shipping form is usually a form.
Let's look at the "budget" definition. "expense reports". An expense report might include a receipt. This is just the shipping document.
If this is part of an expense report, it might be budget. But the page itself is just the FedEx Airbill.
The FedEx Airbill captures data: Who sent it, who received it, what's in it, how it's paid. It's a form.
> Let's consider if it's an **invoice**.
Some datasets classify shipping invoices as invoices. But this is the "Airbill" (the shipping contract/label), not the "Invoice" (the bill for shipping costs). The Airbill has "Total Declared Value $1.00". It doesn't have a "Total Due" or "Shipping Cost" line item that is filled in (the box for shipping cost is empty or not prominent, actually looking closely at section 7 Payment: "Bill To: [X] Sender". "FedEx Account No...". "Total Packages 1", "Total Weight 8 oz", "Total Declared Value $1.00". There is no "Charge" column filled with a dollar amount for shipping. The $1.00 is declared value.
So it's not billing money. It's recording a shipment.
So it's a **form**.
> Final check:
- Check 1: file_folder. No, has content.
- Check 2: handwritten. No, mostly printed form.
- Check 3: Fax. No.
- Check 4: Questionnaire. No.
- Check 5: Resume. No.
- Check 6: Publication. No.
- Check 7: Financial. No, not a bill for goods/services (no shipping cost listed, just declared value). Not a budget (not internal planning).
- Check 8: Specification. No.
- Check 9: Presentation. No.
- Check 10: Form. Yes, FedEx Airbill with filled fields and checkboxes.
- Check 11: Correspondence. No.
- Check 12: News. No.
- Check 13: Scientific report. No.
- Check 14: Advertisement. No.
> The label is **form**.
> One detail: "The World On Time" is the FedEx slogan at the bottom. "T11717-1860" is the Bates number.
The document is a filled FedEx USA Airbill.
Function: Capturing shipping data (From, To, contents, payment method).
Category: form.
> Wait, is there any chance it's an **invoice**?
"invoice: ... a receipt ...".
If I buy something and get a receipt, is it an invoice?
In accounting, a receipt confirms payment. An invoice requests payment.
This is a shipping document.
In the tobacco archive context, shipping documents (bills of lading, airbills) are often classified as forms or sometimes invoices if they are the bill.
Here, it's the "Sender's Copy" of the Airbill. It's the shipping instruction.
The definition of form (Check 10) is broad: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This fits perfectly.
> Let's look at the "budget" definition again.
"money-only records... financial or money-data table".
This has money data ($1.00 declared value), but it's not money-only. It has addresses, names, weights.
So it's not budget.
> Conclusion: **form**.
> One more check. Could it be **file_folder**?
"A page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content".
This page has a Bates number (T11717-1860) and a lot of content (the form). So not file_folder.
> Could it be **handwritten**?
"Most of the content is freeform handwriting... NOT on a printed template."
This is on a printed template (FedEx Airbill). The handwriting fills the fields. So not handwritten.
> So **form** is the correct label.
> Scratchpad summary:
- Pre-scan: FedEx header, not mail client. Bates number T11717-1860. No masthead.
- Check 1: file_folder. No, page has full form content.
- Check 2: handwritten. No, printed form with filled fields.
- Check 3: Fax. No.
- Check 4: Questionnaire. No.
- Check 5: Resume. No.
- Check 6: Publication. No.
- Check 7: Financial. No, it's a shipping airbill (Sender's copy), not a bill for charges (no shipping cost listed, just declared value). It captures shipping data.
- Check 8: Specification. No.
- Check 9: Presentation. No.
- Check 10: Form. Yes, FedEx USA Airbill with filled fields (From/To/Address) and checkboxes (Service type, Payment). Captures factual shipping data.
- Check 11: Correspondence. No.
- Check 12: News. No.
- Check 13: Scientific report. No.
- Check 14: Advertisement. No.
> Runner-up: invoice. Ruled out because the document is a shipping airbill (Sender's copy) recording a shipment (From/To/Packages/Weight) rather than a vendor bill stating charges owed for goods/services (no shipping cost line item, just declared value and payment method "Sender"). The primary function is data capture for shipping (form), not billing.
> Actually, looking very closely at the bottom right: "Total Declared Value $1.00".
Section 7 Payment: "Bill To: [X] Sender".
There is no "Total Charge" or "Shipping Cost" filled in.
This confirms it's the shipping instruction/receipt (Airbill), not the invoice (bill).
So **form** is definitely correct.
> One final check on Check 10 text: "A filled analytical or lab data sheet... and internal authorization/approval forms with an approval signature/date block."
This is a filled form with a signature block (Section 8 Release Shipment).
It fits perfectly.
> Final Label: form.

---

## invoice → budget (2 errors)

### `rvl_cdip__invoice__0001.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject". There is a date/time "06/12/96 02:56 PM" and a code "TPS025UN", but this looks like a system printout, not an email header. Wait, let's look closer. "TEMPORARY PAYMENT SYSTEM DISPLAY VOUCHER INFORMATION". No email headers.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a Bates number "51818 2970" at the bottom right.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has "TEMPORARY PAYMENT SYSTEM DISPLAY VOUCHER INFORMATION", account numbers, payee info, amounts. It has real content. Not file_folder.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: There is a handwritten note "NATIONAL APRIL" with a signature/date scribble. But the majority of the content is typed system output (account info, payee, amounts, instructions).
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header. The date/time is system-generated.
    *   Result: not this check.
> *   **Check 4: questionnaire**
    *   Evidence: No survey questions.
    *   Result: not this check.
> *   **Check 5: resume**
    *   Evidence: No career history.
    *   Result: not this check.
> *   **Check 6: scientific_publication**
    *   Evidence: No journal header.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: "TEMPORARY PAYMENT SYSTEM DISPLAY VOUCHER INFORMATION".
    *   "ACCOUNT: 768840", "PAYEE: KENNEDY WHOLESALE".
    *   "TOTAL AMOUNT DUE: 126.00".
    *   "PAY BY VOUCHER", "SEND CHECK TO: PAYEE".
    *   "VOUCHER NUMBER ASSIGNED: 1531396".
    *   "PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS".
    *   "CHECK STUB:".
    *   "PAYMENT REPORT WILL PRINT AT DESTINATION: 54XX".
    *   "PRESS PF1 TO RETURN TO TEMPORARY PAYMENT SELECTION MENU".
    *   This looks like a check stub or a payment voucher display.
    *   Let's check the definitions in Check 7.
    *   **invoice**: "A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee for named goods/services/charges — invoice". Wait. "A payment VOUCHER naming a payee... is a payment instrument... invoice".
    *   **budget**: "A check face/check stub — a check number, bank, MICR line, "PAY TO THE ORDER OF", signature line, or detachable stub — is the DISBURSEMENT instrument and stays budget".
    *   Let's look closely at the text. "CHECK STUB:" is printed on the page. "PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS CHECK STUB:".
    *   The page is a "DISPLAY VOUCHER INFORMATION" screen printout. It says "PRESS PF1 TO RETURN TO TEMPORARY PAYMENT SELECTION MENU". This is a computer screen printout.
    *   It lists "TOTAL AMOUNT DUE: 126.00".
    *   It says "SEND CHECK TO: PAYEE X DIV OFFICE".
    *   It mentions "CHECK STUB".
    *   Is it an invoice or a budget?
    *   The definition for **budget** says: "A check face/check stub ... is the DISBURSEMENT instrument and stays budget".
    *   The definition for **invoice** says: "A payment VOUCHER naming a payee, vendor/item fields, an amount ... and a payment date is a payment instrument that BILLS a named payee ... invoice".
    *   Wait, let's re-read carefully.
    *   "A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee for named goods/services/charges — invoice, whether it pays a vendor for goods/services or a grantee/recipient (e.g. a contribution payment for a grant). It is not the budget clause for an INTERNAL REQUEST/CHECKLIST/STATEMENT form requesting that money be spent or contributed."
    *   "Also covers money-only records: ... a check face or check stub ... is budget". Wait. "A check face/check stub ... is the DISBURSEMENT instrument and stays budget".
    *   Let's look at the text again. "CHECK STUB:" is a label. The text below it is empty? No, "PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS" is above "CHECK STUB:".
    *   Actually, the text "PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS CHECK STUB:" seems to be a header for a section that isn't fully filled out or is describing what the check stub is for.
    *   The page is a "DISPLAY VOUCHER INFORMATION" screen.
    *   Let's look at the "invoice" bullet: "A payment VOUCHER naming a payee... is a payment instrument... invoice".
    *   Let's look at the "budget" bullet: "A check face/check stub ... is the DISBURSEMENT instrument and stays budget".
    *   This page is a "DISPLAY VOUCHER INFORMATION". It shows a voucher number (1531396). It shows a total amount due (126.00). It says "PAY BY VOUCHER".
    *   Is this a voucher that bills someone? Or a check stub?
    *   The text says "CHECK STUB:" followed by blank space, then "PAYMENT REPORT WILL PRINT...".
    *   Actually, looking at the layout:
        *   "PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS"
        *   "CHECK STUB:"
    *   This looks like a screen printout of a payment system.
    *   Let's re-evaluate "invoice" vs "budget".
    *   Invoice: "an outside vendor... states charges owed". Here, "PAYEE: KENNEDY WHOLESALE". "TOTAL AMOUNT DUE: 126.00". "PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS". This looks like a payment to Kennedy Wholesale for displays.
    *   Is it a bill from Kennedy Wholesale? No, it's an internal system ("TEMPORARY PAYMENT SYSTEM") showing a payment *to* Kennedy Wholesale.
    *   "SEND CHECK TO: PAYEE". This is an internal instruction to send a check.
    *   So this is an internal disbursement record.
    *   Budget definition: "internal money planning, tracking, or disbursement... check face or check stub... is budget".
    *   This is a record of a payment/disbursement (voucher info). It's tracking a payment.
    *   Wait, let's look at the "invoice" definition again. "A payment VOUCHER naming a payee... is a payment instrument that BILLS a named payee... invoice".
    *   But this is a "DISPLAY VOUCHER INFORMATION" screen. It's not the voucher itself sent to the payee, it's the system display.
    *   However, let's look at the "budget" definition: "A check face/check stub... is the DISBURSEMENT instrument and stays budget".
    *   The text explicitly says "CHECK STUB:".
    *   Also, "PAYMENT REPORT WILL PRINT AT DESTINATION". This is a system printout.
    *   Let's look at the "form" check (Check 10). "Filled or blank fields... for capturing factual data". This is a system printout, essentially a form/screen capture.
    *   But Check 7 says: "Money function overrides form layout... budget: internal money planning, tracking, or disbursement... check face or check stub... is budget".
    *   This page is a "DISPLAY VOUCHER INFORMATION". It records a payment of $126.00 to Kennedy Wholesale.
    *   Is it an invoice? An invoice is usually from a vendor. This is from "TEMPORARY PAYMENT SYSTEM". It's an internal record.
    *   Is it a budget? "internal money planning, tracking, or disbursement". Yes, this is tracking/disbursement.
    *   Specifically, "check face or check stub... is budget". The text says "CHECK STUB:". Even though the stub content is sparse ("PAYMENT INFO FOR..."), the page is labeled as voucher info/check stub info.
    *   Let's look at the "invoice" caveat: "It is not the budget clause for an INTERNAL REQUEST/CHECKLIST/STATEMENT form requesting that money be spent or contributed." This is a payment display, not a request.
    *   Let's look at the "budget" bullet: "Also covers money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient... is budget". This has amount (126.00) and recipient (Kennedy Wholesale).
    *   Wait, "PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS". This is an expenditure.
    *   So it's a record of an expenditure.
    *   Let's check Check 10 (Form). "administrative form... filled or blank fields". This is a system printout with fields. But Check 7 says money function overrides.
    *   So it's either invoice or budget.
    *   Invoice: "outside vendor... states charges owed". This page is internal ("TEMPORARY PAYMENT SYSTEM", "ACCT. DIVISION: 5426"). It's not an outside vendor stating charges. It's the company's system showing a payment to be made.
    *   Budget: "internal money... disbursement... check stub". This fits perfectly. It's an internal record of a disbursement (voucher/check stub info).
> *   **Check 8: specification**
    *   Evidence: No product data, MSDS, etc.
    *   Result: not this check.
> *   **Check 9: presentation**
    *   Evidence: No slide layout.
    *   Result: not this check.
> *   **Check 10: form**
    *   Evidence: It has fields (Account, Payee, Total Amount Due). But Check 7 (Financial) takes precedence for money content. "Money function overrides form layout".
    *   Result: not this check (because Check 7 applies). Wait, if Check 7 doesn't apply (i.e., not invoice/budget), then it's form. But it is financial.
> *   **Check 11: correspondence**
    *   Evidence: No memo/letter structure.
    *   Result: not this check.
> *   **Check 12: news_article**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 13: scientific_report**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 14: advertisement**
    *   Evidence: No.
    *   Result: not this check.
> **Re-evaluating Check 7 (Financial Document):**
The page is "TEMPORARY PAYMENT SYSTEM DISPLAY VOUCHER INFORMATION".
It shows:
- Account: 768840
- Payee: Kennedy Wholesale
- Total Amount Due: 126.00
- Voucher Number: 1531396
- Payment Info: April National Promotion 45 Displays.
- "CHECK STUB:" label.
- Handwritten note "NATIONAL APRIL".
> This is a record of a payment.
Is it an invoice?
- Invoice: "an outside vendor... states charges owed". No, this is internal.
- Invoice: "A payment VOUCHER naming a payee... is a payment instrument that BILLS a named payee". A voucher *is* a payment instrument. But usually a voucher is the internal document authorizing payment, while the check is the payment.
- The text says "SEND CHECK TO: PAYEE". So the check hasn't been sent or is being prepared.
- The text says "CHECK STUB:". This implies this page *is* or represents the check stub.
- Budget definition: "A check face/check stub ... is the DISBURSEMENT instrument and stays budget".
- Budget definition: "internal money planning, tracking, or disbursement". This is tracking a disbursement.
> So **budget** seems the best fit.
> Let's look at the "invoice" definition again. "A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee for named goods/services/charges — invoice".
This is tricky. "A payment VOUCHER... is a payment instrument that BILLS a named payee... invoice".
If this page is a "Voucher Information" display, is it the voucher itself?
The title is "DISPLAY VOUCHER INFORMATION".
It says "VOUCHER NUMBER ASSIGNED: 1531396".
It says "PAY BY VOUCHER".
It says "SEND CHECK TO: PAYEE".
This looks like the screen where you set up a payment.
The "CHECK STUB:" section is likely where the check stub details would go, or this page *is* the check stub printout.
Actually, "CHECK STUB:" is followed by blank space, then "PAYMENT REPORT WILL PRINT...".
Wait, "PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS" is above "CHECK STUB:".
Maybe the "CHECK STUB" is the text "PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS"?
Regardless, it's an internal financial record.
> Let's look at the "budget" bullet: "Also covers money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient... is budget".
This page has Amount (126.00) and Recipient (Kennedy Wholesale) and Description (April National Promotion 45 Displays).
It is a statement of a payment/expenditure.
So **budget** fits well.
> Let's check if it could be **form**.
Check 10: "administrative form... filled or blank fields".
Check 7: "Money function overrides form layout... budget: internal money planning, tracking, or disbursement... check face or check stub... is budget".
Since it's a financial record (check stub/voucher info), Check 7 applies.
Between invoice and budget:
- Invoice is for "outside vendor... states charges owed". This is internal (Account Division 5426, Temporary Payment System). It's not a bill from Kennedy Wholesale. It's the company's record of paying Kennedy Wholesale.
- Budget is "internal money... disbursement... check stub". This fits.
> So the label is **budget**.
> Wait, let's look at the handwritten note. "NATIONAL APRIL" with a signature.
Check 2: "Most of the content is freeform handwriting...". No, most is typed.
Check 2 caveat: "Handwriting filling in labeled printed fields is form". Here, the handwriting is a note "NATIONAL APRIL" next to the typed text. It doesn't fill a field. But the majority is typed. So not handwritten.
> Final decision: **budget**.
> One detail: "A payment VOUCHER naming a payee... is a payment instrument that BILLS a named payee... invoice".
If this document is considered a "Payment Voucher" (it says "DISPLAY VOUCHER INFORMATION", "VOUCHER NUMBER ASSIGNED"), does it bill the payee?
Usually, a voucher is an internal document. The check is sent to the payee.
The text says "SEND CHECK TO: PAYEE". So the check is the instrument sent to the payee.
The voucher is the internal authorization.
The definition says: "A payment VOUCHER naming a payee... is a payment instrument that BILLS a named payee... invoice". This is confusing. Let's re-read carefully.
"A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee for named goods/services/charges — invoice, whether it pays a vendor for goods/services or a grantee/recipient (e.g. a contribution payment for a grant). It is not the budget clause for an INTERNAL REQUEST/CHECKLIST/STATEMENT form requesting that money be spent or contributed."
> This suggests that if it's a voucher that pays a vendor, it's an invoice?
"A payment VOUCHER... is a payment instrument that BILLS a named payee... invoice".
But then: "A check face/check stub ... is the DISBURSEMENT instrument and stays budget".
And: "It is not the budget clause for an INTERNAL REQUEST...".
> Let's look at the content again.
"TEMPORARY PAYMENT SYSTEM DISPLAY VOUCHER INFORMATION"
"TOTAL AMOUNT DUE: 126.00"
"PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS"
"CHECK STUB:"
> This looks like a printout of a check stub or a voucher record.
If it's a "Check Stub", it's **budget**.
The text explicitly says "CHECK STUB:".
Even if the stub content is minimal, the label is there.
Also, the "Payment Report will print..." suggests this is a system output for tracking.
Internal tracking of disbursement = budget.
> Let's consider **form** (Check 10).
If it's not invoice or budget.
But Check 7 says money function overrides.
Is this money function? Yes, "Total Amount Due: 126.00", "Payee: Kennedy Wholesale".
So it must be invoice or budget.
Since it's internal (Account Division, Temporary Payment System) and looks like a check stub/record, it's **budget**.
> One more check: Is it a **specification**? No.
Is it a **presentation**? No.
> The handwritten note "NATIONAL APRIL" is just a note.
> Final classification: **budget**.
> Wait, let's look at the "invoice" definition again.
"an outside vendor, supplier, or agency states charges owed... invoice".
This is not an outside vendor stating charges. This is the company's system.
"A payment VOUCHER... is a payment instrument that BILLS a named payee... invoice".
Does this voucher bill Kennedy Wholesale?
"PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS".
It's paying for displays. Kennedy Wholesale is likely the vendor.
So the company is paying Kennedy Wholesale.
Is this document the bill from Kennedy Wholesale? No.
Is this document the company's record of payment (voucher/check stub)? Yes.
The definition says "A payment VOUCHER... is a payment instrument that BILLS a named payee... invoice". This implies the voucher *is* the billing instrument?
Actually, in accounting, a voucher is internal. A check is external.
But the text says "A payment VOUCHER... is a payment instrument that BILLS a named payee... invoice". This is a specific rule in the prompt.
Let's read it very carefully: "A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee for named goods/services/charges — invoice".
If this page is a "Voucher", then by this specific rule, it is an **invoice**.
BUT, the page also says "CHECK STUB:".
And the budget rule says: "A check face/check stub ... is the DISBURSEMENT instrument and stays budget".
> Conflict:
- Voucher rule -> invoice.
- Check stub rule -> budget.
> Which one wins?
The page title is "DISPLAY VOUCHER INFORMATION".
It contains "VOUCHER NUMBER ASSIGNED".
It contains "CHECK STUB:" label.
Usually, a check stub is part of the check (budget). A voucher is the authorization (often internal).
The prompt says: "A payment VOUCHER naming a payee... is a payment instrument that BILLS a named payee... invoice".
This seems to classify internal vouchers that pay vendors as invoices?
"It is not the budget clause for an INTERNAL REQUEST/CHECKLIST/STATEMENT form requesting that money be spent or contributed." -> This distinguishes it from a request form.
So a voucher that actually pays (names amount, payee) is an invoice?
> Let's look at the "budget" definition again.
"budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register..."
"A check face/check stub ... is the DISBURSEMENT instrument and stays budget".
> The page has "CHECK STUB:" printed on it.
"PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS CHECK STUB:"
This looks like the text for the check stub.
If the page *is* the check stub (or the display of it), then it's **budget**.
> Let's look at the "invoice" caveat: "A hotel/motel guest bill... is an invoice". "A landlord's rent/lease statement... is an invoice".
"Also a provider's periodic customer statement... is budget, not invoice — it is a statement of charges for an ongoing account".
> This page: "TEMPORARY PAYMENT SYSTEM". "ACCOUNT: 768840". "ACCT. DIVISION: 5426".
This is an internal system.
"TOTAL AMOUNT DUE: 126.00".
"TOTAL PAYMENT ITEMS: 2".
"PAY BY VOUCHER".
"SEND CHECK TO: PAYEE".
This is a screen printout of a payment setup.
It is not a bill from a vendor (invoice).
It is not a check stub sent to a vendor.
It is an internal record of a disbursement.
"internal money... tracking, or disbursement... is budget".
> The "payment voucher" rule for invoice seems to apply to a document that *is* the voucher sent to the payee or acts as the bill. Here, it's a "DISPLAY VOUCHER INFORMATION" from a "TEMPORARY PAYMENT SYSTEM". It's a system printout.
The text "CHECK STUB:" suggests this is the stub side of the check or a record of the check stub.
Given "CHECK STUB:" is explicitly printed, and budget covers "check face or check stub", I will go with **budget**.
> Also, the handwritten note "NATIONAL APRIL" is on a budget/financial document.
> Let's reconsider **form**.
Check 10: "administrative form... filled or blank fields".
This is a system printout with fields.
But Check 7: "Money function overrides form layout".
So it's financial.
> Is it **invoice**?
"A payment VOUCHER naming a payee... is a payment instrument that BILLS a named payee... invoice".
If I treat this as a "Payment Voucher" (it has Voucher Number), then it's invoice.
But the content is "DISPLAY VOUCHER INFORMATION" from a computer system.
And it says "CHECK STUB:".
And "PRESS PF1 TO RETURN...". This is a computer screen printout.
Computer screen printouts of financial data are often records/logs.
"internal money... tracking... is budget".
This is tracking a payment.
> I'll stick with **budget**.
> One distinct feature: "CHECK STUB:".
Budget definition: "a check face or check stub... is budget".
> Final check:
Label: budget.
Evidence: "TEMPORARY PAYMENT SYSTEM", "TOTAL AMOUNT DUE: 126.00", "PAYEE: KENNEDY WHOLESALE", "CHECK STUB:" label. Internal disbursement record.
> Wait, is there any chance it's **form**?
If the financial content is just "mentioned", it's form.
But here, the *primary structure* is financial data (Account, Payee, Amount, Voucher #).
Check 7: "Check 7 applies only when financial content IS the page's primary structure". Yes, it is.
> So it's budget.
> One detail: "A payment VOUCHER naming a payee... is a payment instrument that BILLS a named payee... invoice".
If this is a voucher, is it billing the payee?
"PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS".
It's paying for displays.
If Kennedy Wholesale is the vendor, they are being paid.
The document is the company's record.
The rule "A payment VOUCHER... is a payment instrument that BILLS a named payee... invoice" is confusing.
Usually, a voucher is internal.
But let's look at the "budget" rule: "A check face/check stub... is budget".
The page says "CHECK STUB:".
I will prioritize the explicit "CHECK STUB" label and the internal nature (Account Division, Temporary Payment System) towards budget. The "invoice" rule for vouchers might apply to a physical voucher sent with payment, but this is a system display.
> Actually, looking at the layout:
"PAYMENT INFO FOR APRIL NATIONAL PROMOTION 45 DISPLAYS"
"CHECK STUB:"
This looks like the text that goes on the check stub.
So this page *is* the check stub (or the printout of it).
Therefore -> **budget**.
> <scratchpad>
file_folder: no — page has financial data (account, payee, amount), not just an ID.
handwritten: no — majority is typed system output; only a small handwritten note "NATIONAL APRIL".
fax: no — date/time is system generated, no fax header.
questionnaire: no — no survey items.
resume: no — no career history.
scientific_publication: no — no journal header.
financial (invoice/budget): yes — "TEMPORARY PAYMENT SYSTEM DISPLAY VOUCHER INFORMATION", "ACCOUNT: 768840", "PAYEE: KENNEDY WHOLESALE", "TOTAL AMOUNT DUE: 126.00", "CHECK STUB:" label. This is an internal financial record/disbursement.
specification: no — no product data.
presentation: no — not a slide.
form: no — Check 7 (financial) overrides form layout.
correspondence: no — no memo/letter structure.
news_article: no.
scientific_report: no.
advertisement: no.
> Runner-up: invoice. Ruled out because this is an internal system printout ("TEMPORARY PAYMENT SYSTEM", "ACCT. DIVISION") acting as a check stub/record of disbursement ("CHECK STUB:" label), which falls under budget (internal tracking/disbursement/check stub), rather than an outside vendor stating charges owed (invoice). The "payment voucher" rule for invoice seems to apply to the instrument billing the payee, but this is an internal display/stub. Actually, the budget definition explicitly includes "check face or check stub" and "internal money... disbursement".
> Wait, let's look at the "invoice" rule again: "A payment VOUCHER naming a payee... is a payment instrument that BILLS a named payee... invoice".
If this is a voucher, it's invoice.
But the page says "DISPLAY VOUCHER INFORMATION". It's a display.
And "CHECK STUB:".
And "PRESS PF1 TO RETURN...".
It's a screen printout.
Screen printouts of internal payment systems are typically budget/expense records.
I'll stick with budget.
> One more look at "invoice": "A payment VOUCHER naming a payee, vendor/item fields, an amount... and a payment date is a payment instrument that BILLS a named payee... invoice".
This page has: Payee (Kennedy Wholesale), Amount (126.00), Voucher Number (1531396).
It lacks a specific payment date (only system date 06/12/96).
It says "SEND CHECK TO: PAYEE". So the check is not sent yet.
This is a setup screen.
Internal setup of a payment -> budget (tracking/disbursement).
> Final label: budget.
</scratchpad>
> <label>budget</label>

---
### `rvl_cdip__invoice__0006.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is a fax-like header at the top right: "TUSSENTIJSDE FACTUUR VAN 02/06/93" and a stamp "REGISTE". Wait, let's look closer.
- Top right: "TUSSENTIJSDE FACTUUR VAN 02/06/93". There's a stamp "REGISTE" with a number "066101.1680".
- Bottom right: "2028743021".
- Left side (rotated): "VERREKENING", "DIENSTVERLENING".
- This looks like a rotated document. Let's rotate it mentally 90 degrees clockwise.
- If I rotate 90 degrees clockwise:
    - Top: "VERREKENING" (Reconciliation/Settlement), "DIENSTVERLENING" (Service provision).
    - "BTW: BE222343301", "SAPOTIAZIEL", "BLOKSEL". This is the sender: "EgTV : IVRIEK" (maybe a company name). Wait, "ELECTRADEL N V." is listed under "DIENSTVERLENING".
    - Address: "STEENOKKERZEELST 56, 1930 ZAVENTEM".
    - "VERSTUIKSADRES" (Bill to address): "C R C M WALK A MSA, TOLLAAAN 101C, 1932 S-STEVENS-WOLME".
    - "TUSSENTIJSDE FACTUUR NR 5 (2 MAAND.)" (Interim invoice number 5 for 2 months).
    - "AARDGAS" (Natural gas).
    - "TOTAAL AARDGAS (BTW 19.5%)."
    - "Laatste tussentijdse factuur. De opname zal in 08/93 gebeuren." (Last interim invoice. The reading will happen in 08/93).
    - "STAND VAN UH REKENING" (Status of your account).
    - "TE BETALEN ... 56.431 F" (To be paid ... 56,431 Francs).
    - "Wij vragen de betaling aan uw financiële instelling." (We request payment to your financial institution).
> **2. Scratchpad checks:**
> *   **Check 1: file_folder.** No, there is substantial content (invoice details, addresses, amounts). Not just a Bates number or folder tab.
*   **Check 2: handwritten.** No, mostly typed text. There is a stamp "0 JUNI 1993" and a handwritten "309" or similar, but the content is typed.
*   **Check 3: FAX TRANSMISSION SHEET.** No fax cover sheet header. The "SENT BY" is not present in the standard fax header format (though there is a registration stamp). Wait, let's look at the top right. "TUSSENTIJSDE FACTUUR VAN 02/06/93". There is a stamp "REGISTE". This is a registration stamp, not a fax header.
*   **Check 4: questionnaire.** No.
*   **Check 5: resume.** No.
*   **Check 6: scientific_publication.** No.
*   **Check 7: FINANCIAL DOCUMENT -> invoice or budget.**
    *   The document is titled "TUSSENTIJSDE FACTUUR" (Interim Invoice).
    *   It lists "AARDGAS" (Natural gas) charges.
    *   It has a total amount: "56.431 F".
    *   It says "TE BETALEN" (To be paid).
    *   It is a bill from a supplier (Electradel N.V. / EgTV) for gas services.
    *   Wait, is it an invoice or a budget?
    *   "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a hotel/motel guest bill... a landlord's rent/lease statement... is an invoice".
    *   This is a utility bill (gas). "TUSSENTIJSDE FACTUUR" means interim invoice.
    *   It bills for "AARDGAS" (natural gas) for a period (implied by "2 MAAND" - 2 months).
    *   "Laatste tussentijdse factuur. De opname zal in 08/93 gebeuren." -> Last interim invoice. Reading will be in 08/93. This is a standard utility billing cycle.
    *   Check 7 definition for invoice: "an outside vendor... states charges owed...". Yes.
    *   Check 7 definition for budget: "provider's periodic customer statement... is budget, not invoice — it is a statement of charges for an ongoing account...". Wait.
    *   Let's re-read the budget bullet carefully: "ALSO a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
    *   This is a crucial distinction.
    *   The document is "TUSSENTIJSDE FACTUUR" (Interim Invoice) for "AARDGAS" (Natural Gas).
    *   It is from "ELECTRADEL N V." (a utility company, likely electricity/gas).
    *   It is addressed to "C R C M WALK A MSA" (a company).
    *   It is a periodic bill for gas consumption.
    *   The text says: "Laatste tussentijdse factuur. De opname zal in 08/93 gebeuren." (Last interim invoice. The reading will happen in 08/93). This implies it's part of a billing cycle (interim bills based on estimates, final bill based on reading).
    *   This fits the "provider's periodic customer statement" or "utility or subscription statement" description under **budget**.
    *   Let's check the invoice bullet again: "A hotel/motel guest bill... is an invoice... Likewise a landlord's rent/lease statement for a specific period... is an invoice".
    *   Let's check the budget bullet again: "ALSO a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice".
    *   This is a gas bill (utility statement). "TUSSENTIJSDE FACTUUR" is an interim bill.
    *   Is it a one-off service (invoice) or ongoing account (budget)? Gas supply is an ongoing account. The text "De opname zal in 08/93 gebeuren" confirms it's an interim estimate based on a reading cycle.
    *   So this should be **budget**.
>     *   Wait, let's look closer at the text.
    *   "TUSSENTIJSDE FACTUUR NR 5 (2 MAAND.)" -> Interim invoice No 5 (2 months).
    *   "AARDGAS" -> Natural gas.
    *   "TOTAAL AARDGAS (BTW 19.5%)." -> Total natural gas (VAT 19.5%).
    *   Amount: 56.431 F (Belgian Francs).
    *   This is a utility bill.
    *   Rule: "provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice".
    *   So this is **budget**.
> *   **Check 8: specification.** No.
*   **Check 9: presentation.** No.
*   **Check 10: form.** No, it's a financial document.
*   **Check 11: correspondence.** No.
*   **Check 12: news_article.** No.
*   **Check 13: scientific_report.** No.
*   **Check 14: advertisement.** No.
> **Re-evaluating Check 7 (Invoice vs Budget):**
- **Invoice:** "an outside vendor... states charges owed for goods or services SOLD... It does not have to be titled 'INVOICE'... A hotel/motel guest bill... is an invoice... Likewise a landlord's rent/lease statement for a specific period... is an invoice".
- **Budget:** "ALSO a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T 'MONTHLY INVOICE' for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
> The document is a "TUSSENTIJSDE FACTUUR" (Interim Invoice) for "AARDGAS" (Natural Gas).
It is from a utility company ("ELECTRADEL N V.", "STEENOKKERZEELST 56, 1930 ZAVENTEM" - this is a Belgian address, likely a utility provider).
The recipient is "C R C M WALK A MSA" (Philip Morris USA / R.J. Reynolds? "MSA" might be a division). Address: "1932 S-STEVENS-WOLME" (Sint-Stevens-Woluwe, Brussels).
The text "Laatste tussentijdse factuur. De opname zal in 08/93 gebeuren." means "Last interim invoice. The reading [of the meter] will happen in 08/93."
This is clearly a periodic utility bill (interim billing based on estimates until the final reading).
According to the rules: "a utility or subscription statement) is budget, not invoice".
> So the label is **budget**.
> Let's double check if there's any other interpretation.
Could it be an invoice?
"invoice: ... an agency/vendor estimate or recap that ONLY plans upcoming placements ... is budget ... But an agency estimate report/change order/recap that bills a client job ... is invoice".
This is a utility bill. Utility bills are explicitly listed under budget: "a utility or subscription statement".
> Let's look at the "invoice" examples: "hotel/motel guest bill", "landlord's rent/lease statement". These are specific one-off periods for specific services (lodging, rent). Gas is a continuous utility. The rule explicitly says "utility or subscription statement" is budget.
> So, **budget**.
> Wait, let's look at the document structure.
It has "STAND VAN UH REKENING" (Status of your account).
"TE BETALEN ... 56.431 F".
"Wij vragen de betaling aan uw financiële instelling." (We request payment to your financial institution - direct debit/bank transfer).
This is a standard utility statement.
> Final decision: **budget**.
> Let's check the rotation. The image is rotated 90 degrees counter-clockwise.
If I rotate it 90 degrees clockwise:
- Top left: "VERREKENING" (Reconciliation), "DIENSTVERLENING" (Service provision).
- Sender: "EgTV : IVRIEK" (maybe "EgTV" is a code, "IVRIEK" is a name? Actually "BTW: BE222343301" is the VAT number. "SAPOTIAZIEL" "BLOKSEL". This looks like a company name. "ELECTRADEL N V." is listed under "DIENSTVERLENING". Electradel is a Belgian energy company).
- Bill to: "C R C M WALK A MSA" (R.J. Reynolds / Philip Morris? "Walk" -> maybe a brand or division. "MSA" -> Management Services Association? Actually, in tobacco archives, this is likely a Philip Morris or RJR entity). Address: "TOLLAAAN 101C, 1932 S-STEVENS-WOLME". Woluwe-Saint-Pierre is a municipality in Brussels.
- "TUSSENTIJSDE FACTUUR NR 5 (2 MAAND.)" -> Interim invoice No 5 (2 months).
- "AARDGAS" -> Natural gas.
- "TOTAAL AARDGAS (BTW 19.5%)."
- Total: 56.431 F.
> This is definitely a utility bill (gas).
Rule: "provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice".
> Therefore, **budget**.
> One detail: "TUSSENTIJSDE FACTUUR" literally translates to "Interim Invoice". In Dutch, "Factuur" is Invoice. However, the classification rules override the literal title based on function. The function is a periodic utility statement.
The rule says: "utility or subscription statement) is budget, not invoice".
> So, label: budget.
> Let's check if there is any other possibility.
Could it be a form? No, it's a financial document.
Could it be a letter? No.
> The scratchpad needs to follow the checks.
> Check 1: file_folder. No. Content is substantial.
Check 2: handwritten. No. Typed text with a stamp.
Check 3: Fax. No.
Check 4: Questionnaire. No.
Check 5: Resume. No.
Check 6: Scientific publication. No.
Check 7: Financial document.
- Evidence: "TUSSENTIJSDE FACTUUR" (Interim Invoice), "AARDGAS" (Natural Gas), "TE BETALEN" (To be paid), amount "56.431 F". Vendor "ELECTRADEL N V." (utility company). Recipient "C R C M WALK A MSA". Text "Laatste tussentijdse factuur. De opname zal in 08/93 gebeuren." (Last interim invoice, reading in 08/93).
- This is a utility statement (periodic customer statement).
- Rule: "provider's periodic customer statement: ... a utility or subscription statement) is budget, not invoice".
- So, budget.
> Runner-up: invoice. Ruled out because this is a periodic utility statement (gas bill) for an ongoing account, explicitly categorized as budget in the instructions ("utility or subscription statement"), whereas invoice is for goods sold or one-off services (like a hotel bill or landlord rent for a specific period, though rent is tricky, the utility example is explicit). Wait, the rule says "landlord's rent/lease statement for a specific period ... is an invoice". But gas is a utility. The rule says "utility or subscription statement ... is budget".
> Let's refine the runner-up.
Runner-up: invoice. Ruled out because the document is a periodic utility statement ("AARDGAS", "tussentijdse factuur" for 2 months, meter reading scheduled for later), which falls under the budget category for "provider's periodic customer statement... utility or subscription statement".
> Final check of the text: "TUSSENTIJSDE FACTUUR NR 5 (2 MAAND.)". Invoice number 5 for 2 months. This is a recurring bill.
> Label: budget.

---

## questionnaire → presentation (1 errors)

### `rvl_cdip__questionnaire__0002.png`
**Expected:** `questionnaire` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** None.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a logo "DR International" and "DIAGNOSTIC RESEARCH INTERNATIONAL" at the bottom. There is a Bates number "51681 4779".
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a title "AN EVALUATION OF EIGHT PRINT ADS FOR THE WINSTON MM 4TH QUARTER REVISED CAMPAIGN" and a list of ad names. It has a logo and company name at the bottom. It is not just an ID/stamp.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: The text is typed. No majority handwriting.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No fax header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: The title is "AN EVALUATION OF EIGHT PRINT ADS FOR THE WINSTON MM 4TH QUARTER REVISED CAMPAIGN". It lists ad names: "Real Man", "Wake Up", "Bull Dog", "Mutt", "Buns", "Sugar & Spice", "Bogus", "Clue". This looks like a cover page for a report or a presentation about an evaluation. Wait, is it a questionnaire? "An evaluation of eight print ads". Usually, an evaluation involves a survey. But the page itself is a title page. Let's look at Check 9.
    *   Result: not this check (yet). It's a title page.
> *   **Check 5: resume**
    *   Evidence: No career history.
    *   Result: not this check.
> *   **Check 6: scientific_publication**
    *   Evidence: No journal name/volume/issue. "Diagnostic Research International" is a company, not a journal.
    *   Result: not this check.
> *   **Check 7: financial document**
    *   Evidence: No financial tables, invoices, or budgets.
    *   Result: not this check.
> *   **Check 8: specification**
    *   Evidence: No material safety data, product formulation, or "shall/must" language.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: The page has a large black bar at the top and a gradient black bar at the bottom (scan artifact or design). It has a logo "DR International". It has a title "AN EVALUATION OF EIGHT PRINT ADS FOR THE WINSTON MM 4TH QUARTER REVISED CAMPAIGN". It lists items. It looks like a cover page for a presentation or a report.
    *   Let's check the rules for Check 9: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation (this check), not file_folder (check 1)."
    *   "A large heading rotated 90 degrees... is a section divider... but a rotated SHORT FILING LABEL... is file_folder."
    *   "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation". Here, there is a solid black bar at the top and a large black gradient area at the bottom. The text is centered in the upper half. This looks like a title slide or a cover page for a deck/report.
    *   Wait, is it a scientific_report title page? "Technical-study title pages: a title page naming a specific study or methodology with a date... is scientific_report (check 13), not presentation". The title is "AN EVALUATION OF EIGHT PRINT ADS...". This is a marketing evaluation, not a scientific study methodology.
    *   Is it a questionnaire cover? "Survey cover pages: a cover/title page whose title names a survey (e.g. 'SURVEY OF WORKPLACE SMOKING RESTRICTIONS'...) is the instrument's cover — questionnaire". This title is "AN EVALUATION OF EIGHT PRINT ADS". It doesn't explicitly say "Survey". However, evaluations of ads often involve questionnaires. But let's look at the layout.
    *   The layout has a big black bar at the top and a big black gradient at the bottom. This looks like a slide cover or a designed title page.
    *   Let's re-read Check 9: "Slide/overhead layouts... a deck title or section-divider page... A near-blank cover or title page... is a presentation".
    *   The page has "DR International" logo, title, list of ads, and company footer. It looks like a cover page for a presentation or a report.
    *   Let's look at Check 13: "Original research write-up -> scientific_report". "A technical-study title page with authors and an internal affiliation and no journal identifiers." This is "Diagnostic Research International", a market research firm. An evaluation of ads is likely a market research report.
    *   However, Check 9 says: "Technical-study title pages: a title page naming a specific experimental method/study is scientific_report (check 13), not presentation, even when it is sparse or printed slide-style on a dark background: the title names an experimental study, not a deck/program/section."
    *   Is "An evaluation of eight print ads" a technical study? It's a market research evaluation.
    *   Let's look at the visual cues. The black bar at the top and the gradient at the bottom look like a slide design or a folder tab? No, it looks like a designed cover page.
    *   Wait, look at the left edge. There are holes (punched holes) and a black bar. This looks like a page from a bound document or a slide.
    *   Actually, look at the black bar at the top and the holes on the left. This looks like a page from a report or a slide.
    *   Let's reconsider Check 1: file_folder. "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body."
    *   The left side has a black vertical bar with holes. This looks like the binding edge of a document or a folder.
    *   The top has a solid black bar.
    *   The bottom has a large black gradient area.
    *   The text is in the white space.
    *   This looks like a cover page for a presentation or a report.
    *   Let's look at the label "51681 4779". This is a Bates number.
    *   Let's look at the content: "AN EVALUATION OF EIGHT PRINT ADS FOR THE WINSTON MM 4TH QUARTER REVISED CAMPAIGN". List of ads. "DIAGNOSTIC RESEARCH INTERNATIONAL".
    *   This is a title page for a document.
    *   Is it a presentation? "Slide/overhead layouts... a deck title...". The layout is sparse. The black gradient looks like a design element.
    *   Is it a scientific_report? "Technical-study title page...". An ad evaluation is not typically a "scientific" study in the academic sense, but market research. However, the instructions say "scientific_report: ... a lab or technical study title page with authors and an internal affiliation...". Diagnostic Research International is a company.
    *   Let's look at Check 9 again. "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation". This page has a title, subtitle, list, logo, footer. It's not "near-blank" but it's a title page.
    *   Wait, is this a questionnaire? "Survey cover pages: a cover/title page whose title names a survey... is questionnaire". The title is "An evaluation...". Not explicitly a survey.
    *   Let's look at the visual structure. The black bar at the top and the holes on the left suggest this might be a slide or a specific document type.
    *   Actually, look at the left edge: black vertical bar with circular holes. This is characteristic of a slide mount or a specific type of scan. Or a folder tab?
    *   "Folder-tab pages... photograph of a physical manila folder TAB... protruding tab-shaped piece of cardboard... usually with a Bates number... The black bar is the photographed folder body/tab edge".
    *   If this is a folder tab: The label is "AN EVALUATION OF EIGHT PRINT ADS...". That's a long label. Folder tabs usually have short labels like "NEWTROL", "Litigation Content". This label is a full title. So it's not a folder tab.
    *   So it's not file_folder (Check 1).
>     *   Let's look at Check 9: "Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
    *   Here we have a solid black bar at the top. And a large black gradient at the bottom. The text is in the upper middle. This looks like a slide or a designed cover.
    *   "A standalone photographic image... carrying only a Bates number is a photographic slide (this check)". This has text.
    *   "A deck title or section-divider page... is a presentation".
    *   This looks like a title page for a presentation or a report.
    *   If it's a report title page, is it scientific_report?
    *   Check 13: "Original research write-up... Requires running prose... A technical-study title page with authors and an internal affiliation and no journal identifiers."
    *   This page has no running prose. It's just a title and a list.
    *   Check 9 says: "A near-blank cover or title page... is a presentation".
    *   The page is mostly black (bottom half) and white (top half with text). It looks like a designed cover.
    *   Let's consider "presentation". The layout is sparse, centered text, logo, footer. It looks like a title slide or cover for a deck. "Diagnostic Research International" is a market research firm. They likely present findings in a deck or a report.
    *   If it's a report, the title page alone is often classified as presentation if it's a deck cover.
    *   Let's look at the "technical-study title page" exception in Check 9. "Technical-study title pages: a title page naming a specific study or methodology with a date... is scientific_report". "An evaluation of eight print ads" is a study, but is it a "technical study" with "experimental method"? Probably not. It's a marketing evaluation.
    *   So it falls back to Check 9: presentation. "A near-blank cover or title page... is a presentation".
>     *   Wait, could it be a questionnaire? "Survey cover pages... title names a survey". "An evaluation" could be a survey. But usually, if it's a survey instrument, the title is "Survey of...". Here it's "Evaluation of...". And there's no indication of questions.
    *   Let's look at the list: "Real Man", "Wake Up", etc. These are ad names. This is a cover for a document evaluating these ads.
    *   The document is likely a report or a presentation.
    *   Since it's just the title page with sparse text and heavy graphical elements (black bars), it fits "presentation" (deck cover or title page).
>     *   Let's re-evaluate Check 1 (file_folder).
    *   "A page titled 'RECOMMENDATIONS' with no subtitle... carries real content — it is a cover/title page... not file_folder."
    *   This page has a title. So not file_folder.
>     *   Let's re-evaluate Check 13 (scientific_report).
    *   "Requires running prose". This page has no running prose. So not scientific_report.
>     *   So it's likely Check 9 (presentation).
    *   Evidence: Title page with sparse text, logo, and heavy graphical design (black bars/gradient). "AN EVALUATION OF EIGHT PRINT ADS...". Looks like a cover for a presentation or a designed report cover. The instructions say "A near-blank cover or title page... is a presentation". Although this has a list, it's a title page.
    *   Wait, is it a "company statement"? No.
    *   Is it a "slide deck"? The layout (sparse text, logo, footer, black bars) is very slide-like. The black gradient at the bottom looks like a design element for a slide or a cover.
    *   The left edge has holes. This is typical of bound documents or slides.
    *   Actually, look at the left edge: black vertical bar with white circles (holes). This looks like the binding of a report or a slide mount.
    *   If it's a slide: "photographic slide image... is presentation".
    *   If it's a title page: "deck title... is presentation".
>     *   Let's check if there's any other category.
    *   advertisement? No, it's an evaluation of ads, not an ad itself.
    *   form? No fields.
>     *   Conclusion: presentation.
>     *   Wait, let's look closer at the "folder tab" rule.
    *   "Folder-tab pages... photograph of a physical manila folder TAB... bearing a short filing label... usually with a Bates number... The label IS filing metadata... so it is NOT a 'topical title'".
    *   The label here is "AN EVALUATION OF EIGHT PRINT ADS...". That's a long title, not a short filing label like "NEWTROL". So it's not a folder tab.
>     *   Let's look at the "Scan-artifact signal" in Check 9.
    *   "a solid black bar along one edge of the page... combined with sparse text... points to a photographed slide/overhead — presentation".
    *   There is a solid black bar at the top. There is a large black area at the bottom. The text is sparse. This fits the signal.
>     *   Final decision: presentation.
>     *   Runner-up: scientific_report. Ruled out because there is no running prose, and the title is a marketing evaluation, not a technical/scientific study with methods/prose. Also, Check 9 (presentation) covers title pages/cover pages that are sparse or designed.
>     *   Wait, is it a questionnaire?
    *   "Survey cover pages: a cover/title page whose title names a survey... is questionnaire".
    *   Title: "AN EVALUATION OF EIGHT PRINT ADS". Not a survey name.
    *   So not questionnaire.
>     *   Is it a form?
    *   No fields.
>     *   So presentation is the best fit.
>     *   One more check: Check 13 "Technical-study title page... is scientific_report".
    *   "An evaluation of eight print ads for the Winston MM 4th Quarter Revised Campaign".
    *   This is a market research title page. Market research reports often have title pages.
    *   If the document is a report, the title page alone...
    *   Check 9: "A near-blank cover or title page... is a presentation".
    *   Check 13: "Requires running prose". A title page alone doesn't have running prose.
    *   So if it's just the title page, and it's not a scientific report (no prose), it falls to presentation (as a deck cover/title page) or file_folder (if it's just an ID, but it has a title).
    *   The instructions say: "A page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."
    *   So it's presentation.
>     *   Wait, is "Diagnostic Research International" a journal? No.
    *   Is it a news article? No.
>     *   Final label: presentation.

---

## questionnaire → form (1 errors)

### `rvl_cdip__questionnaire__0006.png`
**Expected:** `questionnaire` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is a Bates number "5038 0091" on the right side. No fax transmission header like "SENT BY:".
- **Masthead/Running head:** No newspaper masthead. No journal running head with volume/issue/page number. There is a title at the top: "SOURCE OF EXPOSED MOTHER HISTORY FORM". Wait, let's look closer. "SOURCE OF EXPOSED MOTHER HISTORY FORM". It looks like a form.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder.**
    *   Evidence: The page has a title "SOURCE OF EXPOSED MOTHER HISTORY FORM" and many questions with handwritten answers. It has real content.
    *   Result: not this check.
> *   **Check 2: handwritten.**
    *   Evidence: Most of the content is printed questions ("How old is the mother?", "How many times has she been pregnant?"). The answers are handwritten ("31", "3", "2", "1", "2", "yes", "she been smoking about 10 years", "15-20", "no", "no", "no", "no", "probably", "no").
    *   Wait, is it "majority handwritten"? The printed text is the questions. The handwritten text is the answers. The printed text is quite dense. Let's look at the rule: "Most of the content is freeform handwriting... NOT on a printed template." This is clearly on a printed template (a form). "Handwriting filling in labeled printed fields is form, not handwritten".
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET.**
    *   Evidence: No "FACSIMILE" header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire.**
    *   Evidence: The title is "SOURCE OF EXPOSED MOTHER HISTORY FORM". It asks questions: "How old is the mother?", "How many times has she been pregnant?", "Did she smoke before the birth of the baby?". This is a survey instrument or a history form used for data collection (likely epidemiological or medical research).
    *   Wait, is it a questionnaire or a form?
    *   Check 4 says: "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines...". This page asks questions about the mother's history.
    *   Check 10 says: "Administrative Form -> Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
    *   Let's distinguish between questionnaire and form.
    *   Questionnaire (Check 4): "survey instrument... asks the reader to answer...". "instructions or directions given to product-test/consumer-test participants".
    *   Form (Check 10): "capturing factual data".
    *   The title says "SOURCE OF EXPOSED MOTHER HISTORY FORM". It looks like a data collection form for a study (epidemiology).
    *   Let's look at the labels. "questionnaire" vs "form".
    *   Check 4: "The page asks the reader to answer...". This page asks questions. "How old is the mother?", "How many times...".
    *   However, Check 10 covers "records-management inventory or log table", "application", "QA/parameter review sheet".
    *   Let's look at the distinction. A questionnaire is usually a survey sent to people. This looks like a researcher filling out data about a subject (the mother). "How old is the mother? 31". This is data capture about a subject, not a survey sent to the subject (though the subject could have answered it, it looks like an interviewer-administered or researcher-recorded form).
    *   Actually, let's look at Check 4 again. "The page asks the reader to answer...". If the reader is the researcher filling out the form about the mother, it's a form. If the reader is the mother, it's a questionnaire.
    *   The text "SOURCE OF EXPOSED MOTHER HISTORY FORM" suggests it's a form for recording history.
    *   Let's look at Check 10: "Administrative Form... Filled or blank fields... for capturing factual data". This fits perfectly. It's a form capturing factual data about a mother's history (pregnancy, smoking, alcohol, drugs, chemicals).
    *   Is there a stronger match for Questionnaire? Questionnaires are usually surveys. This is a "History Form".
    *   Let's re-read Check 4 carefully. "The page asks the reader to answer...". If this is a survey instrument given to a respondent, it's a questionnaire. If it's a data collection sheet for a researcher, it's a form.
    *   The title "SOURCE OF EXPOSED MOTHER HISTORY FORM" strongly points to "form".
    *   Also, Check 10 explicitly mentions "filled or blank fields... for capturing factual data". This is exactly what this is.
    *   Wait, is it a scientific_report? No, it's just data.
    *   Let's look at the "questionnaire" definition again. "survey instrument... asks the reader to answer".
    *   Let's look at the "form" definition. "capturing factual data".
    *   In tobacco archives, these are often "interviewer-administered questionnaires" or "data collection forms".
    *   However, the label "form" is very broad. Let's look for specific evidence.
    *   The page has printed questions and handwritten answers.
    *   Check 2 says: "Handwriting filling in labeled printed fields is form, not handwritten". So it's at least not handwritten.
    *   Is it a questionnaire? A questionnaire is a set of questions. This is a set of questions.
    *   But Check 10 is "Administrative Form".
    *   Let's look at the calibration notes: "A handwritten note about a questionnaire... is questionnaire". "A freeform handwritten consumer opinion/feedback card is handwritten, not questionnaire — questionnaire requires a PRINTED instrument with printed question items, rating scales, or response boxes".
    *   This page has printed question items and response lines (where the handwriting is). So it fits the "printed instrument with printed question items" description of a questionnaire.
    *   BUT, Check 10 says: "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
    *   So a filled questionnaire is... a questionnaire? Or a form?
    *   Check 4: "The page asks the reader to answer...". If the page *is* the survey instrument, it's a questionnaire.
    *   Check 10: "Administrative Form... capturing factual data".
    *   Usually, if it's a survey (like a census, a market research survey), it's a questionnaire. If it's a medical record or a data sheet for a study, it's a form.
    *   The title "SOURCE OF EXPOSED MOTHER HISTORY FORM" uses the word "FORM".
    *   Let's look at the content. It's about "Exposed Mother". This sounds like an epidemiological study (e.g., DES exposure, or smoking exposure). "Did she smoke before the birth of the baby?". "Did she drink alcoholic beverages". "Was she exposed to chemicals on the job?". This is a data collection form for a research study.
    *   In the tobacco archive context, these are often called "forms" or "questionnaires".
    *   Let's look at the checks order. Check 4 (questionnaire) comes before Check 10 (form).
    *   Check 4: "The page asks the reader to answer...". Does this page ask the reader (the person filling it out) to answer? Yes. "How old is the mother? 31". The person filling it out is answering questions about the mother.
    *   Is it a survey instrument? A survey instrument asks the *respondent* questions. Here, the questions are about a third party ("the mother"). "How old is the mother?". This is an interviewer form or a researcher data sheet.
    *   Check 4 says: "instructions or directions given to product-test/consumer-test participants". This is not that.
    *   Check 4 says: "enrolment/commitment application". No.
    *   Check 4 says: "cover letter transmitting a survey". No.
    *   The core of Check 4 is "survey instrument". A survey asks the respondent about themselves. This asks about "the mother". This is a data collection form.
    *   Therefore, Check 10 (form) is more appropriate. It's a form for capturing factual data (history of the mother).
> *   **Check 5: resume.** No.
*   **Check 6: scientific_publication.** No.
*   **Check 7: financial document.** No.
*   **Check 8: specification.** No.
*   **Check 9: presentation.** No.
*   **Check 10: ADMINISTRATIVE FORM -> form.**
    *   Evidence: "SOURCE OF EXPOSED MOTHER HISTORY FORM". Printed questions ("How old is the mother?", "How many times...") with handwritten answers ("31", "3", "2"). Fields for capturing factual data (age, pregnancy count, smoking history, alcohol, drugs, chemicals).
    *   This fits "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
    *   Result: **form**.
> Let's double check Check 4 (questionnaire).
"The page asks the reader to answer, rate, choose, or commit...".
If I fill out a form about my medical history, is it a questionnaire?
Usually, a medical history form is a form. A survey sent to people is a questionnaire.
The title says "HISTORY FORM".
The content is data capture about a subject (the mother).
Check 10 is the best fit.
> Let's look at the "questionnaire" definition again. "survey instrument... asks the reader to answer".
If this is a page from a survey book where the interviewer asks the mother these questions and writes the answers, it could be considered part of a questionnaire instrument.
However, Check 10 is "Administrative Form".
Let's look at the labels. "form" is a very common label.
The title literally says "FORM". "SOURCE OF EXPOSED MOTHER HISTORY FORM".
Check 10: "A form does NOT have to be blank — a filled form recording data is still a form".
This is a filled form.
> Let's consider if it's a "scientific_report".
Check 13: "Running narrative prose...". This is not narrative prose. It's Q&A. "Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."
So it's definitely not scientific_report.
> So it's between questionnaire and form.
Check 4 (questionnaire) vs Check 10 (form).
Check 4 is "SURVEY INSTRUMENT".
Check 10 is "ADMINISTRATIVE FORM".
The page is a "HISTORY FORM". It captures factual data.
The questions are about a third party ("the mother"). A survey/questionnaire usually targets the person filling it out (or the person being interviewed directly). Here, the questions are "How old is the mother?". This implies the person filling it out is someone else (a researcher or interviewer).
This is a data collection form.
Check 10 covers "capturing factual data".
> Final decision: form.
> Wait, is there any other check?
Check 1: file_folder. No, it has content.
Check 2: handwritten. No, it's on a template.
> Let's re-read the "questionnaire" check carefully.
"The page asks the reader to answer...".
If the "reader" is the person filling the form, they are answering "How old is the mother?".
But is it a "survey instrument"?
A survey instrument is typically a tool for gathering survey data.
This is a "History Form".
In the tobacco archive, these are often "interview schedules" or "data forms".
If I have to choose, "form" is safer because the title says "FORM" and it's capturing structured data (fields).
Also, Check 10 explicitly says: "a filled form recording data is still a form, including handwriting in its cells."
> Let's look at the evidence for "questionnaire".
"printed question items". Yes.
But "questionnaire" is usually for surveys.
This looks like a medical/epidemiological data sheet.
The label "form" is appropriate for a data capture sheet.
> Let's look at the scratchpad instructions: "Once an earlier check matches, later checks do not override it."
Check 4 is before Check 10.
Does Check 4 match?
"The page asks the reader to answer... opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey."
This page has open-response lines ("How old is the mother? 31").
It asks the reader to answer.
Is it a survey instrument?
If this is a page from a study where they interview mothers, this is the interviewer's form.
Interviewer-administered questionnaires are still questionnaires.
BUT, the title is "SOURCE OF EXPOSED MOTHER HISTORY FORM".
And Check 10 says: "Administrative Form... capturing factual data".
And Check 13 says: "a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."
> Let's look at the distinction in the prompt's calibration:
"A handwritten note about a questionnaire... is questionnaire".
"A freeform handwritten consumer opinion/feedback card is handwritten, not questionnaire — questionnaire requires a PRINTED instrument with printed question items, rating scales, or response boxes".
This page has printed question items and response boxes/lines. So it fits the *structure* of a questionnaire.
However, Check 10 says: "Filled or blank fields... for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form".
> This is a conflict between Check 4 and Check 10.
Check 4: Questionnaire.
Check 10: Form.
> Let's look at the content again.
"THE MOTHER BEFORE THE BIRTH OF THE CHILD"
"PERSONAL HISTORY"
Questions about age, pregnancy, abortion, children, smoking, alcohol, drugs, chemicals.
This is a medical/obstetric history form.
In medical contexts, these are "forms" (e.g., patient history form).
In research contexts, they are "data collection forms" or "instruments".
If it's an instrument for a survey, it's a questionnaire.
If it's a form for data entry, it's a form.
> The title "SOURCE OF EXPOSED MOTHER HISTORY FORM" contains the word "FORM".
Check 10 is "ADMINISTRATIVE FORM -> form".
The definition includes "capturing factual data".
This is definitely capturing factual data.
> Is there a "survey" aspect?
"SOURCE OF EXPOSED MOTHER" -> This sounds like a study on exposure (e.g., to chemicals or smoking) and its effect on the child.
The data is being collected about the mother.
This is a data collection form.
I will lean towards **form** (Check 10).
> Why not questionnaire?
Questionnaire (Check 4) is for "survey instrument". A survey usually asks the respondent about their own opinions, behaviors, demographics.
Here, the questions are about "the mother". The person filling it out is likely a researcher or interviewer recording data about a subject.
This is a data capture form.
Check 10 is the best fit.
> Also, look at Check 10: "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
This page is a filled form.
> Let's check if there's any other label.
"scientific_report"? No, no narrative prose.
"invoice"? No.
> So, **form**.
> One detail: "SOURCE OF EXPOSED MOTHER HISTORY FORM".
Maybe "SOURCE OF EXPOSED" is a typo for "SOURCE OF EXPOSURE"? Or "MOTHER OF EXPOSED CHILD"?
"SOURCE OF EXPOSED MOTHER HISTORY FORM" -> Maybe "History of Mother of Exposed [Child]".
Regardless, it's a history form.
> Final check of the steps:
1. file_folder: No, has content.
2. handwritten: No, printed template with handwriting.
3. fax: No.
4. questionnaire: It has questions, but it's a history form for data capture about a third party. The title says "FORM". Check 10 is more specific for data capture forms. Wait, Check 4 comes first. Does Check 4 match?
"The page asks the reader to answer...". Yes.
"open-response lines". Yes.
Is it a "survey instrument"?
If I have to be strict: A survey instrument asks the *respondent* questions. Here the questions are about "the mother". The reader (filler) is answering about the mother. This is an interviewer form.
Interviewer forms are often classified as forms (data collection) rather than questionnaires (which are the instrument given to the respondent).
However, sometimes interviewer scripts are called questionnaires.
But the title says "FORM".
And Check 10 explicitly covers "capturing factual data".
I'll stick with **form**.
> Wait, let's look at the "questionnaire" definition again.
"The page asks the reader to answer...".
If the page is the instrument used to collect data, it could be a questionnaire.
But Check 10 is "Administrative Form".
In the tobacco archive, these epidemiological data sheets are usually forms.
Let's look at the label list: `advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification`.
> If I choose `questionnaire`: Evidence is printed questions.
If I choose `form`: Evidence is "HISTORY FORM" title, structured data capture, filled fields.
> Let's look at the pre-scan/scratchpad rule: "deliberate through the checks below, in order, and commit to the FIRST one with strong, concrete evidence".
Check 4: "The page asks the reader to answer...".
Does this page ask the reader to answer? Yes. "How old is the mother? 31". The reader (filler) answers "31".
Is it a survey instrument?
"survey instrument... asks the reader to answer, rate, choose, or commit".
This fits.
BUT, "instructions or directions given to product-test/consumer-test participants". No.
"enrolment/commitment application". No.
"cover letter transmitting a survey". No.
> The core of Check 4 is "survey instrument".
Is a "Mother History Form" a survey instrument?
It's a data collection instrument.
In many contexts, "questionnaire" and "form" are close.
But Check 10 is "Administrative Form".
And Check 10 says: "A form does NOT have to be blank — a filled form recording data is still a form".
And Check 13 says: "a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."
> Let's assume the label is **form**.
Evidence: Title "SOURCE OF EXPOSED MOTHER HISTORY FORM", structured questions with handwritten answers capturing factual data (age, pregnancy, smoking, etc.).
> One more check: Check 2 (handwritten).
"Most of the content is freeform handwriting... NOT on a printed template."
This is on a printed template. So not handwritten.
> So it's form.
> One edge case: "questionnaire".
If this is a page from a survey book where the interviewer reads questions to the mother and writes answers...
The title "SOURCE OF EXPOSED MOTHER HISTORY FORM" suggests it's a form for the study records.
I will go with **form**.
> Wait, looking closely at the text: "SOURCE OF EXPOSED MOTHER HISTORY FORM".
Actually, it looks like "SOURCE OF EXPOSED MOTHER HISTORY FORM".
Maybe "SOURCE" is a column header? No, it's centered at the top.
"THE MOTHER BEFORE THE BIRTH OF THE CHILD"
"PERSONAL HISTORY"
> This is a data sheet.
Label: **form**.
> Final check on Check 4 vs Check 10.
Check 4: Questionnaire. "The page asks the reader to answer...".
Check 10: Form. "Filled or blank fields... for capturing factual data".
The page is a filled form capturing factual data.
The title contains "FORM".
I'll stop at Check 10.
> Wait, is there any evidence for Check 4 that is stronger?
"The page asks the reader to answer...".
If I consider this a survey (epidemiological survey), then it's a questionnaire.
But the title says "FORM".
And the content is structured data (fields).
Check 10 is "Administrative Form".
In the absence of a clear "survey" context (like "Please answer these questions about your smoking habits"), and with a title "HISTORY FORM", **form** is the better label.
Also, the calibration says: "form, scientific_report, and handwritten are historically the most over-predicted labels". This suggests I should be careful.
But "questionnaire" is under-predicted.
If this is a survey instrument, it should be questionnaire.
Is it a survey instrument?
It asks questions about the mother's history.
If the study is about the child's health and the mother's history is the data...
This is a data collection form.
Usually, data collection forms in research are called "forms" or "instruments".
If the label "questionnaire" is available, and this is a set of questions...
But Check 10 is explicitly for "capturing factual data".
And Check 13 says "labeled field-value entries... is a filled form".
This page is labeled field-value entries (Question -> Answer).
So Check 10 applies.
> I will classify as **form**.
> One detail: "5038 0091" is a Bates number.
Check 1: "A Bates number or archive stamp alone is NOT enough... A page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content".
Here, the title is "SOURCE OF EXPOSED MOTHER HISTORY FORM". This is a bold headline title? It's centered, uppercase.
But the page has full body content (questions and answers). So it's not file_folder.
> Final decision: **form**.
> Wait, let's look at the "questionnaire" definition one last time.
"The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey."
This page has open-response lines. "How old is the mother? 31".
It asks the reader to answer.
Is it a survey?
If this is a page from a "Questionnaire on Mother's History", then it's a questionnaire.
The title says "HISTORY FORM".
In tobacco archives, these are often "interviewer-administered questionnaires" which are forms.
But the label "form" is distinct.
If I have to choose, the title "FORM" is strong evidence for Check 10.
Also, the content is factual data capture (medical history), not opinions or survey responses (though smoking/alcohol are survey-like, they are factual history).
Check 10: "capturing factual data".
Check 4: "opinion items...". This is not opinion, it's history (facts). "How old is the mother? 31". Fact. "Did she smoke? Yes". Fact.
So it's capturing factual data -> Form.
> Label: form.

---

## scientific_publication → scientific_report (1 errors)

### `rvl_cdip__scientific_publication__0010.png`
**Expected:** `scientific_publication` | **Predicted:** `scientific_report`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** None. There's a "FILE COPY" stamp and a handwritten note, but no From/To/Sent/Subject.
- **Masthead/Running head:**
    - Top right: "4153" (handwritten).
    - Title: "Neuropeptide Tyrosine in the Cardiovascular System".
    - Authors: John Wharton and Julia M. Polak.
    - Affiliation: Department of Histochemistry, Royal Postgraduate Medical School, Du Cane Road, London W12 0NN, United Kingdom.
    - Text body: Introduction, Immunohistochemistry.
    - Right side vertical text: "1990 ANNUAL REPORT". Wait, let's look closer. "1990 ANNUAL REPORT" is printed vertically on the right side.
    - Bottom handwritten text: "In Central + Peripheral Significance of Neuropeptide Y and its Related Peptides". "Annals of the New York Academy of Science Vol 601, 1990".
    - Bottom right: "PUBLICATIONS 029744".
    - There is a "FILE COPY" stamp.
> Let's re-evaluate the "1990 ANNUAL REPORT" text. It's vertical on the right side.
Let's look at the bottom handwritten text: "Annals of the New York Academy of Science Vol 601, 1990". This looks like a citation or a note about where this was published.
The text itself is a scientific paper abstract or introduction. "Neuropeptide Tyrosine (NPY) is an amidated 36-amino acid sequence..."
> Let's check the checks in order.
> **Check 1: file_folder**
- Content: Title, authors, affiliation, running text (Introduction, Immunohistochemistry). Not just an ID. Not a folder tab.
- Result: no.
> **Check 2: handwritten**
- Most content is typed text. There is a handwritten note at the bottom ("In Central + Peripheral Significance...") and "4153" at the top. "FILE COPY" is a stamp.
- Result: no.
> **Check 3: FAX TRANSMISSION SHEET**
- No fax header. "FILE COPY" is a stamp.
- Result: no.
> **Check 4: questionnaire**
- No survey questions.
- Result: no.
> **Check 5: resume**
- Not a career history.
- Result: no.
> **Check 6: scientific_publication**
- Evidence: "Annals of the New York Academy of Science Vol 601, 1990" is handwritten at the bottom. Wait, is this the page's own identifier?
- The text says "This work was supported by the British Heart Foundation and Council for Tobacco Research, USA."
- The title is "Neuropeptide Tyrosine in the Cardiovascular System".
- The bottom text says "Annals of the New York Academy of Science Vol 601, 1990". This looks like a citation added by a librarian or archivist, or it's the source.
- Let's look for a running head. "1990 ANNUAL REPORT" is printed vertically on the right side. This looks like it belongs to the document this was scanned from (a 1990 Annual Report).
- Wait, the text is an article *from* the Annals of the New York Academy of Sciences.
- Is there a journal masthead on *this* page?
- The page has "PUBLICATIONS 029744" at the bottom. This looks like a Bates number or archive ID.
- The handwritten text "Annals of the New York Academy of Science Vol 601, 1990" suggests this is a reprint or a clipping from that publication.
- Check 6 says: "does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal...?"
- The handwritten text cites the journal. The vertical text "1990 ANNUAL REPORT" suggests this page is inside a "1990 Annual Report".
- Let's look at the content. It's an introduction to a paper. "INTRODUCTION", "Immunohistochemistry". It has running narrative prose.
- This looks like a scientific report or a scientific publication.
- If it's a reprint from a journal, it's scientific_publication. If it's an internal report, it's scientific_report.
- The handwritten note "Annals of the New York Academy of Science Vol 601, 1990" indicates the source.
- However, the page itself doesn't have the journal's running head (like "Annals NY Acad Sci 601: ..."). It has "1990 ANNUAL REPORT" on the side. This suggests the page was scanned from a document titled "1990 Annual Report".
- Wait, the "1990 ANNUAL REPORT" text is vertical. It looks like a label on the side of a page or a binding.
- Let's look at the bottom: "PUBLICATIONS 029744". This is likely a Bates number or internal archive number.
- The content is a scientific paper excerpt. "Neuropeptide Tyrosine in the Cardiovascular System".
- Is it a scientific_report? "Original research write-up -> scientific_report". "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page with authors and an internal affiliation and no journal identifiers."
- Here we have authors (John Wharton, Julia M. Polak), affiliation (Royal Postgraduate Medical School), and running prose (Introduction, Immunohistochemistry).
- The handwritten note cites "Annals of the New York Academy of Science". This implies the page *is* from there, or is a copy of it.
- But the page itself doesn't have the journal's masthead. It has "FILE COPY" and "1990 ANNUAL REPORT" (vertical).
- Actually, looking closely at the right side, "1990 ANNUAL REPORT" is printed vertically. This looks like the document this page belongs to is the "1990 Annual Report".
- The page content is an article *included* in the 1990 Annual Report? Or is it a clipping?
- The bottom text "Annals of the New York Academy of Science Vol 601, 1990" is handwritten. This is likely a note by the archivist indicating the source of the reprint.
- So this page is likely a reprint of an article from the Annals, pasted or scanned into the "1990 Annual Report" or a "PUBLICATIONS" file (indicated by "PUBLICATIONS" at the bottom).
- If it's a reprint of a published paper, does it count as scientific_publication?
- Check 6: "Evidence for this check: a named journal on the page plus a publication identifier... OR a formal paper or abstract in published conference proceedings... Also include a dated, titled science, medical... periodical page whose own masthead identifies that specialist publication".
- This page does *not* have the journal's own masthead. It has "1990 ANNUAL REPORT" on the side. The journal name is handwritten at the bottom.
- The text is "INTRODUCTION" and "Immunohistochemistry". It's a section of a paper.
- Check 13: "scientific_report". "Running narrative prose... a lab or technical study title page with authors and an internal affiliation and no journal identifiers."
- Here we have authors and affiliation. The text is narrative prose. The identifier "Annals..." is handwritten, not printed as part of the document's original layout (except maybe as a note). The printed text has "1990 ANNUAL REPORT" on the side.
- Wait, is "1990 ANNUAL REPORT" the running head? No, it's vertical.
- Let's look at the bottom right: "PUBLICATIONS 029744". This looks like a file folder label or a page in a "Publications" section of an annual report.
- If the document is the "1990 Annual Report" and this page is a publication listed in it, then the page itself is a scientific publication (reprint).
- But the instructions say: "does THIS page itself carry a running head/masthead... belonging to a journal...?" No.
- "A scientific-looking page with no publication identity is NOT a publication."
- The handwritten text provides the publication identity, but is it "on the page" as a running head? No, it's handwritten at the bottom.
- However, the content is clearly a scientific paper excerpt.
- Let's look at Check 13: "scientific_report". "Running narrative prose with objectives, methods, results, or discussion... a lab or technical study title page with authors and an internal affiliation and no journal identifiers."
- This fits well. Authors: Wharton and Polak. Affiliation: Royal Postgraduate Medical School. Content: Introduction, Immunohistochemistry (methods/results discussion).
- The handwritten note "Annals of the New York Academy of Science..." is likely a cataloging note.
- The vertical text "1990 ANNUAL REPORT" suggests the source document is the 1990 Annual Report of some institute (likely Tobacco Research, given the footnote "Council for Tobacco Research").
- So this is a page from the 1990 Annual Report, containing a reprint of a scientific paper.
- Is the page classified as the Annual Report (presentation? no), or the scientific paper (scientific_report)?
- The page *is* the scientific paper text. The surrounding elements (1990 Annual Report, Publications, Bates number) are metadata.
- The content is scientific narrative prose.
- So it should be scientific_report.
> Let's re-read Check 6 carefully.
"First, use your pre-scan finding: does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings? If yes... proceed here... Evidence for this check: a named journal on the page plus a publication identifier... OR a formal paper or abstract in published conference proceedings... Also include a dated, titled science, medical, engineering, or technical periodical page whose own masthead identifies that specialist publication... A scientific-looking page with no publication identity is NOT a publication."
> The page has "Annals of the New York Academy of Science Vol 601, 1990" handwritten. Is that enough?
Usually, handwritten notes are not considered the page's own identity unless it's the main content. Here, the main content is the typed text. The typed text has no journal masthead. The vertical text "1990 ANNUAL REPORT" is the document's identity.
So this page is part of the "1990 Annual Report".
The content on the page is a scientific paper excerpt.
Since it lacks the journal's own masthead/running head (the handwritten note is just a citation/note), it falls to Check 13: scientific_report.
"lab or technical study title page with authors and an internal affiliation and no journal identifiers." -> The title page of the article is here. Authors and affiliation are present. No printed journal identifiers (only handwritten).
"Running narrative prose..." -> Yes, Introduction and Immunohistochemistry sections.
> So, scientific_report.
> Let's check for other possibilities.
- presentation: No, it's dense text.
- form: No.
- advertisement: No.
> Wait, is "1990 ANNUAL REPORT" a presentation?
Check 9: "Slide/overhead layouts... deck title... meeting/program/speaker cover page...". No.
Check 13: "technical/project status report whose content is primarily technical... is scientific_report". An Annual Report containing scientific publications is a collection, but this specific page is the scientific text.
> Let's look at the handwritten text again.
"In Central + Peripheral Significance of Neuropeptide Y and its Related Peptides"
"Annals of the New York Academy of Science Vol 601, 1990"
This looks like the archivist labeling the clipping. The clipping is from the Annals.
The document it's scanned into is likely the "1990 Annual Report" (vertical text) or a "Publications" file (bottom text "PUBLICATIONS").
The page content is the scientific paper.
Since the page doesn't have the journal's printed masthead (only handwritten citation), it's treated as a scientific report (the text itself).
> Actually, let's look at the "FILE COPY" stamp.
And "4153" handwritten.
And "PUBLICATIONS 029744".
> The text is:
Title: Neuropeptide Tyrosine in the Cardiovascular System
Authors: John Wharton and Julia M. Polak
Affiliation: Department of Histochemistry, Royal Postgraduate Medical School...
Sections: INTRODUCTION, Immunohistochemistry.
Footnote: This work was supported by...
> This is a scientific paper excerpt.
Classification: scientific_report.
> Let's double check Check 6.
"A scientific-looking page with no publication identity is NOT a publication."
The page has a handwritten publication identity. Does that count?
"Note which one you see, if either, before you reach those checks. A journal or author being cited within the body prose... is NOT the same as the page itself carrying that identifier as its own running head... citations inside running text describe other work; a running head/copyright line on this page describes THIS page."
The handwritten text "Annals of the New York Academy of Science..." is at the bottom. It's not a running head. It's a note.
The printed text has "1990 ANNUAL REPORT" on the side. This is the document's identity.
So this page is from the 1990 Annual Report.
The content is scientific prose.
So scientific_report.
> One detail: "Also scientific_report: ... a technical-study title page naming a specific experimental method/study (see check 9)".
Check 9 says: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".
This page has a title "Neuropeptide Tyrosine in the Cardiovascular System", authors, affiliation. It looks like the first page of a paper.
So it fits scientific_report.
> Final decision: scientific_report.
> Scratchpad:
- file_folder: no, has title, authors, text.
- handwritten: no, mostly typed.
- fax: no.
- questionnaire: no.
- resume: no.
- scientific_publication: no journal masthead on page (only handwritten citation "Annals..."). Vertical text "1990 ANNUAL REPORT" suggests source document.
- financial: no.
- specification: no.
- presentation: no, dense text.
- form: no.
- correspondence: no.
- news_article: no.
- scientific_report: yes, title, authors, affiliation, running narrative prose (Introduction, Immunohistochemistry), no printed journal identifiers (only handwritten note).
- advertisement: no.
> Runner-up: scientific_publication. Ruled out because the page lacks its own printed journal masthead/volume/issue (the journal name is handwritten at the bottom as a citation/note, and the vertical text indicates it's from a 1990 Annual Report).
> Wait, is "1990 ANNUAL REPORT" the journal? No, it's likely the Tobacco Institute or similar annual report.
The footnote mentions "Council for Tobacco Research".
So it's an internal report containing a publication. The page itself is the scientific text.
> Label: scientific_report.

---

## scientific_report → presentation (1 errors)

### `rvl_cdip__scientific_report__0008.png`
**Expected:** `scientific_report` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** None.
- **Masthead/Running head:** There is a Bates number "2505411841" rotated on the right side. There is a date "printed 18.05.99 18:04". There is a reference "Ref.: Steele, Mutat. Res. 1995". This looks like a citation, not a running head for the page itself. Wait, "Mutat. Res. 1995" is a citation. The page itself doesn't have a journal masthead.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a scatter plot chart, a title "Mutagenicity of U.S. cigarettes", axes labels, data points, a regression line equation. It has a Bates number.
    *   Result: Not file_folder. It has real content (a chart).
> *   **Check 2: handwritten**
    *   Evidence: The text is typed. The chart is printed. No significant handwriting.
    *   Result: Not handwritten.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No fax header.
    *   Result: Not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No questions, no survey instrument.
    *   Result: Not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No biographical info.
    *   Result: Not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: "Ref.: Steele, Mutat. Res. 1995". This is a citation. The page itself doesn't have a journal name, volume, issue, page range, or copyright line belonging to a journal. It looks like a chart generated from data, possibly referencing a paper.
    *   Result: Not scientific_publication.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: No money, no financial data.
    *   Result: Not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: The chart is about "Mutagenicity of U.S. cigarettes". It plots "Spec. Mutagenicity (rev/mg)" vs "TPM Yield (mg/cig.)". It has a regression line "Y = -39.2*X + 1805".
    *   Is this a specification? Specifications usually have "shall/must" language, tolerances, or product formulation. This is a scatter plot of data.
    *   Wait, let's look at Check 10 and 13.
    *   Check 8 says: "A labeled product/parameter rate-data chart — e.g. a statistical process-control chart titled with the product name (e.g. "WINSTON KS RATE DATA") plotting a measured property over time/subgroup against spec limits (e.g. "USPEC"/"SPEC") — is a specification".
    *   This chart plots "Spec. Mutagenicity" vs "TPM Yield". It's a scatter plot. It's not a rate-data chart over time. It's a correlation plot.
    *   Let's check Check 10 and 13.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: The layout is sparse. Title at top. Chart in center. Bates number on side. "printed 18.05.99 18:04". "* USmarket Chart 1". "User]".
    *   This looks like a chart from a presentation or a report.
    *   Check 9 says: "A standalone chart or table of values alone — an untitled data table or a bare chart with no deck styling — is NOT a slide; it is a form (check 10). BUT a TITLED, DESIGNED DECK CHART — a chart that is itself styled as a slide (its own title/caption, a company logo or date, a rotated or centered chart-per-page layout, e.g. a "brand shares" pie chart or a "performance triggers" table page in a deck) — IS a presentation".
    *   This chart has a title "Mutagenicity of U.S. cigarettes". It has a reference. It has a date "printed 18.05.99". It has a label "* USmarket Chart 1".
    *   However, let's look at Check 13. "Original research write-up -> scientific_report".
    *   Check 13 says: "Also scientific_report: a hand-plotted experimental GRAPH of test measurements...". This is a computer-generated scatter plot (looks like it, given the regression line equation and print date).
    *   Wait, let's re-read Check 10. "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a research-measurement chart is scientific_report (check 13), and a financial/money chart is budget (check 7) ONLY when it is a standalone data table used for money planning or tracking".
    *   This is a "research-measurement chart". It plots Mutagenicity vs TPM Yield. This is scientific data.
    *   So it should be scientific_report?
    *   Let's check the definition of scientific_report (Check 13): "Running narrative prose with objectives, methods, results, or discussion... Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."
    *   Wait. "Also scientific_report: a hand-plotted experimental GRAPH of test measurements...". This is a computer plot, not hand-plotted.
    *   But is a single chart page a scientific_report?
    *   Usually, a page with just a chart and no prose is tricky.
    *   Let's look at the "presentation" check again. "A standalone chart or table of values alone... is NOT a slide; it is a form (check 10). BUT a TITLED, DESIGNED DECK CHART... IS a presentation".
    *   This chart has a title, axes, data. It looks like a slide from a presentation or a figure from a report.
    *   The text "* USmarket Chart 1" and "User]" suggests it's a generated chart, possibly from a database or presentation software.
    *   The date "printed 18.05.99" suggests a computer printout.
    *   The reference "Ref.: Steele, Mutat. Res. 1995" suggests this chart is based on or comparing to a published paper.
    *   If this is a figure from a report, and there's no prose, what is it?
    *   Let's look at Check 10 again. "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This is scientific data (mutagenicity). So it's not a generic form.
    *   "a research-measurement chart is scientific_report (check 13)".
    *   So if it's a research-measurement chart, it falls under scientific_report?
    *   But Check 13 says "Requires running prose". "a page that is only labeled field-value entries... is a filled form".
    *   Wait, the bullet point in Check 13 says: "Also scientific_report: a hand-plotted experimental GRAPH of test measurements (see check 10)". This implies graphs are scientific_report.
    *   But this is a computer plot.
    *   Let's look at Check 9 (presentation) again. "A standalone chart or table of values alone... is NOT a slide... BUT a TITLED, DESIGNED DECK CHART... IS a presentation".
    *   Is this a "TITLED, DESIGNED DECK CHART"? It has a title "Mutagenicity of U.S. cigarettes". It has a reference. It has a regression equation. It looks like a slide.
    *   However, the content is scientific data.
    *   Let's look at the labels. 16 categories.
    *   If it's a chart from a scientific report, and there's no prose, is it scientific_report?
    *   The instructions say: "If nothing matches, choose the label whose defining evidence is closest... never default to scientific_report."
    *   Let's re-evaluate Check 13. "Requires running prose". This page has NO running prose. Just a title, a reference, a chart, an equation, a Bates number, a print date.
    *   So Check 13 fails the "Requires running prose" test, unless the "hand-plotted experimental GRAPH" exception applies. But this isn't hand-plotted. It's a computer printout ("printed 18.05.99").
    *   Let's re-evaluate Check 10. "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This is scientific data. So it's not a form under the "generic administrative" rule.
    *   Wait, the rule says: "a chart of a product's measured parameters against spec limits is specification (check 8), a research-measurement chart is scientific_report (check 13)".
    *   So a research-measurement chart is scientific_report. Even if it lacks prose? The bullet point says "Also scientific_report: a hand-plotted experimental GRAPH...". This implies graphs are scientific_report.
    *   But the main text says "Requires running prose". This is a contradiction or a specific exception.
    *   Let's look at the "presentation" check (Check 9). "A standalone chart or table of values alone... is NOT a slide; it is a form (check 10). BUT a TITLED, DESIGNED DECK CHART... IS a presentation".
    *   This chart is titled. It is designed (axes, labels, regression line). It looks like a slide.
    *   The text "* USmarket Chart 1" and "User]" looks like software output (maybe a database chart or presentation software).
    *   The Bates number is on the side.
    *   If this is a slide from a presentation, it's presentation.
    *   If this is a figure from a report, it's scientific_report (but lacks prose).
    *   Let's look at the content. "Mutagenicity of U.S. cigarettes". "Ref.: Steele, Mutat. Res. 1995". This is comparing data to a reference.
    *   This looks like a slide from a presentation analyzing mutagenicity.
    *   Let's check the "presentation" definition again. "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)... A standalone chart or table of values alone... is NOT a slide... BUT a TITLED, DESIGNED DECK CHART... IS a presentation".
    *   This chart is titled "Mutagenicity of U.S. cigarettes". It has a reference. It has a regression equation. It is a chart-per-page layout.
    *   The label "USmarket Chart 1" suggests it's part of a series, likely a presentation or report.
    *   Given the sparse layout, title, and chart, it fits "TITLED, DESIGNED DECK CHART".
    *   Wait, is it a "research-measurement chart"? Yes. Check 10 says "a research-measurement chart is scientific_report (check 13)".
    *   But Check 9 says "a TITLED, DESIGNED DECK CHART... IS a presentation".
    *   Which check wins? Check 9 is before Check 10 and 13? No, the checks are numbered 1-14. I must walk them in order.
    *   Check 1: file_folder (No)
    *   Check 2: handwritten (No)
    *   Check 3: fax (No)
    *   Check 4: questionnaire (No)
    *   Check 5: resume (No)
    *   Check 6: scientific_publication (No - citation is internal)
    *   Check 7: financial (No)
    *   Check 8: specification (No - no "shall/must", no product formulation. It's a scatter plot of data).
    *   Check 9: presentation.
        *   Evidence: "Mutagenicity of U.S. cigarettes" (Title). "* USmarket Chart 1". Scatter plot with regression line. "printed 18.05.99". Bates number.
        *   Is it a "TITLED, DESIGNED DECK CHART"? Yes, it has a title, it's a chart, it's on a page by itself (chart-per-page layout).
        *   The text says: "BUT a TITLED, DESIGNED DECK CHART — a chart that is itself styled as a slide (its own title/caption, a company logo or date, a rotated or centered chart-per-page layout... ) — IS a presentation".
        *   This page has a title, a date (printed 18.05.99), chart-per-page layout.
        *   So Check 9 matches.
>     *   Wait, let's look at the "research-measurement chart" rule in Check 10. "a research-measurement chart is scientific_report (check 13)".
    *   But Check 9 comes before Check 10. "Once an earlier check matches, later checks do not override it."
    *   So if Check 9 matches (presentation), then it's presentation.
    *   Does Check 9 match?
    *   "A standalone chart or table of values alone... is NOT a slide; it is a form (check 10). BUT a TITLED, DESIGNED DECK CHART... IS a presentation".
    *   This is a standalone chart. Is it a "TITLED, DESIGNED DECK CHART"?
    *   It has a title: "Mutagenicity of U.S. cigarettes".
    *   It has a caption/reference: "Ref.: Steele, Mutat. Res. 1995".
    *   It has a date: "printed 18.05.99 18:04".
    *   It has a label: "* USmarket Chart 1".
    *   This looks like a slide from a presentation (e.g., a market analysis or technical presentation). The label "USmarket Chart 1" strongly suggests it's part of a deck or a market report presentation.
    *   So Check 9 is a strong match.
>     *   Let's check if there's any other match.
    *   Check 13: scientific_report. "Requires running prose". This page has no running prose. So Check 13 fails. The exception "hand-plotted experimental GRAPH" doesn't apply (this is computer generated). Even if it did, Check 9 comes first.
    *   Check 10: form. "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This is scientific data. So it's not a generic form. The rule says "a research-measurement chart is scientific_report". But Check 9 catches it first as a "TITLED, DESIGNED DECK CHART".
>     *   Wait, is "USmarket Chart 1" a deck chart? "USmarket" sounds like a market analysis. "Chart 1" implies a series. This is very typical of a presentation deck.
    *   The layout is sparse. Title at top. Chart in middle. Bates number on side. Print date at bottom. This is classic slide/chart layout.
>     *   Let's reconsider Check 8 (specification). "A labeled product/parameter rate-data chart... plotting a measured property over time/subgroup against spec limits". This chart plots Mutagenicity vs TPM Yield. It's a correlation, not a rate-data chart over time. And there are no spec limits (USPEC/SPEC) visible, just a regression line. So not Check 8.
>     *   So Check 9 (presentation) seems the best fit.
>     *   Let's double check Check 6 (scientific_publication). "Ref.: Steele, Mutat. Res. 1995". This is a citation. The page itself is not the publication. The publication is "Mutat. Res." (Mutation Research). This page is a chart *referencing* it. So not Check 6.
>     *   Let's double check Check 13 (scientific_report). "Also scientific_report: a hand-plotted experimental GRAPH". This is not hand-plotted. "Requires running prose". No prose. So not Check 13.
>     *   So it's between presentation (Check 9) and form (Check 10 - research-measurement chart).
    *   Check 9 says: "BUT a TITLED, DESIGNED DECK CHART... IS a presentation".
    *   Check 10 says: "a research-measurement chart is scientific_report (check 13)". (And implies it's not a form).
    *   Since Check 9 < Check 10, if Check 9 matches, it's presentation.
    *   Does Check 9 match? "TITLED, DESIGNED DECK CHART — a chart that is itself styled as a slide (its own title/caption, a company logo or date, a rotated or centered chart-per-page layout...".
    *   Title: "Mutagenicity of U.S. cigarettes".
    *   Date: "printed 18.05.99".
    *   Layout: Chart-per-page.
    *   Label: "* USmarket Chart 1". This looks like a slide title or chart ID in a deck.
    *   Yes, it fits "TITLED, DESIGNED DECK CHART".
>     *   Wait, is there any evidence for "scientific_report" that overrides?
    *   The content is scientific (mutagenicity). But the function/layout is a chart/slide.
    *   The instructions say: "Judge each page by its FUNCTION... a page full of technical data can still be a form... but a bill is a bill even when it is printed on a form."
    *   Here, the function is a chart in a presentation/report.
    *   If it's a standalone chart from a report, and lacks prose, it's ambiguous.
    *   But the "TITLED, DESIGNED DECK CHART" rule in Check 9 specifically captures titled charts that look like slides.
    *   The label "USmarket Chart 1" is a strong indicator of a presentation deck (e.g. "US Market Analysis" deck, Chart 1, Chart 2, etc.).
>     *   Let's look at the "Runner-up" requirement. "add one final line naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out."
    *   Runner-up: scientific_report. Evidence: The content is scientific data (mutagenicity vs TPM yield), but the page lacks running prose (required for scientific_report) and matches the "titled, designed deck chart" criteria for presentation.
    *   Runner-up: form. Evidence: It's a chart, but Check 10 says research-measurement charts are scientific_report, and Check 9 catches titled deck charts as presentation. Also, generic forms are for administrative data.
>     *   Final decision: presentation.
>     *   Wait, let's look at the text "* USmarket Chart 1". "USmarket" could be a project name.
    *   "User]" looks like a software prompt or label.
    *   "printed 18.05.99 18:04" is a print timestamp.
    *   This looks like a computer-generated chart, possibly printed from a database or presentation software.
    *   In the tobacco archive, these are often slides from presentations or figures from reports.
    *   If it's a figure from a report, and there's no prose, what is it?
    *   Check 9: "A standalone chart or table of values alone... is NOT a slide; it is a form (check 10). BUT a TITLED, DESIGNED DECK CHART... IS a presentation".
    *   This is the key. Is it a "TITLED, DESIGNED DECK CHART"?
    *   It has a title. It is designed (axes, labels, regression line). It is on a page by itself.
    *   The label "USmarket Chart 1" suggests it's part of a series, typical of a deck.
    *   So presentation is the correct label.
>     *   One more check: Check 8 specification. "A labeled product/parameter rate-data chart... plotting a measured property over time/subgroup against spec limits". This is not over time. It's a scatter plot. So not specification.
>     *   So, presentation.
>     *   Wait, is it a "scientific_report" because it's a graph?
    *   Check 13: "Also scientific_report: a hand-plotted experimental GRAPH". This is not hand-plotted.
    *   Check 13 main text: "Requires running prose".
    *   So scientific_report is out.
>     *   Is it a "form"?
    *   Check 10: "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This is scientific data. So not a generic form.
    *   The rule says "a research-measurement chart is scientific_report". But scientific_report requires prose. This is a catch-22?
    *   No, Check 9 catches it first. "BUT a TITLED, DESIGNED DECK CHART... IS a presentation".
    *   So the chart is a presentation slide.
>     *   Final check of the text: "Mutagenicity of U.S. cigarettes", "Ref.: Steele, Mutat. Res. 1995".
    *   This is likely a slide from a presentation discussing mutagenicity, referencing a paper.
    *   Label: presentation.

---

## specification → form (1 errors)

### `rvl_cdip__specification__0010.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is a handwritten note at the top, but no email headers.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head with volume/issue/page number on this specific page (though there is a reference to "RDR, 1979, No. 3"). Wait, let's look closer. The bottom right has a Bates number "50056 6558". The reference section lists "RDR, 1979, No. 3 December 13, 1979 32 p." This looks like a reference to a report, not the page's own identifier.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: There is a handwritten title "1-Pyrrolidine Carboxaldehyde" and a code "[3760-54-1]". There are field labels like "Structural Formula", "Mol. Form.", "Mol. Weight", "Types of Tobacco", "Reference".
    *   Is it just an identifier? No, it has structured fields for chemical data and references. It looks like a data sheet or form. Wait, let's look at the content. It's a page capturing chemical information about "1-Pyrrolidine Carboxaldehyde".
    *   Is it a folder tab? No.
    *   Is it a patent index card? No.
    *   Conclusion: Not file_folder. It has real content (fields, reference).
> *   **Check 2: handwritten**
    *   Evidence: Top has handwritten "1-Pyrrolidine Carboxaldehyde" and "[3760-54-1]". There are checkmarks next to "Smoke" and "Green".
    *   Is *most* content handwritten? No. The page is mostly typed text (labels like "Structural Formula", "Mol. Form.", "Reference:", "Bibliography"). The handwriting is just filling in the top fields.
    *   Conclusion: Not handwritten. It's a filled form or data sheet.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header.
    *   Conclusion: Not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No questions for a respondent.
    *   Conclusion: Not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No CV content.
    *   Conclusion: Not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal running head on this page. The reference "RDR, 1979, No. 3" is a citation to another document ("SMOKE COMPARISON STUDY...").
    *   Conclusion: Not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: No money, prices, or financial tables.
    *   Conclusion: Not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: "Structural Formula", "Mol. Form.", "Mol. Weight", "Chem. Groups", "Derivatives". "Types of Tobacco... PENTANE PUFFED VS. FREON-11 PUFFED TOBACCO."
    *   Is this a specification? It looks like a data sheet for a chemical compound (1-Pyrrolidine Carboxaldehyde, CAS 3760-54-1).
    *   Check 8 says: "Material Safety Data Sheet... product formulation... test-analysis tables keyed to product/part codes... labeled product/parameter rate-data chart".
    *   This looks like a chemical data sheet. Is it a specification? "Product-referenced test data is a specification." "A titled product-analysis table... is a specification".
    *   However, let's look at Check 10 (Form). "Filled or blank fields, boxes, checkboxes... for capturing factual data". "A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) is a form".
    *   This page has fields: "Structural Formula", "Mol. Form.", "Mol. Weight", "M.P", "B.P", "Chem. Groups", "Derivatives". It has a reference section.
    *   Wait, let's look at the structure. It's a template for capturing chemical data. "Analytical information (detailed) - Smoke / Green / Cured / Non-Leaf". "Quantitative (all figures) / Qualitative only".
    *   This looks like a form for capturing chemical/analytical data.
    *   Let's check Check 10 again. "A filled analytical or lab data sheet... is a form". This page is a lab data sheet (chemical properties).
    *   Let's check Check 8 again. "test-analysis tables keyed to product/part codes". This is keyed to a chemical name "1-Pyrrolidine Carboxaldehyde". But is it a product specification? It looks like a data collection form for a chemical.
    *   Let's look at the reference: "Dube, Michael F.; Charles W. Miller; Charles R. Green SMOKE COMPARISON STUDY OF FREON-AND PENTANE-PUFFED TOBACCO CIGARETTES RDR, 1979, No. 3". This is a reference to a report.
    *   The page itself is a data capture sheet. It has fields for "Structural Formula", "Mol. Form", etc. It is largely blank (filled only at the top).
    *   Actually, looking closely, the top is filled by hand: "1-Pyrrolidine Carboxaldehyde", "[3760-54-1]". Checkboxes for "Smoke", "Green".
    *   The rest is blank typed fields.
    *   This is a form. Specifically, a lab data sheet or chemical data form.
> *   **Check 9: SLIDE DECK... -> presentation**
    *   Evidence: No slide layout.
    *   Conclusion: Not this check.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: "Structural Formula", "Mol. Form.", "Mol. Weight", "M.P", "B.P", "Chem. Groups", "Derivatives". "Types of Tobacco (all details)". "Reference:". "Bibliography (see other side):".
    *   This is a structured template for capturing data (chemical properties, tobacco types, references).
    *   Check 10 explicitly covers: "A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) is a form".
    *   This page is exactly that: a lab data sheet for a chemical compound (1-Pyrrolidine Carboxaldehyde) with fields for formula, weight, melting point, boiling point, etc.
    *   It captures factual data.
    *   Conclusion: This is a form.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: No TO/FROM/RE header. No salutation.
    *   Conclusion: Not this check.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: No masthead.
    *   Conclusion: Not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: No running narrative prose. It's a template with fields. The reference section lists a report title, but the page itself is not the report.
    *   Conclusion: Not this check.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: No marketing.
    *   Conclusion: Not this check.
> **Re-evaluating Check 8 vs Check 10:**
- Check 8 (Specification): "test-analysis tables keyed to product/part codes... labeled product/parameter rate-data chart". "A titled product-analysis table... is a specification".
- Check 10 (Form): "A filled analytical or lab data sheet... is a form".
- The page has a title (handwritten): "1-Pyrrolidine Carboxaldehyde".
- It has fields for chemical data.
- Is it a specification? A specification usually defines requirements ("shall", "must") or product properties for manufacturing. This looks like a data sheet to *record* properties or literature data. "Analytical information (detailed)". "Quantitative... Qualitative only".
- The reference is to a study "SMOKE COMPARISON STUDY...". This page seems to be a summary sheet or a data extraction form from that study or related to it.
- The text "Types of Tobacco (all details) PENTANE PUFFED VS. FREON-11 PUFFED TOBACCO." suggests it's capturing data about tobacco types.
- This is a data capture form. It's a "lab data sheet" or "chemical data form".
- Check 10 says: "A filled analytical or lab data sheet... is a form". Even if it's not fully filled (it's mostly blank with handwritten top), it's a form template. Wait, the check says "Filled or blank fields...". "A form does NOT have to be blank — a filled form recording data is still a form".
- The page has typed labels and blank lines/boxes. It is a form.
> **Let's check the reference again.**
"Reference: RDR 3 1979 Dube, Michael F... SMOKE COMPARISON STUDY... RDR, 1979, No. 3 December 13, 1979 32 p."
This is a reference card or a data sheet associated with a report (RDR 1979, No. 3).
The page itself is a form for capturing chemical information.
> **Final decision:** Form.
> **Scratchpad steps:**
1.  **file_folder**: No. Has typed fields and content (chemical name, reference). Not just an ID.
2.  **handwritten**: No. Mostly typed labels. Handwriting is just the top title and a few checks.
3.  **FAX**: No.
4.  **questionnaire**: No.
5.  **resume**: No.
6.  **scientific_publication**: No. No journal header on this page. The reference is to another doc.
7.  **financial**: No.
8.  **specification**: No. Not a product spec with "shall/must" or manufacturing change. It's a data sheet.
9.  **presentation**: No.
10. **form**: Yes. Structured fields for chemical data ("Structural Formula", "Mol. Form.", "Mol. Weight", "M.P", "B.P", "Chem. Groups", "Derivatives", "Types of Tobacco", "Reference"). Matches "filled analytical or lab data sheet" or general administrative form for data capture.
11. **correspondence**: No.
12. **news_article**: No.
13. **scientific_report**: No. No running prose. Just fields and a reference citation.
14. **advertisement**: No.
> Runner-up: scientific_report. Ruled out because there is no running narrative prose; it is a structured data sheet/form with fields. The reference text is just a citation, not the body of the report.
Runner-up: specification. Ruled out because it lacks requirement language ("shall/must") and is a data capture sheet rather than a product definition or test-analysis table of results (though it has fields for results, the page itself is the form). Actually, check 10 explicitly mentions "analytical or lab data sheet" as a form.
> Wait, is it a "specification"?
Check 8: "test-analysis tables keyed to product/part codes... labeled product/parameter rate-data chart".
This page has "Types of Tobacco... PENTANE PUFFED VS. FREON-11 PUFFED".
But the main content is chemical properties of "1-Pyrrolidine Carboxaldehyde".
It looks like a "Chemical Data Sheet" or "Literature Data Sheet".
Check 10: "A filled analytical or lab data sheet... is a form".
This fits best.
> One detail: "Bibliography (see other side):". This implies it's part of a larger document, likely a report or a file. But the page itself is a form.
The handwritten text "1-Pyrrolidine Carboxaldehyde" and "[3760-54-1]" (CAS number) fills the top.
The checkboxes "Smoke", "Green" are filled.
This is a filled form (partially).
> Final label: form.

---

## budget → presentation (1 errors)

### `rvl_cdip__budget__0008.png`
**Expected:** `budget` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is "4/2/83 JMC" at the top right, which looks like a date and initials, but not a full email header.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head with volume/issue/page number. There is a Bates number "670665021" at the bottom right.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a title "VICEROY REVISED 1983 MARKETING PLAN" and a table of contents with sections (I. EXECUTIVE SUMMARY, II. PROPOSED PLAN, etc.) and exhibits (EXHIBIT 1, EXHIBIT 2, etc.). It has page numbers (1, 2, 3...). It has handwritten notes ("Not all my marketing plan full pg", "Oct top 14 TH", "402", "Crimson top 14", "Night", "Import").
    *   Conclusion: Not file_folder. It has real content (a table of contents/outline for a marketing plan).
> *   **Check 2: handwritten**
    *   Evidence: There is significant handwritten text on the right side ("Not all my marketing plan full pg", "Oct top 14 TH", "402", "Crimson top 14", "Night", "Import") and some scribbles at the top ("JMC", "2 SC", "Put"). However, the majority of the page is typed text (a table of contents/outline).
    *   Conclusion: Not handwritten. The typed content is the primary structure.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. The "4/2/83 JMC" is just a date and initials.
    *   Conclusion: Not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No survey questions, rating scales, or commitment forms. It's a marketing plan outline.
    *   Conclusion: Not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No CV/resume content.
    *   Conclusion: Not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal name, volume, issue, or DOI.
    *   Conclusion: Not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: The document is titled "VICEROY REVISED 1983 MARKETING PLAN". It lists "BUDGET AND SHARE EXHIBITS" (Exhibit 1: Viceroy Share Forecast, Exhibit 2: Viceroy Profit and Loss Statement, Exhibit 3: Funds Available..., Exhibit 4: Budget Plan Summary...). It lists "BUDGET" as section III.
    *   Wait, is this a budget document itself? Or a plan that *contains* budget info?
    *   The page is a Table of Contents (TOC) or an outline for a document called "VICEROY REVISED 1983 MARKETING PLAN".
    *   Let's look at the content. It lists sections: I. Executive Summary, II. Proposed Plan (Creative, Media, Promotion, Product, Packaging, Research, Spending Level Test, Simon, Spending Principles), III. Budget, IV. Next Steps.
    *   It lists Exhibits 1-23.
    *   This is a Table of Contents for a marketing plan.
    *   Is it a budget? Check 7 says: "budget: internal money planning, tracking, or disbursement... financial or money-data table...". This page is an outline/TOC. It lists exhibits related to budget (Exhibit 1, 2, 3, 4, 20, 21, 22). But the page itself is an outline/TOC.
    *   Wait, let's look at the labels again.
    *   Is it a "presentation"? Check 9: "Slide/overhead layouts... a deck title or section-divider page... a near-blank cover or title page...". This page looks like a Table of Contents page for a report or presentation.
    *   Let's re-evaluate Check 9 (presentation).
    *   "a deck title or section-divider page". This is a Table of Contents.
    *   "a near-blank cover or title page... mostly empty space with only a bold headline title...". This page is dense with text (a list).
    *   However, marketing plans are often presented as slide decks or reports.
    *   Let's look at Check 13 (scientific_report). "Running narrative prose...". This is a list/outline. Not scientific report.
    *   Let's look at Check 10 (form). "Filled or blank fields...". This is not a form.
> Let's reconsider the content. It's a "REvised 1983 MARKETING PLAN". It lists sections and exhibits.
It looks like a Table of Contents for a document.
Is there a better category?
- advertisement: No.
- email: No.
- file_folder: No.
- handwritten: No.
- invoice: No.
- letter: No.
- memo: No.
- news_article: No.
- presentation: "Slide/overhead layouts... a deck title or section-divider page...". A Table of Contents for a marketing plan could be part of a presentation or a report.
- questionnaire: No.
- resume: No.
- scientific_publication: No.
- scientific_report: No.
- specification: No.
- form: No.
- budget: The document is a "Marketing Plan" which includes a "Budget" section. But is the page itself a budget?
    - Check 7: "budget: internal money planning... financial or money-data table...". This page lists exhibits *about* budget. It is not a budget table itself.
    - However, marketing plans are often classified as... wait.
    - Let's look at the labels again.
    - Is it a "memo"? "4/2/83 JMC". Handwritten notes "Not all my marketing plan full pg". This looks like a draft or a cover page/TOC for a document being reviewed.
    - The handwritten notes "Not all my marketing plan full pg" suggests this is a page from a larger document, possibly a draft being reviewed.
    - The page lists "Page" numbers (1, 2, 3...). This is definitely a Table of Contents.
> Let's look at the categories again.
1. advertisement
2. budget
3. email
4. file_folder
5. form
6. handwritten
7. invoice
8. letter
9. memo
10. news_article
11. presentation
12. questionnaire
13. resume
14. scientific_publication
15. scientific_report
16. specification
> What is a Table of Contents for a marketing plan?
- If it's a slide deck TOC -> presentation.
- If it's a report TOC -> scientific_report? No, scientific_report requires running narrative prose.
- Is it a "form"? No.
> Let's look at Check 9 (presentation) again.
"Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page... a near-blank cover or title page... a deck cover, or a section divider".
This page is a Table of Contents. A TOC is often a section divider or part of a presentation/report structure.
The layout is a list. "I. EXECUTIVE SUMMARY ... 1", "II. PROPOSED PLAN ... 3".
This looks like the Table of Contents page of a report or a presentation deck.
Given the context (tobacco industry archive, marketing plans), these were often presented as slide decks or bound reports.
The handwritten notes ("Not all my marketing plan full pg", "Oct top 14 TH", "402", "Crimson top 14") look like editorial comments on a draft.
"JMC" at the top right. "4/2/83".
This looks like a draft document page.
> Let's look at Check 13 (scientific_report).
"Running narrative prose...". This page is a list. So not scientific_report.
> Let's look at Check 11 (correspondence -> memo).
"internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
This page has "VICEROY REVISED 1983 MARKETING PLAN" at the top. No TO/FROM/RE block.
The handwritten notes are comments. Not a memo.
> Let's look at Check 7 (budget).
The document is a "Marketing Plan". Section III is "BUDGET".
The exhibits listed are budget-related (Share Forecast, P&L, Funds Available, Budget Plan Summary).
But the page itself is a Table of Contents.
Is a Table of Contents for a budget document a budget?
Check 7: "budget: ... financial or money-data table ...". This is not a money-data table. It's a list of exhibits.
> Let's reconsider **presentation**.
Check 9: "Slide/overhead layouts... a deck title or section-divider page...".
A Table of Contents is a section divider or part of a deck structure.
Also: "a near-blank cover or title page... mostly empty space with only a bold headline title...". This page is not near-blank.
But: "a deck title or section-divider page". A TOC is a section divider (it divides the document into sections).
Also, marketing plans in this era (1983) were very often slide decks (overhead projections) or bound reports presented to management.
The layout is a list of sections and page numbers. This is typical of a Table of Contents in a report or a deck.
The handwritten notes suggest it's a working document, maybe a draft of the TOC or the document itself.
> Wait, look at the bottom right: "670665021". Bates number.
Top right: "4/2/83 JMC". Date and initials.
This looks like a scanned page from a file.
> Let's look at the "Runner-up" logic.
If I choose **presentation**:
Evidence: It's a Table of Contents / Outline for a "Revised 1983 Marketing Plan". Marketing plans are often presentations (deck covers, section dividers). The layout is a structured list of sections and exhibits, typical of a document outline or deck structure. The handwritten notes ("Not all my marketing plan full pg") suggest it's a draft being reviewed, possibly for a presentation or report.
Actually, let's look at the content again.
It lists "EXHIBIT 1 ... EXHIBIT 23".
This is a Table of Contents.
Is a Table of Contents a "presentation"?
Check 9 says: "a deck title or section-divider page". A TOC is a section divider.
Also: "Slide/overhead layouts... bullet lists". This is a list.
> What about **scientific_report**?
No, no narrative prose.
> What about **form**?
No fields to fill.
> What about **budget**?
The document is a marketing plan which *contains* a budget. But the page is a TOC.
However, sometimes documents are classified by their primary subject if the form is ambiguous.
But the instructions say: "Judge each page by its FUNCTION... a page full of technical data can still be a form... a bill is a bill even when it is printed on a form."
Here, the page is a Table of Contents.
Function: To outline the document "VICEROY REVISED 1983 MARKETING PLAN".
> Let's look at the labels again.
Is there a label for "Table of Contents" or "Outline"? No.
It must fall into one of the 16.
> Could it be **memo**?
"4/2/83 JMC". Handwritten notes.
Sometimes internal memos contain outlines.
But there is no TO/FROM/RE header.
> Could it be **letter**?
No.
> Let's look at **presentation** again.
"Slide/overhead layouts... a deck title or section-divider page...".
In the tobacco industry, marketing plans were often presented as slide decks.
This page looks like the Table of Contents slide/page of a marketing plan presentation.
The handwritten notes "Not all my marketing plan full pg" -> "Not all my marketing plan [is] full page". This is a comment on the layout/content.
"Oct top 14 TH" -> likely a note about a chart or exhibit.
This looks like a draft page from a presentation or report being edited.
> Let's consider **scientific_report** again.
"Original research write-up...". No.
> Let's consider **specification**.
No.
> Let's consider **advertisement**.
No.
> Let's consider **news_article**.
No.
> Let's consider **questionnaire**.
No.
> Let's consider **resume**.
No.
> Let's consider **email**.
No.
> Let's consider **file_folder**.
No, it has content.
> Let's consider **handwritten**.
No, mostly typed.
> Let's consider **invoice**.
No.
> Let's consider **form**.
No.
> So it's between **presentation**, **budget**, **scientific_report**, **memo**, **letter**.
> If I have to choose the *best* fit:
The document is a "Marketing Plan".
Marketing plans are business documents.
In this archive (tobacco industry), marketing plans are often reports or presentations.
The page is a Table of Contents.
A Table of Contents is often part of a **presentation** (deck) or a **report** (scientific_report? No, scientific_report is for research).
Wait, "scientific_report" is for "Original research write-up". A marketing plan is not original research.
So scientific_report is out.
> Is it a **budget**?
The plan includes a budget. Section III is "BUDGET".
Exhibits 1-4 are budget exhibits.
But the page is a TOC.
Check 7: "budget: ... financial or money-data table ...". This is not a money-data table.
Check 7 caveat: "A technical/project status report whose content is primarily technical ... is scientific_report ... even if it embeds a budget-vs-actual COSTS section".
By analogy, a marketing plan whose content is primarily marketing (creative, media, promotion) is not a budget, even if it embeds a budget section.
So not budget.
> Is it a **memo**?
Internal document. "4/2/83 JMC".
But no memo header structure.
> Is it a **presentation**?
Check 9: "Slide/overhead layouts... a deck title or section-divider page...".
A Table of Contents is a section divider.
Also, marketing plans are frequently presented as slide decks.
The layout is a list of sections and page numbers. This is very common in slide decks (TOC slide) or reports.
Given the handwritten notes ("Not all my marketing plan full pg"), it looks like a draft of a document.
If it's a draft of a report, what is the label?
The labels don't have "report" except "scientific_report".
Marketing plans are not scientific reports.
They are often **presentations** (deck) or **forms** (if it's a template) or **memos** (if it's a transmittal).
> Let's look at the handwritten text again.
"Not all my marketing plan full pg." -> "Not all my marketing plan [is] full page".
"Oct top 14 TH" -> "October top 14 [th]?"
"402"
"Crimson top 14"
"Night"
"Import"
These look like notes about exhibits or data.
"Exhibit 19: Targeted Network Mail Test".
"Exhibit 20: National Theoretical Budget for Spending Level Test".
> This is a Table of Contents for a document.
In the absence of a "document outline" or "table of contents" label, where does it fit?
If it's a slide deck TOC -> **presentation**.
If it's a report TOC -> ?
The instructions say: "If nothing matches, choose the label whose defining evidence is closest...".
> Let's look at **presentation** (Check 9) again.
"Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement... or a photographic slide image".
"a deck title or section-divider page".
A Table of Contents is a section divider (it divides the document into parts).
Also, "a near-blank cover or title page... mostly empty space...". This page is not near-blank.
But "a deck title or section-divider page" is a strong match for a TOC in a deck.
Marketing plans in 1983 were heavily slide-based.
The page lists "Page" numbers (1, 2, 3...). This implies it's a TOC for a multi-page document.
If the document is a slide deck, the page numbers might refer to slide numbers.
"EXHIBIT 1 ... 1", "EXHIBIT 2 ... 2". Wait.
I. EXECUTIVE SUMMARY ... 1
II. PROPOSED PLAN ... 3
A. CREATIVE ... 3
...
EXHIBIT 1 ... (no page number listed next to it? Ah, the page numbers are in the right column).
Let's trace the lines.
I. EXECUTIVE SUMMARY ... 1
PLAN SUMMARY ... 2
II. PROPOSED PLAN ... 3
A. CREATIVE ... 3
B. MEDIA/TARGET AUDIENCE ... 4
C. PROMOTION ... 6
D. PRODUCT ... 9
E. PACKAGING ... 9
F. RESEARCH ... 9
G. SPENDING LEVEL TEST ... 10
H. SIMON ... 11
I. SPENDING PRINCIPLES AND RESOURCE ALLOCATION ... 11
III. BUDGET ... 12
IV. NEXT STEPS ... 12
> Then the Exhibits list:
BUDGET AND SHARE EXHIBITS
EXHIBIT 1 ... (no page number)
...
EXHIBIT 23 ... (no page number)
> This is a Table of Contents.
The page numbers 1-12 correspond to the main sections.
The exhibits are likely appendices or separate pages.
> This looks like the Table of Contents page of a **presentation** (deck) or a report.
Given the labels, **presentation** is the best fit for a marketing plan outline/deck TOC.
Why?
- Marketing plans are often presentations.
- A TOC is a section divider (Check 9: "a deck title or section-divider page").
- The layout is a structured list (bullet list-like).
> Let's check if it could be **form**.
No.
> Let's check if it could be **memo**.
Sometimes a memo is just a document with a date and initials.
But "VICEROY REVISED 1983 MARKETING PLAN" is a title.
A memo usually has "TO: ... FROM: ... DATE: ... RE: ...".
Here we have "4/2/83 JMC" at the top right. This is date and initials.
This is common in memos or drafts.
But the content is a TOC.
If I have to choose between memo and presentation...
A marketing plan is a substantial document. A memo is usually short correspondence.
This is a TOC for a substantial document.
So **presentation** (as in a deck/report structure) is better than memo.
> Wait, is there any other label?
**scientific_report**: "technical/project status report whose content is primarily technical...". A marketing plan is not technical research.
> **budget**: The document *contains* a budget, but is not a budget document itself (it's a plan).
Check 7: "budget: internal money planning...". A marketing plan is money planning (allocating budget to media, promotion, etc.).
But the page is a TOC.
If the page was "BUDGET AND SHARE EXHIBITS" with the actual tables, it would be budget.
Since it's the TOC, it's the structure of the document.
> Let's look at the handwritten notes again.
"Not all my marketing plan full pg." -> This is a comment on the content.
"Oct top 14 TH" -> Note about data.
This is a draft page.
> I will classify this as **presentation**.
Reasoning:
- It is a Table of Contents / Outline for a "Revised 1983 Marketing Plan".
- Marketing plans in this context are often slide decks or presentation documents.
- Check 9 includes "a deck title or section-divider page". A TOC serves as a section divider/overview for a deck or report.
- The layout is a list of sections and exhibits, typical of a presentation structure or report outline.
- The handwritten notes suggest it's a working draft, possibly for a presentation.
> Wait, let's look at **file_folder** again.
"A page titled 'RECOMMENDATIONS' with no subtitle... carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."
This page is titled "VICEROY REVISED 1983 MARKETING PLAN" (with a TOC).
So it's not file_folder. It's a section divider / cover page / TOC.
Check 9: "a deck title or section-divider page".
This fits. A TOC is a section divider.
> One more check: **scientific_report**.
"technical-study title page naming a specific experimental method/study is scientific_report (check 13), not presentation".
This is a "Marketing Plan", not a technical study. So not scientific_report.
> So **presentation** is the strongest candidate.
The page is a Table of Contents for a marketing plan. In the tobacco industry archives, marketing plans were often presented as slide decks (overhead projections) or bound reports. The TOC page is a standard part of such presentations/reports. The label "presentation" covers "deck title or section-divider page". A TOC is a section divider.
> Also, look at the handwritten note: "Not all my marketing plan full pg."
This implies the writer is discussing the layout of the plan.
"JMC" initials.
This is likely a draft page from a presentation deck or the report version of it.
> Final decision: **presentation**.
> Wait, let's look at the "Runner-up" requirement.
Runner-up: **budget**. Ruled out because although the plan includes a budget section and exhibits, the page itself is a Table of Contents/Outline, not a financial data table or budget statement. The primary function is to outline the document structure.
Or runner-up: **form**. Ruled out because it has no fields/boxes for data capture.
Or runner-up: **memo**. Ruled out because it lacks the TO/FROM/RE header structure and is a document outline, not correspondence.
> Let's refine the evidence for **presentation**.
- Title: "VICEROY REVISED 1983 MARKETING PLAN".
- Content: Table of Contents listing sections (Executive Summary, Proposed Plan, Budget, Next Steps) and Exhibits (1-23).
- Layout: Structured list with page numbers.
- Handwritten notes: Editorial comments ("Not all my marketing plan full pg", "Oct top 14 TH").
- Function: Outlines the structure of a marketing plan document/presentation.
- Check 9 match: "a deck title or section-divider page". A TOC is a section divider. Marketing plans are often presentations.
> One detail: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)".
This page is not sparse. It's a dense list.
But "a deck title or section-divider page" is the key.
Also "a near-blank cover or title page... mostly empty space...". This page is not near-blank.
But a TOC is a standard page in a presentation deck (the "Agenda" or "Contents" slide).
> Is there any other possibility?
What about **form**?
No.
> What about **scientific_report**?
No.
> I'll go with **presentation**.
> Wait, could it be **budget**?
Check 7: "budget: ... financial or money-data table ...".
The page lists "BUDGET AND SHARE EXHIBITS".
But it's just a list of titles.
"EXHIBIT 1 VICEROY SHARE FORECAST".
This is a TOC for the exhibits.
If the page *was* Exhibit 1, it would be budget (financial data).
Since it's the TOC, it's structural.
> I will stick with **presentation**.
Actually, looking at the layout, it's a Table of Contents.
In many classification tasks, a TOC is part of the document it introduces.
If the document is a "Marketing Plan", and the labels don't have "marketing_plan", what is the closest?
Marketing plans are often **presentations** (to management/board).
Or they are **reports** (scientific_report is too specific to research).
The instructions say: "If nothing matches, choose the label whose defining evidence is closest".
Presentation is closest because marketing plans are often slide decks/presentations, and a TOC is a section divider.
> Let's check the labels again.
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> If I have to choose between **presentation** and **memo**.
A memo is correspondence. This is a document outline.
A presentation is a deck/report. This fits a document outline better.
> One final check: **file_folder**.
"A page titled 'RECOMMENDATIONS' ... is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."
This page is titled "VICEROY REVISED 1983 MARKETING PLAN" (with TOC).
So it's presentation (section divider/cover).
> The handwritten text "Not all my marketing plan full pg" is a strong indicator of a draft document/presentation being reviewed.
> Final label: **presentation**.
> Wait, looking closely at the top right: "4/2/83 JMC".
And the handwritten "2 SC" with a circle.
And "Put" with a scribble.
This looks like a proof or a draft page with editorial marks.
Editorial marks on a draft of a marketing plan (which is likely a presentation deck or report).
So **presentation** is appropriate.
> One distinct possibility: **scientific_report**.
Why? "technical/project status report".
A marketing plan is a project status/plan.
But scientific_report requires "Running narrative prose". This page has no narrative prose. It's a list.
So not scientific_report.
> So **presentation** is the best fit.
> Evidence for presentation:
- Title "VICEROY REVISED 1983 MARKETING PLAN".
- Table of Contents layout (sections I-IV, Exhibits 1-23).
- Section divider / outline function.
- Handwritten editorial notes on a draft.
> Runner-up: **budget**. The document is a marketing plan which includes a budget section, but the page is a TOC, not a financial table.
Runner-up: **form**. No form fields.
Runner-up: **memo**. No memo header.
> I will output **presentation**.
> Wait, is there any chance this is a **form**?
"administrative form... filled or blank fields...". No.
> Is there any chance this is a **specification**?
"product formulation...". No.
> Okay, **presentation**.
> One detail: "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation".
This page is not near-blank.
But "a deck title or section-divider page" is also in Check 9.
A TOC is a section divider.
> Also, "Slide/overhead layouts... bullet lists".
The TOC is a list.
> I'm confident in **presentation**.
> Wait, let's look at the "Runner-up" instruction: "add one final line naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out."
Runner-up: **budget**. Evidence ruled it out: The page is a Table of Contents listing exhibits, not a financial data table or budget statement itself (Check 7 requires financial content to be the page's primary structure).
> Actually, looking at the content, it's a "Marketing Plan".
In the tobacco industry, these are often called "Plans".
If I have to classify a "Marketing Plan" TOC...
It's the structure of a **presentation** or **report**.
Since "report" isn't a label (only scientific_report), and scientific_report requires narrative prose...
**presentation** is the only one that fits a structured document outline/deck.
> Final check.
Label: presentation.
Evidence: Table of Contents for "VICEROY REVISED 1983 MARKETING PLAN", listing sections and exhibits, with editorial handwritten notes. Fits "deck title or section-divider page" or structured list layout of a presentation.
> One more thing. "4/2/83 JMC".
Could this be a **memo**?
"internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block".
Here we have date and initials. No TO/FROM/RE.
So not memo.
> Final decision: **presentation**.

---

## budget → form (1 errors)

### `rvl_cdip__budget__0009.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a Bates number "65503 5219" at the bottom. There is a "NOTICE" box at the bottom left.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a title "VARIANCE SHEET", a location "BRONX & WILLIAMSBURG - LOUISVILLE", and a list of checkboxes with text. It has handwritten text "throughout rest of file". It has a Bates number.
    *   Is it a folder tab? No, it's a full page document titled "VARIANCE SHEET".
    *   Is it identifier-only? No, it has body content (checkboxes, text).
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: Most content is typed (checkboxes, instructions). There is handwritten text "throughout rest of file" next to "OTHER (SPECIFY)".
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: Not a survey asking the reader to answer. It's a sheet checking reproduction quality.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal name/volume/issue.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: No financial data.
    *   Result: not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: No product data, MSDS, etc.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: Let's look closely at the layout.
    *   The page has a title "VARIANCE SHEET".
    *   Subtitle: "BRONX & WILLIAMSBURG - LOUISVILLE".
    *   Text: "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE:" (Wait, "MOTIVATIONS"? Probably "MODIFICATIONS" or "MOTIVATIONS" - actually looks like "MOTIVATIONS" or "MODIFICATIONS". Let's look closer. "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE:" - actually likely "MODIFICATIONS" or similar, but let's read the text).
    *   List of checkboxes:
        *   ( ) DOCUMENT COPIES ARE IN THE SAME SEQUENCE AS THEY APPEARED IN THE ORIGINAL.
        *   ( ) DUPLICATE DOCUMENTS APPEARED IN THE ORIGINAL.
        *   ( ) PAGE NUMBER(S) MISSING IN THE ORIGINAL.
        *   (X) POOR QUALITY ORIGINAL. (Checked)
        *   ( ) OVERLAY ITEM COULD NOT BE REMOVED WITHOUT DAMAGE TO THE ORIGINAL.
        *   ( ) NO DOCUMENTS WERE FOUND WITHIN THE ORIGINAL:
            *   ( ) FILE FOLDER.
            *   ( ) REMOVE EXPANDABLE FILE.
            *   ( ) MANITO FILE.
            *   ( ) ENVELOPE.
            *   ( ) OTHER (SPECIFY) _______
        *   (X) OTHER (SPECIFY) "throughout rest of file" (Handwritten).
    *   Bottom: "NOTICE If the file image is less clear than this notice, it is due to the quality of the document being filmed." and Bates number "65503 5219".
    *   Wait, look at the check 9 description: "a one-page status/location display sheet — a titled sheet stating where a record range or item is located, printed in slide-style layout with a title, a line of reference numbers, and checkbox-style options (e.g. an "ARCHIVE LOCATION VARIANCE SHEET" listing "THE NUMBER (RANGE) 2060574004-2060574012 IS LOCATED: ( ) IN THE AUDIO CABINET ( ) IN THE VIDEO CABINET ( X ) ON THE OVERSIZE SHELF ...") — is a presentation (this check), not a form."
    *   This is a "VARIANCE SHEET". It looks like a status sheet for reproduction/archiving.
    *   Let's check Check 10: ADMINISTRATIVE FORM. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A QA/parameter review sheet."
    *   The document is a "VARIANCE SHEET" for reproduction. It has checkboxes. It is filled out (checked "POOR QUALITY ORIGINAL" and "OTHER").
    *   Is it a form or a presentation?
    *   Check 9 caveat: "a one-page status/location display sheet ... is a presentation (this check), not a form."
    *   This sheet is checking variances/motivations during reproduction. It's a status sheet.
    *   However, let's look at the structure. It's a form with checkboxes.
    *   Let's re-read Check 9 carefully. "a one-page status/location display sheet — a titled sheet stating where a record range or item is located... is a presentation". This sheet states "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE". It's a status sheet about the reproduction process.
    *   Let's look at Check 10: "administrative form... QA/parameter review sheet". This looks like a QA sheet for reproduction. "POOR QUALITY ORIGINAL", "OVERLAY ITEM COULD NOT BE REMOVED". This is a QA/parameter review sheet or a reproduction log.
    *   Wait, is it a form? "Filled or blank fields, boxes, checkboxes... for capturing factual data". Yes, it captures data about the reproduction variance.
    *   Let's look at the "presentation" definition again. "Slide/overhead layouts... deck title... meeting/program/speaker cover page... corporate press release... photographic slide image... near-blank cover... section divider... speech text... one-page status/location display sheet".
    *   The "one-page status/location display sheet" example is "ARCHIVE LOCATION VARIANCE SHEET". This is a "VARIANCE SHEET".
    *   The text says: "BRONX & WILLIAMSBURG - LOUISVILLE". This looks like a location or project name.
    *   The content is checking boxes about the reproduction quality.
    *   Is this a "status/location display sheet"? It's a status sheet about the reproduction.
    *   Let's compare Check 9 and Check 10.
    *   Check 10: "administrative form... QA/parameter review sheet". This fits perfectly. It's a sheet reviewing parameters (quality, sequence, missing pages) of a reproduction.
    *   Check 9: "one-page status/location display sheet... stating where a record range or item is located". This sheet isn't stating where a record is located. It's stating what variances were made during reproduction.
    *   So it's likely a form (Check 10).
>     *   Wait, let's look at the layout. It's a page with a white box in the middle (the document being scanned?) and the text is inside that box?
    *   Actually, the image shows a scanned page. The main content is inside a white rectangle. The background is noisy/grainy (scan artifact).
    *   The text is centered. "VARIANCE SHEET".
    *   It has checkboxes.
    *   It has handwritten text.
    *   This is a filled form. "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
    *   So Check 10 (form) seems strong.
>     *   Let's re-evaluate Check 9 (presentation).
    *   "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead — presentation".
    *   Here, there is a noisy background, but the text is a structured form.
    *   The "VARIANCE SHEET" is a form used in records management / archiving.
    *   "BRONX & WILLIAMSBURG - LOUISVILLE" -> locations.
    *   "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE:" -> likely "MODIFICATIONS" or "OBSERVATIONS". Actually, looking very closely at crop 2: "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE:" -> "MODIFICATIONS"? No, "MOTIVATIONS"? Maybe "CONDITIONS"? "AT THE TIME OF REPRODUCTION THE FOLLOWING CONDITIONS WERE MADE"? No. "AT THE TIME OF REPRODUCTION THE FOLLOWING NOTES WERE MADE"?
    *   Let's assume it's a form.
>     *   Let's look at the "NOTICE" box at the bottom: "If the file image is less clear than this notice, it is due to the quality of the document being filmed." This is a standard notice for microfilm/archival reproduction.
    *   This document is a "Variance Sheet" used during the filming/reproduction process to note issues.
    *   This is an administrative form for records management / archiving.
    *   Check 10: "administrative form... records-management inventory or log table... QA/parameter review sheet". This fits "QA/parameter review sheet" or just a form for capturing data about the reproduction.
>     *   Is there any other category?
    *   Check 1: file_folder. No, it has content.
    *   Check 11: Correspondence. No.
    *   Check 12: News article. No.
    *   Check 13: Scientific report. No.
    *   Check 14: Advertisement. No.
>     *   So it's between Form (10) and Presentation (9).
    *   The "one-page status/location display sheet" in Check 9 is a specific exception. "e.g. an 'ARCHIVE LOCATION VARIANCE SHEET' listing 'THE NUMBER (RANGE)... IS LOCATED...'".
    *   This sheet is a "VARIANCE SHEET". But it's not listing location. It's listing reproduction issues.
    *   "AT THE TIME OF REPRODUCTION THE FOLLOWING [MODIFICATIONS/NOTES/CONDITIONS] WERE MADE".
    *   The checkboxes are about document quality.
    *   This is a QA sheet. Check 10 explicitly mentions "QA/parameter review sheet".
    *   "A research grant application... stays form... Likewise, a QA/parameter review sheet naming an institute, review dates, and testing parameters as labeled fields/entries (not running prose) stays form, not scientific_report".
    *   This sheet has labeled fields (checkboxes) and entries (checked boxes, handwritten text).
    *   So it is a form.
>     *   Wait, is it a "presentation"?
    *   "a one-page status/location display sheet ... is a presentation".
    *   The example is "ARCHIVE LOCATION VARIANCE SHEET".
    *   This is "VARIANCE SHEET".
    *   But the content is different. The example is about location. This is about reproduction quality.
    *   The instruction says: "Judge each page by its FUNCTION".
    *   Function: Capturing data about reproduction variances. This is data capture. -> Form.
    *   The "status/location display sheet" in check 9 is described as "presenting where something is, rather than capturing data for records".
    *   This sheet is capturing data (checking boxes, writing "throughout rest of file"). It's a log/record of what happened during reproduction.
    *   So it's a form.
>     *   Let's check the labels again.
    *   form: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... QA/parameter review sheet."
    *   This fits perfectly.
>     *   Let's double check Check 1 (file_folder).
    *   "A page titled 'RECORDS MANAGEMENT INVENTORY' ... is a form".
    *   This is a "VARIANCE SHEET". It's a form.
>     *   Final decision: form.
>     *   Wait, let's look at the "presentation" check 9 again.
    *   "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead".
    *   The image has a noisy background, but the text is a clear form. The white box is the paper. The background is the scanner bed or something.
    *   Actually, looking at the full image, it looks like a scan of a page that was filmed or is a scan of a microfilm frame?
    *   The "NOTICE" says "If the file image is less clear than this notice, it is due to the quality of the document being filmed."
    *   This implies the document itself is a notice for a filmed document.
    *   The content is the "VARIANCE SHEET".
    *   The variance sheet is a form used by the archivist/reproducer.
    *   So the page *is* the variance sheet.
    *   The variance sheet is a form.
>     *   Let's check if it could be a "presentation" because of the layout.
    *   The layout is centered text, checkboxes. It's not a slide deck.
    *   It's a form.
>     *   One more check: Check 4 (questionnaire).
    *   "The page asks the reader to answer...". No, it's a sheet for the reproducer to fill out, not a survey for a respondent. Although it has checkboxes, it's a QA sheet.
>     *   So, Form (Check 10).
>     *   Wait, is there any chance it's "file_folder"?
    *   "A page whose content is a physical folder tab... is file_folder".
    *   This is not a folder tab. It's a full page document.
>     *   Is there any chance it's "handwritten"?
    *   "Most of the content is freeform handwriting". No, mostly typed checkboxes. Handwriting is just "throughout rest of file".
>     *   So, Form.
>     *   Let's refine the scratchpad.
    *   Check 1: file_folder. No, has body content (checkboxes, text). Not a folder tab.
    *   Check 2: handwritten. No, mostly typed.
    *   Check 3: Fax. No.
    *   Check 4: Questionnaire. No, not a survey instrument for respondents. It's a reproduction variance sheet.
    *   Check 5: Resume. No.
    *   Check 6: Publication. No.
    *   Check 7: Financial. No.
    *   Check 8: Specification. No.
    *   Check 9: Presentation. No. The "status/location display sheet" exception is for sheets stating location (e.g. "IS LOCATED: ..."). This sheet captures reproduction data (QA/parameter review). Also, layout is not sparse slide-like, it's a structured form.
    *   Check 10: Form. Yes. "Filled or blank fields, boxes, checkboxes... QA/parameter review sheet". The page is a "VARIANCE SHEET" with checkboxes for reproduction issues (Poor quality, overlay item, etc.) and handwritten specification. It captures factual data about the reproduction process.
    *   Check 11: Correspondence. No.
    *   Check 12: News. No.
    *   Check 13: Scientific report. No.
    *   Check 14: Advertisement. No.
>     *   Runner-up: presentation. Ruled out because it's a structured form capturing reproduction data (QA sheet), not a status/location display sheet or slide deck. The "Variance Sheet" is a form for records management/reproduction logging.
>     *   Wait, is "VARIANCE SHEET" a form? Yes.
    *   "administrative form... QA/parameter review sheet". Yes.
>     *   Final label: form.

---

## budget → scientific_report (1 errors)

### `rvl_cdip__budget__0010.png`
**Expected:** `budget` | **Predicted:** `scientific_report`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "Tobacco Institute" logo, "cigarette tax data" title, address. Not a newspaper/magazine masthead or journal running head. It's a report header.
> **Check 1: file_folder**
- Evidence: The page has a title "Monthly State Cigarette Tax Report", paragraphs of text, a note, and a Bates number "THLBC 005161". It has real content.
- Not this check.
> **Check 2: handwritten**
- Evidence: The text is typed. There is a "RECEIVED" stamp and a date "20 1990" (looks like a stamp). No majority handwriting.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax cover sheet header. The "RECEIVED" stamp is a receiving stamp, not a fax transmission header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey questions, rating scales, or transmittal note about a survey.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: No CV or resume content.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal name, volume, issue, page range, or DOI on the page itself. The header is "Tobacco Institute cigarette tax data".
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: The document is a "Monthly State Cigarette Tax Report". It discusses tax collections, package counts, tax rates.
- Is it an invoice? No, it's not billing a vendor or client for goods/services. It's a report on tax data.
- Is it a budget? "internal money planning, tracking, or disbursement... financial or money-data table... statement of account". This is a report on tax collections. Wait, let's look closer.
- "Sales tax collections for the 41 states... amounted to approximately $93.2 million".
- "The aggregate of the cigarette taxes... was $329,259,463."
- This looks like a report. Is it a scientific_report? Or a form? Or a presentation?
- Let's check the other categories.
- Check 7 says: "financial or money-data table (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures), and a handwritten list of budget categories and dollar amounts... is budget". This page has money data (tax collections, package counts). But it's a report with running prose.
- Wait, check 7 says: "If the page is otherwise formatted as correspondence (letterhead + external address + "Dear ..." salutation + prose + closing signature, or a TO:/FROM:/RE: memo header followed by prose) and a dollar figure... classify it as correspondence". This is not correspondence.
- Check 7 says: "A technical/project status report whose content is primarily technical... is scientific_report (check 13), even if it embeds a budget-vs-actual COSTS section". This is a report on tax data.
- Let's look at Check 13: scientific_report. "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page...". This is a report from the Tobacco Institute about cigarette tax data. It has running prose: "In February 1989, cigarette taxes in the 50 states...". It discusses volume, percentages, aggregate taxes.
- Is it a scientific_report? It's a technical report / data report. "Monthly State Cigarette Tax Report".
- Let's re-read Check 7 budget definition: "financial or money-data table... is budget". This is not a table, it's prose. "A statement of account... is budget". This is a report.
- Let's look at Check 13 again. "Original research write-up... Running narrative prose with objectives, methods, results, or discussion". This is a report of data. "technical/project status report whose content is primarily technical... is scientific_report". This is a report on tax data.
- Wait, is there a better fit?
- Let's look at the labels: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
- The document is a "Monthly State Cigarette Tax Report" from the Tobacco Institute. It contains running prose describing tax data.
- Could it be a memo? No TO/FROM/RE header.
- Could it be a letter? No salutation/closing.
- Could it be a presentation? No, it's a text report.
- Could it be a scientific_report? Yes, it's a technical report with running prose about data (tax collections, package volumes). The Tobacco Institute produces these reports. It fits "scientific_report" as a technical report/write-up, or maybe just a report. Wait, the labels don't have "report" except "scientific_report".
- Let's check if it fits "budget". Budget is "internal money planning, tracking... financial or money-data table". This is a report on tax collections. It's not internal planning. It's a published (internal) report.
- Let's check "scientific_report". "Running narrative prose with objectives, methods, results, or discussion". This page has results (tax collections, package counts). It's a technical report.
- Let's check "form". No fields/boxes.
- Let's check "specification". No product data.
> Let's reconsider the content. It's a report on cigarette tax data.
"In February 1989, cigarette taxes in the 50 states and the District of Columbia were imposed on 1,794,409,000 packages."
This is a data report.
Is it a scientific_report? The instructions say: "scientific_report requires running prose". This has running prose. "A technical/project status report whose content is primarily technical... is scientific_report". This is a technical report on tax data.
Wait, is there a category for "report"? No, only "scientific_report".
Let's look at the labels again.
Maybe it's a "budget"? No, it's not internal planning.
Maybe it's a "form"? No.
> Let's look at the pre-scan and checks again.
Check 13: scientific_report. "Running narrative prose with objectives, methods, results, or discussion... a technical/project status report whose content is primarily technical... is scientific_report". This document is a report (Monthly State Cigarette Tax Report) with running prose describing results (tax collections, package counts). It fits scientific_report best among the options, as it's a technical report from an institute.
> Wait, is it a "news_article"? No masthead.
Is it a "presentation"? No.
> Let's look at the "Tobacco Institute" header. It's a letterhead-like header but no address to external person.
"cigarette tax data" is the title.
"Monthly State Cigarette Tax Report" is the subtitle.
"Report for February 1989".
> This is a report. In this classification scheme, technical reports with running prose are often classified as scientific_report.
Let's check if there's any other fit.
"financial or money-data table... is budget". This is not a table. It's prose.
"A technical/project status report whose content is primarily technical... is scientific_report". This is a report on tax data.
> Let's assume scientific_report.
> Wait, let's look at Check 7 again. "budget: ... financial or money-data table ... is budget". This is not a table.
"invoice: ...". No.
> So it's scientific_report.
> Let's double check Check 11: memo.
"internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
The header is "Tobacco Institute cigarette tax data ... 1875 I Street...". Then "Monthly State Cigarette Tax Report". Then "Report for February 1989". Then prose.
No TO/FROM/RE header. So not a memo.
> Check 11: letter.
"letterhead with an external recipient address...". No external address.
> So it's scientific_report.
> Evidence for scientific_report: Running narrative prose describing tax data (package counts, tax aggregates, percentages) in a "Monthly State Cigarette Tax Report" format. It is a technical report/write-up.
> Wait, is there any chance it's a "form"? No fields.
Is it a "specification"? No.
> Final decision: scientific_report.
> One more check: "A technical-study title page naming a specific experimental method/study is scientific_report". This is a report page.
"Running narrative prose with objectives, methods, results, or discussion". This page has results (data on tax collections).
> Let's refine the scratchpad.
- file_folder: no, has body content.
- handwritten: no, typed.
- fax: no.
- questionnaire: no.
- resume: no.
- scientific_publication: no journal ID.
- financial (invoice/budget): The page contains money data ($93.2 million, $329 million), but it is formatted as a narrative report ("Report for February 1989", paragraphs of text), not a line-item table, ledger, or budget tracking sheet. Check 7 says financial content must be the page's primary structure (line-item table, ledger, etc.) or a money-data table. This is prose. Check 7 caveat: "A technical/project status report whose content is primarily technical... is scientific_report, even if it embeds a budget-vs-actual COSTS section". This is a report on tax data (technical/administrative data), so it falls under scientific_report.
- specification: no.
- presentation: no, dense prose.
- form: no fields.
- correspondence: no memo/letter structure (no TO/FROM/RE, no salutation/closing).
- news_article: no masthead.
- scientific_report: yes, running narrative prose reporting on cigarette tax data (results/data).
- advertisement: no.
> Runner-up: budget. Ruled out because the page is a narrative report, not a financial table, ledger, or internal planning document; the money figures are data points in a report, not the primary structure for tracking/planning.
> Wait, is "Monthly State Cigarette Tax Report" a scientific report? It's a report from the Tobacco Institute. In this dataset (tobacco archive), these reports are often classified as scientific_report if they have running prose and technical data. The instructions say "scientific_report requires running prose". This has it.
> Let's confirm the label: scientific_report.

---

## email → form (1 errors)

### `rvl_cdip__email__0005.png`
**Expected:** `email` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** I see "From:", "Date:", "Name:", "To:". Wait, let's look closer.
    - "Phone Message for Staples, Sharon"
    - "From: Staples, Sharon"
    - "Date: Mon, Aug 25, 1997 12:43 PM"
    - "Name: Janet Lojeski"
    - "To: Ropp, Kevin"
    - "Left you a voicemail message."
    - This looks like a voicemail transcript or a phone message log, not an email. The headers are "From:", "Date:", "Name:", "To:". It's not a standard email header (From/To/Sent/Subject). Wait, let's check the rules. "email: mail-client header block (From/To/Sent/Subject, cc, attachments) or a forwarded/threaded mail trail." This has From, To, Date. But it says "Phone Message for Staples, Sharon". And "Name: Janet Lojeski". "Telephoned". "Left you a voicemail message." This is a phone message log/voicemail transcript. Is it an email? No, it doesn't have "Subject:" or "Sent:". It looks like a printed voicemail message. Let's look at the memo/letter rules.
- **Masthead/Running head:** There is a vertical number "2075247924B" on the right side. This looks like a Bates number. No masthead.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder.**
    *   Evidence: "Phone Message for Staples, Sharon", "From: Staples, Sharon", "Date: Mon, Aug 25, 1997 12:43 PM", "Name: Janet Lojeski", "To: Ropp, Kevin", "Left you a voicemail message."
    *   There is actual content (a message). It's not just an ID.
    *   Not file_folder.
> *   **Check 2: handwritten.**
    *   Evidence: Text is typed. "Left you a voicemail message." is typed.
    *   Not handwritten.
> *   **Check 3: FAX TRANSMISSION SHEET.**
    *   Evidence: No "FACSIMILE" header. The vertical text "2075247924B" is a Bates number.
    *   Not a fax sheet.
> *   **Check 4: questionnaire.**
    *   Evidence: No questions to answer.
    *   Not questionnaire.
> *   **Check 5: resume.**
    *   Evidence: No career history.
    *   Not resume.
> *   **Check 6: scientific_publication.**
    *   Evidence: No journal header.
    *   Not scientific_publication.
> *   **Check 7: financial document.**
    *   Evidence: No money.
    *   Not financial.
> *   **Check 8: specification.**
    *   Evidence: No product data.
    *   Not specification.
> *   **Check 9: presentation.**
    *   Evidence: Sparse text, but it's a message. Not a slide deck.
    *   Not presentation.
> *   **Check 10: administrative form.**
    *   Evidence: It has fields "From:", "Date:", "Name:", "To:". It looks like a form for a phone message. But let's check correspondence first.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter.**
    *   **Email:** "From:", "To:", "Date:". But no "Subject:". And the content is "Phone Message for Staples, Sharon". "Name: Janet Lojeski". "Telephoned". "Left you a voicemail message." This is a voicemail message log. Is it an email? The rules say: "email: mail-client header block (From/To/Sent/Subject, cc, attachments) or a forwarded/threaded mail trail." This doesn't have Subject. It has "Name:". It looks like a printed voicemail message from a phone system.
    *   **Memo:** "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". Here we have "From:", "Date:", "Name:", "To:". The content is "Left you a voicemail message." This is very short.
    *   **Letter:** "letterhead with an external recipient address...". No.
    *   Let's re-evaluate "memo". "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... is a memo". Here "To: Ropp, Kevin". "From: Staples, Sharon". "Name: Janet Lojeski". This looks like a phone message record.
    *   Wait, is this a "memo"? The headers are "From:", "Date:", "Name:", "To:". This is a standard phone message pad format.
    *   Let's look at the labels again. `memo`, `letter`, `email`.
    *   Is it a `form`? "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". A phone message log is a form capturing data (who called, who it's for, message).
    *   Let's look at Check 10: "administrative form". A phone message log is a form.
    *   Let's look at Check 11 again. "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". This page has "From:", "Date:", "Name:", "To:". It lacks "RE:" or "SUBJECT:". The content is "Left you a voicemail message." This is not really memo-style prose. It's a log entry.
    *   Let's look at the "Phone Message" title. "Phone Message for Staples, Sharon".
    *   This is a printed voicemail message.
    *   Is there a better category?
    *   Let's reconsider `email`. Sometimes voicemail transcripts are emailed. But the headers are "From:", "Date:", "Name:", "To:". An email would have "From:", "To:", "Date:", "Subject:". This has "Name:". This is typical of a phone system printout (like a Cisco IP phone message log).
    *   Is it a `memo`? A memo is correspondence. A phone message is a record.
    *   Let's look at the definition of `form` (Check 10): "Filled or blank fields... for capturing factual data". This page has fields "From:", "Date:", "Name:", "To:" filled in. "Left you a voicemail message." is the content. This fits "form" well. It's a filled phone message form.
    *   Wait, is it a `memo`? "A dated internal note addressed to a named person...". "To: Ropp, Kevin". "From: Staples, Sharon". "Name: Janet Lojeski". This is a note from Janet Lojeski to Kevin Ropp (via Staples, Sharon?). "Left you a voicemail message."
    *   Actually, let's look at the structure.
        *   Title: Phone Message for Staples, Sharon
        *   From: Staples, Sharon
        *   Date: Mon, Aug 25, 1997 12:43 PM
        *   Name: Janet Lojeski
        *   [Bullet] Telephoned
        *   To: Ropp, Kevin
        *   Left you a voicemail message.
    *   This is a voicemail message record.
    *   Is it a `form`? Yes, it's a structured record.
    *   Is it a `memo`? It has To/From/Date. But it lacks the memo structure (RE/Subject, prose body). The body is just "Left you a voicemail message." and "Telephoned".
    *   Let's check `email` again. "mail-client header block (From/To/Sent/Subject...)". This has From, To, Date. But "Name:" is not standard email. And "Phone Message" title. It's likely a printout from a phone system.
    *   Let's check `file_folder`. No, it has content.
    *   Let's check `handwritten`. No.
>     Let's go back to `form` (Check 10).
    "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
    This page has labeled fields: From, Date, Name, To. And the content "Left you a voicemail message."
    This is a filled form (a phone message log).
>     Wait, is there a `memo` possibility?
    "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
    This has From, Date, To. But no RE/SUBJECT. And the text is "Left you a voicemail message." This is not really prose.
    Also, the title is "Phone Message for...".
>     Let's look at the labels again.
    `advertisement`, `budget`, `email`, `file_folder`, `form`, `handwritten`, `invoice`, `letter`, `memo`, `news_article`, `presentation`, `questionnaire`, `resume`, `scientific_publication`, `scientific_report`, `specification`.
>     If I have to choose between `form` and `memo`.
    A phone message slip is a form.
    The text "Left you a voicemail message" is the message content.
    The fields are filled.
    So `form` seems appropriate.
>     Let's check if it could be `email`.
    Some systems print emails with headers. But "Name: Janet Lojeski" is weird for an email. Usually it's "From: Janet Lojeski <email>". Here "From: Staples, Sharon". "Name: Janet Lojeski". This implies Janet called, and the message is for Sharon Staples.
    "To: Ropp, Kevin".
    This is a message *for* Sharon Staples, *from* Janet Lojeski (who telephoned), *to* Kevin Ropp? Or is it a message *from* Sharon Staples *to* Kevin Ropp?
    "Phone Message for Staples, Sharon".
    "From: Staples, Sharon". (Maybe Sharon is the sender of the message log?)
    "Name: Janet Lojeski". (The person who called?)
    "To: Ropp, Kevin". (The recipient?)
    "Left you a voicemail message." (The content).
    This is a voicemail transcript/log.
    Voicemail logs are forms.
>     Let's look at Check 11 again. "email: mail-client header block...". This is not a mail-client header. It's a phone system header.
    "memo: ... TO:/FROM:/RE:/SUBJECT:/DATE: ...". This lacks RE/SUBJECT.
    "letter: ... external recipient address ...". No.
>     So it's likely `form`.
>     Wait, let's look at the "Phone Message" title.
    Is it a `memo`?
    "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... is a memo".
    Here "To: Ropp, Kevin". No title/division.
    "From: Staples, Sharon". No title.
    So not a memo by the strict rule.
>     So `form` (Check 10) is the best fit. "Filled or blank fields... for capturing factual data". This captures who called, who it's for, date, and the message.
>     Let's re-read Check 10 carefully.
    "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
    "This also covers: ... internal authorization/approval forms with an approval signature/date block."
    A phone message log is a form for capturing a message.
>     Let's consider `email` again.
    Sometimes faxed documents have headers.
    "A FAX machine transmission header ('SENT BY:', phone number, '# N/N') is NOT an email header".
    This doesn't have that.
>     What about `file_folder`?
    "Almost no body content: only an archive/Bates number...".
    This has body content: "Left you a voicemail message."
    So not file_folder.
>     So `form` seems correct.
>     Wait, is there any other category?
    `scientific_report`? No.
    `specification`? No.
>     Let's look at the vertical text "2075247924B". This is a Bates number.
    Bates numbers are on almost everything in this archive.
>     Let's look at the layout.
    Top: "Phone Message for Staples, Sharon" with a line under it.
    Left side:
    From: Staples, Sharon
    Date: Mon, Aug 25, 1997 12:43 PM
    Name: Janet Lojeski
    [bullet] Telephoned
    To: Ropp, Kevin
    Body: "Left you a voicemail message."
>     This is a structured record. It's a form. Specifically, a phone message form.
>     Let's check if it could be `memo`.
    The instructions say: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
    This has From, Date, To. But no RE/SUBJECT. And the text is very short.
    Also, the title "Phone Message for..." suggests it's a log entry, not a memo.
>     Let's check `email`.
    "email: mail-client header block (From/To/Sent/Subject, cc, attachments)".
    This has From, To, Date. But "Name:" is not standard. And "Phone Message" title.
    It's likely a printout from a phone system (like a Cisco CallManager message log). These are forms.
>     So, `form`.
>     Wait, is there a chance it's `email`?
    If this was an email forwarded as a message?
    "From: Staples, Sharon"
    "To: Ropp, Kevin"
    "Date: ..."
    "Name: Janet Lojeski" -> This is weird for email.
    "Left you a voicemail message." -> This is the body.
    If it's a voicemail transcript, it's a form.
>     Let's look at the "Runner-up" requirement.
    "add one final line naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out."
>     If I pick `form`:
    Runner-up: `memo`. Evidence: It has From/To/Date fields, but lacks the full memo header (RE/SUBJECT) and memo-style prose structure; it's a structured log entry (phone message).
    Or runner-up: `email`. Evidence: It has From/To/Date, but lacks Subject and mail-client formatting; it's a phone message log.
>     Let's refine the `form` evidence.
    Check 10: "Filled or blank fields... for capturing factual data".
    Evidence: Labeled fields "From:", "Date:", "Name:", "To:" filled with data ("Staples, Sharon", "Mon, Aug 25...", "Janet Lojeski", "Ropp, Kevin") and a message field "Left you a voicemail message." This is a filled phone message form.
>     Let's check if it's `file_folder`.
    "A page is NOT file_folder if it carries any real content... a note."
    "Left you a voicemail message" is a note. So not file_folder.
>     Let's check `handwritten`.
    Text is typed.
>     So `form` is the label.
>     Wait, is there a category for "message"? No.
    The categories are: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
>     A phone message log is a form.
>     One distinct possibility: Is this an `email`?
    Some email clients print messages with headers.
    But "Name: Janet Lojeski" is not an email header.
    And "Phone Message for..." is a title.
    This is definitely a phone message log.
>     Final decision: `form`.
>     Wait, let's look at Check 11 again.
    "memo: ... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... is a memo".
    Here "To: Ropp, Kevin". No title.
    "From: Staples, Sharon". No title.
    So not memo.
>     "letter: ... external recipient address ...". No.
>     So `form` is the best fit.
>     Let's double check Check 1.
    "file_folder: Almost no body content... A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
    "Left you a voicemail message" is a note. So not file_folder.
>     So `form`.
>     Scratchpad:
    - file_folder: no — page has body content ("Phone Message...", "Left you a voicemail message"), not just an ID.
    - handwritten: no — text is typed.
    - fax: no — no fax header.
    - questionnaire: no — no questions.
    - resume: no.
    - scientific_publication: no.
    - financial: no.
    - specification: no.
    - presentation: no.
    - form: yes — page has labeled fields ("From:", "Date:", "Name:", "To:") filled with factual data ("Staples, Sharon", date, "Janet Lojeski", "Ropp, Kevin") and a message ("Left you a voicemail message."). This is a filled phone message log/form.
    - correspondence (email/memo/letter): no — lacks email headers (Subject, Sent), lacks memo headers (RE, Subject, internal titles), lacks letter structure (salutation, closing). It's a structured log.
    - news_article: no.
    - scientific_report: no.
    - advertisement: no.
>     Runner-up: memo. Ruled out because it lacks the full TO/FROM/RE/SUBJECT/DATE header block and memo-style prose; it is a structured phone message log with labeled fields.
    Or runner-up: email. Ruled out because it lacks mail-client headers like Subject/Sent and has "Name:" field which is typical of phone systems, not email.
>     Actually, looking closely at the text:
    "Phone Message for Staples, Sharon"
    "From: Staples, Sharon"
    "Date: Mon, Aug 25, 1997 12:43 PM"
    "Name: Janet Lojeski"
    "• Telephoned"
    "To: Ropp, Kevin"
    "Left you a voicemail message."
>     This is a voicemail message record. It's a form.
>     One final check: Could it be `email`?
    If this is a printout of an email that says "Phone Message for...".
    But "Name: Janet Lojeski" is not an email field.
    And "• Telephoned" is not email content.
    It's a phone system printout. Phone system printouts are forms.
>     Final label: `form`.

---

## form → file_folder (1 errors)

### `rvl_cdip__form__0004.png`
**Expected:** `form` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** None.
- **Masthead/Running head:** There is text "Insecticides" at the top right (rotated) and "51303 2938" at the bottom right (rotated). Wait, let's look at the orientation. The text "Insecticides" is at the top right, running vertically. "51303 2938" is at the bottom right, running vertically. This looks like a folder tab or a section divider.
- Let's re-orient. If I rotate the image 90 degrees clockwise:
    - Top: "Insecticides" (rotated 90 deg counter-clockwise relative to normal reading, so if I rotate image 90 deg clockwise, "Insecticides" is at the top right, reading left-to-right? No.
    - Let's look at the text "Insecticides". It is vertical, reading top-to-bottom. Wait, "I-n-s-e-c-t-i-c-i-d-e-s". The 'I' is at the top. So it reads top-to-bottom.
    - "51303 2938". '5' is at the top. Reads top-to-bottom.
    - Actually, let's look at the layout. There is a black bar on the right edge (and bottom edge). This looks like a photographed folder tab or a slide.
    - Wait, the black bar is on the right side and bottom side.
    - Let's look at the text orientation. "Insecticides" is near the top right corner. "51303 2938" is near the bottom right corner.
    - If I rotate the image 90 degrees counter-clockwise: "Insecticides" is at the top, reading left-to-right. "51303 2938" is at the bottom right.
    - Let's assume the text is meant to be read horizontally. If I rotate 90 deg CCW:
        - Top right: "Insecticides".
        - Bottom right: "51303 2938".
    - This looks like a folder tab. The text "Insecticides" is a short label. The number "51303 2938" looks like a Bates number or archive number.
    - There is a black bar along the right edge and bottom edge. This is characteristic of a photographed folder tab (the folder body is the black bar).
> **2. Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Content: "Insecticides" (short label), "51303 2938" (Bates number/archive number).
- Is there a bold headline title? "Insecticides" is a short label.
- Is it a folder tab? The black bar along the right and bottom edges suggests a photographed folder tab. The label "Insecticides" names the folder's contents.
- "A short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... is a filing label, not a bold headline title... The page stays file_folder even when the label is rotated 90 degrees".
- The text "Insecticides" is rotated 90 degrees (vertical).
- The number "51303 2938" is a Bates number.
- This fits the "folder-tab pages" description perfectly. "a short filing label that names the folder's contents... usually with a Bates number stamped on the folder body... The black bar is the photographed folder body/tab edge".
- So, Check 1 matches.
> **3. Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- No handwriting.
> **4. Check 3: FAX TRANSMISSION SHEET -> form**
- No fax header.
> **5. Check 4: SURVEY INSTRUMENT -> questionnaire**
- No.
> **6. Check 5: PERSON'S CAREER HISTORY -> resume**
- No.
> **7. Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- No journal header. "Insecticides" is just a label.
> **8. Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- No financial content.
> **9. Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- No.
> **10. Check 9: SLIDE DECK -> presentation**
- "A near-blank cover or title page... is a presentation... not file_folder."
- EXCEPTION: "a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab... is a folder-tab label and stays file_folder".
- "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide... BUT this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB".
- This page has a solid black bar (right and bottom edges) and sparse text ("Insecticides", "51303 2938").
- However, the text "Insecticides" is a short filing label naming the folder contents. The black bar is the folder body.
- So it is file_folder, not presentation.
> **11. Check 10: ADMINISTRATIVE FORM -> form**
- No fields.
> **12. Check 11: CORRESPONDENCE -> email, memo, letter**
- No.
> **13. Check 12: PUBLISHED JOURNALISM -> news_article**
- No.
> **14. Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- No prose.
> **15. Check 14: PROMOTIONAL MATERIAL -> advertisement**
- No.
> **Conclusion:**
The page is a photograph of a file folder tab. The label is "Insecticides". The number is "51303 2938" (Bates number). The black bar is the folder body. This is Check 1: file_folder.
> Let's double check the "presentation" caveat.
"A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider even alongside a small handwritten letter/number annotation — but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab (product/collection/month/file name, e.g. 'NEWTROL', 'Litigation Content', 'FEBRUARY') is a folder-tab label and stays file_folder (check 1)."
"Insecticides" is a short filing label naming the folder's contents (a collection of documents about insecticides).
The black bar is the folder body.
So it is file_folder.
> Final check of the text:
"Insecticides" (top right, vertical)
"51303 2938" (bottom right, vertical)
Black border on right and bottom.
This is a folder tab scan.
> Label: file_folder.

---

## form → memo (1 errors)

### `rvl_cdip__form__0008.png`
**Expected:** `form` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is a date "10-29-89" and names "Beverly Monroe - x3817/Chris Hardin - x2823". This looks like a fax transmission header or a memo-like note, but let's look closer. Wait, "LAW DEPARTMENT - PATENT SECTION" is at the bottom.
- **Masthead/Running head:** No newspaper masthead. No journal running head. There is a Bates number "2024027224" rotated on the right side.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: There is a Bates number "2024027224". There is a black bar on the left and right edges. Wait, looking closely at the layout.
    *   The text is in the center: "Date 10-29-89", "Attached is the patent(s) you requested...", "LAW DEPARTMENT - PATENT SECTION Beverly Monroe - x3817/Chris Hardin - x2823".
    *   There is a checkmark next to the first line "Attached is the patent(s) you requested."
    *   This looks like a fax cover sheet or a transmittal note.
    *   Is it a folder tab? No, it's a piece of paper with text. The black bars look like scan artifacts or maybe the edges of a folder, but the text is clearly a message.
    *   Wait, let's look at the "folder tab" rule. "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body."
    *   Here, the text is a message: "Attached is the patent(s) you requested...". This is content. It's not just a filing label.
    *   So, not file_folder.
> *   **Check 2: handwritten**
    *   Evidence: "Date 10-29-89" is handwritten. The checkmark is handwritten. The rest is typed.
    *   Most content is typed. Not majority handwritten.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: "FACSIMILE", "FAX COVER SHEET"? No.
    *   Wait, is this a fax cover sheet? It has "Date", checkboxes for attached items ("Attached is the patent(s)..."), and a signature/contact block at the bottom ("LAW DEPARTMENT - PATENT SECTION Beverly Monroe...").
    *   It looks like a fax cover sheet or a transmittal memo.
    *   Let's check the definition: "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header..."
    *   This page doesn't have that specific header. It looks like a generic transmittal note.
> *   **Check 4: QUESTIONNAIRE**
    *   Evidence: No survey questions.
> *   **Check 5: RESUME**
    *   Evidence: No.
> *   **Check 6: SCIENTIFIC_PUBLICATION**
    *   Evidence: No journal header.
> *   **Check 7: FINANCIAL DOCUMENT**
    *   Evidence: No money.
> *   **Check 8: SPECIFICATION**
    *   Evidence: No product specs.
> *   **Check 9: PRESENTATION**
    *   Evidence: No slide deck layout.
> *   **Check 10: ADMINISTRATIVE FORM**
    *   Evidence: It has fields (Date, checkboxes). But is it a form capturing data? It's a transmittal note. "Attached is the patent(s) you requested." It's a message.
> *   **Check 11: CORRESPONDENCE (email, memo, letter)**
    *   Let's look at the structure.
    *   "Date 10-29-89"
    *   Checkboxes: "Attached is the patent(s) you requested." (Checked)
    *   "Attached is a patent(s) that may be of interest to you."
    *   "Attached for your files is a copy of your recently issued patent."
    *   "Other _______"
    *   Bottom: "LAW DEPARTMENT - PATENT SECTION Beverly Monroe - x3817/Chris Hardin - x2823"
    *   This is a memo or a letter.
    *   It is addressed to "Chris Hardin" (implied, or maybe Beverly Monroe is sending to Chris Hardin? "Beverly Monroe - x3817 / Chris Hardin - x2823"). Usually, this format "Sender - ext / Recipient - ext" or "From / To".
    *   Actually, "Beverly Monroe - x3817/Chris Hardin - x2823" looks like "From: Beverly Monroe ... To: Chris Hardin ...". Or it's the contact info.
    *   Let's re-read the memo rule: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
    *   This doesn't have TO/FROM/RE headers explicitly.
    *   Rule: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo".
    *   Here, we have a date "10-29-89". We have names "Beverly Monroe" and "Chris Hardin". We have internal extensions "x3817", "x2823". This indicates internal communication.
    *   The text is "Attached is the patent(s) you requested..." This is memo-style prose (short, functional).
    *   Is it a letter? No external address, no "Dear...", no closing signature (though there are names at the bottom).
    *   Is it an email? No mail-client header. The pre-scan says "A FAX machine transmission header... is NOT a mail-client header". This looks like a faxed document or a memo sent via fax.
    *   Wait, is this a "FAX TRANSMISSION SHEET" (Check 3)?
    *   Check 3 says: "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET'... header". This page doesn't have that header.
    *   However, the layout (checkboxes for attachments, date, names/extensions) is classic fax cover sheet / transmittal memo.
    *   But Check 3 is specific about the header text. If the header text isn't there, it's not Check 3.
    *   Let's look at Check 11 again. "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block... OR a dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose".
    *   Here we have "Date 10-29-89". We have names and extensions (internal). The text is a transmittal note.
    *   This fits "memo" or "letter" (internal note).
    *   Wait, is there a specific category for this?
    *   Let's look at the "folder tab" possibility again (Check 1).
    *   "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body."
    *   The black bars on the left and right look like the edges of a folder or a scan artifact.
    *   But the text is a full message. "Attached is the patent(s) you requested." This is content.
    *   Wait, look at the layout. It's a small box in the middle of a large white page.
    *   The black bars are thick.
    *   Is this a "slide" (Check 9)? "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide".
    *   Here we have black bars on left and right. Text is in the center.
    *   But the text is a memo/transmittal.
    *   Let's reconsider Check 1: file_folder.
    *   "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
    *   This page carries a note: "Attached is the patent(s) you requested." So not file_folder.
>     *   Let's reconsider Check 11: Correspondence.
    *   The text is a transmittal note. "Attached is the patent(s) you requested."
    *   It is addressed to Chris Hardin (internal, x2823) from Beverly Monroe (internal, x3817).
    *   This is a memo. "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo". Here we have Name + Extension (which implies division/internal). "LAW DEPARTMENT - PATENT SECTION" is the division.
    *   So it's a memo.
>     *   Wait, is it a "form"?
    *   Check 10: "Filled or blank fields, boxes, checkboxes... for capturing factual data".
    *   This has checkboxes. But the purpose is to transmit a document (patent).
    *   Check 3: "Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels."
    *   Does this page count as a fax sheet?
    *   The text doesn't say "FAX COVER SHEET". But the layout is extremely characteristic of a fax cover sheet / transmittal memo used in offices (date, checkboxes for what's attached, sender/receiver info).
    *   However, the rule for Check 3 is specific: "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header". This page lacks that specific header text.
    *   The rule for Check 11 says: "A FAX machine transmission header ('SENT BY:', phone number, '# N/N' page count) is NOT an email header... classify the underlying document by its own content (a faxed memo is a memo)".
    *   This document looks like a memo sent via fax (or a fax cover sheet without the big header).
    *   Actually, often these "transmittal" pages with checkboxes are considered memos or forms.
    *   Let's look at the "memo" definition again. "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
    *   This page has "Date 10-29-89". Then the text. Then the names.
    *   It lacks TO/FROM/RE.
    *   But the alternative rule: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo".
    *   Here: Date (10-29-89). Names (Beverly Monroe, Chris Hardin). Extensions (x3817, x2823). Division (LAW DEPARTMENT - PATENT SECTION).
    *   This fits the "dated internal note" memo definition perfectly.
>     *   Wait, is it a "form"?
    *   Check 10 covers "administrative form". A transmittal sheet with checkboxes could be a form.
    *   But Check 11 (Correspondence) usually beats Form if it's a memo/letter.
    *   Wait, the order is: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11...
    *   Check 10 is BEFORE Check 11.
    *   Check 10: "Filled or blank fields, boxes, checkboxes... for capturing factual data".
    *   This page has checkboxes. "Attached is the patent(s) you requested." (Checked).
    *   Is the primary purpose "capturing factual data"? Or is it a transmittal message?
    *   The text says "Attached is...". It's a message.
    *   However, the structure is a form (checkboxes).
    *   Let's check the precedence. "Money function overrides form layout." (Check 7).
    *   "A form does NOT have to be blank — a filled form recording data is still a form".
    *   But Check 11 says: "A page whose primary structure is a memo header + prose... stays memo".
    *   Here the structure is: Date, Checkboxes (message content), Footer (Sender/Receiver).
    *   This is a transmittal memo.
    *   In the tobacco archive, these "Patent Section" transmittal sheets are often memos.
    *   Let's look at Check 3 again. "Fax sheets are forms...". If this is a fax cover sheet, it's a form.
    *   But it lacks the header.
    *   Let's look at the visual evidence.
    *   The page has a Bates number "2024027224".
    *   The text is centered.
    *   There are black bars on the sides. This looks like a scan of a small piece of paper (a note) placed on a larger background, or a fax transmission where the margins are black.
    *   Actually, looking closely at the black bars: they are thick, solid black. This is typical of a scanned folder tab or a slide, BUT the text is a memo.
    *   Wait, Check 9 (Presentation) caveat: "a one-page status/location display sheet... is a presentation". Not this.
    *   Check 1 (file_folder): "Folder-tab pages... label IS filing metadata... page stays file_folder".
    *   Is this a folder tab?
    *   "A short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... bearing a short filing label... usually with a Bates number".
    *   This page has a lot of text: "Attached is the patent(s) you requested...". This is not a short filing label. This is a message.
    *   So not file_folder.
>     *   Let's go back to Check 11: Memo.
    *   Evidence: Date "10-29-89". Internal names "Beverly Monroe - x3817/Chris Hardin - x2823". Division "LAW DEPARTMENT - PATENT SECTION". Text "Attached is the patent(s) you requested."
    *   This is a memo. A transmittal memo.
    *   Is there a better fit?
    *   Check 10: Form. "administrative form... filled or blank fields, boxes, checkboxes".
    *   The page has checkboxes. But the content is a transmittal message.
    *   Usually, a transmittal memo with checkboxes is classified as a memo (correspondence) because its function is communication, not data capture (like a survey or application).
    *   However, the instructions say: "Judge each page by its FUNCTION".
    *   Function: Transmitting a patent document.
    *   This is correspondence (memo).
>     *   Let's check if it's an "email". No mail header.
    *   Let's check if it's a "letter". No external address, no salutation. Internal names + extensions = memo.
>     *   Wait, is this a "form" because it's a "transmittal form"?
    *   Check 10: "administrative form".
    *   Check 3: "Fax sheets are forms".
    *   If this is considered a fax cover sheet (even without the big header), it would be a form.
    *   But the text doesn't say "Fax".
    *   The text is "Date 10-29-89".
    *   The layout is very sparse.
    *   Let's look at the "memo" rule again. "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block... OR a dated internal note addressed to a named person...".
    *   This fits the second part: "dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION".
    *   Name: Chris Hardin (implied recipient). Beverly Monroe (sender).
    *   Division: Law Department - Patent Section.
    *   Extensions: x3817, x2823.
    *   Date: 10-29-89.
    *   Prose: "Attached is the patent(s) you requested."
    *   This is a memo.
>     *   Why might it be a form?
    *   It has checkboxes. "Attached is... [check]". "Attached is... [ ]".
    *   But the purpose is to tell the recipient what is attached. It's a cover note.
    *   Cover notes are memos/letters.
    *   "A cover/transmittal letter keeps its full letter formatting... and is STILL questionnaire... if its prose mentions enclosing...". (Check 4).
    *   Here, it's a transmittal memo.
>     *   Let's look at the black bars again.
    *   "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide... presentation".
    *   Here we have black bars on left and right. Text is sparse (center).
    *   But the text is a memo.
    *   Check 9 caveat: "Technical-study title pages... is scientific_report". Not this.
    *   Check 9: "a near-blank cover or title page... is a presentation".
    *   This is not a cover page. It's a transmittal note.
>     *   Let's reconsider Check 1: file_folder.
    *   "A page is NOT file_folder if it carries any real content... or a note."
    *   This carries a note. So not file_folder.
>     *   Conclusion: It's a memo.
    *   Wait, is it a "form" (Check 10)?
    *   "administrative form... for capturing factual data".
    *   This captures "what is attached" via checkboxes.
    *   But the primary function is communication (transmittal).
    *   In the tobacco archive classification, transmittal memos are often memos.
    *   However, if it's a "Fax Cover Sheet" (Check 3), it's a form.
    *   Does this look like a fax cover sheet? Yes, functionally.
    *   But Check 3 requires specific headers: "FACSIMILE", "FAX COVER SHEET", etc.
    *   This page doesn't have them.
    *   So Check 3 fails.
    *   Check 10 (Form) vs Check 11 (Memo).
    *   Check 10 comes before Check 11.
    *   Check 10: "Filled or blank fields, boxes, checkboxes...".
    *   This page has boxes and checkboxes.
    *   Is it an "administrative form"?
    *   "A form does NOT have to be blank — a filled form recording data is still a form".
    *   But "Money function overrides form layout" (Check 7).
    *   "A page whose primary structure is a memo header + prose... stays memo". (Check 11).
    *   Wait, the checks are ordered 1 to 14.
    *   If Check 10 matches, I stop.
    *   Does Check 10 match?
    *   "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
    *   The checkboxes capture "what is attached". That is factual data (metadata about the attachment).
    *   The "Date" field is filled.
    *   The names are printed.
    *   So it is a filled form.
    *   BUT, is the primary purpose "capturing factual data" (like a survey or application) or "correspondence" (transmitting a document)?
    *   The text "Attached is the patent(s) you requested" is the content.
    *   Usually, a transmittal sheet is a memo.
    *   Let's look at the memo definition in Check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
    *   This page doesn't have TO/FROM/RE.
    *   Alternative memo rule: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo".
    *   This page has Date, Names, Extensions (internal), Division. Prose: "Attached is...".
    *   This fits the memo definition perfectly.
>     *   Conflict: Check 10 (Form - has checkboxes) vs Check 11 (Memo - fits internal note definition).
    *   Order: Check 10 is before Check 11.
    *   If Check 10 has positive evidence, I must stop there.
    *   Evidence for Check 10: "boxes, checkboxes". The page has checkboxes next to the sentences. "Date ___" is a field.
    *   Is this an "administrative form"?
    *   "administrative form... for capturing factual data".
    *   The checkboxes capture which patent is attached. That is factual data.
    *   However, the text is a message.
    *   Let's look at the "Runner-up" logic. "Once an earlier check matches, later checks do not override it."
    *   If I say Check 10 matches, then it's a form.
    *   If I say Check 10 doesn't match (because it's a memo), then I go to Check 11.
    *   Why would Check 10 not match?
    *   "A form does NOT have to be blank...".
    *   "It does NOT cover money records...".
    *   "It does NOT cover product-change authorization...".
    *   Is a transmittal sheet a form?
    *   Often, yes. "Transmittal form".
    *   But if it has memo-style prose and internal addresses, it's a memo.
    *   The instructions say: "Judge each page by its FUNCTION".
    *   Function: Transmitting a patent.
    *   This is a memo (correspondence).
    *   The checkboxes are just part of the memo's content (listing what's attached).
    *   In a memo, you can have a list. "Attached are: [x] Patent A, [ ] Patent B". This is prose/list in a memo.
    *   The layout is sparse.
    *   Let's look at the "memo" rule again. "memo-style prose". "Attached is the patent(s) you requested." is prose.
    *   The checkboxes are like bullet points.
    *   I will bet on **memo**.
>     *   Wait, let's look at the black bars and Bates number.
    *   Bates number: 2024027224.
    *   This is a scanned document from an archive.
    *   The black bars might be the edges of the original paper or scan artifacts.
    *   The text is clearly a transmittal note from the Law Department Patent Section.
    *   "Beverly Monroe - x3817 / Chris Hardin - x2823".
    *   This is internal communication.
    *   Internal communication = memo.
>     *   Let's check if it's a "letter".
    *   "letter: letterhead with an external recipient address...". No external address. Internal extensions. So not letter.
>     *   So it's a memo.
>     *   Wait, is there any chance it's a "form"?
    *   Check 3: "Fax sheets are forms".
    *   If this is a fax sheet (functionally), it's a form.
    *   But Check 3 requires specific text headers. "FACSIMILE", etc.
    *   This page doesn't have them.
    *   So Check 3 is "not this check".
>     *   Check 10: "administrative form".
    *   Does this page capture data? It captures "Date" and "Which patent attached".
    *   But the main text is "Attached is the patent(s) you requested."
    *   This is a note.
    *   "A dated internal note... IS a memo".
    *   The note has checkboxes. That doesn't make it a form if the primary function is a note/memo.
    *   Actually, a form is for "capturing factual data". A memo is for "communication".
    *   This is communication: "Here is the patent you asked for."
    *   So Memo.
>     *   Final check: Check 11.
    *   Evidence: Date "10-29-89". Internal names "Beverly Monroe" (x3817) and "Chris Hardin" (x2823). Division "LAW DEPARTMENT - PATENT SECTION". Text "Attached is the patent(s) you requested."
    *   This is a memo.
>     *   Wait, is it "email"?
    *   Pre-scan: "A mail-client header block...". No.
    *   "A FAX machine transmission header... is NOT a mail-client header".
    *   This looks like a faxed memo. The black bars and sparse text might be from a fax transmission or a scan of a small note.
    *   But the content is a memo.
>     *   One more possibility: **file_folder**.
    *   Check 1: "Folder-tab pages... label IS filing metadata... page stays file_folder".
    *   Is this a folder tab?
    *   The text is "LAW DEPARTMENT - PATENT SECTION". That's a department name.
    *   But the rest is a message.
    *   "Attached is the patent(s) you requested."
    *   A folder tab wouldn't have a message like that. A folder tab would just say "Patents 1989" or "Chris Hardin".
    *   This page has a full message. So not file_folder.
>     *   So, **memo**.
>     *   Wait, let's look at the labels again.
    *   advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
>     *   Is it a **form**?
    *   Some classifications might call a "Transmittal Form" a form.
    *   But the instructions say: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block... OR a dated internal note...".
    *   This fits the "dated internal note" perfectly.
    *   "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo".
    *   Name: Chris Hardin. Division: Law Dept - Patent Section (implied for both, or sender). Extensions confirm internal.
    *   Prose: "Attached is..."
    *   So it's a memo.
>     *   Why would it be a form?
    *   If the checkboxes are considered "fields, boxes, checkboxes... for capturing factual data".
    *   But the "memo" rule is specific about internal notes.
    *   And Check 11 is after Check 10.
    *   If Check 10 matches, I must stop.
    *   Does Check 10 match?
    *   "Filled or blank fields, boxes, checkboxes...". Yes, there are checkboxes.
    *   "for capturing factual data". The checkboxes capture which item is attached.
    *   Is this the *primary* function?
    *   The primary function is to transmit the patent. The checkboxes are a convenience to list what's attached.
    *   In a memo, you can have a list.
    *   "Attached is the patent(s) you requested. [Check] Attached is a patent(s) that may be of interest... [ ]".
    *   This is a checklist within a memo.
    *   I'll stick with **memo**. The "dated internal note" rule is very specific and fits well. The checkboxes are just part of the note's content (indicating what is attached).
>     *   Wait, look at the bottom: "LAW DEPARTMENT - PATENT SECTION Beverly Monroe - x3817/Chris Hardin - x2823".
    *   This looks like a signature block or a routing block.
    *   If it's a routing block, it's still a memo.
>     *   Let's check the scratchpad example for "faxed memo".
    *   "classify the underlying document by its own content (a faxed memo is a memo)".
    *   This is a faxed memo (or a memo sent via fax, indicated by the sparse layout and Bates number).
    *   Content is a memo.
>     *   Final decision: **memo**.
>     *   Wait, is there any evidence for **form**?
    *   Check 10: "administrative form".
    *   If I classify this as a form, the runner-up is memo.
    *   If I classify this as a memo, the runner-up is form.
    *   The text is a transmittal note. Transmittal notes are memos.
    *   The checkboxes are minimal.
    *   I will go with **memo**.
>     *   Wait, let's look at the black bars again.
    *   Check 9: "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide... presentation".
    *   Here we have black bars on left and right. Text is sparse.
    *   But the text is a memo.
    *   Check 9 caveat: "Technical-study title pages... is scientific_report".
    *   Check 9: "a near-blank cover or title page... is a presentation".
    *   This is not a cover page. It's a note.
    *   The black bars are likely scan artifacts from a small piece of paper (the note) scanned on a large bed, or a fax transmission artifact.
    *   The content is a memo.
>     *   One detail: "Date 10-29-89". Handwritten.
    *   Check 2: "handwritten". "Most of the content is freeform handwriting". No, only the date and checkmark are handwritten. Rest is typed. So not handwritten.
>     *   So, **memo**.
>     *   Wait, could it be **email**?
    *   Pre-scan: "A mail-client header block...". No.
    *   "A FAX machine transmission header... is NOT a mail-client header".
    *   This looks like it could be an email printed out? No, date is 1989. Email wasn't common then. It's a memo/fax.
>     *   Final label: **memo**.
>     *   Wait, let's re-read Check 10 carefully.
    *   "administrative form... for capturing factual data".
    *   "A form does NOT have to be blank — a filled form recording data is still a form".
    *   "This also covers: a standalone labeled data chart...".
    *   "internal authorization/approval forms with an approval signature/date block".
    *   This page has a date block. But no approval signature block (just names/extensions).
    *   The checkboxes are for "what is attached".
    *   I think **memo** is the strongest fit due to the "dated internal note" rule.
>     *   Let's check the runner-up.
    *   If I choose memo, runner-up is form (because of checkboxes/date field) or file_folder (because of Bates number/black bars).
    *   The text content "Attached is..." rules out file_folder.
    *   The memo rules rule out form (function is communication, not data capture).
>     *   Wait, is "LAW DEPARTMENT - PATENT SECTION" a header?
    *   It's at the bottom.
    *   Usually headers are at the top.
    *   But the rule says: "A dated internal note addressed to a named person... IS a memo even without literal 'TO:/FROM:' labels".
    *   Here, the names and extensions are at the bottom, acting as From/To.
    *   "Beverly Monroe - x3817 / Chris Hardin - x2823".
    *   This is "From: Beverly... To: Chris...".
    *   So it's a memo.
>     *   One last check: **specification**? No.
    *   **scientific_report**? No.
>     *   The label is **memo**.

---

## form → specification (1 errors)

### `rvl_cdip__form__0010.png`
**Expected:** `form` | **Predicted:** `specification`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** None.
- **Masthead/Running head:** There is a Bates number "620423067" at the bottom right. No journal masthead. No newspaper masthead.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a lot of data (tables, rows, columns). It's not just an ID or stamp.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: The page is mostly typed labels on the left ("BRAND", "PRODUCTION DATE", "OPERATOR NUMBER", "CIGARETTE", "P.D. (INCHES)", etc.) and handwritten numbers in the columns. Wait, let's look closer.
    *   The left column is typed: "BRAND", "PRODUCTION DATE", "OPERATOR NUMBER", "DATE ANALYSIS EXPECTED", "DATE RECEIVED", "CIGARETTE", "P.D. (INCHES)", "Cigarette", "Sealed Cigarette", "Tob. Sect.", "Filter", "WEIGHT (MG)", "Circ. (MM)", "Cigarette", "N.T.W.", "Tobacco", "Density (MG/CC)", "FILTER", "Texhil/Pillow (%)", "Triceratin (%)", "TEODA (%)", "Ventilation Rate (%)", "PAPER", "Porosity (CORSETA)", "Citrate (%)", "Phosphate (%)", "RPM (% INC)", "Lamina", "Recon. Tob.", "Stem", "Puffed", "TOR. ANALYSES (%)", "Alkaloids", "Total Sugar", "Reducing Sugar", "Moist. (Cond)", "Tarate (PRG)", "Menthol", "Prop. Glycol", "Glycerin", "Mixrate", "SMOKING (CIG)", "Tar (MG)", "Nicotine (MG)", "Efficiency (%)", "Puffs", "NO (MG)", "CO (MG)", "Cil. Perf. Firmness (Gts/25 cks)", "E-d Stability (MG/Cl)", "Coal Retention (%)", "Corr. BORE FV (CC/GM)", "ROTC FV Moisture (%)", "Corr. FILL VALUE (MG/CC)", "FV MOISTURE (%)".
    *   The top row has handwritten text: "ST JAMES C4 1001 BA", "11/2", "P57L D6 P57L D15", "45%", "35%".
    *   The data columns have handwritten numbers: "36.036", "6.0 0.70", "4.9 0.22", "31", "34.0 05.45", "1300.8", "374.0", "8448", "AVP.5", "42.0 5.12", "9.1 0.40 9", "0.74 0.03 9", "427 1.66 9", "26 0.25 16", "103 0.64 16", "172 - 2", "24.6", "6.5 0.38 8", "0.53 0.02 8", "454 0.62 8", "10.50 14 16", "70.062 16", "172 - 2", "10.2 1".
    *   Most of the content is a structured table with typed labels and handwritten data entries.
    *   Rule: "Handwriting filling in labeled printed fields is form, not handwritten". This is a filled form.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No fax header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
    *   Evidence: Not a survey. It's technical data.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE**
    *   Evidence: No journal header.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT**
    *   Evidence: No money, invoices, budgets. It's cigarette analysis data (Tar, Nicotine, Weight, etc.).
    *   Result: not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: The page is titled/structured around "BRAND ST JAMES C4 1001 BA". It lists cigarette parameters: P.D. (Inches), Weight (mg), Circ. (mm), N.T.W., Density, Filter properties (Texhil/Pillow, Triceratin, TEODA, Ventilation Rate), Paper properties (Porosity, Citrate, Phosphate), Tor. Analyses (Alkaloids, Sugar, Moisture, Tarate, Menthol, Prop. Glycol, Glycerin, Mixrate), Smoking (Cig) analyses (Tar, Nicotine, Efficiency, Puffs, NO, CO), Perf. Firmness, Stability, Coal Retention, Bore FV, Moisture.
    *   This looks like a product analysis table or a specification sheet for a cigarette brand ("ST JAMES C4 1001 BA").
    *   Rule: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough".
    *   The top line says "BRAND ST JAMES C4 1001 BA". This names the product.
    *   The table contains product parameters and measurements (likely from a test).
    *   Wait, is it a scientific report? Or a form? Or a specification?
    *   Let's check Check 10 (Form) vs Check 8 (Specification) vs Check 13 (Scientific Report).
    *   Check 8: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification".
    *   This page is a table of test data for a specific product ("ST JAMES C4 1001 BA"). It lists physical and chemical properties. This fits "test-analysis tables keyed to product/part codes" or "product-referenced test data".
    *   Let's look at Check 10 (Form): "A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) is a form". Wait.
    *   Let's re-read Check 10: "A filled analytical or lab data sheet... is a form".
    *   Let's re-read Check 8: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification."
    *   There is a conflict here. Let's look closely at the text.
    *   The page has a grid. Left column: labels. Top rows: Brand, Production Date, Operator Number, Date Analysis Expected, Date Received. Then columns for data (looks like multiple samples or runs: "P57L D6", "P57L D15", maybe averages?).
    *   The data is handwritten.
    *   Is this a "filled analytical or lab data sheet" (form) or "product-referenced test data" (specification)?
    *   Check 8 says: "A labeled product/parameter rate-data chart... is a specification". "A titled product-analysis table... is a specification".
    *   Check 10 says: "A filled analytical or lab data sheet... is a form".
    *   Let's look at the structure. It's a grid with typed labels on the left and handwritten values. It looks like a data capture sheet.
    *   However, Check 8 is specific: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification."
    *   The table is keyed to "BRAND ST JAMES C4 1001 BA". It analyzes cigarette properties. This is product documentation/specification data.
    *   Wait, let's look at Check 13 (Scientific Report). "Requires running prose". This page has no running prose. Just a table. So not scientific_report.
    *   Let's look at Check 10 again. "A form does NOT have to be blank — a filled form recording data is still a form... This also covers: ... a filled analytical or lab data sheet...".
    *   But Check 8 says: "Product-referenced test data is a specification." and "A titled product-analysis table... is a specification".
    *   Which takes precedence? The checks are ordered 1-14.
    *   Check 8 comes before Check 10.
    *   Check 8: "PRODUCT OR MATERIAL DOCUMENTATION -> specification". Evidence: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification."
    *   The page is a table of test data for "ST JAMES C4 1001 BA". It lists cigarette specs (P.D., Weight, Circ, Tar, Nicotine, etc.). This is product analysis data.
    *   Therefore, Check 8 matches.
>     *   Wait, let's look at the "form" definition in Check 10. "A filled analytical or lab data sheet... is a form".
    *   But Check 8 is higher priority (Check 8 vs Check 10).
    *   Check 8 text: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification."
    *   The page is definitely a test-analysis table for a product ("ST JAMES").
    *   So it should be `specification`.
>     *   Let's reconsider. Is it a `scientific_report`? No running prose.
    *   Is it a `form`? It's a data sheet. But Check 8 explicitly covers "test-analysis tables keyed to product/part codes".
    *   Let's check the labels. "specification" is Check 8. "form" is Check 10.
    *   Since 8 < 10, if Check 8 matches, we stop.
    *   Does Check 8 match? "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification." Yes. The table is keyed to "BRAND ST JAMES C4 1001 BA". It contains product analysis data (Tar, Nicotine, Weight, etc.).
>     *   Wait, is there any other check?
    *   Check 9: Presentation. No.
    *   Check 11: Correspondence. No.
    *   Check 12: News. No.
    *   Check 14: Advertisement. No.
>     *   Let's look really closely at the content.
    *   Top row: "BRAND ST JAMES C4 1001 BA". "PRODUCTION DATE 11/2". "OPERATOR NUMBER". "DATE ANALYSIS EXPECTED P57L D6 P57L D15". "DATE RECEIVED 45% 35%".
    *   This looks like a batch record or a test result sheet for a cigarette product.
    *   In tobacco archives, these are often "product specifications" or "quality control data".
    *   Check 8: "A labeled product/parameter rate-data chart... is a specification". "A titled product-analysis table... is a specification".
    *   This is a product-analysis table.
>     *   Let's check the "form" caveat in Check 10. "A filled analytical or lab data sheet... is a form".
    *   But Check 8 is earlier. "Product-referenced test data is a specification."
    *   The instruction says: "Walk checks 1-14 below IN ORDER. For each check... If evidence is present: STOP HERE."
    *   So if Check 8 has evidence, I stop at Check 8.
    *   Evidence for Check 8: The page is a table analyzing "BRAND ST JAMES C4 1001 BA". It lists cigarette parameters (P.D., Weight, Circ, Tar, Nicotine, etc.) which are product specifications/analyses. The text "test-analysis tables keyed to product/part codes" and "Product-referenced test data is a specification" applies.
>     *   Wait, is it a `scientific_report`?
    *   Check 13: "Requires running prose". This page has no running prose. Just a table. So not scientific_report.
>     *   Is it a `form`?
    *   Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A filled analytical or lab data sheet... is a form".
    *   This is a filled analytical data sheet.
    *   BUT Check 8 is before Check 10.
    *   Check 8: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification."
    *   The page is a test-analysis table for a specific product ("ST JAMES").
    *   So Check 8 wins.
>     *   Let's refine the evidence for Check 8.
    *   "BRAND ST JAMES C4 1001 BA" identifies the product.
    *   The table contains "SMOKING (CIG)" data (Tar, Nicotine, CO, NO), "CIGARETTE" physical data (Weight, Circ, P.D.), "FILTER" data, "PAPER" data.
    *   This is product material documentation / test analysis for a specific product.
    *   Label: `specification`.
>     *   Wait, let's look at the "form" definition again.
    *   "A form does NOT have to be blank... This also covers: ... a filled analytical or lab data sheet".
    *   "It does NOT cover money records... It does NOT cover product-change authorization pages...".
    *   Check 8 covers "test-analysis tables keyed to product/part codes".
    *   The page is a table of test analysis for "ST JAMES".
    *   So Check 8 is the correct match.
>     *   Let's check if there's any other interpretation.
    *   Could it be `scientific_report`? No, no prose.
    *   Could it be `form`? Yes, it looks like a form. But Check 8 is higher priority and fits "product-referenced test data".
    *   The prompt says: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself".
    *   Here we have "BRAND ST JAMES C4 1001 BA" at the top. This is the product title.
    *   The table has chemical constituents (Tar, Nicotine, Alkaloids) and measurements.
    *   So it is a specification.
>     *   Final check:
    *   Check 1: file_folder - No, has content.
    *   Check 2: handwritten - No, handwriting fills a form.
    *   Check 3: Fax - No.
    *   Check 4: Questionnaire - No.
    *   Check 5: Resume - No.
    *   Check 6: Publication - No.
    *   Check 7: Financial - No.
    *   Check 8: Specification - Yes. Product analysis table for "ST JAMES C4 1001 BA".
    *   Check 9: Presentation - No.
    *   Check 10: Form - (Skipped because 8 matched). Although it looks like a filled form, Check 8's specific rule for product test-analysis tables overrides it. Wait, the instructions say "Once an earlier check matches, later checks do not override it." So if Check 8 matches, I stop.
    *   Check 11: Correspondence - No.
    *   Check 12: News - No.
    *   Check 13: Scientific Report - No (no prose).
    *   Check 14: Advertisement - No.
>     *   Runner-up: `form`. Ruled out because Check 8 (specification) matches first due to the product-referenced test-analysis table nature ("BRAND ST JAMES...", cigarette analysis data). Actually, looking closely at the rules: "A filled analytical or lab data sheet... is a form (check 10)". But Check 8 says "test-analysis tables keyed to product/part codes... is a specification". Since 8 < 10, specification wins.
>     *   Wait, is "ST JAMES C4 1001 BA" a product code? Yes, "C4 1001 BA" looks like a product code/blend code.
    *   The table is keyed to this product.
    *   So it is a specification.
>     *   One detail: "Date Analysis Expected P57L D6 P57L D15". "Date Received 45% 35%". These look like sample IDs or dates.
    *   The columns have headers "X SD N". This is statistical data (Mean, Standard Deviation, N).
    *   This is definitely product test data.
>     *   Final decision: `specification`.

---

## letter → handwritten (1 errors)

### `rvl_cdip__letter__0002.png`
**Expected:** `letter` | **Predicted:** `handwritten`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** No "From:", "To:", "Sent:", "Subject:" headers. There is a handwritten date "Dec. 4, 1972" and a signature. No fax transmission header like "SENT BY: ... # N/N". Wait, there's a handwritten note at the top "PMM" and "Dec. 4, 1972". This looks like a handwritten letter.
- **Masthead/Running head:** No newspaper masthead. No journal running head. Just a Bates number at the bottom "990684127 PRODUCED FROM B&W WEB SITE".
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder.**
    *   Evidence: The page has a handwritten letter. It has body content ("Dear Sir: I received a free sample..."). It is not just an ID/stamp.
    *   Result: not this check.
> *   **Check 2: handwritten.**
    *   Evidence: The entire page content is freeform handwriting. "PMM / Dec. 4, 1972 / Dear Sir: / I received a free sample of your Seaberg 10 and may I say they are the best tasting low tar cigarettes I have ever smoked. / Very Truly / Mrs. Pauline R. Conner".
    *   Is it on a printed template? No, it looks like freeform handwriting on blank paper (maybe a bit of a faint box at the top, but mostly blank). Wait, let's look closer. There is a faint rectangular box at the top, but the text is handwritten.
    *   The rule says: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
    *   "This includes meeting-minutes sheets and log tables printed with ruled columns and headers... handwriting fills a printed table, so it is a filled form".
    *   "The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
    *   Here, it's a letter written by hand. "Dear Sir: ... Very Truly, Mrs. Pauline R. Conner". It's a handwritten letter.
    *   Wait, is it a "handwritten" category or a "letter" category?
    *   Check 2 says: "Most of the content is freeform handwriting... This wins over a typed letter or memo layout."
    *   Check 11 says: "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature".
    *   The conflict is between Check 2 (handwritten) and Check 11 (letter).
    *   Check 2 rule: "This wins over a typed letter or memo layout." It doesn't explicitly say it wins over a handwritten letter category, but "handwritten" is a category.
    *   Let's re-read Check 2: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout."
    *   Wait, the categories are: `advertisement`, `budget`, `email`, `file_folder`, `form`, `handwritten`, `invoice`, `letter`, `memo`, `news_article`, `presentation`, `questionnaire`, `resume`, `scientific_publication`, `scientific_report`, `specification`.
    *   If a page is a handwritten letter, which one is it? `handwritten` or `letter`?
    *   Check 2: "Most of the content is freeform handwriting... This wins over a typed letter or memo layout." This implies if it's handwritten, it's `handwritten`.
    *   Check 11: "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature". This description usually implies a typed letter on letterhead.
    *   Let's look at the "handwritten" definition again. "Most of the content is freeform handwriting... NOT on a printed template."
    *   The page has "Dear Sir:", "Very Truly", signature. It is a letter. But it is handwritten.
    *   Check 2 says "handwritten" covers "notes, letters, memos, drafts". So a handwritten letter is `handwritten`.
    *   Let's check the precedence. Check 2 comes before Check 11.
    *   Check 2: "Most of the content is freeform handwriting... This wins over a typed letter or memo layout."
    *   The page is almost entirely handwritten.
    *   Let's look at the content: "I received a free sample of your Seaberg 10 and may I say they are the best tasting low tar cigarettes I have ever smoked." This is consumer feedback.
    *   Is it a questionnaire? No, it's not a printed survey instrument. It's a freeform handwritten opinion/feedback card.
    *   Check 2 rule: "Conversely, a respondent's freeform handwritten opinion/feedback card (a person's own words in response to a printed prompt such as 'Tell us what you think' — e.g. 'I think NOW in the KNOW is... Please take me off of Mailing list...') IS handwritten, NOT questionnaire".
    *   This fits perfectly. It's a handwritten feedback letter/card.
    *   So `handwritten` is the correct label.
> Let's double check Check 11 (letter).
"letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person..."
The page has a date ("Dec. 4, 1972"), salutation ("Dear Sir:"), prose body, closing ("Very Truly"), signature ("Mrs. Pauline R. Conner").
However, Check 2 is higher priority (Check 2 vs Check 11).
Check 2: "Most of the content is freeform handwriting... This wins over a typed letter or memo layout."
Actually, the text says "This wins over a typed letter or memo layout." It doesn't explicitly say it wins over the `letter` category if the `letter` category is defined by structure. But `handwritten` is a specific category for freeform handwriting.
Usually, if a document is mostly handwritten, it's `handwritten`.
Let's look at the "handwritten" definition again. "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
The page is a handwritten letter. The content is a letter. But the medium is handwriting.
The instructions say: "Judge each page by its FUNCTION... Do not rush to the label that matches the page's subject matter".
Wait, Check 2 says "handwritten" covers "notes, letters, memos, drafts". So a handwritten letter is classified as `handwritten`.
Check 11 `letter` seems to imply a typed letter (letterhead, etc.). "letterhead with an external recipient address...". This page has no letterhead. It's just blank paper with handwriting.
So `handwritten` is the best fit.
> Let's re-evaluate Check 4 (questionnaire).
"Conversely, a respondent's freeform handwritten opinion/feedback card... IS handwritten, NOT questionnaire".
This page is a respondent's feedback ("I received a free sample... best tasting..."). It is handwritten. So it is `handwritten`.
> Let's check the order.
Check 1: file_folder. No.
Check 2: handwritten. Yes. "Most of the content is freeform handwriting...". Evidence: The entire body is handwritten text "Dear Sir: I received a free sample...". No printed template fields are filled (it's freeform on blank paper).
Stop here.
> Runner-up: `letter`. Ruled out because the page is mostly freeform handwriting on blank paper (no letterhead), and Check 2 (handwritten) takes precedence for freeform handwriting notes/letters. Also, Check 11 `letter` requires letterhead or specific external address structure, whereas this is a freeform handwritten note/letter. Actually, the definition of `letter` in Check 11 says "letterhead with...". This page has no letterhead. It has a Bates number. So it's not a formal typed letter. It's a handwritten note/letter. Check 2 covers "notes, letters...".
> Final decision: `handwritten`.
> Wait, let's look at the top right. "PMM" (Philip Morris?) and "Dec. 4, 1972".
The text: "Dear Sir: I received a free sample of your Seaberg 10 and may I say they are the best tasting low tar cigarettes I have ever smoked. Very Truly Mrs. Pauline R. Conner".
This is a consumer feedback letter.
Since it is handwritten and not on a printed form (no boxes, no ruled lines for data capture), it is `handwritten`.
> One detail: "A typed page with only a signature, stamp, or margin note is not handwritten." -> This is a handwritten page.
"Handwriting filling in labeled printed fields is form, not handwritten" -> There are no labeled printed fields. It's freeform.
> So, Check 2 matches.
> Evidence for Check 2: The page consists almost entirely of freeform handwriting: "PMM / Dec. 4, 1972 / Dear Sir: / I received a free sample of your Seaberg 10... / Very Truly / Mrs. Pauline R. Conner". There are no printed field labels or boxes.
Runner-up: `letter`. Ruled out because Check 2 (handwritten) applies to freeform handwriting notes/letters not on a printed template, and `letter` (Check 11) typically implies letterhead/typed structure (though the definition includes "dated note addressed to a named EXTERNAL person", the "handwritten" check is higher priority and explicitly covers "letters" in freeform handwriting). Actually, looking at Check 11, "letter: ... OR a dated note addressed to a named EXTERNAL person...". Here the addressee is "Dear Sir" (external). But Check 2 is earlier. "Most of the content is freeform handwriting... This wins over a typed letter or memo layout." The label `handwritten` exists specifically for this.
> Let's refine the "Runner-up" line.
Runner-up: letter, ruled out because the page is freeform handwriting on blank paper (no letterhead), and check 2 (handwritten) explicitly covers handwritten notes/letters and precedes check 11. Also, it's a consumer feedback card which is explicitly called out as `handwritten` in the calibration notes.
> Calibration note: "A freeform handwritten consumer opinion/feedback card is handwritten, not questionnaire — questionnaire needs a PRINTED instrument..."
This confirms `handwritten`.
> Final check of the text:
"990684127 PRODUCED FROM B&W WEB SITE" at the bottom. Bates number.
The content is handwritten.
> Label: handwritten.

---

## letter → memo (1 errors)

### `rvl_cdip__letter__0010.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** No "From:", "To:", "Sent:", "Subject:" in the email sense. There is "To:", "From:", "Subject:", "Date:", but it looks like a memo header. Wait, let's look closer. "Inter-office Memorandum". "To: Mr. R. H. Cundiff". "From: Research & Development CIM Evaluation Team". "Subject: CIM Evaluation". "Date: November 2, 1977". This is a memo header.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is an RJR logo and "Inter-office Memorandum".
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder.**
    *   Evidence: The page has a lot of body content (text, headings like "Implementation", "Need and/or Uniqueness", "Economics", "ACTION"). It is not just an ID or stamp.
    *   Result: not this check.
> *   **Check 2: handwritten.**
    *   Evidence: There is a handwritten note "No. 20 By [signature/initials]". But the majority of the content is typed text.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET.**
    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. The "No. 20 By..." looks like a routing number, but not a fax cover sheet.
    *   Result: not this check.
> *   **Check 4: questionnaire.**
    *   Evidence: No survey questions.
    *   Result: not this check.
> *   **Check 5: resume.**
    *   Evidence: No career history.
    *   Result: not this check.
> *   **Check 6: scientific_publication.**
    *   Evidence: No journal name, volume, issue, page range on the page itself (except the Bates number 50437 2363 and form number RJRI FORM 2422).
    *   Result: not this check.
> *   **Check 7: financial document (invoice/budget).**
    *   Evidence: Mentions "tobacco savings", "added costs", "lowered machine efficiencies". But it's not a line-item table, ledger, or bill. It's a memo discussing economics.
    *   Result: not this check.
> *   **Check 8: specification.**
    *   Evidence: Discusses "CIM Evaluation", "Product Improvement on Low Tar Cigarettes". Mentions "flavor cone". But it's an evaluation memo, not a material safety data sheet or product formulation spec.
    *   Result: not this check.
> *   **Check 9: presentation.**
    *   Evidence: Not a slide deck. Not a press release. Not a speech.
    *   Result: not this check.
> *   **Check 10: administrative form.**
    *   Evidence: Bottom says "RJRI FORM 2422 - Rev. 7/70". However, the content is a filled-out memo. Wait, let's look at the structure. It has "To:", "From:", "Subject:", "Date:". It has body text. Forms capture data. This is a memo using a form template (RJRI FORM 2422). The instructions say: "A page whose primary structure is a memo header + prose... stays memo". The form number at the bottom is just the template. The content is a memo. Let's check check 11.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter.**
    *   **Email:** No mail-client header (From/To/Sent/Subject in email format). The "To/From/Subject/Date" are memo headers.
    *   **Memo:** "Inter-office Memorandum" at the top. "To: Mr. R. H. Cundiff". "From: Research & Development CIM Evaluation Team". "Subject: CIM Evaluation". "Date: November 2, 1977". Followed by prose ("The CIM submitted by Hal E. Guess has been evaluated..."). This fits the memo definition perfectly. Internal header block followed by memo-style prose.
    *   **Letter:** No external address, no "Dear...", no closing signature (just an "ACTION:" block).
    *   Result: **memo**.
> *   **Check 12: news_article.**
    *   Evidence: No masthead.
    *   Result: not this check.
> *   **Check 13: scientific_report.**
    *   Evidence: It discusses technical stuff (CIM, low tar cigarettes, making equipment), but the format is a memo. "Requires running narrative prose...". It has prose, but the primary structure is a memo (TO/FROM/SUBJECT/DATE). Check 11 (memo) comes before Check 13? Wait, the checks are numbered 1-14. I must follow the order.
    *   Check 11 is "CORRESPONDENCE -> email, memo, or letter".
    *   Check 13 is "ORIGINAL RESEARCH WRITE-UP -> scientific_report".
    *   The memo header is strong evidence for Check 11. The content is technical, but the function is a memo. "A page whose primary structure is a memo header + prose... stays memo".
> *   **Check 14: advertisement.**
    *   Evidence: No.
    *   Result: not this check.
> **Re-evaluating Check 10 vs Check 11:**
The page has "RJRI FORM 2422 - Rev. 7/70" at the bottom.
The top says "Inter-office Memorandum".
It has "To:", "From:", "Subject:", "Date:".
The content is a summary of comments on a CIM (Cigarette Improvement Method? or similar) evaluation.
Check 11 says: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose...".
This page has exactly that. "Inter-office Memorandum" is the title. "To: Mr. R. H. Cundiff", "From: Research & Development...", "Subject: CIM Evaluation", "Date: November 2, 1977".
The body text follows.
So it is a memo.
> **Runner-up:** form. The page has a form number "RJRI FORM 2422" at the bottom. However, the content is a memo. The instructions say "A page whose primary structure is a memo header + prose... stays memo". The form is just the template. Also, check 10 says "Filled or blank fields... for capturing factual data". This page has narrative prose summarizing comments, not filling fields (except maybe the "No. 20 By..." handwritten part, but that's minor). The primary function is communication (memo).
> **Final decision:** memo.
> Let's double check the "memo" definition in Check 11.
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."
Here we have:
To: Mr. R. H. Cundiff
From: Research & Development CIM Evaluation Team
Subject: CIM Evaluation
Date: November 2, 1977
Header: Inter-office Memorandum.
Prose: "The CIM submitted by Hal E. Guess has been evaluated..."
This is a classic memo.
> One detail: "No. 20 By [handwritten]". This is a routing number, common in memos.
> The label is `memo`.

---

## news_article → advertisement (1 errors)

### `rvl_cdip__news_article__0004.png`
**Expected:** `news_article` | **Predicted:** `advertisement`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is a fax-like header at the top right "35", but it looks like a page number. Wait, let's look closer. "THE NEW YORK TIMES MONDAY SEPTEMBER 11, 1989". This is a newspaper masthead.
- **Masthead/Running head:** "THE NEW YORK TIMES MONDAY SEPTEMBER 11, 1989" at the top. This is a newspaper masthead. This points towards check 12 (news_article) or check 14 (advertisement). Wait, let's look at the content.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder.** No. There is a lot of text content.
*   **Check 2: handwritten.** No. It's typed text.
*   **Check 3: FAX TRANSMISSION SHEET.** No.
*   **Check 4: questionnaire.** No.
*   **Check 5: resume.** No.
*   **Check 6: scientific_publication.** No. The masthead is "The New York Times", a general news outlet, not a scientific journal.
*   **Check 7: financial document.** No.
*   **Check 8: specification.** No.
*   **Check 9: presentation.** No.
*   **Check 10: form.** No.
*   **Check 11: correspondence.** No.
*   **Check 12: news_article.** Let's look closely.
    *   Top: "THE NEW YORK TIMES MONDAY SEPTEMBER 11, 1989". This is a newspaper masthead.
    *   Headline: "All Advertising Should Be Truthful".
    *   Sub-headline/image: "Reprinted with permission from November 10, 1969, Advertising Age". "The Truth Seems a Little Twisted".
    *   Text body: "This is not an attempted defense of cigarette or cigarret advertising. This is a simple formulation of the belief that the rules of fairness, accuracy, and truth in advertising should apply to all advertisers..."
    *   Bottom: "What Is Advertising Age? The national newspaper of the advertising and marketing industry... Not a defender of smoking".
    *   Footer: "the tobacco institute 1776 K Street, N.W., Washington, D.C. 20006".
    *   Wait, is this an advertisement or a news article?
    *   Check 12 says: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement (product imagery, slogans, a Surgeon General warning, brand styling) is an advertisement (check 14) even if printed inside a newspaper/magazine with a running masthead and some surrounding text; news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
    *   Check 14 says: "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures."
    *   Let's analyze the content. It's a full-page ad by "the tobacco institute".
    *   The text is an op-ed/letter to the editor style, reprinted from Advertising Age.
    *   The bottom section says "What Is Advertising Age? ... Not a defender of smoking". This is promotional copy for Advertising Age, placed by the Tobacco Institute.
    *   The Tobacco Institute is the advertiser. They are buying space in the New York Times (or it's a clipping from the NYT).
    *   Actually, looking closely at the top: "THE NEW YORK TIMES MONDAY SEPTEMBER 11, 1989". This looks like a clipping from the New York Times.
    *   The content is an advertisement *by* the Tobacco Institute *in* the New York Times (or reprinted).
    *   Wait, the text says "Reprinted with permission from November 10, 1969, Advertising Age".
    *   The main text is an essay about advertising truthfulness.
    *   The bottom part is an ad for "Advertising Age" published by "the tobacco institute".
    *   Let's re-read Check 12 vs Check 14.
    *   Check 12: "Newspaper or magazine masthead... Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement (check 14)... news_article requires the page to present primarily as editorial/multi-story news content".
    *   Check 14: "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures."
    *   This page is a full-page advertisement placed by the Tobacco Institute. It looks like a "public service announcement" or an ad campaign. The bottom clearly says "the tobacco institute" with an address. The text "What Is Advertising Age?" is promotional text for the magazine Advertising Age.
    *   The top part "The Truth Seems a Little Twisted" is the headline of the ad content.
    *   This is an advertisement. The Tobacco Institute is advertising their viewpoint or advertising the magazine Advertising Age. Actually, it looks like an ad *by* the Tobacco Institute *in* the New York Times, or a clipping of an ad.
    *   Wait, the top says "Reprinted with permission from November 10, 1969, Advertising Age". This suggests the text is an excerpt.
    *   The bottom block "What Is Advertising Age? ... Not a defender of smoking" is clearly an advertisement for Advertising Age, paid for by the Tobacco Institute.
    *   The whole page is a promotional layout. It's an advertisement.
    *   Let's check the labels. `advertisement`.
> Let's look at the structure.
- Top: NYT masthead.
- Main headline: "All Advertising Should Be Truthful".
- Image of a newspaper clipping: "The Truth Seems a Little Twisted". Text inside the clipping discusses cigarette advertising rules.
- Bottom text: "What Is Advertising Age? ... the tobacco institute".
- This is a full-page ad. The Tobacco Institute is placing an ad. The ad content is a reprinted article/essay, and the bottom is a blurb about Advertising Age.
- Actually, looking at the layout, it looks like a page from a publication *reprinting* an ad or an article.
- But the bottom clearly identifies "the tobacco institute" as the entity.
- Check 14: "Marketing layout: product imagery, slogans, brand styling... Judge by DOMINANT content... single brand advertisement... is advertisement".
- The dominant content is the Tobacco Institute's message/ad.
- Is it a news article? It's inside a newspaper (NYT), but the content is clearly an advertisement by the Tobacco Institute. The NYT masthead is there, but the content is an ad.
- Check 12 caveat: "a page whose dominant layout is a single brand advertisement ... is an advertisement (check 14) even if printed inside a newspaper/magazine with a running masthead".
- So this is `advertisement`.
> Let's double check.
- The text "All Advertising Should Be Truthful" is the headline.
- The text body is an essay.
- The bottom is "the tobacco institute".
- This is an advertisement placed by the Tobacco Institute. It's likely a "public advertisement" or "issue advertisement".
- Therefore, `advertisement`.
> Let's re-evaluate Check 12. "news_article requires the page to present primarily as editorial/multi-story news content". This page presents as a single ad layout (headline, body, logo/address at bottom). It is not multi-story news. It is a single promotional layout.
> So, `advertisement`.
> Wait, is it a `news_article`?
The top has "THE NEW YORK TIMES".
The content is an article "The Truth Seems a Little Twisted".
But the bottom is "the tobacco institute".
Usually, if it's a clipping from a newspaper, and the main content is an article, it might be news_article.
BUT, the bottom block "What Is Advertising Age? ... Not a defender of smoking" with the Tobacco Institute address is clearly an advertisement *for* Advertising Age, placed by the Tobacco Institute.
The top part "Reprinted with permission..." suggests this is a reprint of an ad or an article.
Actually, this looks like a full-page advertisement in the New York Times (or a similar paper) by the Tobacco Institute. The Tobacco Institute often ran full-page ads.
The text "All Advertising Should Be Truthful" is the ad headline.
The text inside the "newspaper" graphic is the ad copy.
The bottom is the ad signature ("the tobacco institute").
So the page *is* an advertisement. The NYT masthead at the top indicates where it was published (or it's a clipping from the NYT).
According to the rules: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement ... is an advertisement (check 14) even if printed inside a newspaper/magazine with a running masthead".
The dominant content is the Tobacco Institute's ad.
> So, `advertisement`.
> Let's check the scratchpad steps.
1. file_folder: no.
2. handwritten: no.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial: no.
8. specification: no.
9. presentation: no.
10. form: no.
11. correspondence: no.
12. news_article: Masthead present ("The New York Times"), but dominant content is an advertisement layout (headline, ad copy, brand signature "the tobacco institute"). Rule says single brand ad inside newspaper is advertisement.
13. scientific_report: no.
14. advertisement: Yes. Marketing layout, brand styling ("the tobacco institute"), slogan-like headline ("All Advertising Should Be Truthful"), promotional text ("What Is Advertising Age?").
> Runner-up: news_article. Ruled out because the page's dominant layout is a single advertisement by the Tobacco Institute (with their address and promotional text for Advertising Age), not editorial news content, despite the NYT masthead at the top.
> Final decision: advertisement.

---

## presentation → scientific_report (1 errors)

### `rvl_cdip__presentation__0003.png`
**Expected:** `presentation` | **Predicted:** `scientific_report`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** No "From/To/Sent/Subject" visible. There is a "RECEIVED APR 10 1989" stamp and "A. M. Hypothesis REJECTED". No email headers.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head/volume/issue/page number on this specific page (there is a Bates number 620921948 at the bottom, but no journal info).
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a lot of content. "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS". It has tables, text, hypotheses. It's not just an ID or stamp.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: Mostly typed text. There is a handwritten note "Less Menthol and" next to "LESS PLEASANT AFTERTASTE". But the majority is typed.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header. Just a "RECEIVED" stamp.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: The page is titled "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS". It lists "ET PREFERRED", "ET MORE LIKABLE OVERALL", "ET BETTER TOBACCO TASTE". It has a column "HYPOTHESIS ACCEPTED / REJECTED". It lists results like "KOOL FT 100 (K)", "NEWPORT FT 100 (K)". It has numbered points 1-6 describing perceptions ("ET PERCEIVED LESS IRRITATING..."). This looks like a summary of results from a study or survey, not the survey instrument itself. Wait, let's look closer. It's a summary of results. Is it a scientific report? Or a form?
    *   Let's check the content. It's a "CPT SUMMARY RESULTS". CPT usually stands for Consumer Perception Test or similar.
    *   It lists hypotheses and whether they were accepted or rejected.
    *   It's a summary of data.
> *   **Check 5: resume**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 6: scientific_publication**
    *   Evidence: No journal name, volume, issue, DOI. Just a Bates number.
    *   Result: not this check.
> *   **Check 7: financial document**
    *   Evidence: No money, no invoices, no budgets.
    *   Result: not this check.
> *   **Check 8: specification**
    *   Evidence: No "shall/must", no MSDS, no product formulation. It's a summary of results.
    *   Result: not this check.
> *   **Check 9: presentation**
    *   Evidence: The layout is sparse, rotated 90 degrees (landscape text on portrait page, or vice versa? The text is vertical. Let's orient it. "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS" is at the top left if rotated. The text runs vertically. Wait, the image is rotated. Let's read it sideways.
    *   Top: "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS".
    *   Columns: "ET PREFERRED", "ET MORE LIKABLE OVERALL", "ET BETTER TOBACCO TASTE".
    *   Rows: "NEWPORT FT KS (KM)", "KOOL FT 100 (KM)", etc.
    *   Right side: "HYPOTHESIS ACCEPTED / REJECTED".
    *   Bottom text: "1 ET PERCEIVED LESS IRRITATING...", "2 YOUNGER (21-35) ADULT SMOKERS FAVORED CURRENT KM 100.", etc.
    *   This looks like a summary page from a report or a slide.
    *   Is it a presentation? "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)... a near-blank cover or title page... a deck cover, or a section divider".
    *   This page has a title, a table of results, and a list of findings. It looks like a summary page from a scientific report or a presentation slide.
    *   Let's look at Check 13: scientific_report. "Running narrative prose with objectives, methods, results, or discussion...". This page has results ("CPT SUMMARY RESULTS") and a list of findings (1-6). It's not really running narrative prose, it's a structured summary.
    *   However, let's look at the "presentation" check again. "A standalone chart or table of values alone... is NOT a slide; it is a form (check 10). BUT a TITLED, DESIGNED DECK CHART... IS a presentation". This is a table of results.
    *   Let's look at Check 10: form. "Filled or blank fields... standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This is research data (CPT results).
    *   Let's look at Check 13 again. "scientific_report: ... a technical/project status report whose content is primarily technical... even when it embeds a budget-vs-actual cost section". "Also scientific_report: a hand-plotted experimental graph...".
    *   This page is a summary of results from a Consumer Perception Test (CPT). It lists hypotheses and results.
    *   Is it a scientific_report? It has "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS". It lists hypotheses. It lists findings 1-6. This looks like a page from a scientific report or a technical summary.
    *   Wait, is it a form? "QA/parameter review sheet". No.
    *   Let's re-evaluate "presentation". The text is rotated. The layout is sparse. "RECEIVED APR 10 1989". "A. M. Hypothesis REJECTED".
    *   Actually, let's look at the content. It's a summary of a test. "CPT SUMMARY RESULTS".
    *   Is there a better fit?
    *   Let's look at the labels again.
    *   advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
>     Let's look at the structure.
    Title: NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS.
    Table:
    Columns: ET PREFERRED, ET MORE LIKABLE OVERALL, ET BETTER TOBACCO TASTE.
    Rows: NEWPORT FT KS (KM), KOOL FT 100 (KM).
    Values: NM FT KS COMP. REP (R), KOOL FT KS (KM).
    Right column: HYPOTHESIS ACCEPTED / REJECTED.
    Values: KOOL FT 100 (K) / NEWPORT FT 100 (K) -> ACCEPTED? No, the columns are aligned.
    Row 1: NEWPORT FT KS (KM) | NM FT KS COMP. REP (R) | KOOL FT 100 (K) / NEWPORT FT 100 (K) -> Hypothesis: KOOL FT 100 (K) / NEWPORT FT 100 (K) ... wait.
    The text is:
    "HYPOTHESIS * A. M. Hypothesis"
    "ACCEPTED REJECTED"
    Under Accepted: KOOL FT 100 (K), NEWPORT FT 100 (K).
    Under Rejected: KOOL Milds KS (KM)1, NEWPORT FT KS (KM), KOOL FT KS (KM).
    This is a summary of statistical results.
>     Text at bottom:
    "1 ET PERCEIVED LESS IRRITATING AND HAVING LESS MENTHOL."
    "2 YOUNGER (21-35) ADULT SMOKERS FAVORED CURRENT KM 100."
    "3 ET PERCEIVED Milder, HAVING LESS MENTHOL & TOBACCO TASTE."
    "4 ET PERCEIVED TO BE SMOOTHER."
    "5 ET PERCEIVED TO HAVE POORER MENTHOL TASTE, less Menthol and LESS PLEASANT AFTERTASTE" (handwritten correction).
    "6 EQUALITY OR BETTER."
>     This is a summary of findings from a study. It looks like a page from a scientific report or a technical summary.
    Check 13: scientific_report. "Running narrative prose...". This isn't really running prose. It's a summary table and a list of numbered findings.
    However, the definition says: "Also scientific_report: ... a technical-study title page...". This isn't a title page.
    "Original research write-up -> scientific_report. Running narrative prose with objectives, methods, results, or discussion...".
    This page contains "results" (CPT Summary Results) and a discussion of findings (1-6).
    Is it a form? "A filled analytical or lab data sheet... is a form". This is a summary of results, not raw data.
    Is it a presentation? "Slide/overhead layouts...". The text is rotated 90 degrees. The layout is sparse. It looks like a slide or an overhead transparency summary.
    "Scan-artifact signal: a solid black bar along one edge... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
    There is a black bar at the top (left in rotated view). The text is sparse.
    Wait, the image is rotated. The top of the page is the left side.
    Left side (top of page): "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS".
    There is a black bar at the very top (left edge of image).
    The text is sparse.
    "RECEIVED APR 10 1989".
    This looks like a summary page from a report, possibly a slide or a summary sheet.
>     Let's look at Check 9: presentation.
    "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)..."
    "A near-blank cover or title page... a deck cover, or a section divider".
    "A standalone photographic image... is a photographic slide".
    "A one-page status/location display sheet... is a presentation".
    This page is a summary of results. It's not a slide deck per se, but it looks like a summary page.
>     Let's look at Check 13: scientific_report.
    "Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."
    This page has a table and a numbered list. It's not running prose.
    However, the numbered list 1-6 is narrative: "ET PERCEIVED LESS IRRITATING...".
    Is it a scientific_report?
    The document is likely a page from a larger report on "NEM Expanded Tobacco".
    The Bates number 620921948 suggests it's from an archive.
    "CPT" = Consumer Perception Test.
    This is a summary of results.
>     Let's reconsider Check 10: form.
    "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a research-measurement chart is scientific_report (check 13)..."
    This is a research-measurement chart/table (CPT results). So if it's a chart/table, it falls to scientific_report (check 13) or specification (check 8).
    Since it's research results (CPT), it's likely scientific_report.
    But scientific_report requires "Running narrative prose".
    "Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."
    This page has a table and a list. Is the list "running narrative prose"?
    "1 ET PERCEIVED LESS IRRITATING AND HAVING LESS MENTHOL." -> This is a finding.
    It's not really running prose.
>     Let's look at Check 8: specification.
    "Product-referenced test data is a specification. A titled product-analysis table... is a specification".
    This table analyzes products: Newport, Kool, Richland.
    "KOOL FT 100 (K)", "NEWPORT FT 100 (K)".
    It's testing tobacco products.
    "test-analysis tables keyed to product/part codes...".
    But this is a "CPT SUMMARY RESULTS" (Consumer Perception Test), not a chemical analysis or formulation.
    Specification is for "Material Safety Data Sheet", "product formulation", "manufacturing-change authorization", "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language".
    This is consumer perception. Not really a specification.
>     Let's look at Check 4: questionnaire.
    "The page asks the reader to answer...". This page is the *results* of a questionnaire/test, not the instrument itself.
    "Notes ABOUT a survey instrument are questionnaire...". This is not a note about it.
>     Let's look at Check 13 again.
    "scientific_report: ... a technical/project status report whose content is primarily technical...".
    This is a summary of a technical test (CPT).
    Even if it lacks full running prose, it's a research result page.
    Wait, the rule says: "Requires running prose — a page that is only labeled field-value entries (even an 'ANALYTICAL DATA SUMMARY' under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
    This page is a summary of results. It has a table and a list of conclusions.
    Is it a form? "QA/parameter review sheet". No.
    Is it a scientific_report?
    The text "1 ET PERCEIVED..." is narrative.
    The table is data.
    This looks like a page from a scientific report (a summary page).
>     Let's look at the "presentation" check again.
    "Slide/overhead layouts...".
    The text is rotated. The layout is very sparse.
    "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead — presentation".
    There is a black bar at the top (left side of image).
    The text is sparse.
    "RECEIVED APR 10 1989".
    "A. M. Hypothesis REJECTED".
    This looks like a summary slide or overhead.
    "A one-page status/location display sheet... is a presentation".
    This is a summary sheet.
    But is it a presentation?
    "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)".
    This has a table and bullet-like numbered list.
    The text is large and sparse.
    The rotation suggests it might be a slide or a summary page designed to be read quickly.
    However, the content is dense with data (the table).
>     Let's look at the label "scientific_report".
    If this is a page from a report on "NEM Expanded Tobacco", it's a scientific_report.
    The Bates number indicates it's an archive document.
    Most archive documents of this type (tobacco industry) are internal reports.
    "CPT SUMMARY RESULTS" is a summary of a Consumer Perception Test.
    This is typical content for a scientific_report (internal technical report).
    Even if it's a summary page, it belongs to the scientific_report category.
    The rule: "scientific_report requires running prose; it is never a catch-all."
    But "Also scientific_report: ... a technical-study title page...".
    And "A scientific commentary/critique... is a research write-up".
    This page is a results summary.
    Is there running prose?
    "1 ET PERCEIVED LESS IRRITATING AND HAVING LESS MENTHOL."
    "2 YOUNGER (21-35) ADULT SMOKERS FAVORED CURRENT KM 100."
    These are sentences.
    "3 ET PERCEIVED Milder, HAVING LESS MENTHOL & TOBACCO TASTE."
    "5 ET PERCEIVED TO HAVE POORER MENTHOL TASTE, less Menthol and LESS PLEASANT AFTERTASTE".
    This is narrative text describing results.
    So it has running prose (numbered list of findings).
    So it fits scientific_report.
>     Let's check "form" (Check 10).
    "A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:...) is a form".
    This is "CPT SUMMARY RESULTS". It's a summary, not a raw data sheet.
    "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data... a research-measurement chart is scientific_report (check 13)".
    This is a research-measurement chart (CPT results). So it's scientific_report.
>     So, scientific_report seems the best fit.
    Evidence: Title "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS", table of product preferences, numbered list of research findings/hypotheses (1-6). This is a results page from a technical study/report.
>     Wait, is there a chance it's a "presentation"?
    "Slide/overhead layouts...".
    The text is rotated 90 degrees.
    "Scan-artifact signal: a solid black bar along one edge... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
    There is a black bar at the top (left).
    The text is sparse? Not really, there's a big table.
    But the layout is very structured.
    However, the content is clearly research results.
    Usually, summary pages from reports are scientific_reports.
    Unless it's explicitly a slide deck.
    "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS" looks like a section header in a report.
    The "RECEIVED" stamp is an archival stamp.
    I will go with scientific_report.
>     Let's re-read the "presentation" caveat.
    "Technical-study title pages: a title page naming a specific study or methodology with a date... is scientific_report (check 13), not presentation".
    This isn't a title page. It's a results page.
    Results pages are scientific_report.
>     Let's check "specification" (Check 8).
    "Product-referenced test data is a specification."
    "A titled product-analysis table... is a specification".
    This table analyzes products (Newport, Kool).
    But it's "CPT SUMMARY RESULTS" (Consumer Perception Test), not a chemical/physical analysis.
    Specification is for "Material Safety Data Sheet", "product formulation", "manufacturing-change authorization", "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language".
    Consumer perception is not specification. It's research.
>     So, scientific_report.
>     One more check: Is it a form?
    "QA/parameter review sheet". No.
    "Filled or blank fields...". The table has fields, but it's data.
    "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data... a research-measurement chart is scientific_report".
    This is a research-measurement chart (CPT results). So scientific_report.
>     Final decision: scientific_report.
    Evidence: Title "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS", table of consumer preference data, numbered list of hypotheses/findings (1-6). This is a results page from a technical study.
>     Wait, look at the handwritten note: "less Menthol and".
    "Handwriting filling in labeled printed fields is form, not handwritten".
    Here, handwriting is annotating the text "LESS PLEASANT AFTERTASTE". "less Menthol and" is added.
    This is an annotation on a report page. Doesn't change category to handwritten (majority is typed).
>     Runner-up: form. Ruled out because the page contains research-measurement data (CPT results) and narrative findings, which belongs to scientific_report, not generic administrative data capture.
    Runner-up: presentation. Ruled out because it's a results page from a technical study with data and narrative findings, not a slide deck layout (though sparse, it's a summary table). Actually, the layout is sparse. But the content is research results. The rule says "Technical-study title pages... is scientific_report". Results pages are also scientific_report.
>     Let's look at the "presentation" check again.
    "A standalone chart or table of values alone... is NOT a slide; it is a form (check 10). BUT a TITLED, DESIGNED DECK CHART... IS a presentation".
    This is a titled table. "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS".
    Is it a "DESIGNED DECK CHART"?
    It has a table and a list.
    It looks like a summary page.
    If it's a summary page from a report, it's scientific_report.
    If it's a slide, it's presentation.
    The "RECEIVED" stamp and Bates number suggest it's a document from an archive, likely a report page.
    The content "1 ET PERCEIVED..." is narrative.
    I'll stick with scientific_report.
>     Wait, is there a chance it's a "specification"?
    "test-analysis tables keyed to product/part codes".
    The table has product codes (KM, K, KL, R).
    But it's "CPT SUMMARY RESULTS" (Consumer Perception Test).
    Specification is for "product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language".
    Consumer perception is not tolerance or requirement language. It's "ET PERCEIVED...".
    So not specification.
>     Final check: scientific_report.
    The page is a summary of results from a Consumer Perception Test (CPT) for "NEM Expanded Tobacco". It contains a data table comparing products (Newport, Kool, Richland) and a numbered list of findings/hypotheses. This is characteristic of a technical report or scientific report (internal document).
>     One detail: "Requires running prose".
    The numbered list 1-6 is prose. "ET PERCEIVED LESS IRRITATING AND HAVING LESS MENTHOL."
    The table is data.
    This fits "results" section of a scientific report.
>     Label: scientific_report.

---