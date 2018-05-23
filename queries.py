from models import *

def return_christian_bales_roles(session):
    bale = session.query(Actor).filter_by(name='Christian Bale').one()
    return bale.roles

def return_catwoman_actors(session):
    catwoman = session.query(Role).filter_by(character='Catwoman').one()
    return catwoman.actors

def return_number_of_batman_actors(session):
    batman = session.query(Role).filter_by(character="Batman").one()
    return len(batman.actors)
