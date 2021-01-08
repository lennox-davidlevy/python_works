alien_color = ["green", "yellow", "red", "green", "yellow", "red"]

score = 0

for color in alien_color:
    if color == "green":
        score += 5
        print(f"{color.title()} alien shot down, score: {score}")
    elif color == "yellow":
        score += 4
        print(f"{color.title()} alien shot down, score: {score}")
    else:
        score += 2
        print(f"{color.title()} alien shot down, score: {score}")

print(score)
