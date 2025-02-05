# BlogApp Backend

A high-performance blog application backend built with FastAPI, SQLAlchemy, and PostgreSQL. Features JWT authentication, CRUD operations for blog posts, and user management.

## Features

- ✅ JWT Authentication & Authorization
- ✅ User registration and management
- ✅ Blog post creation, update, deletion
- ✅ Alembic database migrations
- ✅ SQLAlchemy ORM integration
- ✅ Pydantic schema validation
- ✅ Repository pattern architecture
- ✅ Proper separation of concerns (routes, schemas, models, repositories)
- ✅ Automated API documentation (Swagger UI & ReDoc)

## Technologies

- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy** (ORM)
- **Alembic** (Database migrations)
- **PostgreSQL** (Database)
- **JWT** (Authentication)
- **Pydantic** (Data validation)
- **Poetry** (Dependency management - recommended)

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL database

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nurgoni/fastapi-blog-app.git
   cd fastapi-blog-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create `.env` file in root directory:
   ```bash
   SECRET_KEY=your-secret-key-here
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   etc...
   ```
4. setup database:
   ```bash
   alembic upgrade head
   ```
### Running the Application

Interactive API documentation available after running the server:

- Swagger UI: `http://localhost:8000/docs`

## Project Structure
```plain
.
├── alembic/                 # Database migration scripts
├── backend/                 # Main application package
│   ├── api/                 # API endpoints
│   │   ├── v1/             # API version 1
│   │   │   ├── route_blog.py
│   │   │   ├── route_login.py
│   │   │   └── route_user.py
│   ├── core/               # Core configurations
│   │   ├── config.py
│   │   ├── hashing.py
│   │   └── security.py
│   ├── db/                 # Database configurations
│   │   ├── models/         # Database models
│   │   │   ├── blog.py
│   │   │   └── user.py
│   ├── repository/         # Database repository layer
│   │   ├── blog.py
│   │   ├── login.py
│   │   └── user.py
│   ├── schemas/            # Pydantic schemas
│   │   ├── blog.py
│   │   ├── login.py
│   │   └── user.py
│   └── main.py             # Application entry point
├── .gitignore
├── alembic.ini             # Alembic configuration
├── Makefile                # Useful commands
├── README.md
└── requirements.txt        # Dependencies
```