from restaurant import Restaurant


class Ice_Cream_Stand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = set()

    def add_flavor(self, flavor):
        flavor = flavor.lower()
        if flavor in self.flavors:
            print(f"{flavor.title()} already exists!")
            return
        self.flavors.add(flavor)
        print(f"{flavor.title()} added!")
        return self.flavors

    def add_many_flavors(self, flavors):
        if flavors:
            for flavor in flavors:
                flavor = flavor.lower()
                if flavor in self.flavors:
                    continue
                self.flavors.add(flavor)
                print(f"{flavor.title()} added!")
        self.get_flavors()

    def get_flavors(self):
        if len(self.flavors) == 0:
            print("There are no flavors available!")
            return
        print("These flavors are available:")
        for idx, flavor in enumerate(self.flavors):
            print(f"\t{idx + 1}: {flavor.title()}")
        return self.flavors

    def get_how_many_flavors(self):
        print(f"There are {len(self.flavors)} flavors available at {self.name.title()}")
        return len(self.flavors)

    def remove_flavor(self, flavor):
        if flavor.lower() in self.flavors:
            self.flavors.remove(flavor.lower())
            print(f"{flavor.title()} removed!")
        else:
            print(f"{flavor.title()} not available")
        return self.flavors


marvel = Ice_Cream_Stand("marvel", "Ice Cream Stand")
marvel.describe_restaurant()
marvel.add_flavor("Chocolate")
marvel.add_many_flavors(["vanilla", "Chocolate", "peacan", "bananan", "caramel"])
marvel.get_flavors()
marvel.get_how_many_flavors()
marvel.add_flavor("Chocolate")
marvel.remove_flavor("CHocolate")
marvel.get_flavors()
