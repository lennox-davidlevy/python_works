from users import User

user_1 = User('john', 'doe', 45, 'georgia')
user_2 = User('jane', 'doe', 15, 'virginia')
user_3 = User('jimmy', 'doe', 31, 'dakota')
user_4 = User('jack', 'doe', 10, 'new york')
user_5 = User('bobby', 'doe', 100, 'alaska')


for i in range(20):
    print(user_1.increment_login_attempts())
print(user_1.login_attempts)
print(user_1.reset_login_attempts())
