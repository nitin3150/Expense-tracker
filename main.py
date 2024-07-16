import csv

def newEntry():
    with open('records.xlsx','w') as file:
        entry = csv.writer(file,delimiter=',')
        date = input("Enter Date(DD/MM/YYYY): ")
        amount = int(input("Enter amount: "))
        Category = input("Category(E for Expenditure and I for income): ")
        description = input("Description(optional): ")
        line = ','.join(date,amount,Category,description)
        entry.writerow(line)

def viewEntry():
    with open('records.csv','r') as file:
        entries = csv.reader(file)

        for entry in entries:
            print(entry)

def main():
    print('''1: Add New entry\n2: View Entries\n3: Exit''')
    select = int(input("Choose an option: "))
    match select:
        case 1:
            newEntry()
        case 2:
            viewEntry()
        case _:
            exit()

if __name__ == "__main__":
    main()