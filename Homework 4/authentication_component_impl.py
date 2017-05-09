from data_store_interface import DataStore

class AuthenticationComponent(object):
    def __init__(self, data_store):
        # create the component that uses the given data store to store user info
        assert isinstance(data_store, DataStore)
        self.data_store = data_store
        pass

    # DO NOT TEST THIS METHOD
    # Implementations can modify this function to plug in an apt transformation
    def transform_password(self, input):
        assert isinstance(input, str)
        return input
        # assert isinstance(ret_val, str)

    def create_user(self, user_name, password):
        # create a user with user_name and password
        # return True if the user was created; False, otherwise
        # user names are unique
        assert isinstance(user_name, str)
        assert isinstance(password, str)
        return self.data_store.create(user_name, self.transform_password(password))
        # assert isinstance(ret_val, bool)

    def login_user(self, user_name, password):
        # check if user_name and password represent an existing user
        # return True if user_name and password represent an existing user; False, otherwise
        assert isinstance(user_name, str)
        assert isinstance(password, str)
        pass
        # assert isinstance(ret_val, bool)

    def change_password(self, user_name, new_password):
        # change the password of user with user_name to new_password
        # return True if password was changed to new_password; False, otherwise
        assert isinstance(user_name, str)
        assert isinstance(new_password, str)
        pass
        # assert isinstance(ret_val, bool)

    def rename_user(self, user_name, new_user_name):
        # rename the user named user_name as new_user_name
        # return True if user was renamed; False, otherwise
        assert isinstance(user_name, str)
        assert isinstance(new_user_name, str)
        pass
        # assert isinstance(ret_val, bool)
