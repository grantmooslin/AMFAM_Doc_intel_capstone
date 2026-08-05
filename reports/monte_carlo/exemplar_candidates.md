# Few-Shot Exemplar Mining

- **Corpus**: /Users/luciusjmorningstar/Downloads/AMFAM_capstone/reports/monte_carlo/corpus.jsonl
- **Targeted pairs**: 12 (from 110 total)
- **Surrogate**: efficacy=0.25, second-exemplar multiplier=1.5

## Simulated gain

- **Expected errors flipped**: 32.8 of 767 corpus errors (4.27% of the error pool)
- **Exemplars selected**: 4 (token cost 11383/12000 chars)

## Confusion pairs targeted

| expected | predicted-as | errors | exemplars available |
|---|---:|---:|---:|
| letter | memo | 53 | 8 |
| budget | invoice | 52 | 8 |
| invoice | form | 41 | 8 |
| specification | form | 41 | 8 |
| budget | form | 33 | 8 |
| scientific_report | form | 23 | 8 |
| invoice | budget | 22 | 8 |
| resume | form | 21 | 8 |
| handwritten | letter | 19 | 8 |
| questionnaire | form | 16 | 8 |
| presentation | file_folder | 16 | 8 |
| presentation | scientific_report | 15 | 8 |

## Selected exemplars

### 1. `rvl_cdip__letter__0029.png` (qwen3.7-flash, v11.8)
**expected**: `letter` | **decoy**: `memo` | **runner_up**: `memo` | **clarity**: 1.00

```
The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "OGILVY & MATHER INC." at the top, which is a letterhead, not a newspaper/magazine masthead or journal running head.

**Check 1: file_folder**
- Evidence: The page has a full letter with body content, letterhead, date, salutation, signature, and handwritten notes. Not just an identifier/stamp.
- Result: not this check.

**Check 2: handwritten**
- Evidence: Most content is typed letter. Handwritten notes at the bottom ("3/30/78 note Reminder", etc.) are just margin notes.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax header.
- Result: not this check.

**Check 4: questionnaire**
- Evidence: No survey instrument or transmittal.
- Result: not this check.

**Check 5: resume**
- Evidence: Not a career history.
- Result: not this check.

**Check 6: scientific_publication**
- Evidence: No journal running head, volume, issue, page range.
- Result: not this check.

**Check 7: financial document (invoice/budget)**
- Evidence: Mentions "coupon", "redemption", but no line-item table, ledger, or financial structure. It's a letter requesting information about a coupon campaign.
- Result: not this check.

**Check 8: specification**
- Evidence: No material safety data, product formulation, or "shall/must" language.
- Result: not this check.

**Check 9: presentation**
- Evidence: Not a slide deck, cover, or statement.
- Result: not this check.

**Check 10: administrative form**
- Evidence: Not a form with fields/boxes.
- Result: not this check.

**Check 11: correspondence (email, memo, letter)**
- Evidence:
  - Letterhead: "OGILVY & MATHER INC."
  - Date: "February 13, 1978"
  - External recipient address: "Mr. John Casey / Cosmopolitan Magazine / 224 West 57 St. / New York, N. Y. 10019"
  - Salutation: "Dear John:"
  - Prose body: "As you know our client..."
  - Closing: "Yours truly, [signature] Douglas E. Pfaffler"
  - This perfectly matches the definition of a letter.
- Result: letter.

**Check 12: news_article**
- Evidence: Not a newspaper/magazine masthead or editorial content.
- Result: not this check.

**Check 13: scientific_report**
- Evidence: Not a research write-up.
- Result: not this check.

**Check 14: advertisement**
- Evidence: Not a promotional layout.
- Result: not this check.

Final label: letter.
Runner-up: memo, ruled out because it has an external recipient address, "Dear John:" salutation, and closing signature, which makes it a letter, not a memo.
```

