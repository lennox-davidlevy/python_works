from users import User

johnny = User('johnny', 'greenwood', 50, 'Israel')
robert = User('robert', 'plant', 70, 'London')
jimmy = User('jimmy', 'page', 70, 'England')

johnny.describe_user()
robert.describe_user()
jimmy.describe_user()

johnny.greet_user()
robert.greet_user()
jimmy.greet_user()
