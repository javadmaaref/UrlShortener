# URL Shortener Service

A simple URL shortening service built using **Django**. This service allows users to shorten long URLs into concise, unique, and easily shareable links. Additionally, the shortened links can redirect users back to the original URLs.

---

## Table of Contents
1. [Features](#features)
2. [Algorithm Overview](#algorithm-overview)
3. [Getting Started](#getting-started)
4. [Project Structure](#project-structure)
5. [Usage](#usage)

---

## Features
- **Shorten URLs**: Convert long URLs into short, unique identifiers.
- **Redirect**: Navigate users to the original URL using the short URL.
- **Unique Identifier Algorithm**: A custom base conversion algorithm ensures unique short URLs.
- **CSRF Protection**: Secure requests to prevent cross-site forgery attacks.
- **Minimalistic UI**: A simple, user-friendly interface to shorten URLs quickly.

---

## Algorithm Overview
The URL shortening algorithm is based on **Base Conversion**. Here's how it works:

1. **Database Record Identification**: Each URL entry in the database is assigned a unique ID.
2. **Base62 Encoding**: This ID is converted into a unique string using characters from a predefined set (`A-Za-z0-9`).
    - The character set consists of **62 characters**: 26 lowercase letters, 26 uppercase letters, and 10 digits.
3. **Short URL Generation**:
    - Convert the unique numeric ID of the database record into a Base62 string.
    - The resulting string is the "short URL".

**Algorithm Code (Base Conversion):**
```python
import string

characters = string.ascii_letters + string.digits  # Character set for Base62

def base_conversion(num):
    if num == 0:
        return characters[0]
    arr = []
    base = len(characters)
    while num:
        rem = num % base
        num = num // base
        arr.append(characters[rem])
    arr.reverse()
    return ''.join(arr)
```

This ensures the short URLs are both compact and unique.

---

## Getting Started

Follow these steps to set up and run the project locally:

### Prerequisites
- **Python**: Version 3.6 or higher.
- **Django**: Installed using pip.
- **Virtualenv** (optional but recommended): To manage dependencies.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/javadmaaref/UrlShortener.git
   cd UrlShortener
   ```

2. **Set Up a Virtual Environment** (optional):
   ```bash
   pip install virtualenv
   virtualenv venv
   # Activate virtual environment:
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate   # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install django
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   python manage.py makemigrations shortener
   python manage.py migrate
   ```

5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## Project Structure

```
UrlShortener/
├── manage.py
├── shortener/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── ...
│   ├── models.py
│   ├── static/
│   │   └── shortener/
│   │       └── styles.css
│   ├── templates/
│   │   └── shortener/
│   │       └── home.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── url_shortener/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── db.sqlite3
```

---

## Usage

### Shorten a URL
1. Navigate to the homepage: `http://127.0.0.1:8000/`
2. Enter a long URL in the input field.
3. Click on the "Shorten" button.
4. A shortened URL will be generated and displayed.

### Redirect Using a Short URL
1. Copy the generated short URL.
2. Paste it into your browser's address bar and hit Enter.
3. You will be redirected to the original long URL.

### API Endpoints
- **POST `/shorten/`**:
  - Request: `{ "original_url": "<your_long_url>" }`
  - Response: `{ "short_url": "http://127.0.0.1:8000/<short_code>" }`
- **GET `/<short_code>/`**:
  - Redirects to the original URL.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.
