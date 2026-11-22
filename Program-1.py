
def auth_decorator(func):

    def wrapper():

        username = input("Enter username: ")
        password = int(input("Enter password: "))

        valid_username = "Rony"
        valid_password = 1234

        if username == valid_username and password == valid_password:
            print("Authentication successful...!")
            func()
        else:
            print("Authentication failed!")

    return wrapper


@auth_decorator
def say_hello():
    print("Hello....authenticated user!")

say_hello()
