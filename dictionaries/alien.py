alien_0 = {"color": "green", "points": 5}
user_points = 0
user_points += alien_0["points"]
print(
    f"You have shot down a {alien_0['color']} alien and scored {alien_0['points']} points!"
)
print(f"Your point total is now: {user_points} points!")
alien_0["x-position"] = 0
alien_0["y-position"] = 25
print(alien_0)


def create_alien(color, points, speed):
    return {
        "color": color,
        "points": points,
        "speed": speed,
        "x_position": 0,
        "y_position": 25,
    }


alien_1 = create_alien("yellow", 10, "fast")
if alien_1["speed"] == "slow":
    x_increment = 1
elif alien_1["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
print(alien_1)
alien_1["x_position"] += x_increment
print(alien_1)
del alien_1["points"]
print(alien_1)
