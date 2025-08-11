# 🏔️ Mountain Passes REST API

A Django REST Framework API for managing tourist mountain pass information with user submissions, coordinates tracking, and image uploads.

## 🛠️ Technologies
- Python 3.10+
- Django 4.2+
- Django REST Framework
- PostgreSQL (default) / SQLite (dev)
- Pillow (image processing)

## 📌 Core Models
| Model | Description |
|-------|-------------|
| `User` | Submitter information with email validation |
| `Pereval` | Mountain pass data with moderation status |
| `Coord` | GPS coordinates (lat/long/altitude) |
| `Level` | Difficulty levels by season |
| `Image` | Pass photos with titles |
| `ActivityType` | Allowed activities |
| `Area` | Geographical regions hierarchy |

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL (optional)

### Installation
```bash
# Clone repository
git clone https://github.com/yourrepo/mountain-passes-api.git
cd mountain-passes-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
