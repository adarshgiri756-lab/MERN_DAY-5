import random

dice_art = {1 :( "┌─────────┐",
                 "│         │",
                 "│    ●    │",
                 "│         │",
                 "└─────────┘"),
            
            2 :( "┌─────────┐",
                 "│ ●       │",
                 "│         │",
                 "│       ● │",
                 "└─────────┘"),
                
            3 : ("┌─────────┐",
                 "│ ●       │",
                 "│    ●    │",
                 "│       ● │",
                 "└─────────┘"),
            
            4 : ("┌─────────┐",
                 "│ ●     ● │",
                 "│         │",
                 "│ ●     ● │",
                 "└─────────┘"),

            5 : ("┌─────────┐",
                 "│ ●     ● │",
                 "│    ●    │",
                 "│ ●     ● │",
                 "└─────────┘"),

            6 :( "┌─────────┐",
                 "│ ●     ● │",
                 "│ ●     ● │",
                 "│ ●     ● │",
                 "└─────────┘") 
                 }

total = 0
dices = []
number_of_dices = int(input("Enter the number of dices:"))
print("Your dices and its total are :")


# This loop is for printing the dices in vertical order -

# for i in range(number_of_dices):
#     dices = random.randint(1,6)
#     total += dices
#     for j in dice_art.get(dices):
#         print(j)

# This loop is for printing the dices in Horizontal order - 

for i in range(number_of_dices):
    dices.append(random.randint(1,6))
    total += dices[i]

for k in range(5):
    for i in range(number_of_dices):
        
        for j in dice_art.get(dices[i])[k]:
            print(j,end= "")
       
    print()

        
print(f"Your total is :{total}")

  