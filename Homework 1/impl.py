# "Develop A Python Program"
# CIS 640 - Tu/Th 1:05
# Author: Christian J. Hughes

# Network of people that have relationships between them
class Network(object):
    def __init__(self):
        # A list of all the Person objects in the Network
        self.people_in_network = []

    def create_person(self):
        # create a person in the network and return the person
        newPerson = Person() # Create a person object
        self.people_in_network.append(newPerson) # Add that person to list of Persons
        return newPerson
    def add_person_property(self, person, prop, value):
        # add property to a person
        setattr(person, prop, value)
    def add_relation(self, person1, person2):
        # add a relation
        # Establish new relationship for person1, and add to their list of relations
        person1Relationship = Relation()
        person1Relationship.inRelationshipWith = person2
        person1.relations.append(person1Relationship)

        # Establish new relationship for person2, and add to their list of relations
        person2Relationship = Relation()
        person2Relationship.inRelationshipWith = person1
        person2.relations.append(person2Relationship)
    def add_relation_property(self, person1, person2, prop, value):
        # add property to a relation
        foundRelation = False
        # Find the appropriate relation attatched to person1, and add the property.
        for relation in person1.relations:
            if relation.inRelationshipWith == person2:
                foundRelation = True
                setattr(relation, prop, value)
                break

        # If attempting to add a property to a relationship that doesn't exist, then raise an exception.
        if foundRelation == False:
            raise RuntimeError()

        # Find the appropriate relation attatched to person2, and add the property.
        for relation in person2.relations:
            if relation.inRelationshipWith == person1:
                setattr(relation, prop, value)
                break
    def get_person(self, name):
        # get the person with given name
        # Look through the list for the person with the given name.
        for person in self.people_in_network:
            if hasattr(person, "name"): #  Make sure that they have been given the proprty "name"
                if person.name == name:
                    return person
        # If no person with such a name exists, then we raise a RuntimeError exception
        raise RuntimeError()
    def friends_of_friends(self, name):
        # get the friends of friends of the person with given name
        # Create a list of friends to return
        friendsOfFriends = []

        # Find the person in the network with the given name
        for person in self.people_in_network:
            if hasattr(person, "name"): # Make sure that they have been given the proprty "name"
                if person.name == name:
                    # Iterate over each of that persons relations to find friends
                    for relation in person.relations: # Look through all given persons relations
                        if hasattr(relation, "friend"):
                            if relation.friend == True:
                                for relationInFriend in relation.inRelationshipWith.relations: # If a friend is found, search through all of their relations.
                                    if hasattr(relationInFriend, "friend"):
                                        if relationInFriend.friend == True and relationInFriend.inRelationshipWith != person:
                                            friendsOfFriends.append(relationInFriend.inRelationshipWith)
                    # Return the completed list
                    return friendsOfFriends
        # If no person with such a name exists, then we through a RuntimeError exception
        raise RuntimeError()

# Class representing a single person in the network.
class Person(object):
    # Attributes will be added to each Person dynamically at runtime.
    def __init__(self):
        # Each Person has a list of relations
        self.relations = []

# Class representing a single (one way) relationship in the network.
class Relation(object):
    # Properties/Attributes will be added to each Relation dynamically at runtime
    # Each relation must be with another party. Initialized to none.
    def __init__(self):
        self.inRelationshipWith = None

# A class for testing the functionality of the Network methods/object creation.
# Provides no functionality beyond testing.
class Test(object):
    def runTests(self):
        myNetwork = Network()
        Jaxon = myNetwork.create_person()
        Christian = myNetwork.create_person()
        Alex = myNetwork.create_person()
        Tyler = myNetwork.create_person()
        myNetwork.add_person_property(Christian, "name", "Christian")
        myNetwork.add_person_property(Jaxon, "name", "Jaxon")
        myNetwork.add_person_property(Jaxon, "name", "Jaxon2")
        myNetwork.add_person_property(Alex, "name", "Alex")
        myNetwork.add_person_property(Tyler, "name", "Tyler")
        myNetwork.add_relation(Christian, Jaxon)
        myNetwork.add_relation(Christian, Tyler)
        myNetwork.add_relation(Alex, Jaxon)
        myNetwork.add_relation(Tyler, Jaxon)
        myNetwork.add_relation(Tyler, Alex)
        myNetwork.add_relation_property(Christian,Jaxon,"friend", True)
        myNetwork.add_relation_property(Christian,Tyler,"friend", True)
        myNetwork.add_relation_property(Alex,Jaxon,"friend", True)
        myNetwork.add_relation_property(Jaxon,Tyler,"friend", True)
        myNetwork.add_relation_property(Alex,Tyler,"friend", True)
        ListOfFriendsOfFriends = myNetwork.friends_of_friends("Christian")
        print(ListOfFriendsOfFriends)
        for i in ListOfFriendsOfFriends:
            print(i.name)

## Create a sample Network to run tests on.
# testing = Test()
# testing.runTests()
