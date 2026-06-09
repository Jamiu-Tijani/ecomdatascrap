# Ecom Data Scrap

A Django REST API that accepts a product search query and returns matching product information scraped from ecommerce stores such as Jumia.

## What this project does

The API is intended to make ecommerce product discovery easier by exposing scraped product search results through a backend service.

At a high level, the service:

1. Accepts a user search query.
2. Requests matching product pages from an ecommerce source.
3. Parses product data from the response.
4. Returns structured product results through the API.

## Tech Stack

- Python
- Django
- Django REST Framework
- BeautifulSoup
- Requests
- Gunicorn / WhiteNoise for deployment support

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

## Local Setup

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Then open the local API in your browser or API client:

```text
http://127.0.0.1:8000/home
```

## Notes

The original deployed endpoint was hosted on Heroku, but Heroku free dynos are no longer generally available. Treat any old Heroku URL as historical unless the app has been redeployed.

## Portfolio Improvement Checklist

To make this stronger as a portfolio/API project:

- Document the request and response format with examples.
- Add the exact endpoint paths and supported query parameters.
- Add error handling behavior for invalid or empty searches.
- Add tests for parser logic and API responses.
- Add rate limiting or caching notes for responsible scraping.
- Add deployment instructions for a current hosting target.
- Add a short note about respecting ecommerce site terms and robots rules.
