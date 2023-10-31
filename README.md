# PyCine Backend

Pycine is a fictional app for learning API Concepts, it has a list of movies, users, and favorite movies. This project is part of the IFPR's Web Development IV Class. This is the back-end of the application, for the front-end go to: **[Pycine-front](https://github.com/bernardotonin/pycine-front)**


## Technologies Used

This application was developed using Python3 and uses the following libraries and API's:

- **[FastAPI](https://fastapi.tiangolo.com/):** FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.
- **[Pydantic](https://docs.pydantic.dev/latest/):** Pydantic is the most widely used data validation library for Python.
- **[SQLAlchemy](https://www.sqlalchemy.org/):** SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- **[TMDB API](https://developer.themoviedb.org/docs):** The TMDB API is a service for those interested in using movie, TV show or actor images and/or data in your application.
- **[Pipenv](https://pipenv.pypa.io/en/latest/):**  Pipenv is a Python virtualenv management tool that supports a multitude of systems and nicely bridges the gaps between pip, python and virtualenv.

## Instalation and Usage
To set up and run the project, follow these steps:
1. Clone the repository:
```
https://github.com/bernardotonin/pycine-back.git
cd pycine-back
 ```
 2. Install pipenv:
 ```
pip install --user pipenv
 ```
 3. Start Virtual Enviroment:
  ```
python3 -m pipenv shell
 ```
 4. Select python interpreter (VSCode) :

  ```
CTRL + P
> Python: Select Interpreter
Select the Pipenv Enviroment.
 ```
 5. Install dependencies:
 ```
python3 -m pipenv install
 ```
> **_Note:_** If you are encountering the error:  python3: can't open file '.../pycine-back/pipenv': [Errno 2] No such file or directory. Create a .env file and add the variable PYTHONPATH and set it equal to the absolute path of the project.

6. Run Uvicorn:
```
uvicorn main:app --port 8080
 ```

7. Setup front-end Server: **[Pycine-front](https://github.com/bernardotonin/pycine-front)**

## Special Thanks

A special thanks to the teacher of this course, **[Felippe Scheidt](https://github.com/fscheidt)**.
