import random

min_value=1
max_value=6
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The value is....")
    value1=random.randint(min_value, max_value)
    print(value1)
    roll_again = input("Press 'y' or 'yes' to roll the dices again.")
print("Have a good day.")


# ACT 1 (MISSOURI/NEBRASKA)
  #1: One of your party catches tuberculosis. Spend one medicine or allow them to die.
  #2: Your wagon axle breaks on an uneven part of a hill.
  #3: Your ox gets tuberculosis.
  #4: You are hit by a stray bullet while hunting.
  #5: You come across a wide bend in the Missouri River. You must ford the river to pass.
  #6: Nothing happens.
