# HODI - A simple swahili learning app

def show_menu():
    print("\nKaribu HODI – Jifunze Kiswahili!")
    print("----------------------------------")
    print("1. Learn Greetings")
    print("2. Learn Numbers")
    print("3. Take a Quiz")
    print("4. Exit")

def learn_greetings():
    greetings = {
        "Hello": "Habari",
        "Good morning": "Asubuhi njema",
        "Good night": "Usiku mwema",
        "Thank you": "Asante",
        "How are you?": "Habari yako?"
    }
    print("\n--- Swahili Greetings ---")
    for eng, swa in greetings.items():
        print(f"{eng} → {swa}")

def learn_numbers():
    numbers = {
        "One": "Moja",
        "Two": "Mbili",
        "Three": "Tatu",
        "Four": "Nne",
        "Five": "Tano"
    }
    print("\n--- Swahili Numbers ---")
    for eng, swa in numbers.items():
        print(f"{eng} → {swa}")

def take_quiz():
    print("\n--- Swahili Quiz ---")
    score = 0

    answer = input("What is 'Thank you' in Swahili? ").strip().lower()
    if answer == "asante":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ It's 'Asante'.")

    answer = input("What is 'Two' in Swahili? ").strip().lower()
    if answer == "mbili":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ It's 'Mbili'.")

    print(f"\nYour score: {score}/2")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ").strip()

    if choice == '1':
        learn_greetings()
    elif choice == '2':
        learn_numbers()
    elif choice == '3':
        take_quiz()
    elif choice == '4':
        print("Asante kwa kutumia HODI! Tutaonana tena.")
        break
    else:
        print("⚠️ Please choose a valid option.")
