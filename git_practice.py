toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def addItem(item):
   toDoList.append(item)
   return toDoList

userAns = input("Do you want to add to your list or quit? A/Q")

while userAns == "A":
   Item = input("What item do you want to add?")
   addItem(Item)
   userAns = input("Do you want to add to your list or quit? A/Q")