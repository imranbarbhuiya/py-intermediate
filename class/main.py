class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user1 = User("001", "Jhon")
user2 = User("002", "Mary")

user1.follow(user2)
user2.follow(user1)

print(user1.followers)
