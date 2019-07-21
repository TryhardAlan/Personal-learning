has_ticket = input("Do you have a ticket? Please enter True or False!")
knife_length = int(input("Please enter you knife length!"))
if has_ticket:
    if knife_length > 20:
        print("Your knife length is %d, you are't obey to get up train!" % knife_length)
    else:
        print("You are allowed to get up train!")
else:
    print("You can't get in!")
