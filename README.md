# Flask URL Shortener
A secure and efficient URL shortener built with Flask, JWT authentication, and SQLAlchemy.
## 📌 Project Overview

This is a full-stack web application that allows users to:

- Register and login securely using JWT authentication.

- Shorten long URLs into easy-to-share short codes.

- Track the number of clicks for each shortened URL.

- Redirect users to the original URL when the short link is accessed.

- Apply rate limiting to prevent abuse.

The project is built with Flask, SQLAlchemy, Flask-Limiter, and Flask-JWT-Extended.
## Technologies Used

- Backend: Python, Flask, Flask-JWT-Extended, Flask-Limiter, SQLAlchemy

- Database: MySQL (local) / can be switched to cloud DB (Postgres/MySQL)

- Frontend: Minimal HTML with form inputs

- Security: Password hashing with Bcrypt, JWT tokens for authentication

- Utilities: python-dotenv for environment variables
## Features

- User Authentication

  - Register new users

  - Login existing users

  - JWT-based secure authentication

- URL Shortening

  - Generate unique short codes for long URLs

  - Prevent duplicate URL entries

  - Redirect users from short link to original URL

- Analytics

  - Track clicks for each shortened URL

  - Expiration mechanism for URLs (optional)

- Rate Limiting

  - Limit the number of API requests per user (e.g., 200/day, 50/hour)
## Project Structure

URL-project/
│
├── app.py              # Main Flask app
├── config.py           # App configuration
├── extensions.py       # Flask extensions (db, bcrypt, JWT)
├── index.html          # Basic frontend
├── models/             # SQLAlchemy models
│   ├── user.py
│   └── url.py
├── routes/             # API routes
│   ├── auth_routes.py
│   └── url_routes.py
├── utils/              # Helper functions
│   └── generator.py
├── requirements.txt    # Python dependencies
└── .gitignore

## Installation & Setup

- Clone the repository:
  - git clone https://github.com/ShakeenaMahima/url-shortener-flask.git
  - cd url-shortener-flask

- Create and activate a virtual environment:
  - python -m venv .venv
  - .\.venv\Scripts\activate
  - source .venv/bin/activate

- Install dependencies:
  - pip install -r requirements.txt
  
- Create a .env file:
  - DATABASE_URL=mysql+pymysql://root:password@localhost/url_shortener
  - SECRET_KEY=your-secret-key
  - JWT_SECRET_KEY=your-jwt-secret-key

- Run the app:
  - $env:FLASK_APP="app.py"       # Windows PowerShell
  - flask run
## Usage

- Register a user via the /register endpoint.

- Login via the /login endpoint.

- Shorten a URL via /shorten.

- Redirect to the original URL using the short code.

- View click analytics by checking the database or API endpoints.
