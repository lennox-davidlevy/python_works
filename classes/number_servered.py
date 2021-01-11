from restaurant import Restaurant



mcdonalds = Restaurant('mcdonalds', 'Fast Food Restaurant')
burger_king = Restaurant('burger king', 'Fast Food Restaurant')
restaurant_1 = mcdonalds.show_number_served()
restaurant_2 = burger_king.show_number_served()
mcdonalds.set_number_served(6_000_000_000)
burger_king.set_number_served(1_000_000_000)

print(mcdonalds.show_number_served())
print(burger_king.show_number_served())







