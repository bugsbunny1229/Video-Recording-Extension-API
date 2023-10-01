# Video Recording Extension API

A specialized Django-based API service designed to support video recording functionality in Chrome Extensions, enabling seamless video capture, storage, and management capabilities.

## Features

- RESTful API endpoints for Chrome Extension integration
- Cloud storage integration using Cloudinary
- Secure database management
- Comprehensive API documentation
- Modern Django-based architecture

## Project Structure

```
Video_Recording_Extension_API/
├── api/              # Main API application
├── core/             # Django project configuration
├── media/            # Media files storage
├── .github/          # GitHub workflows
└── Documentation.md  # Detailed project documentation
```

## Technical Stack

- Backend: Django 4.2.5
- Database: SQLite
- API Framework: Django REST Framework
- Cloud Storage: Cloudinary
- Documentation: Swagger/OpenAPI (drf-yasg)

## Prerequisites

- Python 3.8+
- pip
- SQLite
- Node.js (for Chrome Extension development)

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

## API Documentation

Once the server is running, you can access the API documentation at:
```
http://localhost:8000/swagger/
```

## Acknowledgments

- Django framework
- Django REST Framework
- Cloudinary
- All contributors who have helped shape this project
