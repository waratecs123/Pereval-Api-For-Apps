# Mountain Passes REST API

## Overview

The **Mountain Passes REST API** is a backend application built using **Django REST Framework (DRF)**.
It is designed to manage and store data about tourist mountain passes, including coordinates, user submissions, and difficulty levels.
The system supports a moderation workflow and image uploads, allowing users to contribute new pass information while ensuring quality control through administrative review.

The API is suitable for use by mobile applications, web interfaces, or other services that collect and process geographic and tourism-related data.

---

## Key Features

* **User Submissions** — Collect mountain pass data directly from users with validated contact information.
* **Moderation Workflow** — Each submission passes through status stages: *new*, *pending*, *accepted*, *rejected*.
* **Geolocation Tracking** — Each pass includes precise GPS coordinates (latitude, longitude, altitude).
* **Seasonal Difficulty Levels** — Define separate difficulty ratings for winter, summer, autumn, and spring.
* **Image Uploads** — Support for multiple images per pass, stored with descriptive titles.
* **Search and Filtering** — Retrieve passes by user email, pass ID, or status.
* **RESTful Architecture** — Built on Django REST Framework, enabling easy integration with external systems.

---

## Technologies

| Component            | Description                                    |
| -------------------- | ---------------------------------------------- |
| **Language**         | Python 3.10+                                   |
| **Framework**        | Django 4.2+                                    |
| **API Toolkit**      | Django REST Framework                          |
| **Database**         | PostgreSQL (production) / SQLite (development) |
| **Image Processing** | Pillow                                         |
| **Version Control**  | Git / GitHub                                   |

---

## Core Data Models

| Model            | Description                                                                       |
| ---------------- | --------------------------------------------------------------------------------- |
| **User**         | Submitter profile with validated email and phone fields.                          |
| **Pereval**      | Core entity representing a mountain pass, with metadata and moderation status.    |
| **Coord**        | Stores geographic coordinates (latitude, longitude, altitude).                    |
| **Level**        | Defines difficulty levels for each season (winter, summer, autumn, spring).       |
| **Image**        | Stores uploaded photos with titles, timestamps, and base64 or file references.    |
| **ActivityType** | Optional list of supported activities (e.g., hiking, skiing, climbing).           |
| **Area**         | Hierarchical structure for geographic regions (e.g., mountain ranges, districts). |

---

## API Endpoints

### 1. Submit a New Mountain Pass

`POST /api/submitData/`

**Request Example:**

```json
{
  "beauty_title": "Beautiful Pass",
  "title": "Test Pass",
  "user": {
    "email": "user@example.com",
    "phone": "79031234567",
    "fam": "Ivanov",
    "name": "Petr",
    "otc": "Sergeevich"
  },
  "coords": {
    "latitude": 45.1234,
    "longitude": 90.1234,
    "height": 2000
  },
  "level": {
    "winter": "1A",
    "summer": "1B",
    "autumn": "",
    "spring": ""
  },
  "images": [
    {"title": "North View", "data": "base64_encoded_image"}
  ]
}
```

**Response Example:**

```json
{
  "status": "success",
  "message": "Submission received and pending moderation.",
  "id": 1023
}
```

---

### 2. Retrieve Pass by ID

`GET /api/submitData/<id>/`

Returns detailed information about a specific mountain pass submission.

**Example Response:**

```json
{
  "id": 1023,
  "title": "Test Pass",
  "beauty_title": "Beautiful Pass",
  "status": "pending",
  "coords": {
    "latitude": 45.1234,
    "longitude": 90.1234,
    "height": 2000
  },
  "level": {
    "winter": "1A",
    "summer": "1B"
  },
  "user": {
    "email": "user@example.com",
    "fam": "Ivanov",
    "name": "Petr",
    "otc": "Sergeevich"
  },
  "images": [
    {"title": "North View", "url": "/media/passes/1023/north_view.jpg"}
  ]
}
```

---

### 3. Update Existing Submission

`PATCH /api/submitData/<id>/`

Allows partial updates of a record if its moderation status is **new** or **pending**.

**Example Request:**

```json
{
  "beauty_title": "Updated Pass Name",
  "coords": {
    "latitude": 45.1111,
    "longitude": 90.2222,
    "height": 2100
  }
}
```

**Example Response:**

```json
{
  "status": "updated",
  "message": "Changes saved successfully."
}
```

If the pass is already accepted or rejected, the API will return an error:

```json
{
  "status": "error",
  "message": "Modification is not allowed for approved submissions."
}
```

---

### 4. Get Submissions by User Email

`GET /api/submitData/?user__email=user@example.com`

Retrieves all mountain passes submitted by a particular user.

**Example Response:**

```json
[
  {
    "id": 1001,
    "title": "Altai Ridge",
    "status": "accepted"
  },
  {
    "id": 1023,
    "title": "Test Pass",
    "status": "pending"
  }
]
```

---

## Moderation Workflow

Each submission passes through the following statuses:

| Status       | Description                                |
| ------------ | ------------------------------------------ |
| **new**      | Submitted by user, waiting for review.     |
| **pending**  | Under moderation process.                  |
| **accepted** | Verified and approved by moderators.       |
| **rejected** | Denied due to incorrect or duplicate data. |

The API automatically restricts user editing once a pass is accepted or rejected.

---

## Installation and Setup

### Prerequisites

* Python 3.10 or higher
* Django 4.2 or higher
* PostgreSQL or SQLite
* Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/waratecs123/Mountain-Passes-REST-API.git
   cd Mountain-Passes-REST-API
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate          # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database settings** in `settings.py` under `DATABASES`.
   Example for PostgreSQL:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'mountain_passes',
           'USER': 'postgres',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. Access the API:

   ```
   http://127.0.0.1:8000/api/
   ```

---

## Testing

To execute automated tests:

```bash
python manage.py test
```

You can add additional tests under `tests/` directories in each Django app.
Tests should cover model validation, endpoint responses, and data integrity.

---

## Deployment

For production deployment, the recommended stack includes:

* **Gunicorn** as the WSGI application server
* **Nginx** for reverse proxy and static/media file serving
* **PostgreSQL** as the primary database
* **Docker** containers (optional) for portability

Ensure you set environment variables:

* `DEBUG=False`
* `ALLOWED_HOSTS`
* `DATABASE_URL`
* `SECRET_KEY`

Run with Gunicorn:

```bash
gunicorn mountainpasses.wsgi:application
```

---

## Contributing

Contributions are encouraged. Follow these steps:

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes with clear messages.
4. Push your branch and create a pull request.

All code contributions must comply with **PEP 8**, **DRF best practices**, and include tests if applicable.

---

## License

This project is released under the **MIT License**.
You may freely use, modify, and distribute this software, provided that the license terms are retained.

---

## Author

**Developed by Waratecs**
For issues, feature requests, or collaboration opportunities, please open a GitHub issue or contact via your developer profile.

