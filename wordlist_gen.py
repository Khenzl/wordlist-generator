import itertools
import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

banner = f"""
{Fore.CYAN}==============================================\n          WORDLIST GENERATOR CLI\n              By: Khenzl\n=============================================={Style.RESET_ALL}\n"""

os.makedirs("results", exist_ok=True)

output_file = "results/wordlist_generated.txt"

def menu():
    print(banner)
    print(f"{Fore.YELLOW}1.{Style.RESET_ALL} Generate Targeted Wordlist")
    print(f"{Fore.YELLOW}0.{Style.RESET_ALL} Exit")
    choice = input(f"\n{Fore.CYAN}[?]{Style.RESET_ALL} Enter your choice: ").strip()
    return choice

def gather_target_info():
    print(f"\n{Fore.YELLOW}Enter target information to generate focused wordlist:{Style.RESET_ALL}")
    name = input("Full Name: ").strip()
    nickname = input("Nickname: ").strip()
    birthdate = input("Birthdate (ddmmyyyy): ").strip()
    birthplace = input("Place of Birth: ").strip()
    address = input("Address: ").strip()
    phone = input("Phone Number: ").strip()
    fav_word = input("Favorite Word: ").strip()
    pet_name = input("Pet's Name: ").strip()
    additional = input("Additional keywords (comma separated): ").strip().split(",")

    base_words = [name, nickname, birthdate, birthplace, address, phone, fav_word, pet_name] + additional
    base_words = [word.lower() for word in base_words if word]
    return list(set(base_words))

def generate_targeted_wordlist():
    base_words = gather_target_info()
    try:
        min_len = int(input(f"{Fore.CYAN}[?]{Style.RESET_ALL} Enter minimum length: ").strip())
        max_len = int(input(f"{Fore.CYAN}[?]{Style.RESET_ALL} Enter maximum length: ").strip())
    except ValueError:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid length input.")
        sys.exit(1)
    print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Generating targeted wordlist...")
    count = 0
    with open(output_file, "w") as f:
        for word in base_words:
            if min_len <= len(word) <= max_len:
                f.write(word + "\n")
                count += 1
            for word2 in base_words:
                combo = word + word2
                if min_len <= len(combo) <= max_len:
                    f.write(combo + "\n")
                    count += 1
                combo_rev = word2 + word
                if min_len <= len(combo_rev) <= max_len:
                    f.write(combo_rev + "\n")
                    count += 1
        print(f"\n{Fore.CYAN}[INFO]{Style.RESET_ALL} Targeted wordlist generation complete. Total {count} entries saved to '{output_file}'.")

def main():
    choice = menu()
    if choice == "1":
        generate_targeted_wordlist()
    elif choice == "0":
        print(f"{Fore.RED}[INFO] Exiting...{Style.RESET_ALL}")
        sys.exit(0)
    else:
        print(f"{Fore.RED}[ERROR] Invalid choice.{Style.RESET_ALL}")
        main()

if __name__ == "__main__":
    main()
