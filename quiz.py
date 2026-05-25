print ("Hello. Welcome to my quiz about animals.")
print("               /'.    .'\                ")
print("               \( \__/ )/                ")
print("         ___   / (.)(.) \                ")
print("    _.-`_  `-.|  ____  |.-`  _`‘-._      ")
print(" .-'.-'//||`'-.\  V--V  /.-'`||\\'-.'-.  ")
print("`'-'-.// ||    / .___.  \    || \\.-'-'` ")
print("      `-.||_.._|        |_.._||.-'       ")
print("              \ ((  )) /                 ")
print("           jgs  '.    .'                 ")
print("                  `\/`                   ")

question1 = input("What is your favourite animal?")
print ("Oh!I like " + question1 + " ,too.That's a great animal.")
question2 = input("Why do you like it?")
print ("Sounds interesting.It's a meaningful reason.")

question3 = input("Do you think bats are as big as elephants? A：yes B：no C：not sure.")
if question3 == "yes":
    print ("well done! Your correct")
elif question3 == "Yes":
    print ("well done! Your correct")
elif question3 == "A":
    print ("well done! Your correct")
else:
    print ("Oh no.Your wrong.It's yes.")
question4 = input("What is the largest mammal in the world? A:Elephants B:people C:Balaenoptera musculus")
if question4 == "C":
    print ("well done! Your correct")
elif question4 == "Balaenoptera musculus":
    print ("well done! Your correct")
elif question4 == "Balaenoptera Musculus":
    print ("well done! Your correct")
else:
    print ("Oh no.The correct answer is C")
