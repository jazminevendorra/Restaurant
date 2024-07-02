# This program will prompt user for cost of a meal consumed at a
#restaurant and produce a bill detailing tax, tip, and total amounts

def main():
    # Intro
    print ("Restaurant Bil Generator ...\n")

    #prompt user for cost of food and drinks
    food = eval(input("Please enter cost of food: \t"))
    drinks=eval(input(" \"      \"    cost of drinks: \t"))

    #calculate cost, tax and tip amount
    cost = food + drinks
    tax = cost * 0.075
    tip = (cost + tax) * 0.18
    total = cost + tax + tip

    #display results
    print("\nRestaurant Bill")
    print("--------------------------------")
    print("\nCost of Meal: \t", "$\t", format(cost,'.2f'))
    print("Tax Amount: \t", "$ \t ", format(tax,'.2f'))
    print("Tip Amount: \t", "$ \t ", format(tip,'.2f'))
    print("\t\t---------------")
    print("Total: \t\t","$\t", format(total,'.2f'))

main()
          
                
