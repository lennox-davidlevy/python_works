class Privileges:
    def __init__(self, fullname):
        self.privileges = set()
        self.fullname = fullname

    def __is_privileges_empty(self):
        return len(self.privileges) == 0

    def add_privilege(self, privilege):
        privilege = privilege.lower()
        if privilege in self.privileges:
            print(f"{self.fullname.title()} already has the ability to {privilege}!")
            return self.privileges
        else:
            self.privileges.add(privilege)
            return self.privileges

    def add_many_privileges(self, privileges):
        if len(privileges) == 0:
            print(f"Empty list provided, nothing added")
            return
        for privilege in privileges:
            privilege = privilege.lower()
            if privilege in self.privileges:
                print(f"{self.fullname.title()} alread has {privilege}")
                continue
            else:
                self.privileges.add(privilege)
                print(f"{privilege} added!")
        return self.privileges

    def show_privileges(self):
        if self.__is_privileges_empty():
            print(f"{self.fullname.title()} has no privileges!")
            return
        print(f"{self.fullname.title()} has the following  privileges:")
        for idx, privilege in enumerate(self.privileges):
            print(f"\t{idx + 1}: {privilege}")

    def remove_privilege(self, privilege):
        privilege = privilege.lower()
        if self.__is_privileges_empty():
            print(f"{self.fullname.title()} has no privileges!")
            return
        elif privilege not in self.privileges:
            print(f"{self.fullname.title()}does not have that privilege!")
            return
        self.privileges.remove(privilege)
        print(f"{privilege.title()} removed!")
        return self.privileges

    def remove_all_privileges(self):
        if self.__is_privileges_empty():
            print(f"{self.fullname.title()} has no privileges!")
            return
        for privilege in self.privileges:
            print(f"{privilege} removed!")
        self.privileges.clear()
        print(f"All privileges for {self.fullname.title()} have been removed!")
        return self.privileges