### 2. `rvl_cdip__specification__0075.png` (qwen3.7-flash, v11.8)
**expected**: `specification` | **decoy**: `form` | **runner_up**: `form` | **clarity**: 1.00

```
The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. Just a Bates number "005724" and "2051530832".

**Check 1: file_folder**
- Evidence: The page has a lot of content (sections, tables, text). Not just an identifier.
- Result: not this check.

**Check 2: handwritten**
- Evidence: Mostly typed text, some handwritten entries in fields (e.g., "212°F", "18", "45", "7.0 to 8.5", "PASTE" circled). But it's a filled form/template. Not majority freeform handwriting.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Result: not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions.
- Result: not this check.

**Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No career history.
- Result: not this check.

**Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range on the page itself.
- Result: not this check.

**Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial line items, invoices, or budgets.
- Result: not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: The page is titled "MATERIAL SAFETY DATA SHEET". It contains sections for "INGREDIENTS", "PHYSICAL DATA", "FIRE AND EXPLOSION HAZARD DATA". It lists chemical names, CAS registry numbers, physical properties (boiling point, vapor pressure, etc.). This matches the definition: "Material Safety Data Sheet ("MATERIAL SAFETY DATA SHEET", hazardous ingredients, physical/fire data)... is a specification".
- Result: YES. This is a specification.

Let's double check.
Check 8: "Material Safety Data Sheet ("MATERIAL SAFETY DATA SHEET", hazardous ingredients, physical/fire data), product formulation or preparation/mixing instructions... is a specification".
The page clearly says "MATERIAL SAFETY DATA SHEET" at the top.
It has Section I (Product info), Section II (Ingredients), Section III (Physical Data), Section IV (Fire and Explosion Hazard Data).
This is a perfect match for specification.

Runner-up: form. A MSDS is a form with fields, but check 8 explicitly says "Material Safety Data Sheet ... is a specification". Check 8 precedes Check 10 (form).

Let's quickly review the checks order:
1. file_folder (no)
2. handwritten (no)
3. fax (no)
4. questionnaire (no)
5. resume (no)
6. scientific_publication (no)
7. invoice/budget (no)
8. specification (yes)

Evidence for check 8: "MATERIAL SAFETY DATA SHEET" header, sections for ingredients, physical data, fire and explosion hazard data, chemical names, CAS registry numbers.

Final label: specification.
```

### 3. `rvl_cdip__resume__0049.png` (qwen3.7-flash, v11.8)
**expected**: `resume` | **decoy**: `form` | **runner_up**: `form` | **clarity**: 1.00

```
The user wants me to classify a scanned document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.

**Document Analysis:**
- Title: "BIOGRAPHICAL SKETCH"
- Top right: "GRANT NUMBER: Kadin, MF" (handwritten)
- Text: "Give the following information for the key personnel and consultants and collaborators. Begin with the principal investigator/program director. Photocopy this page for each person."
- Fields: NAME (Harvey F. Lodish), POSITION TITLE (Member, Whitehead Institute for Biomedical Research, Professor of Biology, M.I.T.)
- Education table: INSTITUTION AND LOCATION, DEGREE, YEAR CONFERRED, FIELD OF STUDY.
- Sections: RESEARCH AND/OR PROFESSIONAL EXPERIENCE, Professional Experience, Honors and Awards, Recent Endowed Lectureships, Recent Editorial Boards, Recent Grant Review Panels, Recent Outside Advisory Committees.
- Bottom: "PHS 398 (Rev. 9/91) Page 2" (handwritten)

**Pre-scan:**
- Mail-client header: None.
- Masthead/running head: None. "PHS 398 (Rev. 9/91)" is a form number, not a journal running head.

**Check 1: file_folder**
- Evidence: Has lots of body content (biographical sketch, education, experience, awards). Not just an ID/stamp.
- Result: not this check.

**Check 2: handwritten**
- Evidence: Mostly typed text. Handwriting is just "Kadin, MF" and "2".
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax header.
- Result: not this check.

**Check 4: questionnaire**
- Evidence: Not a survey instrument.
- Result: not this check.

**Check 5: resume**
- Evidence: Title is "BIOGRAPHICAL SKETCH". Text says "Give the following information for the key personnel...". Lists education, positions, honors, publications (lectureships, editorial boards, advisory committees). Bottom says "PHS 398 (Rev. 9/91)".
- Check 5 rule: "CV, resume, professional profile, or biographical sketch listing education, positions, honors, and publications — including standardized templates such as PHS 398 "BIOGRAPHICAL SKETCH" pages, even when they carry a "Form Page" notation — the biographical content decides this, not the form-page label."
- Result: YES. This is a resume/biographical sketch.

Let's double check.
Is there any other check that matches?
Check 10: form. It is a form (PHS 398), but Check 5 explicitly says "including standardized templates such as PHS 398 'BIOGRAPHICAL SKETCH' pages... the biographical content decides this, not the form-page label." So Check 5 overrides Check 10.

Let's verify the text: "PHS 398 (Rev. 9/91)" is at the bottom left. "BIOGRAPHICAL SKETCH" is at the top. Content is Harvey F. Lodish's career history.

So the label is resume.

Scratchpad construction:
- file_folder: no — page has extensive biographical content (education, experience, awards), not just an identifier.
- handwritten: no — mostly typed text, only minor handwritten annotations ("Kadin, MF", "2").
- fax: no — no fax transmission header.
- questionnaire: no — not a survey instrument.
- resume: yes — titled "BIOGRAPHICAL SKETCH", lists education, professional experience, honors, lectureships, editorial boards, and advisory committees for Harvey F. Lodish; explicitly mentions "PHS 398 (Rev. 9/91)" which is a standardized template for a biographical sketch/CV. Check 5 covers this explicitly.
- Runner-up: form, ruled out because Check 5 explicitly states that PHS 398 "BIOGRAPHICAL SKETCH" pages are classified as resume based on biographical content, overriding the form layout.

Final label: resume.
```

### 4. `rvl_cdip__questionnaire__0071.png` (qwen3.7-flash, v11.8)
**expected**: `questionnaire` | **decoy**: `form` | **runner_up**: `form` | **clarity**: 1.00

```
The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking each condition in order.

**Pre-scan:**
- Mail-client header block: None.
- Masthead or running head: None. There's a title "INTERNATIONAL SYMPOSIUM ON EPIDEMIOLOGY AND PREVENTION OF Atherosclerotic Disease." and "Anacapri, 24- 26 June 1981". No journal running head.

**Check 1: file_folder**
- Evidence: The page has a title, questions, and options. Not just an identifier/stamp.
- Result: not this check.

**Check 2: handwritten**
- Evidence: Typed text throughout. No significant handwriting.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Result: not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: The page is titled "INTERNATIONAL SYMPOSIUM ON EPIDEMIOLOGY AND PREVENTION OF Atherosclerotic Disease." and "Anacapri, 24- 26 June 1981". It contains questions like "SEX", "AGE", "DO YOU NOW SMOKE? YES NO", "IF YES, CIGARETTE? YES NO", "IF YES, NUMBER/DAY", "IF NOT NOW A SMOKER, Former smoker YES NO, Never smoked YES NO", "DO YOU KNOW YOUR BLOOD PRESSURE? YES NO", "IF YES, WHAT IS IT?", "DO YOU KNOW YOUR SERUM CHOLESTEROL? YES NO", "IF YES, WHAT IS IT?". This is clearly a survey instrument or questionnaire asking respondents to answer questions about smoking, blood pressure, and cholesterol.
- Result: questionnaire.

Let's double check.
Is it a scientific_report? No running prose, just questions.
Is it a form? It's a survey instrument. Check 4 (questionnaire) precedes Check 10 (form).
"A page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines... is questionnaire."
This page asks "DO YOU NOW SMOKE? YES NO", etc. It's a questionnaire.

Let's review the checks:
1. file_folder: no
2. handwritten: no
3. FAX: no
4. questionnaire: yes. The page contains a series of questions (SEX, AGE, DO YOU NOW SMOKE?, etc.) with YES/NO options and open-response lines ("WHAT IS IT?"). This is a survey instrument.

Runner-up: form. Ruled out because check 4 (questionnaire) specifically covers survey instruments asking the reader to answer questions, which takes precedence over the generic administrative form check.

Final label: questionnaire.
```

