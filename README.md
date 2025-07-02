# WOHRatingBot

WOHRatingBot is a Telegram bot and mini-application for the **World_of_hosts** community. Its goal is to maintain a fully transparent, non-commercial rating of hosting providers. Users can explore hosters, leave reviews, and see detailed statistics, while verified administrators keep their information current. Moderation happens in a Telegram supergroup where each host has its own discussion topic.

## Overview
- **Transparency first.** Ratings are public, free, and based solely on community feedback.
- **Mini-app experience.** The Telegram web app lets users browse hosts and vote with ease.
- **Supergroup integration.** Host topics in a Telegram supergroup keep all data and discussions organized.
- **Extensibility.** New rating categories and service types can be added without code changes.

## Features
### Mini-Application
- **Host profiles** contain required details: service descriptions, pricing, website, control panel, and social links (Telegram, YouTube, etc.).
- **Voting and reviews** use 1–5 star scores with optional text. Every submission must be approved by a moderator before publication.
- **Rating breakdown** by criteria such as service type, price/quality ratio, reliability, support quality, and custom metrics.
- **Recommendation system** suggests hosts based on location, service type, budget, and past searches.
- **Search history** allows users to revisit previous queries quickly.

### Host Management
- Any user may **submit a host** for verification. Ownership must be proven before listing.
- Verified hosts receive a **special badge** in their profile.
- Administrators can update details through the mini-app with buttons for change requests, reminders, or removing outdated data.
- Hosts caught bribing users for ratings can have their scores **reset to zero** and flagged for review.

### Supergroup Topics
- The bot creates a **dedicated topic** for each host with all provided data pinned for easy reference.
- Topics double as chats with moderators. Buttons allow moderators to accept or reject hosts, send reminders, or delete entries.
- All reviews are forwarded to the topic where moderators can "Allow" or "Reject" them.
- Suspicious spikes in activity trigger alerts in a separate moderation topic.

### Notifications and Reminders
- Scheduled reminders prompt host admins to confirm or update their data.
- Hosts receive alerts about rating drops, new reviews, or policy violations.
- Users can opt in to notifications about host recommendations or service updates.

### Moderation and Anti-Spam
- Every piece of user-generated content—ratings, reviews, profile edits—is reviewed by moderators.
- Rate limiting, reputation checks, and anomaly detection help prevent fake votes or spam.
- All moderation actions are logged for transparency, and verified-owner checks prevent impersonation.

### Support and Feedback
- A built-in **support system** lets users report problems or ask questions from the mini-app.
- Frequently asked questions and previous searches help users find answers quickly.

### API and Future Plans
- A public **REST API** will expose ratings, host data, and statistics for external use.
- Additional analytics, advanced recommendation algorithms, import/export tools, and multi-language support are planned for later releases.

## Administration
- Administrators manage hosts, categories, and reviews using bot commands or the mini-app.
- Moderators ensure neutrality and may edit or remove any data that violates rules.
- Activity logs and alerts help detect suspicious behavior and maintain data integrity.
- The project is community-driven with no paid rankings or advertisements.

## Getting Started
1. Clone this repository.
2. Install dependencies and provide a Telegram API token.
3. Run the bot and open the mini-application from Telegram.
4. Use the supergroup topics to manage host submissions and reviews.

Further setup instructions and contribution guidelines will be added as the project evolves.
