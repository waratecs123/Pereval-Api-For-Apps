# Mountain Passes REST API

A Django REST Framework API for managing tourist mountain pass information with user submissions, coordinates tracking, and image uploads.

## Key Features
- **User submissions** with email/phone validation
- **Moderation workflow** (new/pending/accepted/rejected)
- **Geolocation tracking** with precise coordinates
- **Difficulty levels** for different seasons
- **Image uploads** with titles
- **Search functionality** by user email or pass ID

## Technologies
- Python 3.10+
- Django 4.2+
- Django REST Framework
- PostgreSQL (production) / SQLite (development)
- Pillow (image processing)

## Core Models
| Model | Description |
|-------|-------------|
| `User` | Submitter information with email validation |
| `Pereval` | Mountain pass data with moderation status |
| `Coord` | GPS coordinates (latitude/longitude/altitude) |
| `Level` | Difficulty levels by season (winter/summer/autumn/spring) |
| `Image` | Pass photos with titles and timestamps |
| `ActivityType` | Allowed activities (hiking, climbing, etc.) |
| `Area` | Geographical regions hierarchy |

## API Endpoints

### 1. Submit New Mountain Pass
`POST /api/submitData/`
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
