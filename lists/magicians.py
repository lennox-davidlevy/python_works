magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  if magician != 'alice':
    print(f"{magician.title()}, that was a great trick")
    print(f"I cannot wait to see your next trick {magician.title()}\n")
  else:
    print(f"{magician.title()}, that was a terrible trick")
    print(f"I never want to see you again, {magician.title()}\n")
print(f"Thank you everyone except Alice, you were wonderful. \nAlice, you stink")