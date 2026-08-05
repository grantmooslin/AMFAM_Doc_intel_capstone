# Misclassification Reasoning — qwen3.7-flash_v11_8_reasoning_320

**Overall Accuracy:** 87.1% (277/318)  
**Total Errors:** 41  
**Unique Confused Pairs:** 24

---

## letter → memo (5 errors)

### `rvl_cdip__letter__0002.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I need to follow a specific scratchpad procedure, checking conditions 1-14 in order.
> **Document Analysis:**
- Top right: "MAR 27 1987" (date stamp)
- Header: "RJR Interoffice Memorandum"
- Subject: "Use of KYDEX(R) For A Waste Tub Stand"
- Date: "March 26, 1987"
- To: "Mr. Bill Hunt"
- From: "Dr. Rob Harrington"
- Body: Running prose discussing scientific/technical details about Kydex(R) plastic sheets (polyacrylic-polyvinyl chloride polymer), toxicity, LD50, etc.
- Signature: "Rob" (signed)
- Bottom left: "RH/Ige", "cc: Dr. A. W. Hayes, Dr. R. L. Suber, Dr. Randy Deskin"
- Bottom right: Handwritten note "3/30 For the buy out for this spg - also for your requested data from Rob in letters for purchase Will" (roughly).
- Right margin: Bates number "50811 2328"
> **Pre-scan:**
- Mail-client header block? No. "RJR Interoffice Memorandum", "To:", "From:", "Subject:". This is a memo header, not an email header (From/To/Sent/Subject with email addresses or mail client format). Wait, check 11 says email requires mail-client header block (From/To/Sent/Subject, cc, attachments) or forwarded/threaded trail. This has "To:", "From:", "Subject:", but it's a standard memo header. Let's look at check 11.
- Masthead/running head? No newspaper/magazine masthead. No journal running head.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a full memo body, subject line, header. Not identifier-only.
- Result: not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Most of the content is typed memo text. There is a handwritten note at the bottom, but it's not the majority.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax cover sheet header. Just a date stamp.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: Not a survey.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: Not a resume.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal running head, volume, issue, page number on this page.
- Result: not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No line-item table, ledger, or financial primary structure. Mentions "buy out" and "purchase" in the handwritten note, but the document itself is a memo about toxicity of a polymer.
- Result: not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: Discusses Kydex(R) properties, but it's a memo evaluating its use, not a Material Safety Data Sheet or product specification document with "shall/must" or manufacturing changes. It's an internal memo.
- Result: not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck, cover, or press release.
- Result: not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: Not a form with fields/boxes/checkboxes.
- Result: not this check.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: Header "RJR Interoffice Memorandum", "Subject:", "To: Mr. Bill Hunt", "From: Dr. Rob Harrington", date "March 26, 1987". Followed by memo-style prose. No external address, no "Dear..." salutation. Internal names + titles (implied by interoffice) + date + prose. This is a memo.
- Wait, check 11 says: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo".
- This page has "RJR Interoffice Memorandum", "Subject:", "To:", "From:", date. It fits memo perfectly.
- Result: memo.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: No.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: The body contains scientific text about toxicity, but the primary structure is a memo (TO/FROM/SUBJECT header). Check 11 (correspondence) precedes check 13. The document is a memo *about* scientific data, not a research write-up itself. The header defines it as a memo.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: No.
> **Conclusion:**
The document is an internal memorandum.
Label: memo.
> Let's double check check 11 details.
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."
The page has:
"RJR Interoffice Memorandum"
"Subject: Use of KYDEX(R) For A Waste Tub Stand"
"March 26, 1987"
"To: Mr. Bill Hunt"
"From: Dr. Rob Harrington"
This is a classic memo header. The body is prose. The handwritten note at the bottom is just an annotation, doesn't change the document type.
> Runner-up: scientific_report. Ruled out because the page has a clear memo header (TO/FROM/SUBJECT) and is an internal interoffice memorandum, not a standalone research write-up. The scientific content is the subject of the memo, not the document type.
> Final label: memo.

---
### `rvl_cdip__letter__0007.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow a specific set of checks in order, using a scratchpad to document my thought process.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There's a date "June 17, 1971", a name "Mr. J. H. Sherrill, Jr.", "Re: VANTAGE MENTHOL (HBD # 71-0197)". Bottom right has a logo and "50030 0163". No journal masthead.
> **Check 1: file_folder**
- Evidence: The page has a date, recipient name, subject line, and several paragraphs of text. It has real content.
- Not this check.
> **Check 2: handwritten**
- Evidence: The text is typed. There is a small handwritten "Bill" at the top right and a circle around "MENTHOL (HBD # 71-0197)". But the majority is typed.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey instrument or transmittal note.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: No resume/CV.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal name, volume, issue, page range, DOI.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT**
- Evidence: No line-item table, ledger, statement, voucher, check face. Mentions "data from the VANTAGE Menthol CAS", but no financial billing.
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
- Evidence: No Material Safety Data Sheet, product formulation, manufacturing-change authorization, test-analysis tables keyed to product codes with "shall/must". It discusses advertising data, but isn't a specification.
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
- Evidence: Not a slide deck, cover, or press release. It's a typed memo.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM**
- Evidence: No fields, boxes, checkboxes, ruled entry lines for capturing data. It's a narrative text.
- Not this check.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence:
  - Date: "June 17, 1971"
  - Recipient: "Mr. J. H. Sherrill, Jr."
  - Subject: "Re: VANTAGE MENTHOL (HBD # 71-0197)"
  - Body: "This reports data from...", "BACKGROUND: ...", "DISCUSSION: ..."
  - Sender: "Joseph Ottaviani, Marketing Research Department"
  - Initials: "JO;sp"
  - "Attachments"
  - This is an internal memo. TO:/FROM: structure is implied by the layout (date, recipient, Re:, body, sender name/title, initials). Wait, let's look closer.
  - "Mr. J. H. Sherrill, Jr." is the recipient.
  - "Re: VANTAGE MENTHOL..."
  - "Joseph Ottaviani, Marketing Research Department" is the sender.
  - This matches the memo definition: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo". Here, "Mr. J. H. Sherrill, Jr." is addressed, but no title is given, but there is a "Re:" line and the sender has "Marketing Research Department". Actually, it has "Re:" which is like "RE:". It's a standard internal memo format.
  - Let's check letter definition: "letterhead with an external recipient address, date, 'Dear ...' salutation...". No external address, no "Dear".
  - So it's a memo.
> **Check 12: PUBLISHED JOURNALISM**
- Evidence: No masthead, byline, dateline (other than the memo date), multi-column typography.
- Not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP**
- Evidence: It's a memo reporting data, not a full scientific report with methods/results discussion in narrative form (though it has BACKGROUND and DISCUSSION, it's clearly a memo format). Check 11 (memo) precedes check 13. Wait, does check 11 precede check 13? Yes, correspondence is check 11, scientific_report is check 13. The structure is memo header + prose.
> **Check 14: PROMOTIONAL MATERIAL**
- Evidence: Not an ad.
> Let's re-verify Check 11 (memo).
Text:
June 17, 1971
Mr. J. H. Sherrill, Jr.
Re: VANTAGE MENTHOL (HBD # 71-0197)
[paragraphs]
Joseph Ottaviani
Marketing Research Department
JO;sp
Attachments
> This is a classic internal memo. The instructions say: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels". Here we have "Re:" which is a subject line, date, recipient name, and sender name + department. It fits memo perfectly.
> Runner-up: letter. Ruled out because there is no external address, no "Dear ..." salutation, and no closing signature. It's an internal note.
> Final label: memo.

---
### `rvl_cdip__letter__0008.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None. (There is a "TO:", "FROM:", "SUBJECT:" block, but it's a memo header, not email).
- Masthead/running head: None. There's a date "April 16, 1993", a Bates number "93-13104" (rotated), and "51969 5114" (rotated). No journal masthead.
> **Check 1: file_folder**
- Evidence: The page has a full memo body, "KEY FINDINGS", bullet points, etc. Not just an identifier.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: The text is typed. There is a handwritten "DGR" at the top right and a rotated handwritten "93-13104" (Bates number, actually looks like a Bates number or internal tracking number, but the main text is typed). Not majority handwritten.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey instrument or transmittal for a survey. It's a memo about "March CAMEL Cash Tracking Results".
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: Not a resume.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal name, volume, issue, page range, DOI.
- Result: not this check.
> **Check 7: FINANCIAL DOCUMENT**
- Evidence: Mentions "March CAMEL Cash Tracking Results", "participation rate", "awareness", "catalog distribution". No line-item table, ledger, statement, voucher, or check face. It's a memo discussing results.
- Result: not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
- Evidence: Not an MSDS, product formulation, or specification with "shall/must".
- Result: not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
- Evidence: Not a slide deck, cover, or press release. It's a memo.
- Result: not this check.
> **Check 10: ADMINISTRATIVE FORM**
- Evidence: Not a form with fields, boxes, checkboxes.
- Result: not this check.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence:
  - "TO: Mr. E. C. Leary"
  - "FROM: G. R. Davis"
  - "SUBJECT: March CAMEL Cash Tracking Results (BIAD #93-13104)"
  - Date: "April 16, 1993"
  - Body: "Attached are the results through March..." followed by "KEY FINDINGS:" and bullet points.
  - This is a classic internal memo header (TO/FROM/SUBJECT/DATE) followed by memo-style prose. No external address, no "Dear ...", no closing signature.
- Result: memo.
> **Check 12: PUBLISHED JOURNALISM**
- Evidence: No masthead, byline, dateline, multi-column news typography.
- Result: not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP**
- Evidence: Not a scientific report with running narrative prose about objectives, methods, results of a study. It's a business memo about marketing tracking results.
- Result: not this check.
> **Check 14: PROMOTIONAL MATERIAL**
- Evidence: Not an advertisement.
- Result: not this check.
> Final classification: memo.
> Let's double check.
Header:
April 16, 1993
TO: Mr. E. C. Leary
FROM: G. R. Davis
SUBJECT: March CAMEL Cash Tracking Results (BIAD #93-13104)
> Body:
"Attached are the results through March from the CAMEL Cash Tracker Tag-on. While I've mentioned a few key findings from the results, a full first quarter analysis utilizing Diary data as well as these Tracker results will be issued when the March Diary data becomes available (probably middle of next month)."
> "KEY FINDINGS:"
- Bullet points with analysis.
> This is clearly a memo.
> Runner-up: letter. Ruled out because there is no external recipient address, no "Dear ..." salutation, and no closing signature. It has a TO:/FROM:/SUBJECT: block.
> Let's write the scratchpad.

---
### `rvl_cdip__letter__0009.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> **Document Analysis:**
- Top right: "CAN" (handwritten)
- Header: "RJR CONFIDENTIAL"
- Date: "October 21, 1993"
- TO: Mr. G. C. Pennell
- FROM: T. F. Witner
- SUBJECT: MAGNA Advertising Study Results
- Body text: "This provides you with key measures for the MAGNA Advertising Study..."
- Bullet points: "Recall/Impact Among Clutter Ads", "Key Measures"
- Tables: Data tables with percentages and numbers (MAGNA, Bull Durham, Viceroy, DORAL, Pyramid, Bristol, Cambridge).
- Bottom right: Bates number "51399 2876"
> **Pre-scan:**
- Mail-client header block? No. "TO:", "FROM:", "SUBJECT:" are present, but this is a memo header, not an email header (From/To/Sent/Subject). Wait, let's check check 11. Email requires mail-client header block (From/To/Sent/Subject, cc, attachments) or forwarded/threaded trail. This has TO:/FROM:/SUBJECT: but it's a standard memo format. Let's look at check 11 memo definition: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose. Yes, this is a memo.
- Masthead/running head? No newspaper/magazine masthead. No journal running head. "RJR CONFIDENTIAL" is a handling marking.
> **Check 1: file_folder**
- Evidence: Has body content, tables, TO/FROM/SUBJECT header. Not just an identifier.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: Mostly typed text. "CAN" handwritten at top right. Not majority handwritten.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Result: not this check.
> **Check 4: questionnaire**
- Evidence: No survey instrument, no questions for reader to answer.
- Result: not this check.
> **Check 5: resume**
- Evidence: Not a career history.
- Result: not this check.
> **Check 6: scientific_publication**
- Evidence: No journal name, volume, issue, page range on the page itself.
- Result: not this check.
> **Check 7: financial document (invoice/budget)**
- Evidence: Mentions advertising study, recall percentages, likeability scores. Not a bill, invoice, budget, or financial ledger.
- Result: not this check.
> **Check 8: specification**
- Evidence: Not a material safety data sheet, product formulation, or "shall/must" requirements.
- Result: not this check.
> **Check 9: presentation**
- Evidence: Not a slide deck, cover, or statement. It's a memo with data tables.
- Result: not this check.
> **Check 10: administrative form**
- Evidence: Not a form with fields/boxes for capturing data. It's a memo with embedded tables.
- Result: not this check.
> **Check 11: correspondence (email, memo, letter)**
- Evidence: "TO: Mr. G. C. Pennell", "FROM: T. F. Witner", "SUBJECT: MAGNA Advertising Study Results", "October 21, 1993". Followed by memo-style prose ("This provides you with key measures..."). Internal address (Mr. G. C. Pennell, T. F. Witner - internal names/titles implied or just internal memo format). No external address, no "Dear...", no closing signature. This is a memo.
- Result: memo. Stop here.
> **Check 12: news_article**
- Evidence: No masthead, byline, dateline.
- Result: not this check.
> **Check 13: scientific_report**
- Evidence: Not a research write-up with narrative prose about objectives/methods/results of a scientific study. It's a business memo about an advertising study.
- Result: not this check.
> **Check 14: advertisement**
- Evidence: Not a promotional layout.
- Result: not this check.
> **Final decision:** memo.
> Let's double check check 11 email vs memo.
Email requires mail-client header block (From/To/Sent/Subject, cc, attachments). This has TO:/FROM:/SUBJECT: but it's the classic memo header. The text says: "memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo even without literal "TO:/FROM:" labels". This page has literal TO:/FROM:/SUBJECT: labels. It is a memo.
> Scratchpad construction:
- file_folder: no — page has TO/FROM/SUBJECT header, body prose, and data tables.
- handwritten: no — mostly typed text, only a small handwritten "CAN" at top right.
- fax: no — no fax cover sheet header.
- questionnaire: no — no survey questions or instrument.
- resume: no — not a career history.
- scientific_publication: no — no journal running head or identifier.
- financial: no — not a bill, invoice, or budget; discusses advertising study metrics.
- specification: no — not a product spec or MSDS.
- presentation: no — not a slide deck or cover page.
- form: no — not a structured data-capture form.
- correspondence: yes — "TO: Mr. G. C. Pennell", "FROM: T. F. Witner", "SUBJECT: MAGNA Advertising Study Results", dated "October 21, 1993", followed by memo-style prose. Internal memo format.
- news_article: no — no masthead or journalistic layout.
- scientific_report: no — business memo about advertising study, not original research write-up.
- advertisement: no — not a promotional ad.
> Runner-up: scientific_report, ruled out because the page is an internal business memo (TO/FROM/SUBJECT header + prose) discussing an advertising study's results, not a scientific research write-up with objectives/methods/prose. Or maybe form, ruled out because it's a memo with embedded tables, not a form. Let's use scientific_report as runner-up since it has data tables and looks technical, but the memo header is the defining feature. Actually, email is a good runner-up because of TO/FROM/SUBJECT, but it's not a mail-client header. Let's use email as runner-up. "email, ruled out because the TO:/FROM:/SUBJECT: block is a standard memo header, not a mail-client header (no Sent:/cc:/attachments), and the body is memo-style prose."
> Wait, the prompt says: "add one final line naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out."
Runner-up: email, ruled out because the header is a standard memo TO:/FROM:/SUBJECT: block, not a mail-client header (lacks Sent:/cc:/attachments), and the body is memo-style prose.
> Let's refine the scratchpad lines to be short.
> file_folder: no — page has TO/FROM/SUBJECT header, body prose, and data tables.
handwritten: no — mostly typed text, only a small handwritten "CAN" at top right.
fax: no — no fax cover sheet header.
questionnaire: no — no survey questions or instrument.
resume: no — not a career history.
scientific_publication: no — no journal running head or identifier.
financial: no — not a bill, invoice, or budget; discusses advertising study metrics.
specification: no — not a product spec or MSDS.
presentation: no — not a slide deck or cover page.
form: no — not a structured data-capture form.
correspondence: yes — "TO: Mr. G. C. Pennell", "FROM: T. F. Witner", "SUBJECT: MAGNA Advertising Study Results", dated "October 21, 1993", followed by memo-style prose.
news_article: no — no masthead or journalistic layout.
scientific_report: no — business memo about advertising study, not original research write-up.
advertisement: no — not a promotional ad.
> Runner-up: email, ruled out because the TO:/FROM:/SUBJECT: block is a standard memo header, not a mail-client header (lacks Sent:/cc:/attachments).
> Final label: memo.

---
### `rvl_cdip__letter__0010.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: No. There is a date "January 21, 1985", "TO:", "FROM:", "SUBJECT:". This looks like a memo header, not an email header (From/To/Sent/Subject/cc). Wait, "TO:", "FROM:", "SUBJECT:" are memo headers. Let's check check 11.
- Masthead/running head: No newspaper/magazine masthead. No journal running head.
> **Check 1: file_folder**
- Evidence: The page has a date, TO/FROM/SUBJECT, and several paragraphs of text. Not an identifier-only page.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: The text is typed. No majority handwriting.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: The text summarizes ideas for qualitative follow-up, but it's a memo summarizing research ideas, not a survey instrument itself or a transmittal note for one.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: Not a resume.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal name, volume, issue, page range, DOI.
- Result: not this check.
> **Check 7: FINANCIAL DOCUMENT**
- Evidence: No financial tables, invoices, or budgets. Mentions "marketing departments", no dollar amounts.
- Result: not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
- Evidence: No material safety data sheet, product formulation, or "shall/must" language.
- Result: not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
- Evidence: Not a slide deck, cover, or press release. It's a typed memo.
- Result: not this check.
> **Check 10: ADMINISTRATIVE FORM**
- Evidence: No fields, boxes, checkboxes, or ruled entry lines for capturing data. It's a prose document.
- Result: not this check.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence:
  - Date: "January 21, 1985"
  - "TO: Mr. Alan R. Cox"
  - "FROM: Susan C. Nassar"
  - "SUBJECT: Marlboro Offensive--Idea Generation"
  - Followed by memo-style prose ("This summarizes what I would recommend...").
  - Internal names + titles (implied by context, Susan C. Nassar, Mr. Alan R. Cox) + date + prose, no salutation or closing. This perfectly matches the memo definition in check 11: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
- Result: memo.
> **Check 12: PUBLISHED JOURNALISM**
- Evidence: No masthead, byline, dateline, multi-column typography.
- Result: not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP**
- Evidence: It's a memo summarizing ideas, not a full scientific report with methods/results narrative in the standard sense, though it discusses research ideas. But check 11 (memo) takes precedence because of the explicit TO/FROM/SUBJECT header block followed by prose. Wait, check 11 says "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". This is a perfect match.
> **Check 14: PROMOTIONAL MATERIAL**
- Evidence: Not an ad.
> Let's double check check 11.
"memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose (no external address, no "Dear ..." salutation)."
The page has:
January 21, 1985
TO: Mr. Alan R. Cox
FROM: Susan C. Nassar
SUBJECT: Marlboro Offensive--Idea Generation
> This is a classic internal memo.
> Runner-up: scientific_report, ruled out because the page has a clear TO/FROM/SUBJECT header block followed by prose, making it a memo (check 11), which precedes scientific_report. Also, it's a summary of ideas/recommendations, not a full research write-up with methods/results.
> Final label: memo.

---

## scientific_report → form (4 errors)

### `rvl_cdip__scientific_report__0008.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "INBIFO Institut für biologische Forschung · Köln", "17.Okt.89 NDA/MWO QA3145.WM". This looks like an internal institute header, not a journal masthead. "BLATT-NR.: 1 von 2". No journal volume/issue/page number.
> **Check 1: file_folder**
- Evidence: The page has a title ("TITEL: Biological Activity of Formaldehyde..."), a table ("ÜBERPRÜFTER PARAMETER", "BEANSTANDUNG"), and approval blocks. It has real content.
- Not this check.
> **Check 2: handwritten**
- Evidence: Mostly typed text. Handwriting is just signatures/dates ("21.Sep.89", "19.Okt.89", initials).
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey questions, rating scales, or questionnaire transmittal.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: No CV/resume.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal name, volume, issue, page range, DOI. "INBIFO Institut für biologische Forschung" is an institute, not a journal.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT**
- Evidence: No financial line items, invoices, budgets.
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
- Evidence: No Material Safety Data Sheet, product formulation, or "shall/must" requirement language. It's a QA review.
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
- Evidence: Not a slide deck, cover, or press release.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM**
- Evidence: The page has a structured table with labeled columns ("ÜBERPRÜFTER PARAMETER", "BEANSTANDUNG"), filled with text. It has approval/signature blocks at the bottom ("KENNTNISNAHME/STELLUNGNAHME DURCH PROJEKTLEITER: HHM", "TEAM: BC TEAM-MANAGER: HHM", "DATUM/ZN", "KENNTNISNAHME DURCH GM: UHA", "DATUM/ZN"). The header says "ÜBERPRÜFUNG DURCH QA-UNIT". This is a QA/parameter review sheet or a filled form capturing factual data (parameters and objections/remarks).
- Let's check the definition: "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells. This also covers: ... a QA/parameter review sheet."
- Yes, this is a QA review sheet / form.
> **Check 11: CORRESPONDENCE**
- Evidence: No TO:/FROM:/RE: memo header followed by prose, no letterhead with external address and salutation.
- Not this check.
> **Check 12: PUBLISHED JOURNALISM**
- Evidence: No newspaper/magazine masthead, byline, dateline.
- Not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP**
- Evidence: No running narrative prose with objectives, methods, results. It's a structured table and approval blocks.
- Not this check.
> **Check 14: PROMOTIONAL MATERIAL**
- Evidence: No marketing layout.
- Not this check.
> Let's double check Check 10 vs Check 13.
Check 10: "administrative form ... QA/parameter review sheet ... filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
Check 13: "Running narrative prose ... Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
The page has a table with "ÜBERPRÜFTER PARAMETER" and "BEANSTANDUNG" (objections/remarks). It's a QA review of a protocol ("PRÜFZEITPUNKT: vor Ausgang des Protocols"). This is a QA/parameter review sheet. It is a form.
> Let's review the evidence for Check 10:
- "ÜBERPRÜFUNG DURCH QA-UNIT" (Review by QA unit)
- Table with "ÜBERPRÜFTER PARAMETER" (Reviewed parameter) and "BEANSTANDUNG" (Objection/Remark)
- "BEMERKUNG:" (Remark)
- "STELLUNGNAHME" (Statement/Comment)
- Approval blocks: "KENNTNISNAHME/STELLUNGNAHME DURCH PROJEKTLEITER", "KENNTNISNAHME DURCH GM"
- This perfectly matches "QA/parameter review sheet" and "administrative form".
> Runner-up: scientific_report. Ruled out because the page lacks running narrative prose (objectives, methods, results) and is instead a structured QA review table with approval blocks, which is a form (check 10).
> Final label: form.

---
### `rvl_cdip__scientific_report__0012.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "2050056147" on the right side.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a lot of content: tables, headings like "B L PLANT ANALYTICAL SUMMARY SHEET", "BURLEY", "PRODUCTION DUST", "SLURRY", "FINISHED PRODUCT CHEMICAL ANALYSIS", "FINISHED PRODUCT % OV TARGET", "HOGSHEAD REPORT". It has filled-in data.
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: The page has typed headers and tables, with handwritten data filling the cells. It is not majority freeform handwriting on blank/lined paper.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions, rating scales, or transmittal note.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No career history.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range, DOI, or copyright line belonging to a journal.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial line-item table, ledger, statement, voucher, or check face. The numbers are analytical data (averages, S.D., percentages, counts), not money.
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: The page is titled "B L PLANT ANALYTICAL SUMMARY SHEET". It contains tables for "BURLEY", "PRODUCTION DUST", "SLURRY", "FINISHED PRODUCT CHEMICAL ANALYSIS", "FINISHED PRODUCT % OV TARGET", "HOGSHEAD REPORT". These are analytical/quality control data sheets, not product specifications (which would be "shall/must" language, material safety data, product formulation). Wait, let's look at check 10.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck, cover, or statement.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: "B L PLANT ANALYTICAL SUMMARY SHEET". It has filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data. It's a QA/parameter review sheet or analytical data summary sheet. The text says: "A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)" is a form. This is a "B L PLANT ANALYTICAL SUMMARY SHEET" with tables for various parameters (Dryer stems OV, Weigh belt OV, Nitrates in stems, Production dust, Slurry, Finished product chemical analysis, Finished product % OV, Hogshead report) filled with handwritten data. This perfectly matches "administrative form" or "filled analytical or lab data sheet".
- Let's check the rules: "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells." "This also covers: ... a filled analytical or lab data sheet".
- Yes, this is a form.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: No correspondence structure.
- Not this check.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: No masthead, byline, etc.
- Not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: No running narrative prose. It's a structured data sheet.
- Not this check.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: No promotional material.
- Not this check.
> Let's double check Check 8 vs Check 10.
Check 8: specification. "Material Safety Data Sheet... product formulation... manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or "shall/must" requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no "shall/must" text is an administrative form (check 10), not a specification."
This page is a "B L PLANT ANALYTICAL SUMMARY SHEET". It's a daily/shift summary sheet for a plant (Burley, Production Dust, Slurry, Finished Product Chemical Analysis, Hogshead Report). It captures operational/analytical data (averages, S.D., counts). It doesn't specify product properties or "shall/must" requirements. It's a data capture form. So it's a form (check 10).
> Let's review the evidence for Check 10:
- Title: "B L PLANT ANALYTICAL SUMMARY SHEET"
- Sections: "BURLEY", "PRODUCTION DUST", "SLURRY", "FINISHED PRODUCT CHEMICAL ANALYSIS", "FINISHED PRODUCT % OV TARGET", "HOGSHEAD REPORT"
- Structure: Tables with rows (C, A, B shifts) and columns (AVERAGE / S.D., TARGET, etc.) filled with handwritten numbers and text.
- This is a filled analytical/lab data sheet or QA/parameter review sheet. Matches Check 10.
> Runner-up: scientific_report. Ruled out because the page is a structured data sheet with tables and handwritten entries, not running narrative prose (check 13 requires running prose).
> Final label: form.

---
### `rvl_cdip__scientific_report__0002.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None. There is a fax-like header "4.JUL.84 DRSP/NO NO69 (DIV) B27" and a signature "DRHA 4. Juli 1984", but no From/To/Sent/Subject mail header. Wait, there's an address block: "DR. W. FINK, PME RESEARCH LABORATORIES, CH-2003 NEUCHATEL". This looks like a letter or memo header, but let's check further.
- Masthead/running head: No newspaper/magazine masthead. No journal running head with volume/issue/page number. There is "INBIFO Institut für biologische Forschung · Köln" and "INBIFO" logo.
> **Check 1: file_folder**
- Evidence: The page has a title "MONTHLY REPORT ANALYTICAL CHEMISTRY, JUNE 1984 PROJECT A 0268/1215", an address block, a responsibility/sign block, remarks, distribution, and a footnote. It has real content. Not file_folder.
> **Check 2: handwritten**
- Evidence: Mostly typed text. Handwriting is just signatures and dates ("4. Jul. 84", "04. JUNI 1984", signature). Not handwritten.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. The top right has "4.JUL.84 DRSP/NO NO69 (DIV) B27" and a signature. Not a fax cover sheet.
> **Check 4: questionnaire**
- Evidence: No survey questions. Not a questionnaire.
> **Check 5: resume**
- Evidence: Not a career history.
> **Check 6: scientific_publication**
- Evidence: No journal name/volume/issue/page number on the page itself. "INBIFO" is an institute. Not a publication.
> **Check 7: financial document (invoice/budget)**
- Evidence: No line-item table of charges, no budget tracking. Not financial.
> **Check 8: specification**
- Evidence: No material safety data, no product formulation, no "shall/must" requirements. Not a specification.
> **Check 9: presentation**
- Evidence: Not a slide deck, not a press release, not a photographic slide. Not a presentation.
> **Check 10: administrative form**
- Evidence: There is a "RESPONSIBILITY (a) DATE SIGN" block with "PROJECT NO. -/1215", "Study Director:", "Quality Assurance:". This looks like an approval block or a cover page for a report. Wait, let's look at the content. It's a cover page for a "MONTHLY REPORT". Is it a form? "A form does NOT have to be blank... internal authorization/approval forms with an approval signature/date block." But this is a cover page for a report. Let's check check 13.
> **Check 11: correspondence (email, memo, letter)**
- Evidence: Address block "DR. W. FINK / PME RESEARCH LABORATORIES / CH-2003 NEUCHATEL". Title "MONTHLY REPORT / ANALYTICAL CHEMISTRY, JUNE 1984 / PROJECT A 0268/1215". Then a responsibility/sign block. Remarks: "This page is not to be transmitted to the client." Distribution: "Original into file of AC / Copies into files of GM and QA". Footnote (a). Footer with company info.
Is this a memo? "internal TO:/FROM:/RE:/SUBJECT:/DATE: header block followed directly by memo-style prose". Here we have an address to an external person (Dr. W. Fink, CH-2003 Neuchatel, Switzerland). PME Research Laboratories is likely external or a specific entity. Wait, INBIFO is "Institut für biologische Forschung". Dr. W. Fink is at PME Research Laboratories in Neuchatel. This is a cover letter or memo accompanying a monthly report.
Wait, let's re-read check 11: "letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. "Mr. T. E. Sandefur") with prose and no TO:/FROM: block."
Here we have an address to Dr. W. Fink, but no "Dear..." salutation, no prose body, no closing signature. It's just a cover page for a "MONTHLY REPORT".
Wait, could it be a memo? "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... is a memo". Dr. W. Fink is at "PME RESEARCH LABORATORIES, CH-2003 NEUCHATEL". This is an external address (Switzerland). So not a memo by the by-name rule.
Is it a letter? No salutation, no prose body, no closing signature.
Let's reconsider check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
The page has:
RESPONSIBILITY (a) | DATE | SIGN
PROJECT NO. -/1215
Study Director: [signature] [date]
Quality Assurance: [date] [signature]
Remarks: This page is not to be transmitted to the client.
Distribution: Original into file of AC, Copies into files of GM and QA.
This is a cover sheet / approval page for a report. Is it a form?
Wait, look at check 13: "ORIGINAL RESEARCH WRITE-UP -> scientific_report. Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page with authors and an internal affiliation and no journal identifiers. Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."
This page is ONLY labeled field-value entries (title, project no, responsibility block, remarks, distribution). It is the cover page of a monthly report. Since it lacks running prose, it cannot be a scientific_report.
Could it be a form? "internal authorization/approval forms with an approval signature/date block." Yes, this is an approval/cover sheet for a report.
Wait, let's look at the label options again.
Is there any other category?
What about "scientific_report"? Check 13 says "Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
This page has "MONTHLY REPORT", "ANALYTICAL CHEMISTRY", "PROJECT A 0268/1215", and an approval block. It is a form (cover/approval page).
Let's check check 10 again: "administrative form -> form. ... internal authorization/approval forms with an approval signature/date block." This fits perfectly. The page is an approval/cover sheet for a monthly report.
> Let's double check if it could be a letter. Addressed to Dr. W. Fink. But no salutation, no body, no closing. Just a cover sheet.
Could it be a memo? Addressed to external person (Switzerland). Not a memo.
> Let's review the evidence for form (check 10):
- "RESPONSIBILITY (a) DATE SIGN" block
- "Study Director:" with signature and date
- "Quality Assurance:" with date and signature
- "Remarks:" and "Distribution:" fields
- This is an internal authorization/approval form or cover sheet for a report. The instructions say: "internal authorization/approval forms with an approval signature/date block" are forms.
> Wait, is there any chance this is a scientific_report?
"Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
This page has no running prose. It's just metadata and approval signatures. So it's a form.
> Let's check if there's any other check.
Check 1: file_folder. No, has real content (title, approval block).
Check 2: handwritten. No.
Check 3: fax. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial. No.
Check 8: specification. No.
Check 9: presentation. No.
Check 10: form. Yes, approval block, labeled fields.
Check 11: correspondence. No salutation, no body, no closing. Addressed to external person but no letter format.
Check 12: news_article. No.
Check 13: scientific_report. No running prose.
Check 14: advertisement. No.
> Therefore, the label is "form".
> Let's refine the scratchpad:
- file_folder: no — page has a title "MONTHLY REPORT", project number, approval block, remarks, and distribution list; not just an identifier.
- handwritten: no — mostly typed, only signatures and dates are handwritten.
- fax: no — no fax cover sheet header.
- questionnaire: no — no survey questions.
- resume: no — not a career history.
- scientific_publication: no — no journal running head or publication identifier.
- financial: no — no financial data or billing.
- specification: no — no product requirements or material data.
- presentation: no — not a slide deck or press release.
- form: yes — contains a "RESPONSIBILITY (a) DATE SIGN" block, "Study Director:" and "Quality Assurance:" fields with signatures and dates, "Remarks:", and "Distribution:" fields; this is an internal authorization/approval form or cover sheet for a report, which falls under check 10.
- correspondence: no — addressed to an external person (Dr. W. Fink, Neuchatel) but lacks a salutation, prose body, and closing signature; not a memo (external addressee) or letter (missing required letter elements).
- news_article: no — no masthead or journalistic layout.
- scientific_report: no — lacks running narrative prose; only labeled field-value entries and an approval block, which check 13 explicitly excludes from scientific_report and assigns to form.
- advertisement: no — no promotional content.
> Runner-up: scientific_report, ruled out because the page lacks running prose and consists only of labeled field-value entries and an approval block, which check 13 explicitly classifies as a form.
> Final label: form.

---
### `rvl_cdip__scientific_report__0003.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There is a Bates number "81305509" on the right side, rotated.
> **Check 1: file_folder**
- Content: "A AND B COMPOUND RESULTS SUMMARY", "FILE NO: A310", followed by a list of fields (NAME, NREC, SEAC, TESTING STATUS, DECISION TREE, ISS, CHEM ABSTRACTS NUMBER, FEMA NUMBER, PH, MUTAGENICITY VEHICLE, IP VEHICLE, ORAL VEHICLE, IV VEHICLE, SPECIAL INSTRUCTIONS, AWESI, ACUTXI R1).
- This is not just an identifier/stamp. It has a title "A AND B COMPOUND RESULTS SUMMARY" and structured data fields. Not file_folder.
> **Check 2: handwritten**
- Content is typed. Not handwritten.
> **Check 3: FAX TRANSMISSION SHEET**
- No fax header.
> **Check 4: questionnaire**
- Not a survey instrument.
> **Check 5: resume**
- Not a resume.
> **Check 6: scientific_publication**
- No journal running head, volume, issue, page number.
> **Check 7: financial document**
- No financial content.
> **Check 8: specification**
- "A AND B COMPOUND RESULTS SUMMARY", "FILE NO: A310", "NAME: BICYCLO[4.4.0]DEC-1-EN-3-ONE".
- Lists testing status, decision tree, chemical abstracts number, pH, mutagenicity vehicle, vehicles, special instructions.
- This looks like a summary of test results for a chemical compound. Is it a specification?
- Specification: Material Safety Data Sheet, product formulation, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, "shall/must" language. Product-referenced test data is a specification. A titled product-analysis table is a specification.
- Wait, this is a "COMPOUND RESULTS SUMMARY". It's a summary of test results for a specific compound.
- Let's check check 10 (form) and check 13 (scientific_report).
> **Check 9: presentation**
- Not a slide deck.
> **Check 10: ADMINISTRATIVE FORM**
- Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data.
- This page has labeled fields: "NAME:", "NREC:", "SEAC:", "TESTING STATUS:", "DECISION TREE:", "ISS:", "CHEM ABSTRACTS NUMBER:", "FEMA NUMBER:", "PH:", "MUTAGENICITY VEHICLE:", "IP VEHICLE:", "ORAL VEHICLE:", "IV VEHICLE:", "SPECIAL INSTRUCTIONS:", "AWESI:", "ACUTXI R1:".
- It is capturing factual data about a compound (BICYCLO[4.4.0]DEC-1-EN-3-ONE).
- Is it a form? "A form does NOT have to be blank — a filled form recording data is still a form... This also covers: a standalone labeled data chart or table... a filled analytical or lab data sheet".
- Wait, check 13: "Original research write-up -> scientific_report". Requires running narrative prose. This page has no running narrative prose, just labeled field-value entries. So it's not scientific_report.
- Is it a specification? "Product-referenced test data is a specification. A titled product-analysis table... is a specification". But this is a "COMPOUND RESULTS SUMMARY" with field-value pairs, not a table of test results (like mainstream smoke analyses). It's more of a data capture sheet or a summary form for a compound's testing status and properties.
- Let's re-read check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... a filled analytical or lab data sheet". This looks like a lab data sheet or a compound summary form.
- Let's re-read check 8: "test-analysis tables keyed to product/part codes... A labeled product/parameter rate-data chart... is a specification". This is not a table or chart, it's a list of fields.
- Let's look at check 10 again: "internal authorization/approval forms with an approval signature/date block." This doesn't have that. But it has "filled fields... for capturing factual data".
- Actually, this looks like a form used to record compound data. "NAME: ... FILE NO: ...". It's a structured data capture page.
- Let's consider if it's a scientific_report. "Requires running narrative prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report." This perfectly matches: "only labeled field-value entries". So it's a form.
> Let's double check check 10 vs check 8.
Check 8: "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification".
This page is titled "A AND B COMPOUND RESULTS SUMMARY". It has "NAME: BICYCLO[4.4.0]DEC-1-EN-3-ONE". It lists properties (PH, vehicles, special instructions) and testing status. It's not a table of test results (measurements), it's a summary of the compound's parameters and testing status. This is a form capturing data/parameters.
Wait, "A AND B COMPOUND RESULTS SUMMARY" could be a form.
Let's look at the fields:
NAME: BICYCLO[4.4.0]DEC-1-EN-3-ONE
NREC:
SEAC:
TESTING STATUS: ACTIVE 11-06-90
DECISION TREE: II 11-21-90
ISS: PENDING 11-06-90
CHEM ABSTRACTS NUMBER: NA
FEMA NUMBER: NA
PH: 5.60 @ 28C
MUTAGENICITY VEHICLE: DMSO
IP VEHICLE:
ORAL VEHICLE: EMUL 12MC; OIL
IV VEHICLE: INSOLUBLE
SPECIAL INSTRUCTIONS: FORMS EMULSION IN 12 MC AND IS SOLUBLE IN CORN OIL
AWESI: PENDING 09-30-91
ACUTXI R1: ORAL PENDING 09-30-91
> This is a structured data entry / summary sheet for a chemical compound. It captures factual data (names, numbers, statuses, vehicles, instructions). It fits "filled or blank fields... for capturing factual data" -> form.
Also, "a filled analytical or lab data sheet" is a form.
> Let's check if there's any other category.
Could it be scientific_report? No, no running prose.
Could it be specification? No "shall/must", no test-analysis table with measurements, just a summary of parameters and status.
> Therefore, form (check 10).
> Let's review the scratchpad steps:
1. file_folder: no — has a title "A AND B COMPOUND RESULTS SUMMARY" and structured data fields, not just an identifier.
2. handwritten: no — typed text.
3. FAX: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no — no journal identifier.
7. financial: no.
8. specification: no — not a test-analysis table with measurements, tolerances, or "shall/must" language; it's a summary of compound parameters and testing status.
9. presentation: no.
10. form: yes — page consists of labeled field-value entries (NAME, NREC, SEAC, TESTING STATUS, DECISION TREE, ISS, CHEM ABSTRACTS NUMBER, FEMA NUMBER, PH, MUTAGENICITY VEHICLE, etc.) capturing factual data about a chemical compound. Check 10 explicitly states that a page that is only labeled field-value entries is a filled form, not a scientific report.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no — requires running narrative prose; this page is only labeled field-value entries.
14. advertisement: no.
> Runner-up: scientific_report, ruled out because the page lacks running narrative prose and consists only of labeled field-value entries, which check 10 classifies as a form.
> Wait, is there any possibility it's a specification?
"Product-referenced test data is a specification."
But this is not test data (results of a test), it's a summary of the compound's properties and testing *status* (ACTIVE, PENDING). "TESTING STATUS: ACTIVE", "DECISION TREE: II", "ISS: PENDING". This is a tracking/summary form for a compound's development status. Definitely a form.
> Final check of the text:
"A AND B COMPOUND RESULTS SUMMARY"
"FILE NO: A310"
"NAME: BICYCLO[4.4.0]DEC-1-EN-3-ONE"
...
"Bates number: 81305509"
> Yes, form.

---

## invoice → form (3 errors)

### `rvl_cdip__invoice__0003.png`
**Expected:** `invoice` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow a specific scratchpad procedure, checking 1-14 in order.
> Let's analyze the image.
The document is a "Telefax Copy" from "INSIFO Institut für biologische Forschung GmbH".
It has a fax header: "Telefax Copy", "16. FEB. 1989", "# 767" (handwritten).
There's a date "16. Aug. 1989" and handwritten notes "Original an Herr zurück 28.1. 89 g", "Kopie 67 28.2. 89".
The main content is a "BESTELLUNG" (Order) Nr.: 522/88/07656.
It lists items: "IDEA-Arbeitsplatz-Kombination", "Standcontainer", "Arbeitstisch", etc.
It has a total price: "Gesamtpreis: 12.377,-- netto", "zuzügl. 14 % MwSt".
It has delivery terms, payment terms.
It is an order form / invoice / purchase order. Wait, "BESTELLUNG" means order. It's a purchase order or an order confirmation.
Let's look at the categories:
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> Is it an invoice?
"invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due... A payment VOUCHER... A hotel/motel guest bill... Likewise a landlord's rent/lease statement... is an invoice"
Wait, this is a "BESTELLUNG" (Order). Is an order an invoice?
Let's check the definition of invoice in the prompt: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document... It does not have to be titled "INVOICE" — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
Wait, a purchase order is not an invoice. But let's look at the text: "Wir bestellen aufgrund umseitiger Einkaufsbedingungen: ... Gesamtpreis: 12.377,-- netto". This is a purchase order (Bestellung).
Is there a "form" category?
"10. ADMINISTRATIVE FORM -> form: Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... A form does NOT have to be blank — a filled form recording data is still a form... This also covers: a standalone labeled data chart or table... and internal authorization/approval forms with an approval signature/date block."
Wait, is a purchase order a form? Or is it an invoice?
Let's re-read check 7 (invoice): "an outside vendor, supplier, or agency states charges owed for goods or services SOLD". This document is from INSIFO to someone else? "Ihr Schreiben... Unter Zeichen PST/IBM Ref. No. IBM108B23". "Wir bestellen..." (We order...). So INSIFO is ordering from someone else (maybe a vendor). Or is INSIFO the vendor? "Als Anlage erhalten Sie Ihr o. a. Angebot in Fotokopie, das Bestandteil dieser Bestellung ist..." (As an attachment you receive your above-mentioned offer in photocopy, which is part of this order...). So INSIFO is the buyer, ordering from a vendor.
Wait, if it's a purchase order, is it a form? Or is it an invoice?
Actually, what if it's considered a form? "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... an application...". A purchase order is a type of form.
Wait, let's look at check 7 again: "invoice: ... an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement with unit prices, amounts, and totals."
Is a purchase order an invoice? No.
Is it a budget? "internal money planning, tracking, or disbursement... budget or expense lines...". No.
Is it a form? "ADMINISTRATIVE FORM -> form: Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data...". A purchase order has line items, quantities, prices. It's a structured document for capturing order data.
Wait, could it be a letter? "letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature". No salutation, no "Dear".
Could it be a memo? "memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose". No.
> Let's look closely at the document.
Header: "Telefax Copy", "INSIFO Institut für biologische Forschung GmbH", "Kaufmännische Verwaltung".
Date: "13.Feb.89".
Reference: "Ihr Schreiben", "Unter Zeichen PST/IBM", "Ref. No. IBM108B23".
Title: "BESTELLUNG Nr.: 522/88/07656".
Table with columns: "Menige" (Menge), "Artikel", "Preis DM".
Rows: numbered list of items (Standcontainer, Arbeitstisch, etc.).
Total: "Gesamtpreis: 12.377,-- netto", "zuzügl. 14 % MwSt".
Terms: "Liefertermin", "Lieferbedingungen", "Zahlungsweise".
Footer: "INSIFO Institut für biologische Forschung GmbH", address, signature.
Bates number: "2024474923" on the right edge.
> This is a purchase order (Bestellung).
Does it fit "invoice"? "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD". This is a buyer stating charges owed? No, it's a buyer ordering goods. The vendor will send an invoice.
Wait, is a purchase order considered a "form"?
Check 10: "ADMINISTRATIVE FORM -> form: Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application (research grant, employment, service request); a records-management inventory or log table... A form does NOT have to be blank — a filled form recording data is still a form... This also covers: a standalone labeled data chart or table... and internal authorization/approval forms with an approval signature/date block."
A purchase order is a standard business form. It has ruled lines for items, quantities, prices. It captures factual data (order details).
Wait, could it be an invoice? Sometimes purchase orders and invoices are confused, but strictly, a purchase order is not an invoice. However, in document classification, sometimes "invoice" is used broadly for billing documents. But the prompt says: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD". This document is from INSIFO (buyer) to a vendor. "Wir bestellen..." (We order...). So it's a purchase order.
Is there an "order" category? No.
The categories are: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
If it's not invoice, it must be form.
Let's check if there's any other match.
Could it be a letter? "A dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block." No, this is a structured order form.
Could it be a memo? No.
> Let's re-read check 7 carefully:
"invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document... It does not have to be titled "INVOICE" — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
This document lists items and a total price ("Gesamtpreis: 12.377,-- netto"). But it is a "BESTELLUNG" (Order), not an invoice. The text says "Als Anlage erhalten Sie Ihr o. a. Angebot in Fotokopie, das Bestandteil dieser Bestellung ist..." (As an attachment you receive your above-mentioned offer in photocopy, which is part of this order...). This confirms it's a purchase order based on an offer.
Since "purchase order" is not explicitly listed, and it's not an invoice (vendor selling), it falls under "form" (check 10) as an administrative form for capturing order data.
Wait, is a purchase order a "form"? Yes, it's a structured document with fields for item, quantity, price.
Let's check check 10 again: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form". This document has a table with ruled lines for capturing order data (items, quantities, prices). It is a filled/formatted order form.
> Wait, is there any chance it's an invoice?
Sometimes, a document titled "BESTELLUNG" with a total price and tax is treated as an invoice in broad terms, but the prompt is very specific: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD". Here, INSIFO is the buyer ("Wir bestellen"). The vendor is the one selling. So INSIFO is not stating charges owed for goods sold; they are stating charges they owe for goods bought. Wait, "charges owed" could mean the buyer owes money. But "goods or services SOLD" implies the vendor's perspective. "an outside vendor... states charges owed for goods or services SOLD". This is from the vendor's perspective. This document is from the buyer's perspective. So it's not an invoice under this strict definition.
Therefore, it's a form.
> Let's check if it could be a letter.
"letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature".
This document has letterhead (INSIFO), date (13.Feb.89), but no "Dear ..." salutation. It has a structured order table. So not a letter.
> Could it be a memo?
"memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose".
No TO:/FROM: block.
> So it's a form (check 10).
> Let's review the scratchpad steps:
1. file_folder: no — has substantial body content (order table, terms, total price), not just an ID/stamp.
2. handwritten: no — mostly typed, only some handwritten annotations ("# 767", "Original an Herr zurück...", "Kopie 67 28.2. 89").
3. fax: no — "Telefax Copy" is a fax transmission header, but the pre-scan says "a FAX machine transmission header... is NOT a mail-client header... you must classify the underlying document by its own content". The underlying document is an order. Wait, check 3 is "FAX TRANSMISSION SHEET -> form: A "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET"... header with To/From/company/phone/page-count fields." This page has "Telefax Copy" and a fax date stamp, but it's not a fax cover sheet; it's the actual document being faxed. So not check 3.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. invoice/budget: no — it's a purchase order ("BESTELLUNG") from a buyer (INSIFO) to a vendor, not an invoice from a vendor stating charges for goods sold. It's not a budget (internal money planning).
8. specification: no.
9. presentation: no.
10. form: yes — it is a structured purchase order ("BESTELLUNG") with a table for capturing order data (items, quantities, prices), delivery terms, and payment terms. It uses ruled lines and fields for factual data capture.
11. correspondence: no — no TO:/FROM: memo header, no "Dear..." letter salutation.
12. news_article: no.
13. scientific_report: no.
14. advertisement: no.
> Wait, is a purchase order considered a "form"?
Yes, "ADMINISTRATIVE FORM -> form: Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data...". A purchase order is a classic administrative form.
> Let's double check if there's any other interpretation.
What if it's considered an invoice because it has a total price and tax?
"invoice: ... It does not have to be titled "INVOICE" — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
But this is a "BESTELLUNG" (Order). The text explicitly says "das Bestandteil dieser Bestellung ist" (which is part of this order). It's a purchase order. A purchase order is not an invoice. An invoice is a bill. A purchase order is a request to buy.
So "form" is the most accurate label.
> Let's refine the scratchpad:
- file_folder: no — page contains a full order document with line items, prices, and terms, not just an identifier.
- handwritten: no — mostly typed text with minor handwritten annotations; handwriting does not make up the majority of the content.
- fax: no — "Telefax Copy" is a fax transmission header, not a fax cover sheet form (check 3). The underlying document is an order.
- questionnaire: no — not a survey instrument.
- resume: no.
- scientific_publication: no — no journal running head.
- invoice/budget: no — this is a "BESTELLUNG" (purchase order) from a buyer (INSIFO) to a vendor, not an invoice from a vendor stating charges for goods sold. It is not an internal budget or expense report.
- specification: no — not a product specification or safety data sheet.
- presentation: no — not a slide deck or cover page.
- form: yes — the page is a structured purchase order ("BESTELLUNG") with a table for capturing order data (items, quantities, prices), delivery terms, and payment terms. It uses ruled lines and fields for factual data capture, fitting the definition of an administrative form.
- correspondence: no — lacks a memo header (TO:/FROM:/RE:) or a letter salutation ("Dear ...") and closing signature; it is a structured business form.
- news_article: no.
- scientific_report: no — no running narrative prose of research.
- advertisement: no.
> Runner-up: invoice, ruled out because the document is a purchase order ("BESTELLUNG") from a buyer to a vendor, not an invoice from a vendor stating charges for goods sold (check 7 requires the vendor's perspective of goods sold).
> Wait, the prompt says: "A hotel/motel guest bill or folio... is an invoice... Likewise a landlord's rent/lease statement... is an invoice".
Is a purchase order an invoice? No.
Is there any other category? "form" is the best fit.
> Let's check the pre-scan for mail-client header or masthead.
- Mail-client header: none. "Telefax Copy" is a fax header.
- Masthead: none. "INSIFO Institut für biologische Forschung GmbH" is a company letterhead, not a newspaper/magazine masthead.
> Check 10 evidence: "BESTELLUNG" (Order) with a table of items ("Menige", "Artikel", "Preis DM"), total price ("Gesamtpreis: 12.377,-- netto"), and terms ("Liefertermin", "Zahlungsweise"). This is a structured form for capturing order data.
> Final label: form.

---
### `rvl_cdip__invoice__0006.png`
**Expected:** `invoice` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "The American Tobacco Company" at the top left, "REQUISITIONER'S COPY" at top right. This is a company letterhead/header, not a newspaper/magazine masthead or journal running head.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a lot of content: purchase order number, date, supplier info, description of posters, pricing, accounting charge number. Not just an identifier.
- Result: not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Mostly typed text. There is a handwritten signature at the bottom right and some handwritten annotations (like "T-045" at top right, and a diagonal line). Not majority handwritten.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions or transmittal note.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No career history.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal running head, volume, issue, page range.
- Result: not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: This is a Purchase Order (PO No. A 21248, Date January 21, 1976). It lists a supplier (MacNaughton Lithograph Company), description of goods (TARYTON 30-Sheet Posters), quantity (2,012), price ($9.62 ea.), and total amount implied. Wait, is a purchase order an invoice or budget?
- Let's look at the definitions.
- invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher... a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document... A check face/check stub... is the DISBURSEMENT instrument and stays budget".
- budget: "internal money planning, tracking, or disbursement... A check face or check stub... Also covers money-only records... A provider's periodic customer statement... is budget, not invoice".
- Wait, what about a Purchase Order? A purchase order is a request to buy goods. It's an internal authorization/request to spend money or a commitment.
- Let's re-read check 7 carefully.
- "invoice: an outside vendor... states charges owed... A payment VOUCHER... is a payment instrument that BILLS a named payee... invoice".
- "budget: internal money planning, tracking, or disbursement... Also covers money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient... is budget, not form... But an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
- Wait, is a Purchase Order a form or a budget or an invoice?
- Let's look at Check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."
- "Caveat: an internal expenditure-authorization form (an "AUTHORIZATION REQUEST" for funds, "ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget — authorizing a specific expenditure or funded project is not planning or tracking money."
- This document is a "PURCHASE ORDER" (implied by "PURCHASE ORDER NO. A 21248", "REQUISITIONER'S COPY", "BILLING INSTRUCTIONS - MAIL YOUR INVOICES..."). It is a requisition/purchase order form. It has fields: Supplier, Ship To, Quantity, Code No., Description, Price. It has an approval block at the bottom (signature, accounting charge no.).
- Is it a form (check 10) or budget (check 7)?
- Check 7 says: "an internal expenditure-authorization form (an "AUTHORIZATION REQUEST" for funds, "ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget". This document *does* have billable charges (Quantity 2,012, Price $9.62 ea., description of posters). Wait, a purchase order *is* a request to buy, but it specifies the charges.
- Let's re-read check 10: "internal authorization/approval forms with an approval signature/date block."
- Let's re-read check 7: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." But is a purchase order a billing page? No, it's a purchase order. The vendor is instructed to "MAIL YOUR INVOICES IN TRIPLICATE...". So this is not the invoice.
- Is it a budget? "internal money planning, tracking, or disbursement... A check face or check stub...". A purchase order is a commitment, but is it budget?
- Let's look at the labels again. "form" is check 10. "budget" is check 7. "invoice" is check 7.
- The document is a Purchase Order / Requisition. It has structured fields (Supplier, Ship To, Quantity, Description, Price). It is an administrative form for purchasing.
- Check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."
- This is a purchase requisition / purchase order form. It captures factual data (supplier, description, quantity, price) and has an approval block (signature at bottom right, accounting charge no.).
- Therefore, it is a form.
> Let's double check if it could be an invoice. "BILLING INSTRUCTIONS - MAIL YOUR INVOICES IN TRIPLICATE TO CONSIGNEE..." - This explicitly says the vendor will send an invoice later. So this page is NOT an invoice.
Could it be a budget? "internal money planning...". A purchase order is a commitment, but the definition of budget focuses on "budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub...". A purchase order is typically classified as a form (procurement form) or if it's just a request, it's a form. The caveat in check 7 says: "an internal expenditure-authorization form... that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget". This has billable charges (quantity, price), but it's still a purchase order/requisition form. Wait, if it has billable charges, does it become an invoice? No, because it's not a vendor stating charges owed; it's the buyer stating what they want to buy and at what price. The vendor will invoice.
Actually, let's look at check 10 again. "administrative form -> form... internal authorization/approval forms with an approval signature/date block." This fits perfectly. A purchase order/requisition is an administrative form.
> Let's check if there's any other category.
- advertisement: no.
- email: no.
- letter: no.
- memo: no.
- news_article: no.
- presentation: no.
- scientific_publication: no.
- scientific_report: no.
- specification: no.
> So it's either form or budget.
Check 7 (budget): "internal money planning, tracking, or disbursement...". A purchase order is a disbursement authorization, but usually, purchase orders are forms. The caveat in check 7: "an internal expenditure-authorization form (an "AUTHORIZATION REQUEST" for funds, "ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget". This document is a "purchase requisition" (it says "REQUISITIONER'S COPY" at the top right). It has billable charges (posters, $9.62 ea.), but it's a requisition/purchase order form. The function is to capture the purchase details (supplier, description, quantity, price) and get approval. This is an administrative form.
Also, check 10 explicitly mentions "internal authorization/approval forms with an approval signature/date block."
> Let's review the document content:
Header: "The American Tobacco Company", "REQUISITIONER'S COPY".
Fields: "PURCHASE ORDER NO. A 21248", "DATE January 21, 1976", "REQ. NO. Auth. M-18".
"BILLING INSTRUCTIONS - MAIL YOUR INVOICES IN TRIPLICATE..."
"TO: MacNaughton Lithograph Company..."
"SHIP TO: As per instructions attached"
"SHIPMENT TO ARRIVE NOT LATER THAN As Below", "VIA Truck", "TERMS Net Cash 10 Days".
Table: "QUANTITY", "CODE NO.", "DESCRIPTION", "PRICE".
Row: "2,012", "", "TARYTON 30-Sheet Posters, Bleed Size 125" x 272" @ $9.62 ea.", "" (price is in description).
Bottom: "ACCOUNTING CHARGE NO. Corporate Media Dept. A.T.Co.", checkboxes for tax/exemption, "Please contact MISS VANCE PULEO", signature.
> This is a Purchase Requisition / Purchase Order form. It is an administrative form (check 10).
> Let's check if it could be a specification (check 8). "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables...". No, this is a purchase order for posters.
> Let's check if it could be an invoice (check 7). "an outside vendor... states charges owed". This is from the buyer (American Tobacco Company) to the vendor (MacNaughton Lithograph Company), instructing them to mail invoices. So it's not an invoice.
> Therefore, the label is `form`.
> Wait, could it be `budget`?
"budget: internal money planning, tracking, or disbursement... A check face or check stub... Also covers money-only records...". A purchase order is a commitment of funds, but the document is a structured form with fields for supplier, description, quantity, price, and an approval block. The instructions say: "an internal expenditure-authorization form... purchase/requisition approval... is a form (check 10), not budget". This is exactly a purchase requisition/approval form.
> Final check of the scratchpad steps:
1. file_folder: no, has real content (PO details, table).
2. handwritten: no, mostly typed.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial (invoice/budget): The page is a purchase requisition/order. It is not an invoice (vendor states charges owed) nor a budget (internal tracking/forecast/check stub). The caveat in check 7 explicitly excludes "purchase/requisition approval" forms from budget, classifying them as form (check 10).
8. specification: no.
9. presentation: no.
10. form: yes. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block." The page has PO number, date, supplier fields, a table for quantity/description/price, accounting charge number, checkboxes, and a signature block. It is a purchase requisition form.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no.
14. advertisement: no.
> Runner-up: budget, ruled out because the document is a purchase requisition/approval form (check 7 caveat explicitly excludes purchase requisition approvals from budget, pointing to form), and it is not an invoice because the billing instructions say "MAIL YOUR INVOICES".
> Label: form.

---
### `rvl_cdip__invoice__0014.png`
**Expected:** `invoice` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify the provided document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "THE AMERICAN TOBACCO COMPANY" logo at top left. "REQUISITIONER'S COPY" at top right. No newspaper/magazine masthead, no journal running head.
> **2. Scratchpad procedure:**
> *Check 1: file_folder*
- Evidence: The page has a lot of content: billing instructions, supplier info, purchase order number, line items with quantities, descriptions, prices, accounting charge, signature. Not just an identifier/stamp.
- Result: not this check.
> *Check 2: handwritten*
- Evidence: There is a handwritten name "L. Cannarota" and a signature at the bottom. But the majority of the content is typed text (form fields, line items, descriptions).
- Result: not this check.
> *Check 3: FAX TRANSMISSION SHEET*
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Result: not this check.
> *Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire*
- Evidence: No survey questions, rating scales, or commitment application.
- Result: not this check.
> *Check 5: PERSON'S CAREER HISTORY -> resume*
- Evidence: No CV/resume content.
- Result: not this check.
> *Check 6: PUBLISHED EVIDENCE -> scientific_publication*
- Evidence: No journal name, volume, issue, page range, DOI on this page.
- Result: not this check.
> *Check 7: FINANCIAL DOCUMENT -> invoice or budget*
- Evidence: The page is a "REQUISITIONER'S COPY" of a Purchase Order (PO No. M 13174). Wait, let's look closer.
- It has "PURCHASE ORDER NO. M 13174", "DATE May 27, 1992", "REQ. NO. Auth #R-44".
- Supplier: Webcraft Technologies, Inc.
- Line items: "CARLTON Tar Chart 'Reward and Shelter' Direct Mail Units", Quantity 400,000, Price $787.21/M. "Plus Prep., Proof, Programming" $7,600.00. "Advanced Postage - 3rd Class Bulk Rate - Indicia" ($93,200.00). "Non-Standard Ink Charge" $250.00/ea.
- "ACCOUNTING CHARGE NO. Marketing Adv. Exp."
- "STATE SALES TAX NOT TO BE CHARGED..."
- "Please contact on any questions regarding this Purchase Order."
- Is this an invoice or a budget?
- Let's re-read Check 7 carefully.
- "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher... a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document... It does not have to be titled 'INVOICE' — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
- "budget: internal money planning, tracking, or disbursement... A check face/check stub... Also covers money-only records... A provider's periodic customer statement... is budget, not invoice"
- Wait, this is a Purchase Order (PO). A PO is a request to buy, not a bill for goods sold yet. But let's look at the billing instructions: "BILLING INSTRUCTIONS - MAIL YOUR INVOICES IN DUPLICATE TO CONSIGNEE... MAIL INVOICES TO OUR ADMINISTRATIVE CENTER." This implies the document itself is a Purchase Order, and the vendor will send an invoice later.
- However, look at the line items: it lists quantities, descriptions, and prices. "400,000 CARLTON Tar Chart... $787.21/M". Total isn't explicitly summed at the bottom, but there are prices.
- Wait, is a Purchase Order an invoice or a budget or a form?
- Let's check Check 10: ADMINISTRATIVE FORM. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."
- This is a Purchase Order form. It has fields for Supplier, Ship To, PO Number, Date, Req No, Quantity, Code No, Description, Price, Accounting Charge No. It has a signature block "By _______".
- Is it a financial document (Check 7) or a form (Check 10)?
- Check 7 says: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face."
- "A check face/check stub... is the DISBURSEMENT instrument and stays budget".
- "An internal expenditure-authorization form (an 'AUTHORIZATION REQUEST' for funds... purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget".
- This document is a "REQUISITIONER'S COPY" of a Purchase Order. It authorizes the purchase. It lists the items and prices, but it's a requisition/purchase order form.
- Wait, look at the bottom: "AT 103-M (5-86)". This is a form number.
- Let's re-evaluate Check 7 vs Check 10.
- Check 7 invoice: "an outside vendor... states charges owed". This is from The American Tobacco Company (buyer) to Webcraft Technologies (supplier). It's a Purchase Order. A PO is not an invoice. An invoice is sent by the vendor. The billing instructions say "MAIL YOUR INVOICES...". So this is not an invoice.
- Check 7 budget: "internal money planning, tracking, or disbursement... A check face... budget". "A provider's periodic customer statement... is budget". This is a PO. Is a PO a budget? "budget: internal money planning...". A PO is a commitment of funds, often part of budget tracking. But is it primarily a financial document like a ledger or statement?
- Let's look at Check 10: "internal authorization/approval forms with an approval signature/date block." A purchase requisition/order is an authorization to spend money. "An internal expenditure-authorization form... that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget". This document has prices listed, but it's a requisitioner's copy of a PO. It's an authorization form.
- Wait, let's look at the content again. It's a "REQUISITIONER'S COPY". It has "PURCHASE ORDER NO.", "DATE", "REQ. NO.". It has "SUPPLIER", "SHIP TO", "QUANTITY", "CODE NO.", "DESCRIPTION", "PRICE". It has "ACCOUNTING CHARGE NO.". It has a signature "By [signature]".
- This is a Purchase Requisition / Purchase Order form. It captures data for an administrative purpose (procurement).
- Let's check if there's any other category.
- Is it a form? Yes, it has fields, boxes, checkboxes ("AS SHOWN BELOW", "EXEMPTION CERTIFICATE", "DIRECT PAYMENT PERMIT", "IN YOUR FILES", "ATTACHED"). It's a structured document for capturing procurement data.
- Let's re-read Check 7 carefully to ensure it's not an invoice. "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD". This document is from The American Tobacco Company (buyer) to Webcraft (supplier). It's a PO. Not an invoice.
- Is it a budget? "budget: internal money planning, tracking, or disbursement...". A PO is a commitment, but is the *primary structure* a financial document like a line-item table of charges owed? The table here is the PO line items. But Check 7 says "Check 7 applies only when financial content IS the page's primary structure... If the page is otherwise formatted as correspondence... and a dollar figure... is merely mentioned... classify as correspondence". Here, the page IS a financial table (PO line items). But is it an invoice or budget?
- "A check face/check stub... stays budget". This is not a check.
- "An internal expenditure-authorization form... is a form (check 10), not budget". This is a requisitioner's copy of a PO, which is an authorization to purchase. It has an approval signature ("By [signature]"). It names the work (CARLTON Tar Chart Direct Mail Units) and has prices. This fits "internal expenditure-authorization form... that names the work/project to be funded and carries an approval signature/date block". The prices are there, but it's an authorization/requisition form.
- Therefore, Check 10 (form) is the best fit.
> Let's double check Check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
This page has:
- Fields: Supplier, Ship To, PO No, Date, Req No, Quantity, Code No, Description, Price, Accounting Charge No.
- Checkboxes: "AS SHOWN BELOW", "EXEMPTION CERTIFICATE", "DIRECT PAYMENT PERMIT", "IN YOUR FILES", "ATTACHED".
- Approval block: "By [signature]".
- It is a Purchase Order / Requisition form.
> Let's check if it could be an invoice. "BILLING INSTRUCTIONS - MAIL YOUR INVOICES IN DUPLICATE TO CONSIGNEE". This explicitly says the vendor should mail invoices. So this document is NOT the invoice. It's the purchase order/requisition.
> Could it be a budget? "budget: internal money planning, tracking, or disbursement...". A PO is a step in disbursement, but the document itself is a form authorizing the purchase. The instructions say: "An internal expenditure-authorization form (an 'AUTHORIZATION REQUEST' for funds, 'ADVERTISING AND SELLING AUTHORIZATION', purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget". This document has prices listed in the description column, but it's a requisitioner's copy of a PO. Wait, it has prices: "$787.21/M", "$7,600.00", "($93,200.00)", "$250.00/ea". These are unit prices or line totals. Is this a billable charges document? No, it's a PO. The vendor will invoice based on this. The text says "Please forward a copy of U.S. Postal Document 3802 with your reconciliation and refund." This is instructions for the vendor.
> Actually, looking closely at the document, it's a "REQUISITIONER'S COPY" of a Purchase Order. The form number is "AT 103-M (5-86)". It's a standard corporate form for requisitions/purchase orders.
Therefore, it is a form (Check 10).
> Let's review the checks again to be sure.
1. file_folder: No, has content.
2. handwritten: No, mostly typed.
3. FAX: No.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No.
7. financial (invoice/budget):
   - Invoice: No, it's a PO, billing instructions say "MAIL YOUR INVOICES".
   - Budget: "internal money planning...". A PO is an authorization. Check 7 caveat: "An internal expenditure-authorization form... purchase/requisition approval... is a form (check 10), not budget". This is a requisitioner's copy of a PO, which is a purchase requisition/approval.
8. specification: No.
9. presentation: No.
10. form: Yes. Fields, checkboxes, approval signature, purchase requisition/order layout.
11. correspondence: No.
12. news_article: No.
13. scientific_report: No.
14. advertisement: No.
> Runner-up: invoice. Ruled out because the document is a "REQUISITIONER'S COPY" of a Purchase Order with billing instructions telling the vendor to "MAIL YOUR INVOICES", meaning this document itself is not the invoice but the authorization/requisition form (Check 10). Also, Check 7 explicitly excludes "purchase/requisition approval" forms from budget, pointing to form (Check 10).
> Wait, let's look at the "financial content IS the page's primary structure" rule in Check 7. The page is a table of line items with prices. But Check 10 covers "internal authorization/approval forms with an approval signature/date block". A PO is exactly that. And Check 7 says "purchase/requisition approval... is a form (check 10), not budget". So even if it has financial data, if it's a requisition/approval form, it's a form.
> Final check of the text:
"REQUISITIONER'S COPY"
"THE AMERICAN TOBACCO COMPANY"
"PURCHASE ORDER NO. M 13174"
"DATE May 27, 1992"
"REQ. NO. Auth #R-44"
"TO: Webcraft Technologies, Inc."
"SHIP TO: Mail 3rd Class Bulk Rate..."
"QUANTITY CODE NO. DESCRIPTION PRICE"
"400,000 ... CARLTON Tar Chart ... $787.21/M"
"ACCOUNTING CHARGE NO. Marketing Adv. Exp."
"By [signature]"
"AT 103-M (5-86)"
> This is clearly a Purchase Requisition / Purchase Order form. Label: form.

---

## file_folder → presentation (3 errors)

### `rvl_cdip__file_folder__0004.png`
**Expected:** `file_folder` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** None. No newspaper/magazine masthead. No journal running head.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Content: There is a Bates number "2065213892" and a rotated text "PRODUCT INTEGRITY - FDA - PRESENTATION".
    *   Wait, let's look at the text. "PRODUCT INTEGRITY - FDA - PRESENTATION". This is a bold heading/title.
    *   Rule: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
    *   Rule: "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."
    *   The text "PRODUCT INTEGRITY - FDA - PRESENTATION" is a bold headline title. It looks like a section divider or a cover page for a presentation.
    *   Wait, is it a folder tab? "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body."
    *   The text is rotated 90 degrees. "PRODUCT INTEGRITY - FDA - PRESENTATION".
    *   Let's check the rule for folder tabs vs presentation dividers.
    *   "How to tell a folder-tab page from a presentation cover/divider (check 9): a folder-tab page's ENTIRE content is the tab, its short filing label, and a Bates/stamp — nothing else is designed on the page. A presentation cover/divider is a DESIGNED title page: multiple styled title elements... a bold title on a designed background... a photograph... or a statement/press-release layout."
    *   "A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider even alongside a small handwritten letter/number annotation — but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab... is a folder-tab label and stays file_folder (check 1)."
    *   The text is "PRODUCT INTEGRITY - FDA - PRESENTATION". This sounds like a title for a presentation, not a folder label like "Litigation Content" or "NEWTROL". "PRESENTATION" is in the title itself.
    *   Also, there is a faint black bar at the bottom? "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation". There is a faint line at the bottom.
    *   Let's look at the text again. "PRODUCT INTEGRITY - FDA - PRESENTATION". This is a title.
    *   Check 9: "SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation". "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation (this check), not file_folder (check 1)."
    *   The page is mostly empty space (white). There is a bold headline title "PRODUCT INTEGRITY - FDA - PRESENTATION" rotated 90 degrees. There is a Bates number "2065213892".
    *   This fits Check 9 perfectly. "A large heading rotated 90 degrees... is a section divider... presentation". Wait, the rule says: "A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider even alongside a small handwritten letter/number annotation — but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab... is a folder-tab label and stays file_folder".
    *   Is "PRODUCT INTEGRITY - FDA - PRESENTATION" a short filing label or a bold headline title? It contains the word "PRESENTATION". It looks like a title page for a presentation.
    *   Let's re-read the folder tab exception: "a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab (product/collection/month/file name, e.g. 'NEWTROL', 'Litigation Content', 'FEBRUARY') is a folder-tab label and stays file_folder". "PRODUCT INTEGRITY - FDA - PRESENTATION" is not a simple folder name like "NEWTROL". It's a title.
    *   Also, Check 9 explicitly mentions: "A near-blank cover or title page — mostly empty space with only a bold headline title... is a presentation".
    *   So this is likely `presentation`.
> *   **Check 2: handwritten**
    *   No handwriting.
> *   **Check 3: FAX**
    *   No fax header.
> *   **Check 4: questionnaire**
    *   No survey questions.
> *   **Check 5: resume**
    *   No career history.
> *   **Check 6: scientific_publication**
    *   No journal header.
> *   **Check 7: financial**
    *   No financial data.
> *   **Check 8: specification**
    *   No product specs.
> *   **Check 9: presentation**
    *   Evidence: "mostly empty space with only a bold headline title" ("PRODUCT INTEGRITY - FDA - PRESENTATION" rotated 90 degrees) and a Bates number. This matches the description of a deck cover or section divider. The text itself says "PRESENTATION".
    *   Wait, is it a folder tab? "PRODUCT INTEGRITY - FDA - PRESENTATION". If this is a folder tab, it would be file_folder. But the text includes "PRESENTATION". Usually folder tabs have names like "FDA PRESENTATION" or "PRODUCT INTEGRITY". But the rule says: "A large heading rotated 90 degrees... is a section divider... presentation". And "A near-blank cover or title page... is a presentation".
    *   Let's look at the "Scan-artifact signal": "a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation". There is a faint line at the bottom, maybe a black bar? The text is in the bottom right quadrant (rotated).
    *   The text is "PRODUCT INTEGRITY - FDA - PRESENTATION". This is clearly a title for a presentation.
    *   So `presentation` is the label.
> *   **Check 10: form**
    *   No fields.
> *   **Check 11: correspondence**
    *   No memo/letter structure.
> *   **Check 12: news_article**
    *   No masthead.
> *   **Check 13: scientific_report**
    *   No running prose.
> *   **Check 14: advertisement**
    *   No marketing layout.
> **Conclusion:**
The page is a near-blank page with a rotated bold title "PRODUCT INTEGRITY - FDA - PRESENTATION" and a Bates number. This fits Check 9 (presentation) as a deck cover or section divider. The text explicitly says "PRESENTATION".
> Let's double check Check 1 (file_folder).
"A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with... a bold headline title (even a single word/short phrase like 'RECOMMENDATIONS' with no subtitle, or a large heading rotated 90 degrees like 'COMPETITIVE BAR PROGRAMS' — even alongside a small handwritten letter or number annotation) carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."
The text "PRODUCT INTEGRITY - FDA - PRESENTATION" is a large heading rotated 90 degrees. It is a bold headline title. Therefore, it is NOT file_folder. It is presentation.
> Final check:
- Evidence for Check 9: Rotated bold text "PRODUCT INTEGRITY - FDA - PRESENTATION", Bates number "2065213892", mostly empty space. This is a section divider or cover page for a presentation.
- Runner-up: file_folder. Ruled out because the page has a bold headline title ("PRODUCT INTEGRITY - FDA - PRESENTATION") rotated 90 degrees, which counts as real content (section divider/presentation cover), not just filing metadata. Also, the title itself says "PRESENTATION".
> Label: presentation.

---
### `rvl_cdip__file_folder__0006.png`
**Expected:** `file_folder` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: No newspaper/magazine masthead. No journal running head. There is a Bates number "2061696347" on the right side.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a large graphic (map-like background), a title "ISSUE MODULE PRODUCT INTEGRITY", "Roger Whidden PM - Worldwide Regulatory Affairs", "Control #74", "PHILIP MORRIS INTERNATIONAL". It has real content (title, author, company name). It is not just an identifier/stamp.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: No handwriting visible. All text is typed/printed.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header or fax transmission fields.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No questions, rating scales, or survey instrument layout.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No CV/resume content. "Roger Whidden" is just a name in a header.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal name, volume, issue, page range, or DOI on the page itself.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: No financial tables, line items, or money tracking.
    *   Result: not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: No material safety data, formulation, or "shall/must" language. "ISSUE MODULE PRODUCT INTEGRITY" sounds like a presentation title or section divider.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: The page looks like a slide or a deck cover.
    *   Layout: Large sparse type ("ISSUE MODULE PRODUCT INTEGRITY"), company name ("PHILIP MORRIS INTERNATIONAL"), author name ("Roger Whidden"), affiliation ("PM - Worldwide Regulatory Affairs"), "Control #74".
    *   Background: A map-like graphic (looks like a world map or a stylized map, possibly Africa/Europe/Asia).
    *   Scan artifact: There are horizontal lines across the image, typical of a photographed slide or overhead transparency. The text is overlaid on a graphic.
    *   Check 9 description: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page... A near-blank cover or title page... a deck cover...". "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead — presentation". Here we have horizontal scan lines (artifact from slide/transparency) and sparse text (title, author, company).
    *   The text "ISSUE MODULE PRODUCT INTEGRITY" is a bold title. "PHILIP MORRIS INTERNATIONAL" is at the bottom. "Roger Whidden / PM - Worldwide Regulatory Affairs" is at the top right. "Control #74" is at the top right.
    *   This looks exactly like a presentation title slide or section divider slide.
    *   Result: YES. This is a presentation.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: No fields, boxes, checkboxes.
    *   Result: not this check.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: No TO/FROM/RE header, no salutation, no closing.
    *   Result: not this check.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: No masthead, byline, dateline.
    *   Result: not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: No running narrative prose. Just a title slide.
    *   Result: not this check.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: Not a marketing layout with product imagery/slogans for sale. It's an internal corporate presentation slide ("Issue Module", "Product Integrity", "Control #74").
    *   Result: not this check.
> **Conclusion:**
The page is a presentation slide/cover. It has the visual characteristics of a photographed slide (horizontal scan lines, sparse text, large title, company branding). The content "ISSUE MODULE PRODUCT INTEGRITY" with "Roger Whidden" and "PHILIP MORRIS INTERNATIONAL" is typical of a corporate presentation title slide or section divider.
> Let's re-verify Check 9.
"Slide/overhead layouts... a deck title or section-divider page... A near-blank cover or title page... a deck cover...".
"Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead". Here we have horizontal lines (scan artifact from a transparency/slide) and the text is sparse.
The text "ISSUE MODULE PRODUCT INTEGRITY" is a title.
"PHILIP MORRIS INTERNATIONAL" is the company.
This is a presentation.
> Runner-up: file_folder. Ruled out because there is a bold topical heading ("ISSUE MODULE PRODUCT INTEGRITY") and real content (author, company), not just a filing label. Wait, check 1 says "A prominent topical heading always counts as real content... it is a cover/title page, section divider, or photographic slide (presentation, check 9)". So file_folder is ruled out.
> Final label: presentation.

---
### `rvl_cdip__file_folder__0011.png`
**Expected:** `file_folder` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header: None.
- Masthead/running head: None. There is text rotated 90 degrees on the left side: "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964". There is a dashed line and a solid line at the bottom.
> **2. Scratchpad procedure:**
> *   **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
    *   Evidence: The page is almost entirely blank. There is rotated text on the left: "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964". There is a dashed line and a solid line at the bottom.
    *   Wait, let's look at the rules for file_folder.
    *   "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
    *   "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title (even a single word/short phrase like "RECOMMENDATIONS" with no subtitle, or a large heading rotated 90 degrees like "COMPETITIVE BAR PROGRAMS" — even alongside a small handwritten letter or number annotation) carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."
    *   The text is "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964". This looks like a bold headline title rotated 90 degrees.
    *   Let's check Check 9: "A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider even alongside a small handwritten letter/number annotation — but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab... is a folder-tab label and stays file_folder".
    *   Is this a folder tab? The text is "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964". It doesn't look like a folder tab label (which usually names a product, collection, month, or file description). It looks like a section divider or title page for a section called "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964".
    *   Wait, let's look at the layout. It's rotated text on the left margin. There's a dashed line. There's a solid line at the bottom. This looks like a section divider or a cover page for a section.
    *   Check 9: "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... a single-word/short-phrase heading with no subtitle at all... a deck cover, or a section divider — is a presentation (this check), not file_folder".
    *   The text "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964" is a bold headline title. It is rotated 90 degrees.
    *   So it's likely a presentation (section divider).
> *   **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
    *   Evidence: None. Text is typed (rotated).
> *   **Check 3: FAX TRANSMISSION SHEET -> form**
    *   Evidence: None.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: None.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: None.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: None. No journal header.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: None.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: None.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: "A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider... is a presentation".
    *   The text "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964" is a large heading rotated 90 degrees.
    *   "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation". There is a solid line at the bottom (maybe a bar artifact? or just a line). The text is sparse and off-center (rotated on the left).
    *   This fits the description of a section divider or slide cover.
    *   Let's re-read the file_folder exception: "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body. The label IS filing metadata... The black bar is the photographed folder body/tab edge... it is NOT a slide-mount scan artifact".
    *   Is there a black bar? There is a solid line at the bottom left. There is a dashed line next to the text. This looks like a scanned page from a document, possibly a section divider.
    *   The text "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964" acts as a title/heading for a section.
    *   Check 9 says: "a near-blank cover or title page — mostly empty space with only a bold headline title... is a presentation".
    *   This page is mostly empty space with a bold headline title (rotated).
    *   So, presentation.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: None.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: None.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: None.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: None. No running prose.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: None.
> **Re-evaluating Check 1 vs Check 9:**
- Check 1 (file_folder): "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title (even a single word/short phrase like 'RECOMMENDATIONS' with no subtitle, or a large heading rotated 90 degrees like 'COMPETITIVE BAR PROGRAMS'... carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."
- The text is "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964". This is a bold headline title, rotated 90 degrees.
- Therefore, it is NOT file_folder. It is a section divider or cover page.
- Check 9 (presentation): "a near-blank cover or title page — mostly empty space with only a bold headline title... a section divider — is a presentation". Also "A large heading rotated 90 degrees... is a section divider".
- So the label is presentation.
> Let's look closely at the image.
- Text: "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964" rotated 90 degrees counter-clockwise.
- Dashed line to the right of the text.
- Solid line at the bottom.
- Very sparse content.
- This matches the "section divider" or "near-blank cover" description in Check 9.
> Wait, is it a folder tab?
- "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body."
- The text "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964" doesn't look like a folder tab label. Folder tab labels are usually short: "Litigation Content", "NEWTROL", "FEBRUARY". This is a section title for a document part.
- Also, the rule says: "a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab... is a folder-tab label and stays file_folder".
- But "a large heading rotated 90 degrees like 'COMPETITIVE BAR PROGRAMS'... carries real content — it is a cover/title page, section divider... (presentation, check 9)".
- "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964" is a heading for a section of analysis. It's a section divider.
> So, presentation.
> Let's check the runner-up.
- file_folder: ruled out because the page carries a bold headline title rotated 90 degrees ("TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964"), which counts as real content (section divider), not just filing metadata.
> Final decision: presentation.
> One detail: "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
- There is a solid line at the bottom. It might be a bar artifact.
- The text is sparse and off-center (rotated on the left edge).
- This reinforces presentation.
> Let's double check Check 1 exception: "EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... is a filing label, not a bold headline title... The page stays file_folder even when the label is rotated 90 degrees".
- Is "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964" a short label on a folder tab?
- It looks like text printed on the page margin, not a photograph of a tab. The dashed line suggests a margin or a fold. The solid line at the bottom looks like a scan artifact or a page border.
- If it were a folder tab, the text would be the content of the tab. But "TOBACCO ANALYSIS: Butler - Dealers Special Samples 1964" sounds like a section title within a larger document (e.g., a report on tobacco analysis for Butler dealers).
- The rule says: "a large heading rotated 90 degrees like 'COMPETITIVE BAR PROGRAMS'... carries real content — it is a cover/title page, section divider... (presentation, check 9)".
- This heading is similar in nature to "COMPETITIVE BAR PROGRAMS". It's a section title.
- So it's presentation.
> Label: presentation.

---

## advertisement → form (2 errors)

### `rvl_cdip__advertisement__0003.png`
**Expected:** `advertisement` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. Just a mostly blank page with some text at the bottom right.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: There is a number "725" handwritten at the top right. There is typed text with labels: "Brand: Lucky 100's", "Publication: News American", "Date: 4/17/74", "Size: 8 1/2 x 14 1/4 (121.1)". "Comments: Ad Warning: 14 pt - short", "T & N - 16 pt - 10pt neg".
    *   Is this just an identifier? No, it has specific data about an advertisement (Brand, Publication, Date, Size, Comments). It's not a folder tab. It's not a Bates number alone. It has real content.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: Most of the content is typed labels ("Brand:", "Publication:", etc.) with handwritten entries ("Lucky 100's", "News American", "4/17/74", "8 1/2 x 14 1/4 (121.1)", "14 pt - short", "16 pt - 10pt neg").
    *   Wait, is it "majority handwritten"? The typed labels are there, but the actual content is handwritten. However, the structure is a printed template with fields (Brand, Publication, Date, Size, Comments). The handwriting fills the fields.
    *   Rule: "Handwriting filling in labeled printed fields is form, not handwritten".
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No questions, no survey instrument.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal header.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: No financial data (money amounts, invoices, budgets). Just ad specs.
    *   Result: not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: "Brand: Lucky 100's", "Publication: News American", "Size: 8 1/2 x 14 1/4". This looks like an ad specification or placement sheet.
    *   Rule: "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables... 'shall/must' language."
    *   This is an ad placement detail. Is it a specification? "Product-referenced test data is a specification." "A labeled product/parameter rate-data chart... is a specification".
    *   Wait, let's look at Check 14 (advertisement) or Check 10 (form).
    *   This page describes an advertisement: Brand, Publication, Date, Size, Ad Warning specs. It's a specification for an ad, or a form capturing ad details.
    *   Let's check Check 10 first.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: Mostly blank space. Text is at the bottom right.
    *   Rule: "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead". There is no black bar here, just white space.
    *   Rule: "A near-blank cover or title page... is a presentation". But this has specific data fields.
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: "Brand:", "Publication:", "Date:", "Size:", "Comments:", "Ad Warning:", "T & N -". These are labeled fields (printed labels) filled with handwritten data.
    *   Rule: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form".
    *   This looks like a form capturing ad placement details.
    *   Result: **YES**. This is a form.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: No TO/FROM/RE header, no salutation, no closing.
    *   Result: not this check.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: "Publication: News American". This is the name of the publication where the ad will run, not the page itself being a news article.
    *   Result: not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: No running prose.
    *   Result: not this check.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: The content is *about* an advertisement (Brand: Lucky 100's, Ad Warning), but the page itself is not the advertisement. It's a data sheet/form describing the ad specs.
    *   Rule: "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures." This page has none of that. It's a text form.
    *   Result: not this check.
> **Re-evaluating Check 10 vs Check 8 (Specification):**
- Check 8: "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables... 'shall/must' language."
- This page is "Brand: Lucky 100's, Publication: News American, Date: 4/17/74, Size: 8 1/2 x 14 1/4". This is an ad placement specification or a form for ad tracking.
- Check 10: "Filled or blank fields... for capturing factual data". This fits perfectly. It's a form capturing ad details.
- Is it a specification? "Product-referenced test data is a specification." This isn't test data. It's ad placement data.
- "A labeled product/parameter rate-data chart... is a specification". This is not a chart.
- So it's a form.
> **Re-evaluating Check 1 (file_folder):**
- "Almost no body content: only an archive/Bates number, a stamp, a short label or ID... No sentences, no topical title."
- This page has "Brand: Lucky 100's", "Publication: News American", etc. This is real content (data about an ad). It's not just an ID.
- Wait, is this a "folder tab"? No, it's a typed form with handwritten entries.
- Is it a "section divider"? No.
> **Conclusion:**
The page is a form (Check 10). It has printed field labels ("Brand:", "Publication:", "Date:", "Size:", "Comments:") and handwritten entries filling those fields. It captures factual data about an advertisement placement.
> Let's double check Check 14 (advertisement).
- "Judge by DOMINANT content... a single brand ad with product imagery... is advertisement".
- This page has no imagery, no slogans (except maybe "Lucky 100's" as a brand name in a field), no Surgeon General warning. It's a metadata sheet for an ad. So it's a form.
> Let's double check Check 2 (handwritten).
- "Most of the content is freeform handwriting... NOT on a printed template."
- This is on a printed template (labels are printed: Brand, Publication, Date, Size, Comments, Ad Warning, T & N). The handwriting fills the fields. So it's a form.
> Final decision: form.
> Wait, looking closely at the text:
"Brand: Lucky 100's"
"Publication: News American"
"Date: 4/17/74"
"Size: 8 1/2 x 14 1/4 (121.1)"
"Comments:"
"Ad Warning: 14 pt - short"
"T & N - 16 pt - 10pt neg"
"725" (handwritten number at top right).
> This is a form capturing ad specifications.
> One detail: "A page whose primary structure is a memo header + prose...". Not applicable.
"A standalone labeled data chart or table... is a form". This is a list of labeled fields. Fits form.
> The label is `form`.
> Let's check if it could be `specification`.
Check 8: "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables... tolerances, or 'shall/must' requirement language."
This is ad specs (font size, placement). Not really a product specification in the manufacturing sense. It's an administrative form for ad tracking/placement.
Check 10 covers "administrative form".
> Let's check if it could be `advertisement`.
Check 14: "Marketing layout: product imagery, slogans...". No imagery here. Just text fields.
> So `form` is the best fit.
> One more check: `file_folder`.
"A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
This page has a table-like structure of fields. It's real content.
> Final check on `handwritten`.
"Handwriting filling in labeled printed fields is form, not handwritten".
The labels "Brand:", "Publication:", "Date:", "Size:", "Comments:", "Ad Warning:", "T & N -" are printed. The entries are handwritten. So it's a form.
> The label is `form`.

---
### `rvl_cdip__advertisement__0015.png`
**Expected:** `advertisement` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. Just a number "1127" and some handwritten text.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: There is a number "1127" (likely a Bates number or similar ID) and some handwritten text.
    *   Is it almost no body content? It has "Brand: Lucky Ten", "Publication: El Diario", "Date: 11/8/74", "Size: 3 1/2 x 7 (24.5 sq.in)". This is a short note describing an advertisement or publication.
    *   Wait, is this a folder tab? No, it looks like a handwritten note on a white page.
    *   Is it a form? No printed fields.
    *   Is it a presentation? No.
    *   Let's look at the content. It's a handwritten note describing an ad placement or publication detail. "Brand: Lucky Ten", "Publication: El Diario", "Date: 11/8/74", "Size: 3 1/2 x 7 (24.5 sq.in)".
    *   Wait, check 1 says: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
    *   "A prominent topical heading always counts as real content... EXCEPTION — folder tabs". This is not a folder tab. It's a handwritten note.
    *   Wait, is it handwritten? Check 2.
> *   **Check 2: handwritten**
    *   Evidence: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
    *   The text is:
        Brand: Lucky Ten
        Publication: El Diario
        Date: 11/8/74
        Size: 3 1/2 x 7 (24.5 sq.in)
    *   There are printed labels: "Brand:", "Publication:", "Date:", "Size:".
    *   Wait, looking closely at the image:
        "Brand: Lucky Ten" -> "Brand:" is typed/printed. "Lucky Ten" is handwritten.
        "Publication: El Diario" -> "Publication:" is typed/printed. "El Diario" is handwritten.
        "Date: 11/8/74" -> "Date:" is typed/printed. "11/8/74" is handwritten.
        "Size: 3 1/2 x 7 (24.5 sq.in)" -> "Size:" is typed/printed. The rest is handwritten.
    *   So there is a printed template with labels "Brand:", "Publication:", "Date:", "Size:".
    *   Check 2 says: "It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form".
    *   So if there are printed field labels, it's a form (Check 10).
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: None.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
    *   Evidence: None.
> *   **Check 5: PERSON'S CAREER HISTORY**
    *   Evidence: None.
> *   **Check 6: PUBLISHED EVIDENCE**
    *   Evidence: None.
> *   **Check 7: FINANCIAL DOCUMENT**
    *   Evidence: None.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
    *   Evidence: None.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
    *   Evidence: None.
> *   **Check 10: ADMINISTRATIVE FORM**
    *   Evidence: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
    *   The page has printed labels: "Brand:", "Publication:", "Date:", "Size:". And handwritten values filling them.
    *   This looks like a form capturing data about an advertisement or publication.
    *   Wait, is it a form? "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
    *   The labels "Brand:", "Publication:", "Date:", "Size:" are printed field labels. The content "Lucky Ten", "El Diario", "11/8/74", "3 1/2 x 7 (24.5 sq.in)" is filled in.
    *   This fits "Administrative Form". It's capturing data about an ad placement (Brand, Publication, Date, Size).
> *   **Check 11: CORRESPONDENCE**
    *   Evidence: None.
> *   **Check 12: PUBLISHED JOURNALISM**
    *   Evidence: None.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP**
    *   Evidence: None.
> *   **Check 14: PROMOTIONAL MATERIAL**
    *   Evidence: None. The page describes an ad, but isn't the ad itself.
> Let's re-evaluate Check 1 vs Check 2 vs Check 10.
The page has printed text: "Brand:", "Publication:", "Date:", "Size:".
And handwritten text: "Lucky Ten", "El Diario", "11/8/74", "3 1/2 x 7 (24.5 sq.in)".
And a number "1127" at the top right.
> Is this a "note" that is handwritten?
Check 2: "The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten. Handwriting filling in labeled printed fields is form, not handwritten".
Here, we have printed field labels: "Brand:", "Publication:", "Date:", "Size:".
So it is NOT handwritten (Check 2 fails).
> Is it file_folder (Check 1)?
Check 1: "Almost no body content: only an archive/Bates number, a stamp, a short label or ID... No sentences, no topical title."
"A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
Wait, "or a note". If it's a note, it's not file_folder?
Actually, the rule says: "A page is NOT file_folder if it carries any real content... or a note."
But then Check 2 says "handwriting... is handwritten".
If it's a filled form, it's Check 10.
The text is structured data: Brand, Publication, Date, Size. This is data capture.
So it's a form (Check 10).
> Let's look at the labels again.
"Brand: Lucky Ten"
"Publication: El Diario"
"Date: 11/8/74"
"Size: 3 1/2 x 7 (24.5 sq.in)"
This is a data entry form, likely for tracking advertisements in publications (El Diario is a Spanish-language newspaper).
It has printed field labels and filled values.
This fits Check 10: "Filled or blank fields... for capturing factual data".
> Let's check if there's any other category.
Could it be a "specification"? No.
Could it be "advertisement"? No, it's metadata about an ad.
> So, Check 10 (form) seems correct.
> Wait, is "1127" a Bates number? Yes, likely.
Is the whole page just a note?
The printed text is very minimal: just the labels.
But the labels define a form structure.
Check 10: "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
> Let's reconsider Check 1 (file_folder).
"A Bates number or archive stamp alone is NOT enough... A page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content".
Here we have a Bates number (1127) and a filled-in data block.
The data block has printed labels. This makes it a form.
> Let's reconsider Check 2 (handwritten).
"Handwriting filling in labeled printed fields is form, not handwritten".
The labels "Brand:", "Publication:", "Date:", "Size:" are printed.
So it is form.
> Final decision: form.
> Wait, looking very closely at the image.
The text "Brand:", "Publication:", "Date:", "Size:" looks like it might be typed on a typewriter or printed.
"Lucky Ten", "El Diario", "11/8/74", "3 1/2 x 7 (24.5 sq.in)" is handwritten.
This is a filled form.
> One detail: "A log/diary sheet is freeform, not a form: a minimal sheet with only ONE typed column header... and blank ruled lines... is handwritten".
Here we have multiple typed labels (Brand, Publication, Date, Size). This is a structured form, not a log sheet.
> So, Check 10 is the winner.
> Let's double check Check 14 (advertisement).
The content is about an advertisement (Lucky Ten in El Diario). But the page itself is not the ad. It's a record of the ad.
Check 14: "Marketing layout: product imagery, slogans...". This page has none of that.
> So, form.
> One more check: Is it a "specification"?
Check 8: "Material Safety Data Sheet... product formulation...". No.
> Is it a "scientific_report"?
No prose.
> So, form.
> Wait, is there any chance this is a "file_folder"?
Check 1: "A patent/invention filing index card with several labeled fields... is still file_folder".
This has labeled fields: Brand, Publication, Date, Size.
But a patent index card is for cataloging/identifying one filed item.
This page is capturing data about an ad placement.
"A page titled 'RECORDS MANAGEMENT INVENTORY'... containing a multi-row/multi-column table... is a form".
This is a single row of data capture.
Check 10: "Filled or blank fields... for capturing factual data".
This fits perfectly. It's a form capturing ad placement data.
> The label is "form".
> Let's re-read the scratchpad instructions.
"Walk checks 1-14 below IN ORDER."
Check 1: file_folder.
Evidence: Bates number 1127. But there is also a data block with labels "Brand:", "Publication:", etc.
Rule: "A page is NOT file_folder if it carries any real content... or a note."
Actually, the rule says "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
Wait, if it's a note, it's not file_folder.
But if it's a filled form, it's form (Check 10).
Since Check 10 comes after Check 1, and Check 1 says "Almost no body content", this page has body content (the filled data).
So Check 1 fails.
> Check 2: handwritten.
Evidence: Handwriting fills the fields.
Rule: "Handwriting filling in labeled printed fields is form, not handwritten".
So Check 2 fails.
> Check 3-9: Fail.
> Check 10: form.
Evidence: Printed labels "Brand:", "Publication:", "Date:", "Size:" with handwritten values. Capturing factual data.
This matches.
> Runner-up: handwritten. Ruled out because the page has printed field labels ("Brand:", "Publication:", etc.) and the handwriting fills these fields, which makes it a form (Check 10), not freeform handwriting (Check 2).
> Final label: form.

---

## budget → invoice (2 errors)

### `rvl_cdip__budget__0008.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: No newspaper/magazine masthead. No journal running head. There is a logo "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING". There is a Bates number "2040766038" rotated on the right side. "FORM M-01 REV 05-82" at the bottom left.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a lot of content: a table with product names, periods, gross amounts, gross change, gross less C/D. It has headers like "ESTIMATE RECAP - PM01(D)", "CLIENT: P.M. INC.", "DESC: 702A CAMBRIDGE SUPPLEMENTS".
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: The page is typed throughout. No significant handwriting.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No survey questions.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No biographical info.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal name, volume, issue, page range, DOI.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: The page is titled "ESTIMATE RECAP - PM01(D)".
    *   It says "EST NO: 9118 REVISES EST DTD 01/13/89".
    *   It lists "GROSS AMOUNT", "GROSS CHANGE", "GROSS LESS C/D".
    *   It has totals: "TOTAL 288,577.48" and "283,671.68".
    *   Let's look at the instructions for Check 7.
    *   "invoice": "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
    *   This page has: "EST NO: 9118", "REVISES EST DTD 01/13/89", "GROSS LESS C/D" (which looks like "C/D" for credits/adjustments, similar to "C/D" in the example "EST AMT LESS C/D"). Wait, the example says "EST AMT LESS C/D". Here it says "GROSS LESS C/D".
    *   Let's re-read the invoice bullet: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns..."
    *   This page has "EST NO: 9118", "REVISES EST DTD 01/13/89". It compares columns (Gross Amount, Gross Change, Gross Less C/D).
    *   Wait, let's look at the budget bullet: "Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
    *   This document is an "ESTIMATE RECAP". It has "EST NO: 9118 REVISES EST DTD 01/13/89". This matches the invoice criteria: "names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")".
    *   The table shows "TOTALS BY PRODUCT/MONTH ON SALE DATE". It lists "32-CAMBRIDGE" (a cigarette brand, likely Camel or similar, actually Cambridge is a brand or product line, maybe "702A CAMBRIDGE SUPPLEMENTS").
    *   The amounts are large: 144,288.74, 72,144.37. These look like ad spend or billing amounts.
    *   Leo Burnett is an advertising agency. P.M. Inc. is Philip Morris.
    *   This is an advertising agency billing/recap for a client.
    *   The text says "EST NO: 9118 REVISES EST DTD 01/13/89". This is a revised estimate.
    *   According to the rules: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")..."
    *   So this is an invoice.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: Not a material safety data sheet or product formulation. It's a financial recap.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: Not a slide deck.
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: It has a form number "FORM M-01 REV 05-82". It has fields. But check 7 (Financial Document) overrides form layout if financial content is the primary structure.
    *   Result: not this check (because check 7 matches).
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: No TO/FROM/RE header followed by prose.
    *   Result: not this check.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: No masthead.
    *   Result: not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: No running narrative prose.
    *   Result: not this check.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: Not a single brand ad. It's an internal/agency financial document.
    *   Result: not this check.
> **Re-evaluating Check 7 (Invoice vs Budget):**
The document is an "ESTIMATE RECAP".
Header: "MAGAZINE ESTIMATE RECAP - PM01(D)"
"EST NO: 9118 REVISES EST DTD 01/13/89"
"DESC: 702A CAMBRIDGE SUPPLEMENTS"
Table columns: "GROSS AMOUNT", "GROSS CHANGE", "GROSS LESS C/D".
Totals: 288,577.48 and 283,671.68.
> The instructions say:
"invoice: ... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns..."
> This document has:
- "EST NO: 9118" (names an estimate number)
- "REVISES EST DTD 01/13/89" (revises a prior estimate)
- Columns comparing amounts (Gross Amount, Gross Change, Gross Less C/D).
> Therefore, it is an invoice.
> Wait, is it a budget?
"budget: ... Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice"
> This document has "EST NO" and "REVISES EST". So it falls into the invoice category according to the specific exception in the instructions.
> Let's check the labels again.
The label is "invoice".
> Let's double check if there's any other category.
It's a financial document.
Check 7: FINANCIAL DOCUMENT -> invoice or budget.
Evidence: "EST NO: 9118 REVISES EST DTD 01/13/89", "ESTIMATE RECAP", line items with dollar amounts totaling ~283k.
Specifically, the invoice bullet says: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")..."
This matches perfectly.
> Final check of the scratchpad steps:
1. file_folder: No, has table content.
2. handwritten: No, typed.
3. fax: No.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No.
7. financial (invoice): Yes. "EST NO: 9118 REVISES EST DTD 01/13/89", "ESTIMATE RECAP", line items with amounts. Matches invoice criteria for agency estimate/recap that revises a prior estimate.
8. specification: No.
9. presentation: No.
10. form: No, check 7 overrides.
11. correspondence: No.
12. news_article: No.
13. scientific_report: No.
14. advertisement: No.
> Runner-up: budget. Ruled out because the document names an estimate number ("EST NO: 9118") and revises a prior estimate ("REVISES EST DTD 01/13/89"), which makes it an invoice (billing document) per the check 7 instructions, rather than a pure planning budget.
> Wait, looking closely at the table:
"TOTALS BY PRODUCT/MONTH ON SALE DATE"
"32-CAMBRIDGE"
"APR 1989 ... 144,288.74"
"MAY ... .00"
"QUARTER 2 ... 144,288.74"
This looks like ad placements or billing for magazine ads.
Leo Burnett is an advertising agency. P.M. Inc. is the client.
This is an invoice/recap of charges/estimates for advertising services.
The text "EST NO: 9118 REVISES EST DTD 01/13/89" confirms it's a revised estimate acting as a bill/recap.
The rule: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")..."
> So, invoice.
> One detail: "GROSS LESS C/D". C/D likely means Credits/Debits or Credits/Adjustments. Similar to "EST AMT LESS C/D" in the example.
> The classification is invoice.

---
### `rvl_cdip__budget__0020.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> Document analysis:
Header: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING"
Title: "OUTDOOR ESTIMATE RECAP - ODO1(S)"
Period: "01/01/90 TO 12/31/90"
Date: "04/06/90"
Page: "1"
Client: "P.M. INC."
Office: "10"
Est No: "O136 REVISES EST DTD 03/09/90"
Desc: "774A MERIT ODP 2-SHEET COMMUTER RAIL"
> Table: "TOTALS BY PRODUCT/MONTH"
Columns: PRODUCT, PERIOD, GROSS AMOUNT, GROSS CHANGE
Rows: 14-PARLIAMENT (MAR 1990, QUARTER 1, APR, MAY, JUN, QUARTER 2, SEP, QUARTER 3, OCT, QUARTER 4, TOTAL)
27-MERIT (MAY 1990, QUARTER 2, JUL, AUG, QUARTER 3, TOTAL)
GRAND TOTAL (MAR 1990, QUARTER 1, APR, MAY, JUN, QUARTER 2, JUL, AUG, SEP, QUARTER 3, OCT, QUARTER 4, TOTAL)
> Footer: "FORM M-01 REV 05-82", Bates number "2040786142"
> Let's go through the checks.
> Check 1: file_folder. No, it has a lot of body content (a financial table).
Check 2: handwritten. No, it's typed.
Check 3: FAX. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial document -> invoice or budget.
Let's look at the invoice vs budget rules for check 7.
"invoice: ... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
The document has:
"EST NO: O136 REVISES EST DTD 03/09/90"
It names an estimate number ("O136") and revises a prior estimate ("REVISES EST DTD 03/09/90").
It has "GROSS AMOUNT" and "GROSS CHANGE" columns.
This matches the invoice bullet perfectly: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")..."
> Wait, let's re-read the budget bullet:
"Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
> This document has "EST NO: O136 REVISES EST DTD 03/09/90". It names an estimate number and revises a prior estimate. Therefore, it is an invoice.
> Let's double check.
"EST NO: O136 REVISES EST DTD 03/09/90" -> names estimate number, revises prior estimate.
"GROSS AMOUNT" and "GROSS CHANGE" -> lists charges/amounts.
This is an invoice.
> Check 8: specification. No.
Check 9: presentation. No.
Check 10: form. No, financial content overrides form layout (check 7).
Check 11: correspondence. No.
Check 12: news_article. No.
Check 13: scientific_report. No.
Check 14: advertisement. No.
> So the label is invoice.
> Let's write the scratchpad.
file_folder: no — the page contains a detailed financial table with line items, totals, and amounts, not just an identifier or stamp.
handwritten: no — the page is entirely typed.
fax: no — no fax transmission header or cover sheet.
questionnaire: no — does not ask the reader to answer or rate anything.
resume: no — not a career history.
scientific_publication: no — no journal running head or publication identifier.
financial (invoice/budget): yes — the document is an "OUTDOOR ESTIMATE RECAP" from Leo Burnett U.S.A. for client P.M. INC. It explicitly states "EST NO: O136 REVISES EST DTD 03/09/90", which names an estimate number and revises a prior estimate. It lists gross amounts and gross changes for products (14-PARLIAMENT, 27-MERIT) and quarters. Under check 7, an agency estimate/recap that names an estimate number and revises a prior estimate is the agency's bill for a client job, making it an invoice, not a budget (which would only plan future spend without an estimate number or revision line).
specification: no — not a material safety data sheet or product formulation.
presentation: no — not a slide deck or cover page.
form: no — although it has a form number at the bottom ("FORM M-01 REV 05-82"), check 7 states that money function overrides form layout, and this is a billing document (invoice).
correspondence: no — no mail header, memo header, or letter structure.
news_article: no — no masthead or journalistic layout.
scientific_report: no — no running narrative prose of research.
advertisement: no — not a promotional layout.
> Runner-up: budget, ruled out because the document names an estimate number ("EST NO: O136") and revises a prior estimate ("REVISES EST DTD 03/09/90"), which under check 7 makes it an invoice (the agency's bill for a client job) rather than a budget (which only plans future spend).
> Final label: invoice.

---

## specification → form (2 errors)

### `rvl_cdip__specification__0006.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "50052 7368" on the right edge.
> **Check 1: file_folder**
- Evidence: The page has a lot of content: "Analytical information (detailed)", "Quantitative", "Qualitative", "Structural Formula", "Types of Tobacco", "Tox.-Pharm. Inform. and other Notes", "Reference", "Bibliography", patent info ("British American Tobacco Limited... MATERIAL FOR FILTERING TOBACCO SMOKE..."). It's not just an identifier.
- Not this check.
> **Check 2: handwritten**
- Evidence: There is a handwritten signature/name at the top ("Goldschlager"?). But the rest is typed text, fields, and printed instructions. Not majority handwritten.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No career history.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal running head, volume, issue, page number on this page itself. The text cites patents and a journal ("Ger. Pat. Gaz."), but that's inside the content.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial data, invoices, budgets.
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: The page is titled "Analytical information (detailed)" with fields for "Smoke", "Green", "Cured", "Non-Leaf", "Itemize:". It asks for "Quantitative", "Qualitative", "Structural Formula", "Mol. Form", "Mol. Weight", "Chem. Groups", "Derivatives", "Types of Tobacco", "Tox.-Pharm. Inform.", "Reference", "Bibliography". It contains patent info for "MATERIAL FOR FILTERING TOBACCO SMOKE - CONTAINING CARBON PARTICLES COATED INTERNALLY - EXTERNALLY WITH POROUS LAYER OF ORGANIC POLYMER." This looks like a data collection form or a specification sheet for a material/patent. Wait, let's look at Check 10.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: The page has structured fields, boxes, checkboxes (Smoke, Green, Cured, Non-Leaf), ruled entry lines for capturing factual data ("Quantitative (all figures)", "Qualitative only", "Structural Formula", "Mol. Form", "Mol. Weight", "Chem. Groups", "Derivatives", "Types of Tobacco", "Tox.-Pharm. Inform. and other Notes", "Reference", "Bibliography"). It's a form for capturing analytical information about a tobacco material/patent. The bottom text says "If there is not sufficient space available for any of the categories, use reverse side, identifying category(ies), and write 'over' on this side. List all answerable information for each constituent and do so in index style." This is clearly a form for data capture.
- Let's re-read Check 8 vs Check 10.
- Check 8: specification. "Material Safety Data Sheet... product formulation... manufacturing-change authorization, test-analysis tables keyed to product/part codes... A titled product-analysis table... is a specification". This page is a form to *capture* analytical information, not a table *of* analysis results. It has blank fields to be filled out (though some patent info is filled in at the bottom). The top part is a template: "Analytical information (detailed) Smoke Green Cured Non-Leaf Itemize: Quantitative... Qualitative... Structural Formula...". This is a form.
- Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form". This page is a form for capturing analytical information about a material/patent.
- Let's check if it's a scientific_report. No running prose.
- Let's check if it's a specification. "test-analysis tables keyed to product/part codes... A labeled product/parameter rate-data chart... is a specification". This is a blank/filled form for *recording* analytical info, not a published analysis table. The bottom has patent info filled in, but the top is a form template. Actually, looking closely, the bottom part is filled with patent data: "RJR CLASS NO. PATENT British American Tobacco Limited... MATERIAL FOR FILTERING TOBACCO SMOKE...". This looks like a patent abstract or data sheet form.
- Is it a form? Yes, it has fields, checkboxes, and instructions for filling it out ("List all answerable information..."). It's an administrative form for capturing data.
> Let's re-evaluate Check 8 vs Check 10.
Check 8: "test-analysis tables keyed to product/part codes... A titled product-analysis table... is a specification". This page is not a table of analysis results; it's a form *to* record analysis results or patent info. The top half is blank fields. The bottom half has some text filled in. The text at the bottom "Bibliography: If there is not sufficient space..." is an instruction for filling the form. This is definitely a form (Check 10).
> Let's check Check 13: scientific_report. "Requires running narrative prose... a page that is only labeled field-value entries... is a filled form (check 10)". This page has labeled field-value entries (mostly blank, some filled at the bottom). So it's a form.
> Therefore, Check 10 is the correct match.
> Let's double check Check 1: file_folder. "A page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content". This page has real content (form fields, patent text). Not file_folder.
> Let's double check Check 8: specification. "Material Safety Data Sheet... product formulation... manufacturing-change authorization, test-analysis tables...". This is a form for "Analytical information (detailed)". It's a data capture form. Check 10 covers "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This matches perfectly.
> Final decision: form.
> Wait, is there any other category?
The page has "Analytical information (detailed)" at the top.
Fields: Smoke, Green, Cured, Non-Leaf (checkboxes).
Quantitative, Qualitative.
Structural Formula, Mol. Form, Mol. Weight, Chem. Groups, Derivatives.
Types of Tobacco.
Tox.-Pharm. Inform. and other Notes.
Reference.
Bibliography.
Bottom text: "RJR CLASS NO. PATENT British American Tobacco Limited... MATERIAL FOR FILTERING TOBACCO SMOKE...".
This is a form for patent/analytical data.
> Label: form.

---
### `rvl_cdip__specification__0013.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None. (There's a date/time at the top left: "DATE . FRI, MAR 1, 1985, 8:21 AM", but no From/To/Sent/Subject).
- Masthead/running head: None. Just a Bates number "50512 3457" at the bottom right.
> **Check 1: file_folder**
- Evidence: The page has a lot of body content (test number, requested by, classification, test purpose, special instructions, filter making, making & packing, testing). Not just an identifier/stamp.
- Not this check.
> **Check 2: handwritten**
- Evidence: The text is typed (dot-matrix or similar). No majority handwriting.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE", "FAX COVER SHEET", etc. The top left has "DATE . FRI, MAR 1, 1985, 8:21 AM" and "PAGE 1 OF 3", which looks like a fax transmission header, but the instructions say: "a FAX machine transmission header is NOT a mail-client header... it does not make the page an email, and you must classify the underlying document by its own content". Wait, check 3 is "FAX TRANSMISSION SHEET -> form". A fax cover sheet has "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", or "TELEFAX MESSAGE NO." header with To/From/company/phone/page-count fields. This page has "DATE", "TEST NUMBER", "CHARGE NUMBER", "REQUESTED BY", "DATE REQUESTED", "RELATED TEST NUMBER", "DIVISION", "CLASSIFICATION", "TEST PURPOSE", "MAKING AND PACKING DATE", "MAIL OUT DATE", "TYPE OF PANEL TESTING", "SPECIAL INSTRUCTIONS", "TOBACCO PROCESSING", "FILTER MAKING", "MAKING & PACKING", "TESTING". This is not a fax cover sheet.
- Not this check.
> **Check 4: questionnaire**
- Evidence: No survey questions, rating scales, etc. It's a test request/instruction sheet.
- Not this check.
> **Check 5: resume**
- Evidence: No career history.
- Not this check.
> **Check 6: scientific_publication**
- Evidence: No journal running head, volume, issue, page range.
- Not this check.
> **Check 7: financial document (invoice/budget)**
- Evidence: "CHARGE NUMBER: 1300", "DATE REQUESTED: 840705", "DIVISION: 775". But no line-item table of charges, no amounts due, no budget tracking. It's a test request.
- Not this check.
> **Check 8: specification**
- Evidence: "CLASSIFICATION: WINS KS", "TEST PURPOSE: CONSUMER SATISFACTION PROGRAM", "SPECIAL INSTRUCTIONS: TOBACCO PROCESSING: TOBACCO VARIETY C53-44X IS STORED... USE AS DESCRIBED IN BLEND FORMULATION. ANALYSE EACH BLEND COMPONENT... FILTER MAKING: PREPARE FILTERS AS DESCRIBED USING CURRENT WIN. KS CONFIGURATION AND SPECS. MAKING & PACKING: NEED 20 CTNS... TESTING: STANDARD ANALYSES."
- This looks like a test request or instruction sheet for a product test. Is it a specification? "Product-referenced test data is a specification. A titled product-analysis table... is a specification". This is not a product-analysis table. It's a request for testing.
- Not this check.
> **Check 9: presentation**
- Evidence: Not a slide deck, cover, or statement.
- Not this check.
> **Check 10: administrative form**
- Evidence: Filled or blank fields, boxes, checkboxes, ruled entry lines for capturing factual data. This page has labeled fields: "DATE", "TEST NUMBER", "CHARGE NUMBER", "PRIORITY", "REQUESTED BY", "DATE REQUESTED", "RELATED TEST NUMBER", "DIVISION", "CLASSIFICATION", "TEST PURPOSE", "MAKING AND PACKING DATE", "MAIL OUT DATE", "TYPE OF PANEL TESTING", "SPECIAL INSTRUCTIONS", "TOBACCO PROCESSING", "FILTER MAKING", "MAKING & PACKING", "TESTING". The fields are filled with typed text. This is a form capturing test request data and instructions. "A form does NOT have to be blank — a filled form recording data is still a form". This is a filled form (test request/instruction form).
- Let's check if there's a better match. It's a test request form. "administrative form -> form". Yes, it has labeled fields and filled data.
> **Check 11: correspondence (email, memo, letter)**
- Evidence: No TO:/FROM:/RE: header followed by prose. No external address, no salutation.
- Not this check.
> **Check 12: news_article**
- Evidence: No masthead, byline, dateline.
- Not this check.
> **Check 13: scientific_report**
- Evidence: No running narrative prose with objectives, methods, results. It's a form with instructions.
- Not this check.
> **Check 14: advertisement**
- Evidence: No marketing layout.
- Not this check.
> Let's re-evaluate Check 10 vs others.
The page is a test request form. It has fields like "TEST NUMBER: PD00237", "REQUESTED BY: WILSON, JOHN (5979)", "CLASSIFICATION: WINS KS", "TEST PURPOSE: CONSUMER SATISFACTION PROGRAM". It has sections for "SPECIAL INSTRUCTIONS", "TOBACCO PROCESSING", "FILTER MAKING", "MAKING & PACKING", "TESTING". This is clearly a form used to request and specify a test. It captures factual data and instructions in a structured layout with field labels.
Therefore, it is a form (check 10).
> Let's double check Check 8 (specification). "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes... 'shall/must' requirement language." This page has "PREPARE FILTERS AS DESCRIBED USING CURRENT WIN. KS CONFIGURATION AND SPECS." but it's not a specification document itself; it's a test request form that references specs. The primary structure is a form with fields.
> Let's double check Check 11 (memo). "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". This page has "DATE . FRI, MAR 1, 1985, 8:21 AM" but no TO:/FROM:/RE: block. It's a form.
> So the label is `form`.
> Wait, could it be a scientific_report? "Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report." This page is exactly labeled field-value entries and structured instructions. So it's a form.
> Final check of the scratchpad steps:
1. file_folder: no, has body content.
2. handwritten: no, typed.
3. fax: no, not a fax cover sheet.
4. questionnaire: no, not a survey.
5. resume: no.
6. scientific_publication: no.
7. financial: no.
8. specification: no, it's a test request form, not a product specification or analysis table.
9. presentation: no.
10. form: yes, filled fields, boxes, ruled lines (implied by the layout), capturing test request data and instructions. "TEST NUMBER", "REQUESTED BY", "CLASSIFICATION", etc.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no, no running prose.
14. advertisement: no.
> Runner-up: specification, ruled out because the page is a test request form with labeled fields and filled data, not a product specification document or analysis table. Or runner-up: scientific_report, ruled out because it lacks running narrative prose and is structured as a filled form. I'll use scientific_report as the runner-up since the content is technical (tobacco processing, filter making, testing).
> Let's refine the runner-up: scientific_report, ruled out because the page consists of labeled field-value entries and structured instructions rather than running narrative prose with objectives, methods, results, or discussion.
> Actually, the instructions say: "add one final line naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out."
Runner-up: scientific_report, ruled out because the page is a structured form with labeled fields (TEST NUMBER, REQUESTED BY, etc.) and lacks running narrative prose.
> Let's write the scratchpad.
file_folder: no — the page has extensive body content (test details, instructions), not just an identifier or stamp.
handwritten: no — the content is entirely typed (dot-matrix print), not freeform handwriting.
fax: no — lacks a "FACSIMILE" or "FAX COVER SHEET" header with To/From/phone fields; the date/time is a machine stamp, not a fax cover sheet.
questionnaire: no — does not ask the reader to answer, rate, or choose; it is a test request/instruction sheet.
resume: no — no career history or biographical information.
scientific_publication: no — no journal running head, volume, issue, or page range on the page.
financial: no — no line-item table of charges, budget tracking, or financial statements; "CHARGE NUMBER" is just a field label.
specification: no — although it references "SPECS" and "blend formulation", the page itself is a test request form, not a product specification, MSDS, or product-analysis table.
presentation: no — not a slide deck, cover, or statement; dense structured text.
form: yes — filled fields, labeled sections (TEST NUMBER, REQUESTED BY, CLASSIFICATION, TEST PURPOSE, SPECIAL INSTRUCTIONS, etc.) capturing test request data and instructions; a filled form recording data is a form.
correspondence: no — lacks a TO:/FROM:/RE: header block followed by prose, or an external address/salutation/closing.
news_article: no — no masthead, byline, or multi-column news typography.
scientific_report: no — lacks running narrative prose with objectives, methods, results, or discussion; it is structured as labeled field-value entries.
advertisement: no — no marketing layout, product imagery, or slogans.
> Runner-up: scientific_report, ruled out because the page consists of labeled field-value entries and structured instructions rather than running narrative prose.

---

## news_article → advertisement (2 errors)

### `rvl_cdip__news_article__0018.png`
**Expected:** `news_article` | **Predicted:** `advertisement`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> Pre-scan:
- Mail-client header block: None.
- Fax transmission header: "JUN 24 '94 10:53AM PHILIP MORRIS P. 6/9". This is a fax transmission header, not a mail-client header.
- Masthead/running head: No newspaper/magazine masthead. No journal running head.
> Check 1: file_folder
- Evidence: The page has a lot of text, a title "HOW SCIENCE AND POLITICS COLLIDED AND BALANCED REPORTING WAS THE CASUALTY.", and a footer "IN ANY CONTROVERSY, FACTS MUST MATTER." with a logo. Not file_folder.
> Check 2: handwritten
- Evidence: Mostly typed text. Not handwritten.
> Check 3: FAX TRANSMISSION SHEET
- Evidence: No fax cover sheet. The top has a fax transmission header, but that's just metadata. Not a fax transmission sheet.
> Check 4: questionnaire
- Evidence: No survey instrument. Not questionnaire.
> Check 5: resume
- Evidence: No career history. Not resume.
> Check 6: scientific_publication
- Evidence: No journal name/volume/issue/page number on the page itself. Not scientific_publication.
> Check 7: financial_document (invoice/budget)
- Evidence: No financial table or ledger. Not financial.
> Check 8: specification
- Evidence: No material safety data sheet, product formulation, etc. Not specification.
> Check 9: presentation
- Evidence: The page has a title, some text, but it looks like a newspaper clipping or a magazine article. Wait, let's look closer. It has a title "HOW SCIENCE AND POLITICS COLLIDED AND BALANCED REPORTING WAS THE CASUALTY." Then bullet points. Then a cut-out article or newspaper clipping image in the middle. Then text at the bottom. It looks like a news article or an advertisement. Let's check check 12 and 14.
> Check 10: administrative_form
- Evidence: No form fields. Not form.
> Check 11: correspondence (email, memo, letter)
- Evidence: No TO/FROM/RE header, no letterhead with external address, no salutation. Not correspondence.
> Check 12: news_article
- Evidence: The page has a title "HOW SCIENCE AND POLITICS COLLIDED AND BALANCED REPORTING WAS THE CASUALTY." It has text that looks like an article. There is a cut-out of a newspaper article in the middle. The bottom text says "published day one, serious questions have been raised about the validity of the EPA's 1992 report...". It mentions "Philip Morris is bringing you this article in its entirety at a four-page spread." This looks like a press release or an advertisement disguised as an article, or a news article. Wait, the bottom says "For a free reprint of this article, or more information, please call 1 800 823-5255." and "IN ANY CONTROVERSY, FACTS MUST MATTER." with a logo (Philip Morris). This is an advertisement or a promotional piece. Let's check check 14.
> Check 13: scientific_report
- Evidence: No running narrative prose of a lab/technical study. Not scientific_report.
> Check 14: advertisement
- Evidence: "Philip Morris is bringing you this article in its entirety at a four-page spread." "For a free reprint of this article, or more information, please call 1 800 823-5255." "IN ANY CONTROVERSY, FACTS MUST MATTER." with the Philip Morris logo. This is a promotional material / advertisement. It's an ad placed in a newspaper/magazine, or a standalone ad. The dominant content is promotional (Philip Morris bringing an article, call for a free reprint, slogan "In any controversy, facts must matter"). Wait, is it an advertisement or a news_article?
Check 12 says: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement (product imagery, slogans, a Surgeon General warning, brand styling) is an advertisement (check 14) even when printed inside a newspaper/magazine with a running masthead and some surrounding text; news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
Check 14 says: "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures. Judge by DOMINANT content (see check 12): a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page with a running masthead and some surrounding text."
> The page has the Philip Morris logo, the slogan "IN ANY CONTROVERSY, FACTS MUST MATTER.", and text saying "Philip Morris is bringing you this article... For a free reprint... please call...". This is clearly an advertisement / promotional material by Philip Morris. It's an ad that uses an article format (often called "advertorial" or "public relations" ad). So it's an advertisement.
> Let's re-evaluate check 12 vs 14.
The page contains an article "How Science and Politics Collided...", but the bottom text is clearly an ad from Philip Morris: "Philip Morris is bringing you this article in its entirety at a four-page spread. For a free reprint of this article, or more information, please call 1 800 823-5255." and the logo with "IN ANY CONTROVERSY, FACTS MUST MATTER."
This is a promotional layout. It's an advertisement.
> Let's check the pre-scan again.
"JUN 24 '94 10:53AM PHILIP MORRIS P. 6/9" -> Fax header.
Title: "HOW SCIENCE AND POLITICS COLLIDED AND BALANCED REPORTING WAS THE CASUALTY."
Text: "The press confidently played up the EPA's side of the story..."
Middle: A scanned newspaper clipping.
Bottom text: "published day one, serious questions have been raised... Philip Morris is bringing you this article in its entirety at a four-page spread. Since the EPA's report has been the basis for a flurry of smoking restrictions, we believe it's important for both smokers and non-smokers to learn these facts in order to make up their own minds. A fair tell, press points show that most Americans prefer documentation and accurate coverage to more sweeping regulations and outright bans. For a free reprint of this article, or more information, please call 1 800 823-5255."
Logo: Philip Morris logo.
Slogan: "IN ANY CONTROVERSY, FACTS MUST MATTER."
> This is definitely an advertisement (check 14). It's a promotional piece by Philip Morris.
> Let's double check check 12: "news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout." This page is one promotional layout (an ad reprinting an article). So it's advertisement.
> Let's review the scratchpad steps:
1. file_folder: no — page has a title, article text, and promotional footer.
2. handwritten: no — typed text.
3. FAX TRANSMISSION SHEET: no — fax header is metadata, not a cover sheet.
4. questionnaire: no — no survey.
5. resume: no — no career history.
6. scientific_publication: no — no journal identifier.
7. financial_document: no — no financial data.
8. specification: no — no product specs.
9. presentation: no — not a slide deck or cover.
10. administrative_form: no — no form fields.
11. correspondence: no — no memo/letter structure.
12. news_article: no — although it contains an article, the dominant content is a promotional layout by Philip Morris ("Philip Morris is bringing you this article...", "For a free reprint... please call...", slogan "IN ANY CONTROVERSY, FACTS MUST MATTER.").
13. scientific_report: no — not a research write-up.
14. advertisement: yes — promotional layout by Philip Morris, slogan, call to action for a free reprint, brand logo.
> Runner-up: news_article, ruled out because the page is a promotional layout by Philip Morris offering a free reprint and featuring their slogan, not primarily editorial news content.
> Final label: advertisement.

---
### `rvl_cdip__news_article__0020.png`
**Expected:** `news_article` | **Predicted:** `advertisement`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I need to follow a specific scratchpad procedure, checking 1-14 in order.
> **Document Analysis:**
- Top header: "THE NEW YORK TIMES, MONDAY SEPTEMBER 15, 1986" (faintly visible at the top). Wait, let's look closer. "THE NEW YORK TIMES, MONDAY SEPTEMBER 15, 1986" is at the very top.
- Main headline: "All Advertising Should Be Truthful"
- There's a box: "Reprinted with permission from November 10, 1969, Advertising Age, The National Newspaper of Marketing..."
- Inside a jagged border: "The Truth Seems a Little Twisted" with text below it.
- Bottom section: "What is Advertising Age? - The national newspaper of the advertising and marketing industry - A constant champion of truth in advertising - Not a defender of smoking"
- Bottom left: "the tobacco institute 1776 K Street, N.W., Washington, D.C. 20006"
- Bottom right: Bates number "901216053"
> **Pre-scan:**
- Mail-client header: None.
- Masthead/running head: "THE NEW YORK TIMES, MONDAY SEPTEMBER 15, 1986" is at the top. This is a newspaper masthead. Wait, is it a newspaper page or an advertisement inside a newspaper?
- Let's look at the content. It's an ad by "the tobacco institute" promoting "Advertising Age". It says "Reprinted with permission from November 10, 1969, Advertising Age".
- The dominant content is a single brand ad (Tobacco Institute) promoting Advertising Age. Wait, is it an advertisement or a news article?
- Check 12: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement (product imagery, slogans, a Surgeon General warning, brand styling) is an advertisement (check 14) even when printed inside a newspaper/magazine with a running masthead and some surrounding text; news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
- This page is clearly an advertisement by the Tobacco Institute. It has the Tobacco Institute logo and address at the bottom. It's promoting Advertising Age. The text "All Advertising Should Be Truthful" is the ad headline.
- Let's check check 14: "PROMOTIONAL MATERIAL -> advertisement. Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures. Judge by DOMINANT content (see check 12): a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page with a running masthead and some surrounding text."
> Let's trace the checks:
1. file_folder: No, has lots of text.
2. handwritten: No.
3. fax: No.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No.
7. invoice/budget: No.
8. specification: No.
9. presentation: No.
10. form: No.
11. correspondence: No.
12. news_article: Has a newspaper masthead ("THE NEW YORK TIMES"), but the dominant content is a single brand advertisement (Tobacco Institute ad for Advertising Age). Check 12 says news_article requires primarily editorial/multi-story news content. This is one promotional layout. So not news_article.
13. scientific_report: No.
14. advertisement: Yes. "the tobacco institute" with address, slogan "All Advertising Should Be Truthful", promoting Advertising Age. It's an ad.
> Wait, is it an advertisement?
"the tobacco institute 1776 K Street, N.W., Washington, D.C. 20006"
Yes, it's an advertisement placed by the Tobacco Institute in The New York Times.
> Let's re-read check 12 and 14 carefully.
Check 12: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement ... is an advertisement (check 14) even when printed inside a newspaper/magazine with a running masthead ... news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
Check 14: "PROMOTIONAL MATERIAL -> advertisement. Marketing layout: ... Judge by DOMINANT content (see check 12): a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page with a running masthead and some surrounding text."
> The page has:
- Masthead: "THE NEW YORK TIMES, MONDAY SEPTEMBER 15, 1986"
- Headline: "All Advertising Should Be Truthful"
- Text reprinted from Advertising Age.
- Bottom: "the tobacco institute" with address.
This is an advertisement.
> Let's do the scratchpad.
> Check 1: file_folder. No, has body content.
Check 2: handwritten. No.
Check 3: fax. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial. No.
Check 8: specification. No.
Check 9: presentation. No.
Check 10: form. No.
Check 11: correspondence. No.
Check 12: news_article. Has "THE NEW YORK TIMES" masthead at the top, but the dominant content is a single promotional layout by "the tobacco institute" (advertisement). Ruled out by check 12's caveat about single brand ads inside newspapers.
Check 13: scientific_report. No.
Check 14: advertisement. Yes. "the tobacco institute" at the bottom, slogan "All Advertising Should Be Truthful", reprinted text from Advertising Age promoting it. This is a promotional layout/advertisement.
> Runner-up: news_article. Ruled out because although there is a newspaper masthead ("THE NEW YORK TIMES"), the dominant content is a single brand advertisement by the Tobacco Institute promoting Advertising Age, not editorial/multi-story news content.
> Final label: advertisement.

---

## presentation → file_folder (2 errors)

### `rvl_cdip__presentation__0017.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned document from a tobacco-industry archive.
I need to follow the scratchpad procedure, checking 1-14 in order.
> Image analysis:
The image is mostly blank white space.
There is a faint, noisy, vertical band on the left side, which looks like scan noise or a very faint, degraded image/text, but it's mostly illegible noise.
There is a number "2071969205" rotated 90 degrees in the bottom right corner.
There is a small black mark "F" or similar in the top right corner.
Let's look closely at the left side. It's a vertical band of noise. It doesn't look like a clear photograph, slide, or text. It looks like scan noise or a very faint artifact.
Wait, let's re-read the rules for `file_folder`.
"Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."
"A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image (people, a scene, a slide) or with a bold headline title... carries real content"
"A page whose content is a physical folder tab, a short filing label (product/collection/month/file name), and a Bates number is file_folder even though the folder body photographs as a solid black bar and the label may be rotated."
> Let's look at the left side again. Is it a folder tab?
The left side has a vertical band of noise, and at the bottom, there's a darker rectangular area. This looks like the edge of a folder or a scanned artifact.
The number "2071969205" is a Bates number.
There is no bold headline title. No sentences. No topical title.
The left side is just noise/faint artifact, not a clear photograph or slide.
Wait, is there a solid black bar? The bottom left has a darker block, but it's mostly noise.
Let's consider `file_folder`. The page has almost no body content. Only a Bates number (2071969205) and some scan noise/artifacts on the left.
Is it a folder tab? The left side could be a photographed folder tab, but it's very degraded. Even if it's just a Bates number and noise, it fits "Almost no body content: only an archive/Bates number...".
Let's check `presentation`: "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder". But this isn't a clear photographic image. It's mostly blank with noise.
Let's check `file_folder` again: "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content". Here, there is no bold headline title, and the left side is just noise/faint artifact, not a clear photographic image.
So `file_folder` is the best fit.
> Let's do the scratchpad checks:
1. file_folder: Almost no body content. Only a Bates number "2071969205" and some scan noise/artifacts on the left edge. No sentences, no topical title. Matches file_folder.
2. handwritten: none.
3. fax: none.
4. questionnaire: none.
5. resume: none.
6. scientific_publication: none.
7. financial: none.
8. specification: none.
9. presentation: no clear photographic slide, just noise.
10. form: none.
11. correspondence: none.
12. news_article: none.
13. scientific_report: none.
14. advertisement: none.
> Wait, is the left side a folder tab? "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body." The left side is very degraded, but it could be a folder tab. Even if it's not a clear folder tab, the page is essentially blank except for a Bates number and scan noise. The rule says: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only." Since the left side is just noise and not a clear photograph or slide, it's pure filing metadata (Bates number). Thus, file_folder.
> Let's double check the left side. It looks like a vertical strip of static/noise, maybe a very faint text or image that is completely illegible. At the bottom, there's a darker rectangular block. This is typical of a scanned folder tab or edge where the scanner picked up the edge of the folder. The Bates number is clearly visible.
Therefore, file_folder is the correct classification.
> Scratchpad:
file_folder: yes — almost no body content; only a Bates number "2071969205" and faint scan noise/artifacts on the left edge (no clear photograph, slide, or bold headline title).
handwritten: not this check.
fax: not this check.
questionnaire: not this check.
resume: not this check.
scientific_publication: not this check.
financial: not this check.
specification: not this check.
presentation: not this check — no clear photographic slide or designed deck page, just scan noise and a Bates number.
form: not this check.
correspondence: not this check.
news_article: not this check.
scientific_report: not this check.
advertisement: not this check.
Runner-up: presentation, ruled out because the left edge is illegible scan noise rather than a clear photographic slide or designed deck page.
> Final label: file_folder.

---
### `rvl_cdip__presentation__0018.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. Just a Bates number "465246617" and some handwritten text "1991-84 foundation" rotated on the right side. A solid black bar on the right edge.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page is almost entirely blank. It has a Bates number "465246617" at the bottom. It has handwritten text "1991-84 foundation" rotated on the right side. There is a solid black bar on the right edge.
- Wait, is this a folder tab? The solid black bar on the right edge looks like the edge of a photographed folder body. The handwritten text "1991-84 foundation" is a short filing label.
- Let's re-read the folder-tab bullet: "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB — a protruding tab-shaped piece of cardboard (often with a cutout/notch shape at the folder's edge) bearing a short filing label that names the folder's contents... usually with a Bates number stamped on the folder body. The label IS filing metadata... The black bar is the photographed folder body/tab edge — it is NOT a slide-mount scan artifact (check 9), and a rotated filing label on a folder tab is NOT a section-divider heading."
- The page has a solid black bar on the right edge. The text "1991-84 foundation" is rotated 90 degrees. This perfectly matches the description of a folder-tab page. The label is "1991-84 foundation". The black bar is the folder body. The Bates number is "465246617".
- Therefore, this is a file_folder page.
> Let's double check check 9 (presentation).
- "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation... BUT this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label (product/collection/month/file name), and a Bates number is file_folder even though the folder body photographs as a black bar."
- The text "1991-84 foundation" is a short filing label naming a date range/collection. It is rotated. This is a folder tab.
> So Check 1 matches.
> Let's write the scratchpad.
- file_folder: yes — the page is almost entirely blank, containing only a Bates number ("465246617"), a solid black bar along the right edge (photographed folder body), and a short rotated handwritten label ("1991-84 foundation") which serves as a filing label for the folder's contents. This matches the folder-tab exception in check 1.
- presentation: no — although there is a solid black bar and sparse rotated text, the text is a short filing label ("1991-84 foundation") on what is clearly a photographed folder tab, not a designed slide or photographic slide image. Check 1's folder-tab rule overrides check 9's scan-artifact signal.
- handwritten: no — the handwriting is just a short filing label on a folder tab, not the majority of the page's content.
> Final label: file_folder.

---

## scientific_publication → news_article (2 errors)

### `rvl_cdip__scientific_publication__0006.png`
**Expected:** `scientific_publication` | **Predicted:** `news_article`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead or running head: Top of the page has "New Scientist 17 June 1982" and "M O N I T O R". This looks like a newspaper/magazine masthead or a section of a magazine. "New Scientist" is a science magazine. "MONITOR" is likely the section name. Multi-column news typography. This points towards check 12 (news_article) or check 6 (scientific_publication). Wait, "New Scientist" is a general-audience magazine (science news). Let's check check 6 and 12.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has dense text, multiple columns, a headline "All routes are leading to the same few cancer genes". Not file_folder.
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Typed text throughout.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No fax header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No resume content.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: "New Scientist 17 June 1982". New Scientist is a magazine, not a research journal. The text cites "Nature", "Science", "Proceedings of the National Academy of Sciences", but these are citations within the text. The page itself has a magazine masthead/section header "MONITOR" from "New Scientist". Check 6 says: "Caveat — general news outlets: a page that presents itself as a newspaper, general-magazine, or encyclopedia piece... is news_article (check 12), not a publication". New Scientist is a general-audience magazine (science news). So this is not scientific_publication.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial content.
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No product specs.
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: No form fields.
- Not this check.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: No correspondence structure.
- Not this check.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: "New Scientist 17 June 1982" at the top, "M O N I T O R" as a section header. Multi-column typography. Headline "All routes are leading to the same few cancer genes". Subheadings "Carcinogens act on irritated tissues". This is a magazine article/feature from New Scientist. New Scientist is a general-audience magazine (even if science-focused, it's a news/magazine outlet, not a peer-reviewed research journal like Nature or Science, though it cites them). The text says "New Scientist 17 June 1982". This is a magazine page. Check 12: "Newspaper or magazine masthead, byline, dateline, multi-column news typography... Also a magazine feature... from a GENERAL-AUDIENCE outlet". New Scientist fits this.
- Yes, this is news_article.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: The text is a summary of research, but it's published in New Scientist, a magazine. Check 12 takes precedence because it's published journalism from a general-audience outlet (magazine). Wait, check 6 caveat: "a page that presents itself as a newspaper, general-magazine, or encyclopedia piece... is news_article (check 12), not a publication". New Scientist is a magazine. So it's news_article.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: Not an ad.
> Let's double check New Scientist. Is it a scientific publication or a news article?
Check 6: "Caveat — general news outlets: a page that presents itself as a newspaper, general-magazine, or encyclopedia piece — multi-column published editorial prose with a masthead, magazine cover, or encyclopedia/reference title belonging to a general-audience outlet — is news_article (check 12), not a publication, even if its text is scientific, names an author with credentials, or cites journal articles as references within the prose".
New Scientist is a weekly magazine covering science and technology. It is a general-audience outlet (popular science magazine). The page has "New Scientist 17 June 1982" and "MONITOR". This is a magazine section. The typography is multi-column. The content is editorial prose about cancer genes. This fits news_article perfectly.
> Let's review the evidence for Check 12:
- Masthead/running head: "New Scientist 17 June 1982"
- Section title: "M O N I T O R"
- Headline: "All routes are leading to the same few cancer genes"
- Multi-column typography (3 columns).
- Subheadings: "Carcinogens act on irritated tissues"
- This is a magazine article.
> Therefore, the label is news_article.
> Runner-up: scientific_publication. Ruled out because "New Scientist" is a general-audience magazine (popular science), not a peer-reviewed research journal, and the page carries a magazine masthead/section header rather than a journal volume/issue/page number belonging to a research journal. The citations to Nature/Science are within the text.
> Let's confirm the exact label: news_article.
Check 12: "PUBLISHED JOURNALISM -> news_article"
String: "news_article"
> Final check of the scratchpad steps:
1. file_folder: no - has body content.
2. handwritten: no - typed.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no - New Scientist is a magazine, not a research journal with its own volume/issue/page number on this page (it has date and section name). The caveat in check 6 explicitly routes magazine content to check 12.
7. financial: no.
8. specification: no.
9. presentation: no.
10. form: no.
11. correspondence: no.
12. news_article: yes - "New Scientist 17 June 1982" masthead, "MONITOR" section header, multi-column layout, headline "All routes are leading to the same few cancer genes".
13. scientific_report: no - it's a published magazine article.
14. advertisement: no.
> The label is news_article.

---
### `rvl_cdip__scientific_publication__0016.png`
**Expected:** `scientific_publication` | **Predicted:** `news_article`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead or running head: Top right says "HOSPITAL-TRAINEE", "Monday, February 2, 1971". Top left says "16". This looks like a newspaper or magazine page. "HOSPITAL-TRAINEE" is a publication name. Let's look closer. "Theory of Emphysema Cause Raises Questions" is a headline. "Surgeon General" is a subhead. "Clinic at U. of Va. Offers Health Care to Families" is another headline. "Antitrypsin Lack Might Increase Fertility" is another. This is clearly a newspaper or magazine page. "HOSPITAL-TRAINEE" is likely a newspaper or newsletter. Let's check check 12.
> **Check 1: file_folder**
- Evidence: No, it has lots of text, headlines, articles.
- Not this check.
> **Check 2: handwritten**
- Evidence: No, it's typed text.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax header.
- Not this check.
> **Check 4: questionnaire**
- Evidence: No survey questions.
- Not this check.
> **Check 5: resume**
- Evidence: No CV/resume.
- Not this check.
> **Check 6: scientific_publication**
- Evidence: "HOSPITAL-TRAINEE" is a publication, but is it a research journal? "HOSPITAL-TRAINEE" sounds like a newspaper or magazine for hospital trainees. Let's check check 12. If it's a general-audience outlet or a specific trade publication, it might be news_article. Wait, "HOSPITAL-TRAINEE" is a newspaper/magazine. Let's look at the content. It's news articles about medical topics. "Theory of Emphysema Cause Raises Questions", "Clinic at U. of Va...", "Antitrypsin Lack Might Increase Fertility". These are news articles.
- Let's check check 12 first.
> **Check 7: financial document**
- Evidence: No financial tables.
- Not this check.
> **Check 8: specification**
- Evidence: No.
- Not this check.
> **Check 9: presentation**
- Evidence: No.
- Not this check.
> **Check 10: form**
- Evidence: No.
- Not this check.
> **Check 11: correspondence**
- Evidence: No.
- Not this check.
> **Check 12: news_article**
- Evidence: Masthead "HOSPITAL-TRAINEE", date "Monday, February 2, 1971", page number "16". Multi-column news typography. Headlines: "Theory of Emphysema Cause Raises Questions", "Clinic at U. of Va. Offers Health Care to Families", "Antitrypsin Lack Might Increase Fertility". Bylines/datelines: "Hospital Tribune—World Wide Report", "Surgeon General". This is clearly a newspaper or magazine page (editorial content from a general or trade outlet). "HOSPITAL-TRAINEE" is a publication. The content is news articles.
- This matches check 12 perfectly.
> **Check 13: scientific_report**
- Evidence: No, it's a newspaper/magazine page.
> **Check 14: advertisement**
- Evidence: No, it's editorial content.
> Let's double check check 6 vs 12.
Check 6: "First, use your pre-scan finding: does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings?"
"HOSPITAL-TRAINEE" is not a research journal. It's a newspaper/magazine for hospital trainees (likely a trade publication or internal newsletter, but formatted like a newspaper).
Check 12: "Newspaper or magazine masthead, byline, dateline, multi-column news typography... Also a magazine feature or an encyclopedia entry... any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet — even when the topic is scientific... Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content".
The page has multiple headlines, multi-column layout, masthead "HOSPITAL-TRAINEE", date "Monday, February 2, 1971". This is a news_article.
> Let's review the pre-scan for masthead: "HOSPITAL-TRAINEE", "Monday, February 2, 1971", "16". This is a newspaper/magazine masthead.
> Therefore, the label is news_article.
> Scratchpad:
file_folder: no — page has multiple articles, headlines, and running text.
handwritten: no — typed text throughout.
questionnaire: no — no survey items.
resume: no — no career history.
scientific_publication: no — "HOSPITAL-TRAINEE" is a newspaper/magazine masthead, not a research journal with volume/issue/page range/DOI.
invoice/budget: no — no financial data.
specification: no — no product data.
presentation: no — not a slide deck.
form: no — no fields/boxes.
email/memo/letter: no — no correspondence headers.
news_article: yes — masthead "HOSPITAL-TRAINEE", date "Monday, February 2, 1971", page "16", multi-column layout with headlines like "Theory of Emphysema Cause Raises Questions", "Clinic at U. of Va. Offers Health Care to Families", "Antitrypsin Lack Might Increase Fertility", and subheads like "Hospital Tribune—World Wide Report". This is published periodical editorial content.
advertisement: no — dominant content is editorial news, not a single brand ad.
> Runner-up: scientific_report, ruled out because the page carries a newspaper/magazine masthead ("HOSPITAL-TRAINEE") and multi-column news typography with multiple headlines, indicating it is a news article from a periodical, not an original research write-up.
> Final label: news_article.

---

## invoice → budget (1 errors)

### `rvl_cdip__invoice__0017.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "93219883" and some text from "LOEWS CLEARING CORPORATION" and "THE CHASE MANHATTAN BANK N.A.".
> **Check 1: file_folder**
- Evidence: The page has a lot of content, it's a check. Not just an identifier.
- Not this check.
> **Check 2: handwritten**
- Evidence: Mostly typed, some handwritten-looking text but it's a check (MICR line, typed payee). Not majority handwritten.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey questions.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: No resume content.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal masthead.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: This is a check. "LOEWS CLEARING CORPORATION", "THE CHASE MANHATTAN BANK N.A.", "No 4506", "AMOUNT 131,416.00", "PAY TO THE ORDER OF THE SUM OF 131,416.00", "3-15-82 COUNCIL FOR TOBACCO RESEARCH-U S A INC".
- A check face/check stub is budget (under check 7). "A check face/check stub — a check number, bank, MICR line, "PAY TO THE ORDER OF", signature line, or detachable stub — is the DISBURSEMENT instrument and stays budget (below), even when the stub's columns are headed "INVOICE DATE"/"INVOICE NO."/"INVOICE AMOUNT"."
- Let's verify the text: "LOEWS CLEARING CORPORATION", "LOCK BOX 456 FIFTH AVENUE NEW YORK, N.Y. 10019", "THE CHASE MANHATTAN BANK N.A.", "No 4506", "AMOUNT 131,416.00", "PAY TO THE ORDER OF THE SUM OF 131,416.00", "3-15-82 COUNCIL FOR TOBACCO RESEARCH-U S A INC". There is a MICR line at the bottom: "0004506* 021000021* 036* 2-4000 20*".
- This is clearly a check face.
- Under check 7: "budget: ... a check face or check stub ... is budget".
- So this is budget.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
- Not this check.
> **Check 10: ADMINISTRATIVE FORM**
- Not this check.
> **Check 11: CORRESPONDENCE**
- Not this check.
> **Check 12: PUBLISHED JOURNALISM**
- Not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP**
- Not this check.
> **Check 14: PROMOTIONAL MATERIAL**
- Not this check.
> Final classification: budget.
> Let's double check check 7 rules.
"budget: internal money planning, tracking, or disbursement ... a check face or check stub ... is budget"
"invoice: ... A check face/check stub ... is the DISBURSEMENT instrument and stays budget (below)"
Yes, a check is budget.
> The document is a check from Loews Clearing Corporation / The Chase Manhattan Bank N.A., number 4506, dated 3-15-82, payable to Council for Tobacco Research-U S A Inc, amount 131,416.00.
This is a check face.
Label: budget.

---

## budget → scientific_report (1 errors)

### `rvl_cdip__budget__0007.png`
**Expected:** `budget` | **Predicted:** `scientific_report`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** None. There is a "RECEIVED" stamp, but no From/To/Sent/Subject.
- **Masthead/Running head:** Top has "Tobacco Institute" logo and "cigarette tax data" with address. This looks like a letterhead or report header, not a newspaper/magazine masthead or journal running head. Bottom has "THILBC 005161" (Bates number).
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a title "Monthly State Cigarette Tax Report", paragraphs of text, a note, and a Bates number. It has real content.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: The text is typed. There is a "RECEIVED" stamp and a handwritten date/number "20 19c" (looks like a stamp or handwritten note, maybe "20 19c" or similar, actually looks like "RECEIVED ... 20 19c" stamp). Wait, "RECEIVED ... 20 19c" is a stamp. The main text is typed.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No questions, no survey instrument.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No biographical info.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal name, volume, issue, page range on the page itself. "Tobacco Institute" is an organization, not a journal.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: The page is a "Monthly State Cigarette Tax Report". It discusses tax collections, package counts, percentages.
    *   Is it an invoice? No, it's a report *about* tax data. It doesn't bill anyone.
    *   Is it a budget? It reports on tax collections and volume. "Sales tax collections... amounted to approximately $93.2 million". This is a report of financial data, but is it a budget or invoice?
    *   Let's look at the definitions.
    *   Invoice: outside vendor states charges owed. No.
    *   Budget: internal money planning, tracking, or disbursement... financial or money-data table... statement of account.
    *   Wait, is this a scientific_report?
    *   Let's check Check 13.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: No material safety data, no product formulation.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: Not a slide deck. Not a press release ("FOR IMMEDIATE RELEASE").
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: No fields, boxes, checkboxes. It's a narrative report.
    *   Result: not this check.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: No TO:/FROM:/RE: header. No "Dear ...". No external address. It's a report.
    *   Result: not this check.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: No newspaper/magazine masthead. "Tobacco Institute" is the publisher/author.
    *   Result: not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: "Monthly State Cigarette Tax Report". "Report for February 1989".
    *   Text: "In February 1989, cigarette taxes in the 50 states... were imposed on 1,794,409,000 packages."
    *   "Cumulative figures on the volume of cigarettes taxed..."
    *   "The aggregate of the cigarette taxes..."
    *   "Sales tax collections..."
    *   "Note: This reports tax collections only..."
    *   This is a report. Is it a scientific report?
    *   Definition: "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page... Requires running prose".
    *   This page has running narrative prose reporting on tax data. It's a technical report from the Tobacco Institute.
    *   Wait, is there a better category?
    *   Let's re-evaluate Check 7 (Financial Document).
    *   "financial or money-data table (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures), and a handwritten list of budget categories and dollar amounts... ALSO a provider's periodic customer statement... is budget".
    *   This is a "Monthly State Cigarette Tax Report". It's a report of data.
    *   Is it a scientific_report? "A technical/project status report whose content is primarily technical... is scientific_report". This is a report on tax data. It's narrative prose.
    *   Let's look at the labels again.
    *   advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
    *   The document is a report from the Tobacco Institute. "cigarette tax data".
    *   It contains narrative prose describing statistics.
    *   "In February 1989... This was a decrease... When the February 1989 package count was compared... Cumulative figures... The aggregate... Sales tax collections..."
    *   This looks like a scientific_report (technical report). The Tobacco Institute produced reports.
    *   Let's check if it fits "budget". Budget is "internal money planning, tracking... financial or money-data table". This is a report *about* tax data, not an internal budget document or a bill. It's a published report (internal or external) from the institute.
    *   Actually, let's look at the "scientific_report" definition again. "Running narrative prose with objectives, methods, results, or discussion". This has results (tax collections, package counts). It's a report.
    *   Is there a "report" category? No. "scientific_report" is the closest for a technical report.
    *   Wait, is it a "form"? No.
    *   Is it a "memo"? No header.
    *   Is it a "letter"? No.
> Let's reconsider the content. It's a "Monthly State Cigarette Tax Report".
It's a narrative summary of tax data.
It fits "scientific_report" best among the options, as it's a technical report with narrative prose presenting data/results. The Tobacco Institute is a research/advocacy organization. This looks like a technical report or data summary.
> Let's check the labels again.
16 categories.
- scientific_report: "Running narrative prose with objectives, methods, results, or discussion... a lab or technical study title page... Requires running prose".
This page has running prose. It reports on cigarette tax data. It's a technical report.
> Let's look for any other fit.
- budget: "financial or money-data table". This is text, not a table. "statement of account". No.
- invoice: No.
> So it's likely scientific_report.
> Wait, is it a "presentation"?
"Technical-study title pages... is scientific_report".
This is a report page. "Report for February 1989".
It's a page from a report.
> Let's look at the header: "Tobacco Institute", "cigarette tax data", address.
This is a letterhead for a report.
The content is narrative prose.
"Report for February 1989"
"In February 1989, cigarette taxes..."
This is a technical report.
> Let's check if it could be a "form". No.
"file_folder"? No.
> So, scientific_report.
> Wait, is there any chance it's a "news_article"?
"Tobacco Institute" is not a news outlet. It's an organization.
The text is a report.
> Let's refine the scientific_report classification.
"Original research write-up -> scientific_report"
"Running narrative prose with objectives, methods, results, or discussion"
This page has results ("Sales tax collections... amounted to approximately $93.2 million").
It's a report. In this archive (tobacco industry), these monthly reports are often classified as scientific_reports or just reports. Since "report" isn't a label, "scientific_report" is the bucket for technical reports with narrative prose.
> Let's double check Check 7 (Financial).
"financial or money-data table... is budget".
This is not a table. It's prose.
"money-only records... is budget".
This is not money-only records, it's a report on tax data (packages, percentages, dollars).
"provider's periodic customer statement... is budget".
This is not a statement from a provider to a customer. It's a report *by* the Tobacco Institute *about* tax data.
> So scientific_report seems correct.
> Let's look at the "RECEIVED" stamp. "RECEIVED ... 20 19c". Maybe a date stamp? "20 19c" -> maybe 1990? "RECEIVED 20 [month] 1990"? Doesn't matter.
> Final check:
- file_folder: No, has content.
- handwritten: No, typed.
- fax: No.
- questionnaire: No.
- resume: No.
- scientific_publication: No journal ID.
- invoice/budget: No, it's a report of data, not a bill or internal budget plan. Although it contains money figures, the primary structure is a narrative report. Wait.
Check 7: "If the page is otherwise formatted as correspondence... and a dollar figure... is mentioned... classify as correspondence".
Check 7: "financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face."
This page is a narrative report. The financial content is in the prose.
So Check 7 doesn't apply strongly to make it invoice/budget.
Check 13: "Running narrative prose with objectives, methods, results, or discussion".
This page has results. It is a report.
So scientific_report.
> One detail: "A technical/project status report whose content is primarily technical... is scientific_report".
This is a monthly report on tax data. It's technical/administrative data reported in prose.
In the tobacco archive context, these "Monthly State Cigarette Tax Reports" are often internal reports or published data summaries. Given the labels, scientific_report is the best fit for a narrative report that isn't a letter/memo/form.
> Wait, is it a "memo"?
No TO/FROM/RE header.
> Is it a "letter"?
No salutation/closing.
> So scientific_report.
> Let's re-read the scientific_report definition carefully.
"Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page with authors and an internal affiliation and no journal identifiers. Requires running prose — a page that is only labeled field-value entries... is a filled form... not a scientific report."
This page has running prose. "In February 1989... This was a decrease... When the February 1989 package count was compared... Cumulative figures... The aggregate... Sales tax collections... Note: This reports tax collections only..."
This is running narrative prose presenting results/data.
It fits scientific_report.
> One counter-argument: Is it a "form"?
"A standalone labeled data chart or table... is a form".
This is not a chart or table. It's text.
> Is it a "specification"?
No.
> So, scientific_report.
> Wait, looking at the header "cigarette tax data".
This looks like a newsletter or a report series.
If it's a newsletter, is it news_article?
"Newspaper or magazine masthead... general-audience outlet".
Tobacco Institute is not a general-audience news outlet. It's an industry group.
So not news_article.
> Final decision: scientific_report.
> Wait, let's look at the "RECEIVED" stamp. "RECEIVED ... 20 19c".
Actually, it looks like "RECEIVED 20 [something] 1990" or similar.
Doesn't change the classification.
> The page is a report.
Label: scientific_report.
> One more check: Could it be a "budget"?
"financial or money-data table... is budget".
This is not a table.
"money-only records... is budget".
This is not money-only.
> Could it be an "invoice"?
No.
> So scientific_report.
> Let's check the scratchpad requirements.
Walk checks 1-14.
1. file_folder: no - has body content (report text).
2. handwritten: no - typed text.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no - no journal ID.
7. financial: no - primary structure is narrative report, not a bill/ledger/table. (Though it contains financial data, it's a report *about* it). Wait, check 7 says "financial content IS the page's primary structure". Here the primary structure is a narrative report. The financial data is the subject. But is it a "financial document"?
Check 7: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face."
This page is a narrative report. So Check 7 is "not this check".
8. specification: no.
9. presentation: no.
10. form: no.
11. correspondence: no.
12. news_article: no.
13. scientific_report: yes - running narrative prose reporting on tax data (results/data). "Monthly State Cigarette Tax Report".
14. advertisement: no.
> Runner-up: budget. Ruled out because the page is a narrative report, not a financial table/ledger/budget plan. The financial data is the subject matter, but the structure is a report (prose), not a financial form (table/ledger). Actually, check 7 says "financial content IS the page's primary structure". Here the structure is prose. So it falls to check 13.
> Wait, is there a category for "report"? No, only "scientific_report".
In this archive, technical reports from institutes are often scientific_reports.
> Final label: scientific_report.

---

## budget → form (1 errors)

### `rvl_cdip__budget__0013.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "65503 5219" and a notice at the bottom left.
> **Check 1: file_folder**
- Content: "VARIANCE SHEET", "BRONX & WILLIAMSBURG - LOUISVILLE", "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE APPLIED".
- It has a list of checkboxes and handwritten text "throughout rest of file".
- This is not just an identifier/stamp. It has real content (a variance sheet). Not file_folder.
> **Check 2: handwritten**
- Most content is typed (checkboxes, instructions). Only one line is handwritten ("throughout rest of file"). Not handwritten.
> **Check 3: FAX TRANSMISSION SHEET**
- No fax header.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Not a survey.
> **Check 5: PERSON'S CAREER HISTORY**
- Not a resume.
> **Check 6: PUBLISHED EVIDENCE**
- No journal masthead.
> **Check 7: FINANCIAL DOCUMENT**
- No financial content.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
- Not a specification.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
- Wait, look at the layout. It's a page with a black border (scan artifact or folder tab?).
- Let's re-read Check 9 caveats: "a one-page status/location display sheet — a titled sheet stating where a record range or item is located, printed in slide-style layout with a title, a line of reference numbers, and checkbox-style options (e.g. an "ARCHIVE LOCATION VARIANCE SHEET" listing "THE NUMBER (RANGE) 2060574004-2060574012 IS LOCATED: ( ) IN THE AUDIO CABINET ( ) IN THE VIDEO CABINET ( X ) ON THE OVERSIZE SHELF ...") — is a presentation (this check), not a form."
- This page is titled "VARIANCE SHEET". It's checking motivations applied during reproduction. "BRONX & WILLIAMSBURG - LOUISVILLE".
- Wait, is this a form? Let's check Check 10.
> **Check 10: ADMINISTRATIVE FORM**
- "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A QA/parameter review sheet."
- This is a "VARIANCE SHEET" with checkboxes for reproduction motivations (document copies, duplicate documents, page numbers missing, poor quality original, overlay item, no documents found, file folder, remove expandable file, manila file, envelope, other).
- It has checkboxes and a handwritten entry "throughout rest of file".
- This is a form capturing factual data (reproduction variance/motivations).
- Let's check if it fits Check 9 better. Check 9 says: "a one-page status/location display sheet... is a presentation". This is a variance sheet for reproduction, not a location display sheet.
- Is it a form? Yes, checkboxes, ruled entry lines for "OTHER (SPECIFY)". Capturing factual data about reproduction.
- Let's re-read Check 10: "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
- This is definitely a form.
> Let's double check Check 9: "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text... points to a photographed slide/overhead — presentation". The black bar here is around the whole page, looks like a scanned folder or a slide mount, but the content is a "VARIANCE SHEET".
Actually, look at the bottom left: "NOTICE If the file image is less clear than this notice, it is due to the quality of the document being filmed." and Bates number "65503 5219". This is a microfilm/fiche reproduction variance sheet.
It's a form used to document reproduction issues.
Check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A QA/parameter review sheet."
This fits perfectly. It's a variance sheet with checkboxes.
> Let's review the checks again.
Check 1: file_folder. No, has content.
Check 2: handwritten. No.
Check 3: fax. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial. No.
Check 8: specification. No.
Check 9: presentation. No, it's a variance sheet with checkboxes, not a slide deck or location display sheet.
Check 10: form. Yes, checkboxes, ruled lines, capturing data about reproduction motivations.
> Wait, is there any other check?
Check 11: correspondence. No.
Check 12: news_article. No.
Check 13: scientific_report. No.
Check 14: advertisement. No.
> So the label is "form".
> Let's refine the scratchpad.
- file_folder: no — the page contains a "VARIANCE SHEET" with a list of checkboxes and handwritten text, not just an identifier or stamp.
- handwritten: no — the page is mostly typed text with checkboxes; only one line is handwritten.
- form: yes — titled "VARIANCE SHEET", contains a list of checkboxes for reproduction motivations (e.g., "DOCUMENT COPIES ARE IN THE SAME SEQUENCE...", "FILE FOLDER", "ENVELOPE") and a ruled entry line for "OTHER (SPECIFY)" filled with handwritten text "throughout rest of file". This is a filled administrative form capturing factual data.
- Runner-up: presentation, ruled out because the page is a structured variance sheet with checkboxes and ruled lines for data capture, not a slide deck, cover, or location display sheet.
> Final check of the text:
"VARIANCE SHEET"
"BRONX & WILLIAMSBURG - LOUISVILLE"
"AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE APPLIED"
Checkboxes next to items.
Handwritten "(X) OTHER throughout rest of file".
Bates number 65503 5219.
Notice at bottom left.
> This is clearly a form.

---

## form → invoice (1 errors)

### `rvl_cdip__form__0001.png`
**Expected:** `form` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: None. There's a Bates number "77917 7 9 / 4" at the bottom, and a black bar at the bottom (scan artifact or folder edge? Wait, the bottom has a black bar with text "NOTICE IF THE FILM IMAGE IS LESS CLEAR THAN THIS NOTICE... 77917 7 9 / 4". This looks like a microfilm edge, not a slide scan artifact. Wait, the top has a black bar too. Let's look closely. Top edge has a black bar. Bottom edge has a black bar with microfilm text. This is a microfilm scan. Not a slide.)
> **Check 1: file_folder**
- Content: "Ted Bates new york/advertising", "BROWN & WILLIAMSON TOBACCO CORPORATION", "PRINT PRODUCTION ESTIMATE". It has a lot of content (fields, tables). Not file_folder.
> **Check 2: handwritten**
- Mostly typed. Some handwritten numbers ("3144", "41125", "548 + 312"). Not handwritten.
> **Check 3: FAX TRANSMISSION SHEET**
- No fax header.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Not a survey.
> **Check 5: PERSON'S CAREER HISTORY**
- Not a resume.
> **Check 6: PUBLISHED EVIDENCE**
- No journal masthead.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Title: "PRINT PRODUCTION ESTIMATE".
- Agency: "Ted Bates new york/advertising".
- Client: "BROWN & WILLIAMSON TOBACCO CORPORATION".
- Fields: BRAND, CAPTION, SUBJECT, PHOTOGRAPHER/ARTIST, REVISED DATE, EST. #, B&W CODE #, JOB #.
- Table: Cost Per Ad/Item, No. of Ads/Items, Estimated Total Cost, Actual Total Cost.
- Items: Dye Transfer, Dupp Bye Transfers, Re-Touching, Transparencies, C-Prints, Photolettering.
- Handwritten totals: "1,800 3144", "1,200", "4,000 - 41125", "600 548 + 312".
- Is this an invoice or budget?
- Check 7 says: "An agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- This document has:
  - "EST. # NP-75-15R2" (estimate number)
  - "REVISED: JULY 29, 1976 / REVISED FEBRUARY 18, 1976 / DATE JULY 8, 1975" (revises a prior estimate)
  - Lists charges and totals for a client job (photographer's fee, model fee, dye transfer, etc., with costs and totals).
  - "Actual Total Cost" column.
- This is an agency estimate/change order that bills a client job. It is an invoice.
- Wait, is it an invoice? "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
- Let's re-read the invoice bullet: "A payment VOUCHER... is a payment instrument that BILLS a named payee... invoice... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
- This document has "EST. # NP-75-15R2", "REVISED" dates, and lists charges (Dye Transfer, etc.) with "Estimated Total Cost" and "Actual Total Cost". It is billing for print production (photography, processing). This is an invoice (or estimate that functions as a bill for the job).
- Let's check the budget bullet: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job... is budget, not invoice". This has an estimate number, revision lines, and charges/amounts. So it's invoice.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Not a specification.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Not a slide deck.
> **Check 10: ADMINISTRATIVE FORM -> form**
- It has fields and a table, but check 7 (financial document) overrides form layout. "Money function overrides form layout — a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> **Check 11: CORRESPONDENCE**
- Not a letter/memo/email.
> **Check 12: PUBLISHED JOURNALISM**
- Not news.
> **Check 13: ORIGINAL RESEARCH WRITE-UP**
- Not a scientific report.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Not an ad.
> So the label is `invoice`.
> Let's double check.
Title: "PRINT PRODUCTION ESTIMATE"
Agency: "Ted Bates new york/advertising"
Client: "BROWN & WILLIAMSON TOBACCO CORPORATION"
Est. #: NP-75-15R2
Revised dates.
Table with costs for photography and processing.
This is an invoice/estimate from an advertising agency for print production. According to the rules: "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." "the word 'estimate' in the title does NOT make it budget." "when it names an estimate number ('EST NO'), revises a prior estimate... lists charges and totals for a client job is the agency's bill (invoice)."
This perfectly matches the invoice definition.
> Runner-up: budget. Ruled out because the document names an estimate number ("EST. # NP-75-15R2"), has revision dates ("REVISED: JULY 29, 1976"), and lists specific charges and totals for a client job (photography/processing costs), making it an agency bill (invoice) rather than a pure planning document.
> Let's quickly review the pre-scan for any email/fax headers.
Top right: "NON-COMMISSONABLE"
Bottom: microfilm edge "NOTICE IF THE FILM IMAGE IS LESS CLEAR THAN THIS NOTICE... 77917 7 9 / 4". No fax header. No email header.
> Final check of the steps:
1. file_folder: no, has content.
2. handwritten: no, mostly typed.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial (invoice): yes. Agency estimate with EST #, revisions, and charge list.
8. specification: no.
9. presentation: no.
10. form: no, check 7 overrides.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no.
14. advertisement: no.
> Label: invoice.

---

## form → file_folder (1 errors)

### `rvl_cdip__form__0004.png`
**Expected:** `form` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There is text "Insecticides" at the top right (rotated) and "51303 2938" at the bottom right (rotated). These look like a section title and a Bates number or archive ID.
> **2. Scratchpad procedure:**
> *   **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
    *   Evidence: The page is almost entirely blank. It has a vertical black bar on the right side (looks like a folder edge or scan artifact). There is text "Insecticides" rotated 90 degrees at the top right. There is text "51303 2938" rotated 90 degrees at the bottom right.
    *   Wait, let's look closer. "Insecticides" is a short label. "51303 2938" looks like a Bates number or archive number.
    *   Is this a folder tab? The black bar on the right looks like the edge of a folder or a scan artifact. The text "Insecticides" is a short filing label.
    *   Let's check the rules for `file_folder`: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only." "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB — a protruding tab-shaped piece of cardboard... bearing a short filing label... usually with a Bates number stamped on the folder body." "The black bar is the photographed folder body/tab edge — it is NOT a slide-mount scan artifact".
    *   Here, we have a black bar on the right edge. Text "Insecticides" and "51303 2938". This looks exactly like a folder tab scan. "Insecticides" is the filing label. "51303 2938" is the Bates number.
    *   Wait, is "Insecticides" a topical title? "A prominent topical heading always counts as real content... EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... is a filing label, not a bold headline title".
    *   The black bar on the right looks like the folder body. The text is rotated. This fits the "folder-tab page" description perfectly. "a short filing label that names the folder's contents... usually with a Bates number... The label IS filing metadata... so it is NOT a 'topical title' for this check. The page stays file_folder even when the label is rotated 90 degrees".
    *   So, Check 1 matches.
> *   **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
    *   Evidence: None. Not handwritten.
> *   **Check 3: FAX TRANSMISSION SHEET -> form**
    *   Evidence: None.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: None.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: None.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: None. No journal header.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: None.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: None.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: None. Although there is a black bar, the text "Insecticides" is a short filing label on a folder tab, not a slide title. The rule says: "BUT this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1)".
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: None.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: None.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: None.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: None.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: None.
> **Conclusion:**
The page is a scan of a folder tab. It has a black bar (folder body), a short label "Insecticides", and a number "51303 2938" (Bates number). This fits Check 1: `file_folder`.
> Let's double check.
Text: "Insecticides" (rotated).
Text: "51303 2938" (rotated).
Black bar on the right edge.
This is a classic folder tab scan.
Label: `file_folder`.
> Runner-up: `presentation`. Ruled out because the black bar and sparse text are characteristic of a photographed folder tab (Check 1 exception), not a slide deck. The text "Insecticides" is a filing label, not a presentation title.
> Final check of the rules:
- "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number... The black bar is the photographed folder body/tab edge... The page stays file_folder even when the label is rotated 90 degrees".
- Matches perfectly.
> One detail: "51303 2938". This looks like a Bates number (51303 is a common Bates range for tobacco archives, e.g., 5130300000+). "Insecticides" is the content of the folder.
> So, `file_folder`.

---

## form → specification (1 errors)

### `rvl_cdip__form__0013.png`
**Expected:** `form` | **Predicted:** `specification`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking each condition in order.
> **Pre-scan:**
- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: None. There is a Bates number "620423067" at the bottom right. No journal name, volume, issue, page range.
> **Check 1: file_folder**
- Evidence: The page has a lot of body content (a table with many rows and columns of data). Not just an identifier/stamp.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: The page is mostly a printed table with some handwritten entries (numbers, dates). The majority of the content is the printed structure (labels like "BRAND", "PRODUCTION DATE", "OPERATOR NUMBER", "CIGARETTE", "P.D. (INCHES)", "WEIGHT (MG)", "FILTER", "PAPER", "TOR. ANALYSES (%)", "SMOKING (CIGS)"). The handwriting fills in the fields.
- Result: not this check. (Handwriting filling printed fields is form).
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No questions, rating scales, or survey items. It's a data table.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No biographical info.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range, DOI, or copyright line on the page itself. Just a Bates number.
- Result: not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial line items, ledger, statement, voucher, check face. It's technical data (cigarette analysis: weight, tar, nicotine, etc.).
- Result: not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: The table is titled/structured around "BRAND St. James C4 1001 84" (or similar, looks like "St. James C4 1001 84"). It contains "MAINSTREAM SMOKE ANALYSES" or similar technical data for a cigarette product. Wait, let's look closer.
- The table has rows: "CIGARETTE", "P.D. (INCHES)", "WEIGHT (MG)", "FILTER", "PAPER", "TOR. ANALYSES (%)", "SMOKING (CIGS)", "Tar (MG)", "Nicotine (MG)", "Resistancy (%)", "Puffs", "NO (MG)", "CO (MG)", "Cig. Perf. Fairness", "E-d Stability", "Coal Retention", "Corr. BORG FV", "BORG FV Moisture", "Corr. FILL VALUE", "FV MOISTURE".
- This is a product analysis table or test-analysis table keyed to product codes/parameters.
- Check 8 says: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough... A labeled product/parameter rate-data chart... is a specification".
- Wait, is this a specification or a form?
- Check 10: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8)".
- Let's re-read Check 8: "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification".
- The table has "BRAND St. James C4 1001 84" at the top. It has columns for different dates/analyses (P57L D6, P57L D15, etc.). It contains measured parameters (Tar, Nicotine, Weight, etc.). This is product-referenced test data / product analysis table.
- Let's check if it's a form (Check 10). "Filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)" is a form. But Check 8 says "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification."
- Wait, is this a specification? "Material Safety Data Sheet... product formulation... manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification."
- The table is a test-analysis table for a specific product ("St. James C4"). It lists measured values for various parameters. This fits "test-analysis tables keyed to product/part codes" or "Product-referenced test data".
- Let's look at Check 10 again: "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8)". This table has measured parameters. Does it have spec limits? The columns have "X SD N" headers, which might be statistical process control (mean, standard deviation, N). This looks like a lab data sheet or test analysis summary.
- Wait, Check 10 says: "a filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)" is a form. But this is a cigarette analysis table.
- Let's re-read Check 8 carefully: "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification."
- The table is analyzing "St. James C4". It has rows for "Tar (MG)", "Nicotine (MG)", etc. This is product-referenced test data. So it should be specification.
- Let's consider if it's a form. "administrative form -> form: Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A filled analytical or lab data sheet... is a form". But Check 8 explicitly says "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification." The priority is: check 8 comes before check 10. If it's a test-analysis table for a product, it's specification.
- Let's look at the headers: "BRAND St. James C4 1001 84". "PRODUCTION DATE", "OPERATOR NUMBER", "DATE ANALYSIS EXPECTED", "DATE RECEIVED". Then columns: "P57L D6", "P57L D15". Underneath: "X SD N". This is a statistical process control or lab analysis sheet for a cigarette product.
- Is it a specification? "A labeled product/parameter rate-data chart — e.g. a statistical process-control chart titled with the product name (e.g. 'WINSTON KS RATE DATA') plotting a measured property over time/subgroup against spec limits (e.g. 'USPEC'/'SPEC') — is a specification". This table has "X SD N" which is mean, standard deviation, N. It's a lab data summary.
- Actually, let's look at Check 10: "A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)". This is a cigarette analysis.
- Wait, Check 8: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification." This table is definitely product-referenced test data (St. James C4).
- Let's check if there's any other category.
- Check 9: presentation. No.
- Check 10: form. "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8)". This table holds product's measured parameters. So it's specification.
- Let's verify the "specification" definition again. "Material Safety Data Sheet... product formulation... manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification." Yes, this is a test-analysis table for a product.
> Let's double check if it could be a form.
Check 10: "administrative form -> form... A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)". This example is for chemical analysis. The cigarette analysis is "test-analysis tables keyed to product/part codes". Check 8 explicitly captures this: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification."
Therefore, specification is the correct label.
> Let's review the table content:
Top row: "BRAND St. James C4 1001 84"
Rows: CIGARETTE, P.D., WEIGHT, FILTER, PAPER, TOR. ANALYSES, SMOKING (CIGS), Tar, Nicotine, Resistancy, Puffs, NO, CO, Cig. Perf. Fairness, E-d Stability, Coal Retention, Corr. BORG FV, BORG FV Moisture, Corr. FILL VALUE, FV MOISTURE.
This is a standard cigarette product analysis / test analysis table. It is product-referenced test data.
Label: specification.
> Wait, is there any chance it's a scientific_report?
Check 13: "Original research write-up -> scientific_report: Running narrative prose... Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."
This page has no running prose, only a table. So not scientific_report.
> Is it a form?
Check 10: "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8)".
This table holds product's measured parameters (Tar, Nicotine, etc. for St. James C4). So it's specification.
> Let's confirm the evidence for specification (Check 8):
- "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification."
- The table is titled/identified by "BRAND St. James C4 1001 84".
- It contains test analysis data (Tar, Nicotine, Weight, etc.) for this product.
- This matches "test-analysis tables keyed to product/part codes" and "Product-referenced test data".
> Runner-up: form. Ruled out because the table is a product-referenced test-analysis table (stating measured parameters for a specific product, St. James C4), which Check 8 explicitly classifies as specification, overriding the generic form rule for labeled data tables.
> Final check of the steps:
1. file_folder: no, has body content.
2. handwritten: no, handwriting fills printed fields.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no journal ID.
7. financial: no.
8. specification: yes, product-referenced test-analysis table ("BRAND St. James C4...").
9. presentation: no.
10. form: no, overridden by check 8 for product test data.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no, no running prose.
14. advertisement: no.
> The label is specification.

---

## handwritten → advertisement (1 errors)

### `rvl_cdip__handwritten__0003.png`
**Expected:** `handwritten` | **Predicted:** `advertisement`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is a handwritten note, but no email header.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head.
- **Layout:** The page is mostly blank white space. In the bottom right quadrant (rotated 90 degrees counter-clockwise), there is a block of content. Let's rotate it mentally.
    - Top part (right side in original): A large black box with "7 ELEVEN" logo, "$3.50 off a carton", "35¢ off a pack", "CAMEL WINSTON". This is clearly an advertisement/coupon.
    - Bottom part (left side in original, below the ad): A mailing label/return address block. "P.O. Box 834039, Richardson, TX 75083-4039". "52273 9120". "PAID U.S. POSTAGE". "Change Service Requested".
    - Address block: "NANCY EVERITT, 2705 SUPERIOR DR, LIVERMORE CA 94550-6615". "#BANKSUD AUTO ************ S-DIGIT 94650". "TD-203258785 003137". "#203258785-21374#". "P131-99". "C1065 P001".
    - Handwritten note: "Please remove, Addressee is deceased. Died of smoking-related illness on 11/15/98."
    - Small text: "MAN AND CIGARETTES TO SMOKERS 21 YEARS OF AGE OR OLDER". "THIS IS NOT A COUPON See other side for details."
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: There is a lot of content (ad, address, handwritten note). Not just an ID/stamp.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: There is a handwritten note ("Please remove..."). But most of the content is printed (ad, address block, postal markings). The handwriting is a small annotation.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No fax header.
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
> *   **Check 7: financial document (invoice/budget)**
    *   Evidence: There is a "PAID U.S. POSTAGE" block and a coupon value ($3.50 off). But this isn't a bill or budget statement. It's a mail piece.
    *   Result: not this check.
> *   **Check 8: specification**
    *   Evidence: No product specs.
    *   Result: not this check.
> *   **Check 9: presentation**
    *   Evidence: The page is mostly blank. The content is rotated. It looks like a scanned mail piece or a coupon. Wait, let's look at the layout.
    *   The content is in the bottom right, rotated.
    *   Is it a slide? No.
    *   Is it a cover? No.
    *   Wait, is it an advertisement? Check 14.
> *   **Check 10: form**
    *   Evidence: No structured data capture fields.
    *   Result: not this check.
> *   **Check 11: correspondence (email/memo/letter)**
    *   Evidence: No letter structure. The handwritten note is an annotation on a mail piece.
    *   Result: not this check.
> *   **Check 12: news_article**
    *   Evidence: No masthead.
    *   Result: not this check.
> *   **Check 13: scientific_report**
    *   Evidence: No running prose.
    *   Result: not this check.
> *   **Check 14: advertisement**
    *   Evidence: The dominant content (when rotated correctly) is a large black box with "7 ELEVEN", "$3.50 off a carton", "35¢ off a pack", "CAMEL WINSTON". This is a coupon/advertisement.
    *   The page also contains a mailing label (mailing piece) and a handwritten note about the addressee being deceased.
    *   The prompt says: "Judge by DOMINANT content: a single brand advertisement (product imagery, slogans, a Surgeon General warning, brand styling) is an advertisement (check 14) even if printed inside a newspaper/magazine with a running masthead and some surrounding text".
    *   Here, the page is essentially a scanned coupon/mailing piece. The main visual element is the 7-Eleven coupon for Camel/Winston cigarettes.
    *   Wait, is it a "mailing label" or "mail piece"? The categories don't have "mailing_label".
    *   Let's re-read the categories.
    *   The page contains a coupon: "$3.50 off a carton... THIS IS NOT A COUPON".
    *   It has a "PAID U.S. POSTAGE" block.
    *   It has a handwritten note: "Please remove, Addressee is deceased. Died of smoking-related illness on 11/15/98."
    *   This looks like a scanned piece of junk mail or a coupon that was mailed, or perhaps a clipping.
    *   Actually, looking closely at the layout: The black box is an advertisement/coupon. The text below it (rotated) is a mailing label/return address for "P.O. Box 834039...".
    *   The handwritten note is on the mailing label part.
    *   The dominant visual feature is the large black advertisement block for Camel/Winston cigarettes at 7-Eleven.
    *   Check 14: "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures."
    *   This is definitely a coupon/advertisement. The text "THIS IS NOT A COUPON" is standard coupon disclaimer.
    *   The handwritten note is an annotation on the document, likely by an archivist or someone processing the mail.
    *   The document itself is an advertisement/coupon (specifically a direct mail coupon or a clipping of one).
    *   Wait, is it a "form"? No.
    *   Is it a "letter"? No.
> Let's look at the "advertisement" definition again.
"Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures."
The page contains a large coupon for Camel/Winston cigarettes at 7-Eleven.
The rest is mailing metadata (return address, postage paid) and a handwritten annotation.
The dominant content is the advertisement/coupon.
> Let's check if there's any other category.
Could it be `file_folder`? No, it has content.
Could it be `handwritten`? No, mostly printed.
Could it be `form`? No.
> The page is essentially a scanned coupon/mailing piece. The main feature is the ad.
The handwritten note says "Please remove, Addressee is deceased...". This suggests it's a piece of mail that was intercepted or processed.
But the document *is* the advertisement/coupon (with mailing info).
Actually, looking at the layout, it looks like a direct mail piece or a coupon clipped from a newspaper/magazine and mailed back? Or a mailing label attached to a coupon?
The text "P.O. Box 834039... PAID U.S. POSTAGE... Change Service Requested" indicates this is a mailing piece (bulk mail).
The content of the mailing piece is the advertisement/coupon.
Therefore, the document is an advertisement.
> Let's refine the scratchpad.
> **Scratchpad:**
- **Pre-scan:** No mail header. No masthead.
- **Check 1 (file_folder):** No. The page has a large advertisement block, mailing address, and handwritten note. Not just an ID.
- **Check 2 (handwritten):** No. Handwriting is a small note ("Please remove..."). Most content is printed (ad, address).
- **Check 3 (fax):** No.
- **Check 4 (questionnaire):** No.
- **Check 5 (resume):** No.
- **Check 6 (scientific_publication):** No.
- **Check 7 (financial):** No. The "$3.50 off" is a coupon discount, not an invoice/budget. "PAID U.S. POSTAGE" is postal, not financial document.
- **Check 8 (specification):** No.
- **Check 9 (presentation):** No. Not a slide deck.
- **Check 10 (form):** No.
- **Check 11 (correspondence):** No. No letter/memo structure. The handwritten note is an annotation.
- **Check 12 (news_article):** No.
- **Check 13 (scientific_report):** No.
- **Check 14 (advertisement):** Yes. The page contains a large marketing layout: "7 ELEVEN", "$3.50 off a carton", "35¢ off a pack", "CAMEL WINSTON", "THIS IS NOT A COUPON". This is a coupon/advertisement. The mailing label and handwritten note are secondary/annotations on this document. The dominant content is the promotional material.
> Wait, is the whole page an advertisement?
The page is mostly white space. The content is in the bottom right, rotated 90 degrees.
If I rotate the image 90 degrees clockwise:
- Top: 7-Eleven logo, "$3.50 off a carton", "35¢ off a pack", "CAMEL WINSTON".
- Bottom: Mailing address block, "PAID U.S. POSTAGE", handwritten note.
This looks like a direct mail piece or a coupon that was part of a mailing.
The definition of advertisement includes "coupons".
"Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures."
This fits perfectly.
> Runner-up: `form` or `letter` or `handwritten`.
- `handwritten`: Ruled out because handwriting is minor annotation.
- `letter`: Ruled out because no salutation/closing, it's a mailing label + ad.
- `form`: Ruled out because it's not capturing data.
> Final decision: `advertisement`.
> One detail: "Judge by DOMINANT content... a single brand advertisement... is an advertisement even if printed inside a newspaper...".
Here, the page *is* the advertisement/coupon (with mailing info). The dominant visual element is the black box with the offer.
> Let's double check Check 14.
"Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures."
The text "THIS IS NOT A COUPON See other side for details" is a classic coupon disclaimer.
The content is "$3.50 off a carton... 35¢ off a pack... CAMEL WINSTON".
This is definitely an advertisement/coupon.
> The handwritten note "Please remove, Addressee is deceased..." is an archival annotation on the scanned item. It doesn't change the document type.
> Final label: advertisement.

---

## handwritten → letter (1 errors)

### `rvl_cdip__handwritten__0012.png`
**Expected:** `handwritten` | **Predicted:** `letter`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** No "From:", "To:", "Sent:", "Subject:" headers. There is a handwritten date "Dec 29, 1995". There is a printed address block at the top: "Inge and Peter Forte, Kilgorewood Drive #7 Bldg 121, 2905 SE Ocean Blvd, Stuart, FL 34996". This looks like a return address or the sender's address block, but it's printed. Wait, let's look closer. "Inge and Peter Forte... Stuart, FL 34996". This is the sender's address.
- **Masthead/Running head:** No newspaper masthead. No journal running head. There is a Bates number "2489021" at the top right. There is a vertical number "51821 5951" on the right side.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a lot of handwritten text. It's a letter. Not just an ID/stamp.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
    *   Wait, is it on a printed template? The paper has horizontal lines. "To whom this may concern," is handwritten. "My wife Inge has been smoking..." is handwritten. "Sincerely, Peter Forte" is handwritten.
    *   Is there a printed template? There are horizontal lines. It looks like lined paper.
    *   Let's check the rules: "A handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
    *   "The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
    *   This page has horizontal lines (ruled paper). The text is freeform handwriting. There are no printed field labels like "Name:", "Address:". The address at the top is printed: "Inge and Peter Forte / Kilgorewood Drive #7 Bldg 121 / 2905 SE Ocean Blvd / Stuart, FL 34996". This looks like a letterhead or a printed return address block.
    *   The body is entirely handwritten. "To whom this may concern, My wife Inge has been smoking 'Manchester Cigarettes' ever since they came out in the market. It's very annoying when she has to use a razor blade to open a pack of Manchester cigarettes. Some day she's going to cut herself. She can't seems to find the way to open them easily. Can you find a way to have this pack easier to open. Thank you. P.S. The cigarettes are ultra light 100. Sincerely, Peter Forte".
    *   This is a freeform handwritten letter on lined paper.
    *   Wait, is it a "handwritten" category? Yes. "Most of the content is freeform handwriting... NOT on a printed template." Lined paper is not a printed template with fields.
    *   Let's check Check 11 (Correspondence -> letter).
    *   Letter definition: "letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person..."
    *   Here we have:
        *   Printed address block at top: "Inge and Peter Forte...". Wait, is this the recipient or sender? Usually, a letterhead has the sender's info. But the letter is signed "Peter Forte". So "Inge and Peter Forte" are the senders. The address is their address.
        *   Date: "Dec 29, 1995" (handwritten).
        *   Salutation: "To whom this may concern," (handwritten).
        *   Body: Handwritten prose.
        *   Closing: "Sincerely, Peter Forte" (handwritten).
    *   This fits the definition of a **letter**.
    *   Let's re-evaluate Check 2 vs Check 11.
    *   Check 2: "Most of the content is freeform handwriting... NOT on a printed template."
    *   Check 11: "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person..."
    *   The instructions say: "Walk checks 1-14 below IN ORDER."
    *   Check 2 comes before Check 11.
    *   Let's look closely at Check 2: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout."
    *   "Handwriting filling in labeled printed fields is form, not handwritten".
    *   "A typed page with only a signature, stamp, or margin note is not handwritten."
    *   "Notes ABOUT a survey instrument are questionnaire, not handwritten".
    *   "A freeform handwritten consumer opinion/feedback card is handwritten, not questionnaire".
    *   The page is almost entirely handwritten. The only printed text is the address block at the top ("Inge and Peter Forte..."), the Bates number ("2489021"), and the vertical number ("51821 5951"). The paper has horizontal lines.
    *   Is lined paper a "printed template"? The rule says: "written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten." So lined paper counts as handwritten if there are no field labels.
    *   So Check 2 seems to match. "Most of the content is freeform handwriting".
    *   However, let's look at Check 11. "letter: ... OR a dated note addressed to a named EXTERNAL person...".
    *   The rule for Check 2 says: "This wins over a typed letter or memo layout." It doesn't explicitly say it wins over a handwritten letter. But "Most of the content is freeform handwriting (notes, letters, memos, drafts)..." implies that a handwritten letter falls under Check 2.
    *   Wait, let's read Check 2 carefully: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout."
    *   If the page is a handwritten letter, does it go to Check 2 (handwritten) or Check 11 (letter)?
    *   Check 2 is "HANDWRITTEN PAGE". Check 11 is "CORRESPONDENCE -> email, memo, or letter".
    *   Usually, if a document is primarily handwritten text on lined paper (like a fan letter or complaint), it's classified as `handwritten`.
    *   Let's check the calibration notes: "Filled forms are still forms... Handwriting that fills a printed form or table is not 'handwritten'; freeform handwriting on unlabeled paper is."
    *   "A handwritten note about a questionnaire... is questionnaire... A freeform handwritten consumer opinion/feedback card is handwritten, not questionnaire".
    *   This looks like a consumer feedback card/letter. "My wife Inge has been smoking... Can you find a way to have this pack easier to open."
    *   It is a freeform handwritten note.
    *   Let's look at the priority. Check 2 is before Check 11.
    *   Check 2 evidence: "Most of the content is freeform handwriting... 'To whom this may concern,' ... 'Sincerely, Peter Forte'". The text is handwritten. The paper is lined (ruled lines), but there are no printed field labels/boxes. The address at the top is printed, but it's just an address block, not a form template with fields.
    *   Wait, is the address block a "letterhead"? "Inge and Peter Forte...". Yes, it's a printed address block.
    *   If it has a letterhead, is it a letter (Check 11) or handwritten (Check 2)?
    *   Check 2 says: "Most of the content is freeform handwriting... NOT on a printed template." Lined paper with a printed address at the top is often considered a template (stationery). But the rule says "written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten." This suggests lined paper is okay for `handwritten`.
    *   However, Check 11 defines `letter`: "letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature".
    *   Here we have: Printed address (sender), Date (handwritten), Salutation (handwritten "To whom this may concern"), Body (handwritten), Closing (handwritten).
    *   The recipient is "To whom this may concern" (external, generic).
    *   So it fits `letter` perfectly under Check 11.
    *   Does it fit `handwritten` under Check 2? "Most of the content is freeform handwriting... NOT on a printed template."
    *   The presence of the printed address block "Inge and Peter Forte..." makes it look like stationery/letterhead.
    *   Let's look at the instruction: "Judge each page by its FUNCTION... a bill is a bill even when it is printed on a form."
    *   Function: It's a letter/complaint.
    *   But Check 2 is "MAJORITY-HANDWRITTEN PAGE". If >50% is handwriting, it's handwritten?
    *   "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
    *   If it is on a printed template (letterhead), then Check 2 might not apply? "NOT on a printed template". A letterhead is a printed template.
    *   The address block is printed. The lines are printed.
    *   So it IS on a printed template (stationery).
    *   Therefore, Check 2 fails because it is on a printed template (letterhead/lines).
    *   Wait, the rule says: "written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten." This implies lined paper is allowed for `handwritten`.
    *   But "NOT on a printed template". Letterhead is a template.
    *   Let's look at the example or calibration. "Handwriting that fills a printed form or table is not 'handwritten'; freeform handwriting on unlabeled paper is." Lined paper is unlabeled (no field labels).
    *   But there is a printed address.
    *   Let's look at Check 11 again. "letter: letterhead with an external recipient address...". The printed block is the sender's address (letterhead). The recipient is "To whom this may concern" (external).
    *   So it is a letter.
    *   Why would Check 2 not win? "This wins over a typed letter or memo layout." It doesn't say it wins over a handwritten letter. It says "Most of the content is freeform handwriting... NOT on a printed template."
    *   If the page has a letterhead (printed address), it is on a printed template. So Check 2 is "not this check" (because it is on a printed template, i.e., letterhead stationery).
    *   Actually, let's look at the text. "Inge and Peter Forte...". This is the sender. The letter is signed by Peter Forte. So it's his stationery.
    *   So it's a letter on letterhead.
    *   Check 2 requires "NOT on a printed template". Letterhead is a printed template. So Check 2 is out.
    *   Check 11: `letter`. Evidence: Letterhead (printed address block), Date (Dec 29, 1995), Salutation ("To whom this may concern"), Prose body, Closing ("Sincerely, Peter Forte").
    *   Wait, is "To whom this may concern" a salutation? Yes.
    *   Is the recipient external? Yes, "To whom this may concern" implies an external entity (the tobacco company).
    *   So it is a `letter`.
> Let's re-read Check 2 carefully.
"Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
If the document is a handwritten letter on lined paper with a printed return address, is it `handwritten` or `letter`?
The calibration says: "Handwriting that fills a printed form or table is not 'handwritten'; freeform handwriting on unlabeled paper is."
Lined paper is "unlabeled paper" (no field labels).
But the address block is printed.
If I classify it as `handwritten`, I ignore the letter structure.
If I classify it as `letter`, I follow Check 11.
Check 2 is before Check 11.
If Check 2 matches, I stop.
Does Check 2 match? "Most of the content is freeform handwriting... NOT on a printed template."
The page has horizontal lines. Is lined paper a "printed template"?
Usually, "printed template" means a form with fields (Check 10).
The rule says: "written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
This explicitly allows lined paper for `handwritten`.
So, is the address block making it a "printed template"?
The address block is just an address. It's not a form template.
However, Check 11 `letter` definition: "letterhead with an external recipient address...".
The printed block "Inge and Peter Forte..." is a letterhead (sender's address).
So it fits `letter` (Check 11).
> Let's look at the priority.
Check 2: "MAJORITY-HANDWRITTEN PAGE".
If the page is mostly handwriting, and it's not on a form (no field labels), it's `handwritten`.
The rule: "A typed page with only a signature, stamp, or margin note is not handwritten." (This is about typed pages).
"The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
This page has lined paper (ruled lines, but no entry cells/fields). The text is freeform.
The printed text is just the address at the top and Bates numbers.
So Check 2 seems to have strong evidence: "Most of the content is freeform handwriting... on lined paper (no printed field labels)".
BUT, Check 11 `letter` is also a strong match.
Which one wins?
Check 2 is "MAJORITY-HANDWRITTEN PAGE".
Check 11 is "CORRESPONDENCE".
The instructions say: "Walk checks 1-14 below IN ORDER."
If Check 2 matches, I stop.
Does Check 2 match?
"Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
Is this on a printed template?
The paper has lines. The address is printed.
If I consider "lined paper with printed address" as a printed template (stationery), then Check 2 fails.
If I consider it as "freeform handwriting on lined paper" (as per the rule "written freely on blank or lined paper... is handwritten"), then Check 2 matches.
> Let's look at the `letter` definition in Check 11.
"letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person..."
This page has:
- Letterhead (printed address: Inge and Peter Forte...)
- Date: Dec 29, 1995
- Salutation: "To whom this may concern,"
- Prose body: Handwritten.
- Closing: "Sincerely, Peter Forte".
This is a perfect match for `letter`.
> Why would `handwritten` be the answer?
If the page was just a scribbled note on a napkin, it's `handwritten`.
If the page is a formal letter (even handwritten) on letterhead, it's `letter`.
The rule for Check 2 says: "NOT on a printed template".
Letterhead is a printed template.
So Check 2 fails because it is on a printed template (letterhead stationery).
The address block "Inge and Peter Forte..." is a printed letterhead.
So Check 2 is "not this check" (because it's on a printed template/letterhead).
Then we go to Check 11.
Check 11 `letter`: Yes, letterhead + date + salutation + body + signature.
> Let's verify the "printed template" condition.
"Most of the content is freeform handwriting ... NOT on a printed template."
"A handwritten note ... written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
This is a bit contradictory. "Lined paper" is allowed for handwritten. But "letterhead" is a template.
The address block is printed. The lines are printed.
If I have to choose, `letter` is more specific to the function (correspondence). `handwritten` is a physical description.
The instructions say: "Judge each page by its FUNCTION... a bill is a bill even when it is printed on a form."
Function here is a letter/complaint.
Also, Check 2 says "This wins over a typed letter or memo layout." It doesn't say it wins over a handwritten letter that fits the `letter` definition.
Actually, if a letter is handwritten, is it `handwritten` or `letter`?
Usually, in these datasets, a handwritten letter on lined paper is `handwritten` if it's freeform.
But here, there is a clear letter structure: Date, Salutation, Body, Closing.
And a printed letterhead.
Let's look at the calibration: "Handwriting that fills a printed form or table is not 'handwritten'; freeform handwriting on unlabeled paper is."
This page is freeform handwriting on labeled paper (lines) + letterhead.
The letterhead makes it a `letter`.
> Let's look at the text again.
"To whom this may concern," -> Salutation.
"My wife Inge..." -> Body.
"Sincerely, Peter Forte" -> Closing.
This is a letter.
Check 11 `letter`: "letterhead with an external recipient address [well, sender address here, but letterhead implies external context], date, 'Dear ...' salutation [here 'To whom this may concern'], prose body, and a closing with signature".
Wait, the definition says "external recipient address". The printed block is the sender's address (Inge and Peter Forte). The recipient is "To whom this may concern" (external).
So it fits `letter`.
> Let's check Check 2 again.
"Most of the content is freeform handwriting... NOT on a printed template."
If the page has a letterhead, it is on a printed template. So Check 2 is out.
Evidence for Check 2: "Most content is handwriting."
Evidence against Check 2: "It is on a printed template (letterhead with address block and lined paper)." The rule says "NOT on a printed template". A letterhead is a printed template.
So Check 2 is not this check.
> Check 3: Fax sheet. No.
Check 4: Questionnaire. No.
Check 5: Resume. No.
Check 6: Scientific publication. No.
Check 7: Financial. No.
Check 8: Specification. No.
Check 9: Presentation. No.
Check 10: Form. No. (No fields to fill, just lines).
Check 11: Correspondence -> letter.
Evidence: Printed letterhead ("Inge and Peter Forte..."), Date ("Dec 29, 1995"), Salutation ("To whom this may concern,"), Prose body (handwritten complaint about cigarette packs), Closing ("Sincerely, Peter Forte").
This is a letter.
> Runner-up: `handwritten`. Ruled out because the page has a printed letterhead (address block) and follows a letter structure (date, salutation, closing), making it a letter (Check 11) rather than just freeform handwriting on unlabeled paper (Check 2 requires "NOT on a printed template"). Wait, the rule says "written freely on blank or lined paper... is handwritten". The presence of the letterhead address block makes it a letter template.
> Let's refine the "printed template" argument.
The rule for Check 2: "The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
This suggests that even if there is an address written, if it's on lined paper with no fields, it's handwritten.
BUT, the address here is PRINTED. "Inge and Peter Forte...".
And the paper has lines.
And the content is a formal letter structure.
Check 11 `letter`: "letterhead with an external recipient address...".
Actually, the printed block is the sender's address. A letterhead usually contains the sender's address.
The definition says "letterhead with an external recipient address". This is slightly confusing. Usually letterhead is sender, recipient address is below date.
Here, there is no recipient address block (like "Mr. Smith, Company, Address"). Just "To whom this may concern".
But "OR a dated note addressed to a named EXTERNAL person...". "To whom this may concern" is an external addressee (generic).
So it fits the second part of the `letter` definition: "a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block." Here it's addressed to "To whom this may concern" (external).
And it has a closing signature.
So it is a `letter`.
> Final decision: `letter`.
> Wait, let's look at the `handwritten` check again.
"Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
If I classify this as `handwritten`, I am saying the function is "handwritten note".
If I classify as `letter`, function is "correspondence".
The text is a complaint/feedback. "Can you find a way to have this pack easier to open."
This is a consumer letter.
In the tobacco archive, these are often classified as `letter` or `handwritten`.
Given the explicit letter structure (Date, Salutation, Body, Signature) and the printed letterhead, `letter` is the correct functional classification.
Check 2 is for "freeform handwriting... NOT on a printed template". The printed letterhead and the formal structure make it a letter, not just a freeform note. The lined paper is part of the stationery (template).
> One detail: "To whom this may concern," is handwritten.
"Dec 29, 1995" is handwritten.
The body is handwritten.
The signature is handwritten.
The only printed text is the address block at the top and the Bates numbers.
Is a page with a printed address block and lined paper a "printed template"? Yes, it's stationery.
So Check 2 fails ("NOT on a printed template").
Check 11 `letter` succeeds.
> Evidence for Check 11:
- Printed address block (letterhead): "Inge and Peter Forte / Kilgorewood Drive #7 Bldg 121 / 2905 SE Ocean Blvd / Stuart, FL 34996".
- Date: "Dec 29, 1995".
- Salutation: "To whom this may concern,".
- Prose body: Handwritten text about Manchester Cigarettes.
- Closing: "Sincerely, Peter Forte".
- External recipient: "To whom this may concern" (generic external).
> Runner-up: `handwritten`. Ruled out because the page contains a printed letterhead (address block) and follows a formal letter structure (date, salutation, closing signature), which fits the `letter` definition in Check 11. Check 2 requires content "NOT on a printed template".
> One more check: Is it a `questionnaire` response?
"Can you find a way to have this pack easier to open."
It's a freeform comment. Not a printed survey instrument.
Check 4: "A freeform handwritten consumer opinion/feedback card is handwritten, not questionnaire".
Wait. "A freeform handwritten consumer opinion/feedback card is handwritten, not questionnaire".
This is a consumer opinion/feedback.
If it's a feedback card, is it `handwritten`?
Check 2: "Most of the content is freeform handwriting...".
If the rule "A freeform handwritten consumer opinion/feedback card is handwritten, not questionnaire" applies, then maybe it is `handwritten`?
Let's check the context of that rule.
"Conversely, a respondent's freeform handwritten opinion/feedback card (a person's own words in response to a printed prompt such as 'Tell us what you think' — e.g. 'I think NOW in the KNOW is... Please take me off of Mailing list...') IS handwritten, NOT questionnaire: questionnaire requires a PRINTED survey instrument with printed question items, rating scales, or response boxes, not a person's freeform writing."
This rule is under Check 2 (handwritten) or Check 4 (questionnaire)?
It's in the main text under Check 2 description? No, it's in the "Calibration" or "Checks" section?
Ah, it's in the main text for Check 2: "Notes ABOUT a survey instrument are questionnaire, not handwritten... Conversely, a respondent's freeform handwritten opinion/feedback card... IS handwritten, NOT questionnaire".
So if this is a "consumer opinion/feedback card", it should be `handwritten`.
> Is this a "feedback card"?
It has a printed address block. It has lines.
It looks like a letter written on lined paper.
"To whom this may concern," suggests a letter.
A feedback card usually has a printed prompt like "Tell us what you think". Here, there is no printed prompt. The person just wrote a letter.
So it's a letter.
The rule "A freeform handwritten consumer opinion/feedback card is handwritten" applies when there is a printed prompt or it's a card. Here, it's a letter on stationery.
The function is correspondence (letter).
> Let's look at the `letter` definition again.
"letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person..."
This fits perfectly.
> So, `letter`.
> Final check of the scratchpad steps:
1. file_folder: No, has content.
2. handwritten: "Most content is handwriting", BUT it is on a printed template (letterhead address block + lined paper) and has letter structure. The rule says "NOT on a printed template". The printed address block makes it a letterhead. So not this check. (Or, if lined paper is allowed, the letter structure pushes it to Check 11. But Check 2 is before Check 11. If Check 2 matches, I stop. Does Check 2 match? "NOT on a printed template". Letterhead is a template. So Check 2 fails.)
3. fax: No.
4. questionnaire: No printed survey instrument.
5. resume: No.
6. scientific_publication: No.
7. financial: No.
8. specification: No.
9. presentation: No.
10. form: No fields.
11. correspondence -> letter: Yes. Letterhead (printed address), Date, Salutation, Body, Closing.
> Label: letter.

---

## presentation → form (1 errors)

### `rvl_cdip__presentation__0001.png`
**Expected:** `presentation` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> **Document Analysis:**
- The document is rotated 90 degrees counter-clockwise. Let's read it as if rotated.
- Title: "Philip Morris USA PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION (4WM Nielsen Shares, 3mm Shipment Shares, Biweekly Consumer Shares, Nielsen Pricing) As of 6/15/98"
- There's a table with columns: "Trigger 1H 1998", "Latest Data 4WM", "98 O.B.", "FULL YR 1997", "4th QTR 1997".
- Rows include: "Share of Market", "Philip Morris USA", "Marlboro", "Premium Category", "Basic Less GPC (Shipments)", "Basic Less Doral (Shipments)", "Share of Segment", "PM-USA Share of Premium", "Marlboro Share of Core Prem Increment*", "Basic Share of Discount", "Share of Young Adults", "Marlboro Smoker Share", "Marlboro Volumetric Share", "Price Gaps", "Marlboro Less Lowest", "Promotion Incidence", "Premium Promo Index", "Discount Promo Index".
- There's a footnote: "* Marlboro Share of Core Premium (Marlboro, Camel, Newport Winston) increment is measured on a 3mm vs. year ago Nielsen share basis. Latest data through May 98. Nielsen shares and pricing reflect data through w/e 6/8/98. CTS shares reflect biweekly data through w/e 6/7/98. Basic less Doral and Basic less GPC (Shipments) data are measured on a 3mm basis. Latest data through May 98."
- Bates number: "2071860450"
- Three black dots on the left margin (when rotated correctly, top margin). These look like binder holes or slide mount artifacts, but let's check the rules.
- Wait, the three black dots are on the left edge. If rotated 90 degrees clockwise to read normally, the dots are at the top. Actually, if I rotate the image 90 degrees clockwise, the text is horizontal. The dots are at the top left. Wait, let's look at the orientation.
- Text runs from bottom to top. So rotate 90 degrees clockwise.
- Top margin has three black dots. This is a classic slide/overhead scan artifact or a binder punch? No, three holes on the left margin (when text is horizontal) are binder holes. Wait, if I rotate 90 degrees clockwise, the text is horizontal, reading left to right. The dots are at the top. Let's re-orient.
- Original image: text is vertical, reading bottom to top. Left side has three black dots. Right side has Bates number "2071860450".
- If I rotate 90 degrees clockwise: text is horizontal, reading left to right. The three black dots are at the top. The Bates number is at the bottom right.
- Wait, if I rotate 90 degrees counter-clockwise: text is horizontal, reading right to left.
- Let's assume standard reading orientation: rotate 90 degrees clockwise.
- Title: "Philip Morris USA PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION..."
- Table with data.
- This is a data table / chart.
> **Check 1: file_folder**
- Not just an identifier. Has a bold title "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION" and a large data table. Not file_folder.
> **Check 2: handwritten**
- No handwriting. Typed text and numbers.
> **Check 3: FAX TRANSMISSION SHEET**
- No fax header.
> **Check 4: questionnaire**
- Not a survey instrument.
> **Check 5: resume**
- Not a resume.
> **Check 6: scientific_publication**
- No journal running head. Bates number 2071860450.
> **Check 7: financial document (invoice/budget)**
- Contains financial data (shares, pricing, promo index), but it's not an invoice or budget. It's a performance trigger table.
> **Check 8: specification**
- Not a material safety data sheet or product formulation.
> **Check 9: presentation**
- "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)..."
- "A near-blank cover or title page... is a presentation"
- "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text... points to a photographed slide/overhead — presentation"
- Wait, what about the three black dots? They look like binder holes or slide mount holes.
- Let's look at the layout: It's a single page with a title and a large table of data. "chart-per-page deck look".
- Is it a standalone chart or table?
- Check 10: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a financial/money chart is budget (check 7), and a research-measurement chart is scientific_report (check 13)"
- Wait, what is this chart? "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION". It's a business performance dashboard / trigger points table.
- Let's re-read Check 9: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page... A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Wait! "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Let's check Check 10: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data..."
- Is this generic administrative/log data? It's business performance data (Nielsen shares, pricing).
- Wait, let's look at the labels again.
- Categories: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
- If it's a standalone chart/table of business data, what is it?
- Let's re-read Check 10 carefully: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a financial/money chart is budget (check 7), and a research-measurement chart is scientific_report (check 13)"
- This chart is about "PM-USA PERFORMANCE TRIGGERS", "Nielsen Shares", "Pricing". It's business/marketing data.
- Is it a budget? "financial/money chart is budget (check 7)". This chart has pricing data ("Price Gaps", "Marlboro Less Lowest", "Promotion Incidence", "Premium Promo Index", "Discount Promo Index"). But it's mostly market share data ("Share of Market", "Share of Segment", "Share of Young Adults").
- Is it a form? "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... This also covers: a standalone labeled data chart or table... a standalone labeled chart is a form only when it holds generic administrative/log data". This is a printed report/table, not a form for capturing data. Wait, a filled form is still a form. But this is a printed table of data, not a form to be filled out.
- Let's re-read Check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Wait, if a standalone chart is a form, what kind of form? "administrative form -> form".
- But is there a better category?
- Let's look at the document again. It's a page from a presentation or a report. "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION". "For discussion" implies it's part of a meeting deck or a report.
- If it's a page from a report, and it's just a table, what is it?
- Let's check Check 13: "scientific_report... Requires running narrative prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report." This page has no running prose, just a table and footnotes. So not scientific_report.
- Check 10: "administrative form -> form". "Filled or blank fields... This also covers: a standalone labeled data chart or table... a standalone labeled chart is a form only when it holds generic administrative/log data". Is market share and pricing data "generic administrative/log data"? Or is it something else?
- Wait, look at Check 7: "financial document -> invoice or budget". "financial or money-data table (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures), and a handwritten list of budget categories and dollar amounts... is budget, not form".
- This table has "Pricing", "Price Gaps", "Promotion Incidence", "Promo Index". It's a pricing and share analysis table. Is it a budget? No, it's historical/current data ("As of 6/15/98", "1H 1998", "98 O.B.", "FULL YR 1997"). It's not a budget (planning) or invoice.
- What about Check 9: "presentation". "Slide/overhead layouts... chart-per-page deck look". The page has a title "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION", a table, and footnotes. The three black dots at the top (when rotated) look like binder holes, but could also be artifacts. Wait, if it's a slide, it would be a presentation. But the rule says: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- So if it's a standalone chart, it's a form.
- Let's re-evaluate "form". "administrative form -> form". "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data".
- Is this generic administrative/log data? It's a business performance dashboard. In the tobacco archive, these are often internal business reports. If it's a standalone table of business data, and it doesn't fit invoice/budget/spec/scientific_report, it falls back to form.
- Wait, is there any other category?
- Let's check the labels again: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
- Could it be a memo? No TO/FROM/RE.
- Could it be a letter? No.
- Could it be a scientific_report? No running prose.
- Could it be a specification? No "shall/must" or product formulation.
- So it must be form or presentation.
- Rule for presentation: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." This is a very specific rule. "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Therefore, this page, being a standalone chart/table of values (trigger points, shares, pricing), must be classified as a form (check 10).
- Let's verify the "generic administrative/log data" part. The rule says "a standalone labeled chart is a form only when it holds generic administrative/log data". This chart holds market share and pricing data. Is that generic administrative/log data? In the context of these 16 labels, business data tables that aren't financial (invoice/budget) or scientific (research) or specifications often fall into "form" as a catch-all for structured data tables in this classification scheme, or perhaps it's considered a form because it's a structured data capture/report template.
- Actually, look at Check 10 again: "This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a financial/money chart is budget (check 7), and a research-measurement chart is scientific_report (check 13)".
- If it's not spec, budget, or scientific_report, and it's a standalone chart, it's a form. The "only when" might be a condition for the *exception*, meaning if it's NOT those special types, it's a form. "a standalone labeled chart is a form [by default], only when it holds [special types] is it [special type]". Wait, the wording is "a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of... is specification...". This implies if it holds market share data, it might NOT be a form?
- But there is no other category for a business performance table!
- Let's re-read carefully: "a standalone labeled chart is a form only when it holds generic administrative/log data". If this chart holds business performance data (shares, pricing), is it a form?
- Maybe it's a presentation? "Slide/overhead layouts... chart-per-page deck look". The title "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION" strongly suggests it's a slide from a presentation deck ("For Discussion"). The three black dots at the top are likely binder holes from a physical report, or artifacts. But wait, if it's a slide, the rule says "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." This rule explicitly demotes standalone charts to form.
- Let's look at the black dots. They are three large black circles. In slide scans, sometimes there are artifacts. But here they look like binder punch holes. If it's a page from a bound report, it's not a slide.
- If it's a page from a report, and it's just a table, and it's not scientific_report (no prose), not budget (not planning/money tracking primarily, though it has pricing), not invoice... what is it?
- In many document classification tasks for this archive, internal business data tables like this are classified as `form` (as a structured data document) or `presentation` (if it's a slide). The rule "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)" is very explicit. I will follow this rule.
- Wait, is there any chance it's a `budget`? "financial or money-data table (price/value estimates...)" is budget. This table has "Pricing", "Price Gaps", "Promotion Incidence". But it's mostly "Share of Market", "Share of Segment". It's a performance trigger table, not a budget.
- Is it a `specification`? No.
- So `form` is the most logical fallback for a standalone data table that doesn't fit the other specific categories.
> Let's double check Check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
This is a definitive rule. The page is a standalone chart/table of values ("PM-USA PERFORMANCE TRIGGERS..."). Therefore, it is a form.
> Let's check the evidence for `form`:
- Standalone labeled data chart/table with rows (Share of Market, etc.) and numeric values (51.6, 52.4, etc.).
- No running narrative prose (rules out scientific_report).
- Not a financial bill or budget (rules out invoice/budget).
- Not a product spec (rules out specification).
- Rule explicitly states standalone charts are forms.
> Scratchpad:
- file_folder: no — has a bold title and a large data table.
- handwritten: no — typed text and numbers.
- fax: no — no fax header.
- questionnaire: no — not a survey.
- resume: no.
- scientific_publication: no — no journal identifier.
- financial (invoice/budget): no — it's a performance trigger table with market share and pricing data, not a bill, voucher, or internal budget planning document. The pricing data is part of a performance dashboard, not a financial statement or budget.
- specification: no — no "shall/must" language, no material safety data, no product formulation.
- presentation: no — although it has a title "FOR DISCUSSION", the rule states "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." The page is a dense data table, not a sparse slide layout.
- form: yes — it is a standalone labeled data chart/table with rows of business metrics (shares, pricing) and numeric values. Per check 10, a standalone labeled chart that is not a spec, budget, or scientific_report is a form.
- email: no — no mail header.
- memo/letter: no — no correspondence structure.
- news_article: no — no masthead.
- advertisement: no — not a marketing ad.
> Runner-up: presentation, ruled out because the page is a standalone chart/table of values, and the rules explicitly state "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> Wait, could it be `scientific_report`? "A technical/project status report whose content is primarily technical... even when it embeds a budget-vs-actual cost section". This is not a technical status report. It's a business performance table. No running prose. Check 13 requires running narrative prose.
> So `form` is the correct label.
> Let's refine the scratchpad.
- Pre-scan: No mail-client header. No masthead. Bates number 2071860450. Three black dots (likely binder holes or artifacts, but text is dense table).
- Check 1: file_folder. No, has title and table.
- Check 2: handwritten. No.
- Check 3: fax. No.
- Check 4: questionnaire. No.
- Check 5: resume. No.
- Check 6: scientific_publication. No journal ID.
- Check 7: financial. No, it's a performance trigger table (shares, pricing indices), not an invoice, budget, or financial statement.
- Check 8: specification. No.
- Check 9: presentation. No, "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Check 10: form. Yes, standalone labeled data chart/table with numeric values.
- Check 11: correspondence. No.
- Check 12: news_article. No.
- Check 13: scientific_report. No running prose.
- Check 14: advertisement. No.
> Final label: form.

---

## presentation → memo (1 errors)

### `rvl_cdip__presentation__0013.png`
**Expected:** `presentation` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> Image analysis:
- Top center: handwritten "DLG", "xJNT" (or similar), "First draft for April 29. Please add."
- Below that: "Lance"
- Bottom right: vertical text "526001380" (Bates number)
- Bottom edge: black bars (scan artifact or folder tab edge?)
- Left side: some diagonal lines, maybe a pen mark or artifact.
> Let's look at the content:
- Handwritten note: "DLG", "xJNT" (or similar), "First draft for April 29. Please add."
- Typed text: "Lance"
- Bates number: "526001380"
> Wait, is this a handwritten page?
Most of the content is freeform handwriting? No, there's very little text. "First draft for April 29. Please add." is typed. "Lance" is typed. "DLG" and "xJNT" are handwritten.
Actually, the page is mostly blank.
Let's check the checks.
> Check 1: file_folder
- Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card.
- "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
- Here we have a note: "First draft for April 29. Please add." and "Lance". This is a note. So not file_folder.
- Wait, what about folder-tab pages? "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... The label IS filing metadata... so it is NOT a 'topical title' for this check."
- The bottom has black bars. Could this be a folder tab? The black bars are at the bottom. The text is at the top. The Bates number is on the right.
- If it's a folder tab, the label would be something like "NEWTROL", "Litigation Content". Here the text is "First draft for April 29. Please add." and "Lance". This is a note, not a filing label.
- So not file_folder.
> Check 2: handwritten
- Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template.
- "A typed page with only a signature, stamp, or margin note is not handwritten."
- Here we have a typed note "First draft for April 29. Please add." and "Lance", with some handwritten initials "DLG". This is mostly typed, or rather, a typed page with a handwritten note. Wait, the note itself is typed: "First draft for April 29. Please add." The handwriting is just "DLG" and maybe "xJNT".
- So not handwritten.
> Check 3: FAX TRANSMISSION SHEET
- No fax header.
> Check 4: SURVEY INSTRUMENT
- No.
> Check 5: resume
- No.
> Check 6: scientific_publication
- No.
> Check 7: financial document
- No.
> Check 8: specification
- No.
> Check 9: presentation
- "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation (this check), not file_folder (check 1)."
- "Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center (e.g., lower-right) rather than in running paragraphs, points to a photographed slide/overhead — presentation — even if the sparse text sounds like a research title; don't let a technical-sounding phrase pull this toward scientific_report when the layout itself is sparse and slide-like rather than a prose page."
- Wait, the text is at the top: "First draft for April 29. Please add." and "Lance". The black bars are at the bottom.
- Is this a presentation? "A near-blank cover or title page... mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation".
- But this is a note: "First draft for April 29. Please add." to "Lance". This looks like a memo or a note.
- Let's check Check 11: CORRESPONDENCE -> email, memo, or letter.
- memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose.
- "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels"
- Here we have "Lance" (name) and "First draft for April 29. Please add." (prose/note).
- Is it a memo? "Lance" is a name. "First draft for April 29. Please add." is the message.
- Let's re-read Check 11: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."
- Here we have "Lance" (name, no title given, but maybe internal), "First draft for April 29. Please add." (prose, has date "April 29").
- Wait, is "Lance" the addressee or the sender? Usually "Lance" at the top or middle could be the addressee.
- Let's look at the layout:
  - Handwritten: "DLG", "xJNT"
  - Typed: "First draft for April 29. Please add."
  - Typed: "Lance"
- This is a very short internal note. "Lance" is the addressee. "First draft for April 29. Please add." is the message.
- Is it a memo? "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo even without literal TO:/FROM: labels". Here we don't have the internal title/division for Lance, but we have the name and date and prose.
- Wait, what about letter? "A dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block." Lance is likely an internal person (Lance is a common first name, often used in tobacco industry docs, e.g., Lance Hill, Lance... wait, Lance is a first name). Without an external address or "Dear", it's not a letter.
- Let's check if there's any other category.
- What about handwritten? "Most of the content is freeform handwriting... NOT on a printed template." Here, the text "First draft for April 29. Please add." is typed. "Lance" is typed. The handwriting is just "DLG" and "xJNT". So not handwritten.
- What about file_folder? "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note." This page carries a note. So not file_folder.
- Is it a presentation? "A near-blank cover or title page... mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation". But this is a note to Lance, not a cover page. The black bars at the bottom might be scan artifacts from a slide, but the text is a memo/note. Wait, "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation". The black bars are at the bottom. The text is at the top. The text is "First draft for April 29. Please add." and "Lance". This doesn't look like a slide. It looks like a scanned piece of paper with a note on it. The black bars at the bottom could be the edge of the paper or a folder tab. If it's a folder tab, it's file_folder. But the text is a note, not a filing label.
- Let's reconsider the black bars. "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... The black bar is the photographed folder body/tab edge". If this is a folder tab, the label would be the filing label. But the text is "First draft for April 29. Please add." which is not a filing label. So it's not a folder tab.
- The black bars are likely just scan artifacts or the edge of the document.
- Let's look at Check 11 again: memo.
- "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."
- Here we have "Lance" (name), "April 29" (date), "First draft for April 29. Please add." (prose). This fits the "dated internal note addressed to a named person... with memo-style prose" description. Even without the explicit title, "Lance" is an internal name.
- Wait, is there any other check?
- Check 2: handwritten. "A typed page with only a signature, stamp, or margin note is not handwritten." This page is a typed page with a margin note ("DLG", "xJNT") and typed text ("First draft...", "Lance"). So not handwritten.
- Check 1: file_folder. "A page is NOT file_folder if it carries any real content — ... or a note." This carries a note. So not file_folder.
> Let's carefully evaluate if this is a memo.
The text is:
DLG (handwritten)
xJNT (handwritten)
First draft for April 29. Please add. (typed)
Lance (typed)
> This is a short internal note to Lance. "First draft for April 29. Please add."
It has a date ("April 29"), a named addressee ("Lance"), and prose ("First draft for April 29. Please add.").
According to Check 11: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."
Here we have name ("Lance"), date ("April 29"), prose ("First draft for April 29. Please add."). We don't have the internal title/division explicitly, but "Lance" is an internal name. The rule says "addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... IS a memo even without literal TO:/FROM: labels". It also says "internal names + titles + date + prose, with no salutation or closing, is a memo header."
Actually, the example says: "Mr. R. J. Smith, Manager - Hanmer Division" from "T. P. Pettigrew...". Here we just have "Lance". Is "Lance" enough?
"A dated note addressed to a bare name with an honorific (e.g. 'Mr. T. E. Sandefur:') — no internal title/division, no TO:/FROM:/RE:/SUBJECT: block, no 'Dear ...' salutation, and no closing signature — is a letter (external addressee), not a memo."
Wait! "A dated note addressed to a bare name with an honorific ... is a letter (external addressee), not a memo."
What if it's just a bare name without an honorific? "Lance" is a bare name.
If it's a bare name, is it a letter or a memo?
"letter: ... OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."
If "Lance" is an external person, it's a letter. If "Lance" is an internal person, it's a memo.
How to tell internal vs external? "The by-name memo rule requires an explicit INTERNAL TITLE/DIVISION in the address line; do not infer internal vs. external from pronoun usage in the prose ('our', 'we', 'my')."
Here, there is NO internal title/division in the address line. The address line is just "Lance".
Therefore, by the strict rule: "A dated note addressed to a bare name with an honorific (e.g. 'Mr. T. E. Sandefur:') — no internal title/division, no TO:/FROM:/RE:/SUBJECT: block, no 'Dear ...' salutation, and no closing signature — is a letter (external addressee), not a memo."
Wait, the rule says "addressed to a bare name with an honorific". What if it's just a bare name without an honorific? "Lance" has no honorific.
But the rule also says: "The by-name memo rule requires an explicit INTERNAL TITLE/DIVISION in the address line". Since there is no internal title/division, it CANNOT be a memo by the by-name rule.
So it must be a letter? Or is it something else?
Wait, if it's not a memo and not a letter (because no external address, no salutation, no closing), what is it?
Let's re-read Check 11:
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
"A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... IS a memo even without literal 'TO:/FROM:' labels"
"letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."
If it's addressed to "Lance" (bare name, no title, no external address, no salutation, no closing), it doesn't fit the memo rule (no internal title) and doesn't fit the letter rule (no external address, no salutation, no closing, and "Lance" is likely internal but we can't prove it's external).
Wait, "A dated note addressed to a bare name with an honorific ... is a letter (external addressee), not a memo." This implies that if it's a bare name WITHOUT an honorific, and no internal title, it might still be classified based on other evidence, or maybe it's just a note. But "note" is not a category. The categories are email, memo, letter.
Is there any other category?
What about handwritten? "Most of the content is freeform handwriting... NOT on a printed template." The text "First draft for April 29. Please add." is typed. "Lance" is typed. The handwriting is just "DLG" and "xJNT". So not handwritten.
What about file_folder? "A page is NOT file_folder if it carries any real content — ... or a note." This carries a note.
What about presentation? "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note (e.g. 'Internal Communication 2000 Plan' with 'Draft for discussion'), a single-word/short-phrase heading with no subtitle at all (e.g. 'RECOMMENDATIONS' centered on an otherwise blank page), a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."
Could this be a presentation? "First draft for April 29. Please add." is a note, not a title. "Lance" is a name.
Wait, look at the black bars at the bottom. "Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center (e.g., lower-right) rather than in running paragraphs, points to a photographed slide/overhead — presentation".
The text is at the top center: "First draft for April 29. Please add." and "Lance". The black bars are at the bottom. The Bates number is on the right.
This doesn't match the slide artifact signal perfectly (text is top center, not lower-right).
Let's reconsider the content. It's a very short typed note with some handwritten initials.
Is it a memo? In many tobacco industry documents, short internal notes like this are classified as memos. The rule says "internal names + titles + date + prose, with no salutation or closing, is a memo header." Here we have "Lance" (internal name), "April 29" (date), "First draft for April 29. Please add." (prose). Even without the explicit title, it's an internal note. The strict rule "requires an explicit INTERNAL TITLE/DIVISION" might be for distinguishing from external letters, but if there's no external address and no salutation, and it's an internal name, it's a memo.
Actually, let's look at the example: "Mr. R. J. Smith, Manager - Hanmer Division" from "T. P. Pettigrew...". Here we just have "Lance".
If I have to choose between memo and letter: "letter: ... OR a dated note addressed to a named EXTERNAL person ... with prose and no TO:/FROM: block." Since we don't know Lance is external, and there's no external address, it's more likely internal. Internal notes without formal headers are memos.
Wait, is there any other label?
What about "handwritten"? The prompt says: "A typed page with only a signature, stamp, or margin note is not handwritten." This page is a typed page with a margin note ("DLG", "xJNT") and typed text. So not handwritten.
What about "form"? No fields.
What about "invoice"? No.
> Let's re-read the memo rule carefully:
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation). Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header. The by-name memo rule requires an explicit INTERNAL TITLE/DIVISION in the address line; do not infer internal vs. external from pronoun usage in the prose ('our', 'we', 'my'). A dated note addressed to a bare name with an honorific (e.g. 'Mr. T. E. Sandefur:') — no internal title/division, no TO:/FROM:/RE:/SUBJECT: block, no 'Dear ...' salutation, and no closing signature — is a letter (external addressee), not a memo."
> If the rule strictly requires an explicit INTERNAL TITLE/DIVISION for the by-name memo rule, and this page has NO internal title/division (just "Lance"), then it CANNOT be a memo by the by-name rule.
And it CANNOT be a letter by the by-name rule because "Lance" is not an external person with an honorific (it's just a first name, no "Mr.", no external address).
So what is it?
Maybe it's not a memo or letter.
Could it be a presentation? "A near-blank cover or title page ... with only a bold headline title and perhaps a subtitle, date, or 'Draft' note ... is a presentation". "First draft for April 29. Please add." is a "Draft" note. "Lance" could be a title? No.
Could it be file_folder? "A page is NOT file_folder if it carries any real content — ... or a note." This carries a note. But wait, is the note "real content"? Yes.
What about handwritten? "Most of the content is freeform handwriting...". Here, the content is mostly blank space, with a small typed note and some handwritten initials. "Scan noise is not handwriting: on a heavily degraded, noisy scan, don't let illegibility read as 'majority handwritten.' If the dominant recognizable elements are a stamp, faint archival text, or an ID/number, with only a small rotated handwritten annotation on the side, classify by the stamp/identifier (often file_folder), not handwritten — handwriting must legibly make up most of the page's actual content, not just be the only thing you can partly read on a noisy scan."
Here, the dominant recognizable elements are the typed note "First draft for April 29. Please add." and "Lance", and the Bates number "526001380". The handwriting is just "DLG" and "xJNT". So not handwritten.
> If it's not file_folder, not handwritten, not memo, not letter... what is it?
Let's reconsider file_folder. "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
Is "First draft for April 29. Please add." a note? Yes. So not file_folder.
> Let's reconsider presentation. "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note (e.g. 'Internal Communication 2000 Plan' with 'Draft for discussion'), a single-word/short-phrase heading with no subtitle at all (e.g. 'RECOMMENDATIONS' centered on an otherwise blank page), a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."
The page is mostly empty space. It has a "Draft" note ("First draft for April 29. Please add."). It has a name "Lance". It has black bars at the bottom (scan artifact for slides?).
"Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center (e.g., lower-right) rather than in running paragraphs, points to a photographed slide/overhead — presentation — even if the sparse text sounds like a research title; don't let a technical-sounding phrase pull this toward scientific_report when the layout itself is sparse and slide-like rather than a prose page."
The black bars are at the bottom. The text is at the top. The text is sparse. This could be a photographed slide/overhead that is mostly blank, with a note on it.
But the text is "First draft for April 29. Please add." and "Lance". This is a memo/note, not a slide title.
Wait, if it's a slide, it would be a presentation. But the text is clearly a memo note.
Is there any chance this is a memo?
"A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... IS a memo even without literal 'TO:/FROM:' labels"
If the rule strictly requires the internal title, and it's missing, maybe it's classified as a letter? "A dated note addressed to a named EXTERNAL person ... with prose and no TO:/FROM: block." But we don't know Lance is external.
Actually, in the tobacco archive, short internal notes like this are often classified as memos. The instruction says: "The by-name memo rule requires an explicit INTERNAL TITLE/DIVISION in the address line; do not infer internal vs. external from pronoun usage in the prose". This implies that if there is NO internal title/division, and it's a bare name, it might be classified as a letter (assuming external) OR it might be that the rule is just giving examples.
Wait, "A dated note addressed to a bare name with an honorific (e.g. 'Mr. T. E. Sandefur:') — no internal title/division, no TO:/FROM:/RE:/SUBJECT: block, no 'Dear ...' salutation, and no closing signature — is a letter (external addressee), not a memo."
This specifically says "with an honorific". "Lance" has no honorific. So this specific rule doesn't apply.
What about just a bare name without an honorific? The rule doesn't explicitly say. But since it's an internal name (Lance is a common first name in this archive, e.g., Lance Hill, Lance...), and there's no external address, no salutation, no closing, it's an internal note. Internal notes are memos. The strict requirement for "NAME + INTERNAL TITLE/DIVISION" might be to distinguish from external letters, but if there's no external address and no salutation, it's internal. I will classify it as memo.
> Wait, look at the text again:
"DLG" (handwritten)
"xJNT" (handwritten)
"First draft for April 29. Please add." (typed)
"Lance" (typed)
> This is a note from someone (initials DLG) to Lance. "First draft for April 29. Please add."
This is a classic internal memo/note. I'll go with memo.
> Let's check if there's any other possibility.
Could it be a form? No.
Could it be an email? No mail header.
Could it be a scientific report? No.
> I'll go with memo.
Evidence: Typed note "First draft for April 29. Please add." addressed to "Lance" with a date ("April 29") and prose, no external address, no salutation, no closing. Fits the internal note memo definition.
> Wait, is "Lance" the sender or receiver? Usually, the name at the bottom or middle is the addressee. "Lance" is below the text. So it's addressed to Lance.
Sender initials: DLG.
This is a memo.
> Let's double check check 11:
"memo: ... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."
Here we have "Lance" (name), "April 29" (date), "First draft for April 29. Please add." (prose). Even without the explicit title, it's an internal name + date + prose. I will classify as memo.
> Runner-up: file_folder, ruled out because the page carries a real note ("First draft for April 29. Please add."), not just filing metadata.
Another runner-up: handwritten, ruled out because the dominant content is typed text and a typed note, with only small handwritten initials.
> Final label: memo.

---

## questionnaire → scientific_report (1 errors)

### `rvl_cdip__questionnaire__0005.png`
**Expected:** `questionnaire` | **Predicted:** `scientific_report`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header: None.
- Masthead/running head: "Bellomy Research" logo at the top. Address at the bottom: "108 Cambridge Plaza Drive • Winston-Salem, NC 27104". No journal masthead. No newspaper masthead.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a title "AROMA MINI GROUPS", a logo "Bellomy Research", "Prepared For: R. J. REYNOLDS TOBACCO COMPANY", "November 1991", and a Bates number "50918 7883". It has real content (title, prepared for, date).
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: There is a handwritten note "File Props" (or similar) near the top right. But the rest is typed.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No fax header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: "AROMA MINI GROUPS" sounds like a research topic, but there are no questions, scales, or survey instructions visible on this page. It looks like a cover page.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No biographical info.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal name, volume, issue, page range.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: No financial data, line items, or money tracking.
    *   Result: not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: No material safety data, product formulation, or "shall/must" language.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: The page is mostly blank space. It has a logo ("Bellomy Research"), a title ("AROMA MINI GROUPS"), "Prepared For: R. J. REYNOLDS TOBACCO COMPANY", "November 1991", and a Bates number.
    *   Let's look at the rules for presentation (check 9): "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."
    *   Wait, is this a presentation cover? "Bellomy Research" is a consulting/research firm. "AROMA MINI GROUPS" is the title. "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991". This looks like the cover page of a report or a presentation deck.
    *   Let's re-read check 9 carefully. "Slide/overhead layouts... a deck title or section-divider page, a meeting/program/speaker cover page... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date... is a presentation".
    *   Wait, is it a scientific_report title page? "Technical-study title pages: a title page naming a specific study or methodology with a date — e.g. 'TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter... / November 28, 1966' — is scientific_report (check 13), not presentation".
    *   "AROMA MINI GROUPS" is a title. "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991". This looks like a cover page for a report or a presentation.
    *   Let's look at check 13: "Original research write-up -> scientific_report". "A lab or technical study title page with authors and an internal affiliation and no journal identifiers." This page has "Bellomy Research" (external affiliation) and "Prepared For: R.J. Reynolds". It doesn't look like a scientific report title page with authors. It looks like a consulting report cover or a presentation cover.
    *   Let's look at the "presentation" definition again. "Slide/overhead layouts... a deck title or section-divider page... A near-blank cover or title page... is a presentation".
    *   However, often these "Prepared For" pages are covers of reports (scientific_report or just a report). But the label set doesn't have "report_cover" except under presentation or scientific_report.
    *   Wait, check 9 says: "Technical-study title pages: a title page naming a specific study or methodology with a date... is scientific_report (check 13), not presentation". "AROMA MINI GROUPS" is a specific study/topic. But is it a "technical-study title page naming a specific experimental method/study"? "Aroma Mini Groups" sounds like a focus group or research study.
    *   Let's look at the layout. It's very sparse. Logo at top, title in middle, "Prepared For" at bottom right. This is classic presentation deck cover or report cover.
    *   If it's a report cover, and it's not a scientific report (no authors, no running prose), what is it?
    *   Let's reconsider check 9: "a deck title or section-divider page... A near-blank cover or title page... is a presentation".
    *   Let's look at the "presentation" label description: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement... or a photographic slide image".
    *   This page is a "deck title" or "cover page" for a document prepared by Bellomy Research for RJ Reynolds. It is very sparse.
    *   Is it a scientific_report? Check 13 requires "Running narrative prose...". This page has no prose. So it's not scientific_report.
    *   Is it a form? No fields.
    *   Is it a file_folder? No, it has a title "AROMA MINI GROUPS" and "Prepared For...". Check 1 says "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only." and "A prominent topical heading always counts as real content... it is a cover/title page, section divider, or photographic slide (presentation, check 9)". So "AROMA MINI GROUPS" makes it a presentation cover/divider.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: No fields, boxes, checkboxes.
    *   Result: not this check.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: No TO/FROM/RE header, no salutation, no closing.
    *   Result: not this check.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: No masthead, no news typography.
    *   Result: not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: No running prose. Just a title page. Check 13 says "Requires running prose — a page that is only labeled field-value entries... is a filled form... not a scientific report." A title page alone without prose is not a scientific report. Wait, "Technical-study title pages... is scientific_report". But "AROMA MINI GROUPS" doesn't name a specific experimental method like "Determination And Reporting Of Total Particulate Matter...". It's a bit ambiguous. However, the layout is extremely sparse, typical of a presentation cover or a report cover. Since there is no prose, it can't be scientific_report (which requires running narrative prose). Wait, check 13 says "Also scientific_report: a technical-study title page naming a specific experimental method/study". "Aroma Mini Groups" is a study name. But is it a "technical-study title page"? Usually scientific reports have authors. This has "Bellomy Research".
    *   Let's look at check 9 again. "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation". This fits perfectly. "AROMA MINI GROUPS" is the bold headline title. "November 1991" is the date. "Prepared For: R. J. REYNOLDS..." is extra info. The page is mostly empty space.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: No product imagery, slogans, Surgeon General warning.
    *   Result: not this check.
> **Conclusion:**
The page is a near-blank cover page with a title "AROMA MINI GROUPS", a logo, and "Prepared For" info. This fits the definition of a presentation cover/deck title page (Check 9). The sparse layout, title, and date are characteristic. It is not a file_folder because it has a topical heading ("AROMA MINI GROUPS") and real content (Prepared For, Date). It is not a scientific_report because it lacks running prose and authors (it's a consulting firm cover).
> Let's double check Check 9 vs Check 1.
Check 1: "A page is NOT file_folder if it carries any real content... A prominent topical heading always counts as real content... it is a cover/title page, section divider, or photographic slide (presentation, check 9)".
The heading "AROMA MINI GROUPS" is prominent. So it's not file_folder.
It matches Check 9: "A near-blank cover or title page — mostly empty space with only a bold headline title... is a presentation".
> Final check: Is it a scientific_report title page?
Check 13: "Technical-study title pages: a title page naming a specific study or methodology with a date... is scientific_report (check 13), not presentation".
Example given: "TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter, Water In Total Particulate Matter, And Nicotine In Cigarette Smoke / November 28, 1966".
My page: "AROMA MINI GROUPS / Prepared For: R. J. REYNOLDS TOBACCO COMPANY / November 1991".
"Aroma Mini Groups" is a study name (focus groups on aroma). But the layout is very sparse, typical of a presentation or a consulting report cover. The instructions say: "Technical-study title pages... is scientific_report... not presentation, even when it is sparse or printed slide-style on a dark background: the title names an experimental study, not a deck/program/section."
"Aroma Mini Groups" is likely a research study (focus groups). But does it name an "experimental method/study"? It's a bit generic.
However, look at the layout. "Bellomy Research" logo. "Prepared For: R.J. Reynolds". This is a consulting deliverable cover.
If it's a consulting report cover, and there's no prose, what is it?
The categories are limited. If it's a cover page for a report, and the report isn't a scientific publication...
Wait, if it's a cover page for a scientific report, is the cover page itself a scientific_report?
Check 13: "Also scientific_report: a technical-study title page naming a specific experimental method/study".
If "Aroma Mini Groups" is the study, maybe it's scientific_report?
But scientific_report requires "Running narrative prose". The title page itself doesn't have prose. But the category is for the document. If the document is a scientific report, the title page is part of it.
However, the instructions say: "Judge each page by its FUNCTION... a page full of technical data can still be a form...".
If this page is just a cover, and the rest of the document (not shown) is the report... I have to judge *this page*.
Check 9: "a deck title or section-divider page... A near-blank cover or title page... is a presentation".
Check 13: "Requires running prose — a page that is only labeled field-value entries... is a filled form... not a scientific report."
If this page has no prose, it cannot be scientific_report based on the "Requires running prose" rule, unless it falls under the exception "Technical-study title page...".
But "Aroma Mini Groups" is not a detailed method name like the example. It's a short title.
Also, the layout is extremely sparse. "mostly empty space with only a bold headline title". This is the exact definition of presentation (Check 9).
"A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note (e.g. 'Internal Communication 2000 Plan' with 'Draft for discussion'), a single-word/short-phrase heading with no subtitle at all (e.g. 'RECOMMENDATIONS' centered on an otherwise blank page), a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."
> The page has:
- Logo
- Title: AROMA MINI GROUPS
- Prepared For: R. J. REYNOLDS TOBACCO COMPANY
- Date: November 1991
- Bates number
- Handwritten note "File Props"
> This is a near-blank cover page. It fits Check 9 perfectly.
> One detail: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".
Does "AROMA MINI GROUPS" name a specific study or methodology? "Mini groups" is a methodology (focus groups).
But the example for scientific_report title page is very descriptive: "Determination And Reporting Of Total Particulate Matter...".
"Aroma Mini Groups" is short.
Also, the "Prepared For" block is very typical of a presentation deck or a consulting report cover. In the tobacco archive, these Bellomy Research documents are often market research reports or presentations.
If I have to choose between presentation and scientific_report for a title page:
- Presentation: "near-blank cover... mostly empty space... bold headline title".
- Scientific_report: "technical-study title page naming a specific study or methodology".
> Let's look at the "presentation" caveat: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation, even when it is sparse or printed slide-style on a dark background: the title names an experimental study, not a deck/program/section."
"Aroma Mini Groups" -> Mini groups are a research method (focus groups). So it names a methodology/study.
However, is this page *only* the title page? Yes.
If I classify it as presentation, I am saying it's a deck cover.
If I classify it as scientific_report, I am saying it's a title page for a report.
But scientific_report requires "Running narrative prose". The check 13 definition starts with "Running narrative prose...". Then it says "Also scientific_report: ... a technical-study title page...".
So a technical-study title page *is* a scientific_report.
Is "Aroma Mini Groups" a technical-study title page?
Bellomy Research is a market research firm. "Aroma Mini Groups" is likely a market research study (focus groups on aroma). Market research reports are often scientific_reports in this archive (if they contain data/prose) or presentations (if they are decks).
But this is just the cover.
Let's look at the "presentation" definition again. "a deck title or section-divider page... A near-blank cover or title page... is a presentation".
The page is *very* near-blank.
The "technical-study title page" exception for scientific_report seems to apply to pages that look like report covers but have the specific descriptive title.
"Aroma Mini Groups" is a bit generic.
Also, the handwritten note "File Props" suggests it's a file copy.
Let's consider the source. Bellomy Research prepared this for RJ Reynolds. This is likely a market research report or presentation.
If it's a presentation deck cover, it's presentation.
If it's a report cover, and the report is a scientific report, the title page is scientific_report.
But I only have this page.
Check 9 says: "A near-blank cover or title page — mostly empty space with only a bold headline title... is a presentation".
This page is mostly empty space.
The exception for scientific_report is "Technical-study title pages: a title page naming a specific study or methodology with a date".
"Aroma Mini Groups" + "November 1991".
Is it a "technical-study"? Market research is technical in this archive.
But the layout is classic presentation cover (sparse, logo top, title center, prepared for bottom).
Actually, many consulting reports have this cover.
Let's look at the label distribution: "news_article and presentation are historically under-predicted". This suggests I should be careful not to miss presentation.
The page is extremely sparse. "mostly empty space".
I will go with **presentation**.
> Wait, let's look at Check 1 again. "A prominent topical heading always counts as real content... it is a cover/title page, section divider, or photographic slide (presentation, check 9)".
So if it has a heading, it's not file_folder. It falls to presentation (check 9) or scientific_report (check 13) or form (check 10) etc.
Since it has no fields (not form), no prose (not scientific_report body), no financials (not budget/invoice).
It's either presentation or scientific_report (title page).
The "technical-study title page" exception in check 13 is specific: "naming a specific study or methodology with a date — e.g. 'TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter... / November 28, 1966'".
My page: "AROMA MINI GROUPS / Prepared For: R. J. REYNOLDS TOBACCO COMPANY / November 1991".
The title "AROMA MINI GROUPS" is short. The example title is long and descriptive.
Also, the "Prepared For" block is very corporate/presentation-like.
I'll bet on **presentation**.
> One more check: Is it a letter? No.
Is it a memo? No.
> Final decision: presentation.
Evidence: Near-blank page, mostly empty space, bold headline title "AROMA MINI GROUPS", date "November 1991", "Prepared For" block. Fits Check 9 definition of a near-blank cover/title page or deck cover.
> Wait, looking closely at the image...
Top: Bellomy Research logo.
Top right: Handwritten "File Props" (or similar).
Center: "AROMA MINI GROUPS".
Bottom right: "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991".
Bottom right vertical: "50918 7883" (Bates number).
Bottom: Address "108 Cambridge Plaza Drive...".
> This is a cover page.
Check 9: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date... is a presentation".
This matches perfectly.
> Runner-up: file_folder. Ruled out because "AROMA MINI GROUPS" is a prominent topical heading, which counts as real content, making it a cover/title page (presentation), not a filing label.
Another runner-up: scientific_report. Ruled out because the page lacks running narrative prose and the title is short/generic compared to the specific "technical-study title page" example, and the layout is sparse/deck-like. Actually, the rule says "Requires running prose... Also scientific_report: a technical-study title page...". But the "near-blank cover" rule in Check 9 is very strong here. "A near-blank cover or title page... is a presentation". The exception for scientific_report is for "Technical-study title pages...". "Aroma Mini Groups" is a study, but the page is a "near-blank cover". The instructions say "Once an earlier check matches, later checks do not override it."
Check 9 comes before Check 13.
Check 9: "A near-blank cover or title page... is a presentation".
Does Check 9 match? Yes, "mostly empty space with only a bold headline title".
Does Check 13 override? No, "Once an earlier check matches, later checks do not override it."
Wait, Check 9 has a caveat: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".
So if it IS a technical-study title page, it's scientific_report.
Is "AROMA MINI GROUPS" a technical-study title page naming a specific study or methodology?
"Mini groups" is a methodology (focus groups). "Aroma" is the topic.
So it names a study/methodology.
And it has a date "November 1991".
So it fits the caveat of Check 9 -> scientific_report.
> Let's re-evaluate.
Check 9 caveat: "Technical-study title pages: a title page naming a specific study or methodology with a date — e.g. 'TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter, Water In Total Particulate Matter, And Nicotine In Cigarette Smoke / November 28, 1966' — is scientific_report (check 13), not presentation, even when it is sparse or printed slide-style on a dark background: the title names an experimental study, not a deck/program/section."
> My page: "AROMA MINI GROUPS". "Mini groups" is a research methodology (focus groups). "Aroma" is the subject.
So it names a study/methodology.
Date: November 1991.
So it fits the caveat. It should be scientific_report.
> BUT, scientific_report requires "Running narrative prose".
Check 13: "Running narrative prose with objectives, methods, results, or discussion... Requires running prose — a page that is only labeled field-value entries... is a filled form... not a scientific report."
"Also scientific_report: ... a technical-study title page naming a specific experimental method/study".
So a technical-study title page IS a scientific_report, even if it doesn't have prose (because it's just the title page).
> So is "AROMA MINI GROUPS" a technical-study title page?
Bellomy Research is a research firm. "Aroma Mini Groups" is a research study (focus groups on aroma).
So yes, it is a title page for a technical study.
Therefore, it is scientific_report.
> Wait, is there any other category?
What about "presentation"?
The caveat says: "Technical-study title pages ... is scientific_report (check 13), not presentation".
So if it's a technical-study title page, it's scientific_report.
> Let's look at the "presentation" definition again.
"a deck title or section-divider page, a meeting/program/speaker cover page... A near-blank cover or title page... is a presentation".
EXCEPTIONS: "a cover/title page that names a survey... is questionnaire... and a technical-study title page naming a specific experimental method/study is scientific_report".
> So the decision is: Is "AROMA MINI GROUPS" a "technical-study title page naming a specific experimental method/study"?
"Mini groups" = focus groups = experimental method/study.
"Aroma" = specific topic.
So yes.
It is scientific_report.
> Let's check the labels.
scientific_report: "Original research write-up". A title page for an original research write-up (the study) is part of that category.
> Let's reconsider the "presentation" label.
Often, these Bellomy Research documents are market research reports. Market research reports are often classified as scientific_report in this archive if they are technical.
If it's a presentation deck, it would be presentation.
The layout is very sparse.
But the caveat is specific: "technical-study title page ... is scientific_report".
> Let's look at the handwritten note: "File Props". Maybe "File Copy"?
Bates number 50918 7883.
> If I have to choose between presentation and scientific_report.
The caveat in Check 9 explicitly pushes technical-study title pages to Check 13 (scientific_report).
"Aroma Mini Groups" is a study title.
So I will go with **scientific_report**.
> Wait, let's look at the "presentation" caveat again.
"Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".
Does "AROMA MINI GROUPS" name a specific study or methodology?
Yes, "Mini Groups" is a methodology (focus groups).
Does it have a date? Yes, "November 1991".
So it matches the caveat.
> Therefore, the label is scientific_report.
> One counter-argument: The page is just a cover. The actual report (with prose) is not here.
But the instructions say: "Judge each page by its FUNCTION...".
If this page is the title page of a scientific report, its function is to identify the report.
Check 13 says "Also scientific_report: a technical-study title page...". So the title page itself is classified as scientific_report.
> Final check: Is it a form? No.
Is it a file_folder? No, has title.
> I will go with scientific_report.
> Wait, looking at the image again.
"AROMA MINI GROUPS"
"Prepared For: R. J. REYNOLDS TOBACCO COMPANY"
"November 1991"
This looks like a cover for a report.
In the tobacco archive, market research reports (like from Bellomy Research) are often scientific_reports.
The title "AROMA MINI GROUPS" indicates the study.
> Let's refine the scratchpad.
> <scratchpad>
file_folder: no — the page has a prominent topical heading "AROMA MINI GROUPS", "Prepared For" block, and date, so it has real content, not just filing metadata.
handwritten: no — only a small handwritten note "File Props" (or similar) at the top right; the rest is typed.
questionnaire: no — no survey questions, scales, or instructions.
resume: no — no biographical info.
scientific_publication: no — no journal running head, volume, or issue.
invoice/budget: no — no financial data.
specification: no — no product data or "shall/must" language.
presentation: yes — the page is a near-blank cover with mostly empty space, a bold headline title "AROMA MINI GROUPS", and a date. However, check 9 has a caveat: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".
form: no — no fields or boxes.
email/memo/letter: no — no correspondence headers or structure.
news_article: no — no masthead or news typography.
scientific_report: yes — the page is a title page for a study ("AROMA MINI GROUPS", a focus group study on aroma) with a date ("November 1991"). Per check 9's caveat, a technical-study title page naming a specific study/methodology is scientific_report (check 13), overriding the presentation cover rule. Also, Bellomy Research is a research firm preparing a study for RJ Reynolds.
Runner-up: presentation, ruled out because the title "AROMA MINI GROUPS" names a specific research study/methodology (mini groups/focus groups) with a date, triggering the check 9 caveat that pushes it to scientific_report (check 13).
</scratchpad>
> Wait, is "Aroma Mini Groups" specific enough?
The example is "Determination And Reporting Of Total Particulate Matter...".
"Aroma Mini Groups" is short.
But "Mini Groups" is a methodology.
I'll stick with scientific_report.
> Actually, let's look at the "presentation" label usage. "news_article and presentation are historically under-predicted".
If this is a presentation cover, and I call it scientific_report, I might be wrong.
But the caveat is explicit. "Technical-study title pages ... is scientific_report".
If I'm not sure if it's a technical-study title page, I should look at the layout.
The layout is "sparse text placed off-center" -> no, it's centered/bottom-right.
"Scan-artifact signal: a solid black bar..." -> no black bar.
The page is clean.
> Let's consider "presentation" again.
"A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note ... is a presentation".
This fits perfectly.
The caveat: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report".
Is "AROMA MINI GROUPS" a technical-study title page?
It's a title page for a study.
But is it "technical"? Market research is technical in this context.
However, if I have to bet, "AROMA MINI GROUPS" is a study title.
So scientific_report.
> One detail: "Prepared For: R. J. REYNOLDS TOBACCO COMPANY".
This is a consulting deliverable.
Consulting deliverables are often reports (scientific_report) or presentations (presentation).
If it's a report cover, and the report is the document...
But I only have the cover.
If the cover is a "technical-study title page", it's scientific_report.
If it's a "deck cover", it's presentation.
"Aroma Mini Groups" sounds like a study name.
I'll go with scientific_report.
> Wait, looking at similar examples in the archive (mental check): Bellomy Research documents are often market research reports. Market research reports with data are scientific_reports. The title page is part of it.
So scientific_report is appropriate.
> Final decision: scientific_report.
> One more look at Check 9: "EXCEPTIONS: ... a technical-study title page naming a specific experimental method/study is scientific_report (check 13) — neither is a deck cover or section divider."
"Aroma Mini Groups" -> "Mini Groups" is the method. "Aroma" is the study topic.
So it is a technical-study title page.
Label: scientific_report.
> <scratchpad>
file_folder: no — page has prominent heading "AROMA MINI GROUPS", "Prepared For", date; not just filing metadata.
handwritten: no — only small handwritten annotation "File Props"; mostly typed.
questionnaire: no — no survey items or instructions.
resume: no — no career history.
scientific_publication: no — no journal identifier.
financial: no — no financial data.
specification: no — no product specs.
presentation: near-match — near-blank cover with title and date. BUT check 9 caveat: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".
form: no — no fields.
correspondence: no — no TO/FROM/salutation.
news_article: no — no masthead.
scientific_report: yes — title page for a study ("AROMA MINI GROUPS", a focus group study) with date "November 1991". Per check 9 caveat, technical-study title pages are scientific_report. Bellomy Research is a research firm.
Runner-up: presentation, ruled out because the title names a specific study/methodology ("Mini Groups"), triggering the check 9 caveat that classifies it as scientific_report.
</scratchpad>
<label>scientific_report</label>

---

## questionnaire → memo (1 errors)

### `rvl_cdip__questionnaire__0010.png`
**Expected:** `questionnaire` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> Document content:
Title: "GMR MARKETING QUESTIONS REGARDING BID RESPONSE"
Sections: Region Managers, Event Staffing, Training, Talent Salaries, Floating Clubs, Vehicle Rental, Agency Travel.
Content: Bullet points with questions and comments about a bid response (e.g., "You have proposed 5 Region Managers. How do you envision dividing their responsibilities?", "Estimates are well above expectations...", "Please provide a total cost for third party labor...").
Bottom right: Bates number "2083156178" rotated 90 degrees.
> Let's go through the checks:
> 1. IDENTIFIER-ONLY PAGE -> file_folder
No, there is a lot of body content (questions and comments). Not file_folder.
> 2. MAJORITY-HANDWRITTEN PAGE -> handwritten
No, it's typed text.
> 3. FAX TRANSMISSION SHEET -> form
No fax header.
> 4. SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
No, this is questions regarding a bid response, not a survey instrument for consumers.
> 5. PERSON'S CAREER HISTORY -> resume
No.
> 6. PUBLISHED EVIDENCE -> scientific_publication
No journal masthead or running head.
> 7. FINANCIAL DOCUMENT -> invoice or budget
It mentions costs, estimates, "total cost for third party labor", "$4,000 weekly fee", "Agency travel estimate is very high". But it's not a line-item table, ledger, statement, voucher, or check face. It's a list of questions/comments regarding a bid response. Not a financial document primary structure.
> 8. PRODUCT OR MATERIAL DOCUMENTATION -> specification
No.
> 9. SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation
No, it's a typed memo-like document with questions. Wait, is it a memo?
> 10. ADMINISTRATIVE FORM -> form
No fields, boxes, checkboxes.
> 11. CORRESPONDENCE -> email, memo, or letter
Let's check for memo/letter.
Title: "GMR MARKETING QUESTIONS REGARDING BID RESPONSE"
Body: Bullet points under headings.
Is there a TO:/FROM:/RE:/SUBJECT: header? No.
Is there an external address, "Dear ...", closing signature? No.
Is there a mail-client header? No.
Wait, let's look closer. "GMR MARKETING QUESTIONS REGARDING BID RESPONSE". This looks like a memo or a set of questions sent internally or to an agency.
Wait, check 11: "memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
"letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person..."
This page has none of those. It's just a title and bullet points.
Wait, what about check 13? "ORIGINAL RESEARCH WRITE-UP -> scientific_report". No, not research.
> Let's re-read the checks. Is there any other category?
What about "memo"? The instructions say: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo even without literal "TO:/FROM:" labels". This page doesn't have that either.
> Wait, is it a "presentation"?
Check 9: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement... or a photographic slide image... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... a single-word/short-phrase heading with no subtitle at all... is a presentation (this check), not file_folder (check 1)."
This page has a title "GMR MARKETING QUESTIONS REGARDING BID RESPONSE" and then a lot of text. Not a near-blank cover.
> Let's re-evaluate check 11: "CORRESPONDENCE -> email, memo, or letter".
If it doesn't have a memo header, is it a letter? No.
Is it an email? No mail-client header.
> Wait, look at the content again. It's a list of questions. Could it be a "questionnaire"? No, check 4 is for survey instruments.
Could it be a "form"? Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank... This also covers: a standalone labeled data chart or table...". This is not a form.
> What about "scientific_report"? Check 13: "Running narrative prose with objectives, methods, results, or discussion...". This is not running narrative prose.
> Let's look at the labels again:
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> Is there any chance this is a "memo"?
"A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. "Mr. R. J. Smith, Manager - Hanmer Division" from "T. P. Pettigrew, Manufacturing Services Manager - Research and Development") with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo even without literal "TO:/FROM:" labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."
This page doesn't have names, titles, or dates at the top.
> Wait, is it a "presentation"?
"Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)..."
This page has bullet lists. But it's dense text, not sparse slide layout.
> Let's reconsider the whole document. It's a page from an archive (Bates number 2083156178).
Title: GMR MARKETING QUESTIONS REGARDING BID RESPONSE.
It's a list of questions sent to an agency (GMR Marketing) regarding their bid response.
This is a form of correspondence, but which one?
If it doesn't fit memo, letter, email... what about "form"? No.
Could it be "scientific_report"? No.
> Let's re-read check 11 carefully.
"memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose (no external address, no "Dear ..." salutation). Without that header-then-prose structure it is not a memo."
"letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. "Mr. T. E. Sandefur") with prose and no TO:/FROM: block."
This page has neither.
> Is there any other check?
Check 10: "ADMINISTRATIVE FORM -> form ... internal authorization/approval forms with an approval signature/date block." No.
> What about "questionnaire"?
Check 4: "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey."
This page asks questions, but it's not a survey instrument. It's questions regarding a bid response.
> Wait, is it a "specification"?
Check 8: "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables... tolerances, or "shall/must" requirement language." No.
> Let's look at the "Runner-up" logic. "If nothing matches, choose the label whose defining evidence is closest to what you can actually read — never default to scientific_report. State in the scratchpad why none of checks 1-14 had positive evidence before doing this."
> Wait! Could it be a "memo"?
Often, internal documents like this are memos. But the strict rule says: "Without that header-then-prose structure it is not a memo."
Is there a header I missed?
"GMR MARKETING QUESTIONS REGARDING BID RESPONSE"
No TO/FROM/DATE.
> Could it be a "letter"?
No salutation, no closing.
> Could it be a "form"?
No fields.
> Let's re-read the prompt's calibration: "form, scientific_report, and handwritten are historically the most over-predicted labels; news_article and presentation are historically under-predicted."
> Is it possible this is a "presentation"?
"Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page..."
This is a typed page with bullet lists. But it's not sparse.
> What about "email"?
No mail-client header.
> Let's look at the content again. It's a list of questions.
Is there any chance it's a "questionnaire"?
"questions regarding bid response" - not a survey.
> Let's reconsider "memo".
Sometimes, a document with a title and bullet points is classified as a memo if it's internal correspondence. But the instructions are very strict: "Without that header-then-prose structure it is not a memo."
Wait, "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... with memo-style prose ... IS a memo even without literal "TO:/FROM:" labels". This page doesn't have that.
> What if it's a "form"?
"A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells. This also covers: a standalone labeled data chart or table... a filled analytical or lab data sheet... and internal authorization/approval forms with an approval signature/date block."
This is none of those.
> Let's look at the labels again.
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> If none match perfectly, I must choose the closest.
"State in the scratchpad why none of checks 1-14 had positive evidence before doing this."
> Let's check if there's any hidden header.
Top: "GMR MARKETING QUESTIONS REGARDING BID RESPONSE"
Bottom right: "2083156178" (Bates number, rotated).
No other text.
> This is a page of questions/comments.
Could it be a "memo"? In many document classification tasks, a page with a title and bulleted internal questions is a memo. But the instructions say: "Without that header-then-prose structure it is not a memo."
Wait, look at check 11 again: "memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
This implies if there's no header, it's NOT a memo.
> What about "letter"? "OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block." No named external person.
> What about "email"? "mail-client header block... or a forwarded/threaded mail trail." No.
> So it's not correspondence (check 11).
> What about "scientific_report"? "Running narrative prose with objectives, methods, results, or discussion...". This is not running narrative prose.
> What about "form"? "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". No.
> What about "presentation"? "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page...". This has bullet lists. But it's not sparse. "A near-blank cover or title page — mostly empty space with only a bold headline title... is a presentation". This page is not near-blank.
> Wait, is there any other category?
"questionnaire": "The page asks the reader to answer, rate, choose, or commit... or a cover letter transmitting a survey." No.
> Let's reconsider the "memo" definition. Is there any way this is a memo?
If I have to choose the closest, "memo" is the closest in function (internal business communication), but it lacks the structural evidence.
Wait! Look at the title: "GMR MARKETING QUESTIONS REGARDING BID RESPONSE".
This is a document sent to GMR Marketing (an agency) asking questions about their bid.
This is a letter or memo. Since it's to an external agency (GMR Marketing), it would be a letter if it had a salutation/closing. Since it doesn't, maybe it's a memo? But memos are internal. GMR is external.
Actually, if it's to an external agency, it's a letter. But it lacks letter formatting.
> Let's look at the instructions again: "If nothing matches, choose the label whose defining evidence is closest to what you can actually read — never default to scientific_report. State in the scratchpad why none of checks 1-14 had positive evidence before doing this."
> Wait, what if it's a "form"?
No.
> What if it's a "specification"?
No.
> Let's think about "presentation".
"Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)..."
This page has bullet lists. But it's text-heavy.
> Let's think about "questionnaire".
"questions regarding bid response" - it asks questions. But not a survey.
> Let's think about "invoice" or "budget".
It mentions costs, estimates. But it's not a financial document primary structure.
> I will classify this as "memo" because it's an internal-style document with a title and bulleted questions, even though it lacks the strict TO/FROM header. Wait, the instructions say "Without that header-then-prose structure it is not a memo."
If I can't use memo, what is it?
Maybe "letter"? "a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block." No named person.
> Let's re-read the scratchpad procedure: "If nothing matches, choose the label whose defining evidence is closest to what you can actually read — never default to scientific_report. State in the scratchpad why none of checks 1-14 had positive evidence before doing this."
> I will state that none of the checks have positive evidence because:
- Not file_folder (has body content).
- Not handwritten (typed).
- Not fax form.
- Not questionnaire (not a survey instrument).
- Not resume.
- Not scientific_publication (no journal header).
- Not invoice/budget (not a financial table/bill).
- Not specification.
- Not presentation (not sparse slide layout, not near-blank cover).
- Not form (no fields/boxes).
- Not email (no mail header).
- Not memo (no TO/FROM/RE header, no internal name/title address).
- Not letter (no external address, salutation, closing).
- Not news_article (no masthead).
- Not scientific_report (no running narrative prose).
- Not advertisement.
> Closest label: "memo" or "letter". Since it's questions to an agency, it's a business letter. But it lacks letter formatting. "memo" is often used for internal business documents. I'll go with "memo" as the closest functional equivalent, or maybe "letter".
Wait, look at check 11: "memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
This is a strict rule. If I follow it, it's NOT a memo.
"letter: ... OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block." No named person.
> Is there any chance this is a "form"?
"A form does NOT have to be blank... This also covers: a standalone labeled data chart or table...". No.
> What about "questionnaire"?
"The page asks the reader to answer, rate, choose, or commit... open-response lines". This page asks questions, but they are not for a survey.
> I will output "memo" as the closest, but state in scratchpad that it lacks the strict header.
Actually, let's look at the content. "GMR MARKETING QUESTIONS REGARDING BID RESPONSE". This is a document from Philip Morris (or similar) to GMR Marketing. It's a business letter. But since it lacks letter formatting, and the instructions say "choose the label whose defining evidence is closest", I'll choose "memo" or "letter". Let's choose "memo" because it's a list of questions, typical of internal or semi-internal business communication.
Wait, "GMR Marketing" is an external agency. So it's a letter. But it lacks letter formatting.
I'll output "memo" as the runner-up and explain.
Actually, if I have to output exactly one label, and none match perfectly, I should pick the closest. "memo" is often used for any business document with a title and body.
Let's choose "memo".
> Wait, look at the Bates number: 2083156178. This is a tobacco archive document.
Often, these are memos.
I'll go with "memo".
> Let's refine the scratchpad:
- file_folder: no — page has substantial body content (title, sections, bullet points).
- handwritten: no — typed text throughout.
- form: no — no fax header, no fields/boxes/checkboxes.
- questionnaire: no — asks business questions about a bid, not a survey instrument.
- resume: no.
- scientific_publication: no — no journal running head.
- invoice/budget: no — mentions costs but is not a financial table/bill/ledger.
- specification: no — no product data, safety data, or "shall/must" language.
- presentation: no — not sparse slide layout, not near-blank cover, not photographic slide.
- form (check 10): no — no structured fields for data capture.
- email: no — no mail-client header (From/To/Sent/Subject).
- memo: no strict evidence — lacks TO:/FROM:/RE:/SUBJECT: header block and internal name/title address, but functionally resembles a memo/business note with title and bulleted prose.
- letter: no strict evidence — lacks external address, "Dear..." salutation, closing signature.
- news_article: no — no masthead, byline, multi-column typography.
- scientific_report: no — lacks running narrative prose with objectives/methods/results; is a list of bullet points.
- advertisement: no — no product imagery, slogans, brand styling.
> Closest label: memo. Functionally, it's a business communication with a title and bulleted questions.
> Wait, is there any possibility it's a "questionnaire"?
"questions regarding bid response" - no.
> I'll output "memo".
Actually, I'll output "memo" and explain the lack of strict header.
Wait, the instructions say: "If nothing matches, choose the label whose defining evidence is closest to what you can actually read".
The defining evidence for memo is "TO:/FROM:/RE:/SUBJECT:/DATE:" header. This is absent.
The defining evidence for letter is "letterhead with external recipient address, date, 'Dear ...' salutation...". Absent.
The defining evidence for presentation is "Slide/overhead layouts... bullet lists". Present (bullet lists). But it's not sparse.
I'll go with "memo" as the closest functional category for a business document with a title and bulleted content.
> Let's reconsider "presentation".
"Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)..."
This page has bullet lists. But it's not sparse.
> I'll stick with "memo".
> One more check: could it be a "form"?
"A form does NOT have to be blank... This also covers: a standalone labeled data chart or table...". No.
> Final decision: memo.

---

## questionnaire → handwritten (1 errors)

### `rvl_cdip__questionnaire__0016.png`
**Expected:** `questionnaire` | **Predicted:** `handwritten`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> Image analysis:
The image shows a mostly blank page with handwritten text at the top: "79-0414", "Lab plan & Questionnaire".
There is a small handwritten "1" and a Bates number "50130 8150" at the bottom right.
The text is entirely handwritten. "Lab plan & Questionnaire".
> Let's go through the checks:
1. file_folder: Almost no body content, only an archive/Bates number, stamp, short label. Wait, "Lab plan & Questionnaire" is a short label. But is it a folder tab? No, it's handwritten on a blank page. Wait, check 1 says "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only." "79-0414" is an ID. "Lab plan & Questionnaire" is a short phrase. Is it a folder tab? No, it's handwritten on a white page. Wait, check 2 is handwritten.
2. handwritten: Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. "Lab plan & Questionnaire" is freeform handwriting on blank paper. No printed field labels. This matches handwritten.
Wait, let's look at check 4: questionnaire. "Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing... is a transmittal note for the instrument — questionnaire (check 4)". But this is just "Lab plan & Questionnaire". It's a note. Is it a transmittal note? It's just a title written by hand. "Lab plan & Questionnaire".
Wait, check 2 says: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout... A typed page with only a signature, stamp, or margin note is not handwritten." Here, the page is mostly blank, with handwritten text "79-0414", "Lab plan & Questionnaire", and a small "1". This is freeform handwriting on blank paper. So it's handwritten.
> Let's re-read check 1: "file_folder: Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title. A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
Here we have a handwritten note "Lab plan & Questionnaire". So it's not file_folder.
> Check 2: "handwritten: Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template... The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
This page is blank paper with freeform handwriting "79-0414", "Lab plan & Questionnaire". So it is handwritten.
> Check 4: "questionnaire: ... Notes ABOUT a survey instrument are questionnaire, not questionnaire... wait. 'Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing (e.g. "Revised questionnaire to be used VIII-IV. Revisions highlighted in VIII file. CPP questionnaire was not changed.") is a transmittal note for the instrument — questionnaire (check 4), even though it is freeform handwriting on blank paper.'"
Does "Lab plan & Questionnaire" count as a note about a questionnaire's revision, distribution, or routing? No, it's just a title/label. It's a handwritten note. The rule says "Notes ABOUT a survey instrument... is a transmittal note... questionnaire". But this is just "Lab plan & Questionnaire". It's a handwritten note. I'll stick with handwritten.
> Wait, is there any other check?
Check 1: file_folder. No, it has a note.
Check 2: handwritten. Yes, freeform handwriting on blank paper.
> Let's double check check 2 vs check 1.
"A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
"Lab plan & Questionnaire" is a note. So not file_folder.
It is handwritten.
> Let's review the whole page:
Top: "79-0414" (handwritten)
Middle: "Lab plan & Questionnaire" (handwritten)
Bottom right: "1" (handwritten), "50130 8150" (Bates number, printed/stamped).
> This is a handwritten note on a blank page.
Label: handwritten.
> Let's check if it could be a folder tab. "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body. The label IS filing metadata... The black bar is the photographed folder body/tab edge".
This page does not have a black bar, it's just a white page with a black border (scan artifact or page edge). The text is handwritten in the middle of the page, not on a tab. So not file_folder.
> Therefore, handwritten is the correct label.
> Scratchpad:
file_folder: no — the page contains a handwritten note ("Lab plan & Questionnaire") and an ID ("79-0414"), not just pure filing metadata or a folder tab.
handwritten: yes — the page is mostly blank with freeform handwriting ("79-0414", "Lab plan & Questionnaire", "1") on blank paper, no printed template or field labels.
questionnaire: no — although the text mentions "Questionnaire", it is just a handwritten title/note, not a transmittal note about revision/routing, nor a printed survey instrument.
Runner-up: file_folder, ruled out because the page carries a handwritten note ("Lab plan & Questionnaire") rather than being pure filing metadata or a folder tab.
> Final label: handwritten.

---

## scientific_publication → scientific_report (1 errors)

### `rvl_cdip__scientific_publication__0001.png`
**Expected:** `scientific_publication` | **Predicted:** `scientific_report`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "47th Tobacco Chemists' Research Conference" at the top. No journal name, volume, issue, page range, DOI, or copyright line belonging to a journal. Wait, there's a page number "5" at the bottom. The top says "47th Tobacco Chemists' Research Conference". This looks like a conference paper abstract or presentation. Let's look closer.
> **Check 1: file_folder**
- Evidence: There is a title "MENTHOL: ITS ORIGINS, CHEMISTRY, PHYSIOLOGY AND TOXICOLOGICAL PROPERTIES", author "Rudolf Hopp", affiliation, abstract text. Not just an identifier.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: There is some handwritten text on the left margin ("ent of the Borgarding a review of the..."), but the majority of the content is typed text (title, author, abstract).
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax header.
- Result: not this check.
> **Check 4: questionnaire**
- Evidence: No survey questions.
- Result: not this check.
> **Check 5: resume**
- Evidence: No career history.
- Result: not this check.
> **Check 6: scientific_publication**
- Evidence: "47th Tobacco Chemists' Research Conference". Is this a published journal? No, it's a conference. Wait, is there a journal identifier? No. Just conference name.
- Result: not this check.
> **Check 7: financial document**
- Evidence: No financial content.
- Result: not this check.
> **Check 8: specification**
- Evidence: No material safety data sheet, product formulation, etc.
- Result: not this check.
> **Check 9: presentation**
- Evidence: "47th Tobacco Chemists' Research Conference", title "MENTHOL: ITS ORIGINS...", author Rudolf Hopp, affiliation, abstract. Wait, is this a presentation cover or a scientific report?
- Let's check the text: "ABSTRACT ... (-)-Menthol, the main constituent of peppermint oils...". It's an abstract of a paper presented at a conference.
- Wait, check 9 says: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation". This is an abstract page.
- Let's look at check 13: "ORIGINAL RESEARCH WRITE-UP -> scientific_report". "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page with authors and an internal affiliation and no journal identifiers."
- This page has an abstract, which is running narrative prose (well, a paragraph). It's from a conference ("47th Tobacco Chemists' Research Conference"). Conference papers/abstracts are often scientific_reports if they are internal or conference proceedings without a journal identifier.
- Wait, is it a presentation? "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page...". This page has an abstract, which is dense text, not sparse slide layout.
- Let's re-read check 13: "a lab or technical study title page with authors and an internal affiliation and no journal identifiers." This has authors, affiliation (Haarmann & Reimer GmbH, Corporate Research, Germany), and no journal identifiers (just a conference name). The content is an abstract (running narrative prose). So it's a scientific_report.
- Let's check if there's any other match.
- What about the handwritten note on the left? "ent of the Borgarding a review of the...". It's a marginal note. Doesn't make it handwritten (check 2).
> Let's evaluate Check 13 vs Check 9.
Check 9: "a technical-study title page naming a specific experimental method/study is scientific_report (check 13), not presentation, even when it is sparse or printed slide-style on a dark background". This page is not sparse, it has an abstract.
Check 13: "Running narrative prose with objectives, methods, results, or discussion... a lab or technical study title page with authors and an internal affiliation and no journal identifiers." This page has an abstract (narrative prose), author, affiliation, and no journal identifiers (only conference name). So it fits scientific_report.
> Wait, is there a journal identifier? "47th Tobacco Chemists' Research Conference". No journal name, volume, issue.
So it's not scientific_publication (check 6).
> Let's review the evidence for scientific_report:
- Title: "MENTHOL: ITS ORIGINS, CHEMISTRY, PHYSIOLOGY AND TOXICOLOGICAL PROPERTIES"
- Author: Rudolf Hopp
- Affiliation: Haarmann & Reimer GmbH, Corporate Research, D-37603 Holzminden, Germany
- Content: "ABSTRACT" followed by a paragraph of running narrative prose describing the chemistry and toxicology of menthol.
- No journal identifier on the page itself (only conference name).
> Therefore, scientific_report.
> Let's double check check 6: "First, use your pre-scan finding: does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings? If yes... Evidence for this check: a named journal on the page plus a publication identifier... OR a formal paper or abstract in published conference proceedings: a named conference/symposium/tagungsband with a year, a titled, authored paper or abstract with an affiliation, and (usually) a page number."
Wait! "a formal paper or abstract in published conference proceedings: a named conference/symposium/tagungsband with a year, a titled, authored paper or abstract with an affiliation, and (usually) a page number."
Does "47th Tobacco Chemists' Research Conference" count as a named conference/symposium with a year? It doesn't have a year explicitly on this page, but it's a named conference. Wait, the rule says "with a year". There is no year on this page. "47th Tobacco Chemists' Research Conference". No year.
Also, the affiliation is "Haarmann & Reimer GmbH, Corporate Research, D-37603 Holzminden, Germany". This is an internal affiliation (company research).
Check 13 says: "a lab or technical study title page with authors and an internal affiliation and no journal identifiers." This matches perfectly. Internal affiliation (company research), no journal identifiers.
> So scientific_report is the correct label.
> Let's check the handwritten text on the left margin just in case.
"ent of the Borgarding a review of the [something] the tobacco [something]r. Steven A. discuss the nd transfer. bacco Company of cigarette d transfer. speaker, let speakers but participation. individual ratione where search in this."
This is a marginal note, probably from a reviewer or editor. It doesn't make the page "handwritten" because the majority is typed.
> Final check of the steps:
1. file_folder: no, has title, author, abstract.
2. handwritten: no, majority is typed.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no, no journal identifier, no year for the conference.
7. financial: no.
8. specification: no.
9. presentation: no, dense text abstract, not sparse slide layout.
10. form: no.
11. correspondence: no.
12. news_article: no.
13. scientific_report: yes, title page/abstract with author, internal affiliation, no journal ID, running prose (abstract).
14. advertisement: no.
> Runner-up: presentation. Ruled out because the page contains a dense abstract (running narrative prose) rather than a sparse slide/overhead layout or near-blank cover, and it has an internal affiliation with no journal identifiers, fitting scientific_report.
> Wait, is there any possibility it's a presentation?
"Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page..."
This is an abstract page from a conference proceedings or a draft of a paper. The text is an abstract. Abstracts are scientific reports (or publications if published). Since there's no journal ID and no year for the conference, it's an internal or unpublished conference paper/abstract -> scientific_report.
> The label is scientific_report.

---