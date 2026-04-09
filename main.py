import datetime
import json

expenses = []
global name, amount, date

def save_expenses(exp):
    with open("expenses.json", "w") as f:
        save = json.dumps(exp)
        print("save", save)

while True:
    print("\n 1. Hinzufügen")
    print("2. Anzeigen")
    print("3. Beenden")

    wähle = input("Wähle: ")

    if wähle == "1":
        name = input("Name: ")
        date = datetime.datetime.now().strftime("%d %B %Y")

        while not name.strip():
            print("Fehler: Bitte Input Name als wörter")
            name = input("Name: ")

        while True:
            amount = input("Betrag: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    print("Bitte Input Betrag als positiv nummer")
                else:
                    break    
            except ValueError:
                print("Bitte Input Betrag als positiv nummer")

        expenses.append({"name": name, "amount": amount, "date": date})
        continue

    elif wähle == "2":
        for expense in expenses:
            print(f'{expense["name"]} | ${expense["amount"]:.2f} | {expense["date"]}')
            continue

    elif wähle == "3":
        print("gut last")
        save_expenses(expenses)
        break

print("Ungültige Eingabe")

