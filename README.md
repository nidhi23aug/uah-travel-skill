# UAH travel skill for Claude Code

A Claude Code skill for University of Alabama in Huntsville travelers. It helps with a work trip from the Travel Authorization to the reimbursement:

- works out allowable costs (GSA meals and lodging, lowest fare class airfare, mileage, registration)
- takes proof screenshots from GSA, airline, hotel and conference sites
- builds the captioned PDF attachments Business Services asks for
- fills the Kuali "UAH Travel Launch" form as a draft
- helps pick flights and hotels that follow UAH rules and saves the booking proof
- assembles the reimbursement packet after the trip

It never submits a form, pays for anything, signs in for you or types a password. You review and submit.

This is a personal project, not an official UAH tool. UAH Business Services and the UAH Travel Guidelines have the final say.

## Install

You need [Claude Code](https://code.claude.com) signed in with a Claude Pro, Max, Team or Enterprise plan, plus Google Chrome.

```
git clone https://github.com/nidhi23aug/uah-travel-skill.git
cd uah-travel-skill
./install.sh
```

`install.sh` copies the skill to `~/.claude/skills/uah-travel-authorization/` and sets up a small Python environment at `~/.venvs/uah-ta` for building PDFs. To update later, run `git pull` and `./install.sh` again.

To install by hand instead, copy `skills/uah-travel-authorization/` into `~/.claude/skills/`, then run:

```
python3 -m venv ~/.venvs/uah-ta
~/.venvs/uah-ta/bin/pip install reportlab pypdf
```

## Connect Claude to Chrome

The skill reads web pages, takes screenshots and fills the Kuali form through the Claude in Chrome extension.

1. Install [Claude in Chrome](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn) (version 1.0.36 or later).
2. Start Claude Code with `claude --chrome`, or type `/chrome` inside Claude Code and choose "Enabled by default".
3. Allow these sites when asked, or add them in the extension's site settings:
   - `gsa.gov` (per diem rates)
   - `google.com/travel` and `google.com/maps` (flights, distances)
   - `uah.edu` (travel guidelines, mileage table)
   - the airline, hotel and conference sites for your trip
   - `uah.kualibuild.com` (the TA form)
   - `mail.google.com` if you want it to find receipts in your email

Sign in to Kuali, your email and any airline or hotel account yourself.

More help: [Claude Code with Chrome](https://code.claude.com/docs/en/chrome), [Getting started with Claude in Chrome](https://support.claude.com/en/articles/12012173-getting-started-with-claude-in-chrome).

## Use it

Open Claude Code with Chrome connected and ask in plain words, for example:

- "Fill a travel authorization for AGU26 in San Francisco. My invitation letter is in Downloads."
- "Which Delta flights can I book from HSV to SFO on Dec 5, coming back Dec 9 after 3 pm?"
- "Take screenshots showing hotels near the venue are over the GSA rate for Dec 5 to 9."
- "Prepare my reimbursement for the FOSS4G trip. Receipts are in my email."

On first use Claude asks for your UAH ID, supervisor, budget unit head, department and Index/Org, and remembers them. Before filling anything it shows you a cost table to check.

## What the skill knows

The rules are in [`skills/uah-travel-authorization/SKILL.md`](skills/uah-travel-authorization/SKILL.md). In short:

- Meals follow the GSA M&IE rate, with 75% on the first and last travel day.
- Lodging should be within the GSA rate for that month plus 10%, booked directly with the hotel or through the conference housing block. Third-party sites such as Booking.com or Expedia are not allowed.
- Airfare must be the airline's lowest fare class (Delta Main Basic, American Basic Economy, United Basic Economy and so on). A higher class needs screenshots from booking time showing the lowest class was unavailable. Paid seats count as upgrades.
- Driving over 400 miles one way needs a drive vs fly comparison, and UAH pays the lesser.
- The Kuali TA is due at least 14 days before departure, with all proof attached as PDFs.
- An amended TA is needed if actual costs exceed the estimate by more than 10%.
- It also knows the Kuali form's quirks (amounts need decimals, use the left navigation, save and wait after each page) and the packet order for reimbursements.

Rules change. Re-read the [UAH Travel Guidelines](https://www.uah.edu/images/administrative/business-services/Forms/travel-forms/06.04.01-uah-travel-guidelines-11.1.2023.pdf) and the [travel information page](https://www.uah.edu/business-services/travel-information) before each trip, and send questions to your department travel contact or travel@uah.edu (subject "2026 Kuali Travel Question").

## Before you submit

- Check every amount and attachment in the Kuali draft.
- Confirm the funding details and the Traveler's Statement box.
- Submit at least 14 days before you leave.

## Contributing

Found a rule that changed or a new Kuali quirk? Open an issue or a pull request that edits `SKILL.md`.

## License

MIT. See [LICENSE](LICENSE).
