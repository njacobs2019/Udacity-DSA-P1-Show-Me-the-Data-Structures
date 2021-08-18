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

grandparents = Group("grandparents")
grandparents.add_user("Papa")
grandparents.add_user("Mimi")

parent1 = Group("parent1")
grandparents.add_group(parent1)
parent1.add_user("Rod")
parent1.add_user("Suzzie")
grandkid1 = Group("grandkid1")
parent1.add_group(grandkid1)
grandkid1.add_user("Rebecca")

parent2 = Group("parent2")
grandparents.add_group(parent2)
parent2.add_user("Wayne")
parent2.add_user("Sue")
grandkid2 = Group("grandkid2")
parent2.add_group(grandkid2)
grandkid2.add_user("Sarah")
grandkid2.add_user("Melissa")
grandkid2.add_user("Andrew")

parent3 = Group("parent3")
grandparents.add_group(parent3)
parent3.add_user("Steve")
parent3.add_user("Jenny")
grandkid3 = Group("grandkid3")
parent3.add_group(grandkid3)
grandkid3.add_user("Kristina")
grandkid3.add_user("Matthew")
greatgrandkid1 = Group("greatgrandkid1")
grandkid3.add_group(greatgrandkid1)
greatgrandkid1.add_user("Jacob")
greatgrandkid1.add_user("Veronica")

parent4 = Group("parent4")
grandparents.add_group(parent4)
parent4.add_user("Stu")
parent4.add_user("Cindy")
grandkid4 = Group("grandkid4")
parent4.add_group(grandkid4)
grandkid4.add_user("Alex")
grandkid4.add_user("Nate")

parent5 = Group("parent5")
grandparents.add_group(parent5)
parent5.add_user("Brian")
parent5.add_user("Lauri")
grandkid5 = Group("grandkid5")
parent5.add_group(grandkid5)
grandkid5.add_user("Nick")
grandkid5.add_user("Liz")

# Print group structure
print(grandparents)
print(grandparents.groups[0])
print(grandparents.groups[1])
print(grandparents.groups[2])
print(grandparents.groups[3])
print(grandparents.groups[4])
print(grandparents.groups[0].groups[0])
print(grandparents.groups[1].groups[0])
print(grandparents.groups[2].groups[0])
print(grandparents.groups[3].groups[0])
print(grandparents.groups[4].groups[0])
print(grandparents.groups[2].groups[0].groups[0])

people = ["Mimi","Papa", "Rod", "Suzzie", "Rebecca", "Wayne", "Sue", "Sarah", "Melissa","Andrew", "Steve", "Jenny",
          "Kristina", "Matthew", "Jacob", "Veronica", "Stu", "Cindy", "Alex", "Nate", "Brian", "Lauri", "Nick",
          "Liz", "Leigh", "Joanie", "Jill", "Pat", "Mickey", "Big Dog", "", "big-dog"]

for person in people:
    exist = is_user_in_group(person, grandparents)
    print("{} - {}".format(person, exist))