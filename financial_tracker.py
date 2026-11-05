

# Financial Tracker - version 1.1


def get_incomes():
    incomes = []
    
    while True :
        income = input("Enter daily income or done: ")
        if income == "done":
            return incomes 
        
        try :
            
            income = int(income)
            
            if income <= 0:
                print("Income must be greater than zero")
                continue 
           
            incomes.append(income)
            
            
        except ValueError:
            print("you should enter a number!")
            
        
def get_expense():
    expenses = []
    
    while True :
        expense = input("Enter your daily expense or done: ")
        if expense == "done":
            return expenses
        
        try :
            expense = int(expense)
            
            if expense <= 0:
                print("Expense must be greater than zero")
                continue
            
            expenses.append(expense)
            
        except ValueError:
            print("you should enter a number!")
            
            

def calculate_total(values):
    if not values:
        print("you should add a number to calculate the total number!")
        return 0
    
    else:
        return sum(values)
        



def calculate_average(values):
    
    if not values:
        print("you should add a number to calculate the average number!")
        return 0
    
    else :
        return sum(values) / len(values)            
                        
            


def find_maximum(values):
    
    if not values:
        print("you should add a number for us to be able to find the biggest number!")
        return 0
    
    else :
        return max(values)
        



def show_report (total_income , total_expense , remaining , average_income , average_expense , max_income , max_expense):
    
    print("\n Total income: "  , total_income  )
    print("Total expense: " ,  total_expense)
    print("Average income:" , average_income)
    print("Average expense:" , average_expense)
    print("Biggest income:" , max_income)
    print("Biggest expense:" , max_expense)
    print("Remaining money:" , remaining)
    

    
    
def save_report(total_income , total_expense , remaining , average_income , average_expense , max_income , max_expense):
    
    with open("report.txt" , "a" , encoding="utf-8") as file:
        
        file.write("\n----FINAL REPORT:----\n")
        file.write(f"Total income: {total_income} \n")
        file.write(f"Total expense: {total_expense} \n")
        file.write(f"Average income: {average_income}\n")
        file.write(f"Average expense: {average_expense}\n")
        file.write(f"Biggest income: {max_income}\n ")
        file.write(f"Biggest expense: {max_expense}\n ")
        file.write(f"Remaining: {remaining } " )
          
    
income_result = get_incomes()
expense_result = get_expense()


total_income = calculate_total(income_result)
total_expense = calculate_total(expense_result)
remaining = total_income - total_expense


average_income = calculate_average(income_result)
average_expense = calculate_average(expense_result)


max_income = find_maximum(income_result)
max_expense = find_maximum(expense_result)


show_report(total_income , total_expense , remaining , average_income , average_expense , max_income , max_expense)
save_report(total_income , total_expense , remaining , average_income , average_expense , max_income , max_expense)


print("your report has been updated!")


