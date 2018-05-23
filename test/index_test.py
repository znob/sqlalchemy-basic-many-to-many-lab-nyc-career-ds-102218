import unittest, sys
sys.path.insert(0, '..')
from queries import *
from models import *

exec(open("../seed.py").read())

class TestBasicHasManyThrough(unittest.TestCase):
    def test_actors(self):
        self.assertEqual(len(session.query(Actor).all()), 5)

    def test_roles(self):
        self.assertEqual(len(session.query(Role).all()), 4)

    def test_actors_have_many_roles(self):
        bale = session.query(Actor).filter_by(name="Christian Bale").one()
        self.assertEqual(len(bale.roles), 3)
        self.assertEqual(bale.roles[0].character, 'Dr. Michael Burry')
        self.assertEqual(bale.roles[1].character, 'Patrick Bateman')
        self.assertEqual(bale.roles[2].character, 'Batman')

    def test_roles_have_many_actors(self):
        catwoman = session.query(Role).filter_by(character="Catwoman").one()
        self.assertEqual(len(catwoman.actors), 2)
        batman = session.query(Role).filter_by(character="Batman").one()
        self.assertEqual(len(batman.actors), 3)

    def test_return_christian_bales_roles(self):
        roles = return_christian_bales_roles(session)
        self.assertEqual(len(roles), 3)

        characters = []
        for role in roles:
            characters.append(role.character)
        self.assertEqual(characters, ['Dr. Michael Burry', 'Patrick Bateman', 'Batman'])

    def test_return_catwoman_actors(self):
        actors = return_catwoman_actors(session)
        self.assertEqual(len(actors), 2)

        names = []
        for actor in actors:
            names.append(actor.name)
        self.assertEqual(names, ['Michelle Pfeiffer', 'Anne Hathaway'])

    def test_return_number_of_batman_actors(self):
        result = return_number_of_batman_actors(session)
        self.assertEqual(result, 3)
