# "Unit Testing with Test Doubles"
# CIS 640 - Tu/Th 1:05
# Author: Christian J. Hughes

from data_store_interface import DataStore
from authentication_component_impl import AuthenticationComponent

# A test double class that provides a basic implementation of the DataStore interface.
class DummyDataStore(DataStore):
    def __init__(self):
        self.names_and_values = {}
        self.num_of_method_calls = 0

    def return_num_of_method_calls(self):
        # Returns the mnumber of method calls made since the object was instantaited
        return self.num_of_method_calls

    def create(self, name, value):
        # create a new entry that records the given name and value
        # return True if the entry was created; False, otherwise
        # each entry is unique in terms the associated name
        self.num_of_method_calls = self.num_of_method_calls + 1
        if name in self.names_and_values:
            # If the key already exists, then return False.
            return False
        else:
            # If the key does not exist, create an entry and return True.
            self.names_and_values[name] = value
            return True

    def read(self, name):
        # return the value of the existing entry corresponding to the name
        # raise RuntimeError exception if there is no entry with the name
        self.num_of_method_calls = self.num_of_method_calls + 1
        if name in self.names_and_values:
            # If the key already exists, return its value.
            return self.names_and_values[name]
        else:
            # If the key does not exist, raise RuntimeError.
            raise RuntimeError()

    def update(self, name, value):
        # update the value of the existing entry corresponding to the name
        # return True if the entry was updated; false, otherwise
        self.num_of_method_calls = self.num_of_method_calls + 1
        if name in self.names_and_values:
            # If the key already exists, update value and return true.
            # TODO - Might need to check if changing to same value counts as updating.
            self.names_and_values[name] = value
            return True
        else:
            # If the key does not exist, return False.
            return False

    def delete(self, name):
        # delete the existing entry corresponding to the name
        # return True if the entry was deleted; false, otherwise
        self.num_of_method_calls = self.num_of_method_calls + 1
        if name in self.names_and_values:
            # If the key exists, delete it and return true.
            del self.names_and_values[name]
            return True
        else:
            # If the key does not exist, return False.
            return False

# Testing class for create_user(self, user_name, password)
class TestCreateUser:

    # Setup method for all tests cases in this class.
    def setup_method(self):
        self.DS = DummyDataStore()
        self.AC = AuthenticationComponent(self.DS)

    # Ensure that this method only access the data store once.
    def test_create_user_should_access_data_store_once(self):
        result = self.AC.create_user("Christian", "password")
        times_accessed = self.DS.return_num_of_method_calls()
        assert times_accessed == 1

    # Test adding a single new user, function should return true.
    def test_create_user_valid_new_user(self):
        result = self.AC.create_user("Christian", "password")
        assert result == True

    # Test adding the same user twice, should return False on second attempt.
    def test_create_user_add_same_user_twice(self):
        self.AC.create_user("Christian", "password")
        result = self.AC.create_user("Christian", "password")
        assert result == False

    # Add two different users with the same password. Should not be sucessful, as passwords are not unique.
    def test_create_user_two_different_users_same_passwords(self):
        self.AC.create_user("Christian", "password")
        result = self.AC.create_user("Chris", "password")
        assert result == True

# Testing class for login_user(self, user_name, password)
class TestLoginUser:

    # Setup method for all tests cases in this class.
    def setup_method(self):
        self.DS = DummyDataStore()
        self.AC = AuthenticationComponent(self.DS)

    # Ensure that this method only access the data store once.
    def test_login_user_should_access_data_store_once(self):
        self.AC.login_user("Christian", "password")
        times_accessed = self.DS.return_num_of_method_calls()
        assert times_accessed == 1

    # Tests the function on a valid existing user and password.
    def test_login_user_existing_user_and_password(self):
        self.AC.create_user("Christian", "password")
        result = self.AC.login_user("Christian", "password")
        assert result == True

    # Tests the function on a valid existing user, but with the wrong password.
    def test_login_user_existing_user_and_bad_password(self):
        self.AC.create_user("Christian", "password")
        result = self.AC.login_user("Christian", "password1")
        assert result == False

    # Tests the function with a user name that does not exist.
    def test_login_user_non_existing_user(self):
        self.AC.create_user("Christian", "password")
        result = self.AC.login_user("Bob", "password")
        assert result == False

# Testing class for change_password(self, user_name, new_password)
class TestChangePassword:

    # Setup method for all tests cases in this class.
    def setup_method(self):
        self.DS = DummyDataStore()
        self.AC = AuthenticationComponent(self.DS)

    # Ensure that this method only access the data store once.
    def test_change_password_should_access_data_store_once(self):
        self.AC.change_password("Christian", "password1")
        times_accessed = self.DS.return_num_of_method_calls()
        assert times_accessed == 1

    # Ensure a valid password change on an existing user works.
    def test_change_password_existing_user_valid_password_change(self):
        self.AC.create_user("Christian", "password")
        result = self.AC.change_password("Christian", "password1")
        assert result == True

    # Attempting to change the password of a user that does not exist, which should return false.
    def test_change_password_non_existing_user(self):
        self.AC.create_user("Christian", "password")
        result = self.AC.change_password("Bob", "password1")
        assert result == False

    # If the new password for a user is the same as the old one, return True.
    def test_change_password_to_same_as_old_password(self):
        self.AC.create_user("Christian", "password")
        result = self.AC.change_password("Christian", "password")
        assert result == True

# Testing class for rename_user(self, user_name, new_user_name)
class TestRenameUser:

    # Setup method for all tests cases in this class.
    def setup_method(self):
        self.DS = DummyDataStore()
        self.AC = AuthenticationComponent(self.DS)

    # Ensure that this method only access the data store three times.
    def test_rename_user_should_access_data_store_three_times(self):
        self.AC.rename_user("Christian", "Chris")
        times_accessed = self.DS.return_num_of_method_calls()
        assert times_accessed == 3

    # Reanme an existing user with a valid new name.
    def test_rename_user_existing_user_valid_rename(self):
        self.AC.create_user("Christian", "password")
        result = self.AC.rename_user("Christian", "Chris")
        assert result == True

    # Attempt to rename a user that does not exist, which should return False.
    def test_rename_user_non_existing_user(self):
        self.AC.create_user("Christian", "password")
        result = self.AC.rename_user("Bob", "Robert")
        assert result == False

    # Attempt to rename an existing user with the same name as the old one, and return True.
    def test_rename_user_existing_user_rename_same_as_old_name(self):
        self.AC.create_user("Christian", "password")
        result = self.AC.rename_user("Christian", "Christian")
        assert result == True
