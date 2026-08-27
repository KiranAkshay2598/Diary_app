# Digital Diary API

A clean Django REST Framework backend application designed for managing personal digital diary entries, daily to-do lists, and event schedules. Originally built as a practice learning project when preparing for backend interviews as a fresher in the 1st quarter of 2021, demonstrating core Django concepts, RESTful API design, and clean code standards.

---

## Key Features

* **User Authentication & Management**: Token-based user registration and authentication using Django REST Framework (`rest_framework.authtoken`).
* **Diary Notes Management**: Create and view personal notes with support for timestamped dates and image attachments.
* **To-Do Task Tracking**: Create to-do lists associated with specific diary notes and update task completion status.
* **Event Scheduling**: Schedule events with date/time conflict detection to prevent double-booking.
* **Media Handling**: Configured media upload processing for note attachments.
* **Modern Standards**: Python 3.11 compatibility, clean service-layer architecture, strict type checking, and explicit PEP8-compliant imports.

---

## Tech Stack

* **Framework**: Django 3.1 & Django REST Framework 3.12
* **Language**: Python 3.11
* **Database**: SQLite (Development)
* **Authentication**: DRF Token Authentication
* **Media Processing**: Pillow

---

## Repository Structure

```
Digital_diary/
├── diary/                   # Django inner settings & configuration package
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── diary_app/               # Primary Django application
│   ├── models.py            # Database models (Diary, Notes, ToDo, Events)
│   ├── serializers.py       # DRF Serializers & custom validation
│   ├── services.py          # Core business logic & transaction layer
│   ├── views.py             # API View controllers with IsAuthenticated rules
│   └── urls.py              # Endpoint routing
├── postman/                 # Postman collection for API testing
│   └── Digital_Diary.postman_collection.json
├── .gitignore               # Excludes virtual environments, db, and media files
├── manage.py                # Django command-line utility
└── requirements.txt         # Project dependencies
```

---

## Getting Started

### Prerequisites
* Python 3.11+
* Git

### Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KiranAkshay2598/Diary_app.git
   cd Diary_app
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

The API will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints Summary

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/diary/register` | Register a new user | No |
| `POST` | `/api/diary/login` | Log in and receive auth token | No |
| `POST` | `/api/diary/notes` | Create a new diary note (supports image upload) | Yes |
| `GET` | `/api/diary/viewnotes` | Retrieve notes (optional filter by `note_date` or `note`) | Yes |
| `POST` | `/api/diary/todo` | Add a to-do item linked to a note | Yes |
| `POST` | `/api/diary/updatetodo` | Mark to-do item as completed | Yes |
| `POST` | `/api/diary/events` | Schedule a new event | Yes |
| `GET` | `/api/diary/viewevents` | Retrieve scheduled events | Yes |
| `POST` | `/api/diary/updateevents` | Activate event reminder status | Yes |

---

## Postman Collection

A pre-configured Postman collection is included in the `postman/` directory:
* File: `postman/Digital_Diary.postman_collection.json`

**To use**:
1. Open Postman.
2. Click **Import** and select `Digital_Diary.postman_collection.json`.
3. Set your `Authorization` header to `Token <your_token>` after registering or logging in.
