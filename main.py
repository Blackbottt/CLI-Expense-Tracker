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
    categories = [
        {
            "type": "Geschaft",
            "options": {
                "A": "Werbetreibend",
                "B": "Bürobedarfsartikel",
                "C": "Reiseausgaben",
                "D": "Versorgungswirtschaft",
                "E": "Beratungskosten",
                "F": "Andere"
            }
        },
        {
            "type": "Persönlich",
            "options": {
                "A": "Wohnungs[Miete/Belehnen]",
                "B": "Verkehrsmittel(Benzin/Öffentliche)",
                "C": "Essen(Lebensmittel/außer Haus)",
                "D": "Gesundheit(Versicherung/Medizinische Ausgaben)",
                "E": "Unterhaltung",
                "F": "Andere"
            }
        },
        {
            "type": "Haushalt Nebenkosten",
            "options": {
                "A": "Nebenkosten(Elekrizitat/Wasser)",
                "B": "Versicherung(Hause/Auto)",
                "C": "Abspeicherungen(Vorsorgevermögen/Notfallfonds)",
                "D": "Bildung(Unterrichtsgebühr/Materialen)",
                "E": "Andere"
            } 
        },
    ]

    print(" \n1. Geschaft \n2. Persönlich \n3. Haushalt Nebenkosten")
    category_type = validator(int, "Wählen Ihrer Budget typisieren: ")

    if category_type == 1:
        print("A. Werbetreibend\nB. Bürobedarfsartikel\nC. Reiseausgaben \nD. Versorgungswirtschaft \nE. Beratungskosten \nF. Andere")
        category_option = validator(str, "Welcher Wahl bitte A, B...?").upper()
        category_option = categories[category_type - 1]["options"][category_option]
        category_type = categories[category_type - 1]["type"]
        return f"{category_type} ({category_option})"
    elif category_type == 2:
        print("\nA. Wohnungs(Miete/Belehnen) \nB. Verkehrsmittel(Benzin/Öffentliche) \nC. Essen(Lebensmittel/außer Haus) \nD. Gesundheit(Versicherung/Medizinische Ausgaben) \nE. Unterhaltung \nF. Andere")
        category_option = validator(str, "Welcher Wahl bitte A, B...?").upper()
        category_option = categories[category_type - 1]["options"][category_option]
        category_type = categories[category_type - 1]["type"]
        return f"{category_type} ({category_option})"
    elif category_type == 3:
        print("\nA. Nebenkosten(Elekrizitat/Wasser) \nB. Versicherung(Hause/Auto) \nC. Abspeicherungen(Vorsorgevermögen/Notfallfonds) \nD. Bildung(Unterrichtsgebühr/Materialen) \nE. Andere")
        category_option = validator(str, "Welcher Wahl bitte A, B...?").upper()
        category_option = categories[category_type - 1]["options"][category_option]
        category_type = categories[category_type - 1]["type"]
        return f"{category_type} ({category_option})"
    
def add_expense():
    name = validator(str, "Name :")
    amount =  validator(float, "Betrag :")
    category = add_category()
    date_iso = datetime.datetime.now().isoformat()
    date = datetime.datetime.fromisoformat(date_iso).strftime("%a %d %B %Y")
    return {"name": name, "amount": amount, "date": date, "category": category}

def show_expenses(expenses):
    if not expenses:
        print("Keine Ausgaben vorhanden")
        return
        
    for i, expense in enumerate(expenses, 1):
            print("\n")
            print(f'{i}. {expense["name"]} | ${expense["amount"]:.2f} | {expense["category"]} | {expense["date"]}')

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

