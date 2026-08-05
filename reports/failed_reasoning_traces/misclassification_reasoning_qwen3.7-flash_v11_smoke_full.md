# Misclassification Reasoning — qwen3.7-flash_v11_smoke_full

**Overall Accuracy:** 87.7% (207/236)  
**Total Errors:** 29  
**Unique Confused Pairs:** 6

---

## news_article → scientific_publication (10 errors)

### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: Top left says "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right says "Vol. 119, No. 4", "Printed in U.S.A.". Bottom center says "624". Bottom right says "T10447-0692". This is a journal running head/footer with volume, issue, page number, and copyright. This points strongly to check 6 (scientific_publication).
> **Check 1: file_folder**
- Evidence: The page has a full article with title, authors, abstract, and running prose. Not just an identifier.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: There is a handwritten "Lung C." at the top, but the majority of the content is typed text.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax cover sheet header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey questions or transmittal note.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: No CV or resume content.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right: "Vol. 119, No. 4", "Printed in U.S.A.". Bottom center: "624". This is a named journal ("AMERICAN JOURNAL OF EPIDEMIOLOGY") plus publication identifiers (volume 119, issue 4, page 624, copyright 1984) on THIS page.
- Result: YES. STOP HERE.
> **Runner-up:** scientific_report. Ruled out because the page carries its own journal running head/footer (journal name, volume, issue, page number, copyright), making it a published reprint (scientific_publication) rather than an internal write-up.
> Final label: scientific_publication.

---
### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header: None.
- Masthead/running head: Top left says "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved." Top right says "Vol. 119, No. 4 Printed in U.S.A.". Bottom center says "624". Bottom right says "T10447-0692". This is a journal running head/footer with volume, issue, page number, and copyright.
> **Check 1: file_folder**
- Evidence: The page has a full article with title, authors, abstract, and running prose. Not just an identifier.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: Mostly typed text. There is a handwritten "Lung C." at the top right, but it's not majority handwritten.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax cover sheet header.
- Result: not this check.
> **Check 4: questionnaire**
- Evidence: No survey instrument.
- Result: not this check.
> **Check 5: resume**
- Evidence: Not a CV/resume.
- Result: not this check.
> **Check 6: scientific_publication**
- Evidence: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright © 1984", page number "624". This is a named journal + volume/issue + page range + copyright on THIS page.
- Result: YES. STOP HERE.
> Runner-up: scientific_report, ruled out because the page carries its own journal running head/footer (American Journal of Epidemiology, Vol. 119, No. 4, page 624, copyright 1984), making it a published reprint (check 6 precedes check 13).
> Final label: scientific_publication.

---
### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: Top left says "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right says "Vol. 119, No. 4", "Printed in U.S.A.". Bottom center says "624". Bottom right says "T10447-0692". This is a journal running head/footer with volume, issue, page number, and copyright.
> **Check 1: file_folder**
- Evidence: The page has a full article with title, authors, abstract, and running text. Not just an identifier.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: Mostly typed text. There is a handwritten "Lung C." at the top right, but it's not majority handwritten.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax cover sheet header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: Not a survey.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: Not a resume.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right: "Vol. 119, No. 4", "Printed in U.S.A.". Bottom center: "624". This is a named journal ("AMERICAN JOURNAL OF EPIDEMIOLOGY") plus publication identifiers (volume 119, issue 4, page 624, copyright 1984) on THIS page.
- Result: YES. STOP HERE.
> Let's double check.
The page is a reprint of an article from the American Journal of Epidemiology, Vol. 119, No. 4, page 624, 1984.
Title: "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES"
Authors: Richard G. Stevens and Suresh H. Moolgavkar.
This perfectly matches check 6: "a named journal on the page plus a publication identifier (volume/issue, page range, DOI, journal copyright line...)"
> Runner-up: scientific_report. Ruled out because the page carries its own journal running head/footer (American Journal of Epidemiology, Vol. 119, No. 4, page 624, copyright 1984), making it a published scientific_publication (check 6 precedes check 13).
> Final label: scientific_publication.

---
### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header: None.
- Masthead/running head: Top left says "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved." Top right says "Vol. 119, No. 4", "Printed in U.S.A.". Bottom center says "624". Bottom right says "T10447-0692". This is a journal running head/footer with volume, issue, page number, and copyright.
> **Check 1: file_folder**
- Evidence: The page has a full article with title, authors, abstract, and running prose. Not just an identifier.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: Mostly typed text. There is a handwritten "Lung C." at the top right, but it's not majority handwritten.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax cover sheet header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey questions or transmittal.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: Not a resume.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved." Top right: "Vol. 119, No. 4", "Printed in U.S.A.". Bottom center: "624". This is a named journal + volume + issue + page range + copyright on THIS page.
- Result: YES. Stop here.
> Runner-up: scientific_report, ruled out because the page carries its own journal running head/footer (American Journal of Epidemiology, Vol. 119, No. 4, page 624, copyright 1984), making it a published reprint (check 6 precedes check 13).
> Final label: scientific_publication.

---
### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** I see "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright c 1984 by The Johns Hopkins University School of Hygiene and Public Health". No "From/To/Sent/Subject" email headers. There is a handwritten "Lung C-" at the top.
- **Masthead/Running head:** Yes, "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright c 1984...". This is a journal running head. Page number "624" is at the bottom. This points strongly to `scientific_publication`.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a full article title "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES", authors, abstract, and running text.
    *   Result: Not this check.
> *   **Check 2: handwritten**
    *   Evidence: Mostly typed text. There is a handwritten "Lung C-" at the top right.
    *   Result: Not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No fax cover sheet header.
    *   Result: Not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
    *   Evidence: No survey questions or transmittal note.
    *   Result: Not this check.
> *   **Check 5: PERSON'S CAREER HISTORY**
    *   Evidence: Authors are listed (Richard G. Stevens and Suresh H. Moolgavkar), but it's an article by them, not their CV.
    *   Result: Not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY". Top right: "Vol. 119, No. 4", "Printed in U.S.A.". Bottom center: "624". Bottom right: "T10447-0692" (Bates number, likely archive). Copyright line: "Copyright c 1984 by The Johns Hopkins University School of Hygiene and Public Health".
    *   This is a page from a published journal. It has the journal name, volume, issue, page number, and copyright.
    *   Result: **MATCH**. This is `scientific_publication`.
> *   **Check 7: FINANCIAL DOCUMENT**
    *   Evidence: No financial data.
    *   Result: Not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
    *   Evidence: No product specs.
    *   Result: Not this check.
> *   **Check 9: SLIDE DECK...**
    *   Evidence: Dense text, not a slide.
    *   Result: Not this check.
> *   **Check 10: ADMINISTRATIVE FORM**
    *   Evidence: No form fields.
    *   Result: Not this check.
> *   **Check 11: CORRESPONDENCE**
    *   Evidence: No memo/letter headers.
    *   Result: Not this check.
> *   **Check 12: PUBLISHED JOURNALISM**
    *   Evidence: "American Journal of Epidemiology" is a scientific journal, not a general news outlet. The content is a scientific abstract and article.
    *   Result: Not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP**
    *   Evidence: It looks like a scientific report (abstract, methods, results), BUT check 6 takes precedence because the page itself carries the journal identifier (running head, volume, page number). The instructions say: "First, use your pre-scan finding: does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings? If yes, that's your evidence — proceed here even if the writing reads like a report...". Wait, check 6 is `scientific_publication`. Check 13 is `scientific_report`. The instructions say "If yes [running head], that's your evidence — proceed here [check 6] even if the writing reads like a report". So check 6 wins over check 13.
> *   **Check 14: PROMOTIONAL MATERIAL**
    *   Evidence: No ads.
    *   Result: Not this check.
