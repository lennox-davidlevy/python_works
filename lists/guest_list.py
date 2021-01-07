import math

#create guest list
guest_list = ['peter thiel', 'elon musk', 'ricky gervais', 'jerry seinfeld']
guest_rsvp_no = 'jerry seinfeld'
secondary_guest = 'larry david'
for guest in guest_list:
  print(f"I want to invite {guest.title()} because I think he is cool")
#change guest list
print(f"\n{guest_rsvp_no.title()} said he cannot come,\nso I am adding {secondary_guest.title()} to the party")
guest_list.remove(guest_rsvp_no)
guest_list.append(secondary_guest)
print(f"\nThe new guest list is now {guest_list}")
table_length = len(guest_list)
print(f"\nThe original table size was {table_length}, but now it is {table_length + 3}, so we will add three more guests")
guest_list.insert(0, 'Liane Levy')
guest_list.append( 'Lulu Levy')
guest_list.insert(math.floor(len(guest_list) / 2), 'David Levy')
print(guest_list)

print(f"\nWell it turns out the table only seats two...")

while len(guest_list) > 2:
  print(f"\nSorry {guest_list.pop()}, but you have been disinvited")

print(f'\nThe new guest list is {guest_list}')
del guest_list[0:2]
print(f"\n guest list is now empty: {guest_list}")


