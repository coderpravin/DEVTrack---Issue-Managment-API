# DevTrack - Issue Management API

A simple **Django-based JSON API** for managing **Reporters** and **Issues**.

The project demonstrates **Python OOP concepts**, inheritance, validation, and JSON file-based data storage.

---

## 📁 Project Structure

```text
project/
│
├── devtrack/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── issue/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── screenshots/
│   └── screenshots.png
│
├── reporters.json
├── issues.json
└── manage.py
```

### Django App Configuration

The `issue` app is installed in the Django project through `devtrack/settings.py`.

```python
INSTALLED_APPS = [
    ...
    "issue",
]
```

The `issue` app contains the OOP classes, API views, validation logic, and URL configurations used by the project.

---

# 🧩 OOP Design

## 1. BaseEntity

`BaseEntity` is an **abstract base class** inherited by both `Reporter` and `Issue`.

It provides:

* `validate()` - validates the object data
* `to_dict()` - converts the object into a dictionary

---

## 2. Reporter

`Reporter` represents a person who reports an issue.

### Fields

| Field   | Description                       |
| ------- | --------------------------------- |
| `id`    | Unique reporter ID                |
| `name`  | Full name of the reporter         |
| `email` | Contact email                     |
| `team`  | Team associated with the reporter |

---

## 3. Issue

`Issue` represents an engineering issue.

### Fields

| Field         | Description                  |
| ------------- | ---------------------------- |
| `id`          | Unique issue ID              |
| `title`       | Issue title                  |
| `description` | Detailed description         |
| `status`      | Current issue status         |
| `priority`    | Issue priority               |
| `reporter_id` | ID of the reporter           |
| `created_at`  | Issue creation date and time |

---

## 4. CriticalIssue

`CriticalIssue` inherits from `Issue`.

It is used when the issue priority is **Critical**.

It overrides the `describe()` method to provide an urgent message.

### Example

```text
[URGENT] Production Database Down - need to take immediate attention
```

---

## 5. LowerPriorityIssue

`LowerPriorityIssue` also inherits from `Issue`.

It provides a different `describe()` message for low-priority issues.

---

# 🚀 API Endpoints

## Reporter APIs

### Get All Reporters

```http
GET /api/reporters/
```

Returns all reporter records.

---

### Get Reporter by ID

```http
GET /api/reporters/?id=1
```

Returns a specific reporter using the reporter ID.

---

### Create Reporter

```http
POST /api/create-reporter/
```

Example request:

```json
{
    "id": 1,
    "name": "Pravin Patil",
    "email": "pravin@example.com",
    "team": "Backend"
}
```

---

# 🐛 Issue APIs

### Create Issue

```http
POST /api/issues/
```

Example request:

```json
{
    "id": 1,
    "title": "Production Database Down",
    "description": "Production database is not responding.",
    "status": "open",
    "priority": "Critical",
    "reporter_id": 1,
    "created_at": "2026-10-07 11:15:00"
}
```

If the priority is `Critical`, a `CriticalIssue` object is created instead of a normal `Issue` object.

---

### Get All Issues

```http
GET /api/all-issues/
```

Returns all issue records.

---

### Get Issue by ID

```http
GET /api/all-issues/?id=5
```

Returns a specific issue using the issue ID.

---

### Filter Issues by Status

```http
GET /api/all-issues/?status=open
```

Returns issues matching the requested status.

### Supported Statuses

* `open`
* `in_progress`
* `resolved`
* `closed`

---

# ⭐ Issue Priority

The application supports the following priorities:

* `low`
* `medium`
* `high`
* `Critical`

For a `Critical` issue, the application creates a `CriticalIssue` object instead of a normal `Issue` object.

The `CriticalIssue` class overrides the `describe()` method to provide an urgent message.

---

# 💾 Data Storage

The project uses **JSON files instead of a database**.

### `reporters.json`

Stores reporter records.

### `issues.json`

Stores issue records.

Both files contain valid JSON arrays.



---

# ✅ Validation

The application validates the following:

### Reporter

* Reporter name should not be empty
* Email should be valid

### Issue

* Title should not be empty
* Description should not be empty
* Status should not be empty
* Priority should not be empty
* Reporter ID should not be empty
* Created date should not be empty

---

# 🛠️ Running the Project

## 1. Activate Virtual Environment

```bash
source venv/bin/activate
```

## 2. Start Django Server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

# 🧪 Testing

The APIs can be tested using **Postman** or any HTTP client.

### Example

```text
POST http://127.0.0.1:8000/api/issues/
```


# 📸 Screenshots

The `screenshots` folder contains screenshots demonstrating the API requests and responses tested using **Postman**.

The screenshots include:

* Reporter creation API
* Get all reporters API
* Get reporter by ID
* Issue creation API
* Get all issues API
* Get issue by ID
* Filter issues by status
* Critical Issue API response


---

# 📌 API Summary

| Method | Endpoint                       | Purpose                 |
| ------ | ------------------------------ | ----------------------- |
| `GET`  | `/api/reporters/`              | Get all reporters       |
| `GET`  | `/api/reporters/?id=1`         | Get reporter by ID      |
| `POST` | `/api/create-reporter/`        | Create reporter         |
| `POST` | `/api/issues/`                 | Create issue            |
| `GET`  | `/api/all-issues/`             | Get all issues          |
| `GET`  | `/api/all-issues/?id=5`        | Get issue by ID         |
| `GET`  | `/api/all-issues/?status=open` | Filter issues by status |

---

# 📚 Technologies Used

* **Python**
* **Django**
* **JSON**
* **Object-Oriented Programming**
* **Postman**
