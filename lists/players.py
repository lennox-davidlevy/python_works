players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players)
# print(players[0:3])
# print(players[:4])
# print(players[2:])
# last three elements:
# print(players[-3:])
print(f"Here are the first three players on my team:")
for idx, player in enumerate(players[:3]):
  print(f"#{idx}: {player.title()}")
