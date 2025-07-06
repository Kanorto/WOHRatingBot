# TODO List for WOHRatingBot

This document outlines the main tasks needed to transform the README description into a fully functioning project. Items are grouped by area and ordered roughly by priority.

## 1. Project Setup
- [ ] Initialize Python project with **aiogram** for the Telegram bot and **FastAPI** for the web application.
- [ ] Create a shared virtual environment and add `requirements.txt`.
- [ ] Configure logging with separate debug mode and log rotation.
- [ ] Provide a unified SQLite database using **SQLAlchemy** and **Alembic** for migrations.
- [ ] Add multi-language support (English and Russian) to both bot and web app.

## 2. Core Telegram Bot
- [ ] Basic command handlers (`/start`, `/help`, `/language`, etc.).
- [ ] Integration with Telegram supergroup topics for host discussions.
- [ ] Buttons for moderators to approve or reject data (hosts, reviews, etc.).
- [ ] Notifications and reminders about rating drops, new reviews, or policy violations.
- [ ] Anti-spam tools: rate limiting, detection of suspicious review spikes.

## 3. Web Application (Mini-App)
- [ ] Build FastAPI app with routes for viewing hosts, submitting reviews, and administration.
- [ ] Create HTML/JS front end that can be served as a Telegram Web App.
- [ ] Implement search and filtering by service type, rating, location, and price.
- [ ] Support user profiles with history of votes and reviews.
- [ ] REST API endpoints for external integrations (ratings, host data, stats).

## 4. Database Models
- [ ] Users, hosters, reviews, ratings, and categories.
- [ ] Relationship tables for votes, subscriptions, and search history.
- [ ] Migration scripts for evolving the schema.

## 5. Administration Tools
- [ ] Bot commands and web forms for moderators to manage hosts and reviews.
- [ ] Activity logs with full details of user actions.
- [ ] Export/import utilities and future integration with Pterodactyl panel.

## 6. Testing & CI
- [ ] Unit tests for bot handlers and web routes.
- [ ] Linting and formatting checks (e.g., flake8, black).
- [ ] GitHub Actions or similar for automated testing.

## 7. Deployment
- [ ] Dockerfile and docker-compose setup to run bot and web app together.
- [ ] Instructions for deployment on Pterodactyl or similar panel.

---

This list can be expanded as the project grows. For now, it serves as the roadmap to build the first working version of WOHRatingBot.


## Next Steps (Core Implementation)

1. **Database Schema**
   - [ ] Define `Hoster` model with service categories, location, and contacts.
   - [ ] Define `Review` and `Rating` models linked to `User` and `Hoster`.
   - [ ] Add Alembic migrations for initial tables.
2. **Bot Commands**
   - [ ] `/add_host` and `/my_hosts` commands for administrators.
   - [ ] `/review` command for users to submit a review via the web app.
   - [ ] Callback handlers for moderator approval buttons.
3. **Web App Views**
   - [ ] Host list and detail pages using Jinja2 templates.
   - [ ] Review submission form with validation.
   - [ ] Admin dashboard to confirm or update host information.
4. **Logging**
   - [ ] Implement structured logging to file with rotation.
   - [ ] Add verbose debug mode controlled by environment variable.
5. **Testing**
   - [ ] Start unit tests for basic models and handlers.
   - [ ] Configure test database and example fixtures.

These tasks build directly on the ideas outlined in the README: a single database, moderator approval workflow, and transparent ratings in both English and Russian.

## Ordered Development Roadmap

1. **Environment setup and config loading**
   - [ ] Create a local virtual environment and install dependencies.
   - [ ] Add an example `.env` file and implement a config loader.
   - [ ] Configure the database engine and create a shared session manager.
   - [ ] Set up basic logging configuration with a debug flag.

2. **Database schema design and Alembic migrations**
   - [ ] Define core models (`User`, `Hoster`, `Review`, `Rating`).
   - [ ] Generate initial Alembic migrations and commit the schema.
   - [ ] Configure `alembic.ini` and the migration environment.
   - [ ] Provide optional seed data for development.

3. **Core bot commands and callbacks**
   - [ ] Implement `/start` and `/help` commands.
   - [ ] Add `/add_host` handler for administrators.
   - [ ] Create callback handlers for approve/reject buttons.
   - [ ] Integrate session middleware for database access.

4. **Web app routes and templates**
   - [ ] Build host list template and route.
   - [ ] Add host detail page with rating information.
   - [ ] Implement review submission form.
   - [ ] Draft admin dashboard templates.

5. **Logging and debug features**
   - [ ] Enable structured logging with rotation.
   - [ ] Toggle verbose debug mode via configuration.
   - [ ] Add detailed error handlers for bot and web app.

6. **Admin tools and moderation workflow**
   - [ ] Implement interface to approve new hosts and reviews.
   - [ ] Build a moderation queue with role checks.
   - [ ] Display activity logs for administrators.
   - [ ] Enforce permissions for sensitive actions.

7. **Deployment scripts and Docker setup**
   - [ ] Create Dockerfile for bot and web application services.
   - [ ] Provide `docker-compose` configuration with the database.
   - [ ] Include sample environment files for deployment.
   - [ ] Add helper scripts for running migrations in containers.

