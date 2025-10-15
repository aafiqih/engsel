from dotenv import load_dotenv

load_dotenv() 

import sys
from app.menus.util import clear_screen, pause
from app.client.engsel import *
from app.menus.payment import show_transaction_history
from app.service.auth import AuthInstance
from app.menus.bookmark import show_bookmark_menu
from app.menus.account import show_account_menu
from app.menus.package import fetch_my_packages, get_packages_by_family
from app.menus.hot import show_hot_menu, show_hot_menu2
from app.service.sentry import enter_sentry_mode
from app.menus.purchase import purchase_by_family, purchase_loop

def show_main_menu(active_user):
    clear_screen()
    print(f"Active Number: {active_user['number']}")
    print("-------------------------------------------------------")
    print("Menu:")
    print("1. Login/Ganti akun")
    print("2. [Test] Purchase all packages in family code")
    print("-------------------------------------------------------")
    print("List Bot Auto Looping:")
    print("3. Bebas Puas + 30H Mastif")
    print("4. Bonus Kuota Utama 45GB")
    print("5. Bonus Kouta Malam 60GB")
    print("6. Bonus Youtube+Tiktok 42GB")
    print("7. Xtra Combo Flex S")
    print("8. Bonus Flex Main Quota 25GB")
    print("9. Bonus Flex Youtube Quota 14GB")
    print("10. Bonus Flex Night Quota 60GB")
    print("11. Bonus Flex TikTok 8GB")
    print("99. Tutup aplikasi")
    print("-------------------------------------------------------")

show_menu = True
def main():
    
    while True:
        active_user = AuthInstance.get_active_user()

        # Logged in
        if active_user is not None:
            show_main_menu(active_user)

            choice = input("Pilih menu: ")
            if choice == "1":
                selected_user_number = show_account_menu()
                if selected_user_number:
                    AuthInstance.set_active_user(selected_user_number)
                else:
                    print("No user selected or failed to load user.")
                continue
            elif choice == "2":
                family_code = input("Enter family code (or '99' to cancel): ")
                if family_code == "99":
                    continue
                use_decoy = input("Use decoy package? (y/n): ").lower() == 'y'
                pause_on_success = input("Pause on each successful purchase? (y/n): ").lower() == 'y'
                purchase_by_family(family_code, use_decoy, pause_on_success)
            elif choice == "3":
                delay = int(input("Enter delay in seconds: "))
                while True:
                    if not purchase_loop(
                        family_code='0069ab97-3e54-41ef-87ea-807621d1922c',
                        order=1,
                        use_decoy=True,
                        delay=delay,
                        pause_on_success=False
                    ):
                        break
            elif choice == "4":
                delay = int(input("Enter delay in seconds: "))
                while True:
                    if not purchase_loop(
                        family_code='5412b964-474e-42d3-9c86-f5692da627db',
                        order=64,
                        use_decoy=True,
                        delay=delay,
                        pause_on_success=False
                    ):
                        break
            elif choice == "5":
                delay = int(input("Enter delay in seconds: "))
                while True:
                    if not purchase_loop(
                        family_code='5412b964-474e-42d3-9c86-f5692da627db',
                        order=34,
                        use_decoy=True,
                        delay=delay,
                        pause_on_success=False
                    ):
                        break
            elif choice == "6":
                delay = int(input("Enter delay in seconds: "))
                while True:
                    if not purchase_loop(
                        family_code='5412b964-474e-42d3-9c86-f5692da627db',
                        order=64,
                        use_decoy=True,
                        delay=delay,
                        pause_on_success=False
                    ):
                        break
            elif choice == "7":
                delay = int(input("Enter delay in seconds: "))
                while True:
                    if not purchase_loop(
                        family_code='4a1acab0-da54-462c-84b1-25fd0efa9318',
                        order=1,
                        use_decoy=True,
                        delay=delay,
                        pause_on_success=False
                    ):
                        break
            elif choice == "8":
                delay = int(input("Enter delay in seconds: "))
                while True:
                    if not purchase_loop(
                        family_code='1b42d4f6-a76e-4986-aa5c-e2979da952f4',
                        order=21,
                        use_decoy=True,
                        delay=delay,
                        pause_on_success=False
                    ):
                        break  
            elif choice == "9":
                delay = int(input("Enter delay in seconds: "))
                while True:
                    if not purchase_loop(
                        family_code='1b42d4f6-a76e-4986-aa5c-e2979da952f4',
                        order=1,
                        use_decoy=True,
                        delay=delay,
                        pause_on_success=False
                    ):
                        break        
            elif choice == "10":
                delay = int(input("Enter delay in seconds: "))
                while True:
                    if not purchase_loop(
                        family_code='1b42d4f6-a76e-4986-aa5c-e2979da952f4',
                        order=110,
                        use_decoy=True,
                        delay=delay,
                        pause_on_success=False
                    ):
                        break        
            elif choice == "11":
                delay = int(input("Enter delay in seconds: "))
                while True:
                    if not purchase_loop(
                        family_code='1b42d4f6-a76e-4986-aa5c-e2979da952f4',
                        order=61,
                        use_decoy=True,
                        delay=delay,
                        pause_on_success=False
                    ):
                        break             
            elif choice == "99":
                print("Exiting the application.")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
                pause()
        else:
            # Not logged in
            selected_user_number = show_account_menu()
            if selected_user_number:
                AuthInstance.set_active_user(selected_user_number)
            else:
                print("No user selected or failed to load user.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting the application.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")