> **Conclusion:**
The page is a reprint or original page from the "American Journal of Epidemiology", Vol 119, No 4, page 624. It has the journal header, copyright, and page number. This fits `scientific_publication`.
> Runner-up: `scientific_report`. Ruled out because the page carries its own journal running head ("AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "624"), making it a published document (reprint or original page) rather than an internal report.
> Let's double check the text.
Title: "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES"
Authors: Richard G. Stevens and Suresh H. Moolgavkar.
Abstract text follows.
Footer: "624".
Header: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright c 1984...".
> This is definitely a scientific publication.
> Final check of the scratchpad procedure:
- Pre-scan: Masthead "AMERICAN JOURNAL OF EPIDEMIOLOGY", Vol 119, No 4. Copyright 1984. Page 624.
- Check 1: file_folder. No, has content.
- Check 2: handwritten. No, mostly typed.
- Check 3: Fax. No.
- Check 4: Questionnaire. No.
- Check 5: Resume. No.
- Check 6: scientific_publication. Yes. Journal name, volume, issue, page number, copyright on the page.
- Stop here.
> Runner-up: scientific_report. Ruled out because the page has a journal running head (American Journal of Epidemiology, Vol 119, No 4, page 624), which makes it a published scientific publication (check 6) rather than an internal scientific report (check 13).
> The label is `scientific_publication`.

---
### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: Top left says "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right says "Vol. 119, No. 4 Printed in U.S.A.". Bottom center says "624". Bottom right says "T10447-0692". This is a journal running head/footer with volume, issue, page number, and copyright.
> **Check 1: file_folder**
- Evidence: The page has a full article with title, authors, abstract, and running prose. Not just an identifier.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: Mostly typed text. There is a handwritten "Lung C." at the top right, but it's not majority handwritten.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax cover sheet header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: Not a survey.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: Not a resume.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right: "Vol. 119, No. 4 Printed in U.S.A.". Bottom center: "624". This is a named journal ("AMERICAN JOURNAL OF EPIDEMIOLOGY") plus publication identifiers (volume 119, issue 4, page 624, copyright 1984) on THIS page.
- Result: STOP HERE. This is scientific_publication.
> Let's double check.
The page is an article from the American Journal of Epidemiology, Vol 119, No 4, page 624.
Title: "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES"
Authors: Richard G. Stevens and Suresh H. Moolgavkar.
This perfectly matches check 6: "a named journal on the page plus a publication identifier (volume/issue, page range, DOI, journal copyright line...)"
> Runner-up: scientific_report. Ruled out because the page carries its own journal running head/footer (American Journal of Epidemiology, Vol. 119, No. 4, page 624, copyright 1984), making it a published reprint (scientific_publication), not an internal write-up.
> Final label: scientific_publication.

---
### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: Top left says "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved." Top right says "Vol. 119, No. 4 Printed in U.S.A.". Bottom center says "624". Bottom right says "T10447-0692". This is a journal running head/footer with volume, issue, page number, and copyright. This points strongly to check 6 (scientific_publication).
> **Check 1: file_folder**
- Evidence: The page has a full article with title, authors, abstract, and running text. Not just an identifier.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: There is a handwritten "Lung Ca" at the top right, but the majority of the content is typed text.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax cover sheet header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey questions or transmittal.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: Not a resume.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved." Top right: "Vol. 119, No. 4 Printed in U.S.A.". Bottom center: "624". Title: "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES". Authors: RICHARD G. STEVENS AND SURESH H. MOOLGAVKAR. This is a published article from a named journal with volume, issue, page number, and copyright on this page itself.
- Result: STOP HERE. This is check 6.
> **Runner-up:** scientific_report, ruled out because the page carries its own journal running head/footer (American Journal of Epidemiology, Vol. 119, No. 4, page 624, copyright 1984), making it a published scientific_publication (check 6) rather than an internal scientific_report (check 13).
> Final label: scientific_publication.

---
### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** None. There's a handwritten "Lung C." at the top, but no From/To/Sent/Subject.
- **Masthead or running head:**
    - Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved."
    - Top right: "Vol. 119, No. 4", "Printed in U.S.A."
    - Bottom center: "624"
    - Bottom right: "T10447-0692" (Bates number)
    - This looks like a page from a scientific journal. Specifically, "American Journal of Epidemiology", Vol 119, No 4, page 624.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a full article with title, authors, abstract, and running text.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: Mostly typed text. Only a small handwritten note "Lung C." at the top.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No fax header.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
    *   Evidence: No survey questions.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY**
    *   Evidence: Authors are listed, but it's an article, not a CV.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: Top left header: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved." Top right: "Vol. 119, No. 4", "Printed in U.S.A.". Bottom center page number: "624".
    *   Title: "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES".
    *   Authors: Richard G. Stevens and Suresh H. Moolgavkar.
    *   This is a page from a published journal. It has the journal name, volume, issue, copyright, and page number.
    *   Result: YES. This is a scientific_publication.
> *   **Check 7: FINANCIAL DOCUMENT**
    *   Evidence: No financial data.
    *   Result: not this check.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
    *   Evidence: No product specs.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK...**
    *   Evidence: Dense text, not a slide.
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM**
    *   Evidence: No form fields.
    *   Result: not this check.
> *   **Check 11: CORRESPONDENCE**
    *   Evidence: No memo/letter structure.
    *   Result: not this check.
> *   **Check 12: PUBLISHED JOURNALISM**
    *   Evidence: It's a scientific journal, not a general news outlet. The masthead is "American Journal of Epidemiology", a research journal. Check 6 takes precedence or rather, check 6 is the specific match for research journals. Wait, let's look at the order. Check 6 is "PUBLISHED EVIDENCE". Check 12 is "PUBLISHED JOURNALISM".
    *   The instructions say: "First, use your pre-scan finding: does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings? If yes, that's your evidence — proceed here [Check 6] even if the writing reads like a report..."
    *   So Check 6 matches.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP**
    *   Evidence: It is a research write-up, but it's a published journal article. Check 6 precedes Check 13. "A scientific-looking page with no journal or proceedings identifier is NOT a publication." This page has the identifier. So it's Check 6.
> *   **Check 14: PROMOTIONAL MATERIAL**
    *   Evidence: No ads.
    *   Result: not this check.
> **Conclusion:**
The page is a reprint from the "American Journal of Epidemiology", Vol 119, No 4, page 624. It has the journal name, copyright, volume, issue, and page number. This fits Check 6: scientific_publication.
> Runner-up: scientific_report. Ruled out because the page carries its own journal running head (American Journal of Epidemiology, Vol 119, No 4, page 624, copyright 1984), making it a published reprint (scientific_publication), not an internal write-up.
> Let's double check the text.
Header: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved.", "Printed in U.S.A."
Title: "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES"
Authors: "RICHARD G. STEVENS and SURESH H. MOOLGAVKAR"
Citation in text: "Am J Epidemiol 1984;119:624-41." (This is a self-citation or reference to the same paper's full citation, actually it looks like the abstract citation). Wait, the abstract says "Stevens, R.G. ... Am J Epidemiol 1984;119:624-41." This confirms it's the article itself.
Page number at bottom: 624.
> This is definitely a scientific_publication.
> Final check of the steps:
1. file_folder: No.
2. handwritten: No.
3. fax: No.
4. questionnaire: No.
5. resume: No.
6. scientific_publication: Yes. Evidence: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright © 1984", page number "624".
7. financial: No.
8. specification: No.
9. presentation: No.
10. form: No.
11. correspondence: No.
12. news_article: No (it's a research journal, not general news).
13. scientific_report: No (Check 6 matches first).
14. advertisement: No.
> The label is scientific_publication.

---
### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header: None.
- Masthead/running head: Top left says "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right says "Vol. 119, No. 4 Printed in U.S.A.". Bottom center says "624". Bottom right says "T10447-0692". This is a journal running head/footer with volume, issue, page number, and copyright.
> **Check 1: file_folder**
- Evidence: The page has a full article with title, authors, abstract, and running prose. Not just an identifier.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: Mostly typed text. There is a handwritten "Lung C." at the top right, but it's not majority handwritten.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax cover sheet header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: Not a survey.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: Not a resume.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved". Top right: "Vol. 119, No. 4 Printed in U.S.A.". Bottom center: "624". This is a named journal + volume/issue + page range + copyright on THIS page.
- Result: YES. Stop here.
> Runner-up: scientific_report, ruled out because the page carries its own journal running head/footer (American Journal of Epidemiology, Vol. 119, No. 4, page 624, copyright 1984), making it a published reprint (check 6), not an internal write-up.
> Final label: scientific_publication.

---
### `test_imagesr_r_c_s_rcs96d00_ti04470692_0709.tif.png`
**Expected:** `news_article` | **Predicted:** `scientific_publication`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** None. There's a handwritten "Lung C" at the top, but no From/To/Sent/Subject.
- **Masthead or running head:**
    - Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved."
    - Top right: "Vol. 119, No. 4", "Printed in U.S.A."
    - Bottom center: "624"
    - Bottom right: "T10447-0692" (Bates number)
    - This looks like a page from a scientific journal. Specifically, "American Journal of Epidemiology", Vol 119, No 4, page 624.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: None. The page has a full article title, authors, abstract, and running text.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: There is a handwritten note "Lung C" at the top right. But the majority of the content is printed text.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: None.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: None. It's an article about lung cancer.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: None.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: Top left header: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Copyright © 1984 by The Johns Hopkins University School of Hygiene and Public Health. All rights reserved." Top right: "Vol. 119, No. 4", "Printed in U.S.A." Bottom center: page number "624".
    *   This matches the criteria for a published journal article. Named journal ("American Journal of Epidemiology") + publication identifier (Vol. 119, No. 4, page 624, copyright line).
    *   Result: YES. STOP HERE.
> *   **Check 7: FINANCIAL DOCUMENT**
    *   Not reached.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
    *   Not reached.
> *   **Check 9: SLIDE DECK...**
    *   Not reached.
> *   **Check 10: ADMINISTRATIVE FORM**
    *   Not reached.
> *   **Check 11: CORRESPONDENCE**
    *   Not reached.
> *   **Check 12: PUBLISHED JOURNALISM**
    *   Not reached.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP**
    *   Not reached. (Though the content is a scientific report, the journal header makes it a publication).
> *   **Check 14: PROMOTIONAL MATERIAL**
    *   Not reached.
> **Final Decision:**
The page has a clear journal running head: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", page number "624", copyright line. This fits Check 6 perfectly.
> Runner-up: scientific_report. Ruled out because the page carries its own journal running head/volume/issue/page number (Check 6 precedes Check 13).
> Let's double check the text.
Title: "A COHORT ANALYSIS OF LUNG CANCER AND SMOKING IN BRITISH MALES"
Authors: RICHARD G. STEVENS and SURESH H. MOOLGAVKAR
Abstract follows.
Running text follows.
Footer: "624"
Header: "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4".
> This is definitely a scientific_publication.
> Wait, looking closely at the top right: "Vol. 119, No. 4".
Top left: "AMERICAN JOURNAL OF EPIDEMIOLOGY".
This is a reprint or a page from the journal.
Check 6 says: "Evidence for this check: a named journal on the page plus a publication identifier (volume/issue, page range, DOI, journal copyright line...)"
Yes, "AMERICAN JOURNAL OF EPIDEMIOLOGY", "Vol. 119, No. 4", "Copyright © 1984...", page "624".
> So the label is scientific_publication.

---

## invoice → budget (6 errors)

### `test_imagesj_j_o_w_jow70f00_0011930077.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking each condition in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None.
> **Check 1: file_folder**
- Evidence: The page has a lot of content (a voucher form with fields, descriptions, amounts, approvals). Not just an identifier/stamp.
- Result: not this check.
> **Check 2: handwritten**
- Evidence: Mostly typed text with some handwritten dates/names ("November 1989", "Rand R. B. Pepple"). Not majority handwritten.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey questions.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: No CV/resume content.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal running head.
- Result: not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: The page is titled "VOUCHER" from "BROWN & WILL FARSON TOBACCO CORPORATION".
- Fields: Date (11/20/89), Vendor No (210119), Vendor (The Franklin Institute), Address (Benjamin Franklin Parkway, Philadelphia, PA 19108), Due Date (12/1/89).
- Item Description: "Final contribution for grant to above institute for basic research"
- Item Amount: $278,000.00
- Pay this amount: $278,000.00
- Account Name: Gen, Corp, Contributions - Medical - Other
- Account No: 665 08-4694
- This is a payment voucher / check stub / payment request.
- Let's look at the rules for Check 7:
  - "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
  - "budget: ... a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
  - Wait, is a voucher an invoice or budget?
  - "invoice: ... a payment voucher ... is an invoice" -> Let's re-read carefully: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
  - Wait, the text says: "invoice: ... a payment voucher ... is an invoice".
  - Let's check the budget definition: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
  - The document is a "VOUCHER" from Brown & Will Farson Tobacco Corporation. It's an internal payment authorization/voucher to pay The Franklin Institute $278,000.00 for a grant.
  - Is it a payment voucher (invoice) or a check stub/expenditure request (budget)?
  - "a payment voucher ... is an invoice" is explicitly listed under invoice. BUT wait: "a contribution/expenditure request or approval form whose whole content is an amount ... is budget".
  - Let's re-read the invoice bullet: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
  - Wait, if it's a "payment voucher", the text explicitly says it's an invoice. BUT let's look at the context. The vendor is "The Franklin Institute". The description is "Final contribution for grant to above institute for basic research". This is a grant payment.
  - Is a grant payment voucher an invoice or budget?
  - Let's look at the budget bullet again: "budget: ... a check face or check stub ... Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts..."
  - Wait, the text says: "invoice: ... a payment voucher ... is an invoice". This seems to override. Let's read carefully: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement with unit prices, amounts, and totals."
  - Actually, a voucher is typically an internal document authorizing payment. The text says "a payment voucher" is an invoice. Wait, no: "an 'INVOICE' header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..." are all examples of invoice.
  - Let's re-read: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
  - Wait, if the vendor is The Franklin Institute, they are stating charges owed? No, the company (Brown & Will Farson) is issuing a voucher to pay them.
  - Let's look at the budget definition: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
  - This is a "VOUCHER" which is an internal expenditure authorization / payment request. "Gen, Corp, Contributions - Medical - Other". It's a contribution/expenditure request or approval form whose whole content is an amount ($278,000.00). This fits "budget" perfectly: "a contribution/expenditure request or approval form whose whole content is an amount".
  - Let's re-evaluate "payment voucher" under invoice. "invoice: ... a payment voucher ...". This might refer to a vendor's payment voucher (i.e., a bill from a vendor asking for payment). But here, the header is "VOUCHER BROWN & WILL FARSON TOBACCO CORPORATION". This is an internal voucher to authorize payment.
  - Let's check the budget bullet again: "Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount". This document is exactly that: a contribution request/approval form (Voucher) for an amount ($278,000.00) to The Franklin Institute for a grant.
  - Therefore, it is budget.
> Let's double check.
Document title: "VOUCHER"
Company: "BROWN & WILL FARSON TOBACCO CORPORATION"
Vendor: "The Franklin Institute"
Description: "Final contribution for grant to above institute for basic research"
Amount: "$278,000.00"
Account: "Gen, Corp, Contributions - Medical - Other"
This is an internal form to authorize a contribution/expenditure.
Check 7 says: "budget: ... Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount ... is budget, not invoice".
Wait, the invoice bullet says: "invoice: ... a payment voucher ...". This is ambiguous. But the budget bullet explicitly says: "a contribution/expenditure request or approval form whose whole content is an amount ... is budget". This document is a contribution request/approval form (a voucher) for a grant amount. So it's budget.
> Let's check if there's any other category.
- form (check 10): "internal authorization/approval forms with an approval signature/date block". But check 7 says "Money function overrides form layout... a billing or payment page stays financial even when it is printed on a form...". And "a contribution/expenditure request or approval form whose whole content is an amount ... is budget". So budget overrides form.
> Let's review the invoice vs budget distinction for vouchers.
"invoice: ... a payment voucher ... is an invoice" -> This likely means a vendor's payment voucher (a bill).
"budget: ... a contribution/expenditure request or approval form whose whole content is an amount ... is budget".
Since this is an internal voucher from Brown & Will Farson to pay a grant, it's an expenditure request/approval form. The content is an amount ($278,000). So it's budget.
> Let's confirm the text: "Final contribution for grant to above institute for basic research". Yes, it's a contribution.
Account name: "Gen, Corp, Contributions - Medical - Other".
This is definitely a budget document (expenditure/contribution tracking).
> Let's do a quick pass of other checks just in case.
- Check 8: specification. No.
- Check 9: presentation. No.
- Check 10: form. "internal authorization/approval forms with an approval signature/date block". But check 7 takes precedence for financial content. "Money function overrides form layout... a billing or payment page stays financial even when it is printed on a form...". Wait, is this a billing page? No, it's an internal contribution request. "a contribution/expenditure request or approval form whose whole content is an amount ... is budget". So budget.
- Check 11: correspondence. No.
- Check 12: news_article. No.
- Check 13: scientific_report. No.
- Check 14: advertisement. No.
> So the label is budget.
> Wait, is there any possibility it's a form?
"internal authorization/approval forms with an approval signature/date block" -> form (check 10).
But check 7: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
And: "Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount ... is budget, not invoice".
This perfectly matches: a contribution/expenditure request (Voucher) whose whole content is an amount ($278,000). So it's budget.
> Let's write the scratchpad.
- file_folder: no — the page has a full voucher form with financial data, not just an identifier.
- handwritten: no — mostly typed, with some handwritten dates/names.
- fax: no — no fax header.
- questionnaire: no — no survey items.
- resume: no — no career history.
- scientific_publication: no — no journal header.
- financial (invoice/budget): yes — titled "VOUCHER" from Brown & Will Farson Tobacco Corporation, authorizing a "$278,000.00" contribution/grant to "The Franklin Institute" for "basic research", with account code "Gen, Corp, Contributions - Medical - Other". This is an internal contribution/expenditure request and approval form whose primary content is an amount, which falls under budget (check 7), not invoice (which is for outside vendor charges for goods/services sold) or form (check 10, overridden by check 7's money function rule).
- specification: no.
- presentation: no.
- form: no — check 7 overrides form layout for financial documents; this is a contribution/expenditure request for a specific amount, classified as budget.
- correspondence: no.
- news_article: no.
- scientific_report: no.
- advertisement: no.
> Runner-up: form, ruled out because check 7 explicitly states that money function overrides form layout, and a "contribution/expenditure request or approval form whose whole content is an amount" is budget, not form.
> Final label: budget.

---
### `test_imagesj_j_o_w_jow70f00_0011930077.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** I see "VOUCHER", "BROWN & WILL FARSON TOBACCO CORPORATION". No "From/To/Sent/Subject" email headers. There is a "SENT BY:" type header? No, I see "DATE: 11/20/89", "VENDOR NO: 18118". Wait, let's look closer.
- Top right: "VOUCHER", "BROWN & WILL FARSON TOBACCO CORPORATION".
- Left side: "DATE: 11/20/89", "VENDOR NO: 18118".
- Vendor: "The Franklin Institute", "Benjamin Franklin Parkway", "Philadelphia, PA 19108".
- "DUE DATE: 12/1/89".
- "ITEM DESCRIPTION": "Final contribution for grant to above Institute for basic research".
- "ITEM AMOUNT": "$278,000.00".
- "TOTAL THIS AMOUNT": "$278,000.00".
- "TO: Mr. W. L. DeWitt".
- "PAY THIS AMOUNT": "$278,000.00".
- "DUPLICATE": "NOT TO BE PAID".
- "ACCOUNT NAME": "Gen, Corp, Contributions - Medical - Other".
- "ACCT CODE": "665 03-4694".
- Handwritten note: "November 16 '89".
- Bates number: "0682321162".
> This looks like a payment voucher or a check stub/face. It's a financial document.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**: No, there is substantial content (a voucher form with financial data). Not just an ID.
*   **Check 2: handwritten**: No, mostly typed form fields, with some handwriting ("November 16 '89", maybe a signature or initials, but the bulk is typed form data). Wait, the handwriting is just a date and maybe initials. The form is filled out.
*   **Check 3: FAX TRANSMISSION SHEET**: No "FACSIMILE" header.
*   **Check 4: questionnaire**: No.
*   **Check 5: resume**: No.
*   **Check 6: scientific_publication**: No journal header.
*   **Check 7: FINANCIAL DOCUMENT**:
    *   This is a "VOUCHER" from "BROWN & WILL FARSON TOBACCO CORPORATION".
    *   It lists a vendor ("The Franklin Institute"), an item description ("Final contribution for grant..."), and an amount ("$278,000.00").
    *   It has account codes ("Gen, Corp, Contributions - Medical - Other", "665 03-4694").
    *   It has a "TOTAL THIS AMOUNT" and "PAY THIS AMOUNT".
    *   Is it an invoice or a budget?
    *   **Invoice definition**: "an outside vendor, supplier, or agency states charges owed... a payment voucher... a receipt, a payment request...". Wait, let's look at the definitions carefully.
    *   "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
    *   "budget: ... internal money planning, tracking, or disbursement ... a check face or check stub ... a provider's periodic customer statement ... is budget, not invoice".
    *   Wait, the text says: "A check face/check stub stays budget even when the detachable stub's columns are headed 'INVOICE DATE'/'INVOICE NO.'/'INVOICE AMOUNT' — a check and its stub record a disbursement from a payment instrument, not a vendor bill for goods or services."
    *   This document is titled "VOUCHER". A voucher is a document used to authorize payment. It looks like a payment voucher or a check authorization form.
    *   Let's re-read Check 7 carefully.
    *   "invoice: ... a payment voucher ...". Wait. "invoice: an outside vendor... states charges owed... a payment voucher...".
    *   Let's check the budget definition: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub...".
    *   Is a "VOUCHER" an invoice or a budget?
    *   The document is from "BROWN & WILL FARSON TOBACCO CORPORATION" (the company itself, presumably, or a subsidiary). It is paying "The Franklin Institute".
    *   "Final contribution for grant to above Institute for basic research".
    *   This is an internal disbursement record. It's a voucher to pay a grant.
    *   Let's look at the "invoice" bullet: "a payment voucher". Wait. "invoice: ... a payment voucher, a vendor's price...". This suggests a payment voucher *from* a vendor? Or a voucher *for* payment?
    *   Usually, a "Voucher" in accounting is an internal document authorizing payment (a check request).
    *   Let's look at the "budget" bullet: "internal money planning, tracking, or disbursement ... a check face or check stub". This looks like a check stub or a voucher for a check.
    *   Let's look at the "invoice" bullet again: "an outside vendor... states charges owed...". Here, the document is *from* Brown & Will Farson Tobacco Corporation (the payer), not the vendor. The vendor is "The Franklin Institute". The document is describing a payment *to* the vendor.
    *   "Final contribution for grant...". This is a disbursement.
    *   The document has account codes: "Gen, Corp, Contributions - Medical - Other". This is internal accounting tracking.
    *   This fits "budget" better: "internal money planning, tracking, or disbursement... a check face or check stub". A voucher is essentially a check authorization/stub.
    *   Wait, let's look at the specific text: "VOUCHER BROWN & WILL FARSON TOBACCO CORPORATION".
    *   It lists "PAY THIS AMOUNT $278,000.00".
    *   It has "ACCOUNT NAME: Gen, Corp, Contributions - Medical - Other".
    *   This is an internal financial record of a disbursement (a grant payment).
    *   Check 7 says: "budget: internal money planning, tracking, or disbursement... a check face or check stub".
    *   Check 7 says: "invoice: an outside vendor... states charges owed". This document is not from the vendor stating charges owed (though it describes the contribution). It is the company's internal voucher to make the payment.
    *   Actually, let's look at the "payment voucher" mention in the invoice section: "invoice: ... a payment voucher, a vendor's price...". This is confusing. Usually a payment voucher is internal.
    *   Let's re-read: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD ... a payment voucher ...". This implies a payment voucher *from* a vendor? Or a voucher *requesting* payment?
    *   Let's look at the budget section: "budget: ... internal money planning, tracking, or disbursement ... a check face or check stub ... ALSO a provider's periodic customer statement ... is budget".
    *   This document is a "VOUCHER" for a "contribution for grant". It's a disbursement record.
    *   Let's look at the "form" check (Check 10). "internal authorization/approval forms with an approval signature/date block". This has "TO: Mr. W. L. DeWitt", "PAY THIS AMOUNT". It looks like a filled form.
    *   But Check 7 says: "Money function overrides form layout... a billing or payment page stays financial even when it is printed on a form...".
    *   So it's either invoice or budget.
    *   Is it an invoice? An invoice is a bill *from* a vendor. This is a voucher *from* the company (Brown & Will Farson) to pay a vendor (Franklin Institute). The description says "Final contribution for grant to above Institute". This is the company's record of paying a grant.
    *   Therefore, it is a disbursement record. Disbursement records are "budget" (internal tracking/disbursement).
    *   Wait, is a "payment voucher" considered an invoice? "invoice: ... a payment voucher...". If the text explicitly says "payment voucher" is an invoice, I should be careful. But usually, a payment voucher is internal.
    *   Let's look at the definition of invoice again: "an outside vendor... states charges owed". Here, the document is *not* from the outside vendor stating charges. It's from the corporation stating they are paying a contribution. The "Item Description" is "Final contribution for grant...". This is not a bill for goods sold. It's a grant payment.
    *   Grants are often tracked as budgets/expenditures.
    *   "budget: ... internal money planning, tracking, or disbursement ... a check face or check stub". This looks exactly like a check stub or a voucher accompanying a check.
    *   Let's look at the "NOT TO BE PAID" box. "DUPLICATE: NOT TO BE PAID". This is a duplicate of a payment document.
    *   This is a financial document. Specifically, a disbursement record.
    *   Label: **budget**.
> Let's refine the "invoice" vs "budget" distinction.
- Invoice: Vendor bills the company. "Here is what you owe me."
- Budget/Check stub: Company records payment. "We are paying this amount from this account."
- This document: "VOUCHER BROWN & WILL FARSON TOBACCO CORPORATION". Vendor: The Franklin Institute. Item: Final contribution for grant. Amount: $278,000. Account: Gen, Corp, Contributions.
- This is the company's internal record of a payment (disbursement). It's a voucher/check stub.
- Check 7: "budget: ... internal money planning, tracking, or disbursement ... a check face or check stub".
- So **budget** is the correct label.
> Wait, is there any other check?
- Check 10: Administrative form. "Filled or blank fields... internal authorization/approval forms".
- But Check 7 says: "Money function overrides form layout... a billing or payment page stays financial...".
- "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
- So if it's a money record, it's Check 7.
- Is this a money record? Yes, it records a payment of $278,000.
- Is it an invoice or budget?
- Invoice: "outside vendor... states charges owed". This is not a vendor bill. It's a company voucher.
- Budget: "internal money planning, tracking, or disbursement... a check face or check stub". This fits perfectly. It's a voucher (check authorization/stub) for a disbursement.
> Let's double check the "payment voucher" mention in invoice.
"invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
This is tricky. "Payment voucher" can mean a document from a vendor requesting payment (like a remittance advice or invoice). But here the header is "VOUCHER BROWN & WILL FARSON TOBACCO CORPORATION". This is the payer's document.
Actually, in accounting, a "voucher" is an internal document. An "invoice" is external.
The text says "REMITTANCE ADVICE INFO. (13 CHAIR ONLY)". This suggests it might be a remittance advice?
"REMITTANCE ADVICE INFO. (13 CHAIR ONLY)" - this is a field label.
If it's a remittance advice, it's often sent with a check.
But the main title is "VOUCHER".
And it has "ACCOUNT NAME: Gen, Corp, Contributions". This is internal chart of accounts.
This is definitely an internal financial record (disbursement).
So **budget**.
> Let's look at the "invoice" definition again. "an agency/vendor ESTIMATE document... is the agency's BILL for a client job — invoice".
This is a grant contribution. Not a bill for goods/services sold in the commercial sense, though a grant is a payment.
"budget: ... internal money planning, tracking, or disbursement". A grant payment is a disbursement.
> Let's consider **form** (Check 10).
"internal authorization/approval forms with an approval signature/date block".
This has "TO: Mr. W. L. DeWitt", "PAY THIS AMOUNT". It looks like a check request form.
But Check 7 says: "Money function overrides form layout... a billing or payment page stays financial...".
And: "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
So if it's a financial document, it's Check 7.
Is it a "money-only form"? "ALSO a contribution/expenditure request or approval form whose whole content is an amount... is budget".
This form's whole content is an amount ($278,000) and account codes.
So it is **budget**.
> Final decision: **budget**.
> Wait, let's look at the "invoice" bullet again. "a payment voucher".
If the text explicitly lists "payment voucher" under invoice, maybe I should be careful.
But the context is "an outside vendor... states charges owed... a payment voucher [from vendor?]".
Here, the document is from the corporation. "BROWN & WILL FARSON TOBACCO CORPORATION".
The vendor is "The Franklin Institute".
So this is the corporation's document.
Corporation's payment record = disbursement = budget.
> One more check: **form**.
Check 10: "administrative form... internal authorization/approval forms".
Check 7 caveat: "an internal expenditure-authorization form ('ADVERTISING AND SELLING AUTHORIZATION', purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget".
Does this have billable charges?
"ITEM DESCRIPTION: Final contribution for grant... ITEM AMOUNT: $278,000.00".
It has an amount.
"ALSO a contribution/expenditure request or approval form whose whole content is an amount... is budget".
This form's content is the amount and the account code.
So it is **budget**.
> Let's re-read the "invoice" definition to ensure it's not an invoice.
"invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD".
The Franklin Institute is the vendor. Does *this page* state charges owed?
The page is titled "VOUCHER BROWN & WILL FARSON...".
The "Item Description" is "Final contribution for grant to above Institute".
This looks like the company's record of the payment, not the Institute's bill.
If it were the Institute's bill, it would be titled "INVOICE" from "The Franklin Institute".
Here, it is titled "VOUCHER" from "BROWN & WILL FARSON".
So it is the company's internal document.
Internal document recording a payment = budget (disbursement).
> So, **budget**.
> One detail: "REMITTANCE ADVICE INFO."
Remittance advice is often sent with a check.
But the main structure is a voucher/check stub.
"DUPLICATE NOT TO BE PAID". This is a stub.
Check 7: "a check face or check stub... is budget".
> Final conclusion: **budget**.
> Wait, is there any possibility it's a **form**?
Check 10: "administrative form".
Check 7: "Money function overrides form layout".
"money-only forms are budget (check 7)".
This is a money form (voucher for $278,000).
So it's budget.
> Let's check the labels again.
advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> The label is **budget**.
> One final check on "invoice".
Could "Final contribution for grant" be considered a charge?
If the Franklin Institute sent this as an invoice...
But the header says "BROWN & WILL FARSON TOBACCO CORPORATION".
And "VENDOR NO: 18118". The corporation is tracking the vendor.
This is the corporation's internal voucher.
So it's a disbursement record. -> budget.
> Scratchpad:
- file_folder: no, has content.
- handwritten: no, mostly typed.
- fax: no.
- questionnaire: no.
- resume: no.
- scientific_publication: no.
- financial (Check 7): Yes. It's a "VOUCHER" from Brown & Will Farson Tobacco Corp. It records a payment of $278,000.00 to The Franklin Institute for a "contribution for grant". It includes account codes ("Gen, Corp, Contributions - Medical - Other", "665 03-4694") and "DUPLICATE NOT TO BE PAID". This is an internal disbursement record / check stub / voucher.
- Invoice vs Budget: Invoice is for goods/services sold by a vendor. This is an internal record of a grant payment (disbursement). Check 7 says "budget: internal money planning, tracking, or disbursement... a check face or check stub". Also "contribution/expenditure request or approval form whose whole content is an amount... is budget". This fits budget.
- form (Check 10): It is a form, but Check 7 overrides for money records. "money-only forms are budget".
> Runner-up: form. Ruled out because Check 7 (financial document) takes precedence for money records, and this is a disbursement record (budget), not just an administrative form. Or runner-up: invoice. Ruled out because it's an internal disbursement record (voucher/check stub) from the payer, not a vendor bill for goods sold.
> Actually, the runner-up should be the one I almost picked.
I almost picked **form** because it has fields and boxes.
Or **invoice** because it has an amount and vendor.
Let's go with **form** as runner-up, ruled out by Check 7 money override.
Or **invoice** as runner-up, ruled out because it's a check stub/voucher (disbursement), not a vendor invoice.
> Let's look at the text "Final contribution for grant to above Institute for basic research".
This is a grant. Grants are often budget items.
The account is "Gen, Corp, Contributions".
This is definitely budget.
> Final label: budget.

---
### `test_imagesj_j_o_w_jow70f00_0011930077.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** No "From/To/Sent/Subject" block. There is a "VOUCHER" header. No fax transmission header like "SENT BY: ... # N/N". Wait, let's look closer. "BROWN & WILL FARSON TOBACCO CORPORATION". "VOUCHER".
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a lot of content: a voucher form with vendor info, dates, amounts, descriptions, approval blocks. It's not just an ID or stamp.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: Most content is typed (form fields filled in). There is some handwriting ("November 1989" at the bottom, maybe a signature or date). But the majority is a printed form structure.
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
    *   Evidence: The page is titled "VOUCHER" (BROWN & WILL FARSON TOBACCO CORPORATION).
    *   Vendor: "The Franklin Institute", Benjamin Franklin Parkway, Philadelphia, PA 19108. Vendor No: 18118.
    *   Date: 11/20/89. Due Date: 12/1/89.
    *   Item Description: "Final contribution for grant to above Institute for basic research".
    *   Item Amount: $278,000.00.
    *   Pay this amount: $278,000.00.
    *   Account Name: "Gen, Corp; Contributions- Medical- Other". Acct No: 665. 03-4694.
    *   This is a payment voucher / check stub / payment request.
    *   Let's check the definitions in Check 7.
    *   "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..." -> Wait, "payment voucher" is listed under invoice? Let's re-read carefully.
    *   "invoice: an outside vendor, supplier, or agency states charges owed... a payment voucher, a vendor's price... a receipt, a payment request..."
    *   "budget: ... a check face or check stub, a check/payment register... ALSO a provider's periodic customer statement... money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
    *   Wait, let's look at the "budget" definition again. "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
    *   The document is a "VOUCHER". A voucher is typically an internal document authorizing payment (a check face/stub or payment authorization).
    *   The description says "Final contribution for grant to above Institute for basic research". This is an expenditure/contribution.
    *   The account is "Gen, Corp; Contributions- Medical- Other".
    *   This looks like an internal payment authorization or check stub/voucher for a contribution.
    *   Let's distinguish between invoice and budget here.
    *   Invoice: "an outside vendor... states charges owed". The Franklin Institute is stating a charge? "Final contribution for grant...". Usually, a grant contribution is a payment *from* the company *to* the institute. The institute isn't selling goods/services in the traditional sense, it's receiving a grant/contribution.
    *   Budget definition: "a contribution/expenditure request or approval form whose whole content is an amount". This form has an approval block ("Rand R. B. Pepple", "Mr. W. L. DeWitt"). It's authorizing a payment of $278,000.00.
    *   Also, "check face or check stub" is budget. A voucher is often the internal document accompanying a check or acting as the check face.
    *   Let's look at the "invoice" bullet: "a payment voucher... is an invoice". Wait. "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
    *   Let's re-read carefully: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
    *   This is confusing. Is a "payment voucher" always an invoice?
    *   Let's look at the context. "BROWN & WILL FARSON TOBACCO CORPORATION". This is the payer. The vendor is "The Franklin Institute".
    *   If Brown & Will Farson is paying Franklin Institute, Franklin Institute is the vendor. But is it a sale of goods/services? "Final contribution for grant". A grant is a contribution.
    *   Let's look at the "budget" bullet: "money-only records: a contribution/expenditure request or approval form whose whole content is an amount". This form is an approval form (has signatures: Rand R. B. Pepple, Mr. W. L. DeWitt). The content is an amount ($278,000.00) for a contribution.
    *   Also, "check face or check stub" is budget. A voucher often functions like a check stub or payment authorization.
    *   Let's look at the structure. It has "VOUCHER" at the top. Vendor No, Date, Remittance Advice Info, Voucher No. Mail check to... Pay to... Item Description... Item Amount. Pay this amount. Account Name, Acct No.
    *   This is a payment voucher / check authorization.
    *   The definition for budget says: "a check face or check stub... a contribution/expenditure request or approval form whose whole content is an amount".
    *   The definition for invoice says: "a payment voucher...". This is a direct contradiction in the prompt text if taken literally. Let's look closer.
    *   "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..." -> This lists "payment voucher" under invoice.
    *   BUT, "budget: ... a check face or check stub...".
    *   Let's look at the specific wording for invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD". The Franklin Institute is not selling goods/services here; it's receiving a grant/contribution. The description is "Final contribution for grant". This is an expenditure by Brown & Will Farson.
    *   The budget definition: "money-only records: a contribution/expenditure request or approval form whose whole content is an amount". This fits perfectly. It's a form requesting/approving a contribution (expenditure) of a specific amount ($278,000).
    *   Also, the account code is "Contributions- Medical- Other". This is internal accounting tracking.
    *   So, is it invoice or budget?
    *   Let's re-read the invoice definition: "an outside vendor... states charges owed". Here, the internal company (Brown & Will Farson) is creating a voucher to pay an outside entity. The outside entity (Franklin Institute) isn't stating charges; the internal company is authorizing a payment. The "Item Description" is filled in by the internal company ("Final contribution for grant...").
    *   Therefore, it's not an invoice from a vendor. It's an internal payment authorization/voucher.
    *   Under budget: "a check face or check stub... a contribution/expenditure request or approval form whose whole content is an amount". This fits an internal voucher for a contribution.
    *   Wait, is a "voucher" a check stub? Often yes.
    *   Let's look at the "form" check (Check 10). "internal authorization/approval forms with an approval signature/date block". But Check 7 says "Money function overrides form layout... a contribution/expenditure request or approval form whose whole content is an amount... is budget".
    *   So Check 7 (budget) overrides Check 10 (form).
>     Let's refine the classification between invoice and budget.
    - Invoice: Vendor bills company. "The Franklin Institute" is the vendor. But the text says "Final contribution for grant". Grants are usually not "goods or services sold" in the commercial sense, though they can be. However, the document is a "VOUCHER" from "BROWN & WILL FARSON TOBACCO CORPORATION". This is the payer's document. An invoice usually comes from the payee. A voucher is the payee's (or payer's internal) document to authorize payment.
    - Actually, a "payment voucher" is often the internal document. The prompt says under invoice: "a payment voucher". This is tricky.
    - Let's look at the budget definition again: "a check face or check stub... a contribution/expenditure request or approval form whose whole content is an amount".
    - The document has approval signatures ("Rand R. B. Pepple", "Mr. W. L. DeWitt"). It is an approval form.
    - The content is a contribution amount ($278,000).
    - The account is "Contributions- Medical- Other".
    - This strongly points to **budget**. It is an internal expenditure tracking/approval document.
>     Let's check the invoice definition again: "an outside vendor, supplier, or agency states charges owed...". Here, the document is generated by Brown & Will Farson (the corporation at the top). It's their voucher. They are paying Franklin Institute. So Franklin Institute is not stating charges on this document; Brown & Will is stating they are paying a contribution.
    - Wait, the "Remittance Advice Info" box says "THIS CHAIR ONLY".
    - "Pay to: Rand R. B. Pepple" (Wait, "Pay to" usually goes to the vendor. Here it says "Pay to: Rand R. B. Pepple"? No, let's look closer. "MAIL CHECK TO ADDRESS SHOWN BELOW" -> The Franklin Institute. "PAY TO ORDER OF" -> Rand R. B. Pepple? Or is that the approver?
    - Let's look at the text: "MAIL CHECK TO ADDRESS SHOWN BELOW [ ] MAIL CHECK WITH ATTACHMENTS [X] PAY TO ORDER OF Rand R. B. Pepple". Wait, if it's a grant to the Institute, why pay to Rand Pepple? Maybe Rand Pepple is the contact?
    - Actually, looking closely at the right side: "VOUCHER NO... [ ] MAIL CHECK TO ADDRESS SHOWN BELOW [ ] MAIL CHECK WITH ATTACHMENTS [X] PAY TO ORDER OF Rand R. B. Pepple". This looks like the payment instruction.
    - But the address block on the left is "The Franklin Institute".
    - Item Description: "Final contribution for grant to above Institute for basic research".
    - This is a payment authorization.
    - Budget definition: "a contribution/expenditure request or approval form whose whole content is an amount". This fits perfectly. It's an approval form for a contribution.
>     So, **budget**.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
    *   Evidence: No MSDS, no product formulation.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK...**
    *   Evidence: Not a slide.
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM**
    *   Evidence: It is a form (voucher). But Check 7 (Financial) overrides if it's money-related.
    *   "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
    *   Since this is a money record (contribution/expenditure approval), it falls under Check 7.
> *   **Check 11: CORRESPONDENCE**
    *   Evidence: No letter/memo structure.
    *   Result: not this check.
> *   **Check 12: PUBLISHED JOURNALISM**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP**
    *   Evidence: No running prose.
    *   Result: not this check.
> *   **Check 14: PROMOTIONAL MATERIAL**
    *   Evidence: No.
    *   Result: not this check.
> **Conclusion:**
The document is a "VOUCHER" from Brown & Will Farson Tobacco Corporation.
It authorizes a payment/contribution of $278,000.00 to The Franklin Institute.
It has account codes ("Gen, Corp; Contributions- Medical- Other").
It has approval signatures.
This fits the definition of **budget**: "money-only records: a contribution/expenditure request or approval form whose whole content is an amount". Also "check face or check stub" (a voucher is similar).
It is not an invoice because the vendor (Franklin Institute) isn't stating charges for goods/services sold in a commercial transaction sense on this document; rather, the company is authorizing an expenditure/contribution. Even if we consider "payment voucher" as a keyword for invoice, the context is clearly an internal expenditure approval for a grant/contribution, which falls under budget ("contribution/expenditure request or approval form").
> Wait, let's look at the invoice definition again: "a payment voucher... is an invoice".
"invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
If the prompt explicitly lists "payment voucher" under invoice, I need to be careful.
But the invoice definition starts with: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD".
Does a grant contribution count as "goods or services SOLD"? Usually no. It's a contribution.
And the budget definition explicitly says: "money-only records: a contribution/expenditure request or approval form whose whole content is an amount".
This document is exactly that: a contribution request/approval form (Voucher) with an amount ($278,000).
The approval block (Rand R. B. Pepple, Mr. W. L. DeWitt) confirms it's an approval form.
The account code "Contributions- Medical- Other" confirms it's tracking a contribution.
So **budget** is the correct label.
> Let's double check the "payment voucher" in invoice list.
"invoice: ... an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
This list seems to describe documents *from* a vendor or *for* payment.
But the budget definition says: "a check face or check stub... a contribution/expenditure request or approval form whose whole content is an amount".
A voucher is essentially a check face/stub or expenditure request.
The key is the content: "Final contribution for grant". This is a contribution/expenditure.
The budget category covers "contribution/expenditure request or approval form".
So budget wins.
> Final check of the text:
Header: VOUCHER, BROWN & WILL FARSON TOBACCO CORPORATION.
Vendor: The Franklin Institute.
Amount: $278,000.00.
Description: Final contribution for grant...
Account: Gen, Corp; Contributions- Medical- Other.
This is an internal financial document tracking a contribution. -> budget.
> One detail: "Rand R. B. Pepple" is listed under "PAY TO ORDER OF". This is weird for a grant to the Institute. Maybe he is the contact person receiving the check? Or maybe it's a personal payment? "Final contribution for grant to above Institute". The address is the Institute. The check is probably made out to the Institute or to him for the Institute. Regardless, it's a financial transaction record.
The account code "Contributions- Medical- Other" is the strongest indicator of "budget" (internal tracking of money/contributions).
> So, label: budget.
> Wait, is it a form?
Check 10: "internal authorization/approval forms with an approval signature/date block".
But Check 7: "It does NOT cover money records: ... money-only forms are budget (check 7)."
So Check 7 overrides Check 10.
> Is it an invoice?
Check 7 invoice: "an outside vendor... states charges owed". The Franklin Institute is the vendor, but the document is a Voucher from Brown & Will. The description is "Final contribution". This is an expenditure.
Check 7 budget: "a contribution/expenditure request or approval form whose whole content is an amount". This fits perfectly.
> Final decision: budget.

---
### `test_imagesj_j_o_w_jow70f00_0011930077.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** I see "VOUCHER", "BROWN & WILL FARSON TOBACCO CORPORATION". No "From/To/Sent/Subject" email headers. There is a "SENT BY:" type header? No, I see "DATE: 11/20/89", "VENDOR NO: 18118". Wait, let's look closer.
- Top right: "VOUCHER", "BROWN & WILL FARSON TOBACCO CORPORATION".
- Left side: "DATE: 11/20/89", "VENDOR NO: 18118".
- Vendor: "The Franklin Institute", "Benjamin Franklin Parkway", "Philadelphia, PA 19108".
- "DUE DATE: 12/1/89".
- "ITEM DESCRIPTION": "Final contribution for grant to above institute for basic research".
- "ITEM AMOUNT": "$278,000.00".
- "TOTAL THIS AMOUNT": "$278,000.00".
- "PAY TO: Mr. W. L. DeWitt".
- Bottom: "Gen, Corp; Contributions-Medical-Other", "565 03-4694".
- Handwritten: "November 16 '89", "068232/1162".
- This looks like a payment voucher or invoice.
> - **Masthead/Running head:** No newspaper masthead. No journal running head.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a lot of content (table, text, amounts). Not just an ID.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: Mostly typed form fields. Handwriting is just a date "November 16 '89" and maybe a number. Not majority handwritten.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
    *   Result: not this check.
> *   **Check 4: questionnaire**
    *   Evidence: Not a survey.
    *   Result: not this check.
> *   **Check 5: resume**
    *   Evidence: Not a CV.
    *   Result: not this check.
> *   **Check 6: scientific_publication**
    *   Evidence: No journal header.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: The document is titled "VOUCHER" (top center). It lists a vendor ("The Franklin Institute"), an item description ("Final contribution for grant to above institute for basic research"), an amount ("$278,000.00"), and account coding ("Gen, Corp; Contributions-Medical-Other").
    *   Let's distinguish between invoice and budget.
    *   **Invoice definition:** "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request...". Wait, "a payment voucher" is listed under invoice? Let's check the text.
    *   Text: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
    *   Wait, is a "payment voucher" an invoice? Yes, "a payment voucher" is listed under invoice.
    *   Let's check "budget": "internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount...".
    *   Wait, there's a conflict. "a contribution/expenditure request or approval form whose whole content is an amount" is budget.
    *   But "a payment voucher" is invoice.
    *   Let's look at the document again. It's a "VOUCHER" from "BROWN & WILL FARSON TOBACCO CORPORATION".
    *   Vendor: "The Franklin Institute".
    *   Description: "Final contribution for grant to above institute for basic research".
    *   Amount: $278,000.00.
    *   Pay to: Mr. W. L. DeWitt.
    *   Account: "Gen, Corp; Contributions-Medical-Other".
    *   This is a payment voucher / check authorization.
    *   Let's re-read Check 7 carefully.
    *   "invoice: ... a payment voucher ...".
    *   "budget: ... a contribution/expenditure request or approval form whose whole content is an amount ...".
    *   Wait, is this a request or a voucher?
    *   The header says "VOUCHER". A voucher is a document authorizing payment.
    *   Let's look at the "invoice" definition again: "a payment voucher... is an invoice".
    *   Let's look at the "budget" definition again: "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
    *   This document has "VOUCHER" at the top. It has "PAY TO: Mr. W. L. DeWitt". It has account codes. It looks like a payment voucher / check stub / voucher for payment.
    *   Wait, the text says: "a payment voucher... is an invoice".
    *   Let's check the budget definition: "a check face or check stub... is budget".
    *   This looks like a voucher that accompanies a check or is the basis for a check.
    *   Actually, let's look at the structure. It has "DATE", "VENDOR NO", "VOUCHER NO", "MAIL CHECK TO...", "PAY TO...", "ITEM DESCRIPTION", "ITEM AMOUNT", "TOTAL THIS AMOUNT", "ACCOUNT NAME", "ACCT CODE", "AND OTHER LEDGER CODES".
    *   This is a payment voucher.
    *   The rule says: "invoice: ... a payment voucher ...".
    *   Wait, let's look closer. "a payment voucher" is explicitly listed under invoice.
    *   "budget: ... a check face or check stub ...".
    *   Is this a check stub? No, it's a voucher.
    *   Is it an invoice? The vendor is "The Franklin Institute". The description is "Final contribution for grant...". Usually, the vendor sends an invoice. Here, the company (Brown & Will Farson) is creating a voucher to pay the vendor.
    *   However, the rule says: "invoice: ... a payment voucher ...".
    *   Let's re-read: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
    *   Wait, if the company is paying a grant, is it an invoice?
    *   "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
    *   This document has account codes ("565 03-4694"), "Gen, Corp; Contributions-Medical-Other". It looks like an internal accounting document (a voucher) to record a payment.
    *   Let's look at the "budget" bullet: "Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount...".
    *   This document is a "VOUCHER". It authorizes payment of $278,000.00.
    *   Is it an invoice or a budget?
    *   Let's look at the "invoice" bullet again: "a payment voucher... is an invoice". This seems to cover documents like a voucher that bills for something? No, a payment voucher is usually internal.
    *   Wait, "a payment voucher" is listed under invoice. "a payment request" is listed under invoice.
    *   Let's look at the "budget" bullet: "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
    *   This is tricky.
    *   Let's look at the document content: "Final contribution for grant to above institute for basic research". $278,000.00.
    *   It is a payment for a grant.
    *   If it's a "contribution/expenditure request or approval form", it's budget.
    *   If it's a "payment voucher", it's invoice.
    *   The header is "VOUCHER".
    *   Let's look at the invoice definition: "an outside vendor... states charges owed... a payment voucher". This implies the vendor's payment voucher or a voucher *from* a vendor? No, "a payment voucher" is a generic term.
    *   Actually, usually a "Voucher" in accounting is a document supporting a payment.
    *   Let's look at the budget definition: "internal money planning, tracking, or disbursement... check face or check stub...".
    *   This looks like a check authorization / voucher.
    *   Let's look at the specific text: "BROWN & WILL FARSON TOBACCO CORPORATION". This is the payer.
    *   Vendor: "The Franklin Institute".
    *   This is a payment record.
    *   Let's reconsider the "invoice" definition. "invoice: ... a payment voucher ...". If the text explicitly says "a payment voucher" is an invoice, then I should probably go with invoice.
    *   BUT, let's look at the budget definition: "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
    *   This form is an approval form (it has "PAY TO", account codes, date). It is a contribution request/approval.
    *   Wait, is there an "INVOICE" header? No.
    *   Is there a "VOUCHER" header? Yes.
    *   The rule says: "invoice: ... a payment voucher ...". This is a direct match for the word "voucher" if we interpret "payment voucher" as the document type.
    *   However, let's look at the context. "Final contribution for grant...".
    *   Let's look at the "budget" rule again: "Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount...".
    *   This document is an approval form for a contribution ($278,000).
    *   Let's look at the "invoice" rule again: "an outside vendor... states charges owed...". Here, the inside company (Brown & Will Farson) is creating the document. The vendor is The Franklin Institute. The Franklin Institute didn't send an invoice (or maybe they did, and this is the internal voucher).
    *   If this is an internal voucher to pay a grant, it's a disbursement record.
    *   "budget: internal money planning, tracking, or disbursement...". Disbursement is budget.
    *   "invoice: an outside vendor... states charges owed". This document is NOT from the outside vendor stating charges owed (though it describes the charge). It is from Brown & Will Farson (the payer).
    *   Wait, the header says "VOUCHER BROWN & WILL FARSON TOBACCO CORPORATION". So it's an internal document.
    *   Internal disbursement/tracking -> budget.
    *   Let's check the invoice definition again. "a payment voucher" is listed. But usually, a payment voucher is the document *attached* to a check.
    *   Let's look at the budget definition: "a check face or check stub... is budget". This looks like a voucher that goes with a check.
    *   Also, "a contribution/expenditure request or approval form whose whole content is an amount... is budget". This fits perfectly. It's a form approving a contribution of $278,000.
    *   So, is it invoice or budget?
    *   The document is a "VOUCHER".
    *   If I follow "a payment voucher" -> invoice.
    *   If I follow "contribution/expenditure request or approval form" -> budget.
    *   Let's look at the invoice definition more closely: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher...". This suggests that if a vendor sends a payment voucher (like a bill), it's an invoice. Or if the document is a payment voucher *from* a vendor?
    *   Actually, in accounting, a "Voucher" is an internal document. An "Invoice" is from a vendor.
    *   The text says "BROWN & WILL FARSON TOBACCO CORPORATION" at the top. This is the company paying.
    *   So this is an internal document.
    *   Internal document for money disbursement -> budget.
    *   Let's check the rule: "Money function overrides form layout... invoice: an outside vendor... states charges owed...". Here, the outside vendor (Franklin Institute) is the payee, but the document is from Brown & Will Farson. Wait, the "REMITTANCE ADVICE INFO" box is there.
    *   The "ITEM DESCRIPTION" says "Final contribution for grant...".
    *   This is a payment record.
    *   Let's look at the budget definition: "internal money planning, tracking, or disbursement...". This is a disbursement record (voucher for payment).
    *   Also: "a contribution/expenditure request or approval form whose whole content is an amount... is budget". This is exactly what this is. It's a form approving a contribution of $278,000.
    *   So, **budget** seems correct.
>     *   Wait, let's look at the "invoice" definition again. "a payment voucher... is an invoice". Why is "payment voucher" under invoice? Maybe it means a vendor's payment voucher (i.e. their bill)? Or a voucher *requesting* payment (payment request)? "a payment request" is under invoice.
    *   "a contribution/expenditure request... is budget".
    *   This document is a "VOUCHER". In corporate accounting, a voucher is a document authorizing payment. It's an internal control document.
    *   The content is "Final contribution for grant...".
    *   This is a disbursement. Disbursement is budget.
    *   Let's assume **budget**.
>     *   Wait, let's look at Check 10: Administrative Form.
    *   "internal authorization/approval forms with an approval signature/date block".
    *   This has "PAY TO", account codes, date. It's a form.
    *   But Check 7 says: "Money function overrides form layout... a payment voucher... is an invoice... a check face... is budget".
    *   So Check 7 overrides Check 10.
    *   Is it invoice or budget?
    *   Invoice: "outside vendor... states charges owed". This document is from Brown & Will Farson (the buyer/payer). It's not a vendor bill. It's an internal voucher.
    *   Budget: "internal money... disbursement... check face or check stub... contribution/expenditure request or approval form whose whole content is an amount".
    *   This fits "contribution/expenditure request or approval form whose whole content is an amount" ($278,000).
    *   So **budget**.
> *   **Check 8: specification**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 9: presentation**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 10: administrative form**
    *   Evidence: It is a form with fields. But Check 7 (Financial) overrides it because it's a money document.
    *   Result: not this check (because Check 7 applies).
> *   **Check 11: correspondence**
    *   Evidence: No.
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
> **Re-evaluating Check 7 (Invoice vs Budget):**
- Document title: "VOUCHER".
- Payer: "BROWN & WILL FARSON TOBACCO CORPORATION".
- Payee: "The Franklin Institute" (Vendor).
- Description: "Final contribution for grant to above institute for basic research".
- Amount: $278,000.00.
- Account: "Gen, Corp; Contributions-Medical-Other".
- This is an internal accounting document (voucher) to record a payment/grant.
- Rule for Invoice: "an outside vendor, supplier, or agency states charges owed... a payment voucher...". Wait. If "a payment voucher" is listed under invoice, maybe I should pick invoice?
- Let's read carefully: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
- The list "a payment voucher, a vendor's price... a receipt, a payment request" seems to be examples of what constitutes an invoice or invoice-like document.
- BUT, the first sentence says: "an outside vendor... states charges owed".
- This document is from Brown & Will Farson (the inside company). It is not from the outside vendor stating charges owed. It is the inside company saying "We are paying $278,000 to Franklin Institute".
- Rule for Budget: "internal money planning, tracking, or disbursement... a check face or check stub... a contribution/expenditure request or approval form whose whole content is an amount...".
- This document is an internal disbursement record (voucher) and an approval form for a contribution (grant).
- The amount is $278,000.
- The content is a contribution for a grant.
- This fits "contribution/expenditure request or approval form whose whole content is an amount" -> **budget**.
> Let's look at the "payment voucher" under invoice again.
"a payment voucher" might refer to a vendor's payment voucher (i.e. their bill). Or it might be a generic term.
However, "a contribution/expenditure request or approval form whose whole content is an amount... is budget" is very specific.
This document is a voucher approving a contribution of $278,000.
So **budget** is the best fit.
> Wait, is there any other category?
- form (Check 10): "internal authorization/approval forms with an approval signature/date block".
- But Check 7 says: "Money function overrides form layout... a contribution/expenditure request or approval form whose whole content is an amount... is budget".
- So Check 7 wins over Check 10.
> Final decision: **budget**.
> Let's double check the "invoice" definition.
"invoice: ... a payment voucher ...".
If the text explicitly lists "a payment voucher" as an example of invoice, I might be wrong.
Let's see: "invoice: an outside vendor... states charges owed... [examples: INVOICE header, a payment voucher, a vendor's price... a receipt, a payment request]".
The examples seem to be things that look like invoices or are used for billing.
A "payment request" is an invoice (requesting payment).
A "payment voucher" is usually internal.
If the document is a "VOUCHER" from the company paying, it's an internal disbursement.
Internal disbursement = budget.
"budget: internal money planning, tracking, or disbursement...".
Yes, disbursement is budget.
> So, **budget**.
> One more check: Is it a form?
Check 10: "administrative form".
Check 7: "Money function overrides form layout... a contribution/expenditure request or approval form whose whole content is an amount... is budget".
The document is a form (voucher) with an amount ($278,000).
So it is budget.
> Label: budget.
> Wait, looking at the image again.
Top: "VOUCHER", "BROWN & WILL FARSON TOBACCO CORPORATION".
Fields: Date, Vendor No, Vendor Name/Address, Due Date, Item Description, Item Amount.
"Final contribution for grant to above institute for basic research", "$278,000.00".
"PAY TO: Mr. W. L. DeWitt".
"TOTAL THIS AMOUNT": "$278,000.00".
Account info: "Gen, Corp; Contributions-Medical-Other", "565 03-4694".
Handwritten: "November 16 '89".
> This is a payment voucher / check authorization.
Function: Disbursement of funds (grant contribution).
Category: budget.
> Runner-up: invoice. Ruled out because the document is an internal voucher/approval form for a contribution (disbursement), not an outside vendor stating charges owed (though it references a vendor, the document itself is the payer's internal record/approval). Also, the rule explicitly says "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
> Wait, could it be **form**?
Check 10: "internal authorization/approval forms with an approval signature/date block".
Check 7: "Money function overrides form layout... a contribution/expenditure request or approval form whose whole content is an amount... is budget".
So budget overrides form.
> Final label: budget.

---
### `test_imagesj_j_o_w_jow70f00_0011930077.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There's a "VOUCHER" header and "BROWN & WILL FARSON TOBACCO CORPORATION". No journal masthead.
> **Check 1: file_folder**
- Evidence: The page has a lot of content: a voucher form with vendor info, dates, amounts, descriptions, approval blocks. Not just an identifier.
- Not this check.
> **Check 2: handwritten**
- Evidence: Mostly typed form with some handwritten text ("November 1989", "$278,000.00"). Not majority handwritten.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No survey questions.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: No resume/CV.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal running head, volume, issue, page number.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: The page is titled "VOUCHER" with "BROWN & WILL FARSON TOBACCO CORPORATION".
- Vendor: "The Franklin Institute", Benjamin Franklin Parkway, Philadelphia, PA 19108.
- Date: 11/20/89. Due Date: 12/1/89.
- Item Description: "Final contribution for grant to above institute for basic research".
- Item Amount: $278,000.00.
- Pay this amount: $278,000.00.
- Account Name: "Gen Corp; Contributions; Medical; Other".
- This is a payment voucher / check stub / payment request.
- Let's look at the rules for Check 7:
  - "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
  - "budget: ... a check face or check stub, a check/payment register ... ALSO a provider's periodic customer statement ... money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
  - Wait, is a voucher an invoice or budget?
  - "invoice: ... a payment voucher ... a receipt, a payment request ... It does not have to be titled 'INVOICE' — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
  - "budget: ... a check face or check stub ... money-only records: a contribution/expenditure request or approval form whose whole content is an amount ... ALSO a provider's periodic customer statement ... is budget, not invoice"
  - Let's re-read carefully: "invoice: ... a payment voucher ... a vendor's price ... a receipt, a payment request ... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget"
  - "budget: ... a check face or check stub ... money-only records: a contribution/expenditure request or approval form whose whole content is an amount"
  - This is a "VOUCHER" from Brown & Will Farson Tobacco Corporation to The Franklin Institute for a "Final contribution for grant ... for basic research" of $278,000.00.
  - Is it a payment voucher (invoice) or a check stub/contribution request (budget)?
  - "a payment voucher ... is an invoice"
  - "a contribution/expenditure request or approval form whose whole content is an amount ... is budget"
  - Wait, the description says "Final contribution for grant to above institute for basic research". This is a payment being made *by* Brown & Will Farson *to* The Franklin Institute.
  - A voucher is typically an internal document authorizing payment. "VOUCHER" at the top. "BROWN & WILL FARSON TOBACCO CORPORATION".
  - Let's check the invoice definition again: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD ... a payment voucher, a vendor's price ... a receipt, a payment request ... It does not have to be titled 'INVOICE' — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
  - Wait, if Brown & Will Farson is issuing a voucher to pay The Franklin Institute, is The Franklin Institute the vendor stating charges owed? No, Brown & Will Farson is the payer. The Franklin Institute is the recipient of a grant/contribution.
  - Let's check the budget definition: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
  - This is a voucher for a contribution/grant. "Final contribution for grant to above institute for basic research".
  - "a contribution/expenditure request or approval form whose whole content is an amount" -> budget.
  - Also, "a check face or check stub" -> budget. A voucher is often part of the check payment process (check stub / voucher).
  - Let's look at the fields: "VOUCHER NO.", "MAIL CHECK TO ADDRESS SHOWN", "MAIL CHECK WITH ATTACHMENTS", "PAY THIS AMOUNT $278,000.00". "DUPLICATE", "NOT TO BE PAID", "ACCOUNT NAME", "ACCT CODE", "AMOUNT". This is a check stub / payment voucher / disbursement record.
  - Under check 7 budget: "a check face or check stub ... money-only records: a contribution/expenditure request or approval form whose whole content is an amount". This fits perfectly. It's a disbursement record / check stub for a contribution.
  - Let's re-read invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD". The Franklin Institute is not selling goods/services here; it's receiving a grant/contribution. Brown & Will Farson is making a payment. This is an internal disbursement / expenditure record.
  - Therefore, it is a budget.
> Let's double check.
"budget: ... money-only records: a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category ... ALSO a provider's periodic customer statement ... is budget, not invoice"
This is a voucher for a contribution. "Final contribution for grant...". It's an expenditure record.
Label: budget.
> Let's check if it could be a form (check 10).
"administrative form -> form: Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; ... internal authorization/approval forms with an approval signature/date block."
But check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
And: "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
So check 7 overrides check 10.
> Is it an invoice?
"invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD ... a payment voucher ... a receipt, a payment request"
Wait, "a payment voucher" is listed under invoice?
Let's read carefully: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
Ah! "a payment voucher" is explicitly listed under invoice!
Wait, but what about the budget definition?
"budget: ... a check face or check stub, a check/payment register ... money-only records: a contribution/expenditure request or approval form whose whole content is an amount"
Which one is it? A voucher to pay a grant.
If Brown & Will Farson is issuing a voucher to pay The Franklin Institute, it's a payment voucher.
But is The Franklin Institute a vendor stating charges owed? No, it's a grant.
Let's look at the invoice definition again: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD ... a payment voucher ... a receipt, a payment request"
The phrase "a payment voucher" might refer to a vendor's payment voucher (i.e. a request for payment from a vendor).
But here, the document is titled "VOUCHER" and is from "BROWN & WILL FARSON TOBACCO CORPORATION". It's an internal document to authorize payment.
"PAY THIS AMOUNT $278,000.00". "Gen Corp; Contributions; Medical; Other".
This is an expenditure / contribution record.
"money-only records: a contribution/expenditure request or approval form whose whole content is an amount" -> budget.
I will classify as budget.
> Let's re-read the invoice bullet: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
If a vendor sends a "payment voucher" (a document requesting payment), it's an invoice.
But this document is FROM Brown & Will Farson TO The Franklin Institute (Mail check to address shown: The Franklin Institute). It's Brown & Will Farson's internal voucher to make a payment.
"VOUCHER / BROWN & WILL FARSON TOBACCO CORPORATION"
"DATE 11/20/89 / VENDOR NO. 18119 / REMITTANCE ADVICE INFO. (13 CHAIR ONLY) / VOUCHER NO."
"NAME The Franklin Institute"
"ADDRESS Benjamin Franklin Parkway, Philadelphia, PA 19108"
"DUE DATE 12/1/89"
"ITEM DESCRIPTION Final contribution for grant to above institute for basic research"
"ITEM AMOUNT $278,000.00"
"PAY THIS AMOUNT $278,000.00"
"Gen Corp; Contributions; Medical; Other"
This is a check stub / payment voucher / disbursement record for a contribution.
Under budget: "a check face or check stub ... money-only records: a contribution/expenditure request or approval form whose whole content is an amount".
This perfectly matches "contribution/expenditure request or approval form whose whole content is an amount" and "check stub".
So it is budget.
> Let's check check 10 just in case.
"administrative form -> form: ... internal authorization/approval forms with an approval signature/date block."
But check 7: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
"It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
So it's budget.
> Final check of the steps:
1. file_folder: no, has content.
2. handwritten: no, mostly typed.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial: yes. It's a voucher for a contribution/grant payment. Matches "budget" -> "money-only records: a contribution/expenditure request or approval form whose whole content is an amount" and "check face or check stub".
8. specification: no.
9. presentation: no.
10. form: overridden by check 7.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no.
14. advertisement: no.
> Label: budget.

---
### `test_imagesj_j_o_w_jow70f00_0011930077.tif.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There's a "VOUCHER" header and "BROWN & WILLIAMSON TOBACCO CORPORATION". No journal masthead.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a lot of content: a voucher form with vendor info, dates, amounts, descriptions, approval blocks. Not just an identifier.
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Mostly typed form with some handwritten entries (dates, names, amounts, "November 1989"). Not majority handwritten.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions or transmittal.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No career history.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal running head, volume, issue, page number.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: The page is titled "VOUCHER" with "BROWN & WILLIAMSON TOBACCO CORPORATION".
- It has "VENDOR NO.", "DATE", "VENDOR", "The Franklin Institute", "ADDRESS", "CITY, STATE & ZIP CODE", "DUE DATE", "ITEM DESCRIPTION" ("Final contribution for grant to above Institute for basic research"), "ITEM AMOUNT" ($278,000.00).
- It has "PAY THIS AMOUNT" ($278,000.00).
- It has account information: "Gen, Corp; Contributions- Medical- Other", "665 03-4694".
- This is a payment voucher / check stub / payment request.
- Let's look at the definitions in Check 7:
  - "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
  - "budget: ... a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
  - Wait, let's distinguish invoice vs budget here.
  - "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD ... a payment voucher ... a receipt, a payment request"
  - "budget: ... a check face or check stub ... a contribution/expenditure request or approval form whose whole content is an amount"
  - The document is a "VOUCHER" from Brown & Williamson Tobacco Corporation. It's an internal payment authorization/voucher to pay The Franklin Institute $278,000.00 for a "Final contribution for grant to above Institute for basic research".
  - Is it a payment voucher (invoice) or a contribution/expenditure request (budget)?
  - "a payment voucher ... is an invoice" -> "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
  - Wait, the text says: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
  - But it also says: "budget: ... a check face or check stub, a check/payment register ... a contribution/expenditure request or approval form whose whole content is an amount"
  - Let's re-read carefully: "invoice: ... a payment voucher ...". A voucher is typically a document authorizing payment, often used interchangeably with a payment voucher or check stub.
  - Wait, "a check face or check stub stays budget even when the detachable stub's columns are headed "INVOICE DATE"/"INVOICE NO."/"INVOICE AMOUNT" — a check and its stub record a disbursement from a payment instrument, not a vendor bill for goods or services."
  - This is a "VOUCHER" from Brown & Williamson Tobacco Corporation. It looks like an internal payment voucher / check requisition. "PAY THIS AMOUNT $278,000.00". "Gen, Corp; Contributions- Medical- Other".
  - Is this a payment voucher (invoice) or a check stub / expenditure request (budget)?
  - "invoice: ... a payment voucher ...". The definition explicitly lists "a payment voucher" under invoice.
  - Let's check the budget definition again: "budget: ... a check face or check stub, a check/payment register ... a contribution/expenditure request or approval form whose whole content is an amount".
  - The document has "VOUCHER" at the top. "BROWN & WILLIAMSON TOBACCO CORPORATION".
  - It has "VENDOR NO. 18118", "VENDOR The Franklin Institute".
  - "ITEM DESCRIPTION Final contribution for grant to above Institute for basic research". "ITEM AMOUNT $278,000.00".
  - "PAY THIS AMOUNT $278,000.00".
  - "Gen, Corp; Contributions- Medical- Other 665 03-4694".
  - This is a payment voucher / check requisition. The instructions say: "invoice: ... a payment voucher ...". So it should be invoice.
  - Wait, let's look at the budget definition: "a contribution/expenditure request or approval form whose whole content is an amount". This is a contribution request? "Final contribution for grant...". But it's a voucher to pay it.
  - Let's re-read the invoice bullet: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
  - The text explicitly says "a payment voucher" is an invoice.
  - Let's check if there's any other financial document type. It's a voucher. Voucher = invoice in this context?
  - Actually, a voucher is often an internal document to authorize payment (like a check requisition). But the rule says "a payment voucher" is under invoice.
  - Let's re-read: "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
  - Yes, "a payment voucher" is explicitly listed under invoice.
  - Let's consider if it's a budget. "budget: ... a check face or check stub ... a contribution/expenditure request or approval form whose whole content is an amount".
  - This form has account codes ("Gen, Corp; Contributions- Medical- Other 665 03-4694"), which is typical of a check stub or payment voucher.
  - However, the rule says "a payment voucher" is invoice. Let's assume invoice.
  - Wait, is it a payment request? "Final contribution for grant to above Institute for basic research". The vendor is The Franklin Institute. They are requesting payment? Or Brown & Williamson is authorizing payment to them?
  - "REMITTANCE ADVICE INFO. (13 CHAIR ONLY)". "MAIL CHECK TO ADDRESS SHOWN". "MAIL CHECK WITH ATTACHMENTS". "PAY THIS AMOUNT". This is Brown & Williamson issuing a check to The Franklin Institute. So it's a payment voucher / check requisition from B&W.
  - If it's a check stub / payment voucher from the payer, is it budget or invoice?
  - "a check face or check stub stays budget even when the detachable stub's columns are headed "INVOICE DATE"/"INVOICE NO."/"INVOICE AMOUNT" — a check and its stub record a disbursement from a payment instrument, not a vendor bill for goods or services."
  - This is a voucher from Brown & Williamson (the payer) to pay The Franklin Institute (the vendor). It records a disbursement. "PAY THIS AMOUNT". It has account codes for the disbursement. This sounds like a check stub or internal payment voucher, which falls under budget ("a check face or check stub", "record a disbursement").
  - BUT the invoice definition says: "invoice: ... a payment voucher ...". This is a contradiction in the prompt's definitions if not read carefully.
  - Let's read the invoice definition again: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
  - Here, "a payment voucher" likely refers to a vendor's payment voucher (a document from the vendor requesting payment, like a remittance advice or voucher attached to an invoice).
  - The budget definition says: "budget: ... a check face or check stub, a check/payment register ... record a disbursement from a payment instrument, not a vendor bill for goods or services."
  - This document is from Brown & Williamson Tobacco Corporation (the payer). It has "VOUCHER" at the top. It has "PAY THIS AMOUNT". It has account codes "Gen, Corp; Contributions- Medical- Other". This is an internal payment authorization / check stub / disbursement record. Therefore, it is budget.
  - Let's verify: "a check face or check stub stays budget ... a check and its stub record a disbursement from a payment instrument, not a vendor bill for goods or services." This document is a voucher from the corporation to pay a vendor. It's essentially a check stub or payment voucher for a disbursement. The account code "Gen, Corp; Contributions- Medical- Other" confirms it's an internal accounting record for a disbursement (budget).
  - Also, "a contribution/expenditure request or approval form whose whole content is an amount" is budget. This is a contribution of $278,000.00.
  - So budget is the correct label.
> Let's double check.
Document: "VOUCHER", "BROWN & WILLIAMSON TOBACCO CORPORATION".
Vendor: "The Franklin Institute".
Description: "Final contribution for grant to above Institute for basic research".
Amount: "$278,000.00".
Account: "Gen, Corp; Contributions- Medical- Other 665 03-4694".
This is an internal payment voucher / check requisition from Brown & Williamson to pay a grant/contribution to The Franklin Institute.
It records a disbursement (budget), not a vendor bill for goods/services (invoice). The vendor is receiving a grant/contribution, not selling goods/services. "Final contribution for grant...". Grants are not invoices for goods/services.
Therefore, it is budget.
> Let's check Check 10: ADMINISTRATIVE FORM -> form.
"A form does NOT have to be blank — a filled form recording data is still a form... It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
Since it's a money record (payment voucher for a grant), it falls under check 7 (budget or invoice).
As established, it's a disbursement record for a contribution, so it's budget.
> Let's review the invoice vs budget distinction for grants/contributions.
"invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD" -> A grant is not goods or services sold.
"budget: ... a contribution/expenditure request or approval form whose whole content is an amount" -> This is a contribution.
So it is budget.
> Final check of the steps:
1. file_folder: no, has content.
2. handwritten: no, mostly typed.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial: yes. It's a voucher for a contribution/grant payment. Records a disbursement. Budget.
8. specification: no.
9. presentation: no.
10. form: no, money records go to check 7.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no.
14. advertisement: no.
> Label: budget.

---

## budget → form (6 errors)

### `test_imagesu_u_s_a_usa07d00_timo0000799.tif.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify the provided document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header: None.
- Masthead/running head: "TOBACCO INSTITUTE ID 12-771-5334 SEP 21 '95 LITIGATION NO.001 P.02". This looks like an archive stamp/Bates-like identifier, not a journal masthead. "TIMO 0000799" at the bottom right. "Confidential Missouri Tobacco Litigation Case No. 972-1465". No journal masthead.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a title "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", filled fields, signatures. It has real content. Not file_folder.
> *   **Check 2: handwritten**
    *   Evidence: Most content is typed form fields with some handwritten entries (Date: 6/4/96, Name: DON KOLLER, Address, Amount: 250.00, signatures). Not majority handwritten.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" or fax cover sheet header. The top line is archive metadata. Not a fax sheet.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: Not a survey asking the reader to answer questions. It's a request for a contribution.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: Not a resume.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal running head.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: Contains "Amount 250.00", "Account Code", "Check Payable to". Title is "POLITICAL CAMPAIGN CONTRIBUTION REQUEST".
    *   Let's check the rules for budget vs invoice vs form.
    *   "budget: internal money planning, tracking, or disbursement... Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts..."
    *   Wait, is this a form or a budget?
    *   Check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
    *   Check 7 caveat: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
    *   This is a "CONTRIBUTION REQUEST" with an amount ($250.00), account code, check payable to, and approval signatures (Regional Vice President, Senior Vice President). It authorizes a single expenditure/contribution.
    *   Therefore, it's an internal expenditure-authorization form. Check 7 says this is a form (check 10), not budget.
    *   Let's re-read Check 7: "an internal expenditure-authorization form ... is a form (check 10), not budget".
    *   So Check 7 does not apply as invoice or budget. It points to Check 10.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: No.
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
    *   Evidence: No.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". Filled fields (Name, Address, Amount, Account Code, Check Payable to). Approval block ("Approved by:", Regional Vice President's signature, Senior Vice President's signature). "Revised 2/95".
    *   This perfectly matches "internal authorization/approval forms with an approval signature/date block" and "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
    *   Check 7 caveat explicitly excludes this from budget: "an internal expenditure-authorization form ... with an approval signature/date block but no billable charges is a form (check 10), not budget". This is a contribution request/authorization, not a bill for goods/services (invoice) or a budget tracking document.
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
    *   Evidence: No TO/FROM/RE header followed by prose. No letterhead with external address and salutation.
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
    *   Evidence: No.
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
    *   Evidence: No running prose.
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
    *   Evidence: No.
> **Conclusion:**
The document is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST" form. It has fields for recipient info, contribution info (amount, account code), and an approval block. According to Check 7 caveat, an internal expenditure-authorization form with an approval block is a form (Check 10), not budget. According to Check 10, it is an administrative form.
> Let's double check Check 7 budget definition: "Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount..." Wait.
Let's re-read carefully: "budget: ... Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category (amounts need not be legible)."
BUT the caveat says: "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> This document is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It has an amount ($250.00), account code, check payable to, and approval signatures. Is it a "contribution/expenditure request or approval form whose whole content is an amount"?
The caveat specifically says "an internal expenditure-authorization form ... with an approval signature/date block but no billable charges is a form (check 10), not budget". This document has an approval signature block and no billable charges (it's a contribution request, not a vendor bill). The amount is $250.00, but it's a request to make a contribution, authorized by VPs.
Actually, let's look at the wording: "a contribution/expenditure request or approval form whose whole content is an amount". This page has recipient info (Don Koller, P.O. Box 135...), current office, party, committees, account code, check payable to, notes, and approval signatures. The "whole content" is not just an amount. It's a full form capturing data about the recipient and the contribution.
More importantly, the caveat for budget says: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget". This document is exactly that: an authorization form for a contribution (expenditure) with an approval signature block.
> So Check 10 (form) is the correct label.
> Let's review the checks again.
Check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
This matches perfectly. "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", fields for Name, Address, Amount, Account Code, Check Payable to, Approved by (signatures).
> Runner-up: budget. Ruled out because it is an internal expenditure-authorization form with an approval block and no billable charges (vendor bill), which the check 7 caveat explicitly classifies as a form (check 10). Also, the content is not just an amount; it captures recipient details, account codes, etc.
> Final label: form.

---
### `test_imagesu_u_s_a_usa07d00_timo0000799.tif.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header block:** None. There is a top line "TOBACCO INSTITUTE ID 12-771-5334 SEP 21 '95 LITRG NO.001 P.02", but this looks like a Bates number/archive stamp or fax header, not a mail client header (From/To/Sent/Subject). Wait, let's look closer. "TOBACCO INSTITUTE ID 12-771-5334 SEP 21 '95 LITRG NO.001 P.02". This is archive metadata. No "From:", "To:", "Subject:".
- **Masthead/Running head:** Top line has "TOBACCO INSTITUTE", "ID 12-771-5334", "SEP 21 '95", "LITRG NO.001 P.02". Bottom has "Confidential Missouri Tobacco Litigation Case No. 972-1455" and "TIMO 0000799". This is not a newspaper/magazine masthead or a journal running head. It's legal/archive metadata.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a title "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", filled fields, signatures. It has real content.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: Most content is typed form fields with handwritten entries (Don Koller, address, amount 250.00, signatures). It's a filled form, not freeform handwriting on blank paper.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. The top line is archive metadata.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: Not a survey asking the reader to answer questions/rate. It's a request for a contribution.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: Not a CV/resume.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal name/volume/issue/page number on the page itself.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: There is an "Amount" field with "250.00". There is an "Account Code". There is "Check Payable to".
    *   Let's check the rules for Check 7.
    *   "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request..."
    *   "budget: ... a contribution/expenditure request or approval form whose whole content is an amount..." -> Wait, let's read carefully.
    *   "Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount... is budget, not invoice".
    *   Wait, let's look at the label "POLITICAL CAMPAIGN CONTRIBUTION REQUEST".
    *   It asks for a contribution of $250.00.
    *   Is it an invoice? No, it's not a vendor billing for goods/services.
    *   Is it a budget? "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
    *   Let's re-read Check 7 carefully.
    *   "budget: ... ALSO a provider's periodic customer statement... money PLANNING for future work is budget... a contribution/expenditure request or approval form whose whole content is an amount... is budget".
    *   Wait, is this a "contribution/expenditure request"? Yes, "POLITICAL CAMPAIGN CONTRIBUTION REQUEST".
    *   It has an amount ($250.00), account code, check payable to.
    *   It has "Approved by:" signatures (Regional Vice President, Senior Vice President).
    *   This looks like an internal approval form for a contribution.
    *   Let's check Check 10 (Administrative Form).
    *   "internal authorization/approval forms with an approval signature/date block." -> form.
    *   "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
    *   Ah! "authorizing a single expenditure is not planning or tracking money." -> form.
    *   Let's re-read the budget bullet: "ALSO a provider's periodic customer statement... money PLANNING for future work is budget... a contribution/expenditure request or approval form whose whole content is an amount... is budget".
    *   Wait, there's a conflict or specific condition.
    *   "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
    *   This page is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It has an amount ($250.00), account code, check payable to. It has approval signatures.
    *   Is it a "contribution/expenditure request or approval form whose whole content is an amount"? Yes.
    *   BUT the caveat says: "an internal expenditure-authorization form... with an approval signature/date block but no billable charges is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
    *   This page authorizes a single expenditure (contribution of $250). It is not tracking money or planning a budget. It's a request/approval for a specific payment.
    *   So it falls under Check 10: "internal authorization/approval forms with an approval signature/date block."
    *   Let's check the wording again. "a contribution/expenditure request or approval form whose whole content is an amount... is budget". This seems to refer to things like expense reports or budget requests.
    *   However, the caveat is very specific: "an internal expenditure-authorization form... with an approval signature/date block but no billable charges is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
    *   This page is exactly that: an authorization form for a contribution (expenditure). It has "Approved by:" with signatures.
    *   So it should be **form** (Check 10).
> Let's re-evaluate Check 7 vs Check 10.
Check 7 (budget): "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
Check 10 (form): "internal authorization/approval forms with an approval signature/date block."
Caveat in Check 7: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> This page is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It requests a contribution of $250. It has approval signatures. It authorizes a single expenditure. Therefore, per the caveat, it is a **form** (Check 10), not budget.
> Let's check if it could be an invoice.
"invoice: ... a payment voucher... a payment request...".
But the caveat says "authorizing a single expenditure is not planning or tracking money" -> form.
Wait, is a "payment request" an invoice?
"invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document..."
But the caveat specifically excludes "internal expenditure-authorization form... with an approval signature/date block but no billable charges" from budget, calling it a form.
Does the invoice definition cover this?
"invoice: an outside vendor, supplier, or agency states charges owed...". This is an internal request (Tobacco Institute requesting a contribution to Don Koller). It's not a vendor billing them.
So it's not an invoice.
> Is it a form?
Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
This page has:
- Title: POLITICAL CAMPAIGN CONTRIBUTION REQUEST
- Fields: Date, State, Recipient Information (Name, Address, Office, Party, Committees), Contribution Information (Amount, Account Code, Check Payable to, Address, Notes).
- Approval block: "Approved by:" with signatures for Regional VP and Senior VP.
- "Revised 2/95".
This is a classic internal authorization/approval form.
> So the label is **form**.
> Let's double check Check 7 budget definition.
"budget: ... a contribution/expenditure request or approval form whose whole content is an amount... is budget".
This is confusing. "whose whole content is an amount".
The page has recipient info, contribution info, approval block.
The caveat says: "an internal expenditure-authorization form ... with an approval signature/date block but no billable charges is a form (check 10), not budget".
This page has an approval signature block. It has no billable charges (it's a contribution, not a bill for goods).
So it is a form.
> Let's look at the labels again.
1. file_folder
2. handwritten
3. form (fax)
4. questionnaire
5. resume
6. scientific_publication
7. invoice or budget
8. specification
9. presentation
10. form (administrative)
11. correspondence
12. news_article
13. scientific_report
14. advertisement
> The label is "form".
> Let's trace the logic:
- Pre-scan: No mail header. No masthead. Top line is archive ID.
- Check 1: Not file_folder (has content).
- Check 2: Not handwritten (filled form).
- Check 3: Not fax sheet.
- Check 4: Not questionnaire.
- Check 5: Not resume.
- Check 6: Not scientific_publication.
- Check 7: Financial content? Yes, amount $250. But is it invoice or budget?
    - Invoice: No, not a vendor bill.
    - Budget: "contribution/expenditure request... is budget". BUT caveat: "internal expenditure-authorization form... with an approval signature/date block but no billable charges is a form (check 10), not budget". This page has approval signatures (Regional VP, Senior VP). It authorizes a single expenditure ($250 contribution). So it's not budget.
- Check 8: Not specification.
- Check 9: Not presentation.
- Check 10: Administrative form. "Filled or blank fields... internal authorization/approval forms with an approval signature/date block." This matches perfectly. The page is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST" form with fields filled in and approval signatures.
- Check 11: Not correspondence (no TO/FROM/RE memo header, no letter structure).
- Check 12: Not news_article.
- Check 13: Not scientific_report.
- Check 14: Not advertisement.
> Final decision: form.
> Wait, is there any other category?
"POLITICAL CAMPAIGN CONTRIBUTION REQUEST"
It's a form.
> Let's re-read the budget caveat carefully.
"Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
This page is a "CONTRIBUTION REQUEST" with "Approved by:" signatures. It authorizes a single expenditure ($250). So it is a form.
> The label is `form`.
> One detail: "A contribution/expenditure request or approval form whose whole content is an amount... is budget".
Does this page's "whole content" amount to just an amount? No, it has recipient info, account code, approval signatures.
The caveat is the key: "with an approval signature/date block but no billable charges is a form". This page has approval signatures.
> So, Check 10 is the match.
> Evidence for Check 10:
- Title: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST"
- Fields: Date, State, Recipient Information (Name, Address, etc.), Contribution Information (Amount, Account Code, Check Payable to).
- Approval block: "Approved by:" with lines for "Regional Vice President's signature" and "Senior Vice President's signature".
- Handwritten entries in fields (Don Koller, 250.00, etc.).
- This is a filled administrative form with an approval block.
> Runner-up: budget. Ruled out because the page is an internal expenditure-authorization form with an approval signature block authorizing a single expenditure ($250 contribution), not a budget tracking/planning document or a vendor invoice. The caveat in Check 7 explicitly states such forms are forms (check 10).
> Final check of the text:
"POLITICAL CAMPAIGN CONTRIBUTION REQUEST"
"Date: 6/4/96"
"Recipient Information" table.
"Contribution Information" table.
"Approved by:" signatures.
"Revised 2/95".
"Confidential Missouri Tobacco Litigation Case No. 972-1455".
> This is definitely a form.
> One small check: Is it a "questionnaire"? No.
Is it a "memo"? No.
> The label is `form`.

---
### `test_imagesu_u_s_a_usa07d00_timo0000799.tif.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking each condition in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "TOBACCO INSTITUTE ID 12-771-5334 SEP 21 '95 LITRG NO.001 P.02" at the top. This looks like archive metadata, not a journal masthead. Bottom: "Confidential Missouri Tobacco Litigation Case No. 972-1465 TIMO 000799". This is a Bates number and litigation stamp.
> **Check 1: file_folder**
- Evidence: The page has a title "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", filled fields, signatures. It has real content. Not file_folder.
> **Check 2: handwritten**
- Evidence: Most content is typed form fields with some handwritten entries (date, name, address, amount, signatures). Not majority handwritten.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax cover sheet header.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: Not a survey instrument.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: Not a resume.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No journal running head, volume, issue, page range.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". Contains "Amount 250.00", "Account Code 1701-7710-M001", "Check Payable to KOLLER for Rep".
- Wait, check 7 says: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
- Let's look at the document: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It has "Amount 250.00", "Account Code", "Check Payable to", "Approved by: (Regional Vice President's signature)", "(Senior Vice President's signature)".
- This is an internal authorization form for a contribution. It's not an invoice (no vendor selling goods/services). It's not a budget (not planning/tracking money, just authorizing a single expenditure).
- Check 10: "internal authorization/approval forms with an approval signature/date block" -> form.
- Let's re-read Check 7: "A contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category (amounts need not be legible). ALSO a provider's periodic customer statement... is budget, not invoice" -> Wait, "A contribution/expenditure request or approval form whose whole content is an amount... is budget". Let me re-read carefully.
- "budget: ... ALSO a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category (amounts need not be legible)." -> Wait, is a contribution request form a budget?
- Let's read Check 7 again: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category (amounts need not be legible)."
- Wait, the text says: "Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount... is budget".
- BUT Check 10 says: "internal authorization/approval forms with an approval signature/date block" is a form.
- Let's check the exact wording in Check 7: "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
- Ah! "an internal expenditure-authorization form ... with an approval signature/date block but no billable charges is a form (check 10), not budget".
- This document is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST" with "Amount 250.00", "Account Code", and "Approved by: (Regional Vice President's signature)". It has an approval signature block. It is authorizing a single expenditure (a contribution). Therefore, it is a form (check 10), not budget.
- Let's verify this. "A contribution/expenditure request or approval form whose whole content is an amount" is listed under budget. BUT the caveat says: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
- This document has an approval signature block ("Approved by: Regional Vice President's signature", "Senior Vice President's signature"). It is authorizing a single expenditure (250.00 contribution). So it falls under the caveat: it is a form (check 10).
> Let's check Check 10: "ADMINISTRATIVE FORM -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; ... internal authorization/approval forms with an approval signature/date block."
This perfectly matches "POLITICAL CAMPAIGN CONTRIBUTION REQUEST" with filled fields (Name, Address, Amount, Account Code) and an approval signature block.
> Let's double check Check 7 budget definition: "Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
Wait, if it's a "contribution/expenditure request or approval form whose whole content is an amount", is it budget or form?
The caveat in Check 7 says: "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
This document has an approval signature/date block (Revised 2/95, Approved by signatures). It is authorizing a single expenditure. So it is a form.
> Let's review the whole document:
Title: POLITICAL CAMPAIGN CONTRIBUTION REQUEST
Fields: Date, State/Local, Recipient Information (Name, Address, Current Office, Aspired Office, Party, Leadership Position, Committees), Contribution Information (Amount, Account Code, Check Payable to, Address, Notes).
Signatures: Approved by (Regional Vice President's signature), (Senior Vice President's signature).
Bottom: Confidential Missouri Tobacco Litigation Case No. 972-1465, TIMO 000799.
> This is clearly a filled administrative form.
> Check 1: file_folder - no, has real content.
Check 2: handwritten - no, mostly typed form with some handwriting.
Check 3: fax - no.
Check 4: questionnaire - no.
Check 5: resume - no.
Check 6: scientific_publication - no.
Check 7: financial - caveat applies, it's an internal authorization form with approval signatures, so it's a form, not budget.
Check 8: specification - no.
Check 9: presentation - no.
Check 10: form - yes, filled fields, boxes, internal authorization/approval form with approval signature block.
> Runner-up: budget. Ruled out because the document is an internal expenditure-authorization form with an approval signature block authorizing a single expenditure, which the check 7 caveat explicitly classifies as a form (check 10), not budget.
> Let's confirm the exact label: "form".
> Evidence for Check 10: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST" with filled fields (Name, Address, Amount, Account Code) and an "Approved by:" block with signature lines for Regional Vice President and Senior Vice President. This is an internal authorization/approval form with an approval signature/date block.
> Evidence against Check 7 (budget): Although it involves money (Amount 250.00), it is an internal expenditure-authorization form with an approval signature block authorizing a single expenditure, not planning or tracking money. The check 7 caveat explicitly states such forms are forms (check 10), not budget.
> Final label: form.

---
### `test_imagesu_u_s_a_usa07d00_timo0000799.tif.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- Mail-client header: None.
- Masthead/running head: "TOBACCO INSTITUTE ID 12-771-5334 SEP 21 '95 LITRG NO.001 P.02". This looks like internal filing metadata, not a journal masthead. "TIMO 0000799" and "Confidential Missouri Tobacco Litigation Case No. 972-1455" are Bates/litigation stamps.
> **2. Scratchpad checks:**
> *   **Check 1: file_folder**
    *   Evidence: The page has a title "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", filled fields, signatures. It has real content.
    *   Result: not this check.
> *   **Check 2: handwritten**
    *   Evidence: Most content is typed form fields with handwritten entries (Don Koller, address, amount 250.00). It's a filled form, not freeform handwriting on blank paper.
    *   Result: not this check.
> *   **Check 3: FAX TRANSMISSION SHEET**
    *   Evidence: No "FACSIMILE" header. The top line is internal metadata.
    *   Result: not this check.
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
    *   Evidence: Not a survey asking the reader to answer. It's a request for a contribution.
    *   Result: not this check.
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
    *   Evidence: Not a CV.
    *   Result: not this check.
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
    *   Evidence: No journal running head.
    *   Result: not this check.
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
    *   Evidence: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". Amount: 250.00. Account Code: 1701-7710-M001. Check Payable to: Koller to Rep.
    *   Wait, is this an invoice or budget?
    *   Check 7 says: "budget: internal money planning, tracking, or disbursement... Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
    *   "invoice: an outside vendor... states charges owed...". This is a request for a contribution, an internal approval form for a disbursement (contribution).
    *   Let's check the budget definition: "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
    *   Wait, let's look at Check 10: "internal authorization/approval forms with an approval signature/date block... is a form (check 10), not budget".
    *   Let's re-read Check 7 carefully: "Caveat: an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
    *   This page is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It has "Approved by:" with signatures. It is an authorization form for a contribution.
    *   Wait, is it a form or a budget?
    *   Check 7 budget definition: "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
    *   Check 10 form definition: "internal authorization/approval forms with an approval signature/date block... is a form (check 10), not budget".
    *   There is a conflict here. Let's look closely.
    *   Check 7: "budget: ... Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount...".
    *   Check 10: "internal authorization/approval forms with an approval signature/date block... is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
    *   Which one wins? The instructions say "Once an earlier check matches, later checks do not override it." But Check 7 and Check 10 are close.
    *   Actually, let's look at the structure. It has fields: Name, Address, Amount, Account Code, Approved by.
    *   Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
    *   Check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." BUT "Caveat: an internal expenditure-authorization form... is a form (check 10), not budget".
    *   This is an internal expenditure-authorization form (Contribution Request with approval signatures). So it should be form (check 10).
    *   Wait, let's re-read Check 7 budget: "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
    *   Let's re-read Check 10 form: "internal authorization/approval forms with an approval signature/date block... is a form (check 10), not budget".
    *   The caveat in Check 7 explicitly says: "an internal expenditure-authorization form... is a form (check 10), not budget". This page is exactly that: a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST" with "Approved by:" signatures. It authorizes a single expenditure (contribution).
    *   So Check 10 (form) is the correct match.
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 9: SLIDE DECK... -> presentation**
    *   Evidence: No.
    *   Result: not this check.
> *   **Check 10: ADMINISTRATIVE FORM -> form**
    *   Evidence: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". Fields: Date, State, Recipient Information (Name, Address, Current Office, etc.), Contribution Information (Amount, Account Code, Check Payable to, Address, Notes). Approval block: "Approved by: (Regional Vice President's signature), (Senior Vice President's signature)". "Revised 2/95".
    *   This is a filled form with fields, boxes, and an approval block.
    *   Result: yes.
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
> **Conclusion:**
The document is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST" form. It has filled fields (handwritten) and an approval block.
Check 7 caveat: "an internal expenditure-authorization form... is a form (check 10), not budget".
Check 10: "internal authorization/approval forms with an approval signature/date block... is a form".
So the label is `form`.
> Let's double check Check 7 vs Check 10.
Check 7 budget: "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
Check 10 form: "internal authorization/approval forms with an approval signature/date block... is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
The page has "Approved by:" with two signatures. It is authorizing a single expenditure (a $250 contribution). Therefore, it falls under the Check 10 form definition and the Check 7 caveat excludes it from budget.
> Final label: form.

---
### `test_imagesa_a_c_y_acy93e00_2040329511.tif.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. There is a Bates number "11/16/89" and "2040329151". No journal masthead.
> **Check 1: file_folder**
- Evidence: The page has a title "PRICE VALUE ESTIMATES" and a large data table with years (1983-1994) and various columns (INDUSTRY VOLUME, PM-USA PRICE VALUE, INDUSTRY PRICE VALUE, PM-USA SHARE OF CATEGORY). It has real content (a table of data).
- Not this check.
> **Check 2: handwritten**
- Evidence: The page is entirely typed/printed. No handwriting.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No biographical info.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range on the page itself.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: The table is titled "PRICE VALUE ESTIMATES". It contains columns for "YEAR", "INDUSTRY VOLUME++", "PM-USA PRICE VALUE" (% CHANGE, VOLUME+, SHARE, VS. YAG, DIFF), "INDUSTRY PRICE VALUE" (% CHANGE, VOLUME+, SHARE, VS. YAG, DIFF), "PM-USA SHARE OF CATEGORY" (SHARE, VS. YAG, DIFF). The values are in millions/billions (footnotes: *PROJECTIONS, +(MILLIONS), ++(BILLIONS)). This is a financial projection/forecast table. It's not an invoice (no vendor charges, no line items for goods sold). It looks like a budget or financial forecast/projection. Wait, let's look at check 7 carefully.
- "budget: internal money planning, tracking, or disbursement... forecast vs. actual... money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements... plans projected spend rather than billing completed work, so it is budget, not invoice".
- This table shows "PRICE VALUE ESTIMATES" with years 1983-1994, including projections for 1991-1994. It's a financial forecast/estimate. Is it a budget? Or is it a form? Or a presentation?
- Let's check check 9: presentation. "Slide/overhead layouts... a deck title or section-divider page... a near-blank cover...". This is a data table. "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." Wait, check 10 says "standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)... is a form".
- Let's re-read check 7: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This is a table of financial estimates/projections. Is it an invoice or budget? "budget: ... forecast vs. actual ... money PLANNING for future work is budget". This is a projection/estimate table. It fits "budget" better than "invoice" (which is for goods sold). Wait, is it a form?
- Let's look at check 10: "ADMINISTRATIVE FORM -> form. Filled or blank fields... A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)... is a form". This page is a standalone labeled data table ("PRICE VALUE ESTIMATES" with rows for years and columns for various metrics).
- Wait, check 7 says: "Money function overrides form layout... invoice: ... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number...". This is not an agency billing a client. It's an internal estimate of industry price values.
- Let's re-evaluate check 7 vs check 10.
- Check 7: "budget: internal money planning, tracking, or disbursement... forecast vs. actual...". This table is a forecast/estimate of price values and volumes. It's financial data. But is it a "budget"? A budget is usually internal money planning. This looks like a market forecast (industry volume, PM-USA share).
- Let's look at check 10 again: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)... is a form". The page is literally a table with rows (years) and columns (metrics). It has no fields to fill out (it's already filled with printed data). "A form does NOT have to be blank — a filled form recording data is still a form". But is a printed data table a form? "standalone labeled data chart or table... is a form".
- Wait, what about check 9? "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Let's check the labels again. Is there a better fit?
- The table is "PRICE VALUE ESTIMATES". It has years 1983-1994. Footnotes: *PROJECTIONS, +(MILLIONS), ++(BILLIONS). This is a financial projection table.
- Could it be a budget? "budget: ... forecast vs. actual ... money PLANNING for future work is budget". This is a projection of future values.
- Let's consider "form". Check 10: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values); a filled analytical or lab data sheet... is a form". This page is a labeled data table.
- Let's consider "scientific_report". No running prose.
- Let's consider "presentation". Check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." So it's not presentation.
- So it's either form or budget.
- Check 7: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This is a table of financial estimates. But is it an invoice or budget? "budget: ... forecast vs. actual ... money PLANNING for future work is budget". This is a projection (future work/planning). So it could be budget.
- However, check 10 explicitly says: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)... is a form". And check 9 says: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Wait, check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." This implies financial pages can be invoice/budget even if they look like forms. But this page is just a table. Is it a "line-item table, ledger, statement, voucher, or check face"? It's a table of estimates.
- Let's look at the "budget" definition again: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts... ALSO a provider's periodic customer statement... is budget, not invoice".
- This table is a forecast of "PRICE VALUE ESTIMATES" for the industry and PM-USA. It's not really an internal budget or expense report. It's a market analysis table.
- If it's not a budget (because it's not internal money planning, it's market data), and it's not an invoice (not a vendor bill), then check 7 doesn't apply.
- Then we fall to check 10: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)... is a form". The page is exactly this: a labeled data table with rows (years) and numeric values.
- Let's verify check 10: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values); a filled analytical or lab data sheet... is a form". Yes, this is a standalone labeled data table.
- Wait, is there any other category? "specification"? No. "email"? No.
- Let's re-read check 10 carefully. "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells. This also covers: ... A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
- The page is a table titled "PRICE VALUE ESTIMATES" with columns and rows of numbers. It fits "standalone labeled data chart or table".
- Therefore, form.
> Let's double check if it could be "budget".
"budget: ... forecast vs. actual ... money PLANNING for future work is budget". This is a projection of industry price values, not internal money planning. It's market data. So not budget.
"invoice: ... an outside vendor ... states charges owed". Not an invoice.
So check 7 is not a match.
> Check 10: "standalone labeled data chart or table ... is a form". This matches perfectly. The page is a table of data.
> Let's check if there's any other evidence.
The page has a Bates number "11/16/89" and "2040329151".
The title is "PRICE VALUE ESTIMATES".
It's a table.
Label: form.
> Wait, is there any possibility it's a "presentation"?
Check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." So definitely not presentation.
> Is there any possibility it's a "scientific_report"?
Check 13: "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report." This page has no running prose, just a table. So not scientific_report.
> So the label is "form".
> Let's review the scratchpad steps:
1. file_folder: no — page has a title "PRICE VALUE ESTIMATES" and a large data table with years and metrics, not just an identifier.
2. handwritten: no — entirely typed/printed.
3. fax: no — no fax header.
4. questionnaire: no — no survey questions.
5. resume: no — no biographical info.
6. scientific_publication: no — no journal identifier.
7. financial: no — not an invoice (no vendor charges) and not a budget (not internal money planning/expense tracking, it's a market forecast table of industry/PM-USA price values and volumes). Check 7 requires financial content to be the primary structure like a bill, ledger, or internal budget/forecast. This is a market data table. Wait, is a market forecast a budget? "money PLANNING for future work is budget". This is estimating future price values, not planning internal money. So check 7 doesn't fit well. Even if it did, check 10 explicitly covers "standalone labeled data chart or table". Let's assume check 7 is not the primary match because it's not a standard financial document (invoice/budget) but a data table. Actually, check 10 says "standalone labeled data chart or table ... is a form".
8. specification: no — no material safety data, product formulation, or "shall/must" language.
9. presentation: no — check 9 explicitly says "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
10. form: yes — the page is a standalone labeled data table ("PRICE VALUE ESTIMATES" with rows for years 1983-1994 and columns for volume, share, price value metrics). Check 10 covers "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)".
11. correspondence: no — no TO/FROM/RE header or letter structure.
12. news_article: no — no masthead or journalistic layout.
13. scientific_report: no — no running narrative prose, only a data table.
14. advertisement: no — no marketing layout, product imagery, or slogans.
> Runner-up: budget, ruled out because the table is a market forecast of industry/PM-USA price values and volumes, not an internal budget, expense report, or vendor invoice (check 7 requires financial content to be a bill, ledger, or internal money planning/tracking, whereas this is a standalone data table classified as form under check 10). Or runner-up: presentation, ruled out because check 9 explicitly states a standalone chart or table of values alone is a form, not a slide.
> I will go with form.

---
### `test_imagesu_u_s_a_usa07d00_timo0000799.tif.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "TOBACCO INSTITUTE ID 12-771-5334 SEP 21 '95 LITRG NO.001 P.02". This looks like an internal archive ID, not a journal masthead. "TIMO 0000799" at the bottom right. "Confidential Missouri Tobacco Litigation Case No. 972-1455" at the bottom left. No journal masthead.
> **Check 1: file_folder**
- Evidence: The page has a title "POLITICAL CAMPAIGN CONTRIBUTION REQUEST", filled fields, signatures. It has real content.
- Not this check.
> **Check 2: handwritten**
- Evidence: Most content is typed form fields with some handwritten entries (Date, Name, Address, Amount, signatures). Not majority handwritten.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: Not a survey instrument. It's a contribution request form.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: Not a resume.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal running head/volume/issue.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". Amount: 250.00. Account Code: 1701-7710-M001. Check Payable to: Koller to Rep.
- Is it an invoice or budget?
- "A contribution/expenditure request or approval form whose whole content is an amount, and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category (amounts need not be legible). ALSO a provider's periodic customer statement... is budget, not invoice"
- Wait, check 7 says: "budget: internal money planning, tracking, or disbursement ... Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
- This is a "CONTRIBUTION REQUEST" form. It requests a contribution of $250.00. It has an approval block ("Approved by: Regional Vice President's signature, Senior Vice President's signature").
- This is an internal expenditure request/approval form. Wait, check 7 says: "A contribution/expenditure request or approval form whose whole content is an amount... is budget".
- Let's re-read check 7 carefully: "budget: ... Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount...".
- Wait, is it a form (check 10) or budget (check 7)?
- Check 10: "internal authorization/approval forms with an approval signature/date block."
- Check 7 caveat: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
- Ah! "an internal expenditure-authorization form ... with an approval signature/date block but no billable charges) is a form (check 10), not budget".
- This is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST". It requests a contribution (expenditure) of $250. It has an approval block. It is an internal expenditure-authorization form. Therefore, it is a form (check 10), not budget.
- Let's check check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; ... internal authorization/approval forms with an approval signature/date block."
- Yes, this is a form.
> Let's double check check 7 vs check 10.
Check 7: "budget: ... a contribution/expenditure request or approval form whose whole content is an amount ... is budget". BUT caveat: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
This document is a "POLITICAL CAMPAIGN CONTRIBUTION REQUEST" with an approval block. It authorizes a single expenditure ($250). It is not tracking money or planning money (budget). It is an authorization form. So it falls under check 10 (form).
> Let's check check 10 again: "internal authorization/approval forms with an approval signature/date block." Yes, it has "Approved by:" with signatures.
> Let's review the whole page:
Title: POLITICAL CAMPAIGN CONTRIBUTION REQUEST
Fields: Date, State, Recipient Information (Name, Address, Current Office, etc.), Contribution Information (Amount, Account Code, Check Payable to, Address, Notes).
Approval block: Approved by: (Regional VP signature), (Senior VP signature).
Footer: Revised 2/95, Confidential Missouri Tobacco Litigation Case No. 972-1455, TIMO 0000799.
> This is clearly a filled form.
> Check 8: specification
- No.
> Check 9: presentation
- No.
> Check 10: ADMINISTRATIVE FORM -> form
- Evidence: Filled fields, boxes, checkboxes (State: Local), ruled entry lines, approval signature/date block ("Approved by:", signatures). Title "POLITICAL CAMPAIGN CONTRIBUTION REQUEST".
- This matches perfectly.
> Check 11: CORRESPONDENCE
- No.
> Check 12: news_article
- No.
> Check 13: scientific_report
- No.
> Check 14: advertisement
- No.
> So the label is "form".
> Let's quickly re-verify check 7 budget vs check 10 form.
Check 7 budget: "a contribution/expenditure request or approval form whose whole content is an amount... is budget".
Check 7 caveat: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
This document is a contribution request (expenditure authorization) with an approval signature block. It authorizes a single expenditure ($250). Thus, it is a form (check 10), not budget.
> Final check of the scratchpad steps:
1. file_folder: no - has real content (title, fields, signatures).
2. handwritten: no - mostly typed form with handwritten entries.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial (invoice/budget): no - it's an internal expenditure authorization form for a single contribution, which check 7 caveat explicitly routes to form (check 10).
8. specification: no.
9. presentation: no.
10. form: yes - filled fields, checkboxes, approval signature block.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no.
14. advertisement: no.
> Runner-up: budget, ruled out because the document is an internal expenditure-authorization form for a single contribution with an approval block, which check 7 explicitly classifies as a form (check 10) rather than budget (planning/tracking money).
> Looks solid.

---

## budget → invoice (4 errors)

### `test_imagest_t_q_i_tqi16e00_2040855570.tif.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow a specific set of checks in order, using a scratchpad to document my reasoning.
> **Document Analysis:**
- Header: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING"
- Title: "OUTDOOR ESTIMATE RECAP - ODO1(S)"
- Period: "01/01/94 TO 12/31/94"
- Date: "05/06/94"
- Client: "P.M. INC."
- Office: "10"
- Est No: "4155"
- Desc: "774A ODP B&H BUS SHELTERS"
- Table: "TOTALS BY PRODUCT/MONTH SHOWING DATE"
- Columns: PRODUCT, PERIOD, GROSS AMOUNT, GROSS CHANGE
- Rows: "12- B&H 85'S", JUN 1994 QUARTER 2, SEP QUARTER 3, OCT DEC QUARTER 4, TOTAL
- Values: 90,250.00, 59,800.00, 150,050.00, Total 330,550.00
- Bottom right: Bates number "204055570" (rotated)
- Bottom left: "FORM MO1A REV 04-14-83"
> **Pre-scan:**
- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: "LEO BURNETT U.S.A." is a company logo/header, not a newspaper/magazine masthead or journal running head.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a table with financial data, headers, etc. Not identifier-only.
- Result: not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Typed throughout.
- Result: not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Result: not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: Not a survey.
- Result: not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: Not a resume.
- Result: not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name/volume/issue/page number.
- Result: not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: "OUTDOOR ESTIMATE RECAP - ODO1(S)". Client: P.M. INC. Est No: 4155. Table shows "GROSS AMOUNT" and "GROSS CHANGE" for "BUS SHELTERS" (outdoor advertising). Total: 330,550.00.
- Let's look at the instructions for Check 7:
  - "budget: internal money planning, tracking, or disbursement... ALSO a provider's periodic customer statement... is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
  - "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
  - Wait, the text says: "an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
  - Let's re-read carefully: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
  - This page HAS an estimate number ("EST NO: 4155"). It lists charges/amounts ("GROSS AMOUNT" 330,550.00). It is for a client job ("CLIENT: P.M. INC.", "DESC: 774A ODP B&H BUS SHELTERS").
  - Wait, the example in the text says: "(e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
  - But then it says: "but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
  - This page has "EST NO: 4155", "CLIENT: P.M. INC.", "GROSS AMOUNT", "TOTAL 330,550.00". It lists charges and totals for a client job. Therefore, it is an invoice.
  - Let's re-read the invoice bullet: "invoice: ... an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement with unit prices, amounts, and totals. ... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
  - This page has "EST NO: 4155", "ESTIMATE RECAP", "CLIENT: P.M. INC.", "GROSS AMOUNT", "TOTAL 330,550.00". It is an estimate recap that names an estimate number and lists charges/amounts for a client job. Thus, it is an invoice.
> Let's double check.
Title: "OUTDOOR ESTIMATE RECAP - ODO1(S)"
"EST NO: 4155"
"CLIENT: P.M. INC."
"GROSS AMOUNT" ... "TOTAL 330,550.00"
This perfectly matches the invoice definition: "an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement with unit prices, amounts, and totals... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO")..."
> Runner-up: budget. Ruled out because the document names an estimate number ("EST NO: 4155") and lists charges/amounts for a client job ("CLIENT: P.M. INC."), making it an agency's bill (invoice) rather than just planning projected spend.
> Let's check check 10: ADMINISTRATIVE FORM -> form.
"A hand-plotted experimental GRAPH... is a research test result... not a form... It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
So check 7 overrides check 10.
> Final label: invoice.
> Let's review the scratchpad requirements:
- Walk checks 1-14 in order.
- Briefly state evidence or "none".
- If evidence present, STOP HERE.
- Keep each check's line short.
- Add one final line naming the runner-up label and the single piece of evidence that ruled it out.
> Check 1: file_folder - no — the page contains a financial table with headers, client info, and dollar amounts, not just an identifier/stamp.
Check 2: handwritten - no — the page is entirely typed.
Check 3: form (fax) - no — no fax cover sheet header.
Check 4: questionnaire - no — not a survey instrument.
Check 5: resume - no — not a career history.
Check 6: scientific_publication - no — no journal running head or publication identifier.
Check 7: invoice/budget - yes — titled "OUTDOOR ESTIMATE RECAP", names an estimate number ("EST NO: 4155"), lists a client ("P.M. INC."), and provides a table of gross amounts and totals ($330,550.00) for bus shelter ads; per check 7, an agency estimate recap that names an estimate number and lists charges for a client job is an invoice, not budget.
Runner-up: budget, ruled out because the page names an estimate number ("EST NO: 4155") and lists billable charges/amounts for a client job, which makes it an invoice (agency's bill) rather than a pure planning recap of projected spend.
> Wait, is there any other check?
Check 8: specification - no.
Check 9: presentation - no.
Check 10: form - no — check 7 overrides money records.
Check 11: correspondence - no.
Check 12: news_article - no.
Check 13: scientific_report - no.
Check 14: advertisement - no.
> The logic holds up perfectly.
Invoice is the correct label.

---
### `test_imagest_t_q_i_tqi16e00_2040855570.tif.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING". This is a company letterhead/logo, not a newspaper/magazine masthead or journal running head.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a table with "PRODUCT", "PERIOD", "GROSS AMOUNT", "GROSS CHANGE", "TOTALS BY PRODUCT/MONTH", "OUTDOOR ESTIMATE RECAP - ODO1(S)". It has real content (a financial table).
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Typed throughout. No majority handwriting.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
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
- Evidence: The page is titled "OUTDOOR ESTIMATE RECAP - ODO1(S)". It lists "CLIENT: P.M. INC.", "EST NO: 4155", "DESC: 774A ODP B&H BUS SHELTERS". It has a table with "PRODUCT", "PERIOD", "GROSS AMOUNT", "GROSS CHANGE", and a "TOTAL" of 330,550.00.
- Let's look at the rules for invoice vs budget.
- "invoice: ... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
- This page has "EST NO: 4155". It compares "GROSS AMOUNT" and "GROSS CHANGE". It has a total. This is an agency estimate/recap that bills a client job (names an estimate number, has gross amount and gross change columns). Wait, let's re-read carefully: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate...". This page has "EST NO: 4155". It has "GROSS AMOUNT" and "GROSS CHANGE". It is an estimate recap.
- Let's check the budget rule: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- This page has "EST NO: 4155". It has "GROSS AMOUNT" and "GROSS CHANGE". It lists amounts for JUN 1994, SEP, OCT, DEC. The period is "01/01/94 TO 12/31/94". The date is "05/06/94". It has an "EST NO". This matches the invoice bullet: "names an estimate number ("EST NO")... lists charges and totals for a client job". So it is an invoice.
- Wait, is it budget? "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
- Let's re-read the budget bullet: "an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- This page has "EST NO: 4155". It has "GROSS AMOUNT" and "GROSS CHANGE". The total is 330,550.00. This is an invoice.
> Let's double check.
Title: "OUTDOOR ESTIMATE RECAP - ODO1(S)"
Header: "CLIENT: P.M. INC. OFFICE: 10 DESC: 774A ODP B&H BUS SHELTERS"
"EST NO: 4155"
Table: PRODUCT, PERIOD, GROSS AMOUNT, GROSS CHANGE.
TOTAL: 330,550.00.
This is an estimate recap that names an estimate number ("EST NO: 4155") and lists charges/amounts (Gross Amount, Gross Change, Total). According to the rules, this is an invoice.
> Let's check check 10 just in case.
**Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: It has a form number at the bottom left "FORM MO1A REV 04-14-83". But check 7 says "Money function overrides form layout. ... A billing or payment page stays financial even when it is printed on a form with fields and approval blocks." and "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
- So check 7 overrides check 10.
> Let's confirm the invoice classification.
"invoice: ... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
This page has "EST NO: 4155" and compares "GROSS AMOUNT" and "GROSS CHANGE". It is an invoice.
> Runner-up: budget. Ruled out because the document names an estimate number ("EST NO: 4155") and has "GROSS AMOUNT" / "GROSS CHANGE" columns with a total, which makes it an agency's bill for a client job (invoice) rather than just planning future spend.
> Let's review the scratchpad steps.
1. file_folder: no — page has a financial table with product, period, amounts, not just an identifier.
2. handwritten: no — typed throughout.
3. fax: no — no fax header.
4. questionnaire: no — not a survey.
5. resume: no — not a career history.
6. scientific_publication: no — no journal identifier.
7. financial (invoice): yes — "OUTDOOR ESTIMATE RECAP" with "EST NO: 4155", "GROSS AMOUNT", "GROSS CHANGE", and a total of $330,550.00. Per check 7, an agency estimate/recap that names an estimate number and lists charges/amounts is an invoice, not budget.
8. specification: no — not an MSDS or product formulation.
9. presentation: no — not a slide deck or cover.
10. form: no — although it has "FORM MO1A" at the bottom, check 7 says money function overrides form layout for billing documents.
11. correspondence: no — no TO/FROM/RE memo header or letter structure.
12. news_article: no — no newspaper/magazine masthead.
13. scientific_report: no — no running narrative prose.
14. advertisement: no — not a promotional layout.
> Final label: invoice.
Wait, let's re-read the budget vs invoice rule carefully.
"an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
> This page:
- Title: "OUTDOOR ESTIMATE RECAP - ODO1(S)"
- "EST NO: 4155" -> names an estimate number.
- "GROSS AMOUNT" and "GROSS CHANGE" -> lists charges/amounts.
- Total: 330,550.00.
This perfectly matches the invoice bullet: "names an estimate number ("EST NO")... lists charges and totals for a client job is the agency's bill (invoice)."
> Therefore, invoice is correct.
The form number "FORM MO1A REV 04-14-83" at the bottom left is just the form template number, but the content is financial billing. Check 7 overrides check 10.
> I will write the scratchpad and output the label.

---
### `test_imagest_t_q_i_tqi16e00_2040855570.tif.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> Document analysis:
Header: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING"
Title: "OUTDOOR ESTIMATE RECAP - ODO1(S)"
Period: "01/01/94 TO 12/31/94"
Date: "05/06/94"
Page: "1"
Client: "P.M. INC."
Office: "10"
Desc: "774A ODP B&H BUS SHELTERS"
Est No: "4155"
> Table: "TOTALS BY PRODUCT/MONTH SHOWING DATE"
Columns: PRODUCT, PERIOD, GROSS AMOUNT, GROSS CHANGE
Rows:
12- B&H 85'S
JUN 1994 QUARTER 2: 90,250.00 / 90,250.00
SEP QUARTER 3: 90,250.00 / 90,250.00
OCT: 90,250.00 / 90,250.00
DEC: 59,800.00 / 59,800.00
QUARTER 4: 150,050.00 / 150,050.00
TOTAL: 330,550.00 / 330,550.00
> Footer: "FORM MO1A REV 04-14-83"
Bates number: "204055570"
> Let's go through the checks.
> Check 1: file_folder. No, has real content (table, title).
Check 2: handwritten. No, typed.
Check 3: FAX. No.
Check 4: questionnaire. No.
Check 5: resume. No.
Check 6: scientific_publication. No.
Check 7: financial document -> invoice or budget.
Title: "OUTDOOR ESTIMATE RECAP - ODO1(S)"
"EST NO: 4155"
"DESC: 774A ODP B&H BUS SHELTERS"
Table shows "GROSS AMOUNT" and "GROSS CHANGE".
Wait, check 7 says:
"budget: ... money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
> Wait, this document has:
- "EST NO: 4155" (names an estimate number)
- "GROSS AMOUNT" and "GROSS CHANGE" columns.
- "TOTALS BY PRODUCT/MONTH"
Is it billing completed work or planning future work?
"PERIOD 01/01/94 TO 12/31/94"
"JUN 1994 QUARTER 2", "SEP QUARTER 3", "OCT", "DEC QUARTER 4". Date is "05/06/94".
So it's planning for future quarters (Q2, Q3, Q4 of 1994, while date is May 1994).
Wait, "GROSS CHANGE" column.
Let's re-read check 7 carefully:
"budget: ... money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
> Wait, the example in the prompt for budget says:
"(e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice"
This document is EXACTLY that: "OUTDOOR ESTIMATE RECAP", "DESC: 774A ODP B&H BUS SHELTERS", "JUN 1994 QUARTER 2", "SEP QUARTER 3", "OCT", "DEC QUARTER 4". Date is 05/06/94. It is planning upcoming placements (Q2, Q3, Q4 1994).
Even though it has "EST NO: 4155", the rule says: "an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
Wait, the rule says "no estimate number... so it is budget". But then it says "but see the invoice bullet — an estimate/recap/change order that names an estimate number... is the agency's bill (invoice)."
This is a bit contradictory. Let's read closely:
"money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
> Ah! The example "(e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter)" is explicitly given as an example of BUDGET.
This document has:
Title: "OUTDOOR ESTIMATE RECAP - ODO1(S)"
Desc: "774A ODP B&H BUS SHELTERS"
Period: "01/01/94 TO 12/31/94"
Date: "05/06/94"
Rows: JUN 1994 QUARTER 2, SEP QUARTER 3, OCT, DEC QUARTER 4.
This is exactly "an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter".
Therefore, it is BUDGET.
> Let's double check.
Is there any "revises a prior estimate" or "prior adjustments"? No.
"GROSS AMOUNT" and "GROSS CHANGE" columns. "GROSS CHANGE" might mean the change from a previous estimate, but there's no prior estimate listed here, just the current planned amounts.
The text says: "(e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
This matches perfectly.
> Let's check check 10: form. "FORM MO1A REV 04-14-83" is at the bottom. But check 7 says "Money function overrides form layout... A provider's periodic customer statement... is budget, not invoice". And "money PLANNING for future work is budget". So check 7 applies.
> Let's review the checks:
1. file_folder: no
2. handwritten: no
3. FAX: no
4. questionnaire: no
5. resume: no
6. scientific_publication: no
7. financial document -> budget. Yes, "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing planned gross amounts by future quarter (Q2, Q3, Q4 1994, dated 05/06/94). This is explicitly called out as budget in the instructions.
8. specification: no
9. presentation: no
10. form: no (check 7 overrides)
11. correspondence: no
12. news_article: no
13. scientific_report: no
14. advertisement: no
> Runner-up: invoice. Ruled out because the document is an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys for future quarters (Q2-Q4 1994) showing only planned gross amounts, which the instructions explicitly classify as budget (planning projected spend) rather than invoice (billing completed work).
> Wait, the prompt says:
"budget: ... money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
> The document has "EST NO: 4155". Does naming an estimate number make it invoice?
"an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
But the example for budget explicitly says: "(e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
The document has "EST NO: 4155" AND it is an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter.
Which rule takes precedence? The example is very specific: "(e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter)". This document is literally that example. The presence of "EST NO: 4155" might just be a standard field on the form ("FORM MO1A REV 04-14-83"). The core function is planning future spend. The example explicitly uses this exact title and description to illustrate BUDGET. I will go with budget.
> Let's re-read carefully:
"money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
> If it names an estimate number, the invoice bullet says it's an invoice.
"an estimate/recap/change order that names an estimate number... is the agency's bill (invoice)."
This document HAS "EST NO: 4155".
So it names an estimate number.
Does it "revises a prior estimate"? It has a "GROSS CHANGE" column.
Does it "reconciles prior adjustments"? No.
Does it "list charges and totals for a client job"? It lists "GROSS AMOUNT" and "TOTAL" 330,550.00.
Wait, if it names an estimate number, it falls under the invoice bullet.
But the budget bullet says: "an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number... (e.g. an "OUTDOOR ESTIMATE RECAP"...)".
This is a classic conflict in the prompt's instructions. Let's look at the wording:
"an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice"
The example is in parentheses, illustrating the condition "ONLY plans upcoming placements — no estimate number...". If it HAS an estimate number, it might not fit the "no estimate number" condition, thus falling to the invoice bullet.
"but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
This document has "EST NO: 4155". It has "GROSS CHANGE". It has "TOTAL" 330,550.00.
Actually, if it's an estimate recap for an advertising agency (Leo Burnett), it's a budget/planning document for the client (P.M. Inc.). Advertising estimates are typically budgets for the client's planned spend. The invoice bullet is for "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... an agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
> Wait! "an agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO")..."
This document HAS "EST NO: 4155".
Therefore, by this explicit rule, it is INVOICE.
Let's re-read: "an agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
> Yes! The rule explicitly says: "when it names an estimate number ("EST NO")... [it is] invoice, not budget".
This document has "EST NO: 4155".
So it is INVOICE.
> Let's check the budget example again: "(e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
This example is for a recap that does NOT have an estimate number, does NOT revise, etc.
Our document HAS "EST NO: 4155". So it triggers the invoice rule.
Also, it has "GROSS CHANGE" column, which might imply revision, but the "EST NO" is the key trigger mentioned in the text: 'when it names an estimate number ("EST NO")... is the agency's bill (invoice)'.
> So the label is invoice.
> Let's verify:
Check 7: financial document.
invoice: "an agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO")..."
Evidence: "EST NO: 4155" is present. Title is "OUTDOOR ESTIMATE RECAP". Client is "P.M. INC.". It lists gross amounts totaling $330,550.00.
Therefore, invoice.
> Runner-up: budget. Ruled out because although it is an "OUTDOOR ESTIMATE RECAP" of planned ad buys, it explicitly names an estimate number ("EST NO: 4155"), which per the instructions makes an agency estimate/recap an invoice (the agency's bill for a client job) rather than a budget (planning projected spend).
> Let's do a quick final check of the text:
"CLIENT: P.M. INC."
"EST NO: 4155"
"OUTDOOR ESTIMATE RECAP - ODO1(S)"
"TOTALS BY PRODUCT/MONTH"
"TOTAL 330,550.00"
This is an invoice (agency bill for a client job).
> Check 1-6: no.
Check 7: invoice.
Check 8-14: no.
> Final label: invoice.

---
### `test_imagest_t_q_i_tqi16e00_2040855570.tif.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, walking through checks 1-14 in order.
> **Pre-scan:**
- Mail-client header block: None.
- Masthead or running head: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING". This is a company letterhead/header, not a newspaper/magazine masthead or journal running head.
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
- Evidence: The page has a table with "PRODUCT", "PERIOD", "GROSS AMOUNT", "GROSS CHANGE", "TOTALS BY PRODUCT/MONTH", "EST NO: 4155", "CLIENT: P.M. INC.", "DESC: 774A ODP B&H BUS SHELTERS". It has real content (a financial table).
- Not this check.
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
- Evidence: Typed text throughout. No majority handwriting.
- Not this check.
> **Check 3: FAX TRANSMISSION SHEET -> form**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions, rating scales, or transmittal note about a survey.
- Not this check.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No biographical info.
- Not this check.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range, DOI.
- Not this check.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: "OUTDOOR ESTIMATE RECAP - ODO1(S)", "PERIOD 01/01/94 TO 12/31/94", "DATE 05/06/94", "EST NO: 4155", "CLIENT: P.M. INC.", "DESC: 774A ODP B&H BUS SHELTERS", "TOTALS BY PRODUCT/MONTH", table with "PRODUCT", "PERIOD", "GROSS AMOUNT", "GROSS CHANGE", "TOTAL 330,550.00".
- Let's look at the invoice vs budget rules in Check 7.
- "invoice: ... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
- Wait, the title is "ESTIMATE RECAP". Does it have an estimate number? Yes, "EST NO: 4155".
- Does it compare original vs present/revised? It has "GROSS AMOUNT" and "GROSS CHANGE".
- Let's re-read the budget rule: "Also a provider's periodic customer statement... is budget, not invoice... Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- Wait, the example in the budget bullet says: "(e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
- Let's look at the document: "OUTDOOR ESTIMATE RECAP - ODO1(S)", "PERIOD 01/01/94 TO 12/31/94", "DATE 05/06/94", "EST NO: 4155", "CLIENT: P.M. INC.", "DESC: 774A ODP B&H BUS SHELTERS".
- Table: "TOTALS BY PRODUCT/MONTH", "SHOWING DATE", "PRODUCT 12- B&H 85'S", "PERIOD JUN 1994 QUARTER 2", "GROSS AMOUNT 90,250.00", "GROSS CHANGE 90,250.00".
- This is an "OUTDOOR ESTIMATE RECAP" of bus-shelter ad buys. It has "EST NO: 4155".
- Wait, the rule says: "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." and "an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- BUT the budget bullet specifically says: "(e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
- Let's look closely at the table: "JUN 1994 QUARTER 2", "SEP QUARTER 3", "OCT DEC QUARTER 4". These are future quarters relative to the date "05/06/94". The period is "01/01/94 TO 12/31/94". This is planning projected spend for the year 1994. It shows "GROSS AMOUNT" and "GROSS CHANGE". It does not show "actual charges and totals owed" for completed work, it shows planned gross amounts.
- Wait, the invoice bullet says: "when it names an estimate number ("EST NO")... the word "estimate" in the title does NOT make it budget."
- Let's re-read carefully: "Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- This document has "EST NO: 4155". It is an "ESTIMATE RECAP". It lists "GROSS AMOUNT" and "GROSS CHANGE". Is it billing completed work or planning? The period is 01/01/94 to 12/31/94, date is 05/06/94. It's planning for the rest of the year. But it has an EST NO.
- Actually, let's look at the exact wording: "an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type... (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend... so it is budget". This example matches the document perfectly: "OUTDOOR ESTIMATE RECAP", "bus-shelter ad buys" (DESC: 774A ODP B&H BUS SHELTERS), "showing only planned gross amounts" (GROSS AMOUNT). The fact that it has "EST NO: 4155" might be a trap, or the rule says "no estimate number... (e.g. an OUTDOOR ESTIMATE RECAP...)". Wait, if it has an estimate number, does it become an invoice? "but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- Does this document "revises a prior estimate"? It has a "GROSS CHANGE" column. "GROSS AMOUNT" vs "GROSS CHANGE". This implies it's revising or comparing.
- Let's re-read the invoice bullet: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
- This document has "EST NO: 4155". It has "GROSS AMOUNT" and "GROSS CHANGE" (comparing original vs present/revised). Therefore, it is an invoice.
- Wait, the budget bullet says: "an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- The document has "EST NO: 4155". It has "GROSS CHANGE". This means it's not "ONLY plans... no estimate number". It names an estimate number. Thus, it falls under the invoice bullet.
- Let's check the labels: invoice or budget. I will go with budget because the example in the budget bullet is EXACTLY this document: "(e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter)". The document is literally an "OUTDOOR ESTIMATE RECAP" of "BUS SHELTERS" showing "GROSS AMOUNT". The "EST NO: 4155" is present, but the example explicitly uses this exact scenario to illustrate BUDGET. Wait, the example says "no estimate number... (e.g. an OUTDOOR ESTIMATE RECAP...)". This implies the example assumes NO estimate number. But this document HAS "EST NO: 4155".
- Let's re-read: "Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice; but see the invoice bullet — an estimate/recap/change order that names an estimate number, revises a prior estimate, reconciles prior adjustments, or lists charges and totals for a client job is the agency's bill (invoice)."
- If it names an estimate number ("EST NO: 4155"), it triggers the invoice bullet: "an estimate/recap/change order that names an estimate number... is the agency's bill (invoice)."
- Let's look at the columns: "GROSS AMOUNT" and "GROSS CHANGE". This is comparing original vs revised. "GROSS AMOUNT" is the original estimate, "GROSS CHANGE" is the revised amount (which happens to be the same here, 90,250.00). This is "comparing original vs. present/revised estimate columns". This explicitly triggers the invoice bullet.
- Therefore, it is an invoice.
> Let's double check.
Title: "OUTDOOR ESTIMATE RECAP - ODO1(S)"
Fields: "EST NO: 4155", "CLIENT: P.M. INC.", "DESC: 774A ODP B&H BUS SHELTERS"
Table: "PRODUCT", "PERIOD", "GROSS AMOUNT", "GROSS CHANGE", "TOTAL"
This matches "names an estimate number ("EST NO")" and "compares original vs. present/revised estimate columns" (Gross Amount vs Gross Change).
So it is an invoice.
> Wait, is there any other check?
Check 10: ADMINISTRATIVE FORM -> form. "A hand-plotted experimental GRAPH... is scientific_report... It does NOT cover money records: billing documents are invoice (check 7)". So check 7 overrides check 10.
> Let's review the invoice vs budget rule again to be absolutely sure.
"invoice: ... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
This document has "EST NO: 4155" and columns "GROSS AMOUNT" and "GROSS CHANGE" (original vs revised). It is an invoice.
> Let's check if there's any other evidence.
"FORM MO1A REV 04-14-83" at the bottom left. This is a form number, but check 7 says "Money function overrides form layout." and "billing documents are invoice (check 7), and money-only forms are budget (check 7)."
> So the label is invoice.
> Let's do a quick pass of other checks just in case.
1. file_folder: no, has table.
2. handwritten: no.
3. fax: no.
4. questionnaire: no.
5. resume: no.
6. scientific_publication: no.
7. financial: yes, invoice.
8. specification: no.
9. presentation: no.
10. form: overridden by 7.
11. correspondence: no.
12. news_article: no.
13. scientific_report: no.
14. advertisement: no.
> Final check of the text:
"LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING"
"OUTDOOR ESTIMATE RECAP - ODO1(S)"
"PERIOD 01/01/94 TO 12/31/94" "DATE 05/06/94" "PAGE 1"
"CLIENT: P.M. INC." "OFFICE: 10" "DESC: 774A ODP B&H BUS SHELTERS"
"EST NO: 4155"
"TOTALS BY PRODUCT/MONTH"
"SHOWING DATE"
"PRODUCT" "PERIOD" "GROSS AMOUNT" "GROSS CHANGE"
"12- B&H 85'S" "JUN 1994 QUARTER 2" "90,250.00" "90,250.00"
...
"TOTAL" "330,550.00" "330,550.00"
> This is an agency estimate recap that names an estimate number ("EST NO: 4155") and compares original vs. present/revised estimate columns ("GROSS AMOUNT" vs "GROSS CHANGE"). According to the rules, this is an invoice, not a budget. The budget rule's example ("OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys) applies when there is NO estimate number and NO revision lines. Here, we have both.
> Therefore, invoice.

---

## letter → memo (2 errors)

### `test_imagesc_c_p_t_cpt85d00_503616995.tif.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow a specific scratchpad procedure, checking 1-14 in order.
> **Document Analysis:**
- Date: "September 10, 1975" at the top right.
- Addressee: "Mr. T. E. Sandefur:"
- Body: "As requested, this will provide you with my comments on Harry Christopher's observations relative to the Hawaii market." followed by numbered points (1-5).
- Content: Discusses marketing plans for "MORE" and "SALEM" cigarettes in Hawaii, mentioning magazines, Parade, taxi exposures, billboard, Aloha Stadium, Kool brand, surfboard self-liquidator, etc.
- Bottom right: Bates number "50361 6995".
> **Pre-scan:**
- Mail-client header block? No.
- Fax transmission header? No.
- Masthead/running head? No.
> **Check 1: file_folder**
- Evidence: No. The page has a date, addressee, and substantial body text (numbered paragraphs). Not just an identifier/stamp.
> **Check 2: handwritten**
- Evidence: No. The text is typed (typewriter font).
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No. No "FACSIMILE" header.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No. Not a survey instrument.
> **Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No. Not a CV/resume.
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No. No journal masthead, volume, issue, page range.
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No. Mentions "effort", "costs" implicitly, but no line-item table, ledger, or financial statement structure. It's a memo about marketing plans.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: No. Not an MSDS, product formulation, or "shall/must" requirement.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
- Evidence: No. Dense text, numbered paragraphs, not sparse slide layout.
> **Check 10: ADMINISTRATIVE FORM -> form**
- Evidence: No. No fields, boxes, checkboxes, ruled entry lines for capturing data. It's a typed letter/memo.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Evidence: Yes.
- "September 10, 1975" (date)
- "Mr. T. E. Sandefur:" (addressee)
- "As requested, this will provide you with my comments..." (prose body)
- Numbered points (1-5).
- No external address block like a formal letter with "Dear Mr. Sandefur" and closing signature, but it fits the memo definition: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo". Wait, is it a memo or a letter?
- Let's check the memo definition: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels".
- Here we have: Date "September 10, 1975", Addressee "Mr. T. E. Sandefur:", Body text. No "Dear...", no closing signature visible (maybe cut off, but looks like a standard internal memo/note).
- Let's check letter definition: "letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."
- Is Mr. T. E. Sandefur external? The text says "As requested, this will provide you with my comments on Harry Christopher's observations relative to the Hawaii market." This sounds like an internal communication between colleagues (e.g., at R.J. Reynolds or Philip Morris, given the brand names MORE, SALEM, Kool, Aloha Stadium). T.E. Sandefur was an internal executive at R.J. Reynolds (or similar). Even if external, the lack of "Dear..." and closing signature, plus the internal-sounding content ("our black ethnic efforts", "our market position"), strongly points to memo.
- Actually, let's look at the memo bullet: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo even without literal 'TO:/FROM:' labels". Here we have "Mr. T. E. Sandefur:" and date. It's a memo.
- Wait, is it a letter? "a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block." If Sandefur is external, it's a letter. But the content "our black ethnic efforts", "our market position" implies internal. Also, no closing signature. Memos often lack closing signatures. Letters usually have "Sincerely, [Name]". This page ends at paragraph 5. It looks like a memo.
- Let's re-read check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo".
- This page has date, addressee name, prose body, no salutation, no closing. It fits memo perfectly.
> **Check 12: PUBLISHED JOURNALISM -> news_article**
- Evidence: No.
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
- Evidence: No. Not running narrative prose about objectives/methods/results of a study. It's business commentary.
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
- Evidence: No.
> **Conclusion:**
The document is a memo. Date, addressee, internal prose, no salutation/closing.
> Let's double check letter vs memo.
Letter: "letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."
Memo: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo".
> The text says "our black ethnic efforts", "our market position". This is internal. So it's a memo.
> Final check of the text:
"September 10, 1975"
"Mr. T. E. Sandefur:"
"As requested, this will provide you with my comments on Harry Christopher's observations relative to the Hawaii market."
1. ...
2. ...
3. ...
4. ...
5. ...
Ends with "We should probably check on the success of the Kool Snark promotion of two years ago."
Bates number 50361 6995.
> This is a classic internal memo.
> Label: memo.

---
### `test_imagesc_c_p_t_cpt85d00_503616995.tif.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.
> **Document Analysis:**
- Date: "September 10, 1975" at the top right.
- Addressee: "Mr. T. E. Sandefur:"
- Body: "As requested, this will provide you with my comments on Harry Christopher's observations relative to the Hawaii market." followed by numbered points (1-5).
- Content: Discusses marketing plans, MORE brand, SALEM brand, Kool brand, Hawaii market, Aloha Stadium, surfboards, etc.
- Bottom right: Bates number "50361 6995".
> **Pre-scan:**
- Mail-client header block? No.
- Masthead/running head? No. Just a date and a Bates number.
> **Check 1: file_folder**
- Evidence: No. It has a full letter/memo body with numbered points. Not just an identifier/stamp.
> **Check 2: handwritten**
- Evidence: No. Typed text.
> **Check 3: FAX TRANSMISSION SHEET**
- Evidence: No.
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
- Evidence: No.
> **Check 5: PERSON'S CAREER HISTORY**
- Evidence: No.
> **Check 6: PUBLISHED EVIDENCE**
- Evidence: No. No journal name, volume, issue, page range, DOI.
> **Check 7: FINANCIAL DOCUMENT**
- Evidence: No. No line-item table, ledger, statement, voucher, check face. Mentions "effort", "costs" implicitly but not financial structure.
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
- Evidence: No.
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
- Evidence: No. Dense text, numbered paragraphs. Not sparse slide layout.
> **Check 10: ADMINISTRATIVE FORM**
- Evidence: No. No fields, boxes, checkboxes.
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
- Email: No mail-client header.
- Memo: Internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block?
  - Wait, let's look at the header: "September 10, 1975" and "Mr. T. E. Sandefur:".
  - The text says: "As requested, this will provide you with my comments on Harry Christopher's observations relative to the Hawaii market."
  - Is this a memo or a letter?
  - Memo definition: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose. OR a dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo.
  - Letter definition: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature. OR a dated note addressed to a named EXTERNAL person with prose and no TO:/FROM: block.
  - Who is Mr. T. E. Sandefur? Internal or external?
  - The text mentions "our black ethnic efforts", "our market position", "we should plan". This implies the sender and recipient are in the same organization (internal).
  - "Mr. T. E. Sandefur" is addressed directly. No "Dear Mr. Sandefur". No closing signature visible (maybe cut off, but looks like a standard internal memo format).
  - Let's check the memo rule: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."
  - Here we have "September 10, 1975" (date) and "Mr. T. E. Sandefur:" (internal name). The prose is "As requested, this will provide you with my comments...". This is memo-style prose. No external address, no "Dear...", no closing signature.
  - Therefore, it is a memo.
> Let's double check letter vs memo.
- Letter: external recipient address, "Dear ...", closing signature.
- Memo: internal, TO/FROM/RE or just name + date + prose.
- The addressee is "Mr. T. E. Sandefur". The text uses "we", "our", "my comments". This is internal correspondence.
- It fits the memo definition: "A dated internal note addressed to a named person by NAME ... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo".
> **Check 12: PUBLISHED JOURNALISM**
- Evidence: No.
> **Check 13: ORIGINAL RESEARCH WRITE-UP**
- Evidence: No. It's a memo about marketing observations, not a scientific research write-up with objectives, methods, results.
> **Check 14: PROMOTIONAL MATERIAL**
- Evidence: No.
> **Conclusion:**
The document is a memo. It's a dated internal note to Mr. T. E. Sandefur discussing marketing plans for the Hawaii market.
> Let's re-read the memo definition carefully:
"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation). Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."
> The page has:
- Date: September 10, 1975
- Addressee: Mr. T. E. Sandefur:
- Prose: "As requested, this will provide you with my comments..."
- No "Dear ...", no external address, no closing signature.
- Content is internal ("our market", "we should plan").
> This is a memo.
> Runner-up: letter. Ruled out because there is no external address, no "Dear ..." salutation, and the content is clearly internal ("our market", "we should plan"), fitting the memo definition for a dated internal note addressed by name.
> Final check of the text:
"September 10, 1975"
"Mr. T. E. Sandefur:"
"As requested, this will provide you with my comments on Harry Christopher's observations relative to the Hawaii market."
Numbered points 1-5.
Bates number 50361 6995.
> This is a classic internal memo.
> Label: memo.

---

## form → presentation (1 errors)

### `test_imagesj_j_e_d_jed71e00_03701993_03702011.tif.png`
**Expected:** `form` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> **1. Pre-scan:**
- **Mail-client header:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a Bates number "03701993" on the right side.
> **2. Scratchpad procedure:**
> *   **Check 1: file_folder**
    *   Evidence: There is a large black rectangular area (looks like a photographed slide or a dark background). On the left, there is a vertical strip of text/numbers. Wait, let's look closer.
    *   There is a vertical text "CHAP 7" and "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z". Wait, it looks like a chart or a table.
    *   Let's look at the numbers: "1 2 3 4 5 6 7 8 9 0". It looks like a column of numbers.
    *   There is a large black block. This looks like a photographic slide or a scan artifact.
    *   Wait, let's look at the layout. It's a vertical strip on the left with letters A-Z and numbers. Then a large black block.
    *   Is this a folder tab? No, it doesn't look like a folder tab. A folder tab is a protruding piece of cardboard. This looks like a slide mount or a photograph of a slide.
    *   Wait, look at the bottom right: "03701993". This is a Bates number.
    *   Look at the left side: "CHAP 7", then letters A-Z vertically. Then numbers.
    *   Look at the bottom: "CH...", "USE...", "MADE...".
    *   This looks like a slide. "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
    *   Wait, the black area is huge. It takes up most of the right side.
    *   Let's re-read Check 9: "photographic slide image (including a blurred or low-quality photo of a slide, chart, or scene)... Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
    *   Here, there is a large black block. The text is on the left.
    *   Wait, is this a folder tab? "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body. The label IS filing metadata... The black bar is the photographed folder body/tab edge".
    *   Let's look at the shape. The black area is a large rectangle. The text is on a white strip to the left.
    *   The text says "CHAP 7", then "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z" vertically. And numbers next to it.
    *   This looks like a chart or a key.
    *   Wait, look at the bottom left: "117.5", "117.5".
    *   Look at the bottom of the white strip: "CH...", "USE...", "MADE...".
    *   This looks like a slide from a presentation. A slide showing a chart or a key.
    *   Let's check Check 1 again: "A page is NOT file_folder if it carries any real content — a photograph or slide image... or a bold headline title... A prominent topical heading always counts as real content".
    *   "CHAP 7" is a heading. "A B C..." is content.
    *   Is it a folder tab? A folder tab usually has a short label like "NEWTROL" or "Litigation Content". This has "CHAP 7" and a list of letters. This is content.
    *   So it's not file_folder.
> *   **Check 2: handwritten**
    *   Evidence: The text looks typed (monospaced font for numbers and letters). "CHAP 7", "A B C...". The numbers look like a computer printout or a slide text. Not majority handwritten.
> *   **Check 3: FAX**
    *   Evidence: No fax header.
> *   **Check 4: questionnaire**
    *   Evidence: No survey questions.
> *   **Check 5: resume**
    *   Evidence: No career history.
> *   **Check 6: scientific_publication**
    *   Evidence: No journal header.
> *   **Check 7: financial**
    *   Evidence: No financial data.
> *   **Check 8: specification**
    *   Evidence: No material safety data or product formulation.
> *   **Check 9: presentation**
    *   Evidence: "Slide/overhead layouts... photographic slide image... Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead".
    *   The page has a large black block (likely the slide itself or a dark background) and text on the left.
    *   Wait, let's look closer at the text. "CHAP 7", "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z". And a column of numbers.
    *   This looks like a slide from a presentation, maybe a chart key or a data slide.
    *   "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder".
    *   "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
    *   Here, the black area is huge. The text is sparse on the left.
    *   This fits the description of a photographed slide/overhead.
    *   Let's check the text content: "CHAP 7", letters A-Z, numbers. This looks like a slide showing a chapter key or a data table from a presentation.
    *   The layout is sparse text on the left, large black area on the right. This is typical of a slide scan where the slide is dark or the background is black.
    *   Actually, looking very closely at the image:
        *   Left side: A vertical white strip. Text "CHAP 7". Letters A-Z vertically. Numbers next to letters.
        *   Bottom of strip: "117.5", "117.5". "CH...", "USE...", "MADE...".
        *   Right side: A large black rectangle. This looks like a photograph of a slide or an overhead transparency. The black area is the slide content (maybe a dark chart) or just the background.
        *   Wait, is this a folder tab?
        *   "Folder-tab pages: ... photograph of a physical manila folder TAB ... bearing a short filing label ... usually with a Bates number ... The black bar is the photographed folder body/tab edge".
        *   If this is a folder tab, the label is "CHAP 7 ... A B C ...". That's not a short filing label. That's a lot of content.
        *   "A page is NOT file_folder if it carries any real content — a photograph or slide image... or a bold headline title". "CHAP 7" is a bold headline title.
        *   So it's not file_folder.
    *   Is it a presentation?
    *   "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)... photographic slide image".
    *   The text "CHAP 7" and the list A-Z with numbers looks like a slide from a presentation, perhaps a "Chapter 7" slide or a key.
    *   The large black area is likely the slide itself (a dark slide) or a photograph of a slide.
    *   The Bates number "03701993" is on the right.
    *   This looks like a scanned slide.
    *   Therefore: presentation.
> *   **Check 10: form**
    *   Evidence: Not a form.
> *   **Check 11: correspondence**
    *   Evidence: No.
> *   **Check 12: news_article**
    *   Evidence: No.
> *   **Check 13: scientific_report**
    *   Evidence: No running prose.
> *   **Check 14: advertisement**
    *   Evidence: No.
> **Re-evaluating Check 1 vs Check 9:**
- The page has a large black block.
- Left side has text: "CHAP 7", "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z", numbers.
- Bottom text: "CH...", "USE...", "MADE...".
- Bates number: 03701993.
- Is this a folder tab?
    - "Folder-tab pages: ... photograph of a physical manila folder TAB ... bearing a short filing label ... product name, collection/company name, month or date range, contract/file description, or alphanumeric identifier".
    - "CHAP 7" could be a filing label? "Chapter 7"?
    - But there is a list of letters A-Z and numbers. That's not a short filing label. That's content.
    - "A page is NOT file_folder if it carries any real content — a photograph or slide image... or a bold headline title". "CHAP 7" is a bold headline. The list A-Z is content.
    - So not file_folder.
> - Is it a presentation?
    - "photographic slide image (including a blurred or low-quality photo of a slide, chart, or scene)".
    - "Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center (e.g., lower-right) rather than in running paragraphs, points to a photographed slide/overhead — presentation".
    - Here, the text is on the left (off-center), sparse. The black bar/block is large.
    - This fits "photographed slide/overhead".
    - The content "CHAP 7" and the list looks like a slide from a deck.
> **Conclusion:** presentation.
> Let's look really closely at the text.
"CHAP 7"
"A"
"B"
...
"Z"
Numbers next to them: 1, 2, 3...
This looks like a slide showing a mapping or a key.
The large black area is likely the rest of the slide (maybe a chart that is dark, or just the slide background).
The Bates number is on the right margin.
This is a scanned slide.
> Label: presentation.
> Wait, is there any other possibility?
- "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- The text is a list of letters and numbers. Is this a chart/table?
- "CHART 1" with rows A-Z and numeric values -> form (check 10).
- Let's check the text again.
- Left strip: "CHAP 7". Then "A", "B", "C"... down to "Z".
- Next to it, a column of numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3...
- Bottom: "117.5", "117.5".
- Bottom right of the white strip: "CH...", "USE...", "MADE...".
- This looks like a data table or a chart.
- "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) ... is a form (check 10), not a presentation."
- BUT, check 9 says: "photographic slide image (including a blurred or low-quality photo of a slide, chart, or scene)".
- If the page is a *photograph* of a slide containing a chart, it is a presentation (photographic slide).
- If the page is a *scan* of a printed chart (paper), it is a form.
- How to tell?
- "Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
- The large black block on the right looks like the body of a slide or a dark background.
- The text is on a narrow strip on the left. This is very characteristic of a slide scan where the slide is not centered or the scan captured the slide mount.
- Also, the text is monospaced, typical of old computer printouts or slide text.
- The Bates number "03701993" is vertical on the right.
- The black area has a texture. It looks like a photograph of a dark slide.
- Let's look at the "folder tab" exception.
- "Folder-tab pages: ... photograph of a physical manila folder TAB ... bearing a short filing label ... The black bar is the photographed folder body/tab edge".
- If this is a folder tab, the label is the text on the left.
- Label: "CHAP 7", "A B C ... Z", numbers.
- Is this a short filing label? No. It's a list.
- "A page is NOT file_folder if it carries any real content — a photograph or slide image... or a bold headline title". "CHAP 7" is a bold headline.
- So it's not file_folder.
> - Is it a form (check 10)?
- "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) ... is a form".
- If this is a paper document (a chart printed on paper), it's a form.
- If this is a slide (photograph of a slide), it's a presentation.
- The visual evidence: Large black block, sparse text on the side, Bates number. This screams "scanned slide" or "photographed slide".
- The text "CHAP 7" suggests a presentation slide for Chapter 7.
- The list A-Z with numbers could be a slide content.
- The instruction: "photographic slide image (including a blurred or low-quality photo of a slide, chart, or scene) ... is a presentation".
- The instruction: "Scan-artifact signal: a solid black bar along one edge ... points to a photographed slide/overhead — presentation".
- The black area is huge. It's not just a bar. It's a large block.
- Wait, "solid black bar along one edge". Here the black area is the main content on the right.
- Maybe the white strip is the slide mount?
- Actually, looking at the layout: The white strip is on the left. The black block is on the right.
- This looks like a slide that is mostly black (dark chart) with text on the left side.
- Or it's a folder tab? No, too much content.
- Let's assume it's a presentation (photographic slide).
> Let's reconsider "form" (check 10).
- "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) ... is a form".
- If the page is a scan of a paper chart, it's a form.
- How to distinguish paper chart vs slide?
- "Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center ... points to a photographed slide/overhead".
- Here, the text is on the left edge (sparse, off-center). The right side is a large black block.
- This matches the "photographed slide" signal.
- Also, the text is very narrow and vertical. "CHAP 7" is rotated? No, "CHAP 7" is horizontal at the top of the strip. The letters A-Z are vertical.
- Wait, "CHAP 7" is at the top. "A" is below it. "B" below that.
- The letters are arranged vertically.
- This looks like a slide layout.
> Let's look at the bottom text: "117.5", "117.5". "CH...", "USE...", "MADE...".
- "CH" could be "Chapter". "USE" could be "Used". "MADE" could be "Made".
- This looks like metadata or slide footer.
> I will go with **presentation**. The layout (sparse text, large dark area, Bates number) strongly indicates a photographed slide/overhead.
> One more check: Check 1 file_folder.
- "A page is NOT file_folder if it carries any real content — a photograph or slide image... or a bold headline title".
- "CHAP 7" is a bold headline title.
- So not file_folder.
> Final decision: presentation.
> Wait, is there any chance it's a **form**?
- If the black area is just a scan artifact (black background) and the white strip is the actual document...
- The white strip has "CHAP 7", letters A-Z, numbers.
- If this is a printed chart on paper, it's a form.
- But the black area is too large and textured. It looks like a photograph of a dark slide.
- The instruction says: "photographic slide image (including a blurred or low-quality photo of a slide, chart, or scene) ... is a presentation".
- The image is low quality, blurry, black and white.
- The text is sparse.
- I'll stick with presentation.
> Let's re-read the folder tab rule.
- "Folder-tab pages: ... photograph of a physical manila folder TAB ... bearing a short filing label ... usually with a Bates number ... The label IS filing metadata ... The black bar is the photographed folder body/tab edge".
- If the white strip is the folder tab...
- Label: "CHAP 7", "A B C ... Z", numbers.
- Is this a short filing label? No. "CHAP 7" is short, but the list is not.
- "A page is NOT file_folder if it carries any real content ... or a bold headline title". "CHAP 7" is a bold headline.
- So even if it's a folder tab photo, the content makes it not file_folder.
- If it's not file_folder, and it's a slide-like layout, it's presentation.
> What about **scientific_report**?
- No running prose.
> What about **specification**?
- No.
> So **presentation** is the best fit.
> One detail: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- This applies if it's a paper chart.
- But "photographic slide image (including ... photo of a slide, chart ...)" is presentation.
- The visual evidence (black block, sparse text, Bates number) points to photographic slide.
- The text "CHAP 7" suggests a presentation chapter.
> I will classify as presentation.
> Wait, looking very closely at the numbers column:
1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3...
It's a long column of numbers.
And letters A-Z.
This looks like a data table.
If it's a data table on a slide, it's a presentation (photo of slide).
If it's a data table on paper, it's a form.
The black background suggests slide.
The text is on the left, sparse.
"Scan-artifact signal: a solid black bar along one edge ... combined with sparse text ... points to a photographed slide/overhead".
Here the black area is the main part. The text is on the edge.
This fits.
> Final label: presentation.

---