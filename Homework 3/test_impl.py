# "Unit Testing with Examples"
# CIS 640 - Tu/Th 1:05
# Author: Christian J. Hughes

import pytest
import impl

# Testing class for create_person(self)
class TestCreatePerson:

    # Checks to ensure that no excpetion is raised when creating a new person
    def test_no_exception_raised(self):
        try:
            myNetwork = impl.Network()
            testPerson = myNetwork.create_person()
        except:
            assert False


# Testing class for add_person_property(self, person, prop, value)
class TestAddPersonProperty:

    # Should overwrite existing property of existing person
    def test_overwrites_existing_property(self):
        try:
            myNetwork = impl.Network()
            testPerson = myNetwork.create_person()
            isHuman = True
            myNetwork.add_person_property(testPerson, isHuman, "Sub-Human")
            myNetwork.add_person_property(testPerson, isHuman, "Sorta-Human")
            myNetwork.add_person_property(testPerson, "name", "john")
            myNetwork.add_person_property(testPerson, "name", "sam")
            assert testPerson == myNetwork.get_person("sam")
        except:
            assert False

    # Should fail when adding a "name" that is a non-string value
    def test_adding_a_name_non_string_value(self):
        with pytest.raises(TypeError):
            myNetwork = impl.Network()
            testPerson = myNetwork.create_person()
            myNetwork.add_person_property(testPerson, "name", 2345678910)

    # Should fail if someone in the network already has the given name
    def test_try_to_add_existing_name_to_new_person(self):
        with pytest.raises(ValueError):
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            testPerson2 = myNetwork.create_person()
            myNetwork.add_person_property(testPerson1, "name", "john")
            myNetwork.add_person_property(testPerson2, "name", "john")

    # Should fail when attempting to add a property to a person that does not exist
    def test_add_property_to_person_that_does_not_exist(self):
        with pytest.raises(RuntimeError):
            myNetwork = impl.Network()
            myNetwork.add_person_property(testPerson, "name", "john")

    # Adding a valid property to an existing person should not raise an exception
    def test_valid_person_and_property(self):
        try:
            myNetwork = impl.Network()
            testPerson = myNetwork.create_person()
            myNetwork.add_person_property(testPerson, "name", "john")
        except:
            assert False


# Testing class for add_relation(self, person1, person2):
class TestAddRelation:

    # Should fail when adding a relation between non-existent person 1, and existing person 2
    def test_person1_does_not_exist(self):
        with pytest.raises(RuntimeError):
            myNetwork = impl.Network()
            testPerson2 = myNetwork.create_person()
            myNetwork.add_relation(testPerson1, testPerson2)

    # Should fail when adding a relation between existing person 1, and non-existent person 2
    def test_person2_does_not_exist(self):
        with pytest.raises(RuntimeError):
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            myNetwork.add_relation(testPerson1, testPerson2)


    # Should fail when adding a relation between non-exsistent persons
    def test_person1_and_person2_do_not_exist(self):
        with pytest.raises(RuntimeError):
            myNetwork = impl.Network()
            myNetwork.add_relation(testPerson1, testPerson2)

    # Should fail when attempting to add a relation to already related persons
    def test_add_relation_to_already_related_persons(self):
        with pytest.raises(ValueError):
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            testPerson2 = myNetwork.create_person()
            myNetwork.add_relation(testPerson1, testPerson2)
            myNetwork.add_relation(testPerson1, testPerson2)


    # Adding a relation between two valid persons should not raise an exception
    def test_valid_relation_between_valid_persons(self):
        try:
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            testPerson2 = myNetwork.create_person()
            myNetwork.add_relation(testPerson1, testPerson2)
        except:
            assert False


# Testing class for add_relation_property(self, person1, person2, prop, value)
class TestAddRelationProperty:

    # Should overwrite existing property of existing relation
    def test_overwrites_existing_relation_property(self):
        try:
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            testPerson2 = myNetwork.create_person()
            testPerson3 = myNetwork.create_person()
            myNetwork.add_person_property(testPerson1, "name", "john")
            myNetwork.add_relation(testPerson1, testPerson2)
            myNetwork.add_relation(testPerson2, testPerson3)
            myNetwork.add_relation_property(testPerson1, testPerson2, "friend", True)
            myNetwork.add_relation_property(testPerson2, testPerson3, "friend", False)
            myNetwork.add_relation_property(testPerson2, testPerson3, "friend", True)

            # If testPerson3 is in the list, then we know that the property was overwritten correctly.
            if testPerson3 in myNetwork.friends_of_friends("john"):
                assert True
            else:
                assert False
        except:
            assert False

    # Should fail when adding a non-boolean friend property to relation
    def test_add_non_boolean_to_friend_property(self):
        with pytest.raises(TypeError):
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            testPerson2 = myNetwork.create_person()
            myNetwork.add_relation(testPerson1, testPerson2)
            myNetwork.add_relation_property(testPerson1, testPerson2, "friend", "yes")
        with pytest.raises(TypeError):
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            testPerson2 = myNetwork.create_person()
            myNetwork.add_relation(testPerson1, testPerson2)
            myNetwork.add_relation_property(testPerson1, testPerson2, "friend", 192810)

    # Should fail when adding a relation property between non-existent person 1, and existing person 2
    def test_person1_does_not_exist(self):
        with pytest.raises(RuntimeError):
            myNetwork = impl.Network()
            testPerson2 = myNetwork.create_person()
            myNetwork.add_relation(testPerson1, testPerson2)
            myNetwork.add_relation_property(testPerson1, testPerson2, "friend", True)

    # Should fail when adding a relation property between existing person 1, and non-existent person 2
    def test_person2_does_not_exist(self):
        with pytest.raises(RuntimeError):
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            myNetwork.add_relation(testPerson1, testPerson2)
            myNetwork.add_relation_property(testPerson1, testPerson2, "friend", True)


    # Should fail when adding a relation property between non-existent persons
    def test_person1_and_person2_do_not_exist(self):
        with pytest.raises(RuntimeError):
            myNetwork = impl.Network()
            myNetwork.add_relation_property(testPerson1, testPerson2, "friend", True)

    # Should fail when attempting to add a relation property to two people with no relation
    def test_add_relation_to_persons_with_no_relation(self):
        with pytest.raises(RuntimeError):
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            testPerson2 = myNetwork.create_person()
            myNetwork.add_relation_property(testPerson1, testPerson2, "friend", True)

    # Adding a valid relation property between two valid people should not raise an exception
    def test_valid_relation_property_between_valid_persons(self):
        try:
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            testPerson2 = myNetwork.create_person()
            myNetwork.add_relation(testPerson1, testPerson2)
            myNetwork.add_relation_property(testPerson1, testPerson2, "friend", True)
        except:
            assert False


# Testing class for get_person(self, name)
class TestGetPerson:

    # Should fail if name parameter is not a string
    def test_pass_non_string_parameter(self):
        with pytest.raises(TypeError):
            myNetwork = impl.Network()
            myNetwork.get_person(True)
        with pytest.raises(TypeError):
            myNetwork = impl.Network()
            myNetwork.get_person(9452)
        with pytest.raises(TypeError):
            myNetwork = impl.Network()
            myNetwork.get_person([2,1])

    # If no person if found with the given name, raise RuntimeError
    def test_no_person_found_with_given_name(self):
        with pytest.raises(RuntimeError):
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            myNetwork.get_person("john")

    # Check to see that searching for a person in the network with a valid name does not raise an exception (and get's correct person).
    def test_get_person_with_valid_person(self):
        try:
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            myNetwork.add_person_property(testPerson1, "name", "john")
            myNetwork.get_person("john")
        except:
            assert False


# Testing class for friends_of_friends(self, name)
class TestFriendsOfFriends:

    # Should fail if name parameter is not a string
    def test_pass_non_string_parameter(self):
        with pytest.raises(TypeError):
            myNetwork = impl.Network()
            myNetwork.friends_of_friends(True)
        with pytest.raises(TypeError):
            myNetwork = impl.Network()
            myNetwork.friends_of_friends(9452)
        with pytest.raises(TypeError):
            myNetwork = impl.Network()
            myNetwork.friends_of_friends([2,1])

    # If no friends of friends exist, must return empty list
    def test_no_friends_of_friends_returns_empty_list(self):
        myNetwork = impl.Network()
        testPerson1 = myNetwork.create_person()
        testPerson2 = myNetwork.create_person()
        myNetwork.add_relation(testPerson1, testPerson2)
        myNetwork.add_relation_property(testPerson1, testPerson2, "friend", True)

    # If no personn is found with the given name, raise RuntimeError
    def test_no_person_found_with_given_name(self):
        myNetwork = impl.Network()
        testPerson1 = myNetwork.create_person()
        myNetwork.add_person_property(testPerson1, "name", "john")
        assert myNetwork.friends_of_friends("john") == []

    # Check to see that it acurately retrieves friends of friends with a valid name
    def test_get_friends_of_friends_with_valid_name(name):
        try:
            myNetwork = impl.Network()
            testPerson1 = myNetwork.create_person()
            testPerson2 = myNetwork.create_person()
            testPerson3 = myNetwork.create_person()
            myNetwork.add_person_property(testPerson1, "name", "john")
            myNetwork.add_relation(testPerson1, testPerson2)
            myNetwork.add_relation(testPerson2, testPerson3)
            myNetwork.add_relation_property(testPerson1, testPerson2, "friend", True)
            myNetwork.add_relation_property(testPerson2, testPerson3, "friend", True)
            friendsOfFriends = myNetwork.friends_of_friends("john")
            assert [testPerson3] == friendsOfFriends
        except:
            assert False
