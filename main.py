import datetime
import json

def validator(prompt, rule_function):
    user_input = input(prompt)
    user_input = rule_function(user_input)
    return user_input
    # else:
        # raise ValueError("Unsupported data type")

def string_validation_logic(user_input, prompt):
    while not user_input.strip():
        print("Fehler: Bitte Input Name als Wörter")
        user_input = input("Name: ")
    return user_input

def float_validation_logic(user_input, prompt):
    while True:
        user_input = input("Betrag :")
        try:
            user_input = float(user_input)
            if user_input <= 0:
                print("Bitte positiven Betrag eingeben")
            else:
                break
        except ValueError:
            print("Bitte positiven Betrag eingeben")

def integer_validation_logic(user_input, prompt):
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            break
        except ValueError:
            print("Bitte positiven Betrag eingeben")
        
    return user_input


def validate_index(list, prompt1, prompt2):
    # this function is different from validator because it validates list index numbers
    if not list:
        print("Keine Ausgaben vorhanden")
        return None

    print(prompt1)

    while True:
        try:
            index = int(input(prompt2))
            if index < 1 or index > len(list):
                print("Eintrag existiert nicht!")
            else:
                break
        except ValueError:
            print("Bitte positiven Betrag eingeben")
    
    validated_index = index - 1
    return validated_index

def add_category(filter="OFF"):
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

    if filter == "OFF":
        print(" \n1. Geschaft \n2. Persönlich \n3. Haushalt Nebenkosten")
        category_type = validator(int, "Wählen Ihrer Budget typisieren: ")

        if category_type == 1:
            print("A. Werbetreibend\nB. Bürobedarfsartikel\nC. Reiseausgaben \nD. Versorgungswirtschaft \nE. Beratungskosten \nF. Andere")
            while True:
                category_option = validator(str, "Welcher Wahl bitte A, B...?").upper()
                if any(value == category_option for value in categories[category_type - 1]["options"].keys()):
                    break
                else:
                    print("Bitte gib einen bestehende option")
            category_option = categories[category_type - 1]["options"][category_option]
            category_type = categories[category_type - 1]["type"]
            return f"{category_type} ({category_option})"
        elif category_type == 2:
            print("\nA. Wohnungs(Miete/Belehnen) \nB. Verkehrsmittel(Benzin/Öffentliche) \nC. Essen(Lebensmittel/außer Haus) \nD. Gesundheit(Versicherung/Medizinische Ausgaben) \nE. Unterhaltung \nF. Andere")
            while True:
                category_option = validator(str, "Welcher Wahl bitte A, B...?").upper()
                if any(value == category_option for value in categories[category_type - 1]["options"].keys()):
                    break
                else:
                    print("Bitte gib einen bestehende option")
            category_option = categories[category_type - 1]["options"][category_option]
            category_type = categories[category_type - 1]["type"]
            return f"{category_type} ({category_option})"
        elif category_type == 3:
            print("\nA. Nebenkosten(Elekrizitat/Wasser) \nB. Versicherung(Hause/Auto) \nC. Abspeicherungen(Vorsorgevermögen/Notfallfonds) \nD. Bildung(Unterrichtsgebühr/Materialen) \nE. Andere")
            while True:
                category_option = validator(str, "Welcher Wahl bitte A, B...?").upper()
                if any(value == category_option for value in categories[category_type - 1]["options"].keys()):
                    break
                else:
                    print("Bitte gib einen bestehende option")
            category_option = categories[category_type - 1]["options"][category_option]
            category_type = categories[category_type - 1]["type"]
            return f"{category_type} ({category_option})"
    else:
        print(" \nA. Geschaft \nB. Persönlich \nC. Haushalt Nebenkosten")
        category_type = validator(str, "Wählen Ihrer Filtern Kategorie: ").upper()
        if category_type == "A": category_type = 0
        elif category_type == "B": category_type = 1
        elif category_type == "C": category_type = 2
        category_type = categories[category_type]["type"]
        return category_type

def add_expense():
    name = validator(str, "Name :")
    amount =  validator(float, "Betrag :")
    category = add_category()
    date_iso = datetime.datetime.now().isoformat()
    date_readable = datetime.datetime.fromisoformat(date_iso).strftime("%a %d %B %Y")
    return {"name": name, "amount": amount, "date": [date_iso, date_readable], "category": category}

def show_expenses(expenses, filter="OFF"):
    if not expenses:
        print("Keine Ausgaben vorhanden")
        return

    if filter == "OFF":    
        for i, expense in enumerate(expenses, 1):
            if i == 1: print("\n")
            print(f'{i}. {expense["name"]} | ${expense["amount"]:.2f} | {expense["category"]} | {expense["date"][1]}')
        total = sum(expense["amount"] for expense in expenses)
    elif filter == "summary":
        month = validator(str, "month :").lower()

        for i, expense in enumerate(expenses, 1):
            date_str = datetime.datetime.fromisoformat(expense["date"][0]).strftime("%B").lower()
            if month == date_str:
                if i == 1: print("\n")
                print(f'{i}. {expense["name"]} | ${expense["amount"]:.2f} | {expense["category"]} | {expense["date"][1]}')
        total = sum(expense["amount"] for expense in expenses if expense["date"][1])

    else:
        filter_found = False
        for i, expense in enumerate(expenses, 1):
            if expense["category"].startswith(filter):
                filter_found = True
                if i == 1: print("\n")
                print(f'{i}. {expense["name"]} | ${expense["amount"]:.2f} | {expense["category"]} | {expense["date"][1]}')
        if filter_found == False:
            print("Kein Ausgaben von diese Kategorie")
        total = sum(expense["amount"] for expense in expenses if expense["category"].startswith(filter))

    print(f"\nGesamt Budget ist {total:.2f}")

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def show_menu():
    expenses = load_expenses()
    
    if expenses == []:
        print("\n1. Hinzufügen")
        print("2. Anzeigen")
        print("3. Beenden")
    else:
        print("\n1. Hinzufügen")
        print("2. Anzeigen")
        print("3. Beenden")
        print("4. Löschen")
        print("5. Bearbeiten")
        print("6. Nach Kategorie Filtern")
        print("7. Monatlich Summary")

    return expenses

while True:
    expenses = show_menu()
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
        delete = validate_index(expenses, "\nWelche Nummer möchten Sie löschen?", "Löscht: ")

        if delete is not None:
            confirmation = input("Sind sie sicher? (j/n)").lower()
            if confirmation == "j": 
                expenses.pop(delete)
                print("Eintrag gelöscht.")
            save_expenses(expenses)
            show_expenses(expenses)
    
    elif wähle == "5":
        show_expenses(expenses)
        edit = validate_index(expenses, "\nWelche Nummer möchten Sie Bearbeiten?", "Bearbeitet: ")

        if edit is not None:
            print("Whelcher Wert sie bearbeiten möchten?")
            specification = validator(str, "Name/Betrag/Kategorie: ").lower()

            if specification == "name":
                name = validator(str, "Name :")
                expenses[edit]["name"] = name

            elif specification == "betrag":
                amount =  validator(float, "Betrag :")
                expenses[edit]["amount"] = amount

            elif specification == "kategorie":
                category = add_category()
                expenses[edit]["category"] = category
            print("Eintrag bearbeitet.")
            save_expenses(expenses)
            show_expenses(expenses)

    elif wähle == "6":
        category_type = add_category(filter="ON")
        show_expenses(expenses, filter=f"{category_type}")

    elif wähle == "7":
        show_expenses(expenses, filter="summary")

    else:
        print("Ungültige Eingabe")

