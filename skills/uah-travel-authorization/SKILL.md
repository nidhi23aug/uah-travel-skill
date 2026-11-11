---
name: uah-travel-authorization
description: Use when a UAH (University of Alabama in Huntsville) traveler wants help with a work trip - filling a Travel Authorization (TA) in the Kuali "UAH Travel Launch" form, working out per diem, hotel, airfare, mileage and registration estimates, taking proof screenshots, building the PDF attachments, booking flights in the allowed fare class, or putting together the reimbursement packet after the trip. Triggers include "fill a travel authorization", "TA for a conference", "Kuali travel form", "travel auth for my trip to X", "proof screenshots for travel", "which flight can I book", "prepare my travel reimbursement". Never submits forms or pays for anything; the traveler reviews, submits and pays.
---

# UAH travel: authorization, booking proof and reimbursement

You help a UAH traveler with a work trip from start to finish: estimate allowable costs under UAH and GSA rules, capture proof from official sites, build captioned PDF attachments, fill the Kuali TA form as a draft, help pick flights and hotels that follow the rules, and assemble the reimbursement packet afterwards.

You never click Submit, never pay, never sign in for the traveler and never type passwords. The traveler does those steps.

## 0. Traveler profile (first run)

Look in memory for a saved traveler profile. If there isn't one, ask these in a single AskUserQuestion and save the answers to memory as `uah-traveler-profile`:

- Traveler's UAH ID (the short login, e.g. `ab0012`) and full name as it appears on their ID
- Staff or faculty, and whether they are an instructor
- Department (as listed in Kuali) and college, if any
- Supervisor's name and UAH ID
- Budget unit head's name and UAH ID
- Default Index/Org to charge (confirm it on every trip; grants change)
- Department travel contact (name and email) for questions

Reuse the profile on later trips and only confirm what may have changed.

## 1. Gather trip inputs

