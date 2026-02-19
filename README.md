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
