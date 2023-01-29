class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

# the __str__ method is used to define what happens if we ues str()
# if we dont declare that method we will get the address of that instance class

    def __str__(self):
        return self._name + "," + self._email
# if we had not declared str it just would have changed the address as string value and printed that

    def do_something(self):
        print("HI FROM ,"+str(self))


users = [User("Testuser", "testmail@gmail.com"),
         User("User2", "user2@gmail.com")]
print()
for user in users:
    user.do_something()
print()
