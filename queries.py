from models import *
from sqlalchemy import create_engine, func

engine = create_engine('sqlite:///actorroles.db')

Session = sessionmaker(bind=engine)
session = Session()



def return_christian_bales_roles():
    return session.query(Actor).filter(Actor.name=="Christian Bale")[0].roles
    # Return a list of Christian Bale role instances

def return_catwoman_actors():
    return session.query(Role).filter(Role.character=="Catwoman")[0].actors
    #  Return a list of actor instances that have played Catwoman

def return_number_of_batman_actors():
    return len(session.query(Role).filter(Role.character=="Batman")[0].actors)
    # Return the number of actors that have played Batman

print(return_christian_bales_roles())
print(return_catwoman_actors())
print(return_number_of_batman_actors())
