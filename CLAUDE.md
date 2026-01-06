# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Syllabus-Scraper is a Flask web application that generates Markdown syllabi from Udemy course URLs. Users paste a Udemy course link, and the app fetches the curriculum via the Udemy API and returns formatted Markdown.

Live site: https://syllabuscraper.com

## Development Commands

### Local Development with Docker
```bash
docker-compose up --build          # Start dev environment (Flask + PostgreSQL)
docker-compose down                # Stop containers
```

### Production
```bash
docker-compose -f docker-compose.prod.yml up --build
```

### Run Flask directly (requires manual DB setup)
```bash
cd services/web
python run.py
```

## Architecture

```
services/web/
├── project/
│   ├── __init__.py         # Flask app initialization, SQLAlchemy config
│   ├── connect_unix.py     # Database connection URL builder (supports Cloud SQL unix sockets)
│   ├── models.py           # SQLAlchemy models: UdemyCourseList, Course
│   └── udemy/
│       ├── views.py        # Flask routes: /, /update, /getsyllabus
│       └── factory.py      # Core logic: extracts course ID from URL, fetches curriculum from API
├── UdemyAPI/
│   └── udemy/udemy.py      # PyUdemy client wrapper for Udemy API
└── run.py                  # Application entry point
```

### Data Flow
1. User submits Udemy URL → `/update` route
2. `Factory.getCourseID()` scrapes the page to extract the course ID from `data-clp-course-id`
3. `Factory.getCurriculumFromApi()` calls Udemy API via `PyUdemy` to fetch curriculum
4. Results cached in PostgreSQL (UdemyCourseList + Course tables)
5. Markdown syllabus returned to frontend

### Key Models
- **UdemyCourseList**: Course metadata (id, name, link, searchcount)
- **Course**: Syllabus content with timestamps (course_syllabus, last_update, last_visit)

## Environment Variables

Required for database connection:
- `DB_USER`, `DB_PASS`, `DB_NAME`, `DB_HOST`, `DB_PORT` (local)
- `INSTANCE_UNIX_SOCKET` (Cloud SQL production)

Required for Udemy API:
- `udemyClientID`, `udemyClientSecret` (get from https://www.udemy.com/user/edit-api-clients/)

## Tech Stack
- Flask 2.2 with Flask-SQLAlchemy
- PostgreSQL 13 (via psycopg2 or pg8000 for Cloud SQL)
- BeautifulSoup4 for HTML parsing
- Gunicorn for production serving
- Docker Compose for containerization
