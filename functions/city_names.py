def build_city(city, country):
    return {"city": city, "country": country}


city_list = []
active_flag = True
while active_flag:
    city = input("input city: ")
    country = input("input country: ")
    built_city = build_city(city, country)
    city_list.append(built_city)
    repeat = input("continue (yes/no)? ")
    if repeat == "no" or repeat == "n":
        active_flag = False

print("\n--- CITY LIST ---")
for city in city_list:
    city_name = city["city"]
    country_name = city["country"]
    print(f"{city_name.title()}, {country_name.title()}")
