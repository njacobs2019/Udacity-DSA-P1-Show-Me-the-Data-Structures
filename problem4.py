class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self):
        s=""
        s+="Group-{} ".format(self.name)
        s+="Users {} ".format(self.users)
        s+="Sub groups {} ".format([x.name for x in self.groups])
        return s

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    
    out = False
    for sub_group in group.get_groups():
        out = is_user_in_group(user, sub_group) or out
    return out

if __name__ == '__main__':
    grandparents = Group("grandparents")
    grandparents.add_user("Papa")

    parent1 = Group("parent1")
    grandparents.add_group(parent1)
    parent1.add_user("Rod")
    parent1.add_user("Suzzie")
    grandkid1 = Group("grandkid1")
    parent1.add_group(grandkid1)
    grandkid1.add_user("Rebecca")

    parent2 = Group("parent2")
    grandparents.add_group(parent2)
    parent2.add_user("Wayne J")

    parent3 = Group("parent3")
    grandparents.add_group(parent3)
    parent3.add_user("Jenny")
    grandkid3 = Group("grandkid3")
    parent3.add_group(grandkid3)
    grandkid3.add_user("Kristina")
    greatgrandkid1 = Group("greatgrandkid1")
    grandkid3.add_group(greatgrandkid1)
    greatgrandkid1.add_user("Jacob")

    parent4 = Group("parent4")
    grandparents.add_group(parent4)
    grandkid4 = Group("grandkid4")
    parent4.add_group(grandkid4)
    grandkid4.add_user("Alex")
    grandkid4.add_user("Nate")
    grandkid4.add_user(5)
    grandkid4.add_user(None)

    parent5 = Group("parent5")
    grandparents.add_group(parent5)
    parent5.add_user("Lauri")
    grandkid5 = Group("grandkid5")
    grandkid5.add_user("Nick")


    people = ["Papa", "Wayne J", "Jenny", "Kristina", "Jacob", "Alex", "Nate", "Lauri", "Nick", "Jill", "Big Dog", "", "big-dog", 5, None]

    for person in people:
        exist = is_user_in_group(person, grandparents)
        print("{} - {}".format(person, exist))

    # Results:
    # Papa - True
    # Wayne J - True
    # Jenny - True
    # Kristina - True
    # Jacob - True
    # Alex - True
    # Nate - True
    # Lauri - True
    # Nick - False    Not connected to grandparents group
    # Jill - False
    # Big Dog - False
    #  - False
    # big-dog - False
    # 5 - True
    # None - True