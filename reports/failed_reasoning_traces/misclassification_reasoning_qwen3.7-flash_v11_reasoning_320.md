# Misclassification Reasoning — qwen3.7-flash_v11_reasoning_320

**Overall Accuracy:** 83.8% (264/315)  
**Total Errors:** 51  
**Unique Confused Pairs:** 26

---

## letter → memo (5 errors)

### `rvl_cdip__letter__0002.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** I see "RJR Interoffice Memorandum", "Subject:", "To:", "From:", "cc:". No "From:/To:/Sent:/Subject:" mail client headers like Outlook. Wait, "To:", "From:", "Subject:" are present. But it's an "RJR Interoffice Memorandum". Let's check the rules.
    - Check 11 (email): "mail-client header block (From/To/Sent/Subject, cc, attachments) or a forwarded/threaded mail trail."
    - Check 11 (memo): "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
    - The document has "RJR Interoffice Memorandum" at the top. It has "Subject:", "To:", "From:", "cc:". This looks like a memo.
    - Is there a fax header? "MAR 27 1987" is a date stamp. "50811 2328" is a Bates number. No "SENT BY:" fax header.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a full memo body, subject line, to/from fields, and handwritten notes. It has real content.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: There is a large handwritten note at the bottom ("3/30 For the long stand..."). However, the majority of the page is typed text (the memo itself). The handwriting is an annotation on a typed memo.
    *   Result: not this check. (Handwriting filling/annotating a typed document doesn't make it handwritten unless it's the majority content on freeform paper).
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. Just a date stamp "MAR 27 1987".
    *   Result: not this check.
> *   **Check 4: questionnaire**
    *   Evidence: No survey questions.
    *   Result: not this check.
> *   **Check 5: resume**
    *   Evidence: No career history.
    *   Result: not this check.
> *   **Check 6: scientific_publication**
    *   Evidence: No journal running head, volume, issue, page number.
    *   Result: not this check.
> *   **Check 7: financial document (invoice/budget)**
    *   Evidence: No line-item table of charges or budget tracking. Mentions "Kydex(R) plastic sheets", toxicity data. No money function as primary structure.
    *   Result: not this check.
> *   **Check 8: specification**
    *   Evidence: Discusses Kydex(R) polymer, toxicity. Not a Material Safety Data Sheet (though it discusses toxicity, it's a memo *about* using it, not the MSDS itself). Not a product formulation or manufacturing change authorization. It's a memo reviewing the use of a material.
    *   Result: not this check.
> *   **Check 9: presentation**
    *   Evidence: Not a slide deck, cover, or statement.
    *   Result: not this check.
> *   **Check 10: administrative form**
    *   Evidence: Not a form with fields for capturing data. It's a memo.
    *   Result: not this check.
> *   **Check 11: correspondence (email, memo, letter)**
    *   Evidence:
        *   Header: "RJR Interoffice Memorandum".
        *   Fields: "Subject: Use of KYDEX(R) For A Waste Tub Stand", "March 26, 1987", "To: Mr. Bill Hunt", "From: Dr. Rob Harrington".
        *   Body: Running prose about scientific affairs reviewing Kydex.
        *   Closing: Signature, "RH/Ige", "cc: Dr. A. W. Hayes...".
    *   This fits the definition of a **memo**: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose.
    *   Wait, is it an email? No mail-client headers like "Sent: ...". It's an interoffice memorandum.
    *   Result: **memo**.
> *   **Check 12: news_article**
    *   Evidence: No masthead.
    *   Result: not this check.
> *   **Check 13: scientific_report**
    *   Evidence: The text is technical (toxicity of polymers), but the structure is a memo ("RJR Interoffice Memorandum", "To:", "From:"). Check 11 (correspondence) precedes Check 13. A memo discussing technical data is still a memo. "A page whose primary structure is a memo header + prose... stays memo".
    *   Result: not this check (memo takes precedence).
> *   **Check 14: advertisement**
    *   Evidence: No marketing layout.
    *   Result: not this check.
> **Conclusion:**
The document is clearly an internal memorandum ("RJR Interoffice Memorandum"). It has the standard memo header (To, From, Subject, Date) and prose body. The handwritten note at the bottom is an annotation, not the primary content. The technical content doesn't override the memo structure.
> Let's double check Check 11 rules.
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo".
Here we have:
- "RJR Interoffice Memorandum"
- "Subject: ..."
- "To: Mr. Bill Hunt"
- "From: Dr. Rob Harrington"
- Date: "March 26, 1987" (and stamped "MAR 27 1987")
- Prose body.
- "cc:" list.
> This is a memo.
> Runner-up: scientific_report. Ruled out because the page has a clear memo header structure ("RJR Interoffice Memorandum", "To:", "From:", "Subject:") and is an internal correspondence, even though the content is technical/scientific. Check 11 (correspondence) comes before Check 13 (scientific_report).
> Final label: memo.

---
### `rvl_cdip__letter__0007.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There's a date "June 17, 1971", a name "Mr. J. H. Sherrill, Jr.", "Re: VANTAGE MENTHOL", and a Bates number "50030 0163" at the bottom right. No journal masthead.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a date, recipient name, subject line, and several paragraphs of text. It has real content.
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: The page is mostly typed text. There is a handwritten "Bill" at the top right and a circle around "(HRD # 71-0197)". Not majority handwritten.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey instrument or transmittal note.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: Not a resume.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal running head, volume, issue, or page number.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No line-item table, ledger, or financial primary structure. Mentions "data from the VANTAGE Menthol CAS", but it's a report of data, not a financial document.
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No Material Safety Data Sheet, product formulation, or "shall/must" language.
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck, cover, or press release.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: No fields, boxes, checkboxes, or ruled entry lines for capturing data.
- Not this check.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence:
  - Date: "June 17, 1971"
  - Recipient: "Mr. J. H. Sherrill, Jr."
  - Subject: "Re: VANTAGE MENTHOL (HRD # 71-0197)"
  - Body: "This reports data from the VANTAGE Menthol CAS by billboard and non-billboard cities. BACKGROUND: ... DISCUSSION: ..."
  - Sender: "Joseph Ottaviani, Marketing Research Department"
  - Initials: "JO;sp"
  - "Attachments"
  - This is an internal memo. It has a date, internal recipient (Mr. J. H. Sherrill, Jr. - likely internal given the context of Marketing Research Department), subject line ("Re:"), and internal sender with department. No external address, no "Dear ..." salutation, no closing signature. It fits the memo definition: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block (or equivalent: date, recipient, Re:, body, sender, initials) followed by memo-style prose.
  - Let's check the memo definition: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels". Here we have date, recipient name, "Re:", body, sender name + department, initials. This is a memo.
- This check matches.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Not this check.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Not this check.
> Final label: memo.
> Let's double check.
Date: June 17, 1971
To: Mr. J. H. Sherrill, Jr.
Re: VANTAGE MENTHOL (HRD # 71-0197)
Body paragraphs: BACKGROUND, DISCUSSION.
Sender: Joseph Ottaviani, Marketing Research Department.
Initials: JO;sp.
Attachments.
This is a classic internal memo.
> Runner-up: letter. Ruled out because there is no external recipient address, no "Dear ..." salutation, and no closing signature. It is an internal note to a named person (Mr. J. H. Sherrill, Jr.) with internal department info (Marketing Research Department), which makes it a memo.
> Wait, is there any chance it's a letter?
"Mr. J. H. Sherrill, Jr." - no title given, but "Re:" line is typical of memos.
"Joseph Ottaviani / Marketing Research Department" - internal department.
No "Dear Mr. Sherrill,".
No "Sincerely, / Joseph Ottaviani".
It's a memo.
> Let's review the scratchpad requirements.
- Briefly state evidence for each check or "not this check".
- Stop at matching check.
- Add final line naming runner-up and evidence that ruled it out.
> Scratchpad:
file_folder: no — the page has a date, recipient, subject, and multiple paragraphs of text, not just an identifier/stamp.
handwritten: no — the page is mostly typed text with only a small handwritten annotation ("Bill" and a circle).
fax: no — no "FACSIMILE" or fax transmission header.
questionnaire: no — does not ask the reader to answer or rate anything.
resume: no — not a career history.
scientific_publication: no — no journal running head, volume, or page number.
financial: no — no line-item table, ledger, or financial primary structure; it reports advertising data, not money.
specification: no — no Material Safety Data Sheet, product formulation, or "shall/must" language.
presentation: no — not a slide deck, cover, or press release.
form: no — no fields, boxes, checkboxes, or ruled entry lines.
email: no — no mail-client header block (From/To/Sent/Subject).
memo: yes — dated "June 17, 1971", addressed to "Mr. J. H. Sherrill, Jr." with "Re: VANTAGE MENTHOL", followed by memo-style prose ("BACKGROUND:", "DISCUSSION:"), and signed internally by "Joseph Ottaviani, Marketing Research Department" with initials "JO;sp". No external address, no salutation, no closing signature.
news_article: no — no masthead or journalistic layout.
scientific_report: no — not a research write-up with running narrative prose about objectives/methods/results; it's an internal business memo reporting on advertising data.
advertisement: no — not a promotional layout.
> Runner-up: letter, ruled out because the page lacks an external recipient address, a "Dear ..." salutation, and a closing signature, and is addressed internally by name and department with a "Re:" subject line, which defines a memo.
> Final label: memo.

---
### `rvl_cdip__letter__0008.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None. There is a "TO:", "FROM:", "SUBJECT:" block, but it's a memo header, not an email header (From/To/Sent/Subject with email addresses or mail client format). Wait, let's look closer. "TO: Mr. E. C. Leary", "FROM: G. R. Davis", "SUBJECT: March CAMEL Cash Tracking Results". This is a standard memo header.
- Masthead or running head: No newspaper/magazine masthead. No journal running head. There is a Bates number "93-13104" rotated on the left, and "51969 5114" on the right. Top right has "DGR2". Date: "April 16, 1993".
> **Check 1: file_folder**
- Evidence: The page has a full memo body with "KEY FINDINGS" and bullet points. Not just an identifier.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: The text is typed. There is a handwritten "DGR2" at the top right and a rotated Bates number "93-13104". Not majority handwritten.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey instrument. It's a memo about results.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: No resume/CV.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal name, volume, issue, page range on the page itself.
- Result: not this check.
> **Check 7: FINANCIAL DOCUMENT**
- Evidence: Mentions "March CAMEL Cash Tracking Results", "participation rate", "awareness". No line-item table of charges, no invoice, no budget ledger. It's a status report/memo.
- Result: not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
- Evidence: No Material Safety Data Sheet, no product formulation, no "shall/must" language.
- Result: not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
- Evidence: Not a slide deck, not a press release, not a speech. It's a memo.
- Result: not this check.
> **Check 10: ADMINISTRATIVE FORM**
- Evidence: No fields, boxes, checkboxes for capturing data. It's a memo with prose.
- Result: not this check.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: "TO: Mr. E. C. Leary", "FROM: G. R. Davis", "SUBJECT: March CAMEL Cash Tracking Results", date "April 16, 1993". Followed by prose body ("Attached are the results..."). This is a classic internal memo header followed by memo-style prose. No external address, no "Dear ..." salutation.
- Result: memo.
> **Check 12: PUBLISHED JOURNALISM**
- Evidence: No masthead, no byline, no multi-column news typography.
- Result: not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP**
- Evidence: It's a memo summarizing results, not a full research write-up with methods/results discussion in narrative prose format of a scientific report. Wait, check 11 (memo) precedes check 13. The structure is memo header + prose. Check 11 wins.
> **Check 14: PROMOTIONAL MATERIAL**
- Evidence: No marketing layout.
- Result: not this check.
> Let's double check Check 11.
"memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose (no external address, no "Dear ..." salutation)."
The page has:
April 16, 1993
TO: Mr. E. C. Leary
FROM: G. R. Davis
SUBJECT: March CAMEL Cash Tracking Results
(BlAD #93-13104)
> Attached are the results...
> This perfectly matches the memo definition.
> Runner-up: scientific_report. Ruled out because the page has a clear TO/FROM/SUBJECT memo header followed by internal correspondence prose, which is classified as memo (check 11) before scientific_report (check 13). Also, it's a summary of tracking results, not an original research write-up with methods/results.
> Final label: memo.

---
### `rvl_cdip__letter__0009.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> **Document Analysis:**
- Top right: "cam" (handwritten)
- Header: "RJR CONFIDENTIAL"
- Date: "October 21, 1993"
- TO: Mr. G. C. Pennell
- FROM: T. F. Witner
- SUBJECT: MAGNA Advertising Study Results
- Body: Running prose discussing "MAGNA Advertising Study", "Honest Value" campaign, "Respect" campaign, recall/impact data, key measures (likeability, post purchase interest).
- Tables: Data tables with percentages and numbers (First Mention, Second Mention, Total First/Second; Likelihood, Post Pur. Int., Pre/Post PI Shift).
- Bottom right: Bates number "51399 2876" (rotated).
> **Pre-scan:**
- Mail-client header block? No. "TO:", "FROM:", "SUBJECT:" are memo headers, not email headers (From/To/Sent/Subject/cc). Wait, email requires "From:/To:/Sent:/Subject:" or forwarded trail. This is a memo header.
- Masthead/running head? No newspaper/magazine masthead. No journal running head. "RJR CONFIDENTIAL" is a handling mark.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: No, there is a full memo with tables and prose.
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Only a small "cam" handwritten at the top right. The rest is typed.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey instrument, no questions for the reader to answer. It's a report of study results.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range on this page.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No line-item table of charges, no invoice/budget structure. The tables are survey results (percentages, recall, likeability).
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No material safety data, no product formulation, no "shall/must" language.
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck, not a press release, not a speech. It's a memo with tables.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: No filled fields, checkboxes, or ruled entry lines for capturing factual data. It's a narrative report with embedded data tables.
- Not this check.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: "TO: Mr. G. C. Pennell", "FROM: T. F. Witner", "SUBJECT: MAGNA Advertising Study Results", date "October 21, 1993". Followed by memo-style prose ("This provides you with key measures..."). Internal address (no external address, no "Dear ..."). This is a classic internal memo.
- This check matches.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: No.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: It discusses a study, but it's formatted as an internal memo (TO/FROM/SUBJECT) reporting results to a colleague. Check 11 (memo) takes precedence because of the TO/FROM/SUBJECT header block followed by prose. Wait, does check 13 override check 11?
- Let's re-read check 11: "memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
- Check 13: "Running narrative prose with objectives, methods, results, or discussion... Requires running prose".
- The instructions say: "Once an earlier check matches, later checks do not override it." Check 11 is before Check 13. The page has a clear memo header (TO/FROM/SUBJECT/DATE) and memo-style prose. So it's a memo.
- Let's check if there's any reason it's not a memo. "A page whose primary structure is a memo header + prose, but whose prose merely discusses, forwards, or requests approval of an invoice/bill... stays memo". Here it discusses study results. It's a memo reporting study results.
- So memo is the correct label.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: No.
> **Runner-up:** scientific_report. Ruled out because the page has a clear internal memo header (TO:/FROM:/SUBJECT:/DATE:) followed by prose, which matches check 11 (memo) before check 13 (scientific_report). The content is a report of a study, but the document function is an internal memo.
> Let's double check check 11 vs 13.
Check 11: "memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose (no external address, no "Dear ..." salutation)."
The page has:
TO: Mr. G. C. Pennell
FROM: T. F. Witner
SUBJECT: MAGNA Advertising Study Results
October 21, 1993
This is exactly the memo header.
Then prose: "This provides you with key measures..."
This is a memo.
> Final label: memo.

---
### `rvl_cdip__letter__0010.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> **Document Analysis:**
- Top right: "January 21, 1985"
- Top left:
  - "TO: Mr. Alan R. Cox"
  - "FROM: Susan C. Nassar"
  - "SUBJECT: Marlboro Offensive--Idea Generation"
- Body: Running narrative prose summarizing recommendations for qualitative follow-up, ideas generated by two groups, observational research ideas, music section.
- Bottom right: "50461 4652" (Bates number)
> **Pre-scan:**
- Mail-client header block? No. "TO:", "FROM:", "SUBJECT:" are memo headers, not email headers (From/To/Sent/Subject with cc, etc., though email can have these, the format here is classic memo). Wait, let's look at check 11. "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". This matches perfectly.
- Masthead/running head? No newspaper/magazine masthead. No journal running head.
> **Check 1: file_folder**
- Evidence: No, there is a full memo with body text.
> **Check 2: handwritten**
- Evidence: No, it's typed text.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax cover sheet header.
> **Check 4: questionnaire**
- Evidence: No survey instrument or transmittal.
> **Check 5: resume**
- Evidence: No career history.
> **Check 6: scientific_publication**
- Evidence: No journal running head, volume, issue, etc.
> **Check 7: financial document**
- Evidence: No financial table, ledger, or primary financial structure. Mentions "Idea Generation", not money.
> **Check 8: specification**
- Evidence: No material safety data sheet, product formulation, or "shall/must" language.
> **Check 9: presentation**
- Evidence: No slide deck layout, no "FOR IMMEDIATE RELEASE", no photographic slide. It's a memo.
> **Check 10: administrative form**
- Evidence: No filled fields, boxes, checkboxes. It's a memo.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: "TO: Mr. Alan R. Cox", "FROM: Susan C. Nassar", "SUBJECT: Marlboro Offensive--Idea Generation", date "January 21, 1985". Followed by memo-style prose. This is a memo.
- Let's check email: No mail-client header block (From/To/Sent/Subject/cc). The pre-scan says "A FAX machine transmission header... is NOT a mail-client header". This is a standard memo header.
- Let's check letter: No external address, no "Dear ...", no closing signature.
- So it's a memo.
> **Check 12: news_article**
- Evidence: No masthead, byline, dateline, multi-column typography.
> **Check 13: scientific_report**
- Evidence: No running narrative prose with objectives/methods/results of a scientific study. It's a business memo about marketing ideas.
> **Check 14: advertisement**
- Evidence: No promotional material, product imagery, slogans.
> **Conclusion:**
The document is a memo.
> Let's double check check 11.
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."
The document has:
"January 21, 1985"
"TO: Mr. Alan R. Cox"
"FROM: Susan C. Nassar"
"SUBJECT: Marlboro Offensive--Idea Generation"
Followed by prose: "This summarizes what I would recommend as ideas for qualitative follow-up..."
This is a classic internal memo.
> Runner-up: letter. Ruled out because there is no external recipient address, no "Dear..." salutation, and no closing signature. It has a TO/FROM/SUBJECT block typical of a memo.
> Final label: memo.

---

## specification → form (5 errors)

### `rvl_cdip__specification__0003.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> Image analysis:
The image is rotated 90 degrees counter-clockwise. Let's mentally rotate it.
Title: "WINSTON KS"
Subtitle: "RATE DATA"
Subtitle: "FROM 02JAN91 TO 28MAY91"
Y-axis (rotated): "Average Weight percent"
X-axis (rotated): "Subgroup Index (DATE)" with dates from JAN 02 to JAN 26.
Data points: box plots or similar statistical plots (USPEC, SPEC).
Text on left (rotated top): "Subgroup Sizes: Min n=26 Max n=56"
Bates number: "51281 9398"
> Let's evaluate the checks:
1. file_folder: No, it has a chart/graph with data.
2. handwritten: No, it's a printed chart.
3. FAX: No fax header.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No journal running head, volume, issue, page number. Just a Bates number "51281 9398".
7. financial: No.
8. specification: No "shall/must", no material safety data sheet.
9. presentation: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." Wait, let's check check 10.
10. form: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... is a form (this check)". Wait, is this a hand-plotted experimental graph? "A hand-plotted experimental GRAPH — data points plotted on graph paper showing the relationship between measured variables for a test... is a research test result (check 13), not a form". This is a computer-generated chart (box plots, "Subgroup Index (DATE)", "Average Weight percent", "USPEC", "SPEC"). It's a labeled data chart/table. Wait, check 10 says: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... is a form". But check 13 says: "Also scientific_report: a hand-plotted experimental graph...". This is not hand-plotted. It's a computer-generated plot. Is it a form? "A standalone labeled data chart or table... is a form". Let's re-read check 10: "This also covers: a standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)". Yes, a standalone chart is a form.
Wait, let's look at check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
So a standalone chart is a form.
Let's check if there's any other category.
Is it a scientific_report? "Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report." This page has no running prose, just a chart. So it's a form.
> Let's double check check 10 vs check 13.
Check 10: "This also covers: a standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)..."
Check 13: "Also scientific_report: a hand-plotted experimental graph of test measurements (see check 10)..."
Since this is a computer-generated chart (box-and-whisker plots, likely from a statistical software like JMP or similar, given the "USPEC" and "SPEC" labels and "Subgroup Index"), it falls under "standalone labeled data chart" -> form.
> Let's review the pre-scan:
- Mail-client header: none.
- Masthead/running head: none. Just "WINSTON KS", "RATE DATA", "FROM 02JAN91 TO 28MAY91", "51281 9398".
> Check 1: file_folder. No, has chart.
Check 2: handwritten. No.
Check 3: FAX. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No journal identifier.
Check 7: financial. No.
Check 8: specification. No.
Check 9: presentation. "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
Check 10: form. "A standalone labeled data chart or table... is a form". The page is a chart showing "Average Weight percent" vs "Subgroup Index (DATE)" for "WINSTON KS RATE DATA". It is a standalone labeled data chart.
Check 11: correspondence. No.
Check 12: news_article. No.
Check 13: scientific_report. No running prose.
Check 14: advertisement. No.
> Therefore, the label is "form".
> Wait, let's carefully read check 10 again:
"This also covers: a standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values); a filled analytical or lab data sheet..."
Yes, a standalone chart is a form.
> Let's check if there's any chance it's a scientific_report.
"Requires running prose — a page that is only labeled field-value entries (even an 'ANALYTICAL DATA SUMMARY' under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
This page is just a chart. No running prose. So it's a form.
> Let's confirm the chart details:
Title: WINSTON KS RATE DATA FROM 02JAN91 TO 28MAY91
Axes: Average Weight percent, Subgroup Index (DATE)
Data: Box plots for USPEC and SPEC.
Text: Subgroup Sizes: Min n=26 Max n=56
Bates: 51281 9398
> This is a standalone labeled data chart. Label: form.
> Scratchpad:
file_folder: no — the page contains a chart with data, not just an identifier/stamp.
handwritten: no — printed chart.
questionnaire: no.
resume: no.
scientific_publication: no — no journal running head, volume, or page number on the page itself.
presentation: no — check 9 explicitly states "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
form: yes — the page is a standalone labeled data chart ("WINSTON KS RATE DATA" with "Average Weight percent" vs "Subgroup Index (DATE)" and box plots), which falls under check 10 ("a standalone labeled data chart or table... is a form").
scientific_report: no — requires running narrative prose; this page is only a chart with no prose.
Runner-up: presentation, ruled out because check 9 explicitly excludes standalone charts from being slides, directing them to form (check 10).
> Final label: form.

---
### `rvl_cdip__specification__0006.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head/volume/issue/page number on this specific page. There is a Bates number "50052 7368" on the right side.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a lot of content. It has fields like "Analytical information (detailed)", "Quantitative", "Qualitative", "Structural Formula", "Types of Tobacco", "Tox.-Pharm. Inform.", "Reference", "Bibliography". It has a block of text about a patent ("British American Tobacco Limited... MATERIAL FOR FILTERING TOBACCO SMOKE...").
    *   Is it a folder tab? No. It's a full page of structured data entry fields.
    *   Is it an identifier-only page? No, it has real content (patent info, fields).
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: There is a handwritten signature/name at the top left: "Goldschlager" (or similar, looks like a signature). But the rest is typed text and form fields.
    *   Is most content freeform handwriting? No. It's a typed form with mostly empty fields, filled with some typed text at the bottom (patent info). Wait, looking closely at the bottom text: "British American Tobacco Limited... MATERIAL FOR FILTERING TOBACCO SMOKE...". This looks like typed text filling in the "Reference" or "Bibliography" section.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header. No fax transmission metadata like "SENT BY:".
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: Does it ask the reader to answer? It looks like a data collection sheet or a form for cataloging chemical information. "Analytical information (detailed)", "Structural Formula", "Mol. Form", "Mol. Weight". It has instructions at the bottom: "If there is not sufficient space available... use reverse side... List all answerable information for each constituent and do so in index style."
    *   Is it a survey? No, it's a technical data sheet or form.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal running head. The text mentions patents and "Ger. Pat. Gaz.", but this is content within the page, not the page's own identifier.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: No financial tables, no dollar amounts, no billing.
    *   Result: not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: The bottom text describes a patent: "MATERIAL FOR FILTERING TOBACCO SMOKE - CONTAINING CARBON PARTICLES COATED INTERNALLY - EXTERNALLY WITH POROUS LAYER OF ORGANIC POLYMER."
    *   Is this a specification? A specification usually has "shall/must" language or is a product formulation. This looks like a data entry form for chemical/patent information. The top part is a form with fields: "Analytical information", "Quantitative", "Qualitative", "Structural Formula", "Types of Tobacco".
    *   Wait, let's look at Check 10 (Form). This looks like a form for capturing data.
    *   Let's re-read Check 8. "Material Safety Data Sheet... product formulation... test-analysis tables keyed to product/part codes... tolerances, or 'shall/must' requirement language."
    *   This page has fields for "Analytical information", "Structural Formula", "Mol. Form", "Mol. Weight". It looks like a form to record chemical analysis data.
    *   The bottom text is a reference to a patent.
    *   Is it a specification? It doesn't look like a product spec document (like an MSDS). It looks like a form to *record* data about a substance.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: No. Dense text at the bottom, form fields at the top.
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
    *   The page has fields: "Analytical information (detailed) Smoke / Green / Cured / Non-Leaf Itemize:", "Quantitative (all figures)", "Qualitative only Quotients or Semi-quant.", "Structural Formula", "Mol. Form", "Mol. Weight", "M.P.", "B.P.", "Chem. Groups", "Derivatives", "Types of Tobacco (all details)", "Tox.-Pharm. Inform. and other Notes", "Reference", "Bibliography".
    *   There is a block of typed text at the bottom filling in the "Reference" and "Bibliography" sections (patent info, keywords).
    *   There is a handwritten signature at the top.
    *   The instructions at the bottom say: "If there is not sufficient space available for any of the categories, use reverse side, identifying category(ies), and write 'over' on this side. List all answerable information for each constituent and do so in index style."
    *   This is clearly a form for capturing chemical/patent data. It's a structured data capture sheet.
    *   "A standalone labeled data chart or table... A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)..." -> This fits "filled analytical or lab data sheet".
    *   Result: **form**.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: "Requires running narrative prose". This page is mostly form fields. The text at the bottom is a patent citation/reference, not a narrative report of research objectives/methods/results. It's data entry.
    *   Result: not this check.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: No.
    *   Result: not this check.
> **Re-evaluating Check 8 vs Check 10:**
Check 8 (Specification): "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes... But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
This page has fields for "Analytical information", "Structural Formula", etc. It is a form to capture data. The text at the bottom is a patent reference. It doesn't have "shall/must". It's not an MSDS. It's a data capture form.
Check 10 (Form): "A filled analytical or lab data sheet... is a form". This page is a sheet for "Analytical information (detailed)". It has fields for chemical properties. It is filled (partially) with patent info. It fits "form" perfectly.
> **Re-evaluating Check 1:**
Is it a file folder? No, it has content.
> **Conclusion:**
The page is a form for capturing analytical/patent information. It has labeled fields (Quantitative, Qualitative, Structural Formula, etc.) and instructions for filling it out. The bottom text is filled-in data (patent reference). This is a filled analytical/lab data sheet or a data capture form.
> Label: **form**.
> Let's double check the "scientific_report" possibility.
Check 13: "Running narrative prose with objectives, methods, results, or discussion... Requires running prose".
The text at the bottom is:
"RJR CLASS NO. PATENT
British American Tobacco Limited, Gt. Brit.
MATERIAL FOR FILTERING TOBACCO SMOKE - CONTAINING CARBON PARTICLES COATED INTERNALLY - EXTERNALLY WITH POROUS LAYER OF ORGANIC POLYMER.
German Patent OLS 2,527,569...
*Also abstr. in: Ger. Pat. Gaz. X (No. 4) D4-D5 (Mar. 3, 1976)*
*Keywords:* carbon, filter, additive; aldehydes, smoke, constituent.
Bibliography: If there is not sufficient space..."
This is a reference entry, not a research write-up. The page structure is a form with headers like "Analytical information", "Quantitative", "Qualitative", "Structural Formula". This is a form.
> Final check on "handwritten":
Top left has "Goldschlager" (handwritten). But the rest is typed form fields and typed text at the bottom. Not majority handwritten.
> Final check on "questionnaire":
It asks for information, but it's a technical data sheet for cataloging chemical/patent info, not a survey for consumers or a research instrument asking opinions. The instructions "List all answerable information for each constituent" suggest it's a data collection form for a database or index. This falls under "administrative form" or "analytical data sheet" -> form.
> The label is **form**.
> Wait, let's look at the "Bibliography" section text again.
"Bibliography: If there is not sufficient space available for any of the categories, use reverse side, identifying category(ies), and write 'over' on this side. List all answerable information for each constituent and do so in index style."
This confirms it's a form for indexing/capturing data about constituents.
> One detail: "A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) is a form".
This page has "Structural Formula", "Mol. Form", "Mol. Weight". It is an analytical data sheet.
> Therefore, **form**.
> One more check: Check 8 "test-analysis tables keyed to product/part codes...".
The bottom text mentions "British American Tobacco Limited... MATERIAL FOR FILTERING TOBACCO SMOKE". This is a product/material.
But the page itself is a form to capture data *about* it.
Check 8 says: "But a generic labeled chart or table with no product/material tie-in at all... is an administrative form".
Here there is a product tie-in in the filled text ("MATERIAL FOR FILTERING TOBACCO SMOKE").
However, the page structure is a blank form with fields "Analytical information", "Quantitative", "Qualitative", "Structural Formula", "Types of Tobacco".
Is this a "test-analysis table"?
A test-analysis table usually has rows of data and columns of measurements.
This page has labels on the left/top and blank space for writing. It's a data entry form.
Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A filled analytical or lab data sheet... is a form".
This fits Check 10 better. The page is a template (form) that has been partially filled.
> The text at the bottom is the filled content.
The top is the form structure.
So it's a filled form.
> Label: form.

---
### `rvl_cdip__specification__0013.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow a strict set of checks in order, starting with a pre-scan.
> **Pre-scan:**
- Mail-client header block: None. "DATE . FRI, MAR 1, 1985, 8:21 AM", "PAGE 1 OF 3", "TEST NUMBER: PD00237", "CHARGE NUMBER: 1300". This looks like a fax transmission header or a computer printout header, not a mail-client header (From/To/Sent/Subject). Wait, "DATE . FRI, MAR 1, 1985, 8:21 AM" and "PAGE 1 OF 3" could be a fax transmission header. Let's look closely. "SENT BY:" is not explicitly there, but "DATE . FRI, MAR 1, 1985, 8:21 AM" and "PAGE 1 OF 3" are typical fax machine transmission metadata. The prompt says: "a FAX machine transmission header is NOT a mail-client header: machine-stamped 'SENT BY:', a date/time with a phone/fax number, and a page count like '# 4/7' ... is fax transmission metadata added by the sending machine — it does not make the page an email". This looks like a fax header or a computer printout header. Let's assume it's not an email.
- Masthead or running head: No newspaper/magazine masthead. No journal running head/volume/issue/page number. There is a Bates number "50512 3457" at the bottom right.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a lot of body content: "TEST NUMBER: PD00237", "REQUESTED BY: WILSON, JOHN", "TEST PURPOSE: CONSUMER SATISFACTION PROGRAM", "SPECIAL INSTRUCTIONS", "FILTER MAKING", "MAKING & PACKING", "TESTING". It is not an identifier-only page.
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: The page is typed throughout. No majority handwriting.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX" header. The top has "DATE . FRI, MAR 1, 1985, 8:21 AM" and "PAGE 1 OF 3", which is likely a fax transmission header or computer printout, but not a fax cover sheet form.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: "TEST PURPOSE: CONSUMER SATISFACTION PROGRAM". But this is an instruction sheet for a test, not a survey instrument asking the reader to answer. It has "SPECIAL INSTRUCTIONS", "FILTER MAKING", "MAKING & PACKING", "TESTING". It's a test request or instruction sheet.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No career history.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range, DOI.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: "CHARGE NUMBER: 1300". But no line-item table of charges, no amounts due, no budget tracking. It's a test request.
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: "TOBACCO VARIETY C53-44X IS STORED IN DAVIE COUNTY HHD #05326032-9; SHED #010529. USE AS DESCRIBED IN BLEND FORMULATION." "PREPARE FILTERS AS DESCRIBED USING CURRENT WIN. KS CONFIGURATION AND SPECS." "NEED 20 CTNS. BANDED & 60 CTNS. NOT BANDED. MAKE PRODUCT TO FIRMNESS." These are instructions for making and testing a product. Is this a specification? "Material Safety Data Sheet", "product formulation or preparation/mixing instructions", "manufacturing-change authorization", "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language." This looks like a test request or instruction sheet for a manufacturing/test process. Let's look at check 10.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck, not a cover, not a statement.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: "FILLED OR BLANK FIELDS, BOXES, CHECKBOXES, AND RULED ENTRY LINES FOR CAPTURING FACTUAL DATA; AN APPLICATION... A STANDALONE LABELED DATA CHART OR TABLE... INTERNAL AUTHORIZATION/APPROVAL FORMS". This page has labeled fields: "DATE", "TEST NUMBER", "CHARGE NUMBER", "PRIORITY", "REQUESTED BY", "DATE REQUESTED", "RELATED TEST NUMBER", "DIVISION", "CLASSIFICATION", "TEST PURPOSE", "MAKING AND PACKING DATE", "MAIL OUT DATE", "TYPE OF PANEL TESTING", "SPECIAL INSTRUCTIONS", "TOBACCO PROCESSING", "FILTER MAKING", "MAKING & PACKING", "TESTING". It is a structured form capturing data about a test request. It's a test request form or instruction sheet. The fields are filled with typed text. This fits "administrative form" or "application" or "filled form". Let's check if there's a better fit.
- Wait, is it a specification? "product formulation or preparation/mixing instructions". The text says "USE AS DESCRIBED IN BLEND FORMULATION", "PREPARE FILTERS AS DESCRIBED USING CURRENT WIN. KS CONFIGURATION AND SPECS". It's giving instructions. But the overall layout is a form with labeled fields (DATE, TEST NUMBER, REQUESTED BY, etc.). Check 10 says "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... This also covers: ... internal authorization/approval forms with an approval signature/date block." This is a test request form. It captures factual data (test number, requested by, purpose, instructions).
- Let's re-read Check 8: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification". This page is not a titled product-analysis table. It's a test request/instruction sheet.
- Let's re-read Check 10: "administrative form -> form. Filled or blank fields... for capturing factual data". This page has fields like "TEST NUMBER: PD00237", "REQUESTED BY: WILSON, JOHN (5979)", "TEST PURPOSE: CONSUMER SATISFACTION PROGRAM". It's a form used to request a test and provide instructions.
> Let's look closely at the content.
"DATE . FRI, MAR 1, 1985, 8:21 AM"
"PAGE 1 OF 3"
"TEST NUMBER: PD00237"
"CHARGE NUMBER: 1300"
"REQUESTED BY: WILSON, JOHN (5979)"
"DATE REQUESTED: 840705"
"CLASSIFICATION: WINS KS"
"DIVISION: 775"
"TEST PURPOSE: CONSUMER SATISFACTION PROGRAM"
"SPECIAL INSTRUCTIONS:"
"TOBACCO PROCESSING: TOBACCO VARIETY C53-44X IS STORED IN DAVIE COUNTY HHD #05326032-9; SHED #010529. USE AS DESCRIBED IN BLEND FORMULATION. ANALYSE EACH BLEND COMPONENT FOR NICOTINE AND REDUCING SUGARS BEFORE MAKING PRODUCT."
"FILTER MAKING: PREPARE FILTERS AS DESCRIBED USING CURRENT WIN. KS CONFIGURATION AND SPECS."
"MAKING & PACKING: NEED 20 CTNS. BANDED & 60 CTNS. NOT BANDED. MAKE PRODUCT TO FIRMNESS. DO NOT SAMPLE ON MAKING AND PACKING FLOOR. SAMPLES WILL BE PULLED LATER."
"TESTING: STANDARD ANALYSES."
> This is a test request form or a work order. It has labeled fields and filled data. It captures factual data about a test. It fits "form" (check 10).
> Is there any other check?
Check 11: CORRESPONDENCE -> email, memo, or letter.
- No TO:/FROM:/RE: header block followed by prose. It's a form with fields.
> Check 12: PUBLISHED JOURNALISM -> news_article.
- No.
> Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report.
- No running narrative prose. It's structured fields.
> Check 14: PROMOTIONAL MATERIAL -> advertisement.
- No.
> So it's form (check 10).
> Let's double check Check 8 (specification).
"product formulation or preparation/mixing instructions"
The text contains preparation instructions: "TOBACCO VARIETY C53-44X IS STORED... USE AS DESCRIBED IN BLEND FORMULATION", "PREPARE FILTERS AS DESCRIBED...", "NEED 20 CTNS... MAKE PRODUCT TO FIRMNESS."
But the overall document is a form with a header (DATE, TEST NUMBER, CHARGE NUMBER, REQUESTED BY, etc.) and sections for instructions. The primary structure is a form capturing test request data and instructions. Check 10 says "A form does NOT have to be blank — a filled form recording data is still a form". This is a filled form recording test request data and instructions.
Also, Check 8 says "test-analysis tables keyed to product/part codes... is a specification". This is not a test-analysis table. It's a test request.
Check 10 covers "administrative form". A test request form is an administrative form.
> Let's review the scratchpad procedure.
1. file_folder: no — page has substantial body content (test request fields, instructions), not just an identifier/stamp.
2. handwritten: no — typed throughout.
3. fax transmission sheet: no — top header is date/page count (likely fax metadata or computer printout), not a "FACSIMILE TRANSMISSION" cover sheet form.
4. questionnaire: no — not asking the reader to answer/rate; it's an internal test request/instruction sheet.
5. resume: no.
6. scientific_publication: no — no journal identifier.
7. financial document: no — "CHARGE NUMBER" is present, but no line-item billing, amounts, or budget tracking.
8. specification: no — contains preparation instructions, but the primary structure is a labeled-field form capturing test request data, not a titled product-analysis table or MSDS.
9. presentation: no — not a slide deck or cover.
10. administrative form: yes — page consists of labeled fields (TEST NUMBER, REQUESTED BY, TEST PURPOSE, SPECIAL INSTRUCTIONS, etc.) filled with typed data to capture factual information about a test request and provide manufacturing/testing instructions. Fits "filled or blank fields... for capturing factual data".
11. correspondence: no — no memo/letter header + prose structure.
12. news_article: no.
13. scientific_report: no — no running narrative prose, just structured fields.
14. advertisement: no.
> Runner-up: specification, ruled out because the page is a structured form with labeled fields capturing test request data and instructions, rather than a titled product-analysis table, MSDS, or requirement-language specification document.
> Wait, is there any possibility it's a scientific_report?
"Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."
This page is only labeled field-value entries. So it's a form.
> Final label: form.

---
### `rvl_cdip__specification__0017.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: No newspaper/magazine masthead. No journal running head/volume/issue/page number on this specific page (there is a Bates number "50623 9622" on the right side, and "ASYST Version 2.00 Page 1 A:AL116.RPT 11/17/87 16:00:04.59" at the bottom).
> **Check 1: file_folder**
- Evidence: The page has a lot of data (tables, chamber conditions, analytes). Not just an identifier/stamp.
- Not this check.
> **Check 2: handwritten**
- Evidence: There is a signature "D. L. HEAVNER" and a handwritten signature. But the majority of the content is typed text and data tables.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey questions, rating scales, or transmittal note for a survey.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: No CV/resume content.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal name, volume, issue, page range, DOI, or copyright line belonging to a journal. The bottom text "ASYST Version 2.00 Page 1 A:AL116.RPT 11/17/87 16:00:04.59" is a computer printout header/footer. The right side has a Bates number "50623 9622".
- Not this check.
> **Check 7: FINANCIAL DOCUMENT**
- Evidence: No financial data, invoices, budgets, or monetary amounts. The data is scientific (mass, pressure, temperature, analytes like CO, NOx, etc.).
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
- Evidence: The page contains "TWO HOUR INTEGRATED AVERAGES(BACKGROUND SUBTRACTED)" with "ANALYTE", "TOTAL", "/CIG". It lists CO, NOx, NO, NO2, FID, CO2, PIEZO1, RAM-1, CNC. This looks like mainstream smoke analysis or similar cigarette testing data. "CIGARETTE: 2 1R4F SEMS".
- Wait, check 8 says: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough".
- Let's look at the title/header: "RUN DATE: 23 NOV 87 FILENAME: A:AL116.DAT CIGARETTE: 2 1R4F SEMS". "PORT # PUFF COUNT INITIAL MASS(mg) FINAL MASS(mg) MASS CONSUMED(mg)". "CHAMBER CONDITIONS...". "TWO HOUR INTEGRATED AVERAGES...".
- Is this a specification? Specifications usually have "shall/must" requirement language, or are product formulation/preparation instructions, or Material Safety Data Sheets. Or "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification."
- Wait, check 13: "ORIGINAL RESEARCH WRITE-UP -> scientific_report". "Running narrative prose with objectives, methods, results, or discussion... Also scientific_report: a hand-plotted experimental graph...". This page is just a data printout from a computer program ("ASYST Version 2.00"). It has no running narrative prose.
- Let's re-read check 10: " ADMINISTRATIVE FORM -> form". "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... a filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)".
- This page is a computer printout of analytical data. "ANALYTICAL DATA SUMMARY" is mentioned in check 10 as a filled analytical or lab data sheet -> form.
- Let's check check 8 again: "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification." But this is just a raw data printout from a run date. "RUN DATE: 23 NOV 87 FILENAME: A:AL116.DAT CIGARETTE: 2 1R4F SEMS". It's a data output.
- Let's check check 13 again: "Requires running prose — a page that is only labeled field-value entries (even an 'ANALYTICAL DATA SUMMARY' under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
- This page is essentially a filled analytical or lab data sheet / computer printout of test data. It has labeled fields (PORT #, PUFF COUNT, INITIAL MASS, etc.) and values. It has "CHAMBER CONDITIONS" with values. It has "TWO HOUR INTEGRATED AVERAGES" with analytes and values. It has a signature block at the bottom ("D. L. HEAVNER [signature]").
- This looks like a lab data sheet or analytical data summary. Check 10 explicitly mentions: "a filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)". This page is very similar: it's a printout of analytical data (mass, chamber conditions, analyte averages) with a signature for verification.
- Therefore, it is a form (check 10).
> Let's double check check 8: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification". This page doesn't have a clear "product-analysis table" title like that. It has "RUN DATE...", "TWO HOUR INTEGRATED AVERAGES". It's a raw data output from a system (ASYST).
Check 10: "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells. This also covers: ... a filled analytical or lab data sheet". This fits perfectly. It's a lab data sheet / analytical data printout with a signature.
> Let's review the whole page:
Header: RUN DATE: 23 NOV 87 FILENAME: A:AL116.DAT CIGARETTE: 2 1R4F SEMS
Table 1: PORT #, PUFF COUNT, INITIAL MASS(mg), FINAL MASS(mg), MASS CONSUMED(mg)
Text: CHAMBER CONDITIONS: STATIC MODE/100% FANS 72F/50% RH, PRESSURE(TORR): 743.3, TEMPERATURE(K): 296.8, PIEZO1 LPM: 1.01, PIEZO1 SLPM: .99
Text: TWO HOUR INTEGRATED AVERAGES(BACKGROUND SUBTRACTED)
Table 2: ANALYTE, TOTAL, /CIG. Rows: CO(PPM), NOx(PPM), NO(PPM), NO2(PPM), FID(PPM), CO2(PPM), PIEZO1(UG/M^3), RAM-1(UG/M^3), CNC(#/CC).
Note: OK--SUBJ#1 = D. WINGATE , SUBJ #2 = B. HAMLIN
Signature: D. L. HEAVNER [signature]
Footer: ASYST Version 2.00 Page 1 A:AL116.RPT 11/17/87 16:00:04.59
Bates number: 50623 9622
> This is a laboratory data sheet / analytical data summary. It captures factual data (mass, conditions, analyte concentrations) in a structured format (tables, labeled fields) and has a signature block for verification. This matches "filled analytical or lab data sheet" under check 10 (form).
> Let's check if it could be scientific_report (check 13). Check 13 requires "Running narrative prose with objectives, methods, results, or discussion". This page has NO running narrative prose. It is purely structured data and a signature. Check 13 explicitly says: "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report." So it cannot be scientific_report.
> Could it be specification (check 8)? Check 8 requires "Material Safety Data Sheet... product formulation... manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language." This is a raw data output from a run, not a specification document defining requirements or product composition. It's a lab data sheet.
> So check 10 (form) is the correct match.
> Let's quickly check the other categories just in case.
- advertisement: no
- budget: no
- email: no
- file_folder: no (has real content)
- handwritten: no (majority is typed)
- invoice: no
- letter: no
- memo: no
- news_article: no
- presentation: no
- questionnaire: no
- resume: no
- scientific_publication: no
- scientific_report: no (no running prose)
> Final decision: form.
> Scratchpad summary:
- file_folder: no — the page contains detailed data tables, chamber conditions, and analyte measurements, not just an identifier or stamp.
- handwritten: no — the page is mostly typed text and data tables; only a signature is handwritten.
- fax: no — no fax transmission header or cover sheet.
- questionnaire: no — no survey questions or transmittal.
- resume: no — no career history.
- scientific_publication: no — no journal running head, volume, or issue. The Bates number and footer are archive/program metadata.
- financial: no — no monetary data.
- specification: no — this is a raw data output/printout from a computer program (ASYST), not a specification with "shall/must" language, tolerances, or product formulation.
- presentation: no — not a slide deck or cover page.
- form: yes — the page is a filled analytical or lab data sheet (computer printout of test data: port counts, mass, chamber conditions, analyte averages) with labeled fields, tables, and a signature block for verification. Check 10 explicitly covers "a filled analytical or lab data sheet". Check 13 requires running prose, which is absent here.
- correspondence: no — no memo/letter structure.
- news_article: no — no masthead or journalistic layout.
- scientific_report: no — lacks running narrative prose; it is purely structured data and a signature, which falls under form (check 10) per the instructions.
- advertisement: no.
> Runner-up: scientific_report, ruled out because the page lacks running narrative prose (objectives, methods, results, discussion) and is purely a structured data sheet with a signature, which is explicitly classified as a form (check 10) in the instructions.

---
### `rvl_cdip__specification__0019.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow a specific scratchpad procedure, checking 1-14 in order.
> **Document Analysis:**
- The document contains three tables.
- Table 1: "CASING CROSS-REFERENCE", "Casing: C-407", lists "CUT TOBACCO", "STATUS", "CHANGE NUMBER", "ACTIVE DATE".
- Table 2: "CASING CROSS-REFERENCE", "Casing: C-428", similar columns.
- Table 3: "BLEND CODE CROSS-REFERENCE", "Blend: BW-2117", "Blend: BW-2128", similar columns.
- Bottom right: handwritten signatures/names "Wayne Sandee 9/30/96", "JG Sweeney 5/1/98".
- Bottom right corner: Bates number "398015304".
> **Pre-scan:**
- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: None. Just Bates number at the bottom.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has tables with data (Casing Cross-Reference, Blend Code Cross-Reference), not just an identifier/stamp.
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Mostly typed tables. Handwriting is just signatures at the bottom.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No career history.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal running head, volume, issue, page range.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial data (money, charges, budget lines). It's product/casing/blend cross-references.
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: "CASING CROSS-REFERENCE", "BLEND CODE CROSS-REFERENCE". Lists cut tobacco, casing codes, change numbers, active dates. This looks like product documentation, specifically cross-references for casings and blends. Wait, is it a specification?
- Let's look at check 8: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification".
- This is a cross-reference table for casings and blends. It maps cut tobacco to casing codes and change numbers. This is product documentation / specification data.
- Let's check check 10 first.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... is a form".
- The page has titled data charts/tables: "CASING CROSS-REFERENCE", "BLEND CODE CROSS-REFERENCE". They have rows and columns (CUT TOBACCO, STATUS, CHANGE NUMBER, ACTIVE DATE).
- Wait, check 8 says "test-analysis tables keyed to product/part codes... is a specification". Is this a test-analysis table? No, it's a cross-reference table.
- Check 10 says: "A standalone labeled data chart or table... is a form".
- Let's re-read check 8: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough". This table is a "CROSS-REFERENCE" table, not an analysis table. It's a lookup table.
- Check 10: "This also covers: a standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)..."
- The tables here are labeled data charts/tables. They map product codes (Casing C-407, Blend BW-2117) to cut tobacco and change numbers. This is administrative data capture / reference table.
- Wait, is it a specification? "manufacturing-change authorization... test-analysis tables keyed to product/part codes". A cross-reference of change numbers and active dates for casings/blends is essentially a specification or product documentation record. But it's structured as a table.
- Let's look at the signatures: "Wayne Sandee 9/30/96", "JG Sweeney 5/1/98". This looks like an approval or review sheet for these cross-references.
- Actually, let's look at check 10 again: "internal authorization/approval forms with an approval signature/date block". The signatures at the bottom could be an approval block. But there are no labeled approval blocks like "Approved by:".
- Let's reconsider check 8: "Product-referenced test data is a specification. A titled product-analysis table... is a specification". This is a cross-reference table. Is it a specification?
- Let's look at the labels: "CS68XTOB CS68MAP CASING CROSS-REFERENCE". This is a data table.
- Check 10: "A standalone labeled data chart or table... is a form".
- Let's check if there's any other category.
- What about "form"? "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A standalone labeled data chart or table... is a form".
- The tables have columns: CUT TOBACCO, STATUS, CHANGE NUMBER, ACTIVE DATE. The rows are filled with data. This is a filled data chart/table. So it's a form.
- Wait, is it a specification? "test-analysis tables keyed to product/part codes". This is not a test analysis. It's a cross-reference.
- Let's assume form (check 10).
> Let's re-evaluate check 8 vs check 10.
Check 8: "Material Safety Data Sheet... product formulation... manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language."
Check 10: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... is a form".
The page contains three labeled data tables: "CASING CROSS-REFERENCE" and "BLEND CODE CROSS-REFERENCE". They are standalone labeled data charts/tables. They are filled with data. This fits check 10 perfectly.
> Let's check the signatures. Handwritten signatures at the bottom. "Handwriting filling in labeled printed fields is form, not handwritten". The signatures are just signing off on the document. The document itself is a table.
> So, check 10: ADMINISTRATIVE FORM -> form.
> Let's double check check 1: file_folder. "A page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content". This page has tables, so it's not file_folder.
> Check 10 is the best fit. "standalone labeled data chart or table".
> Wait, could it be a specification? "manufacturing-change authorization". The tables show "CHANGE NUMBER" and "ACTIVE DATE". This tracks changes to casings and blends. But it's presented as a cross-reference table. Check 10 explicitly covers "standalone labeled data chart or table".
> Let's look at the evidence for form:
- "CASING CROSS-REFERENCE" table with columns "CUT TOBACCO", "STATUS", "CHANGE NUMBER", "ACTIVE DATE".
- "BLEND CODE CROSS-REFERENCE" table with similar columns.
- These are standalone labeled data charts/tables filled with data.
- Check 10: "This also covers: a standalone labeled data chart or table... is a form".
> Runner-up: specification. Ruled out because the tables are cross-reference data charts/tables, not test-analysis tables, product formulations, or documents with "shall/must" requirement language. They are administrative data tables.
> Final label: form.

---

## budget → form (4 errors)

### `rvl_cdip__budget__0005.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There's a government seal, "RECIPIENT COMMITTEE CAMPAIGN STATEMENT", "(Government Code Sections 84200-84217)", "Form 420 1985". No newspaper/magazine masthead, no journal running head.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a lot of content: "RECIPIENT COMMITTEE CAMPAIGN STATEMENT", fields for committee name, address, treasurer, etc. It's not just an identifier.
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Most of the content is typed. There is some handwriting (signatures, dates, filling in fields like "1/1/85", "3/17/85", "3/20/85", "San Francisco, CA", "Vigo G. Nielsen, Jr."). But it's filling out a printed form.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: Not a resume.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name/volume/issue/page number.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: It's a "RECIPIENT COMMITTEE CAMPAIGN STATEMENT". It's a legal/regulatory filing form for campaign finance. It's not an invoice or budget in the sense of check 7 (line-item table of charges, internal money planning, etc.). Wait, is it a form? Yes, it's a government form. Let's look at check 10.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No material safety data sheet, product formulation, etc.
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: "Form 420 1985", "RECIPIENT COMMITTEE CAMPAIGN STATEMENT", "(Government Code Sections 84200-84217)". It has fields, boxes, checkboxes ("YES", "NO"), ruled entry lines for capturing factual data (Name of Committee, Address, Name of Treasurer, etc.). It's a filled government form.
- This matches perfectly.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: Not correspondence.
- Not this check.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: Not journalism.
- Not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: Not a research write-up.
- Not this check.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: Not an ad.
- Not this check.
> Let's double check Check 10 vs Check 7.
Check 7: "financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face."
This is a "CAMPAIGN STATEMENT" which is a legal disclosure form. It doesn't have line-item charges for goods/services (invoice) or internal money planning/budget tracking (budget). It's a regulatory filing form. The instructions say: "A research grant application with structured section headings... stays form (this check)". This is a government form (Form 420). It has fields, checkboxes, signature blocks. It is an administrative form.
> Wait, is a campaign finance statement a "statement of account" (budget)?
Check 7 budget: "internal money planning, tracking, or disbursement... a statement of account, a check face or check stub, a check/payment register... Also a provider's periodic customer statement... is budget, not invoice".
But this is a "RECIPIENT COMMITTEE CAMPAIGN STATEMENT" under Government Code. It's a legal compliance form. The primary structure is a form with fields to capture data (committee name, address, treasurer, controlled committee status, candidates, verification). It's not a financial ledger or budget tracking document in the business sense. It's a regulatory form.
Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... A form does NOT have to be blank — a filled form recording data is still a form".
This is definitely a form.
> Let's review the evidence for Check 10:
- "Form 420 1985"
- "RECIPIENT COMMITTEE CAMPAIGN STATEMENT"
- Fields: "NAME OF COMMITTEE", "ADDRESS OF COMMITTEE", "NAME OF TREASURER", "PERMANENT ADDRESS OF TREASURER", checkboxes for "IS THIS A CONTROLLED COMMITTEE? ( ) YES (X) NO", tables for candidates, verification block with signature lines.
- This is a classic administrative/legal form.
> Runner-up: budget. Ruled out because this is a regulatory disclosure form (Government Code Sections 84200-84217) capturing committee identity and status, not an internal money planning, tracking, or disbursement document (budget) or a vendor bill (invoice).
> Final label: form.

---
### `rvl_cdip__budget__0012.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There is a "CONFIDENTIAL Missouri Tobacco Litigation Case No. 972-1465" at the bottom, which is a legal stamp. There is a "RECEIVED ACCOUNTING MAY 17 1993" stamp.
> **Check 1: file_folder**
- Evidence: The page has a title "CHECKLIST Political Campaign Contribution Requests", a "CONTRIBUTIONS POLICY" section, numbered steps, and filled-in fields. It has real content.
- Not this check.
> **Check 2: handwritten**
- Evidence: There is handwriting filling in the fields (e.g., "Missouri", "$250.00", dates, signatures). However, the page is a printed structured form with field labels ("Checklist for ___ requests from ___ (state) totalling $___", "Regional Office:", checkboxes, etc.). The handwriting fills the fields of a printed structured form.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. The "RECEIVED ACCOUNTING" stamp is not a fax transmission header.
- Not this check.
> **Check 4: questionnaire**
- Evidence: Not a survey instrument asking the reader to answer. It's an internal checklist for processing contribution requests.
- Not this check.
> **Check 5: resume**
- Evidence: No career history.
- Not this check.
> **Check 6: scientific_publication**
- Evidence: No journal running head.
- Not this check.
> **Check 7: financial document (invoice/budget)**
- Evidence: Mentions "$250.00", "Account Charged: 1491-7720-00512". But the primary structure is a checklist for processing political campaign contribution requests, not a line-item table, ledger, or statement of charges. It's an internal authorization/checklist form.
- Not this check.
> **Check 8: specification**
- Evidence: No material safety data, product formulation, or "shall/must" requirement language for a product.
- Not this check.
> **Check 9: presentation**
- Evidence: Not a slide deck, cover, or statement.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM**
- Evidence: "CHECKLIST Political Campaign Contribution Requests". It has filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data and tracking a process (Regional Office, State Activities Headquarters, Accounting steps). It has signatures and dates. It is an internal authorization/approval form or checklist for capturing data and tracking a workflow.
- This matches perfectly.
> **Check 11: correspondence**
- Evidence: No TO:/FROM:/RE: memo header followed by prose, no letterhead with external address and salutation.
- Not this check.
> **Check 12: news_article**
- Evidence: No masthead, byline, dateline.
- Not this check.
> **Check 13: scientific_report**
- Evidence: No running narrative prose with objectives, methods, results.
- Not this check.
> **Check 14: advertisement**
- Evidence: No marketing layout, product imagery, slogans.
- Not this check.
> **Conclusion:**
The document is a filled administrative form/checklist for political campaign contribution requests. It has field labels, checkboxes, signatures, and dates. It fits check 10 (form).
> Let's double check check 7. "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." But this is not a billing or payment page. It's a checklist for *requests* for contributions. "Contributions may be made to individual candidate committees only... Contribution checks must be mailed...". It's an internal process checklist. Check 10 covers "internal authorization/approval forms with an approval signature/date block".
> Let's double check check 1. "A page titled 'RECORDS MANAGEMENT INVENTORY' ... is a form". This is a checklist. "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note." This has real content (the checklist text and filled fields).
> So, form is the correct label.
> Runner-up: handwritten. Ruled out because the handwriting merely fills the fields of a printed structured form (checklist with field labels, checkboxes, ruled lines), which stays form (check 10), not handwritten (check 2).
Another runner-up: invoice/budget. Ruled out because the page is a process checklist/authorization form, not a line-item table, ledger, or statement of charges (check 7).
> Final label: form.

---
### `rvl_cdip__budget__0013.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: None. There is a Bates number "65503 5219" at the bottom. There is a notice box at the bottom left.
> **Check 1: file_folder**
- Content: "VARIANCE SHEET", "BRONX & WILLIAMSON - LOUISVILLE", "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE:" followed by a list of checkboxes and handwritten text "throughout rest of file".
- This has real content (a variance sheet with checkboxes and handwritten notes). Not just an identifier/stamp.
- Not file_folder.
> **Check 2: handwritten**
- Most content is typed (checkboxes, instructions). Handwriting is just "throughout rest of file" next to "OTHER (SPECIFY)".
- Not handwritten.
> **Check 3: FAX TRANSMISSION SHEET**
- No "FACSIMILE" or fax header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Not a survey.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Not a resume.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE**
- No journal masthead, volume, issue, page range.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT**
- No financial content.
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
- No material safety data sheet, product formulation, etc.
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
- Let's look at the layout. It's a page with a title "VARIANCE SHEET", some text, checkboxes, and a handwritten note.
- Wait, check 9 has a caveat: "a one-page status/location display sheet — a titled sheet stating where a record range or item is located, printed in slide-style layout with a title, a line of reference numbers, and checkbox-style options (e.g. an "ARCHIVE LOCATION VARIANCE SHEET" listing "THE NUMBER (RANGE) 2060574004-2060574012 IS LOCATED: ( ) IN THE AUDIO CABINET ( ) IN THE VIDEO CABINET ( X ) ON THE OVERSIZE SHELF ...) — is a presentation (this check), not a form."
- This is a "VARIANCE SHEET" for "BRONX & WILLIAMSON - LOUISVILLE". "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE:"
- Checkboxes:
  - DOCUMENT COPIES ARE IN THE SAME SEQUENCE...
  - DUPLICATE DOCUMENTS APPEARED...
  - PAGE NUMBER(S) MISSING...
  - POOR QUALITY ORIGINAL. (checked)
  - OVERLAY ITEM COULD NOT BE REMOVED...
  - NO DOCUMENTS WERE FOUND WITHIN THE ORIGINAL:
    - FILE FOLDER. (checked)
    - REMOVE EXPANDABLE FILE.
    - MANITO FILE.
    - ENVELOPE.
  - OTHER (SPECIFY) (R) throughout rest of file (handwritten)
- This is a status/location display sheet or a variance sheet for reproduction. It's checking off motivations for why a document might be missing or poor quality.
- Wait, is this a form (check 10) or a presentation (check 9)?
- Check 9 caveat: "a one-page status/location display sheet — a titled sheet stating where a record range or item is located, printed in slide-style layout with a title, a line of reference numbers, and checkbox-style options ... is a presentation (this check), not a form."
- This sheet is titled "VARIANCE SHEET". It has checkboxes. It's checking off reasons for variance in reproduction.
- Let's re-read check 9: "a one-page status/location display sheet ... is a presentation (this check), not a form. It presents where something is, rather than capturing data for records."
- This sheet is capturing data about reproduction variance. Is it a form?
- Check 10: "ADMINISTRATIVE FORM -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; ... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
- This sheet has checkboxes and ruled entry lines ("OTHER (SPECIFY) _______________"). It is capturing factual data (motivations for reproduction variance).
- Wait, the caveat in check 9 specifically mentions "ARCHIVE LOCATION VARIANCE SHEET". This is a "VARIANCE SHEET" for reproduction.
- Let's look at the layout. It's a scanned page of a document. The notice at the bottom says "If the file image is less clear than this notice, it is due to the quality of the document being filmed." This is a microfilm/fiche reproduction variance sheet.
- Is it a form? Yes, it has checkboxes and a field for "OTHER (SPECIFY)". It captures data about the reproduction process.
- Let's check check 9 again. "a one-page status/location display sheet ... is a presentation ... not a form. It presents where something is, rather than capturing data for records." This sheet is capturing data (motivations for variance), not just presenting where something is.
- So it's likely a form (check 10).
> Let's re-evaluate check 10: "ADMINISTRATIVE FORM -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
This page has checkboxes (boxes) and a ruled entry line for "OTHER (SPECIFY)". It is filled with handwritten marks (circles/checks) and text "throughout rest of file". This perfectly matches "filled form recording data".
> Let's check if there's any other category.
- email: no
- memo: no
- letter: no
- news_article: no
- questionnaire: no
- resume: no
- scientific_publication: no
- scientific_report: no
- specification: no
- advertisement: no
> So it's form.
> Let's double check check 9 caveat: "a one-page status/location display sheet — a titled sheet stating where a record range or item is located, printed in slide-style layout with a title, a line of reference numbers, and checkbox-style options (e.g. an "ARCHIVE LOCATION VARIANCE SHEET" listing "THE NUMBER (RANGE) 2060574004-2060574012 IS LOCATED: ( ) IN THE AUDIO CABINET ( ) IN THE VIDEO CABINET ( X ) ON THE OVERSIZE SHELF ...) — is a presentation (this check), not a form. It presents where something is, rather than capturing data for records."
This sheet is a "VARIANCE SHEET" for reproduction. It's not stating where a record is located. It's stating motivations for variance in reproduction (e.g., poor quality, overlay item, no documents found). It is capturing data for records (reproduction quality control). So it's a form.
> Evidence for form: "VARIANCE SHEET" title, checkboxes for reproduction motivations (e.g., "POOR QUALITY ORIGINAL", "FILE FOLDER"), and a ruled line for "OTHER (SPECIFY)" filled with handwritten text "throughout rest of file". This is a filled form capturing factual data.
> Runner-up: presentation, ruled out because the sheet is capturing data (reproduction motivations/checkboxes) rather than just presenting a location/status in a slide-style layout, and it has form fields (checkboxes, ruled lines) typical of an administrative form.
> Wait, is there any chance it's a presentation? "printed in slide-style layout with a title, a line of reference numbers, and checkbox-style options". The layout here is a standard document page, not really slide-style. It has a title, a subtitle, a list of checkboxes, and a handwritten note. It looks like a standard form.
> Let's confirm the label: form.
> Check 1: file_folder - no, has content.
Check 2: handwritten - no, mostly typed.
Check 3: fax - no.
Check 4: questionnaire - no.
Check 5: resume - no.
Check 6: scientific_publication - no.
Check 7: financial - no.
Check 8: specification - no.
Check 9: presentation - no, it's a form capturing data.
Check 10: form - yes, checkboxes, ruled lines, filled with data.
> Final label: form.

---
### `rvl_cdip__budget__0015.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There is a Bates number "2024140844" rotated on the right side. No journal masthead.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page contains a large table with financial data (QUARTERLY CLOSING P/E, DISCOUNT TO S&P 400, etc.). It has real content (a table of data).
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: The page is entirely typed text and numbers in a table. No majority handwriting.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax cover sheet header. The Bates number is just a stamp.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions, rating scales, or transmittal note.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No biographical info.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range, or DOI on the page itself.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: The table is titled "QUARTERLY CLOSING P/E" (Price-to-Earnings ratio). It shows years (1980-1993), PM (Philip Morris?), S&P 400, S&P 500, Discount to S&P 400, Discount to S&P 500, Short-term interest. This is financial data, specifically stock market / valuation metrics. Is it an invoice or budget?
- Invoice: Outside vendor charges. No.
- Budget: Internal money planning, tracking, disbursement, forecast vs actual, expense reports, statement of account, check face, check/payment register, or status report whose PRIMARY content is budget and spend tracking. Also covers money-only records.
- Wait, is this a budget? It's a table of historical P/E ratios and discounts. It's financial data. Let's look at the labels. "budget" covers "money-only records: a contribution/expenditure request...". Wait, what about a table of financial metrics?
- Let's re-read check 7: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face."
- "budget: internal money planning, tracking, or disbursement... Also covers money-only records... A provider's periodic customer statement... is budget, not invoice".
- Is this a budget? It's a table of P/E ratios. It's not really a budget, invoice, or statement of account.
- Let's look at check 10: ADMINISTRATIVE FORM -> form. "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... is a form".
- The page is a standalone labeled data chart or table. "QUARTERLY CLOSING P/E" table with rows for years and quarters, and columns for PM, S&P 400, S&P 500, etc.
- Let's check check 10: "This also covers: a standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)..."
- This is a table of financial data (P/E ratios). It's a standalone labeled data chart/table. So it's a form.
- Wait, check 7 says "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)." But this isn't really a money record in the sense of a budget or invoice. It's a table of market data (P/E ratios, discounts, interest rates).
- Let's re-evaluate check 10: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... is a form". This table has rows (Years/Quarters) and columns (PM, S&P 400, etc.) and numeric values. It fits the description of a standalone labeled data chart or table.
- Let's check if there's any other category. "scientific_report"? No running prose. "presentation"? No, it's a dense table.
- So it's likely "form".
> Let's double check check 7. "budget: internal money planning, tracking, or disbursement...". This table is historical market data (P/E ratios for Philip Morris vs S&P 400/500). It's not internal money planning or tracking. It's just a data table.
Check 10: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... is a form". This matches perfectly. The table is labeled "QUARTERLY CLOSING P/E" and has rows and columns of numeric values.
> Let's review the table content:
Headers: YEAR, PM, S&P 400, DISCOUNT TO S&P 400, S&P 500, DISCOUNT TO S&P 500, SHORT-TERM INTEREST.
Rows: 1980 (1-4), 1981 (1-4), ..., 1993 (1-4), Ongoing.
This is a standalone labeled data chart/table.
> Therefore, Check 10 (form) is the correct match.
> Let's quickly check other categories just in case.
- advertisement: No.
- email: No.
- file_folder: No, has a table.
- handwritten: No.
- invoice: No, not a vendor bill.
- letter: No.
- memo: No.
- news_article: No.
- presentation: No, it's a dense data table, not a slide deck. (Check 9 says "A standalone chart or table of values alone is NOT a slide — it is a form (check 10).")
- questionnaire: No.
- resume: No.
- scientific_publication: No journal header.
- scientific_report: No running prose.
- specification: No "shall/must" or product formulation.
> So the label is "form".
> Wait, let's look at the "money-only records" part of check 7. "Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category (amounts need not be legible)." This doesn't fit a P/E ratio table.
Check 10 explicitly says: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... is a form". And "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> The table is exactly a standalone labeled data chart/table.
> Final check of the scratchpad steps:
1. file_folder: no — page has a large data table.
2. handwritten: no — typed table.
3. fax: no — no fax header.
4. questionnaire: no — no survey.
5. resume: no.
6. scientific_publication: no — no journal header.
7. financial: no — not an invoice or budget (it's historical market data/P/E ratios, not internal planning/tracking or vendor billing).
8. specification: no.
9. presentation: no — "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
10. form: yes — "a standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)". The page is a table titled "QUARTERLY CLOSING P/E" with rows for years/quarters and columns for financial metrics (PM, S&P 400, S&P 500, discounts, interest) and numeric values.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no — no running prose.
14. advertisement: no.
> Runner-up: presentation, ruled out because the page is a standalone chart/table of values, which the instructions explicitly state is a form (check 10), not a slide. Or runner-up: scientific_report, ruled out because there is no running narrative prose, only a data table.
> I will use "form".

---

## invoice → form (3 errors)

### `rvl_cdip__invoice__0003.png`
**Expected:** `invoice` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None. There is a "Telefax Copy" header, but it's a fax transmission header, not a mail-client header.
- Masthead or running head: No newspaper/magazine masthead. No journal running head.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a lot of content: "BESTELLUNG" (Order), line items, prices, addresses, dates. Not just an identifier.
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Mostly typed text. Handwriting is just "# 767", "Original an Herr ...", "28.1. 89 g", "Kopie 67", "28.2. 89", and a signature. Not majority handwritten.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: "Telefax Copy" is at the top, but it's not a "FACSIMILE TRANSMISSION" or "FAX COVER SHEET" with To/From/company/phone/page-count fields as the primary structure. Wait, let's look closer. "Telefax Copy" is just a stamp/header. The document itself is a "BESTELLUNG" (Order). A fax cover sheet is a specific form. This is a faxed document. The pre-scan says: "a FAX machine transmission header is NOT a mail-client header... you must classify the underlying document by its own content". The underlying document is an order/invoice.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No CV/resume content.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal running head, volume, issue, page range.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: "BESTELLUNG" (Order) Nr.: 522/88/07656. Line items: "1. 1 Standcontainer", "2. 1 Arbeitstisch", etc. "Gesamtpreis: 12.377,-- netto", "zuzügl. 14 % MwSt". "Wir bestellen aufgrund umseitiger Einkaufsbedingungen". This is a purchase order or an invoice/quote. Wait, "BESTELLUNG" means Order. "Wir bestellen..." (We order...). It references "Ihrem Angebot Nr. 18039 vom 27.Jan.89" (your offer No. 18039 from Jan 27, 89). So this is a purchase order based on a quote.
- Let's re-read check 7: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document...".
- Is a purchase order an invoice? No. But wait, what about "budget"? "internal money planning, tracking, or disbursement...". A purchase order is not internal money planning.
- Let's look at the labels again: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
- Wait, is this a form? "ADMINISTRATIVE FORM -> form". Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... A purchase order is a form? Or is it an invoice?
- Let's re-read check 7 carefully. "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... It does not have to be titled 'INVOICE' — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
- What about a purchase order? "BESTELLUNG" = Order. "Wir bestellen aufgrund umseitiger Einkaufsbedingungen" (We order based on the enclosed purchasing conditions). It lists items and a total price.
- Is there an "invoice" label that covers purchase orders? No.
- Let's check "form": "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application (research grant, employment, service request); a records-management inventory or log table... A form does NOT have to be blank... This also covers: a standalone labeled data chart or table... internal authorization/approval forms with an approval signature/date block."
- A purchase order is a form capturing data (items, quantities, prices).
- Wait, look at the bottom right: "INBIFO Institut für biologische Forschung GmbH...". The document is from INBIFO. It's an order placed BY INBIFO. "Wir bestellen..." (We order...).
- Is it an invoice? No, it's an order.
- Is it a budget? No.
- Is it a form? Yes, it's a structured document with fields for capturing order data (Bestellung Nr., Artikel, Menge, Preis).
- Let's re-evaluate check 7: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." But this is an order, not a billing page. "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget". This is a purchase order from a buyer to a seller.
- Actually, could it be an invoice? Sometimes "Bestellung" is used loosely, but "Wir bestellen" clearly means "We order". The seller's offer is referenced ("Ihrem Angebot Nr. 18039"). So this is a Purchase Order (PO).
- Purchase orders are typically classified as forms if they are structured documents for capturing data, or maybe invoice if the taxonomy is loose? Let's check the labels. There is no "purchase_order" label. The closest is "form" or "invoice".
- Let's look at check 10: "ADMINISTRATIVE FORM -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... A form does NOT have to be blank... This also covers: a standalone labeled data chart or table... internal authorization/approval forms with an approval signature/date block."
- A purchase order is a standard business form. It has ruled lines for "Menge" (Quantity), "Artikel" (Article), "Preis DM" (Price). It is filled out (typed). So it's a form.
- Wait, is there any other category? "invoice" is for "charges owed for goods or services SOLD". This is a purchase order, so it's not an invoice from the seller's perspective. It's a form used by the buyer.
- Let's check if there's any other evidence. "BESTELLUNG Nr.: 522/88/07656". "Gesamtpreis: 12.377,-- netto". "Liefertermin: ca. 9 - 11 Wochen". "Zahlungsweise: 8 Tage 2 % Skonto". This is a standard purchase order form.
- Therefore, check 10 (form) is the best fit.
> Let's double check check 7. "invoice: ... a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document...". This is not a vendor's price schedule (it's a buyer's order referencing a vendor's offer). It's not a receipt. It's not a payment request. It's not an agency estimate.
So check 7 does not apply.
> Check 10: "ADMINISTRATIVE FORM -> form". The page has a structured layout with headers "Menge", "Artikel", "Preis DM", and a numbered list of items. It's a filled form (purchase order).
> Let's review the scratchpad requirements:
- Walk checks 1-14 in order.
- State evidence or "not this check".
- Stop at first matching check.
- Add runner-up label and evidence that ruled it out.
> Check 1: file_folder. No, has body content.
Check 2: handwritten. No, mostly typed.
Check 3: fax transmission sheet. No, "Telefax Copy" is just a stamp on a faxed document, not a fax cover sheet form. The underlying document is a purchase order.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial document (invoice/budget). No, it's a purchase order ("BESTELLUNG", "Wir bestellen"), not an invoice (charges owed) or budget (internal planning). Wait, is a purchase order considered an invoice in this taxonomy? "invoice: an outside vendor, supplier, or agency states charges owed...". A purchase order is the buyer stating what they want to buy. It's not a vendor stating charges owed. So not invoice. Not budget.
Check 8: specification. No.
Check 9: presentation. No.
Check 10: administrative form. Yes. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data...". The page is a purchase order form with ruled lines for quantity, article, price. It captures factual data about an order.
Check 11: correspondence. No.
Check 12: news_article. No.
Check 13: scientific_report. No.
Check 14: advertisement. No.
> Wait, is a purchase order a "form"? Yes, business forms include purchase orders, invoices, receipts, etc. But the taxonomy separates "invoice" (check 7) from "form" (check 10). Check 7 says "Money function overrides form layout: a billing or payment page stays financial...". A purchase order is not a billing or payment page. It's an order. So it falls under "form" (check 10).
> Let's refine the evidence for Check 10:
- Evidence: "BESTELLUNG" (Order) header, structured table with columns "Menge" (Quantity), "Artikel" (Article), "Preis DM" (Price), numbered line items (1-15), and fields for "Gesamtpreis", "Liefertermin", "Zahlungsweise". This is a filled administrative form capturing order data.
> Runner-up: invoice. Ruled out because the document is a purchase order ("BESTELLUNG", "Wir bestellen" - "We order") referencing a vendor's offer ("Ihrem Angebot Nr. 18039"), not a vendor's statement of charges owed for goods sold (invoice).
> Let's check if there's any memo or letter aspect.
Top left: "INBIFO Institut für biologische Forschung GmbH...". Address.
Top right: "INBIFO Vortragsforschung...". Address.
Date: "13.Feb.89".
"Ihr Zeichen: PST/IBM", "Ref. No.: IBM108B23".
"Kopie 67".
This looks like a faxed purchase order. The header "Telefax Copy" and the handwritten notes ("# 767", "Original an Herr...", "Kopie 67") indicate it's a faxed document. But the underlying document is a purchase order form.
Check 3: "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET'... header with To/From/company/phone/page-count fields. Fax sheets are forms, never memo or letter...". This page does not have a fax cover sheet header with those fields. It has "Telefax Copy" stamped on it. The pre-scan says: "a FAX machine transmission header is NOT a mail-client header... you must classify the underlying document by its own content". The underlying document is a purchase order.
> So, form is the correct label.
> Let's re-read check 10 carefully to ensure a purchase order fits.
"Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application (research grant, employment, service request); a records-management inventory or log table... A form does NOT have to be blank... This also covers: a standalone labeled data chart or table... internal authorization/approval forms with an approval signature/date block."
A purchase order is a standard business form. It has ruled entry lines for capturing factual data (items, quantities, prices).
> Is there any chance it's an invoice?
"invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... It does not have to be titled 'INVOICE' — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
This document is titled "BESTELLUNG" (Order). The text says "Wir bestellen aufgrund umseitiger Einkaufsbedingungen" (We order based on the enclosed purchasing conditions). It references "Ihrem Angebot Nr. 18039" (your offer No. 18039). This is definitively a purchase order from the buyer (INBIFO) to the seller. It is not an invoice from the seller. Therefore, it is not an invoice.
> Final check of the steps:
1. file_folder: no - has body content.
2. handwritten: no - mostly typed.
3. fax transmission sheet: no - "Telefax Copy" is a stamp, not a fax cover sheet form. Underlying document is a purchase order.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial document: no - it's a purchase order, not an invoice (vendor billing) or budget (internal planning).
8. specification: no.
9. presentation: no.
10. administrative form: yes - structured purchase order form with ruled lines for data capture.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no.
14. advertisement: no.
> Runner-up: invoice. Ruled out because the document is a buyer's purchase order ("BESTELLUNG", "Wir bestellen") referencing a vendor's offer, not a vendor's statement of charges owed (invoice).
> The label is `form`.

---
### `rvl_cdip__invoice__0006.png`
**Expected:** `invoice` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow a strict set of checks in order, starting with a pre-scan.
> **Pre-scan:**
- Mail-client header block: None. There is a "REQUISITIONER'S COPY" and "PURCHASE ORDER NO. A 21248", "DATE January 21, 1976". No From/To/Sent/Subject.
- Masthead/running head: "The American Tobacco Company" logo at the top left. "REQUISITIONER'S COPY" at top right. No newspaper/magazine masthead, no journal running head.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a lot of content: billing instructions, purchase order number, supplier address, description of posters, price, accounting charge number. Not just an identifier.
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Mostly typed text. There is a handwritten signature at the bottom right and some handwritten annotations (like "T-045" at top right, and a diagonal line). Not majority handwritten.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions, rating scales, or commitment application.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No CV/resume content.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range, DOI.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: This is a Purchase Order. Let's look closely at the definition.
- "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
- "budget: internal money planning, tracking, or disbursement... money-only records... a provider's periodic customer statement..."
- Wait, is a Purchase Order an invoice or budget or form?
- Let's check Check 10: ADMINISTRATIVE FORM -> form.
- "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... A form does NOT have to be blank... internal authorization/approval forms with an approval signature/date block."
- A purchase order is an internal authorization/approval form to buy something. It has fields: Purchase Order No, Date, Req No, To (Supplier), Ship To, Shipment to arrive not later than, Via, Terms, Quantity, Code No, Description, Price.
- Let's re-read Check 7: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." But a purchase order is not a billing or payment page stating charges owed. It's a request to buy.
- "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
- This page is a "PURCHASE ORDER NO. A 21248". It authorizes a purchase. It has an approval signature/date block (signature at bottom right, "Accounting Charge No."). It does not state charges owed by a vendor (it's not an invoice). It's not a budget (internal money planning/tracking, though it has a price, it's a PO).
- Wait, the description says "TARYTON 30-Sheet Posters... @ $9.62 ea." Quantity 2,012. Total price = 2012 * 9.62 = ~19,355.
- Is this an invoice? "an outside vendor... states charges owed". No, this is from The American Tobacco Company (the buyer) to MacNaughton Lithograph Company (the supplier). It's a purchase order.
- Purchase orders are typically forms (administrative forms for procurement).
- Let's check Check 10 again: "internal authorization/approval forms with an approval signature/date block." Yes, a purchase order is an authorization to purchase.
- Let's check if it fits "invoice". No, it's not from a vendor stating charges owed.
- Let's check if it fits "budget". "internal money planning, tracking, or disbursement...". A PO is a commitment, but the caveat says "an internal expenditure-authorization form... is a form (check 10), not budget". A purchase order is exactly an expenditure authorization form.
- So Check 10 is the best fit.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No Material Safety Data Sheet, no product formulation, no "shall/must" requirement language for a product's composition. The description mentions "Overruns or underruns must not exceed 5%." but this is a shipping/quantity condition for a purchase order, not a product specification document. The document is a purchase order for posters.
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck, not a press release, not a photographic slide.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: "PURCHASE ORDER NO. A 21248", "REQUISITIONER'S COPY". Fields for Supplier, Ship To, Quantity, Code No, Description, Price. Accounting Charge No. Signature block. "internal authorization/approval forms with an approval signature/date block". A purchase order is a classic administrative form for capturing procurement data and authorizing an expenditure.
- This matches perfectly.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: No TO:/FROM:/RE: memo header followed by prose. No letterhead with external address + Dear... salutation + closing signature (it has a signature, but it's a form signature, not a letter closing). The "To:" is a field label for the supplier address, not a memo header.
- Not this check.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: No masthead, byline, dateline.
- Not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: No running narrative prose with objectives, methods, results.
- Not this check.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: Not a marketing layout, product imagery, slogans. It's a purchase order.
- Not this check.
> **Conclusion:**
The document is a Purchase Order. Purchase orders are administrative forms used to authorize an expenditure and capture factual data (supplier, items, quantities, prices). The instructions explicitly state: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget". This is a purchase requisition/order (it says "REQUISITIONER'S COPY" at the top right). It has an approval signature. It is a form.
> Let's double check Check 7 vs Check 10.
Check 7: "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
This page is a "REQUISITIONER'S COPY" of a "PURCHASE ORDER". It authorizes a purchase. It has a signature block. It is a form.
> Evidence for Check 10:
- "REQUISITIONER'S COPY"
- "PURCHASE ORDER NO. A 21248"
- Fields: "TO:", "SHIP TO:", "QUANTITY", "CODE NO.", "DESCRIPTION", "PRICE", "ACCOUNTING CHARGE NO."
- Approval signature at the bottom right.
- "internal authorization/approval forms with an approval signature/date block" matches this perfectly.
> Runner-up: invoice. Ruled out because this is a purchase order (buyer to supplier), not an invoice (supplier to buyer stating charges owed). The caveat in check 7 explicitly excludes internal expenditure-authorization forms like purchase/requisition approvals from being budget, pointing them to form (check 10).
> Let's refine the scratchpad.
file_folder: no — page has substantial content (purchase order details, descriptions, pricing), not just an identifier.
handwritten: no — mostly typed text with a signature and minor annotations.
form (check 3): no — no fax header.
questionnaire: no — no survey items.
resume: no — no career history.
scientific_publication: no — no journal identifier.
invoice/budget (check 7): no — this is a purchase order/requisition from the buyer (American Tobacco) to a supplier (MacNaughton Lithograph Company), not a vendor invoice stating charges owed. The check 7 caveat explicitly states that an "internal expenditure-authorization form (purchase/requisition approval...)" is a form, not budget.
specification: no — not a product formulation or MSDS.
presentation: no — not a slide deck or press release.
form (check 10): yes — "REQUISITIONER'S COPY", "PURCHASE ORDER NO.", structured fields for supplier, shipment, quantity, description, price, accounting charge, and an approval signature block. This is an internal expenditure-authorization form / purchase requisition.
correspondence: no — no memo/letter structure.
news_article: no — no journalism layout.
scientific_report: no — no research prose.
advertisement: no — not promotional material.
> Final label: form.

---
### `rvl_cdip__invoice__0014.png`
**Expected:** `invoice` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "THE AMERICAN TOBACCO COMPANY" logo at top left. "REQUISITIONER'S COPY" at top right. No journal masthead.
> **Check 1: file_folder**
- Evidence: The page has a lot of content: billing instructions, supplier info, purchase order number, line items with quantities, descriptions, prices, accounting charge, signature. Not just an identifier/stamp.
- Not this check.
> **Check 2: handwritten**
- Evidence: There is a handwritten name "L. Cannarota" and a signature at the bottom. But the majority of the content is typed (form fields, line items, billing instructions).
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey questions or transmittal note.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: No CV/resume content.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal name, volume, issue, page range, DOI.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: The page is a "REQUISITIONER'S COPY" of a purchase order or invoice. Wait, let's look closer.
- "PURCHASE ORDER NO. M 13174"
- "DATE May 27, 1992"
- "TO: Webcraft Technologies, Inc."
- Line items: "CARLTON Tar Chart 'Reward and Shelter' Direct Mail Units", "400,000", "$787.21/M", "$7,600.00", "Advanced Postage - 3rd Class Bulk Rate - Indicia", "400,000", "($93,200.00)", "Non-Standard Ink Charge", "3", "$250.00/ea".
- "ACCOUNTING CHARGE NO. Marketing Adv. Exp."
- "STATE SALES TAX NOT TO BE CHARGED"
- "Please contact on any questions regarding this Purchase Order."
- This is a purchase order or an invoice/billing document. Let's re-read check 7.
- "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due... It does not have to be titled "INVOICE" — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
- Wait, is this a purchase order (budget/internal) or an invoice (vendor billing)?
- "REQUISITIONER'S COPY" usually implies a purchase requisition or purchase order.
- "PURCHASE ORDER NO. M 13174"
- "TO: Webcraft Technologies, Inc." (Supplier)
- "SHIP TO: Neil 3rd Class Bulk Rate..."
- "F.O.B. Neil June 15, 1992 Complete"
- "TERMS Net 20 Days"
- Line items with quantities, descriptions, prices.
- "ACCOUNTING CHARGE NO. Marketing Adv. Exp."
- "Please contact on any questions regarding this Purchase Order."
- This is a Purchase Order (PO). A PO is an internal document authorizing a purchase. Wait, check 7 says: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget".
- But this has billable charges: "$7,600.00", "($93,200.00)", "$250.00/ea".
- Wait, is a purchase order an invoice or a budget or a form?
- Let's re-read check 7 carefully:
  - "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document... It does not have to be titled "INVOICE" — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
  - "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount... ALSO a provider's periodic customer statement... is budget, not invoice"
  - "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money. But an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
- This document is a "REQUISITIONER'S COPY" of a "PURCHASE ORDER". It lists charges: "$7,600.00", "($93,200.00)", "$250.00/ea". Total isn't explicitly summed at the bottom, but there are line items with prices.
- Wait, is a purchase order an invoice? "an outside vendor... states charges owed". Here, the buyer (American Tobacco Company) is sending a Purchase Order to the vendor (Webcraft Technologies). The vendor will invoice them. Or is this a vendor's invoice sent to the requisitioner?
- "REQUISITIONER'S COPY" suggests it's a copy of the purchase order kept by the person who requisitioned it.
- "BILLING INSTRUCTIONS - MAIL YOUR INVOICES IN DUPLICATE TO CONSIGNEE... MAIL INVOICES TO OUR ADMINISTRATIVE CENTER... AS SHOWN BELOW" -> This is instructions to the vendor on where to mail invoices. This confirms the document itself is a Purchase Order (or requisition) sent to the vendor, telling them what to bill.
- Wait, if it's a Purchase Order, is it a form or a budget?
- Check 7: "an internal expenditure-authorization form... with an approval signature/date block but no billable charges is a form (check 10), not budget". This HAS billable charges (unit prices, quantities).
- "But an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." This is a buyer's document (Purchase Order), not a vendor's document stating charges owed.
- Let's look at Check 10: "ADMINISTRATIVE FORM -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."
- A purchase order / requisition form with line items for quantities, descriptions, prices, accounting charge, and a signature block ("By [signature]") is an internal authorization/approval form or a purchase requisition form.
- Wait, check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." But this is NOT a billing or payment page. It's a purchase order/requisition. The billing instructions say "MAIL YOUR INVOICES...". So this is not the invoice.
- Is it a budget? "budget: internal money planning, tracking, or disbursement... a contribution/expenditure request or approval form whose whole content is an amount...". This is a purchase requisition/order. It has line items, quantities, prices, accounting charge.
- Let's re-read check 7 budget definition: "internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
- This document is a "REQUISITIONER'S COPY" of a "PURCHASE ORDER". It authorizes a purchase. It has an approval signature ("By [signature]"). It has an accounting charge ("Marketing Adv. Exp.").
- Is it a form (check 10) or budget (check 7)?
- Check 10: "internal authorization/approval forms with an approval signature/date block." A purchase requisition/order is an authorization form.
- Check 7 caveat: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money. But an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
- This document HAS billable charges listed (unit prices, quantities, line totals like $7,600.00). Does that make it an invoice? No, because it's not a vendor document stating charges owed. It's a buyer's purchase order. The vendor will send an invoice.
- Wait, could it be an invoice? "REQUISITIONER'S COPY" - usually vendors send invoices to the buyer. If this is a copy of the invoice sent to the requisitioner? No, "PURCHASE ORDER NO. M 13174". It's a purchase order.
- Let's look at the structure: It has fields for Supplier, Ship To, F.O.B., Terms, Quantity, Code No., Description, Price. This is a standard purchase order form.
- Is a purchase order a form or a budget?
- "an internal expenditure-authorization form... is a form (check 10), not budget". Even if it has line items? The caveat says "with an approval signature/date block but no billable charges". This HAS billable charges (prices, quantities).
- But it's not an invoice (vendor billing) and not a budget (internal planning/tracking of spend, like an expense report or check stub). A purchase order is an authorization to buy.
- Let's re-read check 10: "ADMINISTRATIVE FORM -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."
- This is definitely an internal authorization/approval form (a purchase order/requisition form) with an approval signature ("By [signature]") and accounting charge. The presence of unit prices and quantities doesn't make it an invoice (which is a vendor's bill) or a budget (which is internal tracking/planning). It's a form used to authorize and specify a purchase.
- Wait, is there any other category?
- Let's check 7 again: "invoice: an outside vendor, supplier, or agency states charges owed...". This is from American Tobacco Company (buyer) to Webcraft Technologies (vendor). So it's not an invoice from a vendor.
- "budget: ... a contribution/expenditure request or approval form whose whole content is an amount...". This has more than just an amount; it has a full purchase order layout. But is a purchase order a budget? No, budget is "internal money planning, tracking, or disbursement". A PO is an authorization.
- The caveat in check 7 explicitly says: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget". This document is a purchase requisition/approval form. Even though it has prices listed (to tell the vendor what to charge), its primary function is authorization and specification of the purchase, not internal budget tracking or vendor billing. The billing instructions ("MAIL YOUR INVOICES...") confirm this is not the invoice.
- Therefore, it is a form (check 10).
> Let's double check.
- Header: "THE AMERICAN TOBACCO COMPANY", "REQUISITIONER'S COPY", "PURCHASE ORDER NO. M 13174".
- Fields: TO (Supplier), SHIP TO, DATE, REQ. NO., F.O.B., TERMS, QUANTITY, CODE NO., DESCRIPTION, PRICE.
- Content: Line items for "CARLTON Tar Chart...", "Advanced Postage...", "Non-Standard Ink Charge".
- Bottom: "ACCOUNTING CHARGE NO. Marketing Adv. Exp.", checkboxes for tax/exemption, signature "By [signature]".
- This is a Purchase Order / Requisition form.
- Check 10: "internal authorization/approval forms with an approval signature/date block." -> form.
- Check 7: "an internal expenditure-authorization form... is a form (check 10), not budget". Even with line items, it's an authorization form. The vendor will invoice based on this. The document itself is a form.
> Let's review the "invoice" definition in check 7: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD". This document is from the buyer (American Tobacco) to the vendor (Webcraft). It's a Purchase Order. A PO is not an invoice. An invoice is sent by the vendor. The billing instructions say "MAIL YOUR INVOICES...". So this is definitely not an invoice.
> Is it a budget? "budget: internal money planning, tracking, or disbursement...". A PO is a commitment, but the check 7 caveat specifically pulls "purchase/requisition approval" forms into check 10 (form), especially when they have an approval signature block. "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget". This document has billable charges (prices), but it's still a purchase requisition/approval form. The primary structure is a form capturing purchase data (supplier, ship to, items, prices, accounting code) and getting approval (signature). It's a form.
> Let's check if there's any other match.
- Check 1: file_folder. No, has real content.
- Check 2: handwritten. No.
- Check 3: fax. No.
- Check 4: questionnaire. No.
- Check 5: resume. No.
- Check 6: scientific_publication. No.
- Check 7: financial. Invoice? No, it's a PO from buyer to vendor. Budget? No, it's an authorization form, not internal tracking/planning. The caveat says purchase/requisition approval forms are forms.
- Check 8: specification. No.
- Check 9: presentation. No.
- Check 10: form. Yes, "internal authorization/approval forms with an approval signature/date block", "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This is a purchase order form.
- Check 11: correspondence. No.
- Check 12: news_article. No.
- Check 13: scientific_report. No.
- Check 14: advertisement. No.
> Conclusion: form.
> Wait, is there any possibility it's an invoice?
"REQUISITIONER'S COPY"
"PURCHASE ORDER NO. M 13174"
"BILLING INSTRUCTIONS - MAIL YOUR INVOICES IN DUPLICATE TO CONSIGNEE..."
This is 100% a Purchase Order sent to the vendor. The vendor will use this to bill the company. The company keeps this as the requisitioner's copy.
A purchase order is an administrative form.
> Let's confirm the label: "form".
> Scratchpad:
file_folder: no — the page has extensive body content including billing instructions, supplier details, line items, prices, and an approval signature, not just an identifier or stamp.
handwritten: no — majority is typed form fields and text; only a name and signature are handwritten.
invoice: no — although it lists prices and quantities, it is a "PURCHASE ORDER" from the buyer (American Tobacco) to the vendor (Webcraft), with "BILLING INSTRUCTIONS - MAIL YOUR INVOICES...", meaning it is not the vendor's bill for charges owed.
budget: no — it is not internal money planning/tracking or a vendor statement; it is a purchase requisition/order. The check 7 caveat explicitly classifies "purchase/requisition approval" forms as forms (check 10), not budget.
form: yes — it is a structured purchase order/requisition form with fields for supplier, ship-to, quantities, descriptions, prices, accounting charge, checkboxes, and an approval signature block ("By [signature]"). This matches "internal authorization/approval forms with an approval signature/date block" and "filled or blank fields... for capturing factual data".
Runner-up: invoice, ruled out because the document is a buyer's purchase order with billing instructions to the vendor, not a vendor's invoice stating charges owed.
> Final label: form.

---

## scientific_report → form (3 errors)

### `rvl_cdip__scientific_report__0008.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "INBIFO Institut für biologische Forschung · Köln", "17.Okt.89 NDA/MWO QA3145.WM". This looks like an internal document header, not a journal masthead. "BLATT-NR.: 1 von 2". No journal name/volume/issue/page number.
> **Check 1: file_folder**
- Evidence: The page has a title "TITEL: Biological Activity of Formaldehyde and Acrolein...", a table with "ÜBERPRÜFTER PARAMETER" and "BEANSTANDUNG", and approval blocks. It has real content.
- Not this check.
> **Check 2: handwritten**
- Evidence: There is some handwriting (signatures, dates "21.Sep.89", "19.Okt.89"), but the majority of the content is typed text in a structured form (table, fields).
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax cover sheet header. The header is "INBIFO Institut für biologische Forschung · Köln".
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions, rating scales, or transmittal note for a survey.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No CV/resume content.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range, DOI, or copyright line belonging to a journal. The header is an internal institute header.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial line-item table, ledger, or statement.
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No Material Safety Data Sheet, product formulation, or "shall/must" requirement language. This is a QA review.
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck, cover, or press release.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: The page has a structured layout with fields, boxes, and a table for capturing factual data/reviews.
- "ÜBERPRÜFUNG DURCH QA-UNIT" (Review by QA unit).
- Table with columns "ÜBERPRÜFTER PARAMETER" (Reviewed parameter) and "BEANSTANDUNG" (Objection/Comment).
- Rows: "Integrating/Subprotocols", "Subprotocol BC Method", "References allgemein".
- "BEMERKUNG:" (Remark).
- "STELLUNGNAHME" (Statement/Comment) box with a signature.
- "KENNTNISNAHME/STELLUNGNAHME DURCH PROJEKTLEITER: HHM", "TEAM: BC TEAM-MANAGER: HHM", "DATUM/ZN".
- "KENNTNISNAHME DURCH GM: UHA", "DATUM/ZN".
- "VERTEILER: UHA, HHM, QA, RM-BKT".
- This is a QA/parameter review sheet or an internal authorization/review form. It captures data (parameters reviewed, objections, acknowledgments).
- Check 10 explicitly covers: "A form does NOT have to be blank — a filled form recording data is still a form... QA/parameter review sheet."
- Yes, this is a form.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: No TO:/FROM:/RE: memo header followed by prose. No letterhead with external address and salutation.
- Not this check.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: No newspaper/magazine masthead, byline, dateline.
- Not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: No running narrative prose with objectives, methods, results, or discussion. It's a structured review sheet.
- Not this check.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: No marketing layout.
- Not this check.
> **Conclusion:**
The document is a QA review sheet ("ÜBERPRÜFUNG DURCH QA-UNIT") with a table of parameters and objections, and acknowledgment blocks. This fits "administrative form" (check 10), specifically a "QA/parameter review sheet".
> Let's double check check 10: "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells. This also covers: ... a QA/parameter review sheet."
The page has:
- Header: INBIFO Institut für biologische Forschung · Köln, date, reference.
- Box: ÜBERPRÜFUNG DURCH QA-UNIT, P 0500/3145, BLATT-NR.: 1 von 2.
- Title: TITEL: Biological Activity of Formaldehyde and Acrolein...
- Table: ÜBERPRÜFTER PARAMETER | BEANSTANDUNG
- Rows filled with text.
- BEMERKUNG: -
- Date/Signature: 21.Sep.89 QA: DATUM/ZN
- Box: STELLUNGNAHME (with signature)
- Bottom blocks: KENNTNISNAHME/STELLUNGNAHME DURCH PROJEKTLEITER, KENNTNISNAHME DURCH GM, VERTEILER.
This is clearly a form (QA review sheet).
> Runner-up: scientific_report. Ruled out because the page is a structured QA review sheet with labeled fields and a table, not running narrative prose (check 13 requires running prose).
> Final label: form.

---
### `rvl_cdip__scientific_report__0012.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. Just a Bates number "2050056147" on the right side.
> **Check 1: file_folder**
- Evidence: The page has a lot of content: tables, headings like "B L PLANT ANALYTICAL SUMMARY SHEET", "BURLEY", "PRODUCTION DUST", "SLURRY", "FINISHED PRODUCT CHEMICAL ANALYSIS", "FINISHED PRODUCT % OV TARGET", "HOGSHEAD REPORT". It has filled data.
- Not file_folder.
> **Check 2: handwritten**
- Evidence: Most content is filled by hand, but it is filled into a printed structured form with field labels, boxes, and ruled entry lines (e.g., "AVERAGE / S.D.", "TARGET RANGE", "C SHIFT AVG", "GROSS", "REFEED", "ACTUAL").
- Not handwritten (handwriting fills a printed structured form).
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: Not a survey instrument. It's a plant analytical summary sheet.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range, DOI, or copyright line.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial content (no dollar amounts, no billing, no budget tracking). It's plant production/chemical analysis data.
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No "MATERIAL SAFETY DATA SHEET", no product formulation, no "shall/must" requirement language. It's a summary sheet of analytical data.
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck, not a cover, not a press release.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: "B L PLANT ANALYTICAL SUMMARY SHEET". It has filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data. It has sections like "BURLEY", "PRODUCTION DUST", "SLURRY", "FINISHED PRODUCT CHEMICAL ANALYSIS", "FINISHED PRODUCT % OV TARGET", "HOGSHEAD REPORT". It captures analytical data (averages, S.D., targets, actuals). This is a filled analytical or lab data sheet / QA/parameter review sheet / records log.
- Matches check 10: "A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) ... is a form". Also "internal authorization/approval forms with an approval signature/date block" or "QA/parameter review sheet". This is an analytical summary sheet with tables and filled data.
- Let's verify: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... This also covers: ... a filled analytical or lab data sheet ... and internal authorization/approval forms with an approval signature/date block."
- Yes, this is a form.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: No TO/FROM/RE header, no letterhead, no salutation.
- Not this check.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: No masthead, no byline, no multi-column news typography.
- Not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: No running narrative prose. It's a table of data.
- Not this check.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: No marketing layout, no product imagery, no slogans.
- Not this check.
> **Conclusion:**
The document is a "B L PLANT ANALYTICAL SUMMARY SHEET" filled with handwritten data in printed tables and boxes. This perfectly matches the definition of an administrative form (check 10), specifically a filled analytical or lab data sheet or a QA/parameter review sheet capturing factual data.
> Let's double check check 10 vs check 13.
Check 13 requires "Running narrative prose with objectives, methods, results, or discussion". This page has no running prose, only tables and filled cells. So it's not a scientific_report.
Check 10 covers "filled analytical or lab data sheet". This is exactly that.
> Runner-up: scientific_report, ruled out because the page lacks running narrative prose and is instead a structured data-capture sheet with tables and filled cells (form).
> Final label: form.

---
### `rvl_cdip__scientific_report__0003.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, checking each condition in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There is a Bates number "81305509" on the right side, rotated. No journal masthead.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Content: "A AND B COMPOUND RESULTS SUMMARY", "FILE NO: A310", followed by a list of fields: NAME, NREC, SEAC, TESTING STATUS, DECISION TREE, ISS, CHEM ABSTRACTS NUMBER, FEMA NUMBER, PH, MUTAGENICITY VEHICLE, IP VEHICLE, ORAL VEHICLE, IV VEHICLE, SPECIAL INSTRUCTIONS, AWESI, ACUTIX R1.
- This is not just an identifier. It has a title "A AND B COMPOUND RESULTS SUMMARY" and a bunch of data fields. Wait, is it a form? Let's check further. It's not file_folder because it has real content (a summary of compound results with specific data fields).
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Content is typed. Not handwritten.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- No fax header.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Not a survey.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Not a resume.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- No journal identifier on the page.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- No financial content.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- "A AND B COMPOUND RESULTS SUMMARY", "FILE NO: A310", "NAME: BICYCLO[4.4.0]DEC-1-EN-3-ONE".
- This looks like a data summary sheet for a chemical compound. Is it a specification? Specifications have "shall/must" language, or product formulation. This is a results summary. Let's keep checking.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Not a slide deck.
> **Check 10: ADMINISTRATIVE FORM -> form**
- "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... This also covers: a standalone labeled data chart or table... a filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)..."
- The page has labeled fields: NAME, NREC, SEAC, TESTING STATUS, DECISION TREE, ISS, CHEM ABSTRACTS NUMBER, FEMA NUMBER, PH, MUTAGENICITY VEHICLE, IP VEHICLE, ORAL VEHICLE, IV VEHICLE, SPECIAL INSTRUCTIONS, AWESI, ACUTIX R1.
- It is a filled analytical or lab data sheet / compound results summary. It captures factual data about a compound (BICYCLO[4.4.0]DEC-1-EN-3-ONE).
- This fits "form" (check 10).
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- No correspondence structure.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- No.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Requires running narrative prose. This page is just labeled field-value entries (NAME: ..., NREC: ..., etc.). Check 10 explicitly says: "a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
- So this is a form, not a scientific report.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- No.
> Let's re-verify Check 10 vs Check 13.
The page is titled "A AND B COMPOUND RESULTS SUMMARY".
It has fields:
NAME: BICYCLO[4.4.0]DEC-1-EN-3-ONE
NREC:
SEAC:
TESTING STATUS: ACTIVE 11-06-90
DECISION TREE: II 11-21-90
ISS: PENDING 11-06-90
CHEM ABSTRACTS NUMBER: NA
FEMA NUMBER: NA
PH: 5.80 @ 28C
MUTAGENICITY VEHICLE: DMSO
IP VEHICLE:
ORAL VEHICLE: EMUL 12MC; OIL
IV VEHICLE: INSOLUBLE
SPECIAL INSTRUCTIONS: FORMS EMULSION IN 12 MC AND IS SOLUBLE IN CORN OIL
AWESI: PENDING 09-30-91
ACUTIX R1: ORAL PENDING 09-30-91
> This is a structured data capture sheet for a chemical compound's testing status and properties. It perfectly matches "a filled analytical or lab data sheet" or "standalone labeled data chart or table" or "labeled field-value entries" under Check 10 (form).
Check 13 explicitly excludes pages that are "only labeled field-value entries".
> Therefore, the label is `form`.
> Let's double check if there's any other category.
Could it be `scientific_report`? No, no running prose.
Could it be `specification`? No "shall/must" language, not a product change authorization, not an MSDS. It's a results summary / data sheet.
Could it be `file_folder`? No, it has real content (compound data).
> Final check of the text:
"A AND B COMPOUND RESULTS SUMMARY"
"FILE NO: A310"
"BICYCLO[4.4.0]DEC-1-EN-3-ONE"
Bates number: 81305509
> This is a filled form / lab data sheet.
> Label: form.

---

## presentation → form (3 errors)

### `rvl_cdip__presentation__0001.png`
**Expected:** `presentation` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow the scratchpad procedure, walking through checks 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "2071860450" at the bottom right. There's a title "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION". No journal masthead.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a lot of content: a table with "Share of Market", "Share of Segment", "Share of Young Adults", "Price Gaps", "Promotion Incidence", "Trigger Points". It has a title "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION".
- Not file_folder.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: The page is typed throughout. No majority handwriting.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions, rating scales, or transmittal note.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No CV/resume content.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range, DOI, or copyright line belonging to a journal.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: The table contains percentages (51.6, 36.0, 74.4), prices (64¢, 58¢, 60¢, 63¢), and indices (100, 145, 107, 119). It's about "Nielsen Shares, Biweekly Consumer Shares, Nielsen Pricing". It's not a line-item table of charges owed, a ledger, a statement, a voucher, or a check face. It's a data table/chart.
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No Material Safety Data Sheet, product formulation, manufacturing-change authorization, or "shall/must" language.
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: The page is a table of data. Wait, let's look at the layout. It's a table with rows and columns. "Philip Morris USA", "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION", "As of 6/15/98". It has bullet points for rows: "Share of Market", "Philip Morris USA", "Marlboro", etc. Columns: "Trigger 1H 1998", "Latest Data 4WM", "98 O.B.", "FULL YR 1997", "4th QTR 1997".
- Is this a slide? It looks like a printed page from a report or a slide deck printed out. But check 10 says "standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) ... is a form (check 10), not a presentation".
- Wait, let's re-read check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Let's check check 10.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: "A form does NOT have to be blank — a filled form recording data is still a form... This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
- The page is a standalone labeled data chart/table: "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION" with rows like "Share of Market", "Philip Morris USA", "Marlboro", "Premium Category", etc., and columns with numeric values (percentages, prices, indices).
- This fits "standalone labeled data chart or table".
- Let's verify if it's a form. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
- Yes, a data table/chart is classified as a form under check 10.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: No TO:/FROM:/RE: header, no salutation, no closing signature.
- Not this check.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: No masthead, byline, dateline, multi-column news typography.
- Not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: No running narrative prose. It's a table.
- Not this check.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: No product imagery, slogans, brand styling (other than corporate data), coupons, flyers. It's internal business data ("Philip Morris USA", "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION").
- Not this check.
> Let's re-evaluate Check 9 vs Check 10.
Check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
Check 10: "This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
The page is exactly a standalone labeled data chart/table. It has rows (Share of Market, Philip Morris USA, Marlboro, etc.) and columns (Trigger 1H 1998, Latest Data 4WM, etc.) with numeric values.
Therefore, it is a form.
> Wait, is there any other category?
The page is a data table. "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION".
It's a table of data.
Check 10 explicitly covers "a standalone labeled data chart or table".
> Let's double check Check 7 (Financial document).
The table has prices (64¢, 58¢, 60¢, 63¢) and indices (100, 145, 107, 119). But it's not an invoice or budget. It's market share and pricing data from Nielsen. "4WM Nielsen Shares, 3mm Shipment Shares, Biweekly Consumer Shares, Nielsen Pricing". This is market research data, not a financial document like an invoice or budget. Check 7 says "financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This is a data table of market metrics, not a financial statement of charges or budget tracking. So not check 7.
> So the label is `form`.
> Let's review the scratchpad requirements.
- file_folder: no — the page has a table with data, not just an identifier.
- handwritten: no — typed throughout.
- fax: no.
- questionnaire: no.
- resume: no.
- scientific_publication: no.
- financial: no — it's market share and pricing data, not an invoice or budget.
- specification: no.
- presentation: no — "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- form: yes — "a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)". The page is a table of "PM-USA PERFORMANCE TRIGGERS" with rows for market share, segment share, young adults share, price gaps, promotion incidence, and columns for dates/periods with numeric values.
- correspondence: no.
- news_article: no.
- scientific_report: no — no running prose.
- advertisement: no.
> Runner-up: presentation, ruled out because the page is a standalone labeled data chart/table, and check 9 explicitly states "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> Final label: form.

---
### `rvl_cdip__presentation__0003.png`
**Expected:** `presentation` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I need to follow a specific scratchpad procedure, checking 1-14 in order.
> **Document Analysis:**
- The document is rotated 90 degrees counter-clockwise. Let's read it as if rotated.
- Title: "HOW DOES IT WORK? TRADITIONAL APPROACH"
- It's a flowchart/diagram showing a process: "Name Generation" -> "Surveys collected at events/promotion" -> "Responses sent to keying vendor" -> "Responses microfilmed/keyed" -> "Tapes sent to Richmond, Approved by LBCo & Loaded in update onto database" -> "Database Counts, Pull, Mailing Tape Generated - sent to lettershop" -> "Lettershop personalizes" -> "Mailing Drops First class" -> "Mail arrives in consumers home".
- There's a table above the flowchart (which is to the right in the rotated view):
  - Columns: "Date", "Time Elapsed (working time between stages)"
  - Rows: 10/24 (5 days), 10/29 (Approx 28 days), 10/30 - 11/10 (Approx 20 days), 11/11 - 12/1 (10 days), 12/2 - 12/8 (3 days), 12/9 - 12/13 (1 day), 12/14 (On Avg 5 days), 12/21.
  - Box: "TOTAL TIME ELAPSED: BEST CASE (12 WEEKS)"
- Bottom right (rotated): "821418202" (Bates number).
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. Just a title "HOW DOES IT WORK? TRADITIONAL APPROACH" and a Bates number.
> **Check 1: file_folder**
- Almost no body content? No, there is a flowchart, a table with dates and times, and a title. It has real content. Not file_folder.
> **Check 2: handwritten**
- Most content is freeform handwriting? No, it's typed text and a printed diagram. Not handwritten.
> **Check 3: FAX TRANSMISSION SHEET**
- No fax header. Not this.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Asks reader to answer? No. It describes a process ("How does it work? Traditional Approach"). Not a questionnaire.
> **Check 5: PERSON'S CAREER HISTORY**
- Resume? No.
> **Check 6: PUBLISHED EVIDENCE**
- Journal running head? No.
> **Check 7: FINANCIAL DOCUMENT**
- Invoice or budget? No financial data, just dates and days elapsed. Not financial.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
- Specification? No.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Slide/overhead layouts? The layout is a flowchart with a table. It looks like a slide from a presentation or a page from a report explaining a process.
- Let's look at the layout: "HOW DOES IT WORK? TRADITIONAL APPROACH". It's a diagram.
- Is it a presentation? "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page...". This looks like a chart-per-page deck look or a section divider/explanatory slide.
- Wait, let's look at check 10.
> **Check 10: ADMINISTRATIVE FORM**
- Filled or blank fields, boxes, checkboxes? The flowchart has boxes, but they are part of a diagram, not data capture fields. The table has dates and times, but it's informational, not a form to be filled out (it's already filled with dates like 10/24, 10/29). Wait, is it a form? "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) ... is a form". This is a chart/table showing a timeline.
- Let's re-read check 10: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) ... is a form (this check), not a presentation".
- The page has a table: Date | Time Elapsed. And a flowchart.
- Is it a form? A form captures factual data. This page *displays* data (a timeline of a process). It's not a form to be filled.
- Let's look at check 9 again. "Slide/overhead layouts... chart-per-page deck look". This looks exactly like a slide from a presentation explaining a "Traditional Approach" to mailing/surveys. The layout is sparse, diagrammatic.
- Wait, the text says: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- This page has a flowchart AND a table. The table has values (dates, days).
- Let's look at the content. It's explaining a process. "How does it work? Traditional Approach".
- Is it a presentation? "deck title or section-divider page... chart-per-page deck look".
- Let's look at the Bates number: 821418202.
- The layout is very much like a slide or a page from a manual/report.
- Let's reconsider check 10: "A standalone labeled data chart or table... is a form". This is a chart (flowchart) and a table (timeline). But is it an "administrative form"? Forms capture data. This is informational.
- Let's look at check 13: scientific_report. "Running narrative prose...". No prose here.
- Let's look at check 9: "presentation". "Slide/overhead layouts... chart-per-page deck look". This fits well. It's a diagram explaining a process, likely from a presentation or a report. But if it's a report, it needs prose. If it's just a chart, check 10 says "standalone labeled data chart or table... is a form".
- Wait, check 9 says: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- This page has a table (Date, Time Elapsed) and a flowchart. The table has values. So by check 9's caveat, it might be a form (check 10).
- BUT, is it an "administrative form"? Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank... This also covers: a standalone labeled data chart or table...".
- The table here is "Date" and "Time Elapsed". It's not capturing data, it's displaying a schedule.
- However, the rule says "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) ... is a form". This table has rows (dates) and values (days). So it fits the "standalone labeled data chart or table" description in check 10.
- Let's look at the flowchart. It's a process diagram.
- Is there a better fit?
- Let's re-read check 9: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)...". This looks like a chart-per-page deck look.
- But check 9 caveat: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- This page has a table of values (dates and days). So it's not a slide/presentation based on that caveat.
- So it falls to check 10: form. "A standalone labeled data chart or table... is a form".
- Wait, is this a form? A form is for "capturing factual data". This table is already filled with data (10/24, 5 days). "A filled form recording data is still a form".
- The table is a schedule/timeline. Is it a form?
- Let's look at the flowchart boxes. They are boxes. "Filled or blank fields, boxes...". The flowchart has boxes with text inside. But they are not fields for capturing data.
- Let's look at the overall function. It's explaining a process.
- Could it be a presentation? "chart-per-page deck look". The layout is very sparse, large title, diagram, table. It looks like a slide.
- The caveat in check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Does this page have a "standalone chart or table of values alone"? It has a flowchart AND a table. The table is part of the page.
- Actually, the table and flowchart are integrated. The table is above the flowchart (in the rotated view). The table shows the timeline for the steps in the flowchart.
- Step 1: Surveys collected... Date 10/24.
- Step 2: Responses sent... Date 10/29. Time elapsed 5 days.
- This is a Gantt chart or timeline chart.
- Is a Gantt chart a form or a presentation?
- Check 10: "A standalone labeled data chart or table... is a form".
- Check 9: "chart-per-page deck look".
- If it's a chart of values, check 9 says it's a form (check 10).
- Let's look at the content again. It's a process diagram with a timeline.
- Is there any other category?
- What about "scientific_report"? No prose.
- What about "specification"? No.
> Let's reconsider the "form" definition. "administrative form... capturing factual data". This is a diagram explaining a process. It's not really an administrative form.
But the rule says: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) ... is a form (this check)".
This page has a table with rows (dates) and numeric values (days). So it fits this specific bullet in check 10.
Also, the flowchart has boxes. "boxes... for capturing factual data". The boxes here contain text describing steps.
However, often process diagrams in business documents are classified as presentations if they are slide-like, or forms if they are charts/tables.
The rule "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)" is strong.
This page has a table of values (Date, Time Elapsed). So it's not a presentation (check 9).
Therefore, it must be a form (check 10) because of the "standalone labeled data chart or table" rule.
> Wait, is there any other evidence?
The title "HOW DOES IT WORK? TRADITIONAL APPROACH".
It looks like a page from a manual or a presentation slide.
If I have to choose between form and presentation:
- Presentation: chart-per-page deck look.
- Form: standalone labeled data chart or table.
The caveat in check 9 explicitly says: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
This page has a table with values (dates and days). Even though it's integrated with a flowchart, the table is a labeled data chart/table.
So check 10 (form) wins over check 9 (presentation).
> Let's check if it's a "specification" (check 8). No.
Let's check if it's a "scientific_report" (check 13). No prose.
> So the classification is likely "form".
Wait, is there any other category?
What about "file_folder"? No, it has content.
What about "handwritten"? No.
> Let's look closely at the table.
Headers: "Date", "Time Elapsed (working time between stages)".
Rows: 10/24, 10/29, 10/30-11/10, 11/11-12/1, 12/2-12/8, 12/9-12/13, 12/14, 12/21.
Values: 5 days, Approx 28 days, Approx 20 days, 10 days, 3 days, 1 day, On Avg 5 days.
This is a labeled data table.
Check 10: "This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
This matches.
> So the label is "form".
> Let's double check check 9.
"Slide/overhead layouts... chart-per-page deck look... A near-blank cover... is a presentation... EXCEPTION... A large heading rotated 90 degrees... is a section divider... but a rotated SHORT FILING LABEL... is file_folder."
The page is rotated 90 degrees. The text is vertical.
"HOW DOES IT WORK? TRADITIONAL APPROACH" is the title.
The layout is a diagram.
If it were a slide, it would be presentation. But the caveat "A standalone chart or table of values alone is NOT a slide — it is a form" applies.
The table has values. So it's a form.
> Wait, is the whole page a "chart"? Yes, it's a process chart with a timeline table.
Is a process chart a form?
Check 10: "A standalone labeled data chart or table... is a form".
Yes.
> Let's consider if it's a "presentation".
"chart-per-page deck look".
If the table wasn't there, it might be a presentation. But the table makes it a chart/table of values.
The rule is explicit: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
Even if it's not "alone" (it's with a flowchart), the presence of a labeled data table with values pulls it to form.
Actually, the flowchart and table are together. The table provides the dates for the flowchart steps.
It's a single integrated diagram.
But the rule "standalone labeled data chart or table" might apply to the table part.
Let's look at the "form" definition again. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
The boxes in the flowchart are not for capturing data. The table is filled with data. "A filled form recording data is still a form".
So a filled table/chart is a form.
> Therefore, form.
> One more check: Is it a "specification"?
"test-analysis tables keyed to product/part codes...". No.
> Is it a "scientific_report"?
"Requires running prose". No prose.
> So "form" is the best fit among the options, driven by the table/chart rule in check 10 overriding the presentation look in check 9.
> Wait, looking at the layout, it's a flowchart.
Flowcharts are often in presentations or reports.
But the specific rule "A standalone labeled data chart or table... is a form" is a catch-all for charts/tables that don't fit elsewhere.
The table here is "Date" vs "Time Elapsed".
It's a data table.
So form.
> Let's refine the scratchpad.
Check 1: file_folder. No, has content (flowchart, table, title).
Check 2: handwritten. No, typed.
Check 3: fax. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No journal header.
Check 7: financial. No money.
Check 8: specification. No.
Check 9: presentation. Layout is chart-per-page, but caveat: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." The page contains a labeled data table (Date, Time Elapsed) with values.
Check 10: form. "A standalone labeled data chart or table... is a form". The page has a table with dates and days elapsed, and a flowchart with boxes. The table is filled with data.
Runner-up: presentation, ruled out because the page contains a labeled data table with values (dates and time elapsed), and check 9 explicitly states that standalone charts/tables of values are forms, not slides.
> Final label: form.

---
### `rvl_cdip__presentation__0011.png`
**Expected:** `presentation` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> **Image analysis:**
- The image is rotated 90 degrees counter-clockwise. Let's read it as if rotated clockwise.
- Title: "American Key Brand Shares And Percent of Shipments"
- Logo: B&W (Brown & Williamson)
- Chart: A pie chart showing brand shares (Pall Mall, Lucky Strike, Tareyton, Private Stock, Other, Misty Slims, Montclair, Carlton).
- Text at bottom (right side in current orientation): "May 1993 MSA 12mm Share", "SC/DOXSE/AMBER/NT/01-15-93", Bates number "361002052".
- Layout: Large bold title on the left (bottom in current orientation), pie chart in the center, small text at the bottom right (top right in current orientation).
- This looks like a slide from a presentation or a chart from a report. Let's check the rules.
> **Pre-scan:**
- Mail-client header: None.
- Masthead/running head: No newspaper/magazine masthead. No journal running head. Just a Bates number and a small code "SC/DOXSE/AMBER/NT/01-15-93".
> **Check 1: file_folder**
- Evidence: No. There is a chart and a title "American Key Brand Shares And Percent of Shipments". Not just an ID/stamp.
> **Check 2: handwritten**
- Evidence: No. Typed text and a printed chart.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No.
> **Check 4: questionnaire**
- Evidence: No.
> **Check 5: resume**
- Evidence: No.
> **Check 6: scientific_publication**
- Evidence: No journal name/volume/issue on the page itself.
> **Check 7: financial document (invoice/budget)**
- Evidence: No. It's brand shares and percent of shipments, not a bill or budget.
> **Check 8: specification**
- Evidence: No. Not a product formulation or MSDS.
> **Check 9: presentation**
- Evidence: "American Key Brand Shares And Percent of Shipments" is a bold title. There is a pie chart. The layout is sparse, typical of a slide or a chart page in a deck. Wait, let's look at the rules for presentation.
- "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)..."
- "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." -> Wait. "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Let's re-read check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Is this a standalone chart? Yes, it's a pie chart with values.
- Wait, check 10: "This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
- Let's look at the title: "American Key Brand Shares And Percent of Shipments". It's a chart.
- Is it a form? "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) ... is a form (check 10), not a presentation."
- Wait, is a pie chart a "labeled data chart or table"? Yes, it's a chart with labeled data (brand names and percentages/numbers).
- Let's check check 9 again: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- So if it's a standalone chart, it's a form.
- Let's check if there's any other evidence. The text "May 1993 MSA 12mm Share" and "SC/DOXSE/AMBER/NT/01-15-93" looks like a slide footer or a chart caption.
- The B&W logo is present.
- Is it a presentation? "Slide/overhead layouts... chart-per-page deck look". But the rule explicitly says: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Let's re-read carefully: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- This page is a pie chart with brand names and values (1.38, 0.35, 0.44, 0.58, 0.71, 0.77, 1.13, 1.32, 19.8%, 16.1%, 11.5%, 10.6%, 5.2%, 3.7%). It is a chart of values.
- Therefore, it falls under check 10: form. "This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
- Wait, is a pie chart a "labeled data chart or table"? Yes.
- Let's check if there's any other category.
- Could it be a scientific_report? No running prose.
- Could it be a news_article? No.
> Let's re-evaluate "standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
The page contains a pie chart with labels (Pall Mall, Lucky Strike, etc.) and values (1.38, 0.35, etc., and percentages). It has a title "American Key Brand Shares And Percent of Shipments".
This is a labeled data chart. So it is a form.
> Wait, is there any other check?
Check 9: "A near-blank cover or title page... is a presentation... EXCEPTIONS... A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
This page is not a near-blank cover. It's a chart page.
The rule says: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
So this is a form.
> Let's double check check 10: "This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
Yes, a pie chart with brand names and numbers is a labeled data chart.
> Let's check if it could be a presentation.
"Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)..."
But the explicit exception: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
This is a very specific rule. I must follow it.
The page is a chart (pie chart) with values. So it's a form.
> Wait, is there any text that makes it a report? No running prose.
Is there any text that makes it a specification? No.
> Let's review the evidence for form (check 10):
- "standalone labeled data chart or table" -> The page is a pie chart showing brand shares and percent of shipments with specific numerical values for each slice.
- Title: "American Key Brand Shares And Percent of Shipments".
- Footer: "May 1993 MSA 12mm Share", "SC/DOXSE/AMBER/NT/01-15-93", Bates number.
- This is a data chart.
> Runner-up: presentation. Ruled out because the rules explicitly state "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> Let's confirm the rotation. The image is rotated. The text "American Key Brand Shares And Percent of Shipments" is vertical. The B&W logo is at the bottom left (in rotated view). The chart is in the center. The text "May 1993 MSA 12mm Share" is at the bottom right.
This is a standard chart page, likely from a report or a deck, but per the rules, a standalone chart is a form.
> Wait, is it a "labeled data chart"? Yes, it has labels (brand names) and data values (percentages/numbers).
Is it a table? No, it's a chart. But the rule says "standalone labeled data chart or table". So chart is included.
> Final decision: form.
> Let's quickly check if there's any other interpretation.
Could it be a scientific_report? "Requires running prose". No prose here.
Could it be a news_article? No masthead.
Could it be an advertisement? No product imagery/slogans, just a data chart.
> So, form is the correct label.
> Scratchpad:
- file_folder: no — page has a chart and title, not just an ID.
- handwritten: no — typed text and printed chart.
- fax: no.
- questionnaire: no.
- resume: no.
- scientific_publication: no — no journal identifier.
- financial: no — brand shares, not a bill/budget.
- specification: no.
- presentation: no — rule says "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." This page is a standalone pie chart with labeled data values.
- form: yes — "standalone labeled data chart or table" is covered under check 10. The page is a pie chart titled "American Key Brand Shares And Percent of Shipments" with labeled slices (Pall Mall, Lucky Strike, etc.) and numeric values (1.38, 0.35, etc.).
- Runner-up: presentation, ruled out because the instructions explicitly state that a standalone chart or table of values alone is a form (check 10), not a slide/presentation.
> Wait, is there any chance this is a "scientific_report" because it's data? No, "Requires running prose".
Is there any chance it's a "news_article"? No.
> The label is form.

---

## advertisement → form (2 errors)

### `rvl_cdip__advertisement__0003.png`
**Expected:** `advertisement` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. Just a white page with some text at the bottom right.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: There is text "Brand: Lucky 100's", "Publication: News American", "Date: 4/17/74", "Size: 8 1/2 x 14 1/4 (121.1)", "Comments: Ad Warning: 14 pt - sheet", "T & N - 16 pt - 10pt neg". There is also a handwritten number "725".
    *   Is it just an identifier/stamp? No, it has structured data fields (Brand, Publication, Date, Size, Comments). It looks like a form or a data entry page. Wait, let's look closer. It's a small block of text at the bottom right.
    *   Is it a folder tab? No.
    *   Is it a Bates number only? No.
    *   Conclusion: Not file_folder.
> *   **Check 2: handwritten**
    *   Evidence: Most of the content is typed ("Brand:", "Publication:", "Date:", "Size:", "Comments:", "Ad Warning:", "T & N -"). The values are handwritten ("Lucky 100's", "News American", "4/17/74", "8 1/2 x 14 1/4 (121.1)", "14 pt - sheet", "16 pt - 10pt neg"). There is also a handwritten "725".
    *   Is it *majority* handwritten? The printed labels are typed. The values are handwritten. It's a filled form. The rule says: "handwriting merely fills the fields or cells of a printed structured form... stays form".
    *   Conclusion: Not handwritten (it's a filled form).
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header.
    *   Conclusion: Not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No questions, no rating scales.
    *   Conclusion: Not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No.
    *   Conclusion: Not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal header.
    *   Conclusion: Not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: No money amounts, no line items of charges. "14 pt", "16 pt" are font sizes.
    *   Conclusion: Not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: "Brand: Lucky 100's", "Publication: News American", "Size: 8 1/2 x 14 1/4". This looks like an ad specification or layout sheet.
    *   Wait, let's look at Check 8 definition: "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables... tolerances, or 'shall/must' requirement language."
    *   This page specifies ad details: Brand, Publication, Date, Size, Ad Warning font sizes. Is this a specification?
    *   "Product-referenced test data is a specification. A titled product-analysis table... is a specification".
    *   This looks like an ad order form or a layout specification for an advertisement.
    *   Let's check Check 10 (Form) vs Check 14 (Advertisement).
    *   Wait, is this an advertisement? No, it's metadata about an ad.
    *   Let's look at Check 10: "Administrative Form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A standalone labeled data chart or table... internal authorization/approval forms".
    *   This page has fields: Brand, Publication, Date, Size, Comments. It is filled out by hand. It captures factual data about an advertisement placement. This fits "form" (check 10).
> *   **Check 9: SLIDE DECK... -> presentation**
    *   Evidence: Sparse text, but it's a filled form block. Not a slide deck.
    *   Conclusion: Not this check.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: Typed labels "Brand:", "Publication:", "Date:", "Size:", "Comments:", "Ad Warning:", "T & N -". Handwritten values filling these fields. This is a structured data capture sheet (likely an ad order or placement specification form).
    *   Rule: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form".
    *   This matches perfectly. It's a form capturing ad details.
> *   **Check 11: CORRESPONDENCE**
    *   Evidence: No TO/FROM/RE header, no salutation.
    *   Conclusion: Not this check.
> *   **Check 12: PUBLISHED JOURNALISM**
    *   Evidence: No masthead. "News American" is the publication name, not the page itself being a newspaper.
    *   Conclusion: Not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP**
    *   Evidence: No running prose.
    *   Conclusion: Not this check.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: No product imagery, slogans, brand styling (other than text "Lucky 100's"). It's a metadata sheet *about* an ad, not the ad itself.
    *   Conclusion: Not this check.
> **Re-evaluating Check 8 vs Check 10:**
Check 8: "specification". "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables... tolerances, or 'shall/must' requirement language."
This page is about an advertisement ("Publication: News American", "Ad Warning"). It's not a product specification (like cigarette composition). It's an ad placement form.
Check 10: "form". "capturing factual data". This fits an ad order form.
> Let's look at the content again.
Brand: Lucky 100's
Publication: News American
Date: 4/17/74
Size: 8 1/2 x 14 1/4 (121.1)
Comments:
Ad Warning: 14 pt - sheet
T & N - 16 pt - 10pt neg
> This is a form recording ad specifications. It's a form.
> Wait, is there any other category?
"advertisement": Marketing layout. This is not a layout. It's a data entry.
"form": Administrative form. Yes.
> Let's check the labels again.
16 categories: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> The page is a filled form.
Labels: Brand, Publication, Date, Size, Comments.
Values are handwritten.
This is a classic "filled form".
> Let's double check Check 1 (file_folder).
"A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
This has a table-like structure (labels and values). It's real content. So not file_folder.
> Let's double check Check 2 (handwritten).
"handwriting merely fills the fields or cells of a printed structured form... stays form".
So not handwritten.
> Let's double check Check 10 (form).
"Filled or blank fields... for capturing factual data".
Yes.
> Is it a specification (Check 8)?
"Product-referenced test data is a specification. A titled product-analysis table... is a specification".
This is an ad specification (font sizes, paper type "sheet", "neg"). But the category "specification" in this list seems to refer to product/material documentation (MSDS, manufacturing, test analysis).
However, "specification" can also mean technical specs.
But Check 10 says: "A form does NOT have to be blank... internal authorization/approval forms...".
Actually, let's look at the definition of specification (Check 8) again.
"Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
> This page has "Brand: Lucky 100's". It is tied to a product.
It has "Ad Warning: 14 pt - sheet". This is a requirement/specification for the ad layout.
Is it a specification or a form?
Check 8: "specification".
Check 10: "form".
> Let's look at the distinction.
Check 8 is for "Product or Material Documentation". This is an ad layout spec.
Check 10 is for "Administrative Form".
Usually, ad order forms or placement forms are forms.
But if it specifies "14 pt - sheet", "16 pt - 10pt neg", these are technical specifications for the ad.
However, the structure is "Brand: ... Publication: ... Date: ... Size: ... Comments: ...". This is a data capture form.
The text says: "But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
Here we have a product tie-in ("Lucky 100's"). We have requirement language ("Ad Warning: 14 pt...").
But is it a "Product or Material Documentation"?
The label is "specification".
Usually, in these tobacco archives, there are "Ad Specs" or "Layout Specs".
If this is an "Ad Spec" page, is it a specification or a form?
The instructions say: "Judge each page by its FUNCTION... a page full of technical data can still be a form".
"A page about money can still be a form — but a bill is a bill even when it is printed on a form."
Here, the page is capturing data about an ad. It's a form used to record ad details.
The content is "Brand, Publication, Date, Size". This is administrative data for ad tracking/ordering.
The "Comments" section has technical details ("14 pt - sheet").
I lean towards **form** (Check 10) because the primary structure is a set of labeled fields (Brand, Publication, Date, Size) capturing factual data about an ad placement. It looks like a standard administrative form for ad ordering or tracking.
> Let's look at the "specification" definition again.
"Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables... tolerances, or 'shall/must' requirement language."
This page doesn't really have "shall/must". It has "Ad Warning: 14 pt - sheet". This is a note/spec.
But the overall layout is a form with fields.
Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
This page has typed labels and handwritten entries. It is capturing factual data (Brand, Publication, Date, Size).
I will go with **form**.
> Wait, let's look at the "advertisement" category (Check 14).
"Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures."
This is not a marketing layout. It's a metadata page.
> Let's look at "presentation" (Check 9).
"Slide/overhead layouts... sparse text".
This is sparse text, but it's a filled form block. Not a presentation.
> Let's reconsider **form** vs **specification**.
If this is a page from an ad campaign file, recording the details of an ad run.
"Brand: Lucky 100's", "Publication: News American", "Date: 4/17/74", "Size: 8 1/2 x 14 1/4".
This is an ad order form or a media plan entry form.
Function: Capturing factual data about an ad placement.
Category: **form**.
> One more check: Is it a **budget**?
No money amounts.
> Is it a **memo**?
No TO/FROM.
> So **form** is the best fit.
> Let's refine the scratchpad.
1. file_folder: No, has structured content (Brand, Publication, etc.).
2. handwritten: No, typed labels with handwritten values (filled form).
3. fax: No.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No.
7. financial: No.
8. specification: "Brand: Lucky 100's" is a product, but the page is a data capture form for ad placement (Publication, Date, Size). It lacks the "shall/must" or detailed product/material analysis of a specification. It's an administrative record of an ad. Wait, "Ad Warning: 14 pt - sheet" is a spec. But the overall page is a form. Check 10 says "generic labeled chart or table... is an administrative form". This is a labeled form.
9. presentation: No.
10. form: Yes. Typed labels (Brand, Publication, Date, Size, Comments) with handwritten entries. Capturing factual data.
11. correspondence: No.
12. news_article: No.
13. scientific_report: No.
14. advertisement: No, no imagery/slogans, just metadata.
> Final decision: **form**.
> Wait, looking closely at the text:
"Brand: Lucky 100's"
"Publication: News American"
"Date: 4/17/74"
"Size: 8 1/2 x 14 1/4 (121.1)"
"Comments:"
"Ad Warning: 14 pt - sheet"
"T & N - 16 pt - 10pt neg"
"725" (handwritten number)
> This is a form recording ad details.
Label: form.
> One edge case: Is it a **specification** because it specifies the ad layout?
Check 8: "specification... test-analysis tables keyed to product/part codes... tolerances, or 'shall/must' requirement language."
This doesn't have "shall/must". It has "Ad Warning: 14 pt". This is a statement of what is there, or a note.
Check 10: "administrative form... capturing factual data".
The page captures: Brand, Publication, Date, Size. These are factual data points for a record.
I'll stick with **form**.
> Actually, let's look at the "specification" caveat: "But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
Here we have a product tie-in ("Lucky 100's"). We have text "14 pt - sheet", "16 pt - 10pt neg". This is requirement language (specifying font sizes).
So it *could* be a specification.
However, the primary structure is "Brand, Publication, Date, Size". This is an order form or tracking form.
In the tobacco archive context, these are often "Ad Order Forms" or "Media Buying Forms".
Function: Administrative data capture.
I will classify as **form**.
> Let's re-read Check 8 carefully.
"Product or Material Documentation -> specification. Material Safety Data Sheet... product formulation... manufacturing-change authorization, test-analysis tables... tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all... is an administrative form".
The key is "Product or Material Documentation". This page documents an *advertisement*, not the product material itself (like cigarette composition). It documents the *placement* of the ad.
So it's not product/material documentation. It's administrative documentation of an ad campaign.
Therefore, **form**.
> Final check.
Label: form.
Evidence: Typed field labels "Brand:", "Publication:", "Date:", "Size:", "Comments:" filled with handwritten data.
Runner-up: specification, ruled out because the page documents ad placement details (publication, date, size) rather than product composition/material properties or manufacturing changes, and lacks "shall/must" requirement language typical of specs. Or runner-up: advertisement, ruled out because it's metadata about an ad, not the ad itself.
> Actually, looking at the layout, it's very sparse.
Could it be **file_folder**?
"A page is NOT file_folder if it carries any real content... a table... or a note."
This has a table-like structure (labels/values). It's real content.
"A Bates number or archive stamp alone is NOT enough... A page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content".
Here we have text content. So not file_folder.
> Could it be **presentation**?
"Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide".
There is no solid black bar. Just white space.
"near-blank cover or title page... bold headline title".
There is no bold headline title. Just a block of text at the bottom.
So not presentation.
> It is a **form**.
> One detail: "725" is handwritten.
"Brand: Lucky 100's" -> "Lucky 100's" is handwritten.
"Publication: News American" -> "News American" is handwritten.
"Date: 4/17/74" -> handwritten.
"Size: 8 1/2 x 14 1/4 (121.1)" -> handwritten.
"Ad Warning: 14 pt - sheet" -> handwritten.
"T & N - 16 pt - 10pt neg" -> handwritten.
> The printed text is:
"Brand:"
"Publication:"
"Date:"
"Size:"
"Comments:"
"Ad Warning:"
"T & N -"
> This is a printed form with handwritten entries.
Definitely **form**.
> One final check on **specification**.
If this is a "Layout Specification" for an ad.
"Product-referenced test data is a specification."
"A titled product-analysis table... is a specification".
This is not a test data table. It's an ad order/track form.
I'm confident in **form**.
> Wait, is there any chance it's **advertisement**?
No, no imagery.
> Is there any chance it's **news_article**?
"Publication: News American". This is the publication where the ad ran. Not the article itself.
> Final label: form.

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
    *   Wait, let's look at the content. "Brand: Lucky Ten", "Publication: El Diario", "Date: 11/8/74", "Size: 3 1/2 x 7 (24.5 sq.in)".
    *   Is this just an identifier? No, it has specific data about a brand, publication, date, and size. It looks like a note or a log entry.
    *   Wait, is it a folder tab? No, it's just text on a white page.
    *   Is it a form? It has printed labels "Brand:", "Publication:", "Date:", "Size:" and handwritten values.
    *   Let's check Check 2 first.
> *   **Check 2: handwritten**
    *   Evidence: Most of the content is freeform handwriting?
    *   The text is:
        Brand: Lucky Ten
        Publication: El Diario
        Date: 11/8/74
        Size: 3 1/2 x 7 (24.5 sq.in)
    *   The labels "Brand:", "Publication:", "Date:", "Size:" are printed (typed). The values are handwritten.
    *   Wait, looking closely at the image: "Brand:", "Publication:", "Date:", "Size:" look like typed text. The values "Lucky Ten", "El Diario", "11/8/74", "3 1/2 x 7 (24.5 sq.in)" are handwritten.
    *   This is handwriting filling in printed fields.
    *   Rule: "Handwriting filling in labeled printed fields is form, not handwritten".
    *   So not handwritten.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: None. No fax header.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
    *   Evidence: None. Not a survey.
> *   **Check 5: PERSON'S CAREER HISTORY**
    *   Evidence: None.
> *   **Check 6: PUBLISHED EVIDENCE**
    *   Evidence: None.
> *   **Check 7: FINANCIAL DOCUMENT**
    *   Evidence: None. No money.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
    *   Evidence: None.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
    *   Evidence: None.
> *   **Check 10: ADMINISTRATIVE FORM**
    *   Evidence: "Brand:", "Publication:", "Date:", "Size:" are printed field labels. The values are filled in (handwritten).
    *   This is a filled form. It captures factual data (Brand, Publication, Date, Size).
    *   Wait, is it a form? "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
    *   Yes, this looks like a form. Specifically, a data capture sheet for an advertisement or publication placement. "Brand: Lucky Ten", "Publication: El Diario", "Date: 11/8/74", "Size: 3 1/2 x 7". This is metadata about an ad.
    *   Let's check if there's a better fit.
> *   **Check 11: CORRESPONDENCE**
    *   Evidence: None. No TO/FROM/RE header, no letter structure.
> *   **Check 12: PUBLISHED JOURNALISM**
    *   Evidence: None.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP**
    *   Evidence: None. No running prose.
> *   **Check 14: PROMOTIONAL MATERIAL**
    *   Evidence: None. This is a record *about* a promotional material (an ad in El Diario for Lucky Ten), not the ad itself.
> **Re-evaluating Check 1 vs Check 10:**
- Check 1 (file_folder): "Almost no body content: only an archive/Bates number, a stamp, a short label or ID... No sentences, no topical title."
- The page has "1127" (Bates number?) and a block of text.
- The text is:
  Brand: Lucky Ten
  Publication: El Diario
  Date: 11/8/74
  Size: 3 1/2 x 7 (24.5 sq.in)
- This is structured data. It's not just an ID. It's a record of an ad placement.
- Is it a form? Yes, it has printed labels and filled values.
- Let's look at the "handwritten" rule again. "Handwriting filling in labeled printed fields is form, not handwritten".
- The labels "Brand:", "Publication:", "Date:", "Size:" are printed. The content is handwritten.
- So it's a form (Check 10).
> Wait, let's look closer at the text.
"Brand: Lucky Ten" -> "Brand:" is typed, "Lucky Ten" is handwritten.
"Publication: El Diario" -> "Publication:" is typed, "El Diario" is handwritten.
"Date: 11/8/74" -> "Date:" is typed, "11/8/74" is handwritten.
"Size: 3 1/2 x 7 (24.5 sq.in)" -> "Size:" is typed, the rest is handwritten.
> This is a filled form. It captures data.
Is there any other category?
- advertisement: No, this is a record of an ad, not the ad itself.
- news_article: No.
> Let's check the labels again.
form: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
> This fits perfectly. It's a data capture form (likely for ad tracking or media buying).
> Let's check if it could be `file_folder`.
"A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
This page has a note/table of data. It's not just a Bates number. The text block is real content.
So not file_folder.
> Let's check `handwritten`.
"Most of the content is freeform handwriting... NOT on a printed template."
This is on a printed template (labels are printed). So not handwritten.
> So `form` is the best fit.
> Wait, is there any other possibility?
The text "1127" is likely a Bates number.
The content describes an advertisement placement: Brand (Lucky Ten), Publication (El Diario), Date (11/8/74), Size (3.5 x 7 inches).
This is a record of an ad.
Could it be a `specification`? No.
Could it be a `budget`? No money.
> It is a form capturing data about an advertisement.
> Final check of the text:
The labels "Brand:", "Publication:", "Date:", "Size:" are clearly typed in a monospaced font (looks like typewriter or early word processor).
The values are handwritten.
This is a filled form.
> Label: form.
> One detail: "A page whose only prominent printed content is 'APPENDIX N' ... is still questionnaire". Not applicable here.
"A log/diary sheet is freeform... minimal sheet with only ONE typed column header... filled with running narrative". This has multiple headers (Brand, Publication, Date, Size). So it's a form.
> The runner-up might be `handwritten` (because it's mostly handwritten text visually) or `file_folder` (because it's sparse).
- Ruled out `handwritten` because it fills printed fields.
- Ruled out `file_folder` because it has real content (data block), not just an ID.
> Let's confirm the labels.
1. file_folder
2. handwritten
3. form (fax)
4. questionnaire
5. resume
6. scientific_publication
7. invoice/budget
8. specification
9. presentation
10. form (administrative)
11. email/memo/letter
12. news_article
13. scientific_report
14. advertisement
> The label is `form`.
> Wait, looking very closely at the image...
The text "Brand:", "Publication:", "Date:", "Size:" looks like it might be typed.
Actually, looking very closely at crop 4 and crop 1...
"Brand:" is typed. "Lucky Ten" is handwritten.
"Publication:" is typed. "El Diario" is handwritten.
"Date:" is typed. "11/8/74" is handwritten.
"Size:" is typed. "3 1/2 x 7 (24.5 sq.in)" is handwritten.
> Yes, printed labels, handwritten entries. This is a filled form.
> One edge case: Is this a `specification`?
"Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables keyed to product/part codes... tolerances, or 'shall/must' requirement language."
No.
> Is this an `advertisement`?
"Marketing layout: product imagery, slogans... Judge by DOMINANT content".
The dominant content is a data record about an ad, not the ad itself. The ad would be the image in El Diario. This is a log entry.
> So `form` is correct.
> Let's double check Check 10 description:
"Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
This matches perfectly.
> Runner-up: `handwritten`. Ruled out because the handwriting fills printed field labels ("Brand:", "Publication:", etc.), making it a filled form, not freeform handwriting on blank paper.
Another runner-up: `file_folder`. Ruled out because the page contains a structured data block (Brand, Publication, Date, Size) describing a specific item, not just a filing ID or stamp.
> Final decision: form.

---

## invoice → budget (2 errors)

### `rvl_cdip__invoice__0001.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is a "RECEIPT MAIL REGISTE 1174" stamp and a "DATE-IN 19.12.93" stamp. These are filing stamps, not email headers.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head with volume/issue/page number. There is a Bates number "2028741084" at the bottom right. There is a "DATE-IN" stamp.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a lot of content. It has a company name "SLOUGH PROPERTIES N.V.", address details, a table with "Omschrijving", "Periode", "Bedrag", "Totaal te betalen". It has a "REKENING NR. 930058". It's not just an ID or stamp.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: Mostly typed text. There are some black smudges/blacks out, but no significant handwriting.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. The "DATE-IN" and "RECEIPT MAIL" are stamps.
    *   Result: not this check.
> *   **Check 4: questionnaire**
    *   Evidence: No survey questions.
    *   Result: not this check.
> *   **Check 5: resume**
    *   Evidence: No career history.
    *   Result: not this check.
> *   **Check 6: scientific_publication**
    *   Evidence: No journal identifier.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: The page is titled/structured as a bill/invoice.
    *   "SLOUGH PROPERTIES N.V." (company name).
    *   "C.R.C. CONTRACT RESEARCH CENTER BVBA" (recipient).
    *   "Brussel, 01/04/1993" (date).
    *   "REKENING NR. 930058" (Invoice Number / Account Number). "Rekening" is Dutch for Invoice/Account.
    *   Table columns: "Omschrijving" (Description), "Periode" (Period: 01/04/1993 tot 30/06/1993), "Bedrag" (Amount: 669060 - likely cents or a specific currency unit, actually 6690.60 maybe? Wait, 669060. Let's look closer. "Bedrag 669060", "Totaal te betalen 669060". "Totaal te betalen" means Total to pay).
    *   "Omschrijving: huur" (Description: rent).
    *   This is a bill for rent ("huur") for a period. It's a statement of charges.
    *   Let's check the rules for invoice vs budget.
    *   "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher... a receipt... an agency/vendor ESTIMATE document...".
    *   "budget: ... a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
    *   Wait, let's re-read carefully.
    *   "A hotel/motel guest bill or folio ... is an invoice".
    *   "A provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer ... is budget, not invoice".
    *   This is a rent bill ("huur"). Rent is a periodic service/lease charge.
    *   "SLOUGH PROPERTIES N.V." is the landlord/property manager. "C.R.C. CONTRACT RESEARCH CENTER BVBA" is the tenant.
    *   "huur" = rent.
    *   Period: 01/04/1993 tot 30/06/1993 (3 months).
    *   Amount: 669060.
    *   Is this an invoice or a budget?
    *   Rule: "A provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
    *   Rent is a periodic charge for an ongoing account (lease). So this looks like **budget**.
    *   Let's check the invoice definition again: "goods sold or one-off services performed". Rent is ongoing.
    *   Let's check the budget definition again: "budget: internal money planning, tracking, or disbursement... Also covers money-only records: ... a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer ... is budget, not invoice".
    *   This fits "provider's periodic customer statement" (rent bill).
    *   Wait, is "huur" (rent) considered a bill for goods/services sold (invoice) or a periodic statement (budget)?
    *   Usually, a rent invoice is an invoice. But the rule specifically says: "a provider's periodic customer statement... is budget, not invoice". Rent is a periodic statement.
    *   Let's look at the "invoice" bullet: "an outside vendor... states charges owed...".
    *   Let's look at the "budget" bullet: "a provider's periodic customer statement... is budget".
    *   The document is "REKENING NR. 930058". "Rekening" means invoice/account.
    *   The description is "huur" (rent).
    *   This is a bill for rent.
    *   Let's re-evaluate "invoice" vs "budget".
    *   Invoice: "goods sold or one-off services performed". Rent is a recurring service (leasing space).
    *   Budget: "provider's periodic customer statement... is budget".
    *   This is a statement of charges for rent (ongoing account). So it should be **budget**.
>     *   Wait, let's look at the structure. It's a single line item "huur" for a period.
    *   Is it a form? No, it's a financial document.
    *   Let's look at Check 10 (Form). "A form does NOT have to be blank... It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)." So it's Check 7.
>     *   Let's reconsider Invoice vs Budget.
    *   Invoice: "an outside vendor... states charges owed for goods or services SOLD".
    *   Budget: "provider's periodic customer statement... is budget".
    *   Rent is a periodic charge. The period is 01/04/1993 to 30/06/1993. This is a quarterly rent bill.
    *   Therefore, it is a periodic customer statement -> **budget**.
>     *   Wait, is there an argument for Invoice?
    *   "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document...".
    *   "A hotel/motel guest bill ... is an invoice".
    *   Rent bill: Usually considered an invoice in accounting (Invoice for rent). But the specific rule says "provider's periodic customer statement... is budget".
    *   Let's look at the text: "SLOUGH PROPERTIES N.V." (Landlord). "C.R.C. CONTRACT RESEARCH CENTER BVBA" (Tenant).
    *   "Gebouw: PLANET I TOLLAAN 101 C...". Building details.
    *   "Omschrijving: huur" (Description: rent).
    *   "Periode: 01/04/1993 tot 30/06/1993".
    *   "Bedrag: 669060". "Totaal te betalen: 669060".
    *   This is a rent statement.
    *   According to the prompt: "a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice".
    *   Rent is like a utility or subscription (ongoing account). So **budget**.
>     *   Let's check if there's any other category.
    *   Form? No, it's a financial document. Check 7 overrides Check 10 for money records.
>     *   Wait, let's look at the "invoice" definition again. "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD". Rent is a service (leasing). But the "budget" definition has a specific carve-out for periodic statements.
    *   "budget: ... Also covers money-only records: ... a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer ... is budget, not invoice".
    *   This is exactly a periodic customer statement (rent for 3 months). So **budget**.
>     *   Let's look at the label "invoice". Is a rent bill an invoice? Yes, legally. But the prompt's classification rules say periodic statements are budget.
    *   Let's look at the label "form". Is this a form? It has a table. But Check 7 says "billing documents are invoice (check 7), and money-only forms are budget (check 7)". So it's not form.
>     *   Let's reconsider the "invoice" definition. "an agency/vendor ESTIMATE document... is the agency's BILL for a client job — invoice, not budget". This is not an agency estimate. This is a property management bill.
    *   "A hotel/motel guest bill... is an invoice". A hotel bill is for a specific stay (one-off service performed). Rent is for a period (ongoing account).
    *   The rule: "provider's periodic customer statement... is budget".
    *   So **budget** seems correct.
>     *   Wait, is it an **invoice**?
    *   "REKENING NR." means Invoice Number.
    *   "Totaal te betalen" means Total to pay.
    *   In many contexts, a rent invoice is an invoice.
    *   But the prompt is very specific: "a provider's periodic customer statement... is budget, not invoice".
    *   Let's assume the prompt's specific rule overrides general knowledge.
    *   The document is a statement of charges for rent (ongoing account). -> **budget**.
>     *   Let's look at the "invoice" bullet again. "invoice: ... a payment voucher ... a receipt ...". This isn't a receipt (it's a bill to pay). It's not a voucher (usually internal).
    *   It's a "REKENING" (Invoice/Statement).
    *   If I have to choose between invoice and budget based on the text:
    *   Text: "huur" (rent), "Periode" (period). This is a periodic statement. -> **budget**.
>     *   Let's check if it could be a **form**.
    *   Check 10: "Administrative Form... Filled or blank fields...".
    *   Check 7: "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
    *   So if it's a billing document, it's Check 7.
>     *   Let's refine the Invoice vs Budget decision.
    *   Invoice: "goods sold or one-off services performed".
    *   Budget: "provider's periodic customer statement... statement of charges for an ongoing account".
    *   Rent is an ongoing account. The period is 3 months.
    *   So **budget**.
>     *   Wait, is there any other evidence?
    *   "SLOUGH PROPERTIES N.V."
    *   "C.R.C. CONTRACT RESEARCH CENTER BVBA"
    *   "Brussel, 01/04/1993"
    *   "REKENING NR. 930058"
    *   Table: Omschrijving (huur), Periode (01/04/1993 tot 30/06/1993), Bedrag (669060), Totaal te betalen (669060).
    *   This is a rent bill.
    *   According to the prompt: "a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer ... is budget, not invoice".
    *   So **budget**.
>     *   Let's double check if "invoice" is a better fit.
    *   "invoice: an outside vendor... states charges owed...".
    *   The prompt says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form...".
    *   The prompt says: "invoice: ... an agency/vendor ESTIMATE document ... is the agency's BILL ... invoice, not budget".
    *   The prompt says: "budget: ... a provider's periodic customer statement ... is budget, not invoice".
    *   This is a periodic statement (rent for Q2 1993). So **budget**.
>     *   Wait, could it be **invoice**?
    *   Some might argue a rent bill is an invoice. But the prompt's calibration rules are specific. "provider's periodic customer statement... is budget".
    *   I will go with **budget**.
>     *   Wait, let's look at the label list. `invoice`, `budget`.
    *   Is there a chance it's **form**?
    *   No, Check 7 overrides.
>     *   Let's look at the "invoice" definition again. "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD".
    *   Rent is a service. But it's periodic.
    *   The "budget" definition explicitly captures "periodic customer statement".
>     *   Let's consider the source. Tobacco industry archive. C.R.C. is Contract Research Center. Slough Properties is the landlord.
    *   This is a bill from the landlord to the tenant.
    *   Landlord bills are periodic statements (rent, utilities).
    *   So **budget**.
>     *   Wait, is there any chance this is a **form**?
    *   "administrative form... filled or blank fields...".
    *   But Check 7 says money records are invoice/budget.
>     *   Let's look at the "invoice" example in the prompt: "an agency estimate change order... is invoice".
    *   This is not an agency estimate.
>     *   Final decision: **budget**.
>     *   Wait, let's look at the text "REKENING NR.". "Rekening" is Dutch for Invoice.
    *   In Dutch, "Rekening" is used for both Invoice and Statement of Account.
    *   "Maandelijkse rekening" = Monthly statement (Budget per prompt rules).
    *   "Factuur" = Invoice (goods sold).
    *   Here it says "REKENING NR.". And the content is "huur" (rent) for a period.
    *   This is a statement of account for rent.
    *   Prompt rule: "provider's periodic customer statement... is budget, not invoice".
    *   So **budget**.
>     *   Let's check if there is any other category.
    *   Letter? No.
    *   Memo? No.
>     *   Wait, is it a **form**?
    *   Check 10: "administrative form...".
    *   Check 7: "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
    *   So if it's money, it's 7.
>     *   Is it **invoice**?
    *   If I treat "huur" (rent) as a service sold, it could be invoice.
    *   But the period "01/04/1993 tot 30/06/1993" makes it periodic.
    *   The rule "provider's periodic customer statement... is budget" is very specific.
    *   I'll stick with **budget**.
>     *   Actually, let's re-read the invoice definition carefully.
    *   "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due...".
    *   "budget: ... a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice".
    *   Rent is like a utility/subscription (ongoing account).
    *   So **budget**.
>     *   One more check: Is it a **specification**? No.
    *   **Presentation**? No.
>     *   Wait, look at the layout. It has a black bar at top and bottom.
    *   "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide... presentation".
    *   But this page has dense text (addresses, table). It's not sparse.
    *   The black bars are likely scanning artifacts from a bound document or just borders.
    *   The content is clearly a financial document.
>     *   Let's look at the "DATE-IN" stamp. "19.12.93".
    *   "RECEIPT MAIL REGISTE 1174".
    *   These are filing stamps.
>     *   So, Check 7 -> Budget.
>     *   Wait, is it an **invoice**?
    *   If the prompt considers "REKENING" (Invoice) as the key...
    *   But the content is "huur" (rent) for a period.
    *   The prompt says: "a provider's periodic customer statement... is budget, not invoice".
    *   This is the key. Even if it says "Rekening" (Invoice), if it's a periodic statement for an ongoing account (rent), it's budget.
    *   Example given: AT&T "MONTHLY INVOICE" is budget.
    *   Here we have a rent statement for 3 months. It's a periodic statement. -> **budget**.
>     *   Let's consider if it's **invoice** because it's a "bill".
    *   "Money function overrides form layout: a billing or payment page stays financial...".
    *   "invoice: ... a hotel/motel guest bill ... is an invoice: it bills for a one-off service performed (lodging), not a periodic account statement."
    *   This is the contrast! Hotel bill (one-off stay) = invoice. Rent (periodic account) = budget.
    *   This document is rent ("huur") for a period ("Periode: 01/04/1993 tot 30/06/1993").
    *   So it is a periodic account statement. -> **budget**.
>     *   Final conclusion: **budget**.

---
### `rvl_cdip__invoice__0017.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "93219883" and some text.
> **Check 1: file_folder**
- Evidence: The page has a lot of content. It's a check. "LOEWS CLEARING CORPORATION", "THE CHASE MANHATTAN BANK N.A.", "PAY TO THE ORDER OF", "The sum of 131,416.00", "3-15-82 COUNCIL FOR TOBACCO RESEARCH-U.S.A. INC". It's a check face/stub. Not file_folder.
> **Check 2: handwritten**
- Evidence: Mostly typed, some handwritten-looking text but it's a printed check. Not handwritten.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax header.
> **Check 4: questionnaire**
- Evidence: No survey instrument.
> **Check 5: resume**
- Evidence: No career history.
> **Check 6: scientific_publication**
- Evidence: No journal masthead.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: This is a check. "LOEWS CLEARING CORPORATION", "THE CHASE MANHATTAN BANK N.A.", "No 4506", "AMOUNT 131,416.00", "PAY TO THE ORDER OF The sum of 131,416.00", "3-15-82 COUNCIL FOR TOBACCO RESEARCH-U.S.A. INC".
- Check 7 says: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register..."
- "A check face/check stub stays budget even when the detachable stub's columns are headed..."
- This is a check face. So it's budget.
> **Check 8: specification**
- Evidence: No.
> **Check 9: presentation**
- Evidence: No.
> **Check 10: form**
- Evidence: No.
> **Check 11: correspondence**
- Evidence: No.
> **Check 12: news_article**
- Evidence: No.
> **Check 13: scientific_report**
- Evidence: No.
> **Check 14: advertisement**
- Evidence: No.
> Let's double check Check 7.
"budget: ... a check face or check stub, a check/payment register ... ALSO a provider's periodic customer statement ... is budget, not invoice"
The document is clearly a check from "THE CHASE MANHATTAN BANK N.A." to "COUNCIL FOR TOBACCO RESEARCH-U.S.A. INC" for $131,416.00.
Therefore, it is a check face, which falls under budget.
> Let's review the scratchpad rules for Check 7:
"budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking."
Yes, a check face is explicitly listed as budget.
> Runner-up: invoice. Ruled out because a check face records a disbursement from a payment instrument, not a vendor bill for goods or services (check 7 caveat: "A check face/check stub stays budget even when...").
> Final label: budget.

---

## budget → invoice (2 errors)

### `rvl_cdip__budget__0008.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING". This is a company logo/header, not a newspaper/magazine masthead or journal running head. "ESTIMATE RECAP - PM01(D)".
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a lot of content: a table with products, periods, gross amounts, gross change, gross less C/D. It has a header "LEO BURNETT U.S.A.", "ESTIMATE RECAP".
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: Typed text throughout. No significant handwriting.
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
    *   Evidence: "LEO BURNETT U.S.A. ADVERTISING", "ESTIMATE RECAP - PM01(D)". "CLIENT: P.M. INC.", "EST NO: 9118 REVISES EST DTD 01/13/89". "DESC: 702A CAMBRIDGE SUPPLEMENTS". Table with "PRODUCT", "PERIOD", "GROSS AMOUNT", "GROSS CHANGE", "GROSS LESS C/D". Totals: 288,577.48 and 283,671.68.
    *   Analysis: This is an agency estimate/recap. Let's look at the rules for invoice vs budget.
    *   Invoice rule: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
    *   Budget rule: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job... plans projected spend rather than billing completed work, so it is budget, not invoice".
    *   Here we have: "EST NO: 9118 REVISES EST DTD 01/13/89". This names an estimate number and revises a prior estimate. It has columns "GROSS AMOUNT", "GROSS CHANGE", "GROSS LESS C/D". This looks like billing/reconciliation.
    *   Wait, let's look closer. "EST NO: 9118 REVISES EST DTD 01/13/89". "DESC: 702A CAMBRIDGE SUPPLEMENTS".
    *   The table shows "TOTALS BY PRODUCT/MONTH ON SALE DATE". Product: 32-CAMBRIDGE. Periods: APR 1989, MAY, QUARTER 2, SEP, QUARTER 3, OCT, QUARTER 4.
    *   Gross Amount: 144,288.74. Gross Change: 72,144.37. Gross Less C/D: 141,835.84.
    *   This is an estimate recap that revises a prior estimate ("REVISES EST DTD..."). It has an estimate number ("EST NO: 9118"). It compares amounts (Gross Amount vs Gross Change vs Gross Less C/D). This fits the invoice definition: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")..."
    *   Wait, is it an invoice? "invoice: ... an agency/vendor estimate or recap that names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
    *   Yes, "EST NO: 9118 REVISES EST DTD 01/13/89" matches "names an estimate number" and "revises a prior estimate".
    *   So it's an invoice.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: Not a material safety data sheet or product formulation.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: Not a slide deck.
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: It has a form number at the bottom left "FORM M-01 REV 05-82". But check 7 says money function overrides form layout. "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
    *   Result: not this check (because check 7 matches first).
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: No TO/FROM/RE header followed by prose.
    *   Result: not this check.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: No newspaper/magazine masthead (Leo Burnett is an ad agency).
    *   Result: not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: No running narrative prose.
    *   Result: not this check.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: Not a single brand ad. It's an internal/agency financial document.
    *   Result: not this check.
> **Re-evaluating Check 7 (Invoice vs Budget):**
The document is "ESTIMATE RECAP - PM01(D)".
Header: "CLIENT: P.M. INC.", "EST NO: 9118 REVISES EST DTD 01/13/89".
Table columns: "GROSS AMOUNT", "GROSS CHANGE", "GROSS LESS C/D".
Totals: 288,577.48 and 283,671.68.
The text says: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns..."
This document has "EST NO: 9118" and "REVISES EST DTD 01/13/89". It has columns comparing amounts. It is an invoice.
> Wait, is there any other check?
Check 10: "FORM M-01 REV 05-82". It is a form. But check 7 says "Money function overrides form layout". So if it's financial, it's invoice/budget.
Is it budget? "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job... plans projected spend rather than billing completed work, so it is budget, not invoice".
This document HAS an estimate number ("EST NO: 9118") and revises a prior estimate ("REVISES EST DTD..."). So it is NOT just planning future work; it's revising a prior estimate, which makes it an invoice (billing document).
> Therefore, the label is invoice.
> Let's double check the "invoice" definition.
"invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement with unit prices, amounts, and totals. It does not have to be titled "INVOICE" — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice. Look for goods sold or one-off services performed (items, quantities, unit prices). An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
> The document is titled "ESTIMATE RECAP".
It has "EST NO: 9118 REVISES EST DTD 01/13/89".
It has columns "GROSS AMOUNT", "GROSS CHANGE", "GROSS LESS C/D".
This perfectly matches the invoice criteria for an agency estimate/recap.
> Final check of the scratchpad steps:
1. file_folder: No, has table content.
2. handwritten: No, typed.
3. fax: No.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No.
7. financial (invoice/budget): Yes. Specifically invoice because "EST NO: 9118 REVISES EST DTD 01/13/89".
8. specification: No.
9. presentation: No.
10. form: No, overridden by check 7.
11. correspondence: No.
12. news_article: No.
13. scientific_report: No.
14. advertisement: No.
> Runner-up: budget. Ruled out because the document names an estimate number ("EST NO: 9118") and revises a prior estimate ("REVISES EST DTD 01/13/89"), which makes it an invoice (billing document) rather than a pure planning budget.
> Wait, looking closely at the image:
"LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING"
"MAGAZINE ESTIMATE RECAP - PM01(D)"
"PERIOD 01/01/89 TO 12/31/89"
"DATE 02/10/89"
"PAGE 1"
"CLIENT: P.M. INC. OFFICE: 10"
"DESC: 702A CAMBRIDGE SUPPLEMENTS"
"EST NO: 9118 REVISES EST DTD 01/13/89"
"SB2"
> Table:
"TOTALS BY PRODUCT/MONTH ON SALE DATE"
PRODUCT | PERIOD | GROSS AMOUNT | GROSS CHANGE | GROSS LESS C/D
32-CAMBRIDGE | APR 1989 | 144,288.74 | 72,144.37 | 141,835.84
| MAY | .00 | 72,144.37- | .00
| QUARTER 2 | 144,288.74 | | 141,835.84
| SEP | 72,144.37 | | 70,917.92
| QUARTER 3 | 72,144.37 | | 70,917.92
| OCT | 72,144.37 | | 70,917.92
| QUARTER 4 | 72,144.37 | | 70,917.92
TOTAL | | 288,577.48 | | 283,671.68
> Bottom right: 2040766038 (Bates number)
Bottom left: FORM M-01 REV 05-82
> This is definitely an invoice (agency estimate recap that revises a prior estimate).
> One detail: "GROSS LESS C/D". C/D likely means Commissions/Discounts. This is a billing statement showing gross amounts and adjustments to get the net billable amount. This confirms it's an invoice/bill.
> Final label: invoice.

---
### `rvl_cdip__budget__0020.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING". This is a company letterhead/header, not a newspaper/magazine masthead or journal running head.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a lot of content (tables, financial data, headers). Not identifier-only.
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Typed text throughout. No majority handwriting.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions or transmittal note.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: Not a resume.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range, DOI, or copyright line belonging to a journal.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: The page is titled "OUTDOOR ESTIMATE RECAP - ODO1(S)".
- It has "EST NO: 0136 REVISES EST DTD 03/09/90".
- It lists "GROSS AMOUNT" and "GROSS CHANGE" for products (14-PARLIAMENT, 27-MERIT) by period (MAR 1990, APR, MAY, etc.).
- Grand total is 205,080.00.
- Let's look at the rules for invoice vs budget under Check 7.
- "invoice: ... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
- This page has "EST NO: 0136 REVISES EST DTD 03/09/90". It compares original vs revised (Gross Amount vs Gross Change). It is an agency (Leo Burnett) estimate recap for a client (P.M. INC.).
- Wait, let's re-read the budget caveat: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- This page has "EST NO: 0136 REVISES EST DTD 03/09/90". It names an estimate number and revises a prior estimate. Therefore, it is an invoice.
- Let's check the labels: invoice or budget. The label is "invoice".
> Let's double check.
Header: LEO BURNETT U.S.A. ADVERTISING
Title: OUTDOOR ESTIMATE RECAP - ODO1(S)
Client: P.M. INC.
Est No: 0136 REVISES EST DTD 03/09/90
Desc: 774A MERIT ODP 2-SHEET COMMUTER RAIL
Table shows Product, Period, Gross Amount, Gross Change.
Totals by product/month.
Grand Total: 205,080.00, 73,560.68-
> This matches the invoice bullet perfectly: "names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")... is the agency's bill (invoice), not budget".
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: Not a material safety data sheet or product formulation.
- Not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck or presentation.
- Not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: It has a form number at the bottom "FORM M-01 REV 05-82", but the content is financial billing (invoice). Check 7 says money function overrides form layout.
- Not this check (or rather, check 7 takes precedence).
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: Not correspondence.
- Not this check.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: Not news.
- Not this check.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: Not a research write-up.
- Not this check.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: Not an ad.
- Not this check.
> Conclusion: invoice.
> Let's review the invoice vs budget rule again.
"an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job ... is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
The page has:
- "EST NO: 0136" (names an estimate number)
- "REVISES EST DTD 03/09/90" (revises a prior estimate)
- Lists charges/amounts (Gross Amount, Gross Change, Totals).
This is definitively an invoice under the rules.
> Final check of the label string: "invoice".
Matches exactly.
Runner-up: budget, ruled out because the document names an estimate number ("EST NO: 0136") and revises a prior estimate ("REVISES EST DTD 03/09/90"), making it the agency's bill for a client job (invoice) rather than a pure planning recap (budget).

---

## file_folder → presentation (2 errors)

### `rvl_cdip__file_folder__0004.png`
**Expected:** `file_folder` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header: None.
- Masthead/running head: None. There is a Bates number "2065213892" and a title "PRODUCT INTEGRITY - FDA - PRESENTATION".
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a title "PRODUCT INTEGRITY - FDA - PRESENTATION" and a Bates number "2065213892". The text is rotated 90 degrees.
    *   Is it a folder tab? The text is "PRODUCT INTEGRITY - FDA - PRESENTATION". This looks like a section divider or a presentation cover page. Wait, let's look closer.
    *   The text is "PRODUCT INTEGRITY - FDA - PRESENTATION". It's a bold heading.
    *   Check 1 says: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
    *   "A prominent topical heading always counts as real content, subtitle or not." -> "PRODUCT INTEGRITY - FDA - PRESENTATION" is a prominent topical heading.
    *   Wait, is it a folder tab? "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... The label IS filing metadata... so it is NOT a 'topical title' for this check."
    *   The label is "PRODUCT INTEGRITY - FDA - PRESENTATION". This sounds like a presentation title, not a folder tab label like "Litigation Content" or "NEWTROL".
    *   Also, Check 9 says: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... a single-word/short-phrase heading with no subtitle at all... a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."
    *   The page is mostly empty space (white) with a bold headline title "PRODUCT INTEGRITY - FDA - PRESENTATION" rotated 90 degrees and a Bates number.
    *   So Check 1 is "not this check".
> *   **Check 2: handwritten**
    *   Evidence: None. It's typed text (rotated).
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: None.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
    *   Evidence: None.
> *   **Check 5: PERSON'S CAREER HISTORY**
    *   Evidence: None.
> *   **Check 6: PUBLISHED EVIDENCE**
    *   Evidence: No journal running head.
> *   **Check 7: FINANCIAL DOCUMENT**
    *   Evidence: None.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
    *   Evidence: None.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: "PRODUCT INTEGRITY - FDA - PRESENTATION". This is a bold headline title. The page is mostly empty space. The text is rotated 90 degrees.
    *   Check 9 says: "A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider even alongside a small handwritten letter/number annotation — but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab... is a folder-tab label and stays file_folder".
    *   Is "PRODUCT INTEGRITY - FDA - PRESENTATION" a short filing label on a folder tab? It says "PRESENTATION". It sounds like a title for a presentation deck.
    *   Check 9 also says: "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation". There is a faint black bar at the bottom (which is the left edge if rotated).
    *   The text is "PRODUCT INTEGRITY - FDA - PRESENTATION". This is clearly a title for a presentation section or cover.
    *   "A near-blank cover or title page — mostly empty space with only a bold headline title... is a presentation (this check), not file_folder (check 1)."
    *   This matches perfectly. It's a section divider or cover page for a presentation.
> *   **Check 10: ADMINISTRATIVE FORM**
    *   Evidence: None.
> *   **Check 11: CORRESPONDENCE**
    *   Evidence: None.
> *   **Check 12: PUBLISHED JOURNALISM**
    *   Evidence: None.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP**
    *   Evidence: None.
> *   **Check 14: PROMOTIONAL MATERIAL**
    *   Evidence: None.
> **Conclusion:**
The page is a near-blank page with a rotated bold heading "PRODUCT INTEGRITY - FDA - PRESENTATION" and a Bates number. This fits the definition of a presentation (section divider or deck cover).
> Let's re-evaluate Check 1 vs Check 9.
Check 1 exception: "Folder-tab pages... a short filing label... (product name, collection/company name, month or date range, contract/file description, or alphanumeric identifier)... The label IS filing metadata... so it is NOT a 'topical title'".
Is "PRODUCT INTEGRITY - FDA - PRESENTATION" a filing label? It contains the word "PRESENTATION". It describes the content of the following pages (a presentation about Product Integrity and FDA). This is a section divider for a presentation deck.
Check 9: "A large heading rotated 90 degrees... is a section divider... is a presentation".
The text is "PRODUCT INTEGRITY - FDA - PRESENTATION". This is a section divider.
> Therefore, the label is `presentation`.
> Let's double check the "solid black bar". At the bottom of the image (which is the left side if rotated), there is a faint black line/bar. This is consistent with a slide scan artifact.
The text is sparse, off-center (bottom right if rotated, or bottom left in current orientation).
This is definitely a presentation slide/cover/section divider.
> Final check of the text: "PRODUCT INTEGRITY - FDA - PRESENTATION". Bates number "2065213892".
This is a section divider page for a presentation.
> Label: presentation.

---
### `rvl_cdip__file_folder__0006.png`
**Expected:** `file_folder` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a Bates number "2061696347" on the right side. There is a name "Roger Whidden", "PM - Worldwide Regulatory Affairs", "Control #74".
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a large graphic (map-like background), a title "ISSUE MODULE PRODUCT INTEGRITY", "PHILIP MORRIS INTERNATIONAL", "Roger Whidden", "Control #74". It has real content (a title, a company name, a person's name). It is not just an archive number or stamp.
    *   Wait, is it a folder tab? No, it looks like a designed title page or slide. The text "ISSUE MODULE PRODUCT INTEGRITY" is a bold headline title. "PHILIP MORRIS INTERNATIONAL" is at the bottom.
    *   Verdict: not this check.
> *   **Check 2: handwritten**
    *   Evidence: No handwriting visible. It's a scanned graphic/text page.
    *   Verdict: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header.
    *   Verdict: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No questions, no survey instrument.
    *   Verdict: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No CV/resume content.
    *   Verdict: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal name, volume, issue, page range.
    *   Verdict: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: No financial data, line items, or budget figures.
    *   Verdict: not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: No material safety data, product formulation, "shall/must" language.
    *   Verdict: not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence:
        *   "Roger Whidden / PM - Worldwide Regulatory Affairs / Control #74" at the top right. This looks like a slide header or a cover slide for a module.
        *   "ISSUE MODULE PRODUCT INTEGRITY" is a large title.
        *   "PHILIP MORRIS INTERNATIONAL" at the bottom.
        *   Background is a map (looks like North America/World map outline).
        *   Bates number "2061696347" on the right.
        *   This looks like a title slide or cover page for a presentation or a module within a presentation.
        *   Check 9 description: "Slide/overhead layouts... a deck title or section-divider page... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... a single-word/short-phrase heading with no subtitle at all... a deck cover, or a section divider — is a presentation".
        *   Also: "Technical-study title pages... is scientific_report". This is "ISSUE MODULE PRODUCT INTEGRITY". Is this a technical study? "Issue Module" sounds like a corporate presentation module (e.g., a training module or a strategic module). "Product Integrity" is a topic.
        *   The layout is sparse text over a graphic background (map). This is typical of a presentation slide or cover slide.
        *   "Roger Whidden" is likely the presenter or author. "Control #74" looks like a slide number or control number.
        *   Let's check the "Scan-artifact signal": "a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead". There are black bars at top and bottom. The text is sparse.
        *   This looks like a presentation cover slide or section divider. "ISSUE MODULE" suggests a section of a presentation.
    *   Verdict: YES. This is a presentation (deck cover or section divider).
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: No fields, boxes, checkboxes.
    *   Verdict: not this check.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: No TO/FROM/RE header, no salutation, no closing.
    *   Verdict: not this check.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: No masthead, no news typography.
    *   Verdict: not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: No running narrative prose. Just a title and some metadata.
    *   Verdict: not this check.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: Not a product ad. It's a corporate internal document ("Issue Module").
    *   Verdict: not this check.
> **Re-evaluating Check 9 vs Check 1 (file_folder):**
- The page has "ISSUE MODULE PRODUCT INTEGRITY" as a large heading.
- "PHILIP MORRIS INTERNATIONAL" at the bottom.
- "Roger Whidden", "PM - Worldwide Regulatory Affairs", "Control #74".
- Bates number "2061696347".
- Is this a folder tab? No. A folder tab is a short label on a physical folder. This is a designed page with a map background and large text.
- Is it a presentation cover? Yes. "deck title or section-divider page". "ISSUE MODULE" sounds like a section divider or title for a module in a presentation. The layout (sparse text, graphic background, company name at bottom) is classic presentation slide/cover style.
- The instructions say: "A near-blank cover or title page — mostly empty space with only a bold headline title... is a presentation... not file_folder."
- "A large heading rotated 90 degrees... is a section divider... but a rotated SHORT FILING LABEL... on a photographed folder tab... is file_folder." Here the text is horizontal (mostly), "ISSUE MODULE" is large. Wait, "ISSUE MODULE" and "PRODUCT INTEGRITY" are overlaid on a map.
- The text "Roger Whidden / PM - Worldwide Regulatory Affairs / Control #74" is in the top right corner, typical of a slide header.
- This is definitely a presentation slide/cover.
> **Final decision:** presentation.
> Let's double check "scientific_report".
- "Technical-study title page naming a specific experimental method/study is scientific_report".
- "ISSUE MODULE PRODUCT INTEGRITY" is not a specific experimental method/study. It's a corporate topic/module.
- No running prose.
> Let's double check "form".
- No fields.
> Let's double check "file_folder".
- "A page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."
- This page has a bold headline title ("ISSUE MODULE PRODUCT INTEGRITY") and a photographic/graphic image (map). So it's presentation.
> The label is presentation.

---

## form → invoice (2 errors)

### `rvl_cdip__form__0001.png`
**Expected:** `form` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: None. There's a Bates number "77917 7 9 / 4" at the bottom, and a black bar at the bottom (scan artifact or folder edge? Wait, the black bar at the bottom has text "NOTICE IF THE FILM IMAGE IS LESS CLEAR THAN THIS NOTICE... 77917 7 9 / 4". This looks like a microfilm or document scanning notice, not a folder tab. Wait, let's look at the top. "Ted Bates new york/advertising", "BROWN & WILLIAMSON TOBACCO CORPORATION", "PRINT PRODUCTION ESTIMATE". No masthead.
> **Check 1: file_folder**
- Almost no body content? No, there's a lot of content: "PRINT PRODUCTION ESTIMATE", fields, tables. Not file_folder.
> **Check 2: handwritten**
- Most content freeform handwriting? No, mostly typed with some handwritten numbers (1,800, 1,200, 4,000 - 4125, 600 SAF + 312). Not handwritten.
> **Check 3: FAX TRANSMISSION SHEET**
- No fax header.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Not a survey.
> **Check 5: PERSON'S CAREER HISTORY**
- Not a resume.
> **Check 6: PUBLISHED EVIDENCE**
- No journal running head.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- "PRINT PRODUCTION ESTIMATE"
- "BROWN & WILLIAMSON TOBACCO CORPORATION"
- "EST. # NP-75-15R2"
- "REVISED: JULY 29, 1976 / FEBRUARY 18, 1976"
- "DATE JULY 8, 1975"
- Table with "Cost Per Ad/Item", "No. of Ads/Items", "Estimated Total Cost", "Actual Total Cost".
- Items: Dye Transfer, Dye Bye Transfers, Re-Touching, Transparencies, C-Prints, Photolettering.
- This is an estimate/recap/change order from an agency (Ted Bates) to a client (Brown & Williamson).
- Let's check the rules for invoice vs budget:
  - "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
  - Here we have: "EST. # NP-75-15R2", "REVISED: JULY 29, 1976 / FEBRUARY 18, 1976", "DATE JULY 8, 1975". It has "Estimated Total Cost" and "Actual Total Cost" columns. It lists billable charges (Photographer's Fee, Model Fee, Dye Transfer, etc.) with quantities and costs.
  - This is an invoice (agency's bill for a client job).
  - Wait, is it a budget? "Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job... plans projected spend rather than billing completed work, so it is budget, not invoice".
  - This document HAS an estimate number ("NP-75-15R2"), HAS revision dates ("REVISED: JULY 29, 1976 / FEBRUARY 18, 1976"), and HAS charges/amounts for a client job (Photographer's fee, Dye Transfer, etc., with Estimated Total Cost and Actual Total Cost). It is billing for production work (prints, photos).
  - Therefore, it is an invoice.
> Let's double check.
Title: "PRINT PRODUCTION ESTIMATE"
Agency: Ted Bates
Client: Brown & Williamson Tobacco Corporation
Est. #: NP-75-15R2
Revised dates present.
Table has "Cost Per Ad/Item", "No. of Ads/Items", "Estimated Total Cost", "Actual Total Cost".
Items are production costs (Photographer's Fee, Model Fee, Dye Transfer, C-Prints, Photolettering).
This is an invoice for print production services.
> Let's check Check 8: specification.
- Not a material safety data sheet, product formulation, or "shall/must" language.
> Let's check Check 9: presentation.
- Not a slide deck.
> Let's check Check 10: form.
- It has fields and a table, but check 7 says "Money function overrides form layout. ... An agency estimate/recap/change order that names an estimate number ... is the agency's bill (invoice)."
> Let's check Check 11: correspondence.
- Not an email, memo, or letter.
> Let's check Check 12: news_article.
- No.
> Let's check Check 13: scientific_report.
- No.
> Let's check Check 14: advertisement.
- No.
> So the label is invoice.
> Wait, is there any chance it's budget?
"budget: internal money planning, tracking, or disbursement ... ALSO a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
But this is a specific job: "PRINT PRODUCTION ESTIMATE" for "BRAND PUEBLITA/ESCAPE", "CAPTION ESCAPE TO PHOENIX 120'S", "SUBJECT PAINT POSTER". It's a one-off job estimate/bill for advertising production.
"invoice: ... an agency/vendor estimate or recap that names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ... or carries a billing designation ... the word "estimate" in the title does NOT make it budget."
This perfectly matches the invoice definition.
> Evidence for invoice:
- "EST. # NP-75-15R2" (estimate number)
- "REVISED: JULY 29, 1976 / FEBRUARY 18, 1976" (revises prior estimate)
- Line items with costs for a specific job ("PRINT PRODUCTION ESTIMATE", "PAINT POSTER", "C-Prints", "Photolettering")
- "Estimated Total Cost" and "Actual Total Cost" columns.
> Runner-up: budget. Ruled out because the document names an estimate number ("EST. # NP-75-15R2"), includes revision dates ("REVISED: ..."), and lists specific billable charges and totals for a client job (print production), making it an invoice (agency bill) rather than a pure planning budget.
> Let's review the scratchpad requirements:
- Walk checks 1-14 in order.
- Briefly state evidence or "not this check".
- Stop at first matching check.
- Add final line naming runner-up and evidence that ruled it out.
> Check 1: file_folder - no, has real content (table, fields, title).
Check 2: handwritten - no, mostly typed with minor handwritten annotations.
Check 3: FAX - no.
Check 4: questionnaire - no.
Check 5: resume - no.
Check 6: scientific_publication - no.
Check 7: financial document - yes, invoice. Evidence: "PRINT PRODUCTION ESTIMATE", "EST. # NP-75-15R2", "REVISED: JULY 29, 1976", line items with costs for a specific advertising job (photographer's fee, C-prints, photolettering), and "Estimated Total Cost" / "Actual Total Cost" columns. Agency estimate with estimate number and revisions is an invoice.
Check 8: specification - no.
Check 9: presentation - no.
Check 10: form - no, check 7 overrides.
Check 11: correspondence - no.
Check 12: news_article - no.
Check 13: scientific_report - no.
Check 14: advertisement - no.
> Final label: invoice.

---
### `rvl_cdip__form__0005.png`
**Expected:** `form` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: None.
> **Check 1: file_folder**
- Evidence: The page has a table with "Publication Title", "Year", "Volume", "Issue", "Start Page", "End Page", "Author", "Qty", "Acctn No.", "Process Fee", "Copyrt Fee", "Rush Fee", "Total Cost", "Media Notes". It has an "Order Confirmation - NOT an Invoice" header. It has shipping info, order date, order number, etc. This is not just an identifier/stamp.
- Not this check.
> **Check 2: handwritten**
- Evidence: There is a handwritten "USA" or similar near the bottom right, but the majority is typed text and a table.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey questions.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: No CV/resume content.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal running head, volume, issue, page range on this page itself. The table lists publications, but this page is an order confirmation.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: The page is titled "Order Confirmation - NOT an Invoice". It lists charges: "Process Fee 8.00", "Copyrt Fee 1.50", "Rush Fee 0.00", "Total Cost 9.50". It has "Account #", "Contract Id: 164". It's a billing document for processing articles ("132 ARTICLES", "MOVEMENT DISORD"). Wait, the title says "Order Confirmation - NOT an Invoice". But it lists fees and a total cost. Let's look closer.
- "Order Confirmation - NOT an Invoice"
- "SHIP TO: MARGARET A. SOUTHWICK..."
- "Order Date: 02/13/1998"
- "Document: MEDLINEPLUS"
- "Order Month: 16.09.20.1.19 1998"
- "Order Number: 13132"
- "Account #: 8012"
- "Phone: 804-274-2661"
- "Email:"
- "Contract Id: 164"
- Table columns: Publication Title, Year, Volume, Issue, Start Page, End Page, Author, Qty, Acctn No., Process Fee, Copyrt Fee, Rush Fee, Total Cost, Media Notes.
- Row: "132 ARTICLES", "MOVEMENT DISORD", 1998, 13, 1, 190, 190, Dremelur+, 1, YP368, 8.00, 1.50, 0.00, 9.50, RM21014 CANCHMAN.
- This is a statement of charges for a service (accessing MEDLINEPLUS articles). It's a vendor's periodic customer statement or a payment request/bill for a service.
- Wait, check 7 says: "A provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
- Is this a monthly service bill? "Document: MEDLINEPLUS", "Order Month: ...". It looks like a statement of charges for database access (MEDLINE).
- Let's re-read check 7: "budget: ... ALSO a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer ... is budget, not invoice".
- However, it also says: "invoice: ... a payment request, or an agency/vendor ESTIMATE document ... It does not have to be titled "INVOICE" — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
- Wait, is this an invoice or a budget?
- The title is "Order Confirmation - NOT an Invoice". But it has "Total Cost 9.50".
- Let's look at the categories again. Is there a better fit?
- What about form? "administrative form -> form". Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data. This is a printed table with data. But it's a financial document.
- Check 7: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
- Is it an invoice or budget?
- "A provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer ... is budget, not invoice". This looks like a statement of charges for MEDLINEPLUS access (Order Month: 16.09.20.1.19 1998 - maybe a date range). It lists "132 ARTICLES", "Process Fee 8.00", "Copyrt Fee 1.50", "Total Cost 9.50". This is a bill for a service (reprinting/accessing articles).
- Actually, let's look at the wording: "Order Confirmation - NOT an Invoice". If it's not an invoice, and it's a statement of charges, maybe it's budget?
- Wait, check 7 says: "invoice: ... an outside vendor, supplier, or agency states charges owed for goods or services SOLD ... a payment request ... lists billable charges and totals".
- "budget: ... A provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer ... is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
- Here, the vendor (likely a database provider like Ovid or similar, given MEDLINEPLUS) is billing for specific articles accessed ("132 ARTICLES", "MOVEMENT DISORD", "Dremelur+"). This is a bill for goods/services sold (reprints or article access). The "NOT an Invoice" might just be a legal disclaimer (e.g., "this is an order confirmation, not the final invoice"), but the content is a statement of charges for specific items (articles).
- Actually, look at the columns: "Publication Title", "Year", "Volume", "Issue", "Start Page", "End Page", "Author", "Qty", "Acctn No.", "Process Fee", "Copyrt Fee", "Rush Fee", "Total Cost". This is an itemized billing statement for article reprints or access. It lists specific articles, quantities, and fees. This is an invoice (or a document functioning as one, despite the title "Order Confirmation - NOT an Invoice"). The title explicitly says "NOT an Invoice", which is tricky. But the content is a bill for services/goods.
- Wait, if the title says "NOT an Invoice", maybe it's a form? "administrative form -> form". But check 7 says "Money function overrides form layout".
- Let's re-read check 7 carefully: "invoice: ... an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement with unit prices, amounts, and totals. It does not have to be titled "INVOICE" — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
- This document lists billable charges (Process Fee, Copyrt Fee, Total Cost) and totals (9.50). It is an itemized billing statement. Even if titled "Order Confirmation - NOT an Invoice", the function is billing.
- Wait, is it budget? "budget: ... a provider's periodic customer statement: a monthly service bill or statement of account ... is budget". This is not a monthly service bill for ongoing account (like phone service); it's a specific order for 132 articles with specific fees. It's a bill for a specific job/order. So it's invoice.
- Let's consider if it's a form. "administrative form -> form". "A hand-plotted experimental GRAPH ... is scientific_report ... It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)." So if it's a billing document, it's invoice or budget.
- The document is an itemized statement of charges for an order (132 articles, fees). This is an invoice (or functions as one). The label "invoice" is appropriate for a billing document listing charges and totals.
- Let's check if there's any other category. "Order Confirmation" could be a form? No, check 7 overrides.
- Let's refine: Is it an invoice? "an outside vendor ... states charges owed for goods or services SOLD ... an itemized billing statement with unit prices, amounts, and totals." Yes, it lists Process Fee, Copyrt Fee, Total Cost.
- Therefore, invoice.
> Let's double check check 10 (form). "administrative form -> form". "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This page has a table with data, but it's a financial document (billing). Check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." So it's not form.
> Let's double check check 7 again. "invoice: ... an agency/vendor ESTIMATE document ... or itemized billing statement with unit prices, amounts, and totals. It does not have to be titled "INVOICE" ... a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
This page lists "Process Fee 8.00", "Copyrt Fee 1.50", "Total Cost 9.50". It's a billing statement. Even though it says "NOT an Invoice", it's a financial document billing for charges. The category is invoice.
> Wait, is there any possibility it's a "budget"? "budget: ... a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
This document is for a specific order ("Order Number: 13132", "Order Date: 02/13/1998", "132 ARTICLES"). It's a bill for a specific job (reprints/access of specific articles), not a monthly subscription statement. So it's invoice.
> Final check of the text: "Order Confirmation - NOT an Invoice". This is a common phrase in order confirmations to distinguish them from the final invoice, but the document itself contains the billing details (charges, totals). In the context of the classification rules, "It does not have to be titled 'INVOICE' ... a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice." This fits perfectly.
> Let's do the scratchpad.
- file_folder: no — page has a detailed table of publication charges, order details, and shipping info, not just an identifier.
- handwritten: no — mostly typed text and a table, with a small handwritten "USA" or similar.
- fax: no — no fax header.
- questionnaire: no — no survey questions.
- resume: no — no career history.
- scientific_publication: no — no journal running head on this page.
- financial (invoice/budget): yes — the page is an "Order Confirmation" that lists an itemized billing statement for 132 articles (Publication Title, Year, Volume, Issue, Process Fee, Copyrt Fee, Total Cost = 9.50). It states charges owed for services/goods (article processing/reprints) with specific fees and totals. Per check 7, an itemized billing statement with billable charges and totals is an invoice, even if titled "Order Confirmation - NOT an Invoice". It is not a periodic monthly subscription statement (budget), but a specific order bill.
- specification: no — no material safety data or product formulation.
- presentation: no — not a slide deck or cover.
- form: no — check 7 says money function overrides form layout for billing documents.
- email: no — no mail header.
- news_article: no — no masthead.
- scientific_report: no — no running prose research write-up.
- advertisement: no — not a promo layout.
> Runner-up: form, ruled out because check 7 (financial document) overrides form layout for billing documents listing charges and totals.
Runner-up: budget, ruled out because this is a specific order bill for goods/services (132 articles with process/copyright fees) rather than a periodic monthly subscription statement for an ongoing account.
> Label: invoice.

---

## form → specification (2 errors)

### `rvl_cdip__form__0012.png`
**Expected:** `form` | **Predicted:** `specification`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** There is a header "FORM 29. KW 84 RO/SN SN103 B13". This looks like a form identifier or internal code, not a journal masthead. There is a Bates number "2501614242" rotated on the right side. No newspaper/magazine masthead.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a header "FORM 29. KW 84 RO/SN SN103 B13", a title "Erläuterungen zum Report-Laufzettel:", and numbered points (1) to (4) with text. It has a Bates number.
    *   Conclusion: Not file_folder. It has real content (text explaining a report run sheet).
> *   **Check 2: handwritten**
    *   Evidence: The text is typed German. No significant handwriting.
    *   Conclusion: Not handwritten.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" or fax header. The header "FORM 29..." is not a fax cover sheet.
    *   Conclusion: Not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No questions for the reader to answer. It's an explanation of a process.
    *   Conclusion: Not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No biographical info.
    *   Conclusion: Not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal name, volume, issue, page range. "FORM 29..." is not a journal identifier.
    *   Conclusion: Not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: No financial data, line items, or money tracking.
    *   Conclusion: Not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: No material safety data, product formulation, or "shall/must" requirements for a product. It's about a "Report-Laufzettel" (Report run sheet).
    *   Conclusion: Not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: Not a slide layout. It's a text document.
    *   Conclusion: Not this check.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: The header says "FORM 29. KW 84 RO/SN SN103 B13". The title is "Erläuterungen zum Report-Laufzettel:" (Explanations for the Report Run Sheet). The content is a set of instructions/definitions (1) to (4) explaining how to fill out or use a "Report-Laufzettel" (Report run sheet/log sheet). Wait, is this a form itself?
    *   Let's look closer. "FORM 29..." suggests it is a form document or a page from a form manual.
    *   The text describes rules: "(1) Der Titel ist vom Projektleiter einzutragen." (The title is to be entered by the project leader). "(2) Jede Weitergabe des Reports ist durch Ausgangsdatum... zu dokumentieren." (Every forwarding of the report is to be documented by outgoing date...). "(3) Folgende Stationen hat jeder Report mindestens einmal zu durchlaufen..." (Each report must pass through the following stations at least once...). "(4) Der Report-Laufzettel ist Teil des Project Management Files (PMF)..." (The report run sheet is part of the Project Management Files...).
    *   This looks like a page from a manual or a specification document explaining a form ("Report-Laufzettel"). Or is it the form itself? No, it's "Erläuterungen zum..." (Explanations for...).
    *   Wait, let's look at the labels. Is there a "manual" or "instruction" label? No.
    *   Let's re-evaluate "form". Check 10: "Filled or blank fields, boxes, checkboxes... A form does NOT have to be blank... This also covers: a standalone labeled data chart or table... internal authorization/approval forms".
    *   This page is text explaining a form. Is it a form?
    *   Let's look at Check 13: "ORIGINAL RESEARCH WRITE-UP -> scientific_report". "Running narrative prose with objectives, methods, results, or discussion... A lab or technical study title page...". This is technical documentation/procedure.
    *   Let's look at Check 8: "PRODUCT OR MATERIAL DOCUMENTATION -> specification". "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables... tolerances, or 'shall/must' requirement language." The text has "ist... einzutragen" (is to be entered), "ist für das Eintragen... zuständig" (is responsible for entering). This is procedural language.
    *   Let's look at the header: "FORM 29. KW 84 RO/SN SN103 B13". This looks like a form number and revision code. "KW 84" could be Calendar Week 84 or similar. "RO/SN" could be initials. "SN103 B13" looks like a document number.
    *   Actually, let's look at the content again. It's a set of instructions for a "Report-Laufzettel" (Report run sheet / log sheet).
    *   Is it a "specification"? Check 8: "specification... 'shall/must' requirement language." The text uses "ist... einzutragen" (must be entered / is to be entered). It defines the process. "Folgende Stationen hat jeder Report mindestens einmal zu durchlaufen" (Each report must pass through the following stations at least once). This is a requirement/specification for a process.
    *   However, usually "specification" in this context refers to product specs (Check 8: "Material Safety Data Sheet", "product formulation", "manufacturing-change authorization", "test-analysis tables").
    *   Let's reconsider "form" (Check 10). "Administrative form... Filled or blank fields...". This page has no fields to fill. It's text.
    *   Let's reconsider "scientific_report" (Check 13). "Running narrative prose...". This is numbered list prose. "A lab or technical study title page...". This is a technical document explaining a reporting procedure.
    *   Let's look at the header again: "FORM 29. KW 84 RO/SN SN103 B13". This looks like a document control header.
    *   Is it a "memo"? Check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block...". No.
    *   Is it a "letter"? No.
>     Let's look at the categories again.
    1. file_folder
    2. handwritten
    3. form (fax cover)
    4. questionnaire
    5. resume
    6. scientific_publication
    7. invoice/budget
    8. specification
    9. presentation
    10. form (administrative)
    11. email/memo/letter
    12. news_article
    13. scientific_report
    14. advertisement
>     The document is "Erläuterungen zum Report-Laufzettel" (Explanations for the Report Run Sheet).
    It lists rules (1)-(4).
    Header: "FORM 29. KW 84 RO/SN SN103 B13".
    This looks like a page from a manual or a standard operating procedure (SOP).
    In the absence of a "manual" or "SOP" label, where does it fit?
>     Let's look at Check 8 (Specification) again.
    "specification... 'shall/must' requirement language. Product-referenced test data is a specification... A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
    The text has requirement language: "ist... einzutragen" (is to be entered), "hat... zu durchlaufen" (must pass through). This is procedural specification.
    However, Check 8 is titled "PRODUCT OR MATERIAL DOCUMENTATION". The examples are MSDS, product formulation, manufacturing change, test-analysis tables. This document is about a "Report-Laufzettel" (Report log sheet), which is an administrative document, not a product/material.
    So Check 8 is likely a mismatch because it's about "Product or Material Documentation".
>     Let's look at Check 10 (Administrative Form).
    "Administrative form -> form. Filled or blank fields, boxes, checkboxes... A form does NOT have to be blank... This also covers: a standalone labeled data chart or table... internal authorization/approval forms...".
    This page is text explaining a form. It is not a form itself (no fields to fill).
    Wait, could the whole page be considered a "form" in a broad sense? No, the header says "FORM 29...". Maybe this *is* Form 29?
    "FORM 29. KW 84..." -> Form number 29, Week 84...
    If this is Form 29, and it contains instructions, maybe it's a form?
    But the content is "Erläuterungen zum Report-Laufzettel" (Explanations for the Report Run Sheet). So Form 29 *is* the explanations? Or Form 29 is the Report Run Sheet and this is an addendum?
    Actually, "FORM 29" might be the document type.
    If this is a document explaining a process, it's technical documentation.
>     Let's look at Check 13 (scientific_report).
    "ORIGINAL RESEARCH WRITE-UP -> scientific_report. Running narrative prose with objectives, methods, results, or discussion... A lab or technical study title page...".
    This is a technical document (internal corporate document) explaining a reporting procedure. It's not really "original research".
    However, in these archives (tobacco industry), internal technical documents, manuals, and procedures often get classified as scientific_report if they are dense text, or form if they are structured.
    But the instructions say: "scientific_report requires running prose... A page that is only labeled field-value entries... is a filled form".
    This page has numbered points (1)-(4) with prose. It is running prose (numbered list).
    Is it a scientific report? "A lab or technical study title page with authors and an internal affiliation and no journal identifiers."
    This page has no author, no affiliation (except maybe implied by the header codes).
    The header "FORM 29. KW 84 RO/SN SN103 B13" looks like a document control number. "RO/SN" could be initials. "SN103" could be a serial number.
>     Let's reconsider the "form" category (Check 10).
    "Administrative form... Filled or blank fields...".
    This page has no fields.
>     Let's look at the header "FORM 29. KW 84 RO/SN SN103 B13".
    This looks like a form identifier.
    Maybe the page *is* a form?
    "Erläuterungen zum Report-Laufzettel" -> Explanations for the Report Run Sheet.
    This is a page of instructions.
>     Let's look at the labels again.
    Maybe it's a **specification**?
    Check 8: "specification... 'shall/must' requirement language."
    The text says: "Der Titel ist vom Projektleiter einzutragen." (The title is to be entered by the project leader). This is a requirement.
    "Jede Weitergabe... ist durch... zu dokumentieren." (Every forwarding... is to be documented...). Requirement.
    "Folgende Stationen hat jeder Report mindestens einmal zu durchlaufen..." (Each report must pass through...). Requirement.
    This is a specification of a process.
    But Check 8 is "PRODUCT OR MATERIAL DOCUMENTATION".
    "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables...".
    This is about a "Report-Laufzettel" (Report log). Not a product.
    However, the rule says: "But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
    This implies that if there *is* requirement language ("shall/must" or equivalent like "ist... zu"), it might be a specification, even if not product-related?
    Wait, the check title is "PRODUCT OR MATERIAL DOCUMENTATION -> specification".
    The text says: "Material Safety Data Sheet... product formulation...".
    Usually, in these datasets, internal manuals/SOPs are tricky.
>     Let's look at **scientific_report** (Check 13).
    "Running narrative prose...".
    This is a technical document. In the tobacco archive, internal technical reports, manuals, and procedures are often classified as scientific_report if they are text-heavy and technical.
    "A lab or technical study title page with authors and an internal affiliation and no journal identifiers."
    This page has no title page feel, just a header and text.
    "Requires running prose — a page that is only labeled field-value entries... is a filled form".
    This page has numbered prose. It fits "running prose" loosely (numbered list).
>     Let's look at **form** (Check 10) again.
    "Administrative form...".
    Sometimes, a page that is a form template or a form instruction sheet is classified as form.
    But the content is purely text instructions.
>     Let's look at the header: "FORM 29. KW 84 RO/SN SN103 B13".
    This looks like a form number. "Form 29".
    If the document is identified as "FORM 29", maybe it is a form?
    But the content is "Erläuterungen..." (Explanations).
    Maybe this is a page *from* a form book?
>     Let's reconsider the **specification** check.
    "specification... 'shall/must' requirement language."
    The German text uses "ist... einzutragen" (is to be entered), "ist... zuständig" (is responsible), "hat... zu durchlaufen" (must pass through). These are imperative/requirement language.
    Even though it's not a "product" specification in the chemical sense, it is a specification of a process (Report-Laufzettel process).
    However, the category is "PRODUCT OR MATERIAL DOCUMENTATION".
    Is a "Report-Laufzettel" a product/material? No.
>     Let's look at **scientific_report** again.
    In many document classification tasks for corporate archives, internal technical documents (like this German text explaining a reporting procedure) are classified as scientific_report or just "report". Here the label is scientific_report.
    "ORIGINAL RESEARCH WRITE-UP -> scientific_report".
    "Running narrative prose with objectives, methods, results, or discussion".
    This text has "methods" (how to fill the report, what stations to pass through).
    It's a technical write-up.
>     Let's look at the pre-scan note: "A journal or author being cited within the body prose... is NOT the same as the page itself carrying that identifier".
    Here, the header is "FORM 29...". Not a journal.
>     Let's look at the label **form** (Check 10).
    "Administrative form... Filled or blank fields...".
    This page has no fields.
>     Let's look at the label **memo** (Check 11).
    "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block...".
    No.
>     Let's look at the label **presentation** (Check 9).
    "Slide/overhead layouts...".
    No.
>     Let's look at the label **file_folder** (Check 1).
    "Almost no body content...".
    This page has body content (4 numbered points).
>     So it's between **scientific_report** and **specification** (maybe?) or **form**.
    Actually, let's look at the header "FORM 29. KW 84 RO/SN SN103 B13".
    This looks like a document control header.
    "KW 84" -> Kalenderwoche 84 (Calendar week 84) or similar.
    "RO/SN" -> Initials.
    "SN103 B13" -> Serial number / version.
>     If I have to choose, this looks like a page from a manual or a technical specification of a process.
    In the tobacco archive dataset (which this prompt seems to be based on, likely the Philip Morris / RJR tobacco archive), documents like this (internal procedures, instructions) are often classified as **scientific_report** if they are text-heavy technical documents, or **form** if they are forms.
    Wait, "Erläuterungen zum Report-Laufzettel" -> Explanations for the Report Run Sheet.
    This is a document explaining a form.
    Is it a form itself? No.
    Is it a scientific report? It's a technical document.
    Let's check the definition of scientific_report: "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page...".
    This is a technical study/procedure write-up. "Methods" section: how to document the report.
>     Let's look at **specification** again.
    "specification... 'shall/must' requirement language."
    The text is full of requirements. "ist... einzutragen", "hat... zu durchlaufen".
    But the category is "PRODUCT OR MATERIAL DOCUMENTATION".
    Is a "Report-Laufzettel" a product? No.
    However, the rule says: "But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
    This implies that if there *is* requirement language, it *could* be a specification, even if generic?
    "A generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
    This sentence is a caveat for Check 8. It says: if it's generic AND no requirement language AND no shall/must -> form.
    Contrapositive: if it has requirement language OR shall/must -> could be specification?
    But the main header of Check 8 is "PRODUCT OR MATERIAL DOCUMENTATION".
    Usually, process specifications are not "product documentation".
>     Let's look at the content again.
    It's a set of instructions for a "Report-Laufzettel" (Report run sheet / log sheet).
    This is an administrative procedure.
    Maybe it's a **form**?
    Check 10: "Administrative form... internal authorization/approval forms...".
    This is not an authorization form.
>     Let's consider **scientific_report** as the catch-all for technical text documents in this archive.
    "scientific_report: ... a lab or technical study title page with authors and an internal affiliation and no journal identifiers."
    This page has no author, but has a header that looks like a document ID.
    The text is technical German.
    It describes a process (methods).
    I will lean towards **scientific_report** because it's a technical text document explaining a procedure, and in these datasets, internal technical manuals/procedures often fall under scientific_report if they aren't forms or specs.
    Wait, is there a better fit?
    What about **form**?
    The header says "FORM 29".
    If the document is literally "Form 29", and it contains text, maybe it's a form?
    But the text is "Erläuterungen zum..." (Explanations for...).
    Usually, a form is a template to be filled. This is instructions on how to fill/use it.
    Sometimes, instruction sheets are classified as forms or reports.
>     Let's look at the example worked out in the prompt? No, the prompt has examples.
    Example 4: agency estimate -> invoice.
    Example 3: journal reprint -> scientific_publication.
    Example 2: lab title page -> scientific_report.
    Example 1: survey -> questionnaire.
>     Let's look at the text "FORM 29. KW 84 RO/SN SN103 B13".
    This looks like a form number.
    If I classify this as **form** (Check 10):
    "Administrative form... Filled or blank fields...".
    This page has no fields.
    "This also covers: a standalone labeled data chart or table...". No.
    "internal authorization/approval forms". No.
>     If I classify as **specification** (Check 8):
    "specification... 'shall/must' requirement language."
    The text has "ist... zu" (is to be / must).
    "Folgende Stationen hat jeder Report mindestens einmal zu durchlaufen" (Each report must pass through...).
    This is requirement language.
    Even though it's not a "product" spec, it's a process spec.
    The caveat says: "But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
    This implies that requirement language pushes it towards specification, away from form.
    So if it has requirement language, it's a specification.
    Is it a "Product or Material Documentation"?
    The "Report-Laufzettel" is a document/material used in project management.
    Maybe it counts?
>     Let's look at **scientific_report** (Check 13).
    "Running narrative prose...".
    This is numbered prose.
    "A lab or technical study title page...".
    This is a technical document.
>     Let's look at the header again. "FORM 29".
    If the document is a form, it should be **form**.
    But it's text.
    Maybe it's a **memo**?
    No TO/FROM.
>     Let's assume the label is **scientific_report**.
    Why? It's a technical document (German) explaining a reporting procedure (methods). It has running prose (numbered list). It's not a form (no fields), not a spec (not product/material, though it has requirements), not a presentation.
    In the tobacco archive, internal technical documents (like this one about report management) are often scientific_reports.
>     Wait, let's look at the header "FORM 29. KW 84 RO/SN SN103 B13".
    Could "FORM" be the document type?
    If the document type is "FORM", maybe it's **form**?
    But the content is text.
    Check 10: "Administrative form...".
    If a page is titled "FORM 29" and contains instructions, is it a form?
    Usually, a form is the thing you fill out. This is the instructions *for* the form ("Erläuterungen zum Report-Laufzettel").
    The "Report-Laufzettel" is the form. This page explains it.
    So this page is a manual page / instruction page.
    Manual pages are often **scientific_report** (technical write-up) or **form** (if part of the form package).
    But Check 4 says: "APPENDIX N pages... is still questionnaire".
    Check 10 says: "administrative form...".
>     Let's look at the text content closely.
    (1) Title entry.
    (2) Forwarding documentation.
    (3) Stations to pass through (Original creation, proofreading, correction, release, etc.).
    (4) Report run sheet is part of PMF (Project Management Files).
    This is a process description.
    Process descriptions are technical documents. -> **scientific_report**.
>     Let's check if there's any other label.
    **specification**: "specification... 'shall/must' requirement language."
    The text is full of "ist... einzutragen" (must be entered), "hat... zu durchlaufen" (must pass through).
    This is specification language.
    Is it a "Product or Material Documentation"?
    The "Report-Laufzettel" is a material (a document).
    The document specifies how this material (the report log) is used.
    This is a stretch.
>     Let's go with **scientific_report**.
    Evidence: Running narrative prose (numbered list) describing a technical/administrative process (methods for report documentation). No journal identifier. No form fields. No financial data. No product imagery.
    Wait, is there a better fit?
    What about **form**?
    The header says "FORM 29".
    If the page is literally a form (Form 29), and the text is the content of the form (instructions printed on the form?), then it's a form.
    "FORM 29. KW 84..." -> Form 29, Week 84...
    If this is Form 29, and it contains the text "Erläuterungen...", then the form *is* the instructions?
    Or is this a page *from* Form 29?
    If a form contains instructions, it's still a form.
    Check 10: "A form does NOT have to be blank — a filled form recording data is still a form... This also covers: ... internal authorization/approval forms".
    If this is "Form 29", and it's an administrative document, maybe it's **form**.
    But the content is purely text instructions, no fields to fill.
    Usually, a page with only text instructions is not a form. A form has fields.
    Unless... the whole page is a "specification" of the form?
>     Let's look at the label **specification** again.
    "specification... 'shall/must' requirement language."
    "But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
    This implies that if there is requirement language, it is a specification.
    The text has "ist... zu" (is to be / must).
    So it has requirement language.
    Therefore, it is a **specification**.
    Even if it's not a "product" spec, the presence of requirement language ("shall/must" equivalent) pushes it to specification over form.
    The category is "PRODUCT OR MATERIAL DOCUMENTATION".
    Maybe "Report-Laufzettel" is considered a "Material" (a document material)?
    Or maybe the "specification" label is broader in this dataset for any document with requirement language?
    The check says: "specification... 'shall/must' requirement language. Product-referenced test data is a specification... But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
    This logic:
    - Has requirement language -> Specification (potentially).
    - No requirement language + generic chart/table -> Form.
    Here, we have requirement language ("hat... zu durchlaufen", "ist... einzutragen").
    So it's not a generic form. It's a specification.
    Is it a product/material? The "Report-Laufzettel" is a document/material used in the project.
    I'll bet on **specification** or **scientific_report**.
>     Let's compare **specification** vs **scientific_report**.
    Scientific report: "Running narrative prose with objectives, methods, results, or discussion".
    This has methods (how to do the report log).
    Specification: "requirement language".
    This has requirement language.
>     Let's look at the header "FORM 29".
    If the document is a form, it should be **form**.
    But the content is text.
    Maybe it's a **memo**? No.
>     Let's look at the source. Tobacco archive.
    This looks like an internal quality assurance or project management document.
    "Project Management Files (PMF)".
    This is internal corporate documentation.
    In the tobacco archive dataset (e.g., from the Truth Tobacco Industry Documents), internal memos, reports, and manuals are common.
    If it's a manual page, it's often **scientific_report** (as a technical write-up) or **form** (if it's a form template).
    Here, it's text explaining a form.
    Actually, let's look at Check 10 again.
    "Administrative form... Filled or blank fields...".
    This page has no fields.
>     Let's look at Check 8 again.
    "specification... 'shall/must' requirement language."
    The text is: "(1) Der Titel ist vom Projektleiter einzutragen." -> The title is to be entered by the project leader. (Requirement)
    "(3) Folgende Stationen hat jeder Report mindestens einmal zu durchlaufen..." -> Each report must pass through... (Requirement)
    This is definitely specification language.
    The category is "PRODUCT OR MATERIAL DOCUMENTATION".
    Is a "Report-Laufzettel" a material? It's a document.
    Maybe the label **specification** is the best fit for a document with requirement language, even if it's process-oriented.
    BUT, the check title is "PRODUCT OR MATERIAL DOCUMENTATION".
    And the examples are MSDS, product formulation.
    This is a process document.
>     Let's look at **scientific_report** (Check 13).
    "ORIGINAL RESEARCH WRITE-UP -> scientific_report".
    "Running narrative prose...".
    This is a technical write-up.
    In the absence of a "manual" or "procedure" label, technical procedures are often **scientific_report**.
    "A lab or technical study title page with authors and an internal affiliation and no journal identifiers."
    This page has a header "FORM 29...". Not a title page.
    But it is a technical document.
>     Let's look at the label **form** (Check 10).
    "Administrative form...".
    Sometimes, a page that is a form instruction sheet is classified as **form**.
    But the content is text.
>     Let's assume the label is **scientific_report**.
    Reason: It's a technical document (German) describing a process (methods). It has running prose (numbered list). It's not a form (no fields), not a spec (not product/material, though it has requirements), not a presentation.
    Wait, the prompt says: "Do not rush to the label that matches the page's subject matter — deliberate through the checks below, in order".
    Subject matter: Report documentation procedure.
    Check 1-7: No.
    Check 8: Specification. "requirement language". The text has "ist... zu" (must). But is it "Product or Material Documentation"? The "Report-Laufzettel" is a document. Maybe.
    Check 9: Presentation. No.
    Check 10: Form. "Administrative form". No fields.
    Check 11: Correspondence. No.
    Check 12: News. No.
    Check 13: Scientific report. "Running narrative prose... technical study...". This fits best as a technical document.
>     Let's look at the header "FORM 29. KW 84 RO/SN SN103 B13".
    This looks like a document control number.
    "KW 84" -> 1984? Or Week 84?
    "RO/SN" -> Initials.
    "SN103 B13" -> Serial.
    This is a technical document ID.
>     I will classify as **scientific_report**.
    Evidence: Running narrative prose (numbered list 1-4) describing a technical/administrative procedure (methods for report documentation). Header "FORM 29..." is a document ID, not a form template with fields. No journal identifier. No product/material focus (it's about a report log process).
    Wait, is there a chance it's **form**?
    The header says "FORM 29".
    If the document is literally "Form 29", and the content is the text of the form (instructions), then it's a form.
    But "Erläuterungen zum..." means "Explanations for...". So this is not the form itself, it's the explanation.
    Explanations are reports/manuals -> **scientific_report**.
>     One more check: **specification**.
    "specification... 'shall/must' requirement language."
    The text has requirement language.
    "But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
    This implies that if there IS requirement language, it is a specification.
    The text has "ist... zu" (is to be / must).
    So it is a specification.
    Is it "Product or Material Documentation"?
    The "Report-Laufzettel" is a material (a document used in the process).
    The document specifies how to use it.
    This is a weak link.
>     Let's look at the label **scientific_report** again.
    "scientific_report: ... a lab or technical study title page with authors and an internal affiliation and no journal identifiers."
    This page has no author, but has a header.
    "Requires running prose". This has numbered prose.
>     I'll go with **scientific_report**.
    Actually, let's look at the label **form** (Check 10).
    "Administrative form...".
    If the page is "FORM 29", maybe it is a form.
    But the content is text.
    In many datasets, a page with "FORM [Number]" at the top is a form.
    But the content is "Erläuterungen..." (Explanations).
    This is a page from a manual.
    Manuals are often **scientific_report** in these datasets (technical write-ups).
>     Final decision: **scientific_report**.
    Wait, let's look at the text again.
    "Erläuterungen zum Report-Laufzettel:"
    (1) ...
    (2) ...
    (3) ...
    (4) ...
    This is a set of instructions.
    Instructions are technical documents. -> **scientific_report**.
>     One distinct possibility: **specification**.
    Check 8: "specification... 'shall/must' requirement language."
    The text is full of requirements.
    "Der Titel ist... einzutragen." (The title is to be entered.)
    "Jede Weitergabe... ist... zu dokumentieren." (Every forwarding is to be documented.)
    "Folgende Stationen hat... zu durchlaufen." (Following stations must be passed through.)
    This is specification language.
    The category is "PRODUCT OR MATERIAL DOCUMENTATION".
    Maybe the "Report-Laufzettel" is considered a "Material" (a document material)?
    Or maybe the "specification" label is used for any document with requirement language in this dataset?
    The caveat says: "But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
    This implies: Requirement language -> Specification.
    So if it has requirement language, it's a specification.
    This page has requirement language.
    So it's a **specification**.
>     Let's compare **specification** and **scientific_report**.
    Scientific report: narrative prose, objectives/methods/results.
    Specification: requirement language ("shall/must").
    This page is mostly requirement language (rules for using the report log).
    So **specification** fits the "requirement language" criterion better.
    Even though it's not a "product" spec, it's a process specification.
    The check title is "PRODUCT OR MATERIAL DOCUMENTATION".
    Maybe "Report-Laufzettel" is a "Material" (document material)?
    Or maybe the check is broader.
>     Let's look at the header "FORM 29".
    If it's a form, it's **form**.
    But it has requirement language, so it's not a generic form (Check 10 caveat).
    So it's **specification**.
>     I will go with **specification**.
    Evidence: Header "FORM 29...", text contains requirement language ("ist... einzutragen", "hat... zu durchlaufen") specifying the process for a "Report-Laufzettel" (Report run sheet). This fits the "requirement language" criterion for specification, distinguishing it from a generic administrative form.
>     Wait, "Product or Material Documentation".
    Is a report log a product or material?
    In a corporate context, documents are materials.
    And the document specifies properties/usage of this material (the report log).
    So **specification** is plausible.
>     Let's reconsider **scientific_report**.
    "Running narrative prose...".
    This is numbered list.
    "A lab or technical study title page...".
    This is not a title page.
>     I'll stick with **scientific_report** as the safest bet for technical text documents in this archive, unless the requirement language is the key.
    The prompt emphasizes: "Do not rush to the label that matches the page's subject matter".
    Subject matter: Report procedure.
    Check 8 (Specification) has "requirement language".
    The text has "ist... zu" (must).
    So Check 8 matches.
    Check 13 (Scientific report) has "running narrative prose".
    The text has numbered prose.
    Check 8 comes before Check 13.
    So if Check 8 matches, it's **specification**.
    Does Check 8 match?
    "specification... 'shall/must' requirement language."
    Yes, "ist... zu" is equivalent to "shall/must".
    "But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
    This implies that if there IS requirement language, it is a specification.
    So **specification** is the correct label based on the checks order.
>     Final check: Is there a product/material tie-in?
    "Report-Laufzettel" (Report run sheet).
    "Project Management Files (PMF)".
    This is about a document/material (the report log).
    So yes, there is a tie-in.
>     Label: **specification**.

---
### `rvl_cdip__form__0013.png`
**Expected:** `form` | **Predicted:** `specification`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: There is a Bates number "620423067" at the bottom right. No journal masthead.
> **Check 1: file_folder**
- Evidence: The page has a lot of data (a table with rows like "BRAND", "PRODUCTION DATE", "OPERATOR NUMBER", "CIGARETTE", "FILTER", "PAPER", "TOR. ANALYSES", "SMOKING", etc.). It has real content, not just an identifier.
- Not this check.
> **Check 2: handwritten**
- Evidence: The page is mostly a printed table with handwritten entries filling the cells. The handwriting fills a printed structured form/table.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: Not a survey.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: Not a resume.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal name/volume/issue on the page itself.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT**
- Evidence: No financial content (invoice/budget). It's technical data (smoke analyses, cigarette dimensions).
- Not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: The table is titled/structured with "BRAND St. James C4 1001 84", "PRODUCTION DATE", "OPERATOR NUMBER", "DATE ANALYSIS EXPECTED", "DATE RECEIVED". Then rows for "CIGARETTE" (P.D., Weight, Circ., N.T.W., Density), "FILTER" (Texhil/Pillow, Triceratin, TEODA, Ventilation Rate), "PAPER" (Porosity, Citrate, Phosphate), "TOR. ANALYSES" (Alkaloids, Total Sugar, etc.), "SMOKING" (Tar, Nicotine, Efficiency, Puffs, NO, CO), "CIG. PERF. Firmness", "End Stability", "Coal Retention", "Corr. BORG FV", "BORG FV Moisture", "Corr. FILL VALUE", "FV MOISTURE".
- This is a product-analysis table or test-analysis table keyed to product codes/parameters. "MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER" is an example from the prompt. This table has chemical constituents and measurements for a specific brand (St. James C4).
- Wait, check 8 says: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough".
- Here, the top row says "BRAND St. James C4 1001 84". The table contains "SMOKING" analyses (Tar, Nicotine, etc.) and "TOR. ANALYSES" (Total Organic Radioactivity? or similar). This is a product test-analysis table.
- Let's check check 10: "standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)".
- Wait, check 8 explicitly says: "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification".
- Is this a specification or a form?
- Check 10: "A hand-plotted experimental GRAPH... is a research test result (check 13), not a form... It does NOT cover money records... It does NOT cover product-change authorization pages".
- Wait, check 13: "ORIGINAL RESEARCH WRITE-UP -> scientific_report. Running narrative prose... Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."
- This page is ONLY a labeled table with field-value entries (handwritten). No running prose.
- So it's either form (check 10) or specification (check 8).
- Check 8: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification. A titled product-analysis table... is a specification".
- The table has "BRAND St. James C4 1001 84" at the top. It has rows for cigarette dimensions, filter properties, paper properties, tor. analyses, smoking analyses. This is a product test-analysis table.
- Let's re-read check 8 carefully: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough; you don't need a code like 'PD 142A' specifically, just clear evidence the table's subject is a product's own composition or properties."
- This page has "BRAND St. James C4 1001 84" and a table of its properties (dimensions, smoke analyses, tor. analyses). This fits "product-referenced test data" and "product-analysis table".
- Let's check check 10 again: "standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values); a filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)".
- The prompt says: "test-analysis tables keyed to product/part codes... is a specification". This table is keyed to "St. James C4 1001 84".
- Wait, is it a scientific_report? No, no running prose.
- Is it a form? "A form does NOT have to be blank — a filled form recording data is still a form... This also covers: a standalone labeled data chart or table... a filled analytical or lab data sheet".
- But check 8 says: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification." and "A titled product-analysis table... is a specification".
- The table here is analyzing the properties of "St. James C4". It's a product test data sheet.
- Let's look at the labels: specification.
- Let's check if there's any other match.
- Check 13: scientific_report requires running prose. This is just a table.
- So it's between form and specification.
- Check 8: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification." The table is testing the properties of a specific cigarette brand (St. James C4). The rows are "CIGARETTE", "FILTER", "PAPER", "TOR. ANALYSES", "SMOKING". This is a product analysis table.
- Therefore, specification.
> Let's double check.
Table headers:
BRAND St. James C4 1001 84
PRODUCTION DATE
OPERATOR NUMBER
DATE ANALYSIS EXPECTED
DATE RECEIVED
CIGARETTE
P.D. (INCHES)
Cigarette, Sealed Cigarette, Tob. Sect., Filter
WEIGHT (MG)
Circ. (MM), Cigarette, N.T.W., Tobacco, Density (MG/CC)
FILTER
Texhil/Pillow (%), Triceratin (%), TEODA (%), Ventilation Rate (%)
PAPER
Porosity (CORRECTS), Citrate (%), Phosphate (%)
TOR. ANALYSES (%)
Alkaloids, Total Sugar, Reducing Sugar, Moist. (Cond), Tarate. (Pkg), Menthol, Prop. Glycol, Glycerin, Nitrate
SMOKING (Cig)
Tar (MG), Nicotine (MG), Efficiency (%), Puffs, NO (MG), CO (MG)
CIG. PERF. Firmness (gts/25 cig), End Stability (MG/Cl), Coal Retention (%), Corr. BORG FV (CC/GM), BORG FV Moisture (%), Corr. FILL VALUE (MG/CC), FV MOISTURE (%)
> This is a detailed product test data sheet for a cigarette brand. It matches "test-analysis tables keyed to product/part codes" and "product-referenced test data" -> specification.
> Let's review the scratchpad steps:
1. file_folder: no — page has a detailed data table with many rows and columns, not just an identifier.
2. handwritten: no — handwriting fills a printed structured table.
3. FAX: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no — no journal identifier.
7. financial: no.
8. specification: yes — the page is a product test-analysis table keyed to "BRAND St. James C4 1001 84", containing product properties (cigarette dimensions, filter, paper, tor. analyses, smoking analyses). Check 8 explicitly includes "test-analysis tables keyed to product/part codes" and "product-referenced test data" as specifications.
9. presentation: no.
10. form: no — although it is a filled table, check 8 takes precedence for product test-analysis tables. Wait, check 10 says "standalone labeled data chart or table... is a form". But check 8 says "test-analysis tables keyed to product/part codes... is a specification". The product tie-in ("BRAND St. James C4") makes it a product-analysis table, which check 8 explicitly classifies as specification.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no — no running narrative prose, only a data table.
14. advertisement: no.
> Runner-up: form. Ruled out because the table is a product test-analysis sheet keyed to a specific brand/product ("St. James C4"), which check 8 explicitly classifies as a specification ("test-analysis tables keyed to product/part codes... Product-referenced test data is a specification").
> Let's confirm check 8 vs check 10.
Check 8: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification. A titled product-analysis table... is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough"
Check 10: "standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values); a filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)"
The page has "BRAND St. James C4 1001 84" at the top. The rows are specific product properties (Tar, Nicotine, etc.). This is a product test data sheet. Check 8 wins.
> Final label: specification.

---

## presentation → file_folder (2 errors)

### `rvl_cdip__presentation__0017.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "2071969205" rotated 90 degrees in the bottom right. There's a small "F" or similar mark in the top right. The left side has some faint, noisy, vertical banding, possibly a scanned artifact or a very faint image, but mostly white space. Wait, looking closely at the left side, there's a vertical band of noise/text, but it's extremely faint and illegible. Let's look at the bottom left. There's a darker rectangular block. It looks like a scanned artifact or a very poor scan of something.
- Let's re-evaluate the image. It's mostly white space.
- Top right: a small black mark, looks like a rotated "F" or a staple mark or a logo fragment.
- Bottom right: "2071969205" rotated 90 degrees. This is a Bates number.
- Left side: A vertical strip of noise, maybe a scanned edge of a previous page or a scan artifact. Bottom left has a darker block, looks like scan noise or a partial scan of a document edge.
- Overall, this page is almost entirely blank except for a Bates number and some scan artifacts.
> **2. Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."
- "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content — it is a cover/title page... not file_folder."
- "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body."
- Let's look at the left side again. Is there a folder tab?
- The left side has a vertical band. It looks like the edge of a scanned document, maybe a folder tab?
- Wait, the prompt says: "A page whose content is a physical folder tab, a short filing label (product/collection/month/file name), and a Bates number is file_folder even though the folder body photographs as a solid black bar and the label may be rotated."
- Let's look at the left side. There is a vertical rectangular area with noise. At the bottom, there is a darker block. This looks like a scanned folder tab or the edge of a folder.
- Actually, looking very closely at the left side, it looks like a very faint, degraded scan of text or an image, but it's mostly illegible noise.
- Wait, is there a folder tab? The left edge has a vertical strip. The bottom left has a dark block.
- Let's re-read the file_folder definition: "Almost no body content: only an archive/Bates number, a stamp, a short label or ID... A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
- "A Bates number or archive stamp alone is NOT enough... if it pairs a Bates number with a photographic image... or with a bold headline title... it is a cover/title page... not file_folder."
- Here, we have a Bates number "2071969205".
- Is there a bold headline title? No.
- Is there a photographic image? The left side has noise, maybe a faint image, but it's mostly scan noise.
- Is there a folder tab? The left side looks like a scanned edge.
- Let's look at the "F" in the top right. It's a small black mark.
- Let's look at the bottom left. It looks like a dark rectangular block, maybe a barcode or a stamp?
- Actually, this looks like a blank page with a Bates number and scan artifacts.
- Wait, if it's just a Bates number and scan artifacts, is it file_folder?
- "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content... not file_folder."
- This implies that if it's *only* a Bates number (and maybe scan noise), it might be file_folder?
- Let's re-read: "A Bates number or archive stamp alone is NOT enough [to be file_folder if there's other content]. A page that pairs a Bates number with a photographic image... carries real content... not file_folder."
- So if it's *only* a Bates number and noise, what is it?
- "Pure filing metadata only." -> file_folder.
- The left side looks like a very faint, degraded scan of text or an image. But it's mostly illegible.
- Let's look at the bottom left block. It looks like a barcode or a dense block of text that is completely illegible.
- Actually, looking at the layout, this is a classic "blank page with Bates number" from a scanned archive. Often these are blank pages or folder tabs.
- Let's consider "file_folder". The page has a Bates number "2071969205". The rest is mostly white space with scan artifacts (left edge noise). This fits "Almost no body content: only an archive/Bates number...".
- Wait, is there a folder tab? The left side vertical band could be a folder tab. "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body."
- If the left side is a folder tab, it's file_folder.
- If the left side is just scan noise, and the page is otherwise blank with a Bates number, it's likely a blank page in a folder, which is often classified as file_folder if it's just metadata, or maybe it's just a blank page. But the instructions say "If nothing matches, choose the label whose defining evidence is closest...".
- Let's look at the checks again.
- Check 1: file_folder. "Almost no body content: only an archive/Bates number...". This page has a Bates number and almost no content. The left side is noise. The top right is a mark. This fits file_folder best.
> Let's look really closely at the image.
- Top right: A small black shape, looks like a rotated "F" or a staple.
- Bottom right: "2071969205" rotated 90 degrees.
- Left side: A vertical strip of gray noise. Bottom left: a darker gray block. This looks like the edge of a scanned document, maybe a folder tab or just the edge of the paper.
- There is no text, no form fields, no letter, no invoice.
- It's essentially a blank page with a Bates number.
- In tobacco archives, blank pages with Bates numbers are often just blank pages, but if I have to classify, "file_folder" is the closest for "identifier-only page" or "filing metadata".
- Wait, is it a "photographic slide"? Check 9: "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder". The left side is not a clear photographic image. It's noise.
- Is it a "presentation" cover? "A near-blank cover or title page — mostly empty space with only a bold headline title...". There is no bold headline title.
- So it's likely file_folder. The Bates number is the only clear content. The left side is likely a scanned artifact or a folder tab edge.
- Let's assume file_folder.
> Let's re-evaluate "file_folder" vs "presentation" (photographic slide).
- If the left side is a blurred photo, it's presentation. But it looks like scan noise (vertical lines, grain).
- If it's a folder tab, it's file_folder. "Folder-tab pages... photograph as a solid black bar/border along one or more edges". The left side has a vertical band, and the bottom left has a dark block. This could be the folder body/tab.
- The label "2071969205" is a Bates number.
- Conclusion: file_folder.
> Let's check the scratchpad procedure.
- Check 1: file_folder. Evidence: Bates number "2071969205", mostly blank page with scan artifacts/folder tab edge on the left. No sentences, no topical title. Fits "identifier-only page" or "folder-tab page".
- Check 2: handwritten. No.
- Check 3: fax. No.
- Check 4: questionnaire. No.
- Check 5: resume. No.
- Check 6: scientific_publication. No.
- Check 7: financial. No.
- Check 8: specification. No.
- Check 9: presentation. No bold title, no clear photo (just noise/artifacts).
- Check 10: form. No fields.
- Check 11: correspondence. No.
- Check 12: news_article. No.
- Check 13: scientific_report. No.
- Check 14: advertisement. No.
> So file_folder is the winner.
> Wait, is there any text on the left?
The left side has vertical lines of text that are extremely faint. "1990...". It looks like a very poor scan of a page. But if I can't read it, I can't classify it by content.
However, usually, if a page is mostly blank with a Bates number, it's treated as a filler page or folder tab.
The instructions say: "A Bates number or archive stamp alone is NOT enough [to be file_folder if there's other content]... Pure filing metadata only."
If the left side is illegible noise, I should treat it as no content.
So file_folder.
> Let's look at the "F" in the top right. It might be a logo or a mark.
Actually, looking very closely at the top right, it looks like a rotated "F" or a staple mark.
The bottom right is definitely a Bates number.
> Final decision: file_folder.
> One more check: Could it be a "file_folder" because it's a folder tab?
"Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body."
The left side looks like a scanned folder tab (vertical band, dark block at bottom). The label might be illegible or missing, but the Bates number is there.
Even if it's just a blank page with a Bates number, in this classification scheme, if it's not a presentation (no title/photo), not a form, etc., file_folder is the bucket for "identifier-only" or blank metadata pages.
> Let's refine the scratchpad.
- file_folder: yes — page is almost entirely blank white space with only a rotated Bates number "2071969205" and scan artifacts (left edge noise/folder tab edge). No readable text, no topical title, no form fields. Fits "identifier-only page" or "folder-tab page" (photographed folder body/tab edge).
- presentation: no — no bold headline title, no clear photographic image (left side is noise/artifacts, not a distinct slide photo), no designed deck cover.
- Runner-up: presentation (photographic slide), ruled out because the left side is illegible scan noise/folder edge, not a clear photographic image or slide, and there is no bold title.
> Actually, looking at the left side, it looks like a very faint scan of a document page that is mostly white. But since I can't read it, I classify based on what's visible. The visible content is a Bates number.
Wait, "A page that pairs a Bates number with a photographic image... carries real content". If the left side is a photographic image (even blurred), it's presentation.
But the left side looks like vertical scan lines (noise), not a photo.
I will stick with file_folder.
> One detail: "A prominent topical heading always counts as real content... EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... is a filing label, not a bold headline title".
Here, there is no prominent topical heading. Just a Bates number.
> Final label: file_folder.

---
### `rvl_cdip__presentation__0018.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There is a vertical black bar on the right side, which looks like a scanned folder edge or slide mount artifact. There is handwritten text "1991-84 November" rotated 90 degrees. There is a Bates number "465246617" at the bottom.
> **2. Scratchpad procedure:**
> *   **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
    *   Evidence: The page is almost entirely blank. It has a vertical black bar on the right edge (looks like a folder edge or slide mount). There is handwritten text "1991-84 November" rotated 90 degrees near the top right. There is a Bates number "465246617" at the bottom.
    *   Wait, let's look at the folder-tab rule: "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB — a protruding tab-shaped piece of cardboard... bearing a short filing label... usually with a Bates number stamped on the folder body. The label IS filing metadata... The black bar is the photographed folder body/tab edge... it is NOT a slide-mount scan artifact... and a rotated filing label on a folder tab is NOT a section-divider heading."
    *   The text "1991-84 November" looks like a filing label (date range). The black bar is on the right edge. This looks exactly like a scanned folder tab.
    *   Let's check the presentation rule: "A near-blank cover or title page... is a presentation... EXCEPTION... a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab... is a folder-tab label and stays file_folder".
    *   The text "1991-84 November" is a short filing label (date range). The black bar is the folder body.
    *   So this is a file_folder page.
> *   **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
    *   Evidence: Only a small handwritten note "1991-84 November". Not majority.
    *   Not this check.
> *   **Check 3: FAX TRANSMISSION SHEET -> form**
    *   Evidence: None.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: None.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: None.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: None.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: None.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: None.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: None. The black bar could be a slide artifact, but the text "1991-84 November" is a filing label, not a title. The rule says: "BUT this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1)". Since it's a folder tab, it's file_folder.
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
The page is a scanned folder tab. It has a short filing label "1991-84 November" (rotated) and a Bates number "465246617". The black bar is the folder body. This matches the "file_folder" definition perfectly.
> Let's double check the "presentation" rule for near-blank pages.
"A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... is a presentation... EXCEPTION... a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab... is a folder-tab label and stays file_folder".
The text is "1991-84 November". This is a date range, typical for folder tabs. It is rotated. The black bar is on the right. This is a folder tab.
> Therefore, file_folder.
> Runner-up: presentation. Ruled out because the page is a photographed folder tab with a short filing label ("1991-84 November") and a Bates number, not a designed deck cover or slide. The black bar is the folder body, not a slide artifact.
> Final label: file_folder.

---

## scientific_publication → news_article (2 errors)

### `rvl_cdip__scientific_publication__0006.png`
**Expected:** `scientific_publication` | **Predicted:** `news_article`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** Top of the page says "New Scientist 17 June 1982". Page number "772". This looks like a newspaper or magazine masthead. "New Scientist" is a science magazine. Let's look closer. "M O N I T O R" is a large header. Wait, "New Scientist 17 June 1982" is at the top. "New Scientist" is a weekly news magazine covering science and technology. This looks like a news article or a section from a magazine.
- Let's check the content. "All routes are leading to the same few cancer genes". "Carcinogens act on irritated tissues". This is editorial/prose content.
- The header "New Scientist 17 June 1982" indicates a magazine/newspaper source.
- Check 12: PUBLISHED JOURNALISM -> news_article. "Newspaper or magazine masthead, byline, dateline, multi-column news typography...". "New Scientist" is a magazine. The layout is multi-column (3 columns). There is a section title "MONITOR". This fits news_article.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder.** No. There is lots of text, columns, headlines. Not just an ID.
*   **Check 2: handwritten.** No. Typed text.
*   **Check 3: FAX.** No.
*   **Check 4: questionnaire.** No.
*   **Check 5: resume.** No.
*   **Check 6: scientific_publication.** "New Scientist" is a general-audience magazine (news outlet), not a research journal like "Nature" or "Science" (though it covers science). Wait, is "New Scientist" a research journal? No, it's a news magazine. The text cites "Nature", "Science", "Proceedings of the National Academy of Sciences". These are citations. The page itself has "New Scientist 17 June 1982" and page number 772. This is a magazine page. Check 6 says: "Caveat — general news outlets: a page that presents itself as a newspaper, general-magazine... is news_article (check 12), not a publication...". "New Scientist" is a general-magazine outlet covering science. So this is likely news_article.
*   **Check 7: financial.** No.
*   **Check 8: specification.** No.
*   **Check 9: presentation.** No. It's dense text, multi-column. Not a slide.
*   **Check 10: form.** No.
*   **Check 11: correspondence.** No. No TO/FROM/Dear.
*   **Check 12: news_article.** Yes. "New Scientist 17 June 1982" is a magazine masthead/date. Multi-column typography. Headlines "All routes are leading to the same few cancer genes", "Carcinogens act on irritated tissues". This is editorial content from a magazine.
*   **Check 13: scientific_report.** No. It's a magazine article citing scientific reports. The page itself is from "New Scientist".
*   **Check 14: advertisement.** No. It's an article.
> **Re-evaluating Check 6 vs Check 12:**
- Check 6: "First, use your pre-scan finding: does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings?"
- The header is "New Scientist 17 June 1982". "New Scientist" is a magazine. Is it a journal? No. It's a news magazine.
- Check 12: "Newspaper or magazine masthead... general-audience outlet... even when the topic is scientific and journal citations appear within the text".
- The text cites "Nature", "Science", "PNAS". These are journal citations.
- The page is from "New Scientist". This is a magazine.
- So it is news_article.
> **Evidence for Check 12:**
- Masthead: "New Scientist 17 June 1982".
- Section title: "MONITOR".
- Headlines: "All routes are leading to the same few cancer genes", "Carcinogens act on irritated tissues".
- Multi-column layout (3 columns).
- Content is journalistic summary of science ("There is a sense of real excitement...", "The story starts with...").
> **Runner-up:** scientific_publication. Ruled out because "New Scientist" is a general-audience magazine (news outlet), not a research journal with volume/issue/page range identifiers typical of academic journals (though it has a page number 772, the masthead is a magazine date). The text contains citations *to* journals (Nature, Science), but the page itself is from a magazine. Wait, let's look at the header again. "New Scientist 17 June 1982". This is definitely a magazine.
> Let's check the labels.
- news_article: "Newspaper or magazine masthead... general-audience outlet". New Scientist fits this.
> Final decision: news_article.
> Wait, is "New Scientist" considered a scientific publication in this context?
The prompt says: "Caveat — general news outlets: a page that presents itself as a newspaper, general-magazine, or encyclopedia piece... is news_article (check 12), not a publication... Per check 6, this does not include a page that itself carries a research journal's own running head... (e.g., 'SCIENCE' magazine's own masthead and page number) — that stays scientific_publication".
Ah, "SCIENCE" magazine (AAAS) is a research journal/proceedings. "New Scientist" is a weekly news magazine.
The text says "New Scientist 17 June 1982".
The content is an article "All routes are leading to the same few cancer genes".
This is a magazine article. So news_article.
> Let's double check Check 6 evidence.
"evidence for this check: a named journal on the page plus a publication identifier (volume/issue, page range, DOI...)"
The page has "772" and "New Scientist 17 June 1982". "New Scientist" is not a research journal in the academic sense (like Nature, Cell, PNAS). It's a popular science magazine. The prompt explicitly distinguishes "research journal's own running head" from "general news outlets". New Scientist is a general news outlet covering science.
Also, the text cites "Nature vol 297, p 478", "Science vol 215, p 1255". These are references.
> So, Check 12 is the match.
> **Scratchpad:**
- file_folder: no — dense text, columns, headlines.
- handwritten: no — typed.
- fax: no.
- questionnaire: no.
- resume: no.
- scientific_publication: no — "New Scientist" is a general-audience magazine, not a research journal. The page cites journals (Nature, Science) but is not from one. The masthead is a magazine date.
- financial: no.
- specification: no.
- presentation: no — dense prose, multi-column.
- form: no.
- correspondence: no.
- news_article: yes — masthead "New Scientist 17 June 1982", section "MONITOR", multi-column layout, headlines "All routes are leading to the same few cancer genes", editorial prose citing scientific studies. This is a magazine article.
- scientific_report: no — it's a magazine article reporting on science, not an original research write-up.
- advertisement: no.
> Runner-up: scientific_publication. Ruled out because the masthead "New Scientist" belongs to a general-audience magazine (news outlet), not a research journal, and the text contains citations to journals rather than being a reprint from one.
> Wait, is there any chance it's a scientific_report?
"Original research write-up -> scientific_report. Running narrative prose...".
But the page has a magazine masthead. Check 12 says "Judge by DOMINANT content... page that presents itself as a newspaper, general-magazine... is news_article".
The page presents itself as "New Scientist". So news_article.
> One detail: "New Scientist" is a science magazine. Is it a "scientific_publication"?
Check 6: "Caveat — general news outlets: a page that presents itself as a newspaper, general-magazine... is news_article (check 12), not a publication, even if its text is scientific...".
New Scientist is a general-magazine (weekly news magazine).
So news_article is correct.
> Final check of the text:
Header: "772 New Scientist 17 June 1982 ... 5001000" (Bates number?)
Title: "M O N I T O R"
Headline: "All routes are leading to the same few cancer genes"
Sub-headline: "Carcinogens act on irritated tissues"
Text is 3 columns.
This is definitely a magazine page.
> Label: news_article.

---
### `rvl_cdip__scientific_publication__0016.png`
**Expected:** `scientific_publication` | **Predicted:** `news_article`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I need to follow a specific scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead or running head: Top right says "HOSPITAL-TRAINEE Monday, February 2, 1971". Top left says "16". This looks like a newspaper or magazine page. "HOSPITAL-TRAINEE" is a masthead. Multi-column news typography. Byline/dateline? "HOSPITAL-TRAINEE World Wide Report". This points toward check 12 (news_article).
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has dense text, multiple columns, headlines like "Theory of Emphysema CauseRaisesQuestions", "Clinic at U. of Va. Offers Health Care to Families", etc. Not an identifier-only page.
- Result: not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Typed text throughout. Some handwritten-looking text? No, it's typed. There's a Bates number "00622624" at the bottom right.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No fax header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No resume content.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: "HOSPITAL-TRAINEE" is a magazine/newspaper section. Wait, is it a journal? "HOSPITAL-TRAINEE" sounds like a newspaper or magazine for hospital trainees. Let's look at check 12. Check 6 requires a named journal with volume/issue/page range/DOI. "Monday, February 2, 1971" is a date. "16" is a page number. This looks like a newspaper/magazine page. Let's check check 12 first. Actually, check 6 says "general news outlets... is news_article (check 12), not a publication". "HOSPITAL-TRAINEE" is likely a newspaper/magazine. Let's assume not scientific_publication for now, or check 12 will catch it.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial tables.
- Result: not this check.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No material safety data or product specs.
- Result: not this check.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: Not a slide deck.
- Result: not this check.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: No form fields.
- Result: not this check.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: No TO/FROM/RE header or letter format.
- Result: not this check.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: Masthead "HOSPITAL-TRAINEE", date "Monday, February 2, 1971", page number "16". Multi-column news typography. Headlines like "Theory of Emphysema CauseRaisesQuestions", "Clinic at U. of Va. Offers Health Care to Families", "Antitrypsin Lack Might Increase Fertility". "HOSPITAL-TRAINEE World Wide Report". This is clearly a newspaper/magazine page with editorial content.
- Result: yes, news_article.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: The content is news articles about science (emphysema, antitrypsin), but the layout is a newspaper/magazine page. Check 12 takes precedence.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: Not an ad.
> Let's double check check 12 vs check 6.
Check 6: "First, use your pre-scan finding: does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings?"
"HOSPITAL-TRAINEE Monday, February 2, 1971" -> This is a newspaper/magazine masthead and date. Not a journal volume/issue.
Check 12: "Newspaper or magazine masthead, byline, dateline, multi-column news typography... Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content".
The page has multiple stories: "Theory of Emphysema...", "Clinic at U. of Va...", "Antitrypsin Lack Might Increase Fertility". It's a news page.
> So the label is news_article.
> Let's review the scratchpad requirements.
Walk checks 1-14 in order.
1. file_folder: no — page has dense multi-column text and headlines.
2. handwritten: no — typed text throughout.
3. fax: no — no fax header.
4. questionnaire: no — no survey items.
5. resume: no — no career history.
6. scientific_publication: no — masthead is "HOSPITAL-TRAINEE" with a date, not a journal volume/issue/DOI.
7. financial: no — no financial tables.
8. specification: no — no product specs.
9. presentation: no — not a slide deck.
10. form: no — no form fields.
11. correspondence: no — no memo/letter headers.
12. news_article: yes — masthead "HOSPITAL-TRAINEE", date "Monday, February 2, 1971", page "16", multi-column news typography with headlines like "Theory of Emphysema CauseRaisesQuestions", "Clinic at U. of Va. Offers Health Care to Families".
13. scientific_report: no — content is news articles about science, not a research write-up.
14. advertisement: no — not a promotional layout.
> Runner-up: scientific_publication, ruled out because the masthead "HOSPITAL-TRAINEE" with a date indicates a newspaper/magazine section (general-audience or trade publication), not a research journal with volume/issue/page range identifiers on this page.
> Final label: news_article.

---

## memo → form (1 errors)

### `rvl_cdip__memo__0009.png`
**Expected:** `memo` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** I see "TO:", "FROM:", "DATE:", "RE:", "TITLE:". Wait, let's look closer.
    - "OUT-OF-HOME AND POINT-OF-SALE MEDIA ADVERTISING SUBMISSION MEMO"
    - "TO: LAW DEPARTMENT"
    - "FROM: Richard [signature] L.C.A."
    - "DATE: 8-15-84" (handwritten)
    - "RE: AD NO. BYT 84-106-0004 PO"
    - "TITLE: [signature] [signature]"
    - This looks like a memo header. Is it an email? No, it's a typed memo with handwritten fields. No "From/To/Sent/Subject" in email format. It's a memo.
- **Masthead/Running head:** No newspaper masthead. No journal running head. There's a Bates number "686025221" at the bottom.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a full memo body, fields, signatures. Not just an ID.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: Most content is typed. Handwriting fills fields (date, signature, title, type of medium, size of ad, warning notice, tar/nicotine, copyright notice, submitted by, law dept signature).
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header. Just a memo.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
    *   Evidence: Not a survey. It's a submission memo for an ad.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE**
    *   Evidence: No journal identifier.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT**
    *   Evidence: Mentions "AD NO.", "30-sheet", "sq. ft./feet". Not a bill or budget.
    *   Result: not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
    *   Evidence: Not an MSDS or product spec.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
    *   Evidence: Not a slide. It's a document.
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM**
    *   Evidence: It has fields (Type of Medium, Size of Ad, Warning Notice, Tar/Nicotine, Copyright Notice, Submitted by, Law Department). It looks like a form.
    *   Wait, let's look at the header: "OUT-OF-HOME AND POINT-OF-SALE MEDIA ADVERTISING SUBMISSION MEMO".
    *   It has a memo header (TO, FROM, DATE, RE, TITLE).
    *   Check 11 is Correspondence (memo). Check 10 is Form.
    *   Let's check the rules for Memo vs Form.
    *   Check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
    *   Here we have:
        *   Header: TO: LAW DEPARTMENT, FROM: [Name], DATE: 8-15-84, RE: AD NO..., TITLE: [Name].
        *   Prose: "Attached for Law Department review is a stat of the mechanical for the ad described in this memo..."
        *   Then there are fields: TYPE OF MEDIUM, SIZE OF AD, WARNING NOTICE, "TAR" AND NICOTINE, COPYRIGHT NOTICE.
        *   Then signatures: Submitted by, Law Department.
    *   The document is titled "SUBMISSION MEMO".
    *   The structure is Memo header + Prose + Form fields (for the ad details) + Signatures.
    *   Check 11 says: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
    *   The prose is there: "Attached for Law Department review is a stat of the mechanical..."
    *   The fields below seem to be part of the memo's content (specifying the ad details), or it's a hybrid.
    *   Let's look at Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
    *   This document has an approval block ("Submitted by", "Law Department" with signature and date 8-16-84).
    *   However, the title is "SUBMISSION MEMO".
    *   Let's re-read Check 11 carefully. "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."
    *   The header is present: TO, FROM, DATE, RE, TITLE.
    *   The prose follows: "Attached for Law Department review..."
    *   The fields (Type of medium, Size of ad, etc.) are filled in by hand.
    *   Is this a form or a memo?
    *   The title says "MEMO".
    *   The structure is TO/FROM/DATE/RE/Title -> Prose -> Specific details (fields) -> Signatures.
    *   Usually, if it has a memo header and prose, it's a memo. The fields are just part of the memo content (specifying the ad parameters).
    *   Wait, look at the bottom: "ORIGINAL - returned to Brand Group", "PHOTOCOPY - retained by Law Department". This is typical of a memo distribution.
    *   The fields "Type of Medium", "Size of Ad", etc., look like a form attached to the memo or part of the memo.
    *   Let's look at the "Runner-up" logic. If I choose memo, what is the runner-up? Form.
    *   Why form? Because it has fields like "Type of Medium: 30-sheet", "Size of Ad: 234 sq. ft./feet", "Warning Notice: Eq #112", "Tar and Nicotine: 34 mg", "Copyright Notice: 1984 B&W T. Co.". And signatures.
    *   But the header is explicitly a memo header. "OUT-OF-HOME AND POINT-OF-SALE MEDIA ADVERTISING SUBMISSION MEMO".
    *   Check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
    *   The text "Attached for Law Department review is a stat of the mechanical..." is memo-style prose.
    *   The fields below elaborate on the "AD NO." mentioned in the RE line.
    *   The signatures are at the bottom.
    *   This fits "memo" best. It's a memo submitting an ad for review. The fields are just the details of the ad being submitted.
    *   Let's check if there's a stronger case for "form".
    *   Check 10: "internal authorization/approval forms with an approval signature/date block."
    *   This has an approval block (Law Department signature).
    *   But Check 11 (Correspondence -> memo) comes before Check 10 (Form)? No, the checks are numbered 1-14.
    *   Wait, the instructions say: "Walk checks 1-14 below IN ORDER... Once an earlier check matches, later checks do not override it."
    *   Check 11 is Correspondence (email, memo, letter).
    *   Check 10 is Administrative Form.
    *   So if it's a memo (Check 11), it stops there. Check 10 is later.
    *   Let's verify Check 11 match.
    *   Header: TO: LAW DEPARTMENT, FROM: [Richard...], DATE: 8-15-84, RE: AD NO..., TITLE: [Brand name].
    *   This is a TO/FROM/DATE/RE/TITLE block.
    *   Followed by prose: "Attached for Law Department review is a stat of the mechanical..."
    *   This is a memo.
    *   The fact that it has fields filled in doesn't make it a form if the primary structure is a memo.
    *   Actually, let's look at the title: "OUT-OF-HOME AND POINT-OF-SALE MEDIA ADVERTISING SUBMISSION MEMO".
    *   It is explicitly a memo.
> Let's double check Check 10 vs Check 11 order.
The list is:
1. file_folder
2. handwritten
3. form (fax) -> wait, check 3 is "FAX TRANSMISSION SHEET -> form".
4. questionnaire
5. resume
6. scientific_publication
7. financial document
8. specification
9. presentation
10. administrative form -> form
11. correspondence -> email, memo, letter
> So Check 11 (memo) comes *after* Check 10 (form).
Wait. "Walk checks 1-14 below IN ORDER... Once an earlier check matches, later checks do not override it."
If Check 10 matches (form), and Check 11 matches (memo), which one wins?
Check 10 is "ADMINISTRATIVE FORM -> form".
Check 11 is "CORRESPONDENCE -> email, memo, or letter".
If the page is a memo, Check 11 matches. If the page is a form, Check 10 matches.
Since 10 < 11, if it's a form, it stops at 10.
If it's a memo, it passes 10 (if 10 doesn't match) and stops at 11.
> Does Check 10 match?
"Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
The page has fields: Type of Medium, Size of Ad, Warning Notice, Tar/Nicotine, Copyright Notice.
It has an approval block: "Submitted by: [sig]", "Law Department: [sig] 8-16-84".
This looks like a form. Specifically, an "Advertising Submission Form" or similar, titled as a memo.
However, the text says "SUBMISSION MEMO".
And the top block is TO/FROM/DATE/RE/TITLE.
Usually, a document with a memo header and prose is a memo, even if it has some form-like fields at the bottom.
But let's look at the definition of Memo in Check 11: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
The header is there. The prose is there ("Attached for Law Department review...").
The fields are below the prose.
The prose explains the attachment ("stat of the mechanical").
The fields seem to be details *of* the ad being submitted, or maybe the "stat" details.
Actually, the text says: "Attached for Law Department review is a stat of the mechanical for the ad described in this memo."
Then it lists details: Type of Medium, Size of Ad, etc. These look like the details of the "stat" or the ad itself.
Then signatures.
> Is this a form or a memo?
If I look at Check 10: "internal authorization/approval forms with an approval signature/date block."
This has an approval block.
But Check 11 says: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
The header is followed by prose.
The prose is followed by fields.
The fields are filled in.
This is a hybrid.
However, the title is "SUBMISSION MEMO".
And the top is a memo header.
In the tobacco archive, these "Submission Memos" for legal review are often memos.
Let's look at the "Runner-up" instruction. "add one final line naming the runner-up label you almost picked instead".
> Let's re-evaluate Check 10 vs Check 11.
If I classify as memo (Check 11):
Evidence: Header "TO: LAW DEPARTMENT", "FROM: [Name]", "DATE: 8-15-84", "RE: AD NO...", "TITLE: [Brand]". Prose: "Attached for Law Department review...".
Runner-up: form (Check 10). Why? Because it has fields (Type of Medium, Size of Ad) and an approval signature block (Law Department signature). But the primary structure is a memo header + prose + approval. The title is "SUBMISSION MEMO".
> If I classify as form (Check 10):
Evidence: Fields for Type of Medium, Size of Ad, Warning Notice, Tar/Nicotine, Copyright Notice. Approval signatures.
But Check 11 is later. If Check 10 matches, I stop.
Does Check 10 match? "Filled or blank fields... for capturing factual data". Yes. "internal authorization/approval forms". Yes.
But Check 11 is "CORRESPONDENCE".
Usually, correspondence (memo/letter) takes precedence if the document is primarily a communication.
The document is communicating a submission to the Law Department.
The fields are just the content of the submission.
The title is "SUBMISSION MEMO".
I will go with **memo**.
> Wait, let's look at the order again.
1. file_folder
2. handwritten
3. fax (form)
4. questionnaire
5. resume
6. scientific_publication
7. financial (invoice/budget)
8. specification
9. presentation
10. form
11. correspondence (email/memo/letter)
> If a document is a memo, it matches Check 11.
If a document is a form, it matches Check 10.
Since 10 < 11, if it matches Check 10, I must stop there.
Does it match Check 10?
"Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
The page has ruled entry lines (underlines) for "Type of Medium", "Size of Ad", etc.
It has an approval signature block.
So Check 10 has positive evidence.
Does Check 11 have positive evidence?
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
The header is there. The prose is there.
So both Check 10 and Check 11 have evidence.
Since 10 comes before 11, and 10 matches, I should stop at 10?
Wait. "Once an earlier check matches, later checks do not override it."
This implies if Check 10 matches, it's a form.
BUT, is a "Submission Memo" a form?
The title says "MEMO".
The top block is a memo header.
The text is prose.
The fields are part of the memo content (describing the ad).
Check 10 says: "A form does NOT have to be blank... This also covers: ... internal authorization/approval forms with an approval signature/date block."
Check 11 says: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
> Let's look at the content.
The document is a memo *about* an ad submission.
The fields (Type of medium, size, etc.) are filled in.
Is this a "filled form"?
Yes, it looks like a form filled in.
But it has a memo header.
Often, these are "Memo-Forms".
Which label wins?
The instructions say: "Judge each page by its FUNCTION... a page full of technical data can still be a form... but a bill is a bill even when it is printed on a form."
Here, the function is to submit an ad for legal review.
The document is titled "SUBMISSION MEMO".
The header is TO/FROM/DATE/RE.
This is the definition of a memo.
The fields are just the details.
If I look at Check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
The prose is "Attached for Law Department review is a stat of the mechanical...".
This is memo-style prose.
The fields follow.
The signatures follow.
This is a memo.
> Why would it be a form (Check 10)?
If the primary function is capturing data (Type of medium, size, etc.) and getting approval.
But the text says "Attached... is a stat... for the ad described in this memo."
The fields describe the ad.
It's a memo describing an ad, with specific fields filled out, and signed off.
I think **memo** is the correct label. The title is literally "SUBMISSION MEMO".
And Check 11 is "CORRESPONDENCE -> email, memo, or letter".
The label is "memo".
> Let's check the labels list: `advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification`.
So "memo" is a valid label.
> Let's reconsider Check 10.
"administrative form -> form".
If I stop at Check 10, the label is "form".
If I go to Check 11, the label is "memo".
The rule: "Walk checks 1-14 below IN ORDER. For each check, before moving to the next one, briefly state... If evidence is present: STOP HERE."
So if Check 10 has evidence, I stop and say "form".
Does Check 10 have evidence?
"Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data" -> Yes (Type of Medium: 30-sheet, etc.).
"internal authorization/approval forms with an approval signature/date block" -> Yes (Submitted by, Law Department signature).
So Check 10 matches.
I must stop at Check 10?
Wait. "Once an earlier check matches, later checks do not override it."
This means if Check 10 matches, the label is "form" (from Check 10 header "ADMINISTRATIVE FORM -> form").
BUT, Check 11 is "CORRESPONDENCE -> email, memo, or letter".
If the document is a memo, it matches Check 11.
If the document is a form, it matches Check 10.
Since 10 < 11, if it matches 10, it's a form.
Is a "Submission Memo" with fields a form?
The instructions say: "Do not rush to the label that matches the page's subject matter... deliberate through the checks below, in order, and commit to the FIRST one with strong, concrete evidence".
Check 10 evidence: Fields (Type of Medium, Size of Ad, etc.) and approval signatures. This is strong evidence for "form".
Check 11 evidence: TO/FROM/DATE header and prose. This is strong evidence for "memo".
Since Check 10 comes before Check 11, and Check 10 has evidence (fields, approval block), I should stop at Check 10?
> Let's look at the "Runner-up" instruction. "add one final line naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out."
If I pick "memo" (Check 11), the runner-up is "form" (Check 10). Evidence ruling out form: The document is primarily a memo (header + prose + title "SUBMISSION MEMO"), and the fields are just details within the memo, not the primary structure of a standalone form. Wait, if I pick memo, I am saying Check 10 did NOT match or was overridden?
No, the rule is "commit to the FIRST one with strong, concrete evidence".
If Check 10 has strong evidence, I must pick it.
Does Check 10 have strong evidence?
"Filled or blank fields... ruled entry lines... approval signature/date block."
Yes, the page has underlined fields filled with handwriting ("30-sheet", "234 sq. ft./feet", "Eq #112", "34 mg", "1984 B&W T. Co.") and two signature blocks with dates.
This fits "form" perfectly.
BUT, the title is "SUBMISSION MEMO".
And the top is a memo header.
Is there a conflict?
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
The structure IS there.
So it matches Check 11.
Does it match Check 10? Yes.
Which one wins? The first one in order. Check 10 is before Check 11.
So if Check 10 matches, the label is "form".
> Let's re-read the priority.
"Walk checks 1-14 below IN ORDER... commit to the FIRST one with strong, concrete evidence... Once an earlier check matches, later checks do not override it."
This is a strict priority list.
1. file_folder
2. handwritten
3. fax (form)
4. questionnaire
5. resume
6. scientific_publication
7. financial
8. specification
9. presentation
10. form
11. correspondence (memo)
> If a page is a memo with form fields, Check 10 (form) comes first.
Does Check 10 match?
"Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
The page has ruled entry lines (underlines) with handwritten data.
It has an approval signature block.
So Check 10 matches.
Therefore, the label should be **form**.
> Wait, let's look at the memo definition again.
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
The header is there. The prose is there.
So Check 11 matches.
Since 10 < 11, and 10 matches, the label is "form".
> Is there any reason Check 10 would NOT match?
"A form does NOT have to be blank... This also covers: ... internal authorization/approval forms with an approval signature/date block."
This page is an authorization/approval form (Law Department approval of an ad submission).
It has fields.
So it is a form.
> But the title is "SUBMISSION MEMO".
And the top is a memo header.
In many classification tasks, "Memo" is a specific category.
Here, "memo" is a sub-category of "CORRESPONDENCE" (Check 11).
"form" is Check 10.
If the document is a memo, it should be "memo".
Why would Check 10 override Check 11?
Because of the order.
"commit to the FIRST one with strong, concrete evidence".
If I see fields and signatures (Check 10 evidence), I stop.
I don't reach Check 11.
> Let's look at the example or calibration notes.
"Filled forms are still forms; a form does not have to be blank."
"A handwritten note about a questionnaire... is questionnaire... not handwritten."
"Money mentioned inside a letter or memo's prose does not make the page invoice/budget... check 7 needs the financial content to be the page's OWN primary structure".
This implies correspondence (letter/memo) is a strong category.
But Check 7 is before Check 11.
Check 10 is before Check 11.
> Let's look at the document content again.
It's a "Submission Memo".
TO: Law Department.
FROM: Richard [Name].
DATE: 8-15-84.
RE: AD NO...
TITLE: [Brand]...
Prose: "Attached for Law Department review is a stat of the mechanical..."
Fields: Type of Medium, Size of Ad, Warning Notice, Tar/Nicotine, Copyright Notice.
Signatures: Submitted by, Law Department.
> This is a memo that *contains* a form-like section or is a hybrid.
If I have to choose between Form (Check 10) and Memo (Check 11).
Check 10: "administrative form -> form".
Check 11: "correspondence -> email, memo, or letter". Label is "memo".
> If I choose "memo":
Evidence: Header TO/FROM/DATE/RE/TITLE, prose "Attached for Law Department review...", title "SUBMISSION MEMO".
Runner-up: "form". Evidence: Fields (Type of Medium, etc.) and approval signatures. Why ruled out? Because the document is primarily a memo (title, header, prose) and the fields are just details within the memo, not a standalone form structure. Wait, if I ruled out form, I must say why Check 10 didn't match or was overridden.
The rule says: "commit to the FIRST one with strong, concrete evidence".
If Check 10 has evidence, I MUST stop at Check 10.
Unless Check 10 evidence is not "strong" or "concrete" enough?
"Filled or blank fields... ruled entry lines... approval signature/date block."
The evidence is very concrete. Underlines with handwriting. Signatures.
So Check 10 matches.
So the label must be **form**.
> Wait, is there a "memo" label? Yes.
Is there a "form" label? Yes.
If the document is a memo, why would it be classified as form?
Because Check 10 comes before Check 11.
This seems like a trap.
"Deliberate through the checks below, in order, and commit to the FIRST one with strong, concrete evidence".
If I see fields (Check 10), I stop. I don't look for memo header (Check 11).
So the label is **form**.
> Let's check if there's any other check.
Check 3: Fax transmission sheet. No.
Check 4: Questionnaire. No.
> Let's look at the "Runner-up" instruction again.
"Once you stop at a matching check, add one final line naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out."
If I stop at Check 10 (form), the runner-up is Check 11 (memo).
Evidence that ruled out memo: The document has filled fields and an approval block, which are defining characteristics of a form (Check 10), and Check 10 precedes Check 11. Wait, the evidence that ruled out memo... memo requires "header-then-prose structure". The document has that. So memo is a strong candidate.
Why is form the winner? Because Check 10 is earlier.
The single piece of evidence that ruled out memo (as the final label) is that Check 10 (form) matched first.
Actually, the instruction says: "naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out."
If I pick "form", the runner-up is "memo". The evidence that ruled out "memo" (i.e., why I didn't pick it as the final label) is that Check 10 (form) matched first and has priority. Or, more content-wise, the presence of filled fields and approval signatures makes it a form, which takes precedence.
> Let's reconsider. Is this document a "memo"?
Title: "OUT-OF-HOME AND POINT-OF-SALE MEDIA ADVERTISING SUBMISSION MEMO".
It is explicitly a memo.
If I classify it as "form", I am ignoring the title and the memo header.
But the instructions say: "Walk checks 1-14 below IN ORDER... commit to the FIRST one with strong, concrete evidence".
Check 10 evidence: "Type of Medium: 30-sheet", "Size of Ad: 234...", signatures. These are filled fields.
Check 11 evidence: "TO: LAW DEPARTMENT", "FROM: ...", prose.
Both have evidence.
Check 10 is before Check 11.
So I must pick **form**.
> Wait, let's look at Check 11 text: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
The structure is there.
Check 10 text: "Filled or blank fields... internal authorization/approval forms with an approval signature/date block."
The structure is there.
> Is there a nuance?
"A form does NOT have to be blank... This also covers: ... internal authorization/approval forms with an approval signature/date block."
This document is an authorization form (Law Department approval).
It is also a memo.
Priority: Form (10) > Memo (11).
So label is **form**.
> Let's check if "memo" is the intended label.
In the tobacco archive, these are often called "Submission Memos".
But functionally, it's a form for legal review.
The fields capture the ad details.
The signatures capture approval.
It's a form.
> Let's look at the scratchpad example 4.
"financial: yes... Runner-up: budget".
It stops at the first match.
> So for this page:
Check 1: file_folder. No. (Has content)
Check 2: handwritten. No. (Mostly typed)
Check 3: fax. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial. No. (Not a bill/budget)
Check 8: specification. No.
Check 9: presentation. No.
Check 10: form. Yes. Fields (Type of Medium, Size, etc.), approval signatures.
Stop here. Label: form.
> Runner-up: memo. Evidence: The page has a memo header (TO/FROM/DATE/RE) and is titled "SUBMISSION MEMO", but Check 10 (form) has priority because it appears earlier in the list and the page contains filled fields and an approval block.
> Wait, is there any chance it's "advertisement"?
Check 14: Promotional material.
The document is *about* an advertisement ("AD NO...", "Type of Medium: 30-sheet", "Brand Group").
But the document itself is a submission memo/form for legal review.
It is not the ad itself.
So not advertisement.
> Final decision: **form**.
> One detail: "OUT-OF-HOME AND POINT-OF-SALE MEDIA ADVERTISING SUBMISSION MEMO".
The header is:
TO: LAW DEPARTMENT
FROM: Richard [signature] L.C.A.
DATE: 8-15-84
RE: AD NO. BYT 84-106-0004 PO
TITLE: [signature] [signature] (looks like "Brandgroup letter" or similar)
> Then prose.
Then fields.
Then signatures.
> The fields are:
TYPE OF MEDIUM: 30-sheet
SIZE OF AD: 234 sq. ft./feet
WARNING NOTICE: Eq #112
"TAR" AND NICOTINE: 34 mg
COPYRIGHT NOTICE: 1984 B&W T. CO.
> Submitted by: [signature]
Law Department: [signature] 8-16-84
> This is a filled form with a memo header.
Check 10 matches "Filled or blank fields... internal authorization/approval forms".
Check 11 matches "memo".
Check 10 < Check 11.
Label: form.
> Wait, looking closely at the label list: `advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification`.
If I choose "form", the label is `form`.
> Let's double check if "memo" is a better fit.
The instructions say: "Judge each page by its FUNCTION... a page full of technical data can still be a form... but a bill is a bill even when it is printed on a form."
Here, the function is legal review submission.
The document is a "Submission Memo".
If I call it "form", I am ignoring the "Memo" title.
But the rules say "commit to the FIRST one with strong, concrete evidence".
Check 10 evidence: Filled fields, approval block.
Check 11 evidence: Memo header, prose.
Both are strong.
Check 10 is first.
So "form".
> Is there any exception?
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
The structure is there.
"A page whose primary structure is a memo header + prose, but whose prose merely discusses, forwards, or requests approval of an invoice/bill... stays memo".
This page discusses/requests approval of an ad.
But Check 10 is "internal authorization/approval forms with an approval signature/date block".
This page HAS an approval signature/date block.
So Check 10 matches.
> I will go with **form**.
> Wait, let's look at the "Runner-up" line in the worked examples.
Worked example 1: Questionnaire. Runner-up: form.
Worked example 4: Invoice. Runner-up: budget.
> If I choose form:
Runner-up: memo.
Evidence: The page has a memo header (TO/Law Department, FROM/...) and title "SUBMISSION MEMO", but the filled fields and approval block trigger Check 10 (form) which precedes Check 11 (memo).
> Actually, looking at the layout, it's a memo *with* a form at the bottom?
No, the fields are inline.
"TYPE OF MEDIUM: 30-sheet ... (e.g., 30 sheet, exterior transit, shelf talker)"
This looks like a form field with a hint.
"SIZE OF AD: 234 sq. ft./feet (efface one)"
"WARNING NOTICE: Eq #112"
These are form fields.
The top is a memo header.
It's a hybrid.
Priority rule: Check 10 (form) > Check 11 (memo).
So **form**.
> One more check: Check 3 "FAX TRANSMISSION SHEET -> form".
Not a fax sheet.
> Check 10: "ADMINISTRATIVE FORM -> form".
Yes.
> Final label: form.
> Wait, is it "memo"?
Let's consider the phrase: "Once an earlier check matches, later checks do not override it."
This is the key.
Check 10 matches. Check 11 matches.
Check 10 is earlier.
So label is form.
> The label string is "form".
> One detail: "A page whose primary structure is a memo header + prose... stays memo".
Does this page have "primary structure" as memo header + prose?
The header is small. The prose is one paragraph.
The fields take up the bottom half.
The signatures take up the bottom.
The primary structure might be the form (fields + approval).
The title is "SUBMISSION MEMO".
But functionally, it's a form for data capture (ad details) and approval.
So "form" is appropriate.
> I'll write the scratchpad.
- file_folder: no — page has body content, fields, signatures.
- handwritten: no — mostly typed, handwriting fills fields.
- fax: no — no fax header.
- questionnaire: no — not a survey.
- resume: no.
- scientific_publication: no.
- financial: no — not a bill/budget.
- specification: no.
- presentation: no.
- form: yes — filled fields (Type of Medium, Size of Ad, etc.) and approval signature block (Law Department). Matches Check 10.
- memo: (skipped because Check 10 matched first, but has evidence: TO/FROM header, title "SUBMISSION MEMO"). Runner-up.
> Wait, if I stop at Check 10, I don't evaluate Check 11?
"Walk checks 1-14 below IN ORDER. For each check, before moving to the next one, briefly state... If evidence is present: STOP HERE."
So I stop at Check 10.
I don't need to evaluate Check 11 in the scratchpad steps, but I need to mention the runner-up.
The runner-up is memo.
> Label: form.

---

## budget → scientific_report (1 errors)

### `rvl_cdip__budget__0007.png`
**Expected:** `budget` | **Predicted:** `scientific_report`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** None. There's a "RECEIVED" stamp, but no From/To/Sent/Subject.
- **Masthead/Running head:** Top has "Tobacco Institute" logo and "cigarette tax data". Address: "1875 I Street, N.W. Washington, D.C. 20006 800/424-9876". This looks like a report header, not a newspaper/magazine masthead or journal running head. Bottom has "THILBC 005161" (Bates number).
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a title "Monthly State Cigarette Tax Report", "Report for February 1989", and several paragraphs of text. It has real content.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: The text is typed. There is a "RECEIVED" stamp and a handwritten "2 D 19c" (maybe a date or code), but the majority is typed text.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" or fax cover sheet header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No questions, rating scales, or survey instrument. It's a report.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No CV/resume content.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal name, volume, issue, page range, DOI on the page itself. The header is "Tobacco Institute cigarette tax data".
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: The text discusses tax collections, package counts, dollar amounts ($329,259,463, $350,569,062, $93.2 million).
    *   Is it an invoice? No, it's not a vendor bill for goods sold.
    *   Is it a budget? "Monthly State Cigarette Tax Report". It reports on tax collections. Let's look at the definition of budget: "internal money planning, tracking, or disbursement... Also covers money-only records... a provider's periodic customer statement... is budget, not invoice". Wait, this is a report *about* tax data.
    *   Let's re-read Check 7 carefully. "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This page is primarily running narrative prose describing tax data ("In February 1989, cigarette taxes in the 50 states..."). It mentions money, but the structure is a report/prose.
    *   Wait, is it a scientific_report? "Running narrative prose with objectives, methods, results, or discussion". This is a report of data. "Monthly State Cigarette Tax Report".
    *   Let's check Check 13: scientific_report. "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page...". This is a report of statistical data (tax collections). Is it a scientific report? Or is it a form? Or a presentation?
    *   Let's look at the labels again.
    *   advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
    *   The document is a "Monthly State Cigarette Tax Report" from the Tobacco Institute. It contains narrative text explaining the data.
    *   Let's re-evaluate Check 7 (Financial). "Money function overrides form layout... invoice: an outside vendor... budget: internal money planning, tracking...". This is a report *about* taxes. It's not a budget (planning/tracking internal money) or an invoice (vendor bill). It's a report of external data.
    *   Let's look at Check 13 (scientific_report). "Running narrative prose with objectives, methods, results, or discussion". This page has results (tax data, package counts). It's a technical report of data. "THILBC 005161" is a Bates number. The Tobacco Institute produced many such reports. These are often classified as scientific_report or just reports. Wait, is there a better category?
    *   Let's look at Check 9 (presentation). "Slide/overhead layouts... deck title...". This is a text-heavy page. Not a presentation.
    *   Let's look at Check 12 (news_article). No masthead.
    *   Let's look at Check 10 (form). No fields/boxes.
    *   Let's look at Check 11 (correspondence). No TO/FROM/RE header. No salutation.
    *   So it's likely scientific_report. The Tobacco Institute published technical reports and data summaries. This looks like a page from a report or a standalone report page. "Running narrative prose with... results". The results are the tax data.
    *   Wait, is it a "specification"? No.
    *   Is it a "budget"? "budget: internal money planning, tracking, or disbursement...". This is a report of state tax data. Not internal tracking.
    *   Is it an "invoice"? No.
>     Let's reconsider the "scientific_report" definition. "Original research write-up... Running narrative prose with objectives, methods, results, or discussion". This page is just "Results" (data) and some commentary. "Report for February 1989". It's a periodic report.
    Actually, let's look at the content. It's a "Monthly State Cigarette Tax Report". It's a data report.
    In this dataset (tobacco archive), reports from the Tobacco Institute like this are often classified as `scientific_report` if they contain narrative prose about data, or sometimes just as reports. But the labels are limited.
    Let's check if there's a better fit.
    Could it be `form`? No.
    Could it be `presentation`? No.
>     Let's look at the structure.
    Header: Tobacco Institute, cigarette tax data.
    Title: Monthly State Cigarette Tax Report.
    Subtitle: Report for February 1989.
    Body: 5 paragraphs of text.
    Footer: THILBC 005161.
>     This is a narrative report. `scientific_report` fits "Running narrative prose with... results". Even if it's not "original research" in the academic sense, in the context of these labels, internal technical reports/data summaries from institutes are usually `scientific_report`.
    Wait, is there a `report` label? No. The labels are: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
    So `scientific_report` is the catch-all for technical reports/narrative prose documents that aren't publications.
>     Let's check `budget` again. "budget: internal money planning, tracking, or disbursement...". This is tracking tax collections. But it's not internal money planning for the company. It's a report on state taxes.
    "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This page is primarily narrative prose. So Check 7 does not apply.
>     So we are left with `scientific_report` (Check 13).
    "Running narrative prose with objectives, methods, results, or discussion".
    The page has results (package counts, tax aggregates). It has discussion/notes ("Note: This reports tax collections only...").
    It is a technical document from the Tobacco Institute.
>     Let's double check `news_article`. No masthead.
    Let's double check `letter`/`memo`. No header.
>     So `scientific_report` seems the best fit.
>     Wait, is there any other category?
    What about `form`? No.
    What about `specification`? No.
>     Let's re-read the `scientific_report` definition. "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page with authors and an internal affiliation and no journal identifiers."
    This page has no author listed, just "Tobacco Institute". But it has narrative prose and results.
    "Also scientific_report: ... a technical/project status report whose content is primarily technical... even when it embeds a budget-vs-actual cost section".
    This is a data report.
>     Let's look at the "Note" at the bottom. "Note: This reports tax collections only...". This is explanatory text.
>     Conclusion: `scientific_report`.
>     Wait, let's look at the header again. "cigarette tax data". "Monthly State Cigarette Tax Report".
    Is it a `budget`?
    "budget: ... a statement of account ... a check face ... a provider's periodic customer statement ... is budget".
    This is a report *from* the Tobacco Institute *about* cigarette tax data. It's not a bill to the Tobacco Institute. It's a report produced by them.
    So not budget.
>     Is it `invoice`? No.
>     So `scientific_report`.
>     Let's refine the scratchpad.
    Check 1: file_folder. No, has text.
    Check 2: handwritten. No, typed.
    Check 3: fax. No.
    Check 4: questionnaire. No.
    Check 5: resume. No.
    Check 6: scientific_publication. No journal ID.
    Check 7: financial. Narrative prose, not a line-item table/ledger. Money is mentioned but not the primary structure (table/bill).
    Check 8: specification. No.
    Check 9: presentation. No, dense text.
    Check 10: form. No fields.
    Check 11: correspondence. No TO/FROM/RE or salutation.
    Check 12: news_article. No masthead.
    Check 13: scientific_report. Yes. Narrative prose reporting results (tax data, package counts) with a note. Internal technical report from Tobacco Institute.
    Check 14: advertisement. No.
>     Runner-up: budget. Ruled out because the page is narrative prose reporting external tax data, not an internal financial tracking document, line-item table, or bill (Check 7 requires financial content to be the primary structure like a table/bill, whereas here money is just the subject of the prose). Or runner-up: form. Ruled out because no fields/boxes.
>     Actually, looking at the labels, `scientific_report` is the standard label for these Tobacco Institute data reports (THILBC series). THILBC likely stands for Tobacco Institute Library/Bibliography Control or similar Bates prefix. These are technical reports.
>     Final check: "Running narrative prose with objectives, methods, results, or discussion".
    The text describes results: "In February 1989... imposed on 1,794,409,000 packages... decrease of 6.56 percent...".
    It discusses cumulative figures.
    It has a note explaining the data.
    This fits `scientific_report`.

---

## form → file_folder (1 errors)

### `rvl_cdip__form__0004.png`
**Expected:** `form` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header: None.
- Masthead/running head: None. There is text "Insecticides" rotated 90 degrees on the right side, and a number "51303 2938" rotated 90 degrees at the bottom right. Wait, let's look at the orientation. The text "Insecticides" is at the top right, rotated 90 degrees clockwise. The number "51303 2938" is at the bottom right, rotated 90 degrees clockwise.
- Let's re-orient mentally. If I rotate the image 90 degrees counter-clockwise:
    - Top left: "Insecticides" (rotated) -> actually, if I rotate CCW, "Insecticides" is at the top, reading left-to-right? No, "Insecticides" is written vertically. Let's assume the text is upright if I rotate the page 90 degrees clockwise.
    - If I rotate 90 degrees clockwise: "Insecticides" is at the top right, reading downwards? No, "Insecticides" is written with the top of the letters facing left. So if I rotate the image 90 degrees counter-clockwise, "Insecticides" is at the top, reading left-to-right. Wait.
    - Let's look at the text "Insecticides". The 'I' is at the top, 's' is at the bottom. The letters are oriented such that the top of the letters points to the left. So if I rotate the image 90 degrees clockwise, the text "Insecticides" will be at the top right, reading left-to-right? No.
    - Let's trace: 'I' is top, 'n' is below it... 's' is bottom. The baseline is on the right. So if I rotate 90 degrees counter-clockwise, the text will be at the top, reading left-to-right. Wait. If baseline is on the right, rotating 90 degrees CCW puts the baseline at the bottom. Yes.
    - So "Insecticides" is a heading at the top right (or top margin).
    - "51303 2938" is at the bottom right. Baseline is on the right. Rotating 90 degrees CCW puts it at the bottom right. This looks like a Bates number or archive number.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: The page is almost entirely blank white space.
    *   Text present: "Insecticides" (rotated) and "51303 2938" (rotated).
    *   Is "Insecticides" a bold topical heading? The instructions say: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
    *   "A prominent topical heading always counts as real content, subtitle or not." -> "Insecticides" is a short phrase heading.
    *   Wait, let's look at the exception: "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... The label IS filing metadata... so it is NOT a 'topical title' for this check."
    *   Is this a folder tab? The image has a solid black bar along the right edge (and bottom edge). This looks like a photographed folder tab or a slide.
    *   Let's check the black bar description: "a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
    *   BUT: "BUT this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label (product/collection/month/file name), and a Bates number is file_folder even though the folder body photographs as a solid black bar and the label may be rotated."
    *   Let's look at the content. "Insecticides" is a short label. "51303 2938" is a Bates number (looks like an archive number, 5 digits space 4 digits).
    *   Is "Insecticides" a filing label for a folder? Yes, it names the contents of the folder (Insecticides).
    *   The page is essentially a blank white space with a black border on the right and bottom (folder body/tab edge) and the label "Insecticides" and the number "51303 2938".
    *   This matches the "Folder-tab pages" description perfectly: "a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... bearing a short filing label that names the folder's contents... usually with a Bates number stamped on the folder body... The black bar is the photographed folder body/tab edge... it is NOT a slide-mount scan artifact... and a rotated filing label on a folder tab is NOT a section-divider heading."
    *   So, Check 1 (file_folder) is a strong match.
> *   **Check 9: presentation**
    *   "A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider even alongside a small handwritten letter/number annotation — but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab (product/collection/month/file name, e.g. 'NEWTROL', 'Litigation Content', 'FEBRUARY') is a folder-tab label and stays file_folder (check 1)."
    *   "Insecticides" is a short filing label naming the folder's contents.
    *   The black bar is the folder body.
    *   Therefore, it is file_folder, not presentation.
> *   **Check 1: file_folder (re-evaluated)**
    *   Evidence: Rotated text "Insecticides" (filing label), rotated number "51303 2938" (Bates number/archive stamp), solid black bar along the right/bottom edges (photographed folder body).
    *   Conclusion: file_folder.
> Let's double check if "Insecticides" could be a section divider for a presentation.
The instructions say: "A large heading rotated 90 degrees... is a section divider... BUT a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab... is a folder-tab label and stays file_folder".
"Insecticides" is a short label (one word). It names the contents (insecticides). The black bar is the folder body. The number is a Bates number. This is a classic folder tab scan.
> So, Check 1 matches.
> Let's quickly check other labels just in case.
- handwritten: no.
- form: no.
- questionnaire: no.
- resume: no.
- scientific_publication: no.
- invoice/budget: no.
- specification: no.
- email/memo/letter: no.
- news_article: no.
- advertisement: no.
> The page is a scanned folder tab.
Label: file_folder.
> Evidence for Check 1:
- Rotated short label "Insecticides" naming folder contents.
- Rotated Bates number "51303 2938".
- Solid black bar along the right/bottom edges indicating photographed folder body/tab edge.
- No sentences, no topical title beyond the filing label.
> Runner-up: presentation (section divider), ruled out because the rotated label "Insecticides" is a short filing label on a photographed folder tab (indicated by the black bar and Bates number), not a designed deck section divider.
> Final check of the text: "Insecticides" and "51303 2938".
The number 51303 2938 is a Bates number format (often 5-6 digits then 4 digits, or similar).
The layout is classic folder tab.
> One detail: "A page is NOT file_folder if it carries any real content... A prominent topical heading always counts as real content... EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... is a filing label, not a bold headline title... The page stays file_folder even when the label is rotated 90 degrees... The black bar is the photographed folder body/tab edge".
This fits perfectly.
> Final decision: file_folder.

---

## form → letter (1 errors)

### `rvl_cdip__form__0006.png`
**Expected:** `form` | **Predicted:** `letter`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, checking each condition in order.
> **Pre-scan:**
- Mail-client header block: No "From/To/Sent/Subject" in email format. There is a "To:/From:/Date:" block, but it's inside a box at the top, typical of a fax cover sheet or memo. Wait, let's look closer.
- Masthead/running head: No newspaper/magazine masthead. No journal running head.
> **Check 1: file_folder**
- Content: There is a header block, a letter body ("Mike, As promised, here are:..."), a signature ("Sue"). Not just an identifier. -> not this check.
> **Check 2: handwritten**
- Most content is typed. Only a signature "Sue" and maybe some minor marks. -> not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Header: "LORILLARD TOBACCO COMPANY / Market Planning and Information Department"
- Box with:
  To: Mike Mozina
  Firm: MSA
  FAX #: Autodial
  From: Susan Smith
  FAX #: 335-7733
  Phone #: 335-7150
  Date: 8/31/98
  # Pages: 3 (including this cover page)
- This looks exactly like a fax cover sheet. "FAX #:", "# Pages: 3 (including this cover page)".
- Wait, is it a fax cover sheet? "FACSIMILE TRANSMISSION" is not explicitly at the top, but it has "FAX #:", "# Pages: 3 (including this cover page)".
- Let's check the rules for Check 3: 'A "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", or "TELEFAX MESSAGE NO." header with To/From/company/phone/page-count fields. Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels.'
- Does this page have one of those headers? It has "LORILLARD TOBACCO COMPANY / Market Planning and Information Department". It doesn't explicitly say "FAX COVER SHEET" or "FACSIMILE TRANSMISSION" at the very top, but it has "FAX #:" and "# Pages: 3 (including this cover page)".
- Wait, look at the body: "Mike, As promised, here are: -- Approval for AWS... -- Table showing... Talk to you soon! Sue". This is a letter/memo body.
- Is it a fax cover sheet? The rules say: 'A "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", or "TELEFAX MESSAGE NO." header with To/From/company/phone/page-count fields.'
- If it doesn't have the exact header, maybe it's a memo?
- Let's check Check 11: CORRESPONDENCE -> email, memo, or letter.
- memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose. Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo.
- Here we have:
  To: Mike Mozina
  Firm: MSA (external firm? MSA could be an external firm, or internal. Mike Mozina at MSA. Susan Smith at Lorillard. So Mike is external or at a different firm.)
  From: Susan Smith
  Date: 8/31/98
  # Pages: 3 (including this cover page)
- Body: "Mike, As promised, here are: ... Talk to you soon! Sue"
- This has a salutation ("Mike,") and a closing ("Talk to you soon! Sue"). This is a letter, not a memo. Memos don't have salutations or closings.
- Wait, is it a fax cover sheet? If it's a fax cover sheet, it's a form (Check 3). But Check 3 requires a specific header: "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", or "TELEFAX MESSAGE NO.". This page doesn't have that exact header. It just has a box with To/From/FAX#/Pages.
- Let's re-read Check 3: 'A "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", or "TELEFAX MESSAGE NO." header with To/From/company/phone/page-count fields. Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels.'
- If the header isn't there, it's not Check 3.
- Let's look at Check 11: letter. 'letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. "Mr. T. E. Sandefur") with prose and no TO:/FROM: block.'
- Here, recipient is Mike Mozina, Firm: MSA. MSA is likely an external firm (e.g., a consulting firm or agency). Lorillard is the sender. So it's addressed to an external person.
- It has a date (8/31/98), prose body, and closing signature ("Sue").
- So it's a letter.
> Wait, is there any other check?
Check 10: form. Filled or blank fields... But Check 11 says correspondence. If it's a letter, it's letter.
Let's check if it's a memo. "memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose (no external address, no "Dear ..." salutation)." This has "Mike," (salutation) and "Talk to you soon! Sue" (closing). So it's not a memo.
It's addressed to Mike Mozina at MSA. MSA is external to Lorillard. So it's a letter to an external person.
> Let's re-evaluate Check 3. Is this a fax cover sheet?
The box contains:
To: Mike Mozina
Firm: MSA
FAX #: Autodial
From: Susan Smith
FAX #: 335-7733
Phone #: 335-7150
Date: 8/31/98
# Pages: 3 (including this cover page)
This is a classic fax cover sheet layout. But the strict rule for Check 3 says: 'A "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", or "TELEFAX MESSAGE NO." header...'. The header here is "LORILLARD TOBACCO COMPANY / Market Planning and Information Department". It doesn't have the exact string. However, the presence of "FAX #:" and "# Pages: 3 (including this cover page)" strongly indicates it's a fax cover sheet. But if the strict string isn't there, maybe it falls under letter/memo?
Actually, the rule says: 'Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels.'
If this is considered a fax sheet, it would be form. But without the explicit header, maybe it's just a letter sent via fax?
Wait, look at the bottom right: "86220400" (Bates number).
The text says "including this cover page". This implies the top part is a cover page.
If it's a fax cover sheet, it's a form. But does it have the required header? "FACSIMILE TRANSMISSION" etc. It doesn't.
Let's assume it's a letter because it has a salutation and closing, and is addressed to an external person (Firm: MSA).
Wait, "Firm: MSA" means the recipient's firm is MSA. This is typical for a fax cover sheet or a letter to an external party.
Since it has "Mike," and "Talk to you soon! Sue", it's a letter.
> Let's check Check 11 again:
"letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. "Mr. T. E. Sandefur") with prose and no TO:/FROM: block."
Here we have:
- External recipient: Mike Mozina, Firm: MSA
- Date: 8/31/98
- Prose body: "As promised, here are: ..."
- Closing with signature: "Talk to you soon! Sue" (handwritten signature)
This perfectly matches the second condition of letter: "a dated note addressed to a named EXTERNAL person ... with prose and no TO:/FROM: block" (well, it has a To/From block, but the second condition is "OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block" - wait, if it HAS a TO:/FROM: block, does it disqualify it from the second condition? No, the first condition is "letterhead with an external recipient address, date, 'Dear ...' salutation...". This doesn't have a formal letterhead or "Dear ...". It has a To/From box.
Actually, the To/From box is typical of a fax cover sheet or a memo. But the body is a letter.
If it's a fax cover sheet, Check 3 applies. "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header with To/From/company/phone/page-count fields."
Does this page have one of those headers? No. It has "LORILLARD TOBACCO COMPANY".
So Check 3 fails on the strict header requirement.
Therefore, it's not Check 3.
> What about Check 10 (form)?
"A form does NOT have to be blank — a filled form recording data is still a form... internal authorization/approval forms with an approval signature/date block."
This page is a cover letter for a fax. The top part is a fax cover sheet layout, but without the explicit "FAX COVER SHEET" header, it might just be treated as the header of a letter.
The body is a letter. So Check 11 (letter) is the best fit.
> Let's review the memo definition:
"memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose (no external address, no "Dear ..." salutation)."
This has an external address (Firm: MSA) and a salutation ("Mike,") and closing ("Talk to you soon! Sue"). So it's not a memo.
> So it must be a letter.
"letter: ... OR a dated note addressed to a named EXTERNAL person (e.g. "Mr. T. E. Sandefur") with prose and no TO:/FROM: block."
Wait, if it has a TO:/FROM: block, does it fit the first condition? "letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature". It doesn't have a formal letterhead or "Dear ...".
But it is a dated note addressed to a named external person (Mike Mozina at MSA) with prose and a closing signature. The TO:/FROM: block is just a fax cover layout. The function is a letter.
> Let's consider if it's a form (Check 3).
If the system considers any page with "FAX #:" and "# Pages:" as a fax cover sheet, it would be form. But the instructions say: 'A "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", or "TELEFAX MESSAGE NO." header...'. Since the header is missing, I should not force it into Check 3.
Actually, many fax cover sheets in this archive might just have the company name and the box. But the rule is strict: 'A "FACSIMILE"... header with...'. If it's not there, it's not Check 3.
Wait, look at the pre-scan: 'BUT a FAX machine transmission header is NOT a mail-client header: machine-stamped "SENT BY:", a date/time with a phone/fax number, and a page count like "# 4/7" ... is fax transmission metadata added by the sending machine — it does not make the page an email, and you must classify the underlying document by its own content (a faxed memo is a memo; a faxed technical commentary is a scientific_report).'
This implies that if the document itself is a memo or letter, and it's faxed, it's still a memo or letter. The top box here is part of the document's layout (a fax cover sheet layout), but since it lacks the explicit "FAX COVER SHEET" header, we classify the underlying document. The underlying document is a letter to Mike Mozina at MSA.
> Underlying document content:
"Mike,
As promised, here are:
-- Approval for AWS Quarterly Store Count Database to begin 3rd Quarter 1998
-- Table showing significant jump in Convenience Store market importance in 2nd Quarter 1998
Talk to you soon!
Sue"
> This is a letter. It's addressed to an external person (Mike Mozina, MSA), has a date, prose body, and a closing signature.
> Let's double check Check 11:
"letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. "Mr. T. E. Sandefur") with prose and no TO:/FROM: block. A dated note to an internal colleague by name + division, with no salutation and no closing, is a memo (above), not a letter."
Here, Mike Mozina is at "Firm: MSA". MSA is external to Lorillard. So it's an external person.
It has a salutation ("Mike,") and closing ("Talk to you soon! Sue").
So it fits the letter category.
> Is there any financial content? No.
Is there any product documentation? No.
Is there any presentation content? No.
> Therefore, the label is letter.
> Let's quickly review the scratchpad steps:
1. file_folder: no, has body content.
2. handwritten: no, mostly typed.
3. FAX TRANSMISSION SHEET: no explicit "FACSIMILE" or "FAX COVER SHEET" header, just a To/From box. The underlying document is a letter. (Even if considered a fax cover sheet, the strict header rule fails, so we look at underlying content). Wait, if it's a fax cover sheet, it's a form. But without the header, it's not Check 3. The underlying content is a letter.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial: no.
8. specification: no.
9. presentation: no.
10. form: no, it's correspondence.
11. correspondence -> letter: yes. Addressed to external person (Mike Mozina, MSA), has date, prose, closing signature.
12. news_article: no.
13. scientific_report: no.
14. advertisement: no.
> Runner-up: memo. Ruled out because it has an external recipient (Firm: MSA), a salutation ("Mike,"), and a closing signature ("Sue"), which disqualifies it from being a memo (memos have no external address, no salutation, no closing).
Another runner-up: form (fax cover sheet). Ruled out because the page lacks the required explicit header ("FACSIMILE", "FAX COVER SHEET", etc.) for Check 3, and the underlying document is a letter.
> Final label: letter.

---

## handwritten → advertisement (1 errors)

### `rvl_cdip__handwritten__0003.png`
**Expected:** `handwritten` | **Predicted:** `advertisement`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is a handwritten note, but no email headers.
- **Masthead/Running head:** No newspaper masthead or journal running head. There is a "7-ELEVEN" logo and a "CAMEL WINSTON" ad.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: There is a large black bar on the right side (rotated). Wait, the image is rotated 90 degrees counter-clockwise. Let's rotate it mentally.
    *   If I rotate the image 90 degrees clockwise:
        *   Top right: "7-ELEVEN" logo.
        *   Main content: "$3.50 off a carton", "35¢ off a pack", "CAMEL WINSTON". This is an advertisement/coupon.
        *   Bottom part (rotated): Address block "NANCY EVERITT", "2705 SUPERIOR DR", "LIVERMORE CA 94550-6615".
        *   Handwritten note: "Please remove, Addressee is deceased. Died of smoking-related illness on 11/15/96."
        *   There is a "PAID" stamp.
        *   There is a barcode/UPC area.
        *   There is a "P.O. Box 834039 Richardson, TX 75083-4039".
    *   Is this a file folder tab? No. It has a lot of content: an ad, an address, a handwritten note.
    *   Wait, let's look at the layout. The main visual element is the "$3.50 off a carton" ad.
    *   Is it a folder tab? No.
    *   So, not file_folder.
> *   **Check 2: handwritten**
    *   Evidence: There is a handwritten note: "Please remove, Addressee is deceased. Died of smoking-related illness on 11/15/96."
    *   But most of the page is printed text (the ad, the address, the "PAID" stamp, the barcode). The handwriting is a small annotation.
    *   So, not handwritten.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header. No machine-stamped transmission header like "SENT BY: ... # N/N".
    *   Not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No survey questions.
    *   Not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No CV/resume content.
    *   Not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal running head.
    *   Not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: There is a "$3.50 off" and "35 cents off". This is a discount/coupon.
    *   There is a "PAID" stamp.
    *   There is an address block.
    *   This looks like a mailer or a coupon attached to a bill? Or a direct mail piece.
    *   Wait, let's look closer. "P.O. Box 834039 Richardson, TX 75083-4039". "52273 9120". "Change Service Requested". "PAID U.S. POSTAGE".
    *   This is a direct mail piece, specifically a coupon/advertisement.
    *   Is it an invoice? No line items of goods sold.
    *   Is it a budget? No.
    *   Not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: No MDS, no formulation, no "shall/must".
    *   Not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: No slide layout.
    *   Not this check.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: No structured fields for data capture.
    *   Not this check.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: No TO/FROM/RE header. No "Dear ...". No external address block in letter format (the address is part of the mailer return address or recipient address block for mail, not a letter body).
    *   The handwritten note is an annotation on a document.
    *   Not this check.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: No newspaper masthead.
    *   Not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: No running narrative prose about research.
    *   Not this check.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: The dominant content is a large "$3.50 off a carton / 35¢ off a pack" offer for "CAMEL WINSTON" cigarettes. It has the "7-ELEVEN" logo. It has a Surgeon General warning: "WARNING: THE SURGEON GENERAL HAS DETERMINED THAT CIGARETTE SMOKING IS DANGEROUS TO YOUR HEALTH." (Actually, looking closely at the rotated text: "WARNING: THE SURGEON GENERAL HAS DETERMINED THAT CIGARETTE SMOKING IS DANGEROUS TO YOUR HEALTH." is visible in the small print block).
    *   Wait, let's re-read the ad text. "THIS IS NOT A COUPON See other side for details."
    *   It is a promotional coupon/advertisement.
    *   The handwritten note "Please remove, Addressee is deceased..." is an annotation on this ad/mail piece.
    *   The page is dominated by the advertisement layout (7-Eleven logo, Camel Winston offer, Surgeon General warning, barcode, postage paid).
    *   Check 14 says: "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures."
    *   This is a coupon/advertisement.
    *   "Judge by DOMINANT content... a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page..."
    *   Here, the page *is* the ad/coupon (likely a direct mail coupon or a clipping from a mailer). The handwritten note is just a marginal note.
    *   So, advertisement.
> Let's double check.
The image is rotated.
If I rotate it 90 degrees clockwise:
- Top right: 7-Eleven logo.
- Center: "$3.50 off a carton", "35¢ off a pack", "CAMEL WINSTON".
- Bottom right: Address to Nancy Everitt.
- Bottom left: Handwritten note "Please remove, Addressee is deceased. Died of smoking-related illness on 11/15/96."
- Bottom center: "P.O. Box 834039...", "Change Service Requested", "PAID U.S. POSTAGE".
- There is a barcode.
- This is clearly a direct mail advertisement/coupon.
> The dominant content is the advertisement.
Label: advertisement.
> Let's check the checks again.
Check 14: PROMOTIONAL MATERIAL -> advertisement.
Evidence: "$3.50 off a carton", "35¢ off a pack", "CAMEL WINSTON", "7-ELEVEN" logo, Surgeon General warning text ("WARNING: THE SURGEON GENERAL HAS DETERMINED..."), "THIS IS NOT A COUPON". This is a marketing layout/coupon.
> Runner-up: form. Why? Because there is an address block and a "Change Service Requested" block, which looks like mailer data. But the primary function is promotional.
Runner-up: handwritten. Because of the note. But the note is minor.
> Final decision: advertisement.
> Wait, is there any other category?
The handwritten note says "Please remove...". This is a note about the document.
The document itself is an ad/coupon.
> Let's look at the "file_folder" check again.
"A page whose content is a physical folder tab... is file_folder".
This is not a folder tab. It's a scanned page containing an ad and a note.
> Let's look at "invoice".
There is a "PAID" stamp. But it's postage paid ("PAID U.S. POSTAGE NON-PROFIT ORG."). Not a bill for goods.
> So, advertisement.
> One detail: "THIS IS NOT A COUPON See other side for details."
It's an advertisement page.
> Final check of the text:
- "$3.50 off a carton"
- "35¢ off a pack"
- "CAMEL WINSTON"
- "7-ELEVEN"
- "WARNING: THE SURGEON GENERAL HAS DETERMINED THAT CIGARETTE SMOKING IS DANGEROUS TO YOUR HEALTH." (This is the standard warning).
- Address: Nancy Everitt, 2705 Superior Dr, Livermore CA.
- Handwritten: "Please remove, Addressee is deceased. Died of smoking-related illness on 11/15/96."
> The page is an advertisement (specifically a direct mail piece/coupon page).
> Label: advertisement.

---

## scientific_report → handwritten (1 errors)

### `rvl_cdip__scientific_report__0016.png`
**Expected:** `scientific_report` | **Predicted:** `handwritten`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header: None.
- Masthead/running head: None. Just a number "2197" at top right and a vertical number "2505336064" on the right side.
> **Check 1: file_folder**
- Content: There is a lot of handwritten text, a table header, and a table caption at the bottom. Not just an identifier/stamp.
- Not file_folder.
> **Check 2: handwritten**
- Most of the content is freeform handwriting (notes, lists of biological effects like "nose", "larynx", "trachea", "lung", "AHH").
- Wait, is it filling a printed form? There is a printed header "EFFECT", "1 R4F", "UR245-35", "FACTOR" with subheaders "N", "INTER-CEPT", "SLOPE". And a printed caption at the bottom: "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR245-35 ... ENERGY, RACE RATS, 92-DAY INHALATION PERIOD".
- The handwriting is filling in the data for this table, or rather, it's a handwritten list of effects and calculations.
- Let's look closely at the handwriting. It lists "nose Level 1 reserve cell, hyperplasia, squamous metaplasia, Level 2 atrophy", "larynx base of epiglottis...", "trachea...", "lung...".
- Is this a handwritten page? "Most of the content is freeform handwriting... NOT on a printed template."
- Here, there is a printed template at the top (headers) and bottom (table caption). The middle is handwritten.
- Wait, check 2 says: "It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form".
- Is this a form? Or is it a scientific report?
- Let's check check 13: scientific_report. "Running narrative prose with objectives, methods, results, or discussion... Also scientific_report: a hand-plotted experimental GRAPH of test measurements...". This is a handwritten table of data/results.
- Wait, check 10: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... is a form". But this is handwritten.
- Let's re-read check 2: "A log/diary sheet is freeform, not a form... A typed page with only a signature... is not handwritten."
- "Handwriting filling in labeled printed fields is form, not handwritten".
- Here, the top has printed headers: EFFECT, 1 R4F (N, INTER-CEPT, SLOPE), UR245-35 (N, INTER-CEPT, SLOPE), FACTOR.
- The bottom has a printed table caption: "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR245-35 ... ENERGY, RACE RATS, 92-DAY INHALATION PERIOD".
- The middle is handwritten text listing biological effects (nose, larynx, trachea, lung) and some crossed-out text.
- This looks like a handwritten page from a scientific report or a lab notebook page.
- Let's look at check 13: "scientific_report ... Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
- Wait, if it's a hand-plotted graph or table, is it scientific_report? "Also scientific_report: a hand-plotted experimental GRAPH of test measurements (see check 10)". This is a table, not a graph.
- Let's re-evaluate check 2: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
- The page has a printed template at the top and bottom, but the main body is freeform handwriting (notes about biological effects).
- Actually, looking closely, the top headers "EFFECT", "1 R4F", "UR245-35", "FACTOR" are typed. The rest is handwritten.
- Is this a handwritten page? "A typed page with only a signature, stamp, or margin note is not handwritten." Here, the majority is handwritten.
- But check 2 says: "It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form".
- Is this a form? A form captures factual data. This looks like a draft or notes for a table in a scientific report.
- Let's look at the bottom caption: "TABLE DOSE RATIO CALCULATION...". This is a caption for a table that is being drafted or calculated here.
- This is likely a page from a scientific report (a draft or a lab notebook page containing data/results).
- Wait, check 13 says: "scientific_report ... Requires running prose — a page that is only labeled field-value entries ... is a filled form".
- But it also says: "Also scientific_report: a hand-plotted experimental GRAPH of test measurements". What about a handwritten table of results?
- Let's look at the content: it's a list of biological effects (nose, larynx, trachea, lung) with sub-items (reserve cell, hyperplasia, etc.). This is data/results from a toxicology study (inhalation period, rats).
- If it's not a form (because it's not a standard form with fields to capture data, but rather a handwritten draft of a table or notes), and not handwritten (because it's on a printed template with a table caption), what is it?
- Let's re-read check 2: "Most of the content is freeform handwriting... NOT on a printed template." This page HAS a printed template (headers and table caption). So check 2 might not apply if it's considered "filling a printed structured form/table". But it's not really a structured form with cells; it's a typed header and a handwritten list.
- Actually, the typed header has columns: N, INTER-CEPT, SLOPE. The handwritten text is a list of effects. It looks like the author is drafting the rows for the table.
- This is a draft page for a scientific report. The final table would have these rows and the numerical values.
- Since it's a draft of a scientific table/graph, it belongs to a scientific_report.
- Let's check check 13 again: "scientific_report ... Also scientific_report: a hand-plotted experimental GRAPH of test measurements... and a technical-study title page...".
- What about a handwritten data table? "A standalone labeled data chart or table ... is a form (check 10)". But this is handwritten and looks like a draft.
- Wait, is there a better fit?
- Let's look at the labels: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
- If it's a handwritten page with some typed headers, check 2 says "Most of the content is freeform handwriting... NOT on a printed template." Here, the template is minimal (just headers and a caption). The bulk is freeform handwriting (notes, lists).
- "Handwriting filling in labeled printed fields is form, not handwritten — but the labeled printed structure has to actually be visible; don't infer a form just because the content resembles form-type data".
- Here, the printed structure is just column headers at the top and a caption at the bottom. The middle is freeform handwriting. This might be classified as `handwritten` if the template is considered negligible, or `scientific_report` if it's considered a draft of a scientific document.
- Let's look at the example: "A log/diary sheet is freeform, not a form: a minimal sheet with only ONE typed column header... and blank ruled lines, filled with running narrative entries by hand... is handwritten".
- Here, we have typed headers at the top and a caption at the bottom. The middle is handwritten.
- Actually, this looks like a page from a scientific report where the author has handwritten the data or notes.
- Let's consider `scientific_report`. "Running narrative prose with objectives, methods, results, or discussion...". This page has results (biological effects, dose ratio calculation).
- But check 13 says: "Requires running prose — a page that is only labeled field-value entries (even an 'ANALYTICAL DATA SUMMARY' under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
- This page is not running prose. It's a list and a table draft.
- Is it a `form`? "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A standalone labeled data chart or table... is a form".
- The bottom says "TABLE DOSE RATIO CALCULATION...". The top has table headers. The middle is the data (handwritten). This is a handwritten table/chart.
- Check 10: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... is a form".
- But check 10 also says: "It does NOT cover money records... It does NOT cover product-change authorization pages...".
- And check 2 says: "It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form".
- So if this is a handwritten table filling a printed template, it's a `form`.
- Wait, is it a `scientific_report`? "Also scientific_report: a hand-plotted experimental GRAPH of test measurements (see check 10)". This is a table, not a graph.
- Let's look at the content again. It's a list of pathological effects (nose, larynx, trachea, lung) and some calculations. This is clearly from a toxicology study.
- If it's a draft page, it might be part of a `scientific_report`. But the page itself is just a handwritten table/notes.
- Let's reconsider `handwritten`. "Most of the content is freeform handwriting... NOT on a printed template." The printed template here is just the top headers and bottom caption. The main body is freeform. "A typed page with only a signature, stamp, or margin note is not handwritten." Here, the main body IS handwriting.
- "Handwriting filling in labeled printed fields is form, not handwritten — but the labeled printed structure has to actually be visible". The labeled printed structure (N, INTER-CEPT, SLOPE) is visible at the top. The handwriting is below it, but not really filling cells; it's a list.
- Actually, the handwriting is listing the rows that would go into the table. "nose Level 1 reserve cell...". These are the row labels. The columns (N, INTER-CEPT, SLOPE) are empty.
- So this is a draft of a table.
- In the tobacco archive, such pages are often classified as `scientific_report` if they are part of a study, or `form` if they are data capture sheets.
- But check 13 says scientific_report requires running prose. "Requires running prose — a page that is only labeled field-value entries ... is a filled form".
- This page has no running prose. It's a list and a table draft.
- So it's either `form` or `handwritten`.
- Let's look at check 2 again: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
- This is a draft (notes for a table). The printed template is minimal.
- "A log/diary sheet is freeform, not a form: a minimal sheet with only ONE typed column header... and blank ruled lines, filled with running narrative entries by hand... is handwritten".
- Here, we have typed headers at the top and a caption at the bottom. The content is handwritten notes/drafts.
- I will lean towards `handwritten` because the majority is freeform handwriting and it's a draft/notes page, not a structured form with visible cells being filled. The printed headers are just column titles for a table that isn't fully drawn.
- Wait, the bottom caption is "TABLE DOSE RATIO CALCULATION...". This is a printed caption.
- Let's look at the vertical text "2505336064". This is a Bates number.
- Top right "2197". Page number.
- This looks like a page from a lab notebook or a draft manuscript page.
- If it's a draft manuscript page, it's `scientific_report`. But check 13 says "Requires running prose".
- What about `form`? "A standalone labeled data chart or table... is a form". This is a labeled data chart (table) that is handwritten.
- Check 10: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... is a form".
- The bottom says "TABLE ...". The top has headers. The middle is the data (handwritten). This fits "standalone labeled data chart or table".
- So `form` is a strong candidate.
- But check 2 says: "It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form".
- So if it's a handwritten table, it's `form`.
- Let's check if there's any other category. `scientific_report`? No running prose.
- Let's re-read check 13: "Also scientific_report: a hand-plotted experimental GRAPH of test measurements (see check 10)". This is a table, not a graph.
- So it's likely `form` or `handwritten`.
- The page has a lot of handwritten text (the list of effects). The printed part is just the table headers and caption.
- "Most of the content is freeform handwriting... NOT on a printed template."
- Is this on a printed template? The template is the table structure (headers + caption). The handwriting is filling the rows.
- "Handwriting filling in labeled printed fields is form, not handwritten". The rows are the fields. The handwriting is listing the row labels.
- I'll go with `handwritten` because the text is freeform notes/drafts (listing effects, crossing things out) rather than filling structured cells with data values. The table columns (N, INTER-CEPT, SLOPE) are empty. The author is drafting the content.
- Wait, if the columns are empty, it's not a filled form. It's a draft.
- "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
- The template is present (headers, caption), but the content is freeform notes.
- Let's look at the example: "A handwritten note about a questionnaire... is questionnaire".
- Here, it's a handwritten draft of a scientific table.
- If I have to choose between `handwritten` and `scientific_report`: `scientific_report` requires running prose. This doesn't have it. `form` requires capturing factual data. This is a draft, not capturing data yet (columns are empty).
- So `handwritten` seems best. "Most of the content is freeform handwriting... (notes, letters, memos, drafts)". This is a draft.
> Let's refine:
- Check 1: file_folder - no.
- Check 2: handwritten - yes, majority is freeform handwriting (notes/drafts listing biological effects), not filling a structured form (columns are empty). The printed headers/caption are minimal.
- Check 3-14: no.
> Wait, is there any chance it's `scientific_report`?
- "Also scientific_report: a hand-plotted experimental GRAPH of test measurements". This is a table, not a graph.
- "Requires running prose". No running prose.
> Is there any chance it's `form`?
- "A standalone labeled data chart or table... is a form".
- But the data isn't captured (columns empty). It's a draft.
- Check 2 says drafts are handwritten. "Most of the content is freeform handwriting (notes, letters, memos, drafts)".
> I will go with `handwritten`.
> Wait, let's look at the bottom caption again: "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR245-35 ... ENERGY, RACE RATS, 92-DAY INHALATION PERIOD".
This is a caption for a table. The top has the table headers. The middle is the handwritten content.
This is a handwritten table.
Check 2: "It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form".
If this is considered a "printed structured table" (headers + caption define the table), and the handwriting is filling it (even if just the row labels), then it's `form`.
But the columns are empty. The handwriting is a list of items to be put in the rows.
"Handwriting filling in labeled printed fields is form, not handwritten — but the labeled printed structure has to actually be visible; don't infer a form just because the content resembles form-type data".
The labeled printed structure (N, INTER-CEPT, SLOPE) is visible. The content (nose, larynx, etc.) resembles form-type data (row labels for a table).
So this might be `form`.
> Let's reconsider `scientific_report`.
- In many tobacco archive datasets, handwritten lab notes or draft data tables are classified as `scientific_report` if they are part of a study, or `handwritten` if they are freeform.
- But the instructions say: "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
- This page is only labeled field-value entries (draft). So it's not `scientific_report`.
- So it's either `form` or `handwritten`.
- "A log/diary sheet is freeform, not a form: a minimal sheet with only ONE typed column header... and blank ruled lines, filled with running narrative entries by hand... is handwritten".
- Here, we have typed headers at the top (multiple columns) and a caption at the bottom. The middle is handwritten.
- The content is a list of biological effects. This is data for a table.
- I'll classify as `handwritten` because it's a draft/notes page, not a filled form. The form (table) is not filled (columns empty). The handwriting is freeform notes listing the rows.
> Actually, looking at the handwriting, it's a list of effects with some crossed out. "nose Level 1 reserve cell, hyperplasia, squamous metaplasia...". This is a draft list.
"Most of the content is freeform handwriting (notes, letters, memos, drafts)". This is a draft.
So `handwritten`.
> Final check:
- Check 1: file_folder - no.
- Check 2: handwritten - yes.
- Runner-up: form, ruled out because the columns are empty and the content is freeform draft notes, not filling structured fields.
> Wait, is there a `specification`? No.
`presentation`? No.
> I'll go with `handwritten`.

---

## news_article → form (1 errors)

### `rvl_cdip__news_article__0008.png`
**Expected:** `news_article` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** I see "HILL AND KNOWLTON", "Press Clipping", "Subject", "Publication: Oriental Daily News", "Date: March 4, 1987", "Circulation: 650,000", "Client: Tobacco Institute of Hong Kong Limited". This looks like a press clipping cover sheet, not an email. No "From/To/Sent/Subject" in the email sense (though there is a "Subject" field, it's part of a clipping service header). Wait, let's look closer. "HILL AND KNOWLTON International Public Relations Counsel". "Press Clipping". "Subject Publication: Oriental Daily News". "Date: March 4, 1987". "Circulation: 650,000". "Client: Tobacco Institute of Hong Kong Limited". This is a press clipping report.
- **Masthead/Running head:** There is a clipping of Chinese text (vertical text). There is a Bates number "2501454254" and page number "30". No journal masthead. No newspaper masthead on this page itself (the clipping is from "Oriental Daily News", but this page is a summary/report *about* the clipping).
> **2. Scratchpad checks:**
> *   **Check 1: file_folder.**
    *   Evidence: There is a lot of text. "In a 'passive smoking' seminar held yesterday...". Not just an ID.
    *   Result: not this check.
> *   **Check 2: handwritten.**
    *   Evidence: Text is typed. There is a Chinese clipping image. No majority handwriting.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET.**
    *   Evidence: No "FACSIMILE" header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire.**
    *   Evidence: Not a survey.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume.**
    *   Evidence: Not a resume.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication.**
    *   Evidence: No journal running head. The text mentions "Oriental Daily News" but this is a press clipping summary.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget.**
    *   Evidence: No financial table. "Circulation: 650,000" is a metric, not money.
    *   Result: not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification.**
    *   Evidence: No product specs.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation.**
    *   Evidence: "HILL AND KNOWLTON ... Press Clipping". This is a report. Wait, let's look at the content. It's a summary of a press clipping.
    *   Is it a presentation? No.
    *   Is it a news article? The content is about a news article ("Oriental Daily News").
    *   Let's check Check 12.
> *   **Check 10: ADMINISTRATIVE FORM -> form.**
    *   Evidence: There are fields like "Subject", "Publication", "Date", "Circulation", "Client". It looks like a cover sheet for a press clipping. Is it a form?
    *   "Press Clipping" is the title.
    *   It has fields: Subject, Publication, Date, Circulation, Client.
    *   But the main content is the text below: "In a 'passive smoking' seminar held yesterday...".
    *   Wait, the text below is the content of the clipping or a summary? "In a 'passive smoking' seminar held yesterday, Mr Steve Kroos... called for rational debate...". This looks like a summary of the clipping or the text of the clipping itself.
    *   Actually, looking closely at the layout: Top part is the header "HILL AND KNOWLTON... Press Clipping". Then a box with Chinese text (the clipping). Then a paragraph of English text summarizing it.
    *   This is a press clipping report.
    *   Is it a form? Check 10 says "Filled or blank fields... for capturing factual data". This is a report *about* a clipping.
    *   Let's look at the categories again.
    *   advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter.**
    *   Evidence: No "To/From/Date/Subject" memo header in the standard sense. It has "Subject", "Date", "Client". But it's a "Press Clipping" report from a PR firm (Hill and Knowlton) to a client (Tobacco Institute of Hong Kong).
    *   Is it a memo? "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". This has "Subject", "Date", "Client". But it's a press clipping summary.
    *   Is it a letter? No external address, no "Dear...".
    *   Is it an email? No mail-client header.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article.**
    *   Evidence: The page contains a summary of a news article from "Oriental Daily News". The text "In a 'passive smoking' seminar..." is a summary/report of an event.
    *   Wait, is the page *itself* a news article? No, it's a press clipping summary from a PR agency.
    *   However, let's look at the content. It describes a seminar.
    *   Is it a scientific_report? "Running narrative prose with objectives, methods, results...". No.
    *   Is it a memo? A PR firm sending a clipping to a client is often a memo or a report.
    *   Let's re-read the checks.
    *   Check 11: memo. "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". The header here is "Subject: Publication: Oriental Daily News", "Date: March 4, 1987", "Client: Tobacco Institute...". This looks like a cover sheet for a press clipping service.
    *   The text below is the content.
    *   Is there a better category?
    *   Let's look at "news_article". "Newspaper or magazine masthead...". The clipping is from "Oriental Daily News". But this page is a Hill and Knowlton document.
    *   Let's look at "scientific_report". No.
    *   Let's look at "form". The top part is a form-like header. But the bottom is text.
    *   Let's look at "presentation". No.
> Let's reconsider the document type. This is a "Press Clipping" report. Hill and Knowlton is a PR firm. They send press clippings to clients.
The document has a header:
HILL AND KNOWLTON
International Public Relations Counsel
Press Clipping
Subject: Publication: Oriental Daily News
Date: March 4, 1987
Circulation: 650,000
Client: Tobacco Institute of Hong Kong Limited
> Then a Chinese text clipping (vertical).
Then a summary paragraph: "In a 'passive smoking' seminar held yesterday, Mr Steve Kroos... called for rational debate...".
> This looks like a **memo** or a **report**.
Wait, check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
This document has "Subject", "Date", "Client". It doesn't have "To" or "From" explicitly labeled, but "Client: Tobacco Institute..." implies the recipient. "Hill and Knowlton" is the sender.
The prose follows.
Is it a memo?
Or is it a **news_article**?
The text describes a news event. But the page is a PR summary.
Actually, look at the text content. It's a summary of a seminar.
Is it a **scientific_report**? No.
> Let's look at the labels again.
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> Could it be **news_article**?
Check 12: "Newspaper or magazine masthead...". The clipping is from a newspaper. But the page itself is a Hill and Knowlton document.
However, sometimes press clippings are classified as news articles if the content is the news. But here the content is a summary.
> Let's look at **memo** again.
"A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo".
Here: "Client: Tobacco Institute of Hong Kong Limited". This is an external client.
So it's not internal.
"letter: letterhead with an external recipient address...". There is no address, just "Client: ...".
> What about **form**?
Check 10: "Filled or blank fields...". The top part is a form header. But the main content is the clipping and summary.
Actually, press clipping reports are often just reports.
> Let's look at **scientific_report**.
Check 13: "Running narrative prose...". The text is narrative. "In a 'passive smoking' seminar...". But it's not a research write-up.
> Let's look at the pre-scan instructions again.
"A mail-client header block... If present, the page is email". Not present.
"A masthead or running head...". No.
> Let's look at the content again.
The text is: "In a 'passive smoking' seminar held yesterday, Mr Steve Kroos, Chairman of the Tobacco Institute of Hong Kong, called for rational debate on the issue that smoking is hazardous to health. He said that discussion by the public on the issue has apparently became sensational and politicalized. Two US scholars pointed out that, although a number of researchs have been conducted throughout the world, no association between passive smoking and health hazards has been established."
> This is a summary of a press clipping.
The document is a "Press Clipping" from Hill and Knowlton.
Is this a **memo**?
Often, PR firms send memos or reports.
If it's a report to a client, it might be a letter or memo.
But the header is "Press Clipping".
> Let's look at **news_article** (Check 12).
"Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content".
This page presents as a PR summary of a news clipping. The dominant content is the summary text and the clipping image.
The clipping is from "Oriental Daily News".
Is the page itself a news article? No.
> Is it a **scientific_report**?
No.
> Is it a **form**?
The top block is a form: Subject, Publication, Date, Circulation, Client.
But the content is text.
Check 10: "A form does NOT have to be blank... This also covers: a standalone labeled data chart or table...".
This is not a chart.
> Let's reconsider **memo**.
Check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
This has "Subject", "Date". It lacks "To", "From", "RE".
But it has "Client".
And "Hill and Knowlton" (Sender) and "Tobacco Institute" (Client/Recipient).
The prose follows.
Is it a memo?
"A dated internal note addressed to a named person... IS a memo". This is addressed to a client (external).
"letter: letterhead with an external recipient address...". No address.
> Maybe it's a **letter**?
"letterhead with an external recipient address, date, 'Dear ...' salutation...". No salutation.
> What about **presentation**?
Check 9: "Slide/overhead layouts...". No.
> What about **file_folder**?
No.
> Let's look at the labels again.
Maybe **news_article**?
The text is about a news event. The clipping is a news article.
But the page is a summary.
> Wait, look at the bottom right: "2501454254" (Bates number) and "30".
This is page 30 of a document.
The document is likely a press clipping report.
> Let's look at the "Press Clipping" header.
It's a cover sheet for a press clipping.
Is a press clipping report a **memo**?
In many tobacco archives, PR reports are memos or reports.
If I have to choose, **memo** seems closest if we consider the header structure (Subject, Date, Client/To).
But "Client" is not "To".
> Let's look at **scientific_report** again.
Check 13: "Running narrative prose with objectives, methods, results, or discussion".
This text has none of that. It's a news summary.
> Let's look at **form** again.
Check 10: "administrative form".
The top part is a form. "Press Clipping" with fields.
But the content is the clipping.
Actually, press clipping services produce a document that is essentially a form filled with the clipping.
But the text below is a summary.
> Let's look at the example worked examples.
Example 1: Questionnaire.
Example 2: scientific_report.
Example 3: scientific_publication.
Example 4: invoice.
> There is no example for press clippings.
> Let's analyze the text "In a 'passive smoking' seminar...".
This is a summary of the clipping.
The clipping is the Chinese text.
The English text is the summary/translation.
> This document is a **press clipping report**.
Which category fits best?
- **news_article**: The content is news. But the layout is a PR summary. Check 12 says "Judge by DOMINANT content... news_article requires the page to present primarily as editorial/multi-story news content". This page presents as a PR summary (Hill and Knowlton header). So not news_article.
- **memo**: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block". This has Subject, Date. It's a business communication. Hill and Knowlton to Tobacco Institute. It's a report/memo.
- **letter**: External recipient. But no "Dear" or address.
- **form**: The top is a form.
> Let's look at the "Client: Tobacco Institute of Hong Kong Limited".
This is a business document.
Hill and Knowlton is a PR firm.
They send press clippings.
This is likely a **memo** or a **report**. Since "report" isn't a label (only scientific_report), maybe **memo**?
Or **letter**?
"A dated note addressed to a named EXTERNAL person... is a letter."
Here the recipient is "Tobacco Institute of Hong Kong Limited" (an organization).
And there is no salutation.
> Let's look at **scientific_report**.
Sometimes internal reports are classified as scientific_report if they have narrative prose.
But this is PR.
> Let's look at **advertisement**.
No.
> Let's look at **email**.
No mail header.
> Let's look at **file_folder**.
No.
> Let's look at **presentation**.
No.
> Is it possible this is a **news_article**?
The text is from a newspaper (Oriental Daily News).
The page contains the newspaper text (in Chinese) and an English summary.
Check 12: "Also a magazine feature or an encyclopedia entry/excerpt... or any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet".
This page presents as a Hill and Knowlton document, not the newspaper. The newspaper is the source.
> So it's a document *about* a news article.
It's a **memo** (business communication) or **form** (press clipping form).
> Let's look at Check 10 (Form) again.
"Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
The top part has fields: Subject, Publication, Date, Circulation, Client.
The content is the clipping.
Is a press clipping sheet a form?
"an application... a records-management inventory... a QA/parameter review sheet".
A press clipping cover sheet with fields for Publication, Date, Circulation, Client... it captures data about the clipping.
But the main content is the clipping and summary.
> Let's look at Check 11 (Correspondence) again.
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
This has "Subject", "Date".
"Client" acts as "To".
"Hill and Knowlton" acts as "From".
The prose is "In a 'passive smoking' seminar...".
This fits the memo structure loosely (Header + Prose).
But it's not internal. "Client" implies external.
"letter: letterhead with an external recipient address...".
Hill and Knowlton is the letterhead.
"Tobacco Institute..." is the recipient.
But no address, no "Dear", no closing.
> Maybe it's a **memo** because it's a business note?
"A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo".
This is addressed to a company.
> Let's consider **scientific_report**.
Check 13: "Running narrative prose...".
The text is narrative.
But it's not research.
> Let's consider the source. Tobacco industry archive.
Hill and Knowlton is a PR firm.
They monitor press.
This is a press monitoring report.
Press monitoring reports are often memos or reports.
If I have to choose from the 16 labels...
**memo** seems the most plausible business document type.
Or **form** (press clipping form).
> Let's look at the "Press Clipping" title.
It's a title.
The fields are metadata.
The content is the clipping.
> Actually, look at the text layout.
Top: Header info.
Middle: Image of Chinese text (vertical).
Bottom: English summary text.
Bottom right: Bates number and page number "30".
> This looks like a page from a larger report (page 30).
The report is a press clipping compilation.
The page itself is a summary of one clipping.
> If this is page 30 of a report, and the report is a press clipping summary...
Is the page a **news_article**? No.
Is it a **scientific_report**? No.
> Let's look at **memo** again.
In the tobacco archive, many documents are memos.
This looks like a memo from Hill and Knowlton to the client.
Header: Subject, Date, Client.
Body: Summary.
This fits the "memo" pattern: Header block + prose.
Even though it's external, memos can be external (though usually letters).
But the instructions say: "memo: internal...". "letter: external...".
"A dated note addressed to a named EXTERNAL person... is a letter."
Here the recipient is "Tobacco Institute of Hong Kong Limited".
So it should be a **letter**?
But there is no "Dear" or closing.
"letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature".
This lacks address, salutation, closing.
> What about **form**?
Check 10: "administrative form".
The top part is a form.
But the content is text.
> Let's look at **news_article** (Check 12) again.
"Newspaper or magazine masthead...".
The clipping has Chinese text.
The header says "Publication: Oriental Daily News".
Maybe the page is considered a **news_article** because it contains the news content?
No, the instructions say: "Judge each page by its FUNCTION".
Function: PR summary of a press clipping.
> Let's look at **scientific_report** (Check 13).
"Running narrative prose...".
The text is narrative.
But it's not scientific research.
> Is there a category I missed?
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> Could it be **email**?
No mail header.
> Could it be **presentation**?
No.
> Let's go back to **memo**.
"A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo".
Here: "Client: Tobacco Institute of Hong Kong Limited". This is an external entity.
So it's not internal.
So it's not a memo by this strict definition.
> "A dated note addressed to a named EXTERNAL person... is a letter."
"Tobacco Institute" is an organization, not a person.
But "Mr Steve Kroos, Chairman..." is mentioned in the text.
> What about **form**?
Check 10: "Filled or blank fields...".
The top part is a form.
"Press Clipping" with fields.
Maybe the whole page is a form?
"an application... a records-management inventory...".
A press clipping sheet is a form used to record clipping details.
But the content is the clipping.
> Let's look at the "Press Clipping" header again.
It's a standard PR report format.
Hill and Knowlton press clipping reports.
These are often bound into books.
This is page 30.
The page function is to present a press clipping and a summary.
> If I have to classify this...
It's not a news article (it's a summary).
It's not a scientific report.
It's not a form (it's a report page).
It's not a memo (external, no standard header).
It's not a letter (no salutation/closing).
> Wait, look at Check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
This has "Subject", "Date".
"Client" is like "To".
"Hill and Knowlton" is like "From".
The prose follows.
Even if it's external, the structure is memo-like.
But the label says "internal".
> What about **letter**?
"letterhead with an external recipient address...".
Hill and Knowlton is the letterhead.
"Tobacco Institute..." is the recipient.
Maybe it's a **letter**?
But no "Dear" or closing.
> Let's look at **news_article** again.
Check 12: "any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet".
This page does not present as the newspaper. It presents as Hill and Knowlton.
> Is it possible this is a **scientific_report**?
Sometimes PR reports are classified as scientific_report if they have narrative prose? No, that's wrong.
> Let's look at the content: "In a 'passive smoking' seminar...".
This is a news summary.
> Maybe **form**?
Check 10: "administrative form".
The page has a structured header (Subject, Publication, Date, Circulation, Client).
This is a form for recording press clippings.
The content (clipping + summary) fills the form.
"A form does NOT have to be blank — a filled form recording data is still a form".
The data recorded is the clipping and the summary.
The fields capture: Publication, Date, Circulation, Client.
This fits "form" (Check 10).
"Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
The top part has these fields.
The rest is the content captured.
Like a "Press Clipping Report Form".
> Let's check the examples.
Worked example 4: invoice.
Worked example 1: questionnaire.
> If I classify as **form**:
Evidence: Header fields "Subject", "Publication", "Date", "Circulation", "Client" capturing data about the press clipping. The page is a structured record of a press clipping.
Runner-up: memo, ruled out because it lacks standard TO/FROM/RE header and is a structured report form, not internal prose.
Runner-up: news_article, ruled out because the page is a PR summary form, not the original newspaper content (though it contains a clipping).
> Actually, let's look at the text "Press Clipping".
It's a title.
The fields are metadata.
The content is the clipping.
In many archives, press clippings are just filed as news articles or forms.
But here, the page is a Hill and Knowlton document.
Hill and Knowlton documents are often memos or reports.
> Let's look at **memo** again.
"A dated internal note... IS a memo".
This is not internal.
> Let's look at **letter**.
"letterhead with an external recipient address...".
No address.
> I'm leaning towards **form** or **memo**.
The header "HILL AND KNOWLTON... Press Clipping" with fields "Subject", "Publication", "Date", "Circulation", "Client" is a form header.
The content is the data.
Check 10: "administrative form... Filled or blank fields... for capturing factual data".
This page captures data about a press clipping (Publication, Date, Circulation, Client, and the clipping itself).
So **form** is a strong candidate.
> Wait, is there a **news_article** possibility?
The text is a summary of a news article.
The clipping is a news article.
But the page is a summary.
Check 12: "Judge by DOMINANT content... news_article requires the page to present primarily as editorial/multi-story news content".
This page presents as a PR summary (Hill and Knowlton header).
So not news_article.
> Is there a **scientific_report** possibility?
No.
> So **form** seems best.
The page is a "Press Clipping" form/report.
It has fields: Subject, Publication, Date, Circulation, Client.
It captures factual data (the clipping details).
> Let's check Check 10 again.
"This also covers: a standalone labeled data chart or table... a filled analytical or lab data sheet... internal authorization/approval forms".
A press clipping summary sheet is a form.
> One more check: **email**.
No.
> One more check: **file_folder**.
No.
> Final decision: **form**.
The page is a structured document (form) from a PR firm recording a press clipping.
Header fields: Subject, Publication, Date, Circulation, Client.
Content: Clipping image and summary text.
Function: To record and present a press clipping (capturing data about the publication, date, circulation, and content).
> Wait, the text "In a 'passive smoking' seminar..." is narrative prose.
Check 13: "scientific_report... Requires running prose".
But this is not scientific.
Check 11: "memo... followed directly by memo-style prose".
The prose is not memo-style (it's a news summary).
> I will go with **form**.
The top block is clearly a form header.
"Subject: Publication: Oriental Daily News"
"Date: March 4, 1987"
"Circulation: 650,000"
"Client: Tobacco Institute of Hong Kong Limited"
These are form fields.
The page is a filled form (press clipping report).
> Wait, look at the label list: "form".
Check 10: "ADMINISTRATIVE FORM -> form".
Yes.
> One counter-argument: The page is page 30 of a report. The report is a press clipping compilation. Each page is a clipping summary.
Is a page in a report a form?
If the page is a template filled with data, yes.
The header is a template. The content is the data.
So **form**.
> Another possibility: **news_article**.
The content is news.
But the function is PR summary.
The instructions say: "Judge each page by its FUNCTION".
Function: PR summary/record of a clipping.
This is an administrative record -> **form**.
> Let's refine the scratchpad.
- file_folder: no, has content.
- handwritten: no, typed.
- fax: no.
- questionnaire: no.
- resume: no.
- scientific_publication: no journal head.
- financial: no.
- specification: no.
- presentation: no.
- form: yes, header fields (Subject, Publication, Date, Circulation, Client) capturing data about a press clipping. The page is a structured record (form) from Hill and Knowlton.
- correspondence: no standard memo/letter structure (no To/From/RE, no salutation/closing, external client).
- news_article: no, it's a PR summary, not the original newspaper content (though it contains a clipping). The dominant layout is the PR header.
- scientific_report: no, not research.
- advertisement: no.
> Runner-up: memo. Ruled out because it lacks standard TO/FROM/RE header and is addressed to an external client (Tobacco Institute) with a PR summary, not internal memo prose. Also, the structured fields (Subject, Publication, Date, Circulation) make it a form/report.
Runner-up: news_article. Ruled out because the page is a Hill and Knowlton PR summary document, not the original Oriental Daily News editorial content. The masthead is not present on this page (only mentioned in fields).
> Actually, is it a **letter**?
"letterhead with an external recipient address...".
Hill and Knowlton is the letterhead.
"Tobacco Institute..." is the recipient.
But no address, no salutation.
So not a letter.
> I'll stick with **form**.
The page is a "Press Clipping" form.
> Wait, looking closely at the text:
"Subject Publication: Oriental Daily News" -> Subject field value is "Publication: Oriental Daily News"? Or Subject is blank, Publication is Oriental Daily News?
"Subject" is a label. "Publication: Oriental Daily News" is the value?
Actually, it looks like:
Subject [blank or implied]
Publication: Oriental Daily News
Date: March 4, 1987
Circulation: 650,000
Client: Tobacco Institute of Hong Kong Limited
> This is a form header.
> Final label: form.
> One detail: "A page whose primary structure is a memo header + prose... stays memo".
Here the structure is "Press Clipping" header + fields + clipping image + summary prose.
The primary structure is the form header + content.
So **form**.
> Wait, is there any chance it's **scientific_report**?
No.
> Is there any chance it's **presentation**?
No.
> I will output **form**.
> Re-evaluating **news_article**.
Check 12: "Also a magazine feature or an encyclopedia entry/excerpt... or any page that presents as published periodical editorial content".
This page does not present as the periodical. It presents as Hill and Knowlton.
> Re-evaluating **memo**.
Check 11: "memo: internal...". This is external.
> So **form** is the best fit.
The page is a form used by a PR firm to log press clippings.
> One final check: Could it be **email**?
No "From/To/Sent/Subject" mail header. "Subject" is present but it's "Subject Publication:..." which is a field label, not a mail header. Mail header is "Subject: ...". Here it's "Subject" then next line "Publication: ...". Actually, "Subject" is a label, and "Publication: Oriental Daily News" is on the next line?
Looking at the image:
"Subject" is on the right.
"Publication: Oriental Daily News" is below it.
"Date: March 4, 1987"
"Circulation: 650,000"
"Client: Tobacco Institute of Hong Kong Limited"
This is a form layout.
> Final decision: **form**.

---

## news_article → advertisement (1 errors)

### `rvl_cdip__news_article__0018.png`
**Expected:** `news_article` | **Predicted:** `advertisement`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** "JUN 24 '94 10:53AM PHILIP MORRIS P. 6/9". This looks like a FAX machine transmission header ("SENT BY:", date/time, page count). Wait, let's look closer. "JUN 24 '94 10:53AM PHILIP MORRIS P. 6/9". This is a fax header. It is NOT a mail-client header (From/To/Sent/Subject). So not email.
- **Masthead/Running head:** There is a title "HOW SCIENCE AND POLITICS COLLIDED AND BALANCED REPORTING WAS THE CASUALTY." There is a footer "IN ANY CONTROVERSY, FACTS MUST MATTER." with a logo (looks like a scale of justice or similar, maybe a company logo). There is a Bates number "2501355879". There is text at the bottom: "From day one, serious questions have been raised about the validity of the EPA's 1992 report on secondhand smoke... For a free reprint of this article, or more information, please call 1 800 823-2325." This looks like a reprint of an article or a press release/advertisement. Wait, let's look at the layout. It has a headline, columns of text, pull quotes ("When someone cites a 'pattern' or 'trend in the data', it's time to look more closely."), and a footer with a slogan. It looks like a newspaper clipping or a magazine article, or perhaps a press release/advertisement.
- Let's look at the text content. "How Science and Politics Collided and Balanced Reporting Was The Casualty." "The press confidently played up the EPA's side of the story." "Stories about the EPA's report 'exaggerated evidence and minimized childhood'." "The complicated presentation of the EPA's report discouraged scrutiny."
- Bottom text: "From day one, serious questions have been raised about the validity of the EPA's 1992 report on secondhand smoke... This week, Philip Morris is bringing you this article in its entirety at a four-page spread. Since the EPA's report has been the basis for a flurry of smoking restrictions, we believe it's important for both smokers and non-smokers to learn their facts in order to make up their own minds. After all, private press does not encourage earlier documentation and stronger evidence to more strongly repudiate and outright deny. For a free reprint of this article, or more information, please call 1 800 823-2325."
- Logo at bottom: "PHILIP MORRIS COMPANIES" (hard to read, but looks like a corporate logo). "IN ANY CONTROVERSY, FACTS MUST MATTER."
- This is a full-page advertisement or a press release disguised as an article. Wait, let's check the categories.
- Categories: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder.** No, there is a lot of body content (headline, columns of text).
*   **Check 2: handwritten.** No, it's typed text.
*   **Check 3: FAX TRANSMISSION SHEET.** No, the fax header is just metadata at the top ("JUN 24 '94..."), not a fax cover sheet form.
*   **Check 4: questionnaire.** No.
*   **Check 5: resume.** No.
*   **Check 6: scientific_publication.** No journal running head. The text mentions "EPA's 1992 report", "Am J Epidemiol" maybe? No, it's an article about the EPA report.
*   **Check 7: financial document.** No.
*   **Check 8: specification.** No.
*   **Check 9: presentation.** No, it's a multi-column article layout. Wait, is it a speech? No. Is it a slide? No.
*   **Check 10: form.** No.
*   **Check 11: correspondence.** No TO/FROM/RE header. No salutation.
*   **Check 12: news_article.** "Newspaper or magazine masthead, byline, dateline, multi-column news typography...". This page has multi-column typography. It looks like a newspaper clipping or a magazine article. The text says "Philip Morris is bringing you this article in its entirety at a four-page spread." This suggests it's a reprint of an article, possibly from a newspaper or magazine, placed as an advertisement or a press release.
    - Let's look at Check 14: advertisement. "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures. Judge by DOMINANT content... a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page... news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
    - The bottom text says: "For a free reprint of this article, or more information, please call 1 800 823-2325." and "IN ANY CONTROVERSY, FACTS MUST MATTER." with the Philip Morris logo. This is clearly an advertisement by Philip Morris. It's a "public service announcement" style ad or a full-page ad presenting an article to argue against the EPA report. The text "Philip Morris is bringing you this article..." is a huge giveaway. It's an ad.
    - Let's re-read Check 12 vs Check 14.
    - Check 12: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement (check 14) even when printed inside a newspaper/magazine... news_article requires the page to present primarily as editorial/multi-story news content".
    - This page presents a single article ("How Science and Politics Collided...") but the footer is a clear advertisement for Philip Morris ("For a free reprint... please call...", "IN ANY CONTROVERSY, FACTS MUST MATTER."). The text at the bottom explicitly says "Philip Morris is bringing you this article...". This is an advertisement. It's a "paid advertisement" or "op-ed" style ad.
    - Wait, is it a news_article? The content is an article. But the page itself is an advertisement *containing* an article. The prompt says: "Judge by DOMINANT content... a single brand ad... is advertisement... news_article requires the page to present primarily as editorial/multi-story news content". This page is a single article, but it's framed as a Philip Morris ad ("Philip Morris is bringing you this article...").
    - Let's look at the layout. It has a headline, columns, pull quotes. It looks like a newspaper page. But the bottom banner "IN ANY CONTROVERSY, FACTS MUST MATTER." and the call to action "For a free reprint... please call..." makes it an advertisement.
    - Actually, let's look at the text again. "From day one, serious questions have been raised... This week, Philip Morris is bringing you this article in its entirety at a four-page spread." This is the text of the ad. The article itself is the content of the ad.
    - So it's an advertisement.
> Let's check the labels again.
- advertisement: Marketing layout, slogans, brand styling. "IN ANY CONTROVERSY, FACTS MUST MATTER." is a slogan. "Philip Morris" branding. Call to action.
- news_article: Editorial content. This is editorial content *within* an ad.
> Let's look at the pre-scan instructions: "A page whose DOMINANT layout is a single brand advertisement (product imagery, slogans, a Surgeon General warning, brand styling) is an advertisement (check 14) even when printed inside a newspaper/magazine with a running masthead and some surrounding text; news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
> This page is a single promotional layout (an article presented by Philip Morris). The bottom text is the ad copy. "For a free reprint of this article... please call...". This is definitely an advertisement.
> Wait, is there a Surgeon General warning? I don't see one clearly, but there is a logo. The text is pro-smoking (arguing against EPA report on secondhand smoke). This is classic tobacco industry advertising (public relations campaign).
> So, Check 14: advertisement.
> Let's double check Check 12 (news_article).
- "Newspaper or magazine masthead..." - There is no masthead visible at the top. Just the fax header.
- "multi-column news typography" - Yes, there are columns.
- "- more -" continuation - No.
- "wire-service credit" - No.
- "magazine feature or encyclopedia entry" - No.
- "general-audience outlet" - The text is from Philip Morris.
> The text at the bottom: "From day one, serious questions have been raised about the validity of the EPA's 1992 report on secondhand smoke. But only barely have they begun to be the subject of serious investigation. This week, Philip Morris is bringing you this article in its entirety at a four-page spread. Since the EPA's report has been the basis for a flurry of smoking restrictions, we believe it's important for both smokers and non-smokers to learn their facts in order to make up their own minds. After all, private press does not encourage earlier documentation and stronger evidence to more strongly repudiate and outright deny. For a free reprint of this article, or more information, please call 1 800 823-2325."
> This is the ad copy. The page is an advertisement.
> Let's check the fax header again. "JUN 24 '94 10:53AM PHILIP MORRIS P. 6/9". This is a fax header. It doesn't make it an email or memo.
> So the classification is advertisement.
> Let's review the checks in order.
1. file_folder: No, lots of text.
2. handwritten: No.
3. FAX TRANSMISSION SHEET: No, just a header line.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: No journal ID.
7. financial: No.
8. specification: No.
9. presentation: No.
10. form: No.
11. correspondence: No.
12. news_article: It has multi-column text, but the bottom text reveals it's a Philip Morris ad bringing an article. "Judge by DOMINANT content... news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout." This is a promotional layout (an ad).
13. scientific_report: No.
14. advertisement: Yes. "Marketing layout... brand styling... 'IN ANY CONTROVERSY, FACTS MUST MATTER.'... 'For a free reprint... please call'". The page is an advertisement by Philip Morris.
> Wait, is it a "news_article" because it's an article?
The instructions say: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content".
This page is a single article, but it's clearly an ad. The text at the bottom is the key. "Philip Morris is bringing you this article...". It's a paid advertisement.
> Let's look at the "worked example" logic.
- If it's an ad inside a newspaper, it's advertisement.
- This page looks like a page from a newspaper/magazine (multi-column), but the footer is a full-page ad footer. Actually, the whole page looks like a reprint of an article *as* an advertisement.
- The text "In Any Controversy, Facts Must Matter" is a slogan.
- The logo is Philip Morris.
> So, advertisement.
> One detail: "A page whose dominant layout is a single brand advertisement (product imagery, slogans, a Surgeon General warning, brand styling) is an advertisement (check 14) even when printed inside a newspaper/magazine with a running masthead and some surrounding text; news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
> This page is a promotional layout. It promotes Philip Morris's view on the EPA report.
> Final decision: advertisement.
> Wait, let's look at the top right. "SECONDHAND SMOKE FACTS FINALLY EMERGE". This is a headline within the article or a subhead.
The main headline is "HOW SCIENCE AND POLITICS COLLIDED AND BALANCED REPORTING WAS THE CASUALTY."
> The text at the bottom is the ad copy.
"For a free reprint of this article, or more information, please call 1 800 823-2325."
"2501355879" is a Bates number.
> The document is an advertisement.
> Let's check if it could be a "news_article".
If I classify it as news_article, I ignore the ad copy at the bottom.
The instructions say: "Judge by DOMINANT content... news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
This is a single promotional layout (an article presented as an ad). So it's advertisement.
> Let's check "presentation".
- "speech text" - No.
- "deck cover" - No.
> Let's check "scientific_report".
- No running prose of a study. It's an article about politics and science.
> So, advertisement.
> One more check: Is it a "memo"?
- Fax header: "JUN 24 '94 10:53AM PHILIP MORRIS P. 6/9". Not a memo header.
> Is it a "letter"?
- No salutation.
> So, advertisement.
> Wait, looking closely at the bottom text: "After all, private press does not encourage earlier documentation and stronger evidence to more strongly repudiate and outright deny." - This is slightly garbled text, likely OCR or bad printing, but the meaning is clear: it's an ad.
> The label is `advertisement`.
> Let's re-read the scratchpad procedure.
- Check 1: file_folder. No.
- Check 2: handwritten. No.
- Check 3: FAX. No (just header).
- Check 4: questionnaire. No.
- Check 5: resume. No.
- Check 6: scientific_publication. No.
- Check 7: financial. No.
- Check 8: specification. No.
- Check 9: presentation. No.
- Check 10: form. No.
- Check 11: correspondence. No.
- Check 12: news_article. Multi-column text, but bottom text is ad copy ("Philip Morris is bringing you this article", "call 1 800..."). Not primarily editorial/multi-story news content, it's a single promotional layout.
- Check 13: scientific_report. No.
- Check 14: advertisement. Yes. Slogan "IN ANY CONTROVERSY, FACTS MUST MATTER.", brand styling (Philip Morris logo), call to action.
> Runner-up: news_article. Ruled out because the page contains explicit advertising copy ("Philip Morris is bringing you this article", "For a free reprint... please call") and a brand slogan/logo at the bottom, making it a promotional layout (advertisement) rather than primary editorial news content.
> Final label: advertisement.

---

## presentation → memo (1 errors)

### `rvl_cdip__presentation__0013.png`
**Expected:** `presentation` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** I see "DLG", "XJNT", "First draft for April 29. Please add.", "Lance". No "From:", "To:", "Sent:", "Subject:". No fax transmission header like "SENT BY: ... # N/N". Wait, there is a Bates number "526001380" rotated on the right side.
- **Masthead/Running head:** No newspaper masthead, no journal running head.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: There is a Bates number "526001380". There is some text: "DLG", "XJNT", "First draft for April 29. Please add.", "Lance".
    *   Is it just an identifier? No, there is text "First draft for April 29. Please add." and a name "Lance". This looks like a note.
    *   Is it a folder tab? No, it's a full page with text.
    *   Wait, let's look closer. The text is sparse. "First draft for April 29. Please add." "Lance". Handwritten "DLG", "XJNT".
    *   Is it a file folder? No, it has content (a note).
> *   **Check 2: handwritten**
    *   Evidence: "DLG", "XJNT" (handwritten). "First draft for April 29. Please add." (typed). "Lance" (typed).
    *   Is *most* of the content freeform handwriting? No. The main text is typed: "First draft for April 29. Please add." and "Lance". The handwriting is just initials/annotations.
    *   Wait, let's re-read the definition. "Most of the content is freeform handwriting... NOT on a printed template."
    *   Here, the typed text is "First draft for April 29. Please add." and "Lance". This looks like a memo or a note.
    *   Let's check the handwritten rule: "A typed page with only a signature, stamp, or margin note is not handwritten." This fits. It's a typed note with some handwritten initials.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header. No fax cover sheet fields.
> *   **Check 4: SURVEY INSTRUMENT**
    *   Evidence: No questions, no rating scales.
> *   **Check 5: resume**
    *   Evidence: No career history.
> *   **Check 6: scientific_publication**
    *   Evidence: No journal header.
> *   **Check 7: financial document**
    *   Evidence: No money.
> *   **Check 8: specification**
    *   Evidence: No product data.
> *   **Check 9: presentation**
    *   Evidence: Sparse text. "First draft for April 29. Please add." "Lance".
    *   Is it a slide deck cover? Or a section divider?
    *   "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation".
    *   "First draft for April 29. Please add." sounds like a note.
    *   Wait, look at the layout. It's very sparse.
    *   Let's look at Check 11: Correspondence.
> *   **Check 10: administrative form**
    *   Evidence: No fields, boxes, checkboxes.
> *   **Check 11: CORRESPONDENCE (email, memo, or letter)**
    *   **Email:** No mail-client header.
    *   **Memo:** Internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block? No.
    *   "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels".
    *   Here we have: "First draft for April 29. Please add." (prose/note). "Lance" (name). Handwritten "DLG", "XJNT".
    *   "Lance" is likely the recipient or sender. "DLG" and "XJNT" look like initials (D.L. G..., X.J.N.T.?).
    *   Actually, "Lance" is typed in the middle. "First draft for April 29. Please add." is typed.
    *   This looks like a memo or a note.
    *   Let's look at the memo definition: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". This doesn't have that block.
    *   "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo". Here we have "Lance" (name). "First draft for April 29. Please add." (prose). Handwritten initials "DLG" (maybe sender?), "XJNT" (maybe initials?).
    *   Wait, is "Lance" the recipient? "First draft for April 29. Please add." addressed to Lance?
    *   Or is "Lance" the sender?
    *   Let's look at the structure. It's a typed note on a mostly blank page.
    *   Is it a letter? No external address, no "Dear...", no closing signature.
    *   Is it a memo? "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo".
    *   The text is "First draft for April 29. Please add." and "Lance".
    *   This fits the description of a memo (internal note).
> *   **Check 12: news_article**
    *   Evidence: No masthead.
> *   **Check 13: scientific_report**
    *   Evidence: No running prose, no objectives/methods.
> *   **Check 14: advertisement**
    *   Evidence: No marketing layout.
> Let's reconsider **Check 1: file_folder**.
- "Almost no body content: only an archive/Bates number, a stamp, a short label or ID... No sentences, no topical title."
- Here we have a sentence: "First draft for April 29. Please add."
- So not file_folder.
> Let's reconsider **Check 2: handwritten**.
- "Most of the content is freeform handwriting... NOT on a printed template."
- The content is mostly blank space, with a few typed lines and some handwritten initials.
- "A typed page with only a signature, stamp, or margin note is not handwritten."
- This is a typed note with margin notes. So not handwritten.
> Let's reconsider **Check 9: presentation**.
- "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note (e.g. 'Internal Communication 2000 Plan' with 'Draft for discussion'), a single-word/short-phrase heading with no subtitle at all (e.g. 'RECOMMENDATIONS' centered on an otherwise blank page), a deck cover, or a section divider — is a presentation".
- The text is "First draft for April 29. Please add." and "Lance".
- This doesn't look like a title page or section divider. It looks like a note.
> Let's look at **Check 11: memo** again.
- "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels".
- Here: "Lance" (named person). "First draft for April 29. Please add." (memo-style prose / note). Handwritten "DLG" (likely initials of sender, e.g., D. L. G...). "XJNT" (maybe initials?).
- This fits the "internal note" definition of a memo perfectly. It's a short internal communication.
> Wait, is there any other category?
- "email": No mail header.
- "letter": No external address, no salutation, no closing.
> So it's a **memo**.
> Let's check the evidence for memo:
- Typed text: "First draft for April 29. Please add."
- Name: "Lance".
- Handwritten initials: "DLG", "XJNT".
- Bates number: 526001380.
- This is an internal note/memo.
> Let's check if it could be **handwritten**.
- "Most of the content is freeform handwriting". No, it's mostly blank with typed text.
> Let's check if it could be **file_folder**.
- "No sentences". There is a sentence "First draft for April 29. Please add." So not file_folder.
> Let's check **presentation**.
- "A near-blank cover... with only a bold headline title...". "First draft for April 29. Please add." is not really a headline title. It's a note. "Lance" is a name.
- However, sometimes sparse pages are presentations. But the text "First draft for April 29. Please add." is clearly a transmittal note or memo text.
> Let's look at the handwritten text "DLG" and "XJNT".
- DLG could be initials. XJNT could be initials.
- "First draft for April 29. Please add."
- "Lance"
- This is a memo from DLG to Lance (or vice versa).
> Final decision: **memo**.
> Wait, let's look at the "scratchpad procedure" requirements.
- Walk checks 1-14 in order.
- Check 1: file_folder. Evidence: Bates number 526001380, text "First draft for April 29. Please add.", "Lance", handwritten "DLG", "XJNT". Not file_folder because there is a sentence/note content. -> not this check.
- Check 2: handwritten. Evidence: Handwritten "DLG", "XJNT". Typed "First draft...", "Lance". Not majority handwritten. -> not this check.
- Check 3: fax. No fax header. -> not this check.
- Check 4: questionnaire. No questions. -> not this check.
- Check 5: resume. No. -> not this check.
- Check 6: scientific_publication. No journal header. -> not this check.
- Check 7: financial. No money. -> not this check.
- Check 8: specification. No. -> not this check.
- Check 9: presentation. Sparse text. But text is a note "First draft...". Not a title or slide. -> not this check. (Though it's close to a near-blank page, the content is a memo note).
- Check 10: form. No fields. -> not this check.
- Check 11: correspondence.
    - email: No mail header.
    - memo: "A dated internal note addressed to a named person... with memo-style prose... IS a memo". Here we have "Lance" (name), "First draft for April 29. Please add." (prose/note), handwritten initials (DLG). This fits the memo definition (internal note without full header block).
    - letter: No external address, no salutation.
    - So **memo**.
> Runner-up: file_folder (ruled out because there is a sentence "First draft for April 29. Please add." and a name "Lance", so it has real content, not just an identifier). Or handwritten (ruled out because most content is typed/blank, not freeform handwriting).
> Actually, looking very closely at the image:
- Top center: handwritten "DLG", "XJNT".
- Typed: "First draft for April 29. Please add."
- Typed: "Lance" (centered).
- Right side, rotated: "526001380".
- Bottom: some black bars (scan artifacts or folder edges?). The bottom has black bars. "Scan-artifact signal: a solid black bar along one edge... points to a photographed slide... presentation".
- Wait. The bottom has black bars. "A solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
- Let's re-evaluate Check 9.
- "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center (e.g., lower-right) rather than in running paragraphs, points to a photographed slide/overhead — presentation — even if the sparse text sounds like a research title; don't let a technical-sounding phrase pull this toward scientific_report when the layout itself is sparse and slide-like rather than a prose page."
- BUT: "BUT this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1)".
- Is this a file folder tab? No, it's a full page with text.
- Is it a slide? The text is "First draft for April 29. Please add." and "Lance". This doesn't look like a slide title. It looks like a memo note.
- However, the layout is extremely sparse.
- Let's look at the memo definition again. "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". This page lacks that block.
- "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo even without literal 'TO:/FROM:' labels".
- Here we have "Lance" and "First draft...". This is a memo.
> Let's look at the black bars at the bottom.
- "A page whose content is a physical folder tab, a short filing label... and a Bates number is file_folder even though the folder body photographs as a solid black bar".
- The bottom has black bars. The right side has the Bates number rotated.
- Is this a folder tab page?
- "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body."
- The label here is "First draft for April 29. Please add." and "Lance". This is not a short filing label like "NEWTROL" or "Litigation Content". It's a sentence.
- So it's not a folder tab.
> So it's a memo. The black bars might just be scan artifacts or the bottom of the page.
Actually, looking at the bottom, there are black shapes. "126001380" is rotated.
The text "First draft for April 29. Please add." and "Lance" is a memo.
> Let's refine the memo evidence.
- Text: "First draft for April 29. Please add."
- Name: "Lance".
- Handwritten initials: "DLG", "XJNT".
- This is an internal note/memo.
> Final check: Is it **handwritten**?
- "Most of the content is freeform handwriting". No.
- "A typed page with only a signature, stamp, or margin note is not handwritten." Yes, this fits. The main content is typed "First draft..." and "Lance". The handwriting is just initials/margin note.
> So **memo** is the correct label.
> One detail: "First draft for April 29. Please add."
This is a note.
"Lance" is the recipient.
"DLG" is the sender (initials).
This is a memo.
> Label: memo.

---

## questionnaire → scientific_report (1 errors)

### `rvl_cdip__questionnaire__0003.png`
**Expected:** `questionnaire` | **Predicted:** `scientific_report`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: No newspaper/magazine masthead. No journal running head/volume/issue/page number on this specific page (just a page number "1" at the bottom and a Bates number "2023226545" rotated on the right).
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a title "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS (PHYSICAL DEPENDENCE)" and a full paragraph of text starting with "Q: Dr. Henningfield...". It has a page number "1" and a Bates number.
    *   Result: Not file_folder. It has real content (text, title).
> *   **Check 2: handwritten**
    *   Evidence: The text is typed. There is no significant handwriting.
    *   Result: Not handwritten.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header or fax transmission metadata like "SENT BY:".
    *   Result: Not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: The title is "QUESTIONS FOR DeNOBLE...". The text starts with "Q: Dr. Henningfield...". This looks like a set of questions for a deposition or testimony (Dr. Henningfield, Surgeon General, Subcommittee). It's a list of questions for a person (DeNoble) to answer or questions *about* their findings. Wait, let's look closer. "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS". The text is a question "Q: ... Isn't it true that...". This is a question for a deposition or hearing. Is it a questionnaire? A questionnaire asks the reader to answer. This is a question *for* someone else (DeNoble) to answer, likely in a legal context (Subcommittee, testified). It's not a survey instrument for consumers. It's a legal document / deposition questions. Let's look at other categories.
> *   **Check 5: resume**
    *   Evidence: No career history.
    *   Result: Not resume.
> *   **Check 6: scientific_publication**
    *   Evidence: No journal name, volume, issue, page range (other than page "1"), DOI. The Bates number is present.
    *   Result: Not scientific_publication.
> *   **Check 7: financial document**
    *   Evidence: No financial data.
    *   Result: Not financial.
> *   **Check 8: specification**
    *   Evidence: No material safety data, product formulation, "shall/must".
    *   Result: Not specification.
> *   **Check 9: presentation**
    *   Evidence: Not a slide deck. Not a press release. Not a speech text.
    *   Result: Not presentation.
> *   **Check 10: administrative form**
    *   Evidence: No fields, boxes, checkboxes. It's a paragraph of text.
    *   Result: Not form.
> *   **Check 11: correspondence -> email, memo, or letter**
    *   Evidence: No "From/To/Sent/Subject". No "TO:/FROM:/RE:". No letterhead with external address. No "Dear...".
    *   Result: Not correspondence.
> *   **Check 12: news_article**
    *   Evidence: No masthead, byline, dateline, multi-column typography.
    *   Result: Not news_article.
> *   **Check 13: scientific_report**
    *   Evidence: "Running narrative prose with objectives, methods, results, or discussion". This page is a single question "Q: ...". It's not a report. Wait, is it a scientific commentary? "Comments to Y.-P. Sun et al."? No.
    *   Let's re-evaluate. The text is: "Q: Dr. Henningfield and the Surgeon General have testified before this Subcommittee that nicotine use creates a physical dependence... Isn't it true that your experiments at Philip Morris... found that nicotine use does not create a physical dependence?"
    *   This is a question for a deposition or a hearing transcript. It's a legal document.
    *   Wait, look at the labels again.
    *   advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
    *   None of these fit perfectly? Let's look closer.
    *   Is it a "questionnaire"? Check 4: "The page asks the reader to answer, rate, choose, or commit... A page does not have to show questions to be a questionnaire...". But this is a question *for* a witness (DeNoble) in a legal context (Subcommittee). It's not a survey.
    *   Is it a "scientific_report"? Check 13: "Running narrative prose...". This is just one question.
    *   Is it a "form"? Check 10: "Filled or blank fields...". No.
    *   Is it a "memo"? No.
    *   Is it a "letter"? No.
> Let's re-read the checks carefully.
Maybe I missed something.
Title: "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS (PHYSICAL DEPENDENCE)".
Text: "Q: Dr. Henningfield... Isn't it true that...?"
This is a page from a legal document, likely a deposition transcript or a set of questions for a witness.
In the tobacco archive, these are often part of litigation documents.
> Let's look at the labels again.
16 categories.
If nothing matches, choose the label whose defining evidence is closest.
> Wait, is it a **questionnaire**?
Check 4: "The page asks the reader to answer...". This page asks a question. But it's a legal question.
"Also counts: instructions or directions given to product-test/consumer-test participants..."
"A cover/transmittal letter keeps its full letter formatting... and is STILL questionnaire... if its prose mentions enclosing... a survey/questionnaire".
This doesn't fit questionnaire well.
> Is it a **scientific_report**?
Check 13: "A scientific commentary/critique with running argument about a study's data and conclusions... is a research write-up".
This is a question *about* a study's data ("your experiments found that..."). It's a legal question challenging scientific findings.
Maybe it's part of a larger document classified as scientific_report? But I only have this page.
The page has running text (a paragraph). It discusses scientific findings (nicotine, physical dependence).
But it's formatted as "Q: ...".
> Let's look at **form** (Check 10).
"A standalone labeled data chart or table...". No.
"internal authorization/approval forms". No.
> Let's look at **presentation** (Check 9).
"Slide/overhead layouts...". No.
> Let's look at **file_folder** (Check 1).
"Almost no body content...". No, there is a paragraph.
> Let's reconsider **questionnaire**.
"The page asks the reader to answer..."
This page asks a question. But it's a legal deposition question.
In the tobacco archive, there are often documents like "Questions for Deposition".
Is there a category for legal documents? No.
The categories are: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> Could it be **scientific_report**?
Check 13: "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript...; a lab or technical study title page...".
This page is a single question. It's not a report.
> Could it be **memo**?
Check 11: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block...". No.
> Could it be **letter**?
Check 11: "letterhead with an external recipient address...". No.
> Let's look at the text again.
"QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS (PHYSICAL DEPENDENCE)"
This looks like a section header in a legal document or a deposition outline.
The text is a question.
> Is there a catch?
"Judge each page by its FUNCTION... a page full of technical data can still be a form... but a bill is a bill even when it is printed on a form."
"Do not rush to the label that matches the page's subject matter — deliberate through the checks below... commit to the FIRST one with strong, concrete evidence".
> Let's look at **questionnaire** again.
Check 4: "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey."
"A page does not have to show questions to be a questionnaire: an appendix page, section cover, transmittal note, or page-numbered part of a survey instrument..."
This page is titled "QUESTIONS FOR...". It is a list of questions.
Is it a survey instrument? No, it's for a legal deposition.
However, in these classification tasks, sometimes "questionnaire" is used broadly for any page with questions? No, the instructions are specific: "survey instrument".
> What about **scientific_report**?
Check 13: "A scientific commentary/critique with running argument about a study's data and conclusions (e.g. 'Comments to Y.-P. Sun et al.' analyzing whether the data support the authors' conclusion) is a research write-up, not an email or letter."
This page is a question *critiquing* or *challenging* the data/conclusions ("Isn't it true that your experiments... found that nicotine use does not create a physical dependence?").
It is a commentary/critique of scientific findings.
It has running prose (the question is a paragraph of prose).
It discusses scientific ability, experiments, nicotine use.
It fits the "scientific commentary/critique" description in Check 13.
"Comments to Y.-P. Sun et al." is an example. This is "Questions for DeNoble" challenging his findings.
So **scientific_report** seems the best fit among the options, as it's a document related to scientific findings and critique, even if formatted as a legal question.
> Wait, let's look at **form** again.
No.
> Let's look at **presentation**.
No.
> Let's look at **news_article**.
No.
> Let's reconsider the **questionnaire** check.
"The page asks the reader to answer..."
This page asks a question. But the "reader" is Dr. Henningfield/DeNoble in a legal setting.
Usually, questionnaires are for consumers or employees.
> Let's look at the label **scientific_report** again.
Check 13: "Running narrative prose with objectives, methods, results, or discussion...".
This page has a paragraph of text. It is a question, but it's a long, complex question discussing methods ("experiments to determine whether..."), results ("found that nicotine use does not create..."), and scientific ability ("conducted to the best of your scientific ability").
It is a critique/commentary on scientific work.
The example "Comments to Y.-P. Sun et al." is a scientific commentary. This "Questions for DeNoble" is a legal question based on scientific commentary.
Given the limited labels, **scientific_report** is the most plausible if we consider it a document discussing scientific findings (even if it's a legal question about them).
> Wait, is there another category?
What about **form**?
Check 10: "A QA/parameter review sheet...". No.
> Let's look at the structure.
Title: QUESTIONS FOR DeNOBLE...
Text: Q: [Paragraph]
Page number: 1
Bates number: 2023226545
> This is a page from a deposition or a set of questions for a deposition.
In the tobacco archive, these are often classified.
If I have to choose, **scientific_report** fits the content (science, experiments, nicotine) and the format (prose, commentary/critique of science).
Or is it **questionnaire**?
"The page asks the reader to answer..."
Technically, it asks a question. But it's not a survey.
> Let's look at the "Calibration" section.
"form, scientific_report, and handwritten are historically the most over-predicted labels... news_article and presentation are historically under-predicted."
This suggests I should be careful with scientific_report.
> Let's re-read Check 13 carefully.
"A scientific commentary/critique with running argument about a study's data and conclusions (e.g. 'Comments to Y.-P. Sun et al.' analyzing whether the data support the authors' conclusion) is a research write-up, not an email or letter."
This page is a question *analyzing* whether the data support the authors' conclusion (or rather, challenging it). "Isn't it true that your experiments... found that nicotine use does not create a physical dependence?"
It is a critique of the scientific findings.
So **scientific_report** is a strong candidate.
> Let's check if it could be a **memo**.
No header.
> Let's check if it could be a **letter**.
No salutation/closing.
> Let's check if it could be a **form**.
No fields.
> Let's check if it could be a **presentation**.
No slide layout.
> So it's between **questionnaire** and **scientific_report**.
Questionnaire: "The page asks the reader to answer...". This page asks a question. But it's a legal question. The instructions say "survey instrument". This is not a survey instrument.
Scientific_report: "Running narrative prose... scientific commentary/critique...". This page is a paragraph of text critiquing scientific findings.
> I will go with **scientific_report**.
> Wait, let's look at the title again: "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS".
This sounds like a document *about* DeNoble's findings.
The text is a question *to* someone (likely a lawyer asking DeNoble, or DeNoble's questions?).
"Dr. Henningfield and the Surgeon General have testified... Isn't it true that your experiments..."
This is a question *to* DeNoble (or Henningfield) about their experiments.
It is a legal document.
In the absence of a "legal_document" category, and given the content is about scientific experiments and findings, **scientific_report** is the closest, especially under the "commentary/critique" umbrella.
> However, let's look at **questionnaire** again.
Is it possible this is classified as a questionnaire because it's a list of questions?
Check 4: "The page asks the reader to answer...".
If the page is a list of questions for a witness, is it a questionnaire?
Usually, no. A questionnaire is a survey.
But the instructions say: "commit to the FIRST one with strong, concrete evidence".
Evidence for questionnaire: The page is titled "QUESTIONS FOR..." and contains a question "Q: ...".
Evidence for scientific_report: The content is about scientific experiments, nicotine, physical dependence, scientific ability. It's a critique of scientific findings.
> Let's look at the example worked out 1: "QUESTIONNAIRE" titled page with questions -> questionnaire.
Here the title is "QUESTIONS FOR DeNOBLE...".
But the content is a legal deposition question.
In tobacco archives, deposition questions are common.
If I have to classify a deposition question page...
Maybe it's **scientific_report** because it's part of the scientific record/litigation about science?
> Let's look at the "Calibration" note: "scientific_report... are historically the most over-predicted labels".
This means I should be careful not to call everything scientific_report.
If this is a legal document (deposition question), and there's no legal category, what is it?
Maybe **form**? No.
Maybe **file_folder**? No.
> Let's reconsider **questionnaire**.
Check 4: "The page asks the reader to answer...".
This page asks a question.
"A page does not have to show questions to be a questionnaire: an appendix page, section cover, transmittal note, or page-numbered part of a survey instrument".
This is a page-numbered part (page 1) of a document titled "QUESTIONS FOR...".
Is "Questions for DeNoble" a survey instrument? No.
> What about **memo**?
No.
> Let's look at the text content again.
"Dr. Henningfield and the Surgeon General have testified before this Subcommittee..."
This is a legal/historical context (Subcommittee, likely the 1994 Congressional hearings on tobacco).
The document is a set of questions for a witness (DeNoble) at these hearings.
This is a legal document / hearing transcript excerpt.
None of the labels fit perfectly.
"Choose the label whose defining evidence is closest to what you can actually read".
> Closest label:
- **scientific_report**: Content is scientific (nicotine, experiments, physical dependence). Format is prose (a long question). Function is commentary/critique of science (challenging the findings).
- **questionnaire**: Format is a question ("Q: ..."). Title has "QUESTIONS". But function is legal, not survey.
> The instructions say: "Judge each page by its FUNCTION, not its subject matter".
Function: Asking a question in a legal hearing.
Subject matter: Science (nicotine).
> If function is "asking a question", does that map to **questionnaire**?
Check 4: "The page asks the reader to answer, rate, choose, or commit...".
Here, the page asks Dr. Henningfield/DeNoble to answer.
"Isn't it true that...?" -> The reader (witness) is expected to answer "Yes" or "No".
So functionally, it asks the reader to answer.
But is it a "survey instrument"? No.
Check 4 says: "The page asks the reader to answer... opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey."
It doesn't explicitly say "legal deposition questions".
But "open-response lines" -> the witness answers.
> However, the "Calibration" says "questionnaire... is historically under-predicted" (wait, "news_article and presentation are historically under-predicted"). "form, scientific_report, and handwritten are historically the most over-predicted".
This implies I should avoid scientific_report and questionnaire if not sure.
> Let's look at **scientific_report** again.
Check 13: "A scientific commentary/critique with running argument about a study's data and conclusions... is a research write-up".
This page is a question, not a "running argument". It's a single question.
But it contains a critique: "Isn't it true that your experiments... found that nicotine use does not create a physical dependence?" (implying they did, and the testimony says they didn't, or vice versa).
Actually, the text says: "They have testified that such physical dependence is important because it shows that nicotine use is addicting. It is my understanding that while you were at Philip Morris you did experiments to determine whether nicotine use created a physical dependence and that your experiments found that nicotine use does not create a physical dependence. Isn't it true that your experiments... found that nicotine use does not create a physical dependence?"
This is a legal question setting up a contradiction or confirming a fact.
It is not a "running narrative prose with objectives, methods, results, or discussion". It's a single question paragraph.
> So **scientific_report** is weak on format (requires running prose, usually a report).
> What about **form**?
Check 10: "Filled or blank fields...". No.
> What about **presentation**?
Check 9: "Slide/overhead layouts...". No.
> What about **news_article**?
Check 12: "Newspaper or magazine masthead...". No.
> This is a tough one. It's a legal document page.
Let's look at the labels again.
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> Could it be **email**?
No mail header.
> Could it be **letter**?
No.
> Could it be **memo**?
No.
> Let's reconsider **questionnaire**.
Title: "QUESTIONS FOR DeNOBLE..."
Content: "Q: ..."
This is literally a page of questions.
In a broad sense, a questionnaire is a set of questions.
Check 4: "The page asks the reader to answer...".
This page asks the reader (the witness) to answer.
Even though it's a legal context, the *function* of the page is to ask a question for an answer.
The label "questionnaire" might be the intended catch-all for "pages with questions" if no better fit exists, but the instructions say "survey instrument".
However, "A page does not have to show questions to be a questionnaire...".
Wait, "The page asks the reader to answer...".
If I have to choose, **questionnaire** fits the "asks to answer" function, even if the context is legal.
BUT, the instructions say "survey instrument or its transmittal". This is not a survey.
> Let's look at **scientific_report** again.
"Requires running prose — a page that is only labeled field-value entries... is a filled form... not a scientific report."
This page has running prose (the question is a paragraph).
"A scientific commentary/critique... is a research write-up".
This is a critique of scientific findings (DeNoble's experiments).
So **scientific_report** fits the "commentary/critique" function.
> Let's compare **questionnaire** vs **scientific_report**.
- Questionnaire: Title has "QUESTIONS", text has "Q:". Function: asking for an answer. Context: Legal (not survey).
- Scientific_report: Content: scientific experiments, nicotine. Function: commentary/critique of science. Format: prose paragraph. Context: Legal hearing about science.
> The instructions say: "Judge each page by its FUNCTION, not its subject matter".
Subject matter: Science (nicotine).
Function: Asking a legal question / Critiquing scientific findings.
> If function is "critiquing scientific findings", it's **scientific_report**.
If function is "asking questions", it's **questionnaire**.
> In the tobacco archive, documents like "Questions for Deposition" are often part of the litigation files.
If I look at similar documents in this dataset (tobacco archive), deposition questions are often classified as **scientific_report** if they discuss scientific findings, or **form** if they are structured, or **letter/memo** if they are correspondence.
Actually, a page with a single question "Q: ..." is often part of a transcript.
If this is a standalone page...
> Let's look at the "Calibration" again.
"form, scientific_report, and handwritten are historically the most over-predicted labels".
This suggests I should be very careful.
If I predict scientific_report, I might be over-predicting.
If I predict questionnaire, I might be under-predicting (since it's under-predicted historically).
> Let's look for evidence for **questionnaire**.
"The page asks the reader to answer..." -> Yes, "Isn't it true that...?"
"open-response lines" -> The witness would answer verbally or in writing.
But it's not a survey.
> Let's look for evidence for **scientific_report**.
"Running narrative prose" -> Yes, a paragraph.
"scientific commentary/critique" -> Yes, challenging the findings of experiments.
"analysis whether the data support the authors' conclusion" -> Yes, "Isn't it true that your experiments... found that...".
> I think **scientific_report** is the best fit because the content is a substantive discussion/critique of scientific data (even if framed as a legal question), and it has running prose. A simple "questionnaire" label is usually reserved for surveys. The "commentary/critique" bullet in Check 13 is a specific catch for documents analyzing scientific data, which this does.
> Wait, is there any other label?
**specification**? No.
**invoice**? No.
> Let's assume **scientific_report**.
Evidence: The page contains a paragraph of text discussing scientific experiments ("experiments to determine whether nicotine use created a physical dependence"), scientific ability ("best of your scientific ability"), and challenging conclusions ("found that nicotine use does not create a physical dependence"). This fits the "scientific commentary/critique with running argument about a study's data and conclusions" description in Check 13. The title "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS" indicates it's related to scientific findings.
> Runner-up: **questionnaire**. Ruled out because although it contains a question ("Q:"), it is a legal deposition question challenging scientific findings, not a survey instrument or consumer test questionnaire (Check 4 requires a survey instrument context, whereas this is legal commentary/critique of science).
> Wait, let's look at the title again. "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS".
This might be a document *by* DeNoble? Or *for* DeNoble?
"Questions for DeNoble" -> Questions directed at DeNoble.
"Findings and Advice to Superiors" -> Maybe the title of the section or the document DeNoble is responding to?
Actually, it looks like a header for a section in a legal document.
> Let's go with **scientific_report**.
> One more check: **form**.
Check 10: "A standalone labeled data chart or table...". No.
"internal authorization/approval forms". No.
> Final decision: **scientific_report**.
The page is a text block discussing scientific experiments and findings, functioning as a critique/commentary (even if it's a legal question). It has running prose. It is not a survey (questionnaire), not a financial doc, not a form.
> Wait, looking at the example worked out 1: "QUESTIONNAIRE" -> questionnaire.
Here the title is "QUESTIONS FOR...".
If the model is strict, "Questions" -> questionnaire.
But the instructions say "Judge each page by its FUNCTION... do not rush to the label that matches the page's subject matter".
Subject matter: Questions. Function: Legal critique of science.
So **scientific_report** is better.
> Also, Check 13 says: "A scientific commentary/critique with running argument about a study's data and conclusions... is a research write-up".
This page is a question that contains a critique: "It is my understanding that... your experiments found that... Isn't it true that...". This is setting up an argument/critique.
> I will output **scientific_report**.
> One detail: "A page that is only labeled field-value entries... is a filled form... not a scientific report."
This page is not field-value entries. It's a paragraph.
> One detail: "Requires running prose".
The text is a paragraph starting with "Q: ...". It is running prose.
> So **scientific_report** fits.
> <scratchpad>
file_folder: no — the page has a title and a full paragraph of text, not just an identifier.
handwritten: no — text is typed.
fax: no — no fax header.
questionnaire: no — although titled "QUESTIONS" and contains "Q:", this is a legal deposition question challenging scientific findings, not a survey instrument or consumer test questionnaire (Check 4 requires survey context).
resume: no — no career history.
scientific_publication: no — no journal running head/volume/issue on this page.
financial: no — no financial data.
specification: no — no material safety data or product specs.
presentation: no — not a slide deck or press release.
form: no — no fields, boxes, or checkboxes.
correspondence: no — no email header, memo header, or letter formatting (salutation/closing).
news_article: no — no masthead or news typography.
scientific_report: yes — the page contains running narrative prose (a paragraph) that functions as a scientific commentary/critique, challenging the data and conclusions of experiments ("your experiments found that nicotine use does not create a physical dependence", "conducted to the best of your scientific ability"). This fits the "scientific commentary/critique with running argument about a study's data and conclusions" description in Check 13.
advertisement: no — no marketing content.
Runner-up: questionnaire, ruled out because the page is a legal question critiquing scientific findings (Check 13 commentary/critique), not a survey instrument (Check 4).
</scratchpad>
<label>scientific_report</label>

---

## questionnaire → presentation (1 errors)

### `rvl_cdip__questionnaire__0005.png`
**Expected:** `questionnaire` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a logo "Bellomy Research" at the top.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a logo "Bellomy Research", a title "AROMA MINI GROUPS", "Prepared For: R. J. REYNOLDS TOBACCO COMPANY", "November 1991", and an address at the bottom. It has real content (title, prepared for, date).
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: There is a handwritten note "File Props" near the top right. But the majority of the content is typed (logo, title, prepared for, date, address).
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" or fax header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: No survey questions, no "APPENDIX N", no transmittal letter mentioning a survey.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: No CV/resume content.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal name, volume, issue, page range.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: No line-item table, no charges, no budget tracking. Just a title page.
    *   Result: not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: No MDS, no formulation, no "shall/must".
    *   Result: not this check.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: The page is a title page/cover page.
    *   "Bellomy Research" logo.
    *   Title: "AROMA MINI GROUPS".
    *   "Prepared For: R. J. REYNOLDS TOBACCO COMPANY", "November 1991".
    *   Address at bottom: "108 Cambridge Plaza Drive • Winston-Salem, NC 27104...".
    *   This looks like a cover page for a report or presentation. Let's look closely at the definition.
    *   "Slide/overhead layouts... a deck title or section-divider page, a meeting/program/speaker cover page... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation (this check), not file_folder (check 1)."
    *   Wait, is this a scientific_report title page?
    *   "Technical-study title pages: a title page naming a specific study or methodology with a date — e.g. 'TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter... / November 28, 1966' — is scientific_report (check 13), not presentation".
    *   "AROMA MINI GROUPS" sounds like a study title or a report title. "Bellomy Research" is a research firm. "Prepared For: R. J. REYNOLDS TOBACCO COMPANY". This is a report cover page.
    *   Let's check Check 13: scientific_report. "Original research write-up... A lab or technical study title page with authors and an internal affiliation and no journal identifiers."
    *   Wait, Bellomy Research is an external firm ("Prepared For: R.J. Reynolds"). This is likely a report submitted to RJR.
    *   Is it a presentation? "a deck title or section-divider page... A near-blank cover or title page... is a presentation".
    *   Let's re-read Check 9: "Slide/overhead layouts... a deck title or section-divider page... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date... is a presentation".
    *   The page is mostly empty space. Title: "AROMA MINI GROUPS". Date: "November 1991". Prepared for: "R. J. REYNOLDS TOBACCO COMPANY". Logo: "Bellomy Research".
    *   This fits the description of a presentation cover or a report cover. Wait, is a report cover a presentation?
    *   "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".
    *   "AROMA MINI GROUPS" is a specific study/topic. Bellomy Research is a research company. This is likely a technical report or a presentation deck cover.
    *   Let's look at the "presentation" definition again. "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page...".
    *   The page is very sparse. Large empty space. Title centered. "Prepared For" block at bottom right. Address at bottom.
    *   This looks like a cover page for a document. Is it a presentation (deck cover) or a scientific_report (title page)?
    *   Check 13: "A lab or technical study title page with authors and an internal affiliation and no journal identifiers." Bellomy Research is an external affiliation. The title page has "Bellomy Research" logo.
    *   Let's look at Check 9 again. "a deck title or section-divider page... A near-blank cover or title page... is a presentation".
    *   The page is a cover page for a document prepared by Bellomy Research for RJR. "AROMA MINI GROUPS".
    *   Often, external research reports have cover pages like this. If it's a report, it might be scientific_report. But scientific_report requires "Running narrative prose...". This page has no prose.
    *   Wait, Check 13 says: "Requires running prose — a page that is only labeled field-value entries... is a filled form... not a scientific report." AND "Also scientific_report: ... a technical-study title page naming a specific experimental method/study (see check 9)".
    *   Check 9 says: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".
    *   "AROMA MINI GROUPS" is a specific study/topic. Date is "November 1991".
    *   However, is it a "technical-study title page"? "AROMA MINI GROUPS" sounds like a focus group topic or a study title.
    *   Let's look at the layout. It's a cover page. "Prepared For: R. J. REYNOLDS TOBACCO COMPANY".
    *   If this is the first page of a report, the report itself (subsequent pages) would be scientific_report. But this specific page is just a title page.
    *   Check 9: "a deck title or section-divider page... A near-blank cover or title page... is a presentation".
    *   Check 9 caveat: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".
    *   Does "AROMA MINI GROUPS" name a specific study or methodology? It sounds like a study title (e.g., a study on aroma mini groups, maybe focus groups).
    *   Let's consider "presentation". "a meeting/program/speaker cover page... a corporate press release...".
    *   This looks like a cover page for a report or a presentation deck.
    *   Let's look at the "presentation" definition: "Slide/overhead layouts... a deck title or section-divider page...".
    *   If this is a cover page for a report (Bellomy Research report), is it a presentation?
    *   Usually, cover pages for reports are not presentations unless it's a deck.
    *   But the instruction says: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note ... is a presentation (this check), not file_folder".
    *   This page is mostly empty space. Title: "AROMA MINI GROUPS". Date: "November 1991". Prepared for: RJR.
    *   This fits "near-blank cover or title page".
    *   Wait, is it a scientific_report title page? "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report".
    *   "AROMA MINI GROUPS" is a bit vague. It could be a study title.
    *   Let's look at the logo: "Bellomy Research". Bellomy Research is a market research firm. They do focus groups, surveys, etc. "Aroma Mini Groups" likely refers to focus groups (mini groups) about aroma.
    *   Market research reports are often presentations or reports.
    *   If it's a market research report, is it scientific_report? Scientific_report is "Original research write-up... Running narrative prose...". This page has no prose.
    *   If this is just the cover page, and the check is for the page itself...
    *   Check 9: "a deck title or section-divider page... A near-blank cover or title page ... is a presentation".
    *   Check 13: "Requires running prose...". This page has no running prose. So it cannot be scientific_report based on the main definition.
    *   The exception in Check 13 is "a technical-study title page naming a specific experimental method/study". "AROMA MINI GROUPS" is not really an experimental method. It's a market research topic.
    *   So Check 13 doesn't fit well because it's not a technical study with experimental methods, and there's no prose.
    *   Check 9 fits: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date... is a presentation".
    *   The page has "AROMA MINI GROUPS" (bold headline title), "November 1991" (date), "Prepared For: R. J. REYNOLDS..." (subtitle/context).
    *   This is a deck cover or report cover. The instructions say "a deck title or section-divider page... is a presentation". And "A near-blank cover or title page... is a presentation".
    *   Let's check if there's any other category.
    *   Could it be a form? No.
    *   Could it be a letter? No salutation, no closing.
    *   Could it be a memo? No TO/FROM header.
>     Let's re-evaluate "scientific_report".
    Check 13: "Also scientific_report: ... a technical-study title page naming a specific experimental method/study (see check 9)".
    Check 9 says: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".
    Is "AROMA MINI GROUPS" a specific study or methodology? "Mini groups" is a market research term (focus groups). It's not a scientific experimental method like "Determination And Reporting Of Total Particulate Matter".
    So it's likely not a technical-study title page in the scientific_report sense.
>     So it falls back to Check 9: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date... is a presentation".
    The page is mostly empty space. Title "AROMA MINI GROUPS". Date "November 1991".
    This matches the "near-blank cover or title page" description for presentation.
>     Wait, is there any other evidence?
    "Bellomy Research" logo. "File Props" handwritten note.
    Address at bottom.
    This is a cover page for a document. In the tobacco archive, external research reports often have cover pages like this. If the document is a report, the cover page is often classified as presentation if it's a deck, or if it's a near-blank cover.
    The instructions say: "A near-blank cover or title page ... is a presentation (this check), not file_folder".
    It also says: "Technical-study title pages ... is scientific_report".
    Since "AROMA MINI GROUPS" is not a technical study title (it's market research), and there is no running prose, it's not scientific_report.
    So it must be presentation.
>     Let's check the runner-up.
    Runner-up: scientific_report. Ruled out because the page is a near-blank cover page with no running prose and "AROMA MINI GROUPS" is not a specific experimental method/study title (it's a market research topic), and the technical-study title page exception requires a specific study/methodology. Also, scientific_report requires running prose (main definition).
    Runner-up: file_folder. Ruled out because there is a bold headline title "AROMA MINI GROUPS" and real content (Prepared For, date), so it's not just filing metadata.
>     Let's refine the Check 9 evidence.
    Evidence: "mostly empty space with only a bold headline title ('AROMA MINI GROUPS') and perhaps a subtitle, date ('November 1991'), and 'Prepared For' block". This matches the "near-blank cover or title page" definition in Check 9.
>     Wait, is it a "company statement"? No.
    Is it a "deck cover"? Yes, likely a cover for a Bellomy Research presentation/report.
>     Let's look at the "presentation" definition again.
    "Slide/overhead layouts... a deck title or section-divider page, a meeting/program/speaker cover page... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation".
    This page fits "near-blank cover or title page".
>     Final decision: presentation.
>     Let's double check Check 13 exception.
    "Technical-study title pages: a title page naming a specific study or methodology with a date — e.g. 'TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter, Water In Total Particulate Matter, And Nicotine In Cigarette Smoke / November 28, 1966' — is scientific_report (check 13), not presentation, even when it is sparse or printed slide-style on a dark background".
    "AROMA MINI GROUPS" is not like that example. It's short, vague. Bellomy Research is a market research firm. This is likely a market research report or presentation. Market research reports are often treated as presentations or forms, but a cover page like this is a presentation cover.
>     Actually, looking at the layout:
    Top: Logo "Bellomy Research". Handwritten "File Props".
    Center: "AROMA MINI GROUPS".
    Bottom Right: "Prepared For: R. J. REYNOLDS TOBACCO COMPANY", "November 1991", Bates number "50918 7883".
    Bottom: Address.
    This is a classic cover page for a report or presentation.
    Given the "near-blank cover" rule in Check 9, it's presentation.
>     One distinct possibility: Is it a "scientific_report" because it's a research report?
    Check 13: "Requires running prose". This page has no prose.
    Exception: "technical-study title page". "AROMA MINI GROUPS" is not a technical study title.
    So not scientific_report.
>     Is it a "form"? No fields.
    Is it a "letter"? No.
>     So "presentation" is the best fit.
>     Wait, could it be "file_folder"?
    Check 1: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
    "A prominent topical heading always counts as real content... 'AROMA MINI GROUPS' is a prominent topical heading."
    So not file_folder.
>     Final check:
    Check 9: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date... is a presentation".
    Evidence: Page is mostly empty space. Bold headline "AROMA MINI GROUPS". Date "November 1991". "Prepared For" block. Logo.
    This matches.
>     Runner-up: scientific_report. Ruled out because the page lacks running prose and "AROMA MINI GROUPS" is not a specific experimental method/study title (it's a market research topic), so the technical-study title page exception doesn't apply.
    Runner-up: file_folder. Ruled out because the page has a prominent topical heading "AROMA MINI GROUPS" and "Prepared For" content, not just filing metadata.

---

## questionnaire → handwritten (1 errors)

### `rvl_cdip__questionnaire__0016.png`
**Expected:** `questionnaire` | **Predicted:** `handwritten`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> Image analysis:
- Top: handwritten "79-0414"
- Middle: handwritten "Lab plan & Questionnaire"
- Bottom right: stamped "50130 8150" (Bates number) and a handwritten "1" or similar mark.
- The page is mostly blank white space.
- The content is entirely handwritten text: "79-0414", "Lab plan & Questionnaire".
- There is a Bates number "50130 8150".
> Let's go through the checks:
> Check 1: IDENTIFIER-ONLY PAGE -> file_folder
- Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card.
- Wait, the text says "Lab plan & Questionnaire". Is this a topical title?
- "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
- "A prominent topical heading always counts as real content, subtitle or not."
- "Lab plan & Questionnaire" is a handwritten note/heading.
- Wait, check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten.
- "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
- "This wins over a typed letter or memo layout."
- The page is entirely handwritten: "79-0414", "Lab plan & Questionnaire".
- Is it a folder tab? No, it's a full page with handwriting.
- Let's check check 2: "Most of the content is freeform handwriting... NOT on a printed template." This page has no printed template, just a Bates stamp. The handwriting is freeform.
- Wait, what about check 1? "A page is NOT file_folder if it carries any real content... or a note." This is a handwritten note.
- Let's look at check 2: "handwritten: Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout."
- The page has "79-0414" and "Lab plan & Questionnaire" written by hand. This is a handwritten note/label.
- Is it a folder tab? No, it's a full sheet of paper with handwriting.
- Let's re-read check 1: "A Bates number or archive stamp alone is NOT enough... A prominent topical heading always counts as real content... EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... is a filing label, not a bold headline title... The page stays file_folder even when the label is rotated..."
- This page is not a folder tab. It's a full page with handwriting.
- So check 1 is not this.
> Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
- "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
- Evidence: Handwritten text "79-0414", "Lab plan & Questionnaire". No printed template.
- This matches handwritten.
> Let's double check check 4: questionnaire.
- "Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing (e.g. "Revised questionnaire to be used VIII-IV. Revisions highlighted in VIII file. CPP questionnaire was not changed.") is a transmittal note for the instrument — questionnaire (check 4), even though it is freeform handwriting on blank paper."
- Wait! "Lab plan & Questionnaire" is a note about a questionnaire? Or is it just a handwritten label?
- "A handwritten note about a questionnaire's revision, distribution, or routing... is a transmittal note for the instrument — questionnaire (check 4)"
- "Lab plan & Questionnaire" sounds like a title or a note indicating what this page is about (a lab plan and a questionnaire). But the page itself is just this handwritten text.
- Wait, if the page is JUST a handwritten note "Lab plan & Questionnaire", is it a transmittal note? Or is it just a handwritten label/note?
- Let's read check 2 carefully: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout. It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form (or the content's own category: a handwritten list of budget categories... is budget, not handwritten)."
- "Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing... is a questionnaire (check 4)"
- Is "Lab plan & Questionnaire" a note about a questionnaire's revision, distribution, or routing? No, it's just a title/label. "Lab plan & Questionnaire". It doesn't mention revision, distribution, or routing. It's just a handwritten note/label.
- Actually, could it be a folder tab? No, it's a full page.
- Let's consider "handwritten". The page is mostly blank, with handwritten "79-0414" and "Lab plan & Questionnaire". This is a handwritten note.
- Wait, what if it's a file_folder? "A page is NOT file_folder if it carries any real content... or a note." This is a note. So not file_folder.
- What about check 9: presentation? "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... is a presentation (this check), not file_folder (check 1)." But this is handwritten, not a designed title page. Check 2 says "Most of the content is freeform handwriting... This wins over a typed letter or memo layout." Does it win over presentation? Presentation is for slide decks, deck covers, etc. This is just a handwritten note on a blank page.
- Let's re-read check 2: "The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
- This page is blank paper with freeform handwriting. So it's handwritten.
> Let's check if there's any other evidence.
- "79-0414" could be a Bates number or an internal ID.
- "50130 8150" is a Bates number.
- "Lab plan & Questionnaire" is handwritten.
- This is a handwritten note/label.
> Is there any chance it's a questionnaire?
- "Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing... is a transmittal note for the instrument — questionnaire (check 4), even though it is freeform handwriting on blank paper."
- "Lab plan & Questionnaire" is not a note about revision, distribution, or routing. It's just a title. So it doesn't meet the specific condition for questionnaire under check 4.
- Therefore, it falls under handwritten (check 2).
> Let's review the checks in order:
1. file_folder: No, it has a handwritten note "Lab plan & Questionnaire", which is real content, not just an identifier. Also not a folder tab.
2. handwritten: Yes, majority content is freeform handwriting ("79-0414", "Lab plan & Questionnaire") on blank paper, not on a printed template.
3. form: No fax header.
4. questionnaire: No printed survey instrument. The note "Lab plan & Questionnaire" is not a note about revision/distribution/routing, just a label.
5. resume: No.
6. scientific_publication: No.
7. financial: No.
8. specification: No.
9. presentation: No, it's handwritten, not a designed deck cover or slide. (Check 2 wins over presentation for freeform handwriting on blank paper? Actually, check 9 says "A near-blank cover or title page... is a presentation... not file_folder". But check 2 says "Most of the content is freeform handwriting... This wins over a typed letter or memo layout." Wait, does handwritten win over presentation? The instructions say "Walk checks 1-14 below IN ORDER. For each check, before moving to the next one, briefly state... If evidence is present: STOP HERE." So if check 2 matches, we stop at check 2.)
- Wait, is "Lab plan & Questionnaire" a bold headline title? It's handwritten. Check 9 says "mostly empty space with only a bold headline title... is a presentation". But this is handwritten. Check 2 is earlier than check 9.
- Let's check the order: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14.
- Check 2 is "MAJORITY-HANDWRITTEN PAGE -> handwritten". Evidence: freeform handwriting on blank paper. Stop here.
> Let's confirm check 2 evidence:
- "79-0414" and "Lab plan & Questionnaire" are handwritten.
- No printed template.
- Matches check 2.
> Runner-up: file_folder, ruled out because the page contains a handwritten note ("Lab plan & Questionnaire") which is real content, not just filing metadata, and it is not a photographed folder tab.
> Final label: handwritten.

---