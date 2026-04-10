import datetime
import json

def add_expense():
    name = input("Name: ")
    while not name.strip():
        print("Fehler: Bitte Input Name als Wörter")
        name = input("Name: ")

    date = datetime.datetime.now().isoformat()

    while True:
        amount = input("Betrag: ")
        try:
            amount = float(amount)
            if amount <= 0:
                print("Bitte positiven Betrag eingeben")
            else:
                break
        except ValueError:
            print("Bitte positiven Betrag eingeben")

    return {"name": name, "amount": amount, "date": date}

def show_expenses(expenses):
    if not expenses:
        print("Keine Ausgaben vorhanden")
        return
    
    for i, expense in enumerate(expenses, 1):
        print(f'{i}. {expense["name"]} | ${expense["amount"]:.2f} | {expense["date"]}')

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

expenses = load_expenses()

while True:
    print("\n1. Hinzufügen")
    print("2. Anzeigen")
    print("3. Beenden")

    wähle = input("Wähle: ")

    if wähle == "1":
        expense = add_expense()
        expenses.append(expense)
        save_expenses(expenses)

    elif wähle == "2":
        show_expenses(expenses)
        
    elif wähle == "3":
        save_expenses(expenses)
        break

    else:
        print("Ungültige Eingabe")

