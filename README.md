# Movie Reservation POC

## Description

The aim of this project is to create a simple web application POC of a reserve a movie ticket with several objectives: 

1. [Test the use of SQLModel instead of SQLAlchemy](#sqlmodel-vs-sqlalchemy)
2. [Check the integration of SQLModel with Alembic](#sqlmodel-integration-with-alembic)
3. [Investigate how to make JOINs in SQLModel and also how to make complex queries](#joins-in-sqlmodel-and-complex-queries)
4. [Implement Dependency Injection pattern and a layered architecture using the dependency-injection package](#dependency-injection)

## SQLModel vs SQLAlchemy

SQLModel is a library that allows you to define your database schema using Python classes. It is built on top of SQLAlchemy and provides a simpler and more intuitive syntax for defining your database models. 

Here is a simple example of how to define a SQLModel class:

```python
from sqlmodel import SQLModel, Field

class Movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    release_year: int
    rating: float
```

In this example, we define a `Movie` class that inherits from `SQLModel` and sets the `table` attribute to `True`. This means that the class will be mapped to a database table.

We also define several fields using the `Field` class, specifying the data type and other attributes. In this case, we set the `default` attribute to `None` to indicate that the field is nullable.

### Pros of SQLModel:

- Simpler and more intuitive syntax for defining database models
- Supports relationships between models
- Supports complex queries using SQLAlchemy's query builder
- Supports database migrations using Alembic

### Cons of SQLModel:

- Not enough documentation compared to SQLAlchemy, this could be related to the fact that SQLModel is less mature.
- Not as powerful as SQLAlchemy

## SQLModel integration with Alembic

Alembic is a database migration tool that helps you manage database schema changes. It provides a command-line interface and a Python API for performing database migrations.

To integrate SQLModel with Alembic, you need to first install Alembic and use the init command to create a new Alembic configuration file:

```bash
alembic init alembic
```

This will create a new `alembic.ini` file in the current directory. There you need to go to the `env.py` file and make the following changes:

1. Import the `SQLModel` module and the `SQLModel.metadata` object.
2. Change the `target_metadata` variable to use the `SQLModel.metadata` object instead of the `Base.metadata` object.
3. Change the `url` variable to use the `settings.database_url` object instead of a hardcoded URL.

```Python
# 1.
from sqlmodel import SQLModel 

# 2.
target_metadata = SQLModel.metadata

# 3.
def get_url():
    return str(settings.database_url)

# And in the function run_migrations_offline() change the url variable to use the get_url() function.
    configuration = config.get_section(config.config_ini_section, {})
    configuration["sqlalchemy.url"] = get_url()

```

After all these changes, you can run some alembic commands to create the initial database schema and perform the migrations:

```bash
alembic revision --autogenerate -m "Initial database schema"
alembic upgrade head
```

## Joins in SQLModel and complex queries

SQLModel supports joins and complex queries using SQLAlchemy's query builder. Here is an example of how to use joins:

```python
from sqlmodel import select

movies = select(Movie).join(Showtime).where(Showtime.showtime_id == 1)
```

In this example, we select all movies and join them with the `Showtime` table based on the `showtime_id` column. We then filter the results to only include movies that have a showtime with the `showtime_id` of 1.
Also you can make complex queries using raw SQL and the execute method:

```python
result = self.db.execute(
  text(
    """
    SELECT showtime.*
    FROM showtime
    INNER JOIN movie ON showtime.movie_id = movie.id
    WHERE movie.id = :movie_id
    """
  ),
  {"movie_id": movie_id},
)
rows = result.fetchall()
```

## Dependency Injection

Dependency Injection is a design pattern that allows you to decouple the dependencies of a class from its implementation. This helps to make the code more modular and easier to test.

In this project, we use the dependency-injection package to implement Dependency Injection. Here is an example of how to use it:

```python
from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.api.v1.routers.auth",
            "src.api.v1.routers.movie",
            "src.controllers.auth",
            "src.controllers.showtime",
            "src.repositories.user",
            "src.repositories.showtime",
        ]
    )

    # DB
    db_session = providers.Resource(get_db)

    # Repositories
    user_repository = providers.Factory(
        UserRepository,
        db=db_session,
    )
    showtime_repository = providers.Factory(
        ShowtimeRepository,
        db=db_session,
    )

    # Controllers
    showtime_controller = providers.Factory(
        ShowtimeController, showtime_repository=showtime_repository
    )
    auth_controller = providers.Factory(
        AuthController,
        user_repository=user_repository,
    )
```

In this example, we define a `Container` class that inherits from `DeclarativeContainer`. We set the `wiring_config` attribute to a `WiringConfiguration` object, which specifies the modules that should be wired up.

We then define the dependencies of the `Container` class using the `providers` module. In this case, we define a `db_session` dependency that is provided by a `Resource` provider, which retrieves the database session from the `get_db` function.

We also define other dependencies, such as `user_repository` and `showtime_repository`, which are provided by `Factory` providers. These providers take a `db` parameter, which is set to the `db_session` dependency.

Finally, we define the `showtime_controller` and `auth_controller` dependencies, which are provided by `Factory` providers. These providers take a `showtime_repository` parameter, which is set to the `showtime_repository` dependency.

## Conclusion

This project demonstrates the use of SQLModel, Alembic, and Dependency Injection to create a simple web application. It provides a starting point for further development and testing of SQLModel and Alembic, as well as Dependency Injection in a real-world application.

I hope this project has been helpful in understanding the differences between SQLModel and SQLAlchemy, and how to integrate them with Alembic and Dependency Injection.
