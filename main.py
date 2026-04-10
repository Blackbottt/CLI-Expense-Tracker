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
    
def get_delete_index(expenses):
    if not expenses:
        print("Keine Ausgaben vorhanden")
        return None

    print("Welche Nummer möchten Sie löschen?")

    while True:
        index = int(input("Löscht: "))
        try:
            if index < 1 or index > len(expenses):
                print("Eintrag existiert nicht!")
            else:
                break
        except ValueError:
            print("Bitte positiven Betrag eingeben")
    
    delete = index - 1
    return delete

expenses = load_expenses()

while True:
    
    if expenses == []:
        print("\n1. Hinzufügen")
        print("2. Anzeigen")
        print("3. Beenden")
    else:
        print("\n1. Hinzufügen")
        print("2. Anzeigen")
        print("3. Beenden")
        print("4. Löschen")

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

    elif wähle == "4":
        show_expenses(expenses)
        to_be_deleted = get_delete_index(expenses)
        if to_be_deleted is not None:
            confirmation = input("Sind sie sicher? (j/n)")
            if confirmation == "j" or confirmation == "J":    
                expenses.pop(to_be_deleted)
                print("Eintrag gelöscht.")
                save_expenses(expenses)
            else:
                show_expenses(expenses)
    
    else:
        print("Ungültige Eingabe")

