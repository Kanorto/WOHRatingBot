# WOHRatingBot

WOHRatingBot is a Telegram bot and mini-application for the
**World_of_hosts** community. Its goal is to provide a fully
transparent, non-commercial rating of hosting providers. Users can
explore hosters, leave reviews, and see detailed statistics while
verified administrators keep their host information current. The entire
workflow is handled in a Telegram supergroup so moderators can easily
track activity and communicate with hoster representatives.

The bot is built with **aiogram** while the mini-application uses
**FastAPI**. Both parts share a single SQLite database through
**SQLAlchemy** with migrations managed by **Alembic** so the data can be
ported to another engine later. English and Russian interfaces are
planned from the start. Extensive logging and a debug mode help trace
user actions and simplify development. Deployment can be done via a
Docker setup or a hosting panel such as **Pterodactyl**.

## Overview
- **Transparency first.** Ratings are public, free of charge, and based
  on community feedback.
- **Mini-app experience.** The Telegram web app offers an intuitive
  interface for browsing hosts and voting.
- **Supergroup integration.** All moderation and discussion happen in a
  Telegram supergroup with topics.
- **Extensibility.** New rating categories and service types can be
  added without code changes.

## Project Structure

```
WOHRatingBot/
├── bot/        # Telegram bot (aiogram)
├── webapp/     # FastAPI mini-application
├── models/     # Database schemas and migrations
├── data/       # Static data or migrations
├── tests/      # Unit tests
├── requirements.txt
├── TODO.md
└── README.md
```

The bot and web app share the same database so they can run together or
be split into separate services later.
The repository now contains basic placeholders for these components so development can begin immediately.

## Key Features

### Rating System
- Users can **vote for hosters** and see a comprehensive rating table.
- Ratings combine multiple criteria:
  - **Types of services** (VPS, dedicated servers, panels, domains, etc.)
  - **User scores** with text reviews
  - **Price/quality ratio**, **reliability**, **support quality**, and any
    custom metrics defined by administrators
- Every rating or user field is subject to **moderator approval** before
  publication.

### Host Profiles
- The mini‑app shows detailed hoster cards with mandatory and optional
  fields: description, service categories, location, pricing, and
  contact links (website, control panel, Telegram, YouTube, and more).
- A **verified owner badge** is displayed once ownership is confirmed.

### Host Management
- Any user can **submit a host** for verification. Ownership must be
  proven before listing.
- Moderators have buttons to **accept**, **delete**, or **request
  changes** to a host's data. Host administrators can update details via
  the mini-app, schedule reminders, or remove outdated entries.
- If a host is caught bribing users for ratings, moderators can
  **reset that host's score** and flag the activity.

### Reviews & Moderation
- All reviews arrive in the hoster's dedicated topic with
  **Allow/Reject** options.
- Moderators can flag suspicious activity; rating spikes are reported in
  a separate topic linking back to the host chat.
- Built‑in tools reduce spam and fake accounts.

### Supergroup Topics
- Each host receives a **dedicated topic** in the supergroup where all
  provided data is stored and pinned for reference. The topic doubles as
  a chat between moderators and the host administrator.
- Buttons in the topic send automated messages such as data refresh
  requests or low‑rating warnings, and all incoming reviews are forwarded
  there with **Allow/Reject** actions.

### Search & Recommendation
- Users can **search** and filter hosts by service type, rating,
  location, or price range.
- Search history is stored to refine **personalized recommendations**.

### Notifications and Reminders
- Scheduled reminders ask host admins to confirm or update their info.
- Hosts receive alerts about rating drops, new reviews, or policy
  violations.
- Users may subscribe to categories and receive recommendations that fit
  their preferences or service updates.

### Support & Feedback
- A built-in **support system** lets users report problems or ask
  questions directly from the mini-app.
- Frequently asked questions and search history help users find answers
  quickly.

### Administration & Configurability
- Administrators can add or remove host information, reviews, and
  categories directly within the bot.
- The rating formula and evaluation criteria are adjustable to keep the
  system fair and neutral.
- Activity logs and alerts help detect suspicious behavior and provide
  transparency for moderator decisions.

### Anti‑Spam & Security
- The bot detects suspicious review spikes and throttles mass activity.
- Verified owner checks prevent impersonation. If a host is caught buying
  positive reviews, the rating is reset.
- Rate limiting, reputation checks, and anomaly detection help prevent
  fake votes or review spam. Multiple protections guard against bot
  manipulation.

### API and Future Plans
- A public **REST API** will provide access to ratings, host data, and
  statistics for external integrations.
- English and Russian interfaces are planned from the start,
  with the option to add more languages later.
- Additional analytics, advanced recommendation algorithms, and import/export tools are planned for future releases.

## Administration
- Administrators can easily add or remove hoster information, reviews,
  and categories through bot commands or the mini‑app interface.
- Moderators oversee all content to ensure neutrality and prevent
  manipulation.
- Activity logs and alerts help detect suspicious behavior and maintain
  data integrity.
- The project remains non-commercial and community-driven with no paid
  rankings or advertisements.

## Getting Started
1. Clone this repository.
2. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the SQLite database and run migrations with Alembic:
   ```bash
   alembic upgrade head
   ```
4. Provide your Telegram API token in the environment or a config file.
5. Start the services during development:
   ```bash
   python bot/main.py         # Telegram bot
   uvicorn webapp.app:app --reload  # Web app
   ```
6. Open the mini-application through Telegram and use the supergroup
   topics to manage host submissions and reviews.


Contribution guidelines and additional deployment instructions will be
added as the project evolves.

### Running Migrations
Migration scripts live in the `data/` directory created by Alembic. Useful commands:
```bash
alembic revision -m "message"  # create migration
alembic upgrade head           # apply migrations
```

## Deployment
The services can run in Docker containers so they are easy to move to
other servers or a panel such as **Pterodactyl**. The same SQLite (or
later PostgreSQL) database is shared between the bot and web app. Logs
are written to files by default, and enabling the debug mode provides
extra details for troubleshooting.

