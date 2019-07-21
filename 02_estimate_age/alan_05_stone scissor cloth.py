import random
# ls is computer all the choices maybe .
ls = ["stone","scissor","cloth"]
computer = str(random.sample(ls,1))
player = input("Please enter your choices(stone, scissor, cloth):")
print("Player choose %s, Computer choose %s" % (player,computer))
if ((player == "stone" and computer == "cloth")
        or (player == "scissor" and computer == "cloth")
        or (player == "cloth" and computer == "stone")):
    print("Player win!")
elif computer == player:
    print("Draw!")
else:
    print("You losed!")
