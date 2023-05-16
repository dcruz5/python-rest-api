# FastAPI REST API
This project is built with FastAPI, a modern Python web framework that allows you to build high-performance web applications with minimal code. The API uses SQLAlchemy ORM to interact with a PostgreSQL database, and is integrated with Alembic for database migrations and psycopg2 for database connections.

## Requirements
- Python 3.7 or higher
- PostgreSQL
- pip
  
## Installation
1. Clone the repository and navigate to the project directory.
```bash
git clone https://github.com/cruz05/python-rest-api.git
cd python-rest-api
```

2. Create a virtual environment for the project and activate it.
```bash
python -m venv venv
source venv/bin/activate
```
3. Install the required packages using pip.

```bash
pip install -r requirements.txt
```

4. Create a new PostgreSQL database and update the SQLALCHEMY_DATABASE_URL variable in the database.py to match your database configuration.
   
```
SQLALCHEMY_DATABASE_URL=postgresql://your-username:your-password@localhost/your-database
```
5. Run the Alembic migrations to create the database tables.
   
```
alembic upgrade head
```

6. Start the FastAPI server.

```bash
uvicorn main:app --reload
```

7. The API will now be available at http://localhost:8000.

## Usage

The API has several endpoints that allow you to create, read, update and delete data in the database. Here are some examples:

* GET /items: Retrieve a list of all items in the database.
* GET /items/{id}: Retrieve a specific item by ID.
* POST /items: Create a new item.
* PUT /items/{id}: Update an existing item by ID.
* DELETE /items/{id}: Delete an item by ID.
  
You can test the API using a tool like Postman or cURL.

## Contributing

If you find a bug or would like to contribute to the project, please open an issue or submit a pull request.