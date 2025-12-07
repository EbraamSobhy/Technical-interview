class User:
    def __init__(self, username, email, password):
      self.username = username
      self.email = email
      self.password = password

    def say_hi_to_user(self, user):
      print(f"Sending message to {user.user}")

user1 = User("Mark", "example@gmail.com", "1234")
user2 = User("Booking.com", "example@gmail.com", "1234")

user1.say_hi_to_user(user2)

    