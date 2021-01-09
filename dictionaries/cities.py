cities = {
    "new york city": {
        "country": "the united states",
        "population": 8000000,
        "fact": "smells like shit.",
    },
    "chicago": {
        "country": "the united states",
        "population": 5000000,
        "fact": "is crime ridden.",
    },
    "los angeles": {
        "country": "the united states",
        "population": 7000000,
        "fact": "is filled with perverts.",
    },
}

for name, facts in cities.items():
    name = name.title()
    country = facts["country"].title()
    population = facts["population"]
    fact = facts["fact"]
    print(f"{name} is in {country} it has a population of {population}.")
    print(f"An interesting fact about {name} is that it {fact}\n")
