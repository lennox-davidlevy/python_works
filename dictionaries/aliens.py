def create_alien(color, points, speed):
    return {
        "color": color,
        "points": points,
        "speed": speed,
        "x_position": 0,
        "y_position": 25,
    }


aliens = []
for alien_number in range(31):
    if alien_number % 3 == 0:
        aliens.append(create_alien("yellow", 10, "medium"))
    elif alien_number % 5 == 0:
        aliens.append(create_alien("red", 15, "fast"))
    else:
        aliens.append(create_alien("green", 5, "slow"))

list_of_aliens = []
for idx, alien in enumerate(aliens):
    name = "alien_" + str(idx)
    temp = {"name": name, "characteristcs": alien}
    list_of_aliens.append(temp)


for alien in list_of_aliens:
    color = alien["characteristcs"]["color"]
    
    
    if color == "red":
        alien["characteristcs"]["color"] = "blue"
        alien["characteristcs"]["speed"] = "super_fast"
        alien["characteristcs"]["points"] = 1000
    if color == "green":
        alien["characteristcs"]["color"] = "yellow"
        alien["characteristcs"]["speed"] = "medium"
        alien["characteristcs"]["points"] = 10
    if color == "yellow":
        alien["characteristcs"]["color"] = "red"
        alien["characteristcs"]["speed"] = "fast"
        alien["characteristcs"]["points"] = 15


for alien in list_of_aliens[:10]:
    print(alien)

# aliens = []
# aliens.append(create_alien("green", 5, "slow"))
# aliens.append(create_alien("yellow", 10, "medium"))
# aliens.append(create_alien("red", 15, "fast"))
# for idx, alien in enumerate(aliens):
#    name = "alien_" + str(idx)
#    print(f"{name}: {alien}\n")





