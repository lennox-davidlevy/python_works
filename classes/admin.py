from users import User
from privilegs import Privileges

# add privileges = [strings:can add post, can delete, can ban]
# add show privileges
# add add privileges
# add remove privileges
# then make privileges its own class


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges(self.fullname)


my_admin = Admin("David", "levy", 35, "queens")
my_admin.describe_user()
my_admin.privileges.show_privileges()
my_admin.privileges.add_privilege("ban")
my_admin.privileges.show_privileges()
my_admin.privileges.add_many_privileges(["ban", "mute", "add post", "delete post"])
my_admin.privileges.show_privileges()
my_admin.privileges.remove_all_privileges()
my_admin.privileges.show_privileges()
