import random

def roll_dice():
    dice_drowing = {
         1:(
        " __________",
        "|     1    |",
        "|          |",
        "|     0    |",
        "|          |",
        "|__________|"
    ),
           2:(
        " __________",
        "|  0       |",
        "|          |",
        "|     2    |",
        "|        0 |",
        "|__________|"
    ),
           3:(
        " __________",
        "| 0    3   |",
        "|          |",
        "|    0     |",
        "|       0  |",
        "|__________|"
    ),
           4:(
        " __________",
        "|  0    0  |",
        "|          |",
        "|     4    |",
        "|  0     0 |",
        "|__________|"
    ),
           5:(
        " __________",
        "|  0  5  0 |",
        "|          |",
        "|     0    |",
        "|  0     0 |",
        "|__________|"
    ),
            6:(
        " __________",
        "|  0     0 |",
        "|          |",
        "|  0  6  0 |",
        "|          |",
        "|  0     0 |",
        "|__________|"
    ),
}

  
    roll = input("Roll the dice? (Yes/No): ")
    
    while roll.lower() == "yes":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        
        print("Dice rolled: {} and {}".format(dice1,dice2))
        print("\n".join(dice_drowing[dice1]))
        print("\n".join(dice_drowing[dice2]))
        
        roll = input("Roll again (yes/no): ")
roll_dice()