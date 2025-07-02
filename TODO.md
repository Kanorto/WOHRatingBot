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
