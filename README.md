# 🏥 Healthcare Backend — Django + DRF + PostgreSQL + Docker

A production‑style backend for a healthcare management system built with:

* Django
* Django REST Framework (DRF)
* PostgreSQL
* Docker & Docker Compose
* JWT Authentication (SimpleJWT)

The system supports user authentication and secure management of **patients**, **doctors**, and **patient–doctor mappings** via REST APIs.

---

# 📦 Tech Stack

* Python 3.11
* Django
* Django REST Framework
* PostgreSQL 15
* Docker & Docker Compose
* djangorestframework-simplejwt

---

# 📁 Project Structure

```
healthcare/
├── healthcare/          # Django project config
├── accounts/            # Custom user + auth APIs
├── patients/            # Patient model + APIs
├── doctors/             # Doctor model + APIs
├── mappings/            # Patient–Doctor mapping APIs
├── manage.py

Dockerfile

docker-compose.yml
.env
requirements.txt
```

---

# 🚀 Getting Started

## 1️⃣ Clone Repository

```bash
git https://github.com/prasangeet/Healthcare-Backend.git
cd Healthcare-Backend
```

---

## 2️⃣ Create Environment File

Create `.env` in project root:

```env
DEBUG=True
SECRET_KEY=change-me

POSTGRES_DB=healthcare
POSTGRES_USER=healthcare_user
POSTGRES_PASSWORD=healthcare_pass
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

---

## 3️⃣ Install Docker (if not installed)

Linux (Fedora example):

```bash
sudo dnf install docker docker-compose-plugin
sudo systemctl enable --now docker
```

Arch Linux

```bash
sudo pacman -S docker docker-compose
sudo systemctl enable --now docker
```

Add user to docker group:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

Verify:

```bash
docker --version
docker compose version
```

---

## 4️⃣ Start Services

Build and start containers:

```bash
docker compose up --build
```

Run in background:

```bash
docker compose up -d --build
```

---

## 5️⃣ Run Migrations

```bash
docker compose exec django python manage.py migrate
```

---

## 6️⃣ Access Server

```
http://localhost:8000
```

---

# 🔐 Authentication

Uses **JWT tokens**.

Login returns:

* access token
* refresh token

Send token in header:

```
Authorization: Bearer <access_token>
```

---

# 👤 Auth APIs

## Register

```
POST /api/auth/register/
```

Body:

```json
{
  "username": "alice",
  "email": "alice@test.com",
  "password": "alice12345"
}
```

---

## Login

```
POST /api/auth/login/
```

```json
{
  "email": "alice@test.com",
  "password": "alice12345"
}
```

Returns JWT tokens.

---

## Current User

```
GET /api/auth/me/
```

Auth required.

---

# 🧑‍⚕️ Patient APIs

All endpoints require authentication.

## Create Patient

```
POST /api/patients/create/
```

```json
{
  "name": "John Doe",
  "age": 45,
  "gender": "male",
  "diagnosis": "Hypertension"
}
```

---

## List My Patients

```
GET /api/patients/
```

Returns only patients created by authenticated user.

---

## Get Patient

```
GET /api/patients/<id>/
```

---

## Update Patient

```
PUT /api/patients/<id>/update/
```

---

## Delete Patient

```
DELETE /api/patients/<id>/delete/
```

---

# 👨‍⚕️ Doctor APIs

Doctors are global records.

## Create Doctor

```
POST /api/doctors/create/
```

---

## List Doctors

```
GET /api/doctors/
```

---

## Get Doctor

```
GET /api/doctors/<id>/
```

---

## Update Doctor

```
PUT /api/doctors/<id>/update/
```

---

## Delete Doctor

```
DELETE /api/doctors/<id>/delete/
```

---

# 🔗 Patient–Doctor Mapping APIs

## Assign Doctor to Patient

```
POST /api/mappings/create/
```

```json
{
  "patient": 1,
  "doctor": 2
}
```

Unique constraint prevents duplicates.

---

## List My Mappings

```
GET /api/mappings/
```

---

## Get Doctors for Patient

```
GET /api/mappings/patient/<patient_id>/
```

---

## Remove Mapping

```
DELETE /api/mappings/<id>/delete/
```

---

# 🛡️ Security Features

* JWT authentication
* Custom user model (email login)
* Ownership enforcement on patients
* Mapping validation
* Unique mapping constraints
* Serializer validation
* Global error handler

---

# 🧪 Testing

Use:

* Postman
* curl
* HTTPie

Example:

```bash
curl -H "Authorization: Bearer <token>" http://localhost:8000/api/patients/
```

---

# 🐳 Docker Commands

Start:

```bash
docker compose up -d
```

Stop:

```bash
docker compose down
```

Logs:

```bash
docker compose logs -f django
```

Shell inside container:

```bash
docker compose exec django bash
```

---

# 📌 Notes

* PostgreSQL runs in Docker
* Django connects using service name `postgres`
* Environment variables used for secrets
* Function-based API views used throughout

---

# ✅ Assignment Requirements Covered

* Django + DRF backend
* PostgreSQL database
* JWT authentication
* Patient CRUD APIs
* Doctor CRUD APIs
* Mapping APIs
* Validation & error handling
* Dockerized setup

---

# 🎯 Ready for Extension

Possible upgrades:

* Swagger docs
* Role-based access
* Admin dashboards
* Audit logs
* Soft deletes

---

**Done. Backend is fully functional and containerized.** 🚀