Read any documents the traveler points to first (invitation letter, acceptance or session chair confirmation, a colleague's TA for the same event). Then ask only what you can't find, in one AskUserQuestion:

- Travel dates. Default is to arrive the day before the event and leave the day after; confirm.
- Fly or drive. Driving more than 400 miles one way needs a drive vs fly comparison.
- Index/Org for this trip.
- Registration category (member or non-member) and which rate tier (early or standard). Don't assume.
- Items paid by PCard (usually registration only).
- Extras such as taxis, poster printing or parking, and whether proof exists.

## 2. Estimate the costs (UAH rules)

Check every rate live. Don't trust remembered numbers.

| Line | Rule | Proof |
|---|---|---|
| Meals (M&IE) | GSA rate for the destination. First and last travel day are paid at 75% (GSA lists this as "First and last day of travel"). | gsa.gov per diem page for the city and fiscal year (FY starts Oct 1) |
| Lodging | Nightly rate within the GSA lodging rate for that month plus 10%. Total = rate x nights + hotel tax (say the tax is an estimate). | The hotel's own site or the conference's official housing block. Never Expedia, Booking.com, Amex Travel or other third parties. |
| Airfare | Coach, booked at least 14 days ahead, in the airline's lowest fare class. Baggage fees are not a reason to pick a higher class. | Airline site or Google Flights for the exact dates, showing the full row of fare classes including Basic |
| Personal vehicle | Miles x current UAH rate (check the table; it follows the IRS rate). Over 400 miles one way, UAH pays the lesser of flying or driving. | uah.edu travel information page plus a Google Maps route |
| Registration | Exact tier and category from the conference site | Conference registration rates page |
| Ground transportation, misc | Itemized estimate. Label it "approximate" if there is no proof. | Simple estimate PDF |

Lowest fare classes Business Services accepts:

- American Airlines Basic Economy (class B)
- Delta Main Basic (class E)
- United Basic Economy (usually class N or K)
- JetBlue Blue Basic
- Southwest Wanna Get Away
- Frontier's lowest unbundled fare

If the traveler books anything higher, they need screenshots taken at booking time that show the lowest class was unavailable under the same search (same airline, dates and flights). Without them, Business Services compares fares after the fact and cuts the reimbursement to the lowest fare. Paid seat selection and other extras count as upgrades and are not reimbursed.

Things that have caught travelers before:

- Hotels near a big conference often run far above GSA plus 10% when booked directly. Check the conference's official housing block first; it often has rates under the cap. Booking through the block goes through the conference housing site, which is allowed.
- Point out deadlines that change money: early registration cutoffs, the housing block closing date, and the 14 day TA rule.
- Screenshots must match the dates and scenario they are used for. If a comparison uses different dates, caption it with its own dates. Don't hide, crop out or edit away cheaper options; use the site's own filters (for example a room type filter) so the filter shows on the page.

Show the traveler a cost table and total before filling anything.

### UAH Business Services rules (Kuali Travel, live since Oct 1, 2026)

Re-read the UAH Travel Guidelines before every trip. They can change, and Business Services enforces them strictly.

- Submit the Kuali TA at least 14 days before departure.
- Attach all proof at TA time as PDFs: cost comparisons, the agenda or meeting site, screenshots. The traveler gathers it.
- The traveler is Business Services' point of contact and tracks the approval status; the supervisor and budget head can't see it.
- Book airfare and lodging directly with the airline or hotel.
- Lodging covers the room and room taxes only (no parking, phone or resort extras).
- Meals already provided by the conference or hotel are deducted at GSA meal amounts on the expense report.
- Mileage to and from the airport is capped at about 10 miles each way.
- An amended TA is needed if the actual cost exceeds the estimate by more than 10%, and travel dates that change should be raised with the department contact.
- A red asterisk (*) marks a required question on the form.
- Trips approved in Kuali are reimbursed in Kuali. Trips approved on the old PDF TA use the old Excel reimbursement form, sent to the department travel contact.

Where to find the form: UAH Self Service > Research > Kuali Build Submission Status > VP Finance - Business Services > UAH Travel Launch (favorite it with the heart icon).

Sources:

- UAH Travel Guidelines: https://www.uah.edu/images/administrative/business-services/Forms/travel-forms/06.04.01-uah-travel-guidelines-11.1.2023.pdf (check for a newer version)
- UAH travel information and mileage table: https://www.uah.edu/business-services/travel-information
- GSA per diem rates: https://www.gsa.gov/travel/plan-book/per-diem-rates

Questions: the department travel contact from the profile, or Business Services at travel@uah.edu with the subject "2026 Kuali Travel Question".

## 3. Capture proof screenshots (Chrome)

Load the claude-in-chrome tools in one ToolSearch (include `browser_batch`, `find`, `form_input`, `file_upload`, `get_page_text`). Work in your own tab. Take screenshots with `save_to_disk: true` and note each saved path. Scroll so the prices and the search details (dates, guests, fare class) are both visible. Accept nothing beyond what is needed to view prices, and never sign in or book.

Screenshots taken by the browser tool don't show the computer's clock. Put the capture date and time in the PDF caption (or a labeled bar above the image). If the traveler wants their own clock visible, set the pages up and ask them to press Cmd+Shift+3 on each one.

For emails (receipts, confirmations) in Gmail, open the print view through `fetch` and `document.write` rather than navigating to it, because the print dialog blocks the browser session. Narrow the page (body width about 640px, zoom about 0.66) and capture it in sections at scale 1 so the text stays readable.

## 4. Build the PDFs

Use `scripts/build_proof_pdfs.py` (reportlab and pypdf; use `~/.venvs/uah-ta` if it exists, otherwise a scratch venv; run Python with `-I`). Write a small JSON spec (see the script header) listing documents and their pages: a text calculation page, a captioned image page, or existing PDFs to merge. Save to `~/Downloads/TA_<EVENT>_<Traveler_Name>/` with numbered names, for example:

1. `1_<Event>_Invitation_and_Role_Confirmation.pdf` (merge the traveler's letters) for Supporting Documentation
2. `2_Airfare_<ORIG>-<DEST>_<dates>.pdf` (lowest fare class shown)
3. `3_Lodging_Estimate_<...>.pdf` (calculation page, hotel or housing block screenshots, GSA lodging rate)
4. `4_Registration_Fee_<Event>.pdf`
5. `5_Meals_GSA_Per_Diem_<City>.pdf` (calculation page and GSA M&IE) for Additional Documentation
6. `6_Ground_Transportation_Estimate.pdf` (if any)
7. `1_Cost_Comparison_Drive_vs_Fly.pdf` (driving trips only)

Check with pypdf text extraction that the numbers match what goes on the form.

## 5. Fill the Kuali form (draft only)

Start a new draft at `https://uah.kualibuild.com/app/6880e80fe715d5027e7f439b/page/6880e80fe715d5027e7f439b/run`. The traveler must already be signed in; if not, ask them to sign in. Note the form number in the header.

1. Traveler Information: Are you the traveler: Yes; traveler, supervisor, staff or faculty, college, department and instructor from the profile.
2. Trip Information: travel type (Continental US for domestic); overnight Yes, then ">7 days?" (end minus start greater than 7); destination; start and end dates (type MM/DD/YYYY then Tab); reason (purpose, roles, event name, venue, dates); distance under 100 miles No; start date passed No; "Do any apply" (drive over 400 miles, other airport, personal days, or "None of these apply"); Supporting Documentation = the invitation or role PDF (one file).
3. Estimate of Cost: type amounts with decimals ("965.00"; bare digits are read as cents). Leave unused lines blank, since a $0 still demands an upload. Upload each line's PDF; the meals PDF goes in Additional Documentation. Check the automatic total.
4. PCard Usage: Yes and which items (usually Registration Fee).
5. Funding Details: copy the setup from the traveler's previous TA if there is one. A common setup is "funded by contracts and grants" Yes; "Contracts & Grants Account?" No (this shows the Index/Org field); Index; Amount Requested = total; Budget Unit Head from the profile. Ask the traveler to confirm.
6. Additional Traveler Info: the Traveler's Statement box is pre-checked (ask the traveler to confirm it). Add a short note covering roles, travel days, hotel choice vs GSA, which amounts are estimates, and anything unusual such as driving instead of flying.

Form quirks:

- Use the left navigation; "Next" is unreliable.
- `file_upload` needs the hidden `input[type=file]` ref (use `find` "hidden input of type=file for <field>"), not the visible "Select a File" button.
- Click Save after each page and wait about 8 seconds before navigating or reloading. A quick navigation once dropped the page 6 notes. The "Apply Edits" banner once closed the form.
- Deleting attachments may be blocked by the permission system. If so, give the traveler exact manual steps.
- Clicking an attachment's filename downloads it; aim carefully at Delete buttons.
- Finally reload the draft and check every page (amounts, attachments, dates, funding, notes).

## 6. Booking help (after approval)

When the traveler asks which flight or hotel to book:

- Search the exact dates and times they want, list the options in a short table (airline, times, connections, lowest fare class price), and recommend one.
- Open the airline's own booking page with the lowest fare class selected, stop before any "accept restrictions", passenger or payment step, and tell the traveler exactly what to click and what to skip (seats, bags, insurance, upgrade offers, credit card offers).
- Capture the fare class comparison before they pay, then add the airline's confirmation email to the airfare proof PDF.
- For hotels, compare the hotel's direct rate with any third-party booking, look for a government or member rate on the hotel's own site, and capture the rates near the venue on the same dates if the stay will be over GSA plus 10%.
- If dates change from the approved TA, tell the traveler to check with the department contact about an amended TA.

## 7. Reimbursement packet (after the trip)

Collect receipts from the traveler's email (airline, hotel folio, rideshare, registration). Build one PDF named `01 <Traveler Name> Complete Packet <City ST>.pdf` in this order:

1. The travel voucher (the Excel form converted to PDF) or the Kuali expense summary
2. Divider page "APPROVAL", then the approved TA form
3. Divider page "PER Diem", then the GSA lodging and M&IE pages
4. Divider page "FLIGHT", then a short explanation page if anything changed, the airline receipts, any change fee receipt, then a "Proof Screenshots" divider and the fare comparison screenshots
5. Divider page "HOTEL", then an explanation page if over GSA, the confirmations and the hotel folios
6. Divider page "TAXIs", then a summary table (date, time, from and to, amount) and each ride receipt
7. Registration receipt (mark it PCard if paid by PCard)
8. The conference agenda

Divider pages are one plain centered word. Rideshare tips are reimbursable. For an explanation page, state the facts plainly (original plan, what changed and why, what it cost) and sign-off lines for the traveler.

## 8. Hand off

Close your extra tabs. Report: the form number or packet path, the cost table and total, what is attached where, and a short "before you submit" list (deadlines, estimated items, funding and statement confirmations, policy caveats). Leave forms in draft. Save the trip to memory as `<event>-<year>-travel` and add any new form quirks to a memory note so the next trip goes faster.
