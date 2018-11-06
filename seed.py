from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models import Actor, Role, ActorRole, engine

Base = declarative_base()
engine = create_engine('sqlite:///actorroles.db')
Session = sessionmaker(bind=engine)



session = Session()

bale = Actor(name="Christian Bale")
hathaway = Actor(name="Anne Hathaway")
pfeiffer = Actor(name="Michelle Pfeiffer")
keaton = Actor(name="Michael Keaton")
arnett = Actor(name="Will Arnett")

batman = Role(character="Batman")
catwoman = Role(character="Catwoman")
burry = Role(character="Dr. Michael Burry")
american_psycho = Role(character="Patrick Bateman")

batman.actors.append(bale)
batman.actors.append(keaton)
batman.actors.append(arnett)
catwoman.actors.append(pfeiffer)
catwoman.actors.append(hathaway)

bale.roles.append(burry)
bale.roles.append(american_psycho)

session.add_all([bale, hathaway, pfeiffer, keaton, arnett])
session.add_all([batman, catwoman])
session.commit()
