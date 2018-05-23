
# SQLAlchemy Basic Many to Many Association

## Objectives

1.  Build a "has many through" relationship using SQLAlchemy
2.  Write an Alembic migration to create a join table consisting of only foreign keys
3.  Query from a database containing this relationship

## Instructions

In the "One to many" associations lab, we used SQLAlchemy to create establish a "belongs to" and "has many" relationship between our `Actor` and `Role` classes.  Every instance of the Actor class could have many roles, and each instance of the Role class belonged to an Actor.

This relationship might not properly mimic the real world, however.  Although Actors do have many Roles, shouldn't a Role also have many Actors?  For instance, the role of James Bond has been played by Sean Connery, George Lazenby, Roger Moore, Pierce Brosnan, and Daniel Craig.  In this lab, we will build out this relationship by creating a join table called `actor_roles` containing `actor_id` and `role_id` columns.

#### `Actor` and `Role`

* Create classes for `Actor` and `Role` in `models.py`
    * Every Actor has an id (primary key) and a name
    * Every Role has an id (primary key) and a character

#### `ActorRole`

Write an Alembic migration to create the `actor_roles` join table

* Recall the Alembic migration flow:
    - run `alembic init alembic`
    - change the sqlalchemy.url in `alembic.ini`
    - create a migration with `alembic revision -m "<migration name here>"`
    - fill in the upgrade and downgrade functions
    - run `alembic upgrade head`


* add foreign keys for `actor_id` and `role_id` using the following format:
>  ```
   sa.Column(
      'actor_id', sa.Integer,
      sa.ForeignKey('actors.id'), primary_key=True
   )
  ```

* Write a class model for the join table, `ActorRole`, in `models.py`
    * make sure to specify the ForeignKey when adding columns for `actor_id` and `role_id`

#### Update `Actor` and `Role` models

* Establish the association between the two models with the `relationship()` function
    - Actor: `roles = relationship('Role', secondary='actor_roles')`
    - Role: `actors = relationship('Actor', secondary='actor_roles')`

#### Query from the relationship

Write queries in `query.py` to satisfy the tests.

* `return_christian_bales_roles` should return the list of Christian Bale's role instances
* `return_catwoman_actors` should return the list of actors that have played Catwoman
* `return_number_of_batman_actors` should return the number of actors in the database who have played Batman
