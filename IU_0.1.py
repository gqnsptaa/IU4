def main():
    FILE_NAME = "golf.csv"
    results = read_results_from_file(FILE_NAME)

    print("Klubbmästerskap i minigolf!")
    print("---------------------------")

    while True:
        print_menu()

        user_choice = input("Val: ")

        if user_choice == "1":
            print_result(results, "Resultater")
        elif user_choice == "2":
            add_result(results, FILE_NAME)
        elif user_choice == "3":
            remove_result(results, FILE_NAME)
        elif user_choice == "4":
            break
        else:
            print("Du valde inte ett giltigt alternativ, försök igen!")

def print_result(result_list, title):
    print(f"{title}")
    print("-"*87)
    print(f"{'Namn':<15}{'1':<15}{'2':<15}{'3':<15}{'Totalt':<15}{'Genomsnitt':<15}")
    print("-"*87)
    for result in result_list:
        for item in result:
            print(f"{item:<15}", end="")
        print("")

def add_result(result_list, filename):
    print("\nLägg till en resultat")
    print("-"*30)
    while True:
        namn = input("Namn: ")
        if not namn.isalpha():
            print("Du måste ange bokstaver!")
            continue
        
        try:
            first_result = int(input("1: "))
            second_result = int(input("2: "))
            third_result = int(input("3: "))
            total = first_result + second_result + third_result
            genomsnitt = round(total / 3)
            break            
        except ValueError:
            print("Du måste ange siffror!")

    result = [namn, first_result, second_result, third_result, total, genomsnitt]
    result_list.append(result)
    save_file(result_list, filename)

def remove_result(result_list, filename):
    print("\nTa bort en resultat")
    print("-"*30)
    remove_name = input("Vems resultat vill du radera? ")
    result_removed = False

    for result in result_list:
        if result[0] == remove_name:
            result_list.remove(result)
            result_removed = True
            break 

    if result_removed:
        print(f"{remove_name} har raderats!")
        save_file(result_list, filename)
    else:
        print("Det finns ingen person med angiven namn!")

def save_file(result_list, filename):
    file_output = "" 

    for result in result_list:
        file_output += ";".join(map(str, result))+"\n"

    my_file = open(filename, 'w')
    my_file.write(file_output)
    my_file.flush()
    my_file.close()

def print_menu():
    print("\nMeny")
    print("----")
    print("1) Visa resultat")
    print("2) Registrera resultat")
    print("3) Radera resultat")
    print("4) Avsluta")

def read_results_from_file(filename): 
    try:
        my_file = open(filename, "r")
        data = my_file.read()
        my_file.close()

        results = []
        for row in data.split("\n"):
            item = row.split(";")
            if len(item) > 1:
                results.append(item)
        return results 
    except FileNotFoundError:
        my_file = open(filename, "w")
        my_file.close()

        return []
    


main()