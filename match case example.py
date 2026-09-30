menu = []

while True:
    try:
        choice = input("1. Add  2. View  3. Exit: ").strip().lower()
        match choice:
            case "1" | "add":
                menu.append(input("Item: "))
                print("Added.")
            case "2" | "view":
                print(menu if menu else "Nothing yet.")
            case "3" | "exit":
                print("Bye!")
                break
            case _:
                print("Invalid choice.")
    except KeyboardInterrupt:
        print("Exiting.")
        break
              
                       
