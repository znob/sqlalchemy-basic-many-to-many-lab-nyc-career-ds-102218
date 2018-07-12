
# SQLAlchemy Basic Many to Many Association

## Objectives

1.  Build a basic "has many through" relationship, consisting of a join table with only foreign keys, using SQLAlchemy
3.  Query from a database containing this relationship

## Instructions

In the "One to many" associations lab, we used SQLAlchemy to establish a "belongs to" and "has many" relationship between our `Actor` and `Role` classes.  Every instance of the Actor class had many roles, and each instance of the Role class belonged to an Actor.

However, this relationship might not accurately represent the equivalent real world relationship.  Although Actors do have many Roles, shouldn't a Role also have many Actors?  For instance, the role of James Bond has been played by Sean Connery, George Lazenby, Roger Moore, Pierce Brosnan, and Daniel Craig.  In this lab, we will build out this "many to many" relationship by creating a join table called `actor_roles` containing `actor_id` and `role_id` columns.  The `actor_roles` table will only have these foreign keys, so there's no need for a full SQLAlchemy Association Object.

> **Note**: After we write all of our models, we need not run our `models.py` file in the terminal for this lab.  The test file executes the models and seed files for us.

#### `Actor` and `Role`

* Create classes for `Actor` and `Role` in `models.py`
    * Every Actor has an id (primary key) and a name
    * Every Role has an id (primary key) and a character

#### `ActorRole`

* Create a class for ActorRole in `models.py` that will serve as the join table
* Each ActorRole instance will have an `actor_id` and a `role_id`. Both will use the ForeignKey to establish the relationship like so:

>  ```
Column(Integer, ForeignKey('actors.id'), primary_key=True)
```

#### Update `Actor` and `Role` models

* Establish the association between the two models with the `relationship()` function
    - Actor: `roles = relationship('Role', secondary='actor_roles')`

    - Role: `actors = relationship('Actor', secondary='actor_roles')`

> **Note**: Run `python -i models.py` in the terminal to test our models and make sure that the relationships are set up properly. We can test our code by creating a few actors and roles and associating them together.

#### Query from the relationship

Write the following queries in `query.py` to satisfy the tests.

* `return_christian_bales_roles` should return the list of Christian Bale's role instances

* `return_catwoman_actors` should return the list of actors that have played Catwoman

* `return_number_of_batman_actors` should return the number of actors in the database who have played Batman
