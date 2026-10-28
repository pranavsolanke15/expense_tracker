import json

FILE = "expenses.json"

def load():
    try:
        with open(FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add(expenses):
    title = input("Kharcha kis cheez ka? ")
    amount = float(input("Amount: "))
    category = input("Category (food/travel/other): ")
    expenses.append({"title": title, "amount": amount, "category": category})
    save(expenses)
    print("Add ho gaya!")

def show(expenses):
    for i, e in enumerate(expenses, 1):
        print(i, e["title"], e["amount"], e["category"])
    print("Total:", sum(e["amount"] for e in expenses))
def delete(expenses):
    show(expenses)
    num = int(input("Kaunsa number delete karna hai? "))
    if 1 <= num <= len(expenses):
        expenses.pop(num - 1)
        save(expenses)
        print("Delete ho gaya!")
    else:
        print("Galat number")

def category_total(expenses):
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    for cat, amt in totals.items():
        print(cat, ":", amt)
expenses = load()
while True:
    choice = input("\n1. Add  2. Show  3. Delete  4. Category Total  5. Exit: ")
    if choice == "1":
        add(expenses)
    elif choice == "2":
        show(expenses)
    elif choice == "3":
        delete(expenses)
    elif choice == "4":
        category_total(expenses)
    else:
        break