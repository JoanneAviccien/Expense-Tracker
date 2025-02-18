import os
from sys import platform
from expense import load_expenses
from read import read_expenses
from menu import display_menu, delete_expense, splash_screen, edit_expenses

# program utama

splash_screen()

while True:
    if platform == "win32":
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.syste('clear')
    expenses = load_expenses()
    read_expenses(expenses)
    display_menu()
    pilihan = int(input("Pilih menu: "))
    match pilihan:
        case 1:
            penambahan()
        case 2:
            delete_expense()
        case 2:
            edit_expenses()
        case 4:
            saring()
        case 5:
            ringkasan()
        case 6:
            print("Terima kasih telah menggunakan aplikasi!")
            break  # Keluar dari loop

