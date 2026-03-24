# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI and apply core backend concepts such as routing, request validation, and proper HTTP responses. By the end of this assignment, you will create and test endpoints for a simple resource-based service.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Project

#### Description
Create a FastAPI application with a health-check endpoint and one resource endpoint to retrieve a list of items.

#### Requirements
Completed program should:

- Create a runnable FastAPI app in `starter-code.py` using `FastAPI()`
- Implement a `GET /health` endpoint that returns a JSON response with status information
- Implement a `GET /books` endpoint that returns a JSON list of at least 3 sample books
- Return valid JSON responses and use appropriate HTTP status code `200`

### 🛠️ Add Create and Validation Endpoints

#### Description
Extend the API with a create endpoint that accepts input data and validates it using Pydantic models.

#### Requirements
Completed program should:

- Define a Pydantic model for incoming book data (for example: `title`, `author`, `year`)
- Implement a `POST /books` endpoint that accepts JSON request data and stores the new book in memory
- Return the created object and use HTTP status code `201`
- Reject invalid data (for example missing `title`) with FastAPI validation errors
- Include at least one example request/response in a code block

```json
POST /books
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "year": 2008
}
```
