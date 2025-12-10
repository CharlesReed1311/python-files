file = open("exercises/members.txt", 'r')
members = file.readlines()
file.close()

new_member = input("Add a new member: ") + "\n"
members.append(new_member)

file = open("exercises/members.txt", 'w')
file.writelines(members)
file.close()
