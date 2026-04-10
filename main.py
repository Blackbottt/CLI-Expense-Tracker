import datetime
import json

def validator(data_type, prompt):
    if data_type == str:
        user_input = input(prompt)

        while not user_input.strip():
            print("Fehler: Bitte Input Name als Wörter")
            user_input = input("Name: ")
    
        return user_input
    
    elif data_type == float:
        while True:
            user_input = input(prompt)
            try:
                user_input = float(user_input)
                if user_input <= 0:
                    print("Bitte positiven Betrag eingeben")
                else:
                    break
            except ValueError:
                print("Bitte positiven Betrag eingeben")

        return user_input

    elif data_type == int:
        while True:
            user_input = input(prompt)
            try:
                user_input = int(user_input)
                break
            except ValueError:
                print("Bitte positiven Betrag eingeben")
        
        return user_input

    else:
        raise ValueError("Unsupported data type")

def add_category():
    print("Budget typisieren: \n1. Geschaft \n2. Persönlich \n3. Haushalt Nebenkosten")
    budget_type = input("Wählen Ihrer Budget typisieren: ")

    try:
        budget_type = int(budget_type)
    except ValueError:
        print("Bitte existiert Betrag eingeben")
    print("Budget typisieren: \n1. Geschaft \n2. Persönlich \n3. Haushalt Nebenkosten")
    # category = input("Category: ")
    if budget_type == "1":
        print("Kategorian: \n1. Werbetreibend\n2. Bürobedarfsartikel\n3. Reiseausgaben \n4. Versorgungswirtschaft \n5. Beratungskosten")

    elif budget_type == "2":
        print("Kategorian: \n1. Wohnungs (Miete/Belehnen) \n2. Verkehrsmittel (Benzin/Öffentliche) \n3. Essen (Lebensmittel/außer Haus) \n4. Gesundheit (Versicherung/ Medizinische Ausgaben) /n5. 	Unterhaltung")

    elif budget_type == "3":
        print("Kategorian: \n1. Nebenkosten (Elekrizitat/Wasser) \n2. Versicherung (Hause/Auto) \n3. Abspeicherungen (Vorsorgevermögen/Notfallfonds) \n4. Bildung (Unterrichtsgebühr/Materialen)")

def add_expense():
    name = validator(str, "Name :")
    amount =  validator(float, "Betrag :")
    date_iso = datetime.datetime.now().isoformat()
    date = datetime.datetime.fromisoformat(date_iso).strftime("%a %d %B %Y")
    # add_category()
    return {"name": name, "amount": amount, "date": date}

def show_expenses(expenses):
    if not expenses:
        print("Keine Ausgaben vorhanden")
        return
        
    for i, expense in enumerate(expenses, 1):
            print("\n")
            print(f'{i}. {expense["name"]} | ${expense["amount"]:.2f} | {expense["date"]}')

    total = sum(expense["amount"] for expense in expenses)
    print(f"\nGesamt Budget ist {total:.2f}")

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

    print("\nWelche Nummer möchten Sie löschen?")

    while True:
        try:
            index = int(input("Löscht: "))
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

    wähle = input("\nWähle: ")

    if wähle == "1":
        expense = add_expense()
        print("expense", expense)
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
            if confirmation == "j":    
                expenses.pop(to_be_deleted)
                print("Eintrag gelöscht.")
                save_expenses(expenses)
            else:
                show_expenses(expenses)
    
    else:
        print("Ungültige Eingabe")