## Proposed exemplar appendix (copy into the next prompt version)

```
### Worked example 1 — letter vs memo

The user wants me to classify a scanned business document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: "OGILVY & MATHER INC." at the top, which is a letterhead, not a newspaper/magazine masthead or journal running head.

**Check 1: file_folder**
- Evidence: The page has a full letter with body content, letterhead, date, salutation, signature, and handwritten notes. Not just an identifier/stamp.
- Result: not this check.

**Check 2: handwritten**
- Evidence: Most content is typed letter. Handwritten notes at the bottom ("3/30/78 note Reminder", etc.) are just margin notes.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax header.
- Result: not this check.

**Check 4: questionnaire**
- Evidence: No survey instrument or transmittal.
- Result: not this check.

**Check 5: resume**
- Evidence: Not a career history.
- Result: not this check.

**Check 6: scientific_publication**
- Evidence: No journal running head, volume, issue, page range.
- Result: not this check.

**Check 7: financial document (invoice/budget)**
- Evidence: Mentions "coupon", "redemption", but no line-item table, ledger, or financial structure. It's a letter requesting information about a coupon campaign.
- Result: not this check.

**Check 8: specification**
- Evidence: No material safety data, product formulation, or "shall/must" language.
- Result: not this check.

**Check 9: presentation**
- Evidence: Not a slide deck, cover, or statement.
- Result: not this check.

**Check 10: administrative form**
- Evidence: Not a form with fields/boxes.
- Result: not this check.

**Check 11: correspondence (email, memo, letter)**
- Evidence:
  - Letterhead: "OGILVY & MATHER INC."
  - Date: "February 13, 1978"
  - External recipient address: "Mr. John Casey / Cosmopolitan Magazine / 224 West 57 St. / New York, N. Y. 10019"
  - Salutation: "Dear John:"
  - Prose body: "As you know our client..."
  - Closing: "Yours truly, [signature] Douglas E. Pfaffler"
  - This perfectly matches the definition of a letter.
- Result: letter.

**Check 12: news_article**
- Evidence: Not a newspaper/magazine masthead or editorial content.
- Result: not this check.

**Check 13: scientific_report**
- Evidence: Not a research write-up.
- Result: not this check.

**Check 14: advertisement**
- Evidence: Not a promotional layout.
- Result: not this check.

Final label: letter.
Runner-up: memo, ruled out because it has an external recipient address, "Dear John:" salutation, and closing signature, which makes it a letter, not a memo.

### Worked example 2 — specification vs form

The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**
- Mail-client header block: None.
- Masthead/running head: None. Just a Bates number "005724" and "2051530832".

**Check 1: file_folder**
- Evidence: The page has a lot of content (sections, tables, text). Not just an identifier.
- Result: not this check.

**Check 2: handwritten**
- Evidence: Mostly typed text, some handwritten entries in fields (e.g., "212°F", "18", "45", "7.0 to 8.5", "PASTE" circled). But it's a filled form/template. Not majority freeform handwriting.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or fax cover sheet header.
- Result: not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: No survey questions.
- Result: not this check.

**Check 5: PERSON'S CAREER HISTORY -> resume**
- Evidence: No career history.
- Result: not this check.

**Check 6: PUBLISHED EVIDENCE -> scientific_publication**
- Evidence: No journal name, volume, issue, page range on the page itself.
- Result: not this check.

**Check 7: FINANCIAL DOCUMENT -> invoice or budget**
- Evidence: No financial line items, invoices, or budgets.
- Result: not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
- Evidence: The page is titled "MATERIAL SAFETY DATA SHEET". It contains sections for "INGREDIENTS", "PHYSICAL DATA", "FIRE AND EXPLOSION HAZARD DATA". It lists chemical names, CAS registry numbers, physical properties (boiling point, vapor pressure, etc.). This matches the definition: "Material Safety Data Sheet ("MATERIAL SAFETY DATA SHEET", hazardous ingredients, physical/fire data)... is a specification".
- Result: YES. This is a specification.

Let's double check.
Check 8: "Material Safety Data Sheet ("MATERIAL SAFETY DATA SHEET", hazardous ingredients, physical/fire data), product formulation or preparation/mixing instructions... is a specification".
The page clearly says "MATERIAL SAFETY DATA SHEET" at the top.
It has Section I (Product info), Section II (Ingredients), Section III (Physical Data), Section IV (Fire and Explosion Hazard Data).
This is a perfect match for specification.

Runner-up: form. A MSDS is a form with fields, but check 8 explicitly says "Material Safety Data Sheet ... is a specification". Check 8 precedes Check 10 (form).

Let's quickly review the checks order:
1. file_folder (no)
2. handwritten (no)
3. fax (no)
4. questionnaire (no)
5. resume (no)
6. scientific_publication (no)
7. invoice/budget (no)
8. specification (yes)

Evidence for check 8: "MATERIAL SAFETY DATA SHEET" header, sections for ingredients, physical data, fire and explosion hazard data, chemical names, CAS registry numbers.

Final label: specification.

### Worked example 3 — resume vs form

The user wants me to classify a scanned document into one of 16 categories.
I need to follow the scratchpad procedure, checking 1-14 in order.

**Document Analysis:**
- Title: "BIOGRAPHICAL SKETCH"
- Top right: "GRANT NUMBER: Kadin, MF" (handwritten)
- Text: "Give the following information for the key personnel and consultants and collaborators. Begin with the principal investigator/program director. Photocopy this page for each person."
- Fields: NAME (Harvey F. Lodish), POSITION TITLE (Member, Whitehead Institute for Biomedical Research, Professor of Biology, M.I.T.)
- Education table: INSTITUTION AND LOCATION, DEGREE, YEAR CONFERRED, FIELD OF STUDY.
- Sections: RESEARCH AND/OR PROFESSIONAL EXPERIENCE, Professional Experience, Honors and Awards, Recent Endowed Lectureships, Recent Editorial Boards, Recent Grant Review Panels, Recent Outside Advisory Committees.
- Bottom: "PHS 398 (Rev. 9/91) Page 2" (handwritten)

**Pre-scan:**
- Mail-client header: None.
- Masthead/running head: None. "PHS 398 (Rev. 9/91)" is a form number, not a journal running head.

**Check 1: file_folder**
- Evidence: Has lots of body content (biographical sketch, education, experience, awards). Not just an ID/stamp.
- Result: not this check.

**Check 2: handwritten**
- Evidence: Mostly typed text. Handwriting is just "Kadin, MF" and "2".
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**
- Evidence: No fax header.
- Result: not this check.

**Check 4: questionnaire**
- Evidence: Not a survey instrument.
- Result: not this check.

**Check 5: resume**
- Evidence: Title is "BIOGRAPHICAL SKETCH". Text says "Give the following information for the key personnel...". Lists education, positions, honors, publications (lectureships, editorial boards, advisory committees). Bottom says "PHS 398 (Rev. 9/91)".
- Check 5 rule: "CV, resume, professional profile, or biographical sketch listing education, positions, honors, and publications — including standardized templates such as PHS 398 "BIOGRAPHICAL SKETCH" pages, even when they carry a "Form Page" notation — the biographical content decides this, not the form-page label."
- Result: YES. This is a resume/biographical sketch.

Let's double check.
Is there any other check that matches?
Check 10: form. It is a form (PHS 398), but Check 5 explicitly says "including standardized templates such as PHS 398 'BIOGRAPHICAL SKETCH' pages... the biographical content decides this, not the form-page label." So Check 5 overrides Check 10.

Let's verify the text: "PHS 398 (Rev. 9/91)" is at the bottom left. "BIOGRAPHICAL SKETCH" is at the top. Content is Harvey F. Lodish's career history.

So the label is resume.

Scratchpad construction:
- file_folder: no — page has extensive biographical content (education, experience, awards), not just an identifier.
- handwritten: no — mostly typed text, only minor handwritten annotations ("Kadin, MF", "2").
- fax: no — no fax transmission header.
- questionnaire: no — not a survey instrument.
- resume: yes — titled "BIOGRAPHICAL SKETCH", lists education, professional experience, honors, lectureships, editorial boards, and advisory committees for Harvey F. Lodish; explicitly mentions "PHS 398 (Rev. 9/91)" which is a standardized template for a biographical sketch/CV. Check 5 covers this explicitly.
- Runner-up: form, ruled out because Check 5 explicitly states that PHS 398 "BIOGRAPHICAL SKETCH" pages are classified as resume based on biographical content, overriding the form layout.

Final label: resume.

### Worked example 4 — questionnaire vs form

The user wants me to classify a scanned document into one of 16 categories.
I will follow the scratchpad procedure, checking each condition in order.

**Pre-scan:**
- Mail-client header block: None.
- Masthead or running head: None. There's a title "INTERNATIONAL SYMPOSIUM ON EPIDEMIOLOGY AND PREVENTION OF Atherosclerotic Disease." and "Anacapri, 24- 26 June 1981". No journal running head.

**Check 1: file_folder**
- Evidence: The page has a title, questions, and options. Not just an identifier/stamp.
- Result: not this check.

**Check 2: handwritten**
- Evidence: Typed text throughout. No significant handwriting.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**
- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Result: not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
- Evidence: The page is titled "INTERNATIONAL SYMPOSIUM ON EPIDEMIOLOGY AND PREVENTION OF Atherosclerotic Disease." and "Anacapri, 24- 26 June 1981". It contains questions like "SEX", "AGE", "DO YOU NOW SMOKE? YES NO", "IF YES, CIGARETTE? YES NO", "IF YES, NUMBER/DAY", "IF NOT NOW A SMOKER, Former smoker YES NO, Never smoked YES NO", "DO YOU KNOW YOUR BLOOD PRESSURE? YES NO", "IF YES, WHAT IS IT?", "DO YOU KNOW YOUR SERUM CHOLESTEROL? YES NO", "IF YES, WHAT IS IT?". This is clearly a survey instrument or questionnaire asking respondents to answer questions about smoking, blood pressure, and cholesterol.
- Result: questionnaire.

Let's double check.
Is it a scientific_report? No running prose, just questions.
Is it a form? It's a survey instrument. Check 4 (questionnaire) precedes Check 10 (form).
"A page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines... is questionnaire."
This page asks "DO YOU NOW SMOKE? YES NO", etc. It's a questionnaire.

Let's review the checks:
1. file_folder: no
2. handwritten: no
3. FAX: no
4. questionnaire: yes. The page contains a series of questions (SEX, AGE, DO YOU NOW SMOKE?, etc.) with YES/NO options and open-response lines ("WHAT IS IT?"). This is a survey instrument.

Runner-up: form. Ruled out because check 4 (questionnaire) specifically covers survey instruments asking the reader to answer questions, which takes precedence over the generic administrative form check.

Final label: questionnaire.

```
