import json
import os
import secrets
from colorama import Fore, Style, init


init(autoreset=True)


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def generate_password(length: int):
    chars = "abcdefghijklmnopqrstuvwxyz" \
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
            "0123456789" \
            "!/#$%&()?@~+-"

    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password


def get_passwords():
    with open('data.json', 'rb') as f:
        passwords = json.load(f)
    return passwords


def add_account(service, login, password):
    new_account = {"login": login, "password": password}

    if os.path.exists('data.json'):
        with open('data.json', 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    else:
        existing_data = {}

    if service in existing_data:
        if new_account not in existing_data[service]:
            existing_data[service].append(new_account)
    else:
        existing_data[service] = [new_account]

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, indent=4, ensure_ascii=False)
    print(' ')
    print(f'{Fore.RED}Added new account:{Style.RESET_ALL}\n{Fore.YELLOW}Service:{Style.RESET_ALL} {service}\n{Fore.YELLOW}Login:{Style.RESET_ALL} {login}\n{Fore.YELLOW}Password:{Style.RESET_ALL} {password}')


def edit_password(password, service, index_acc):
    if os.path.exists('data.json'):
        with open('data.json', 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    
    if service in existing_data:
        existing_data[service][index_acc]['password'] = password

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, indent=4, ensure_ascii=False)
    print(' ')
    print(f'{Fore.RED}Edited account:{Style.RESET_ALL}\n{Fore.YELLOW}Service:{Style.RESET_ALL} {service}\n{Fore.YELLOW}Login:{Style.RESET_ALL} {existing_data[service][index_acc]['login']}\n{Fore.YELLOW}Password:{Style.RESET_ALL} {password}')

while True:
    print(Fore.RED + """██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝

███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
""" + Style.RESET_ALL)
    print(f"""   {Fore.YELLOW}[1]{Style.RESET_ALL} Add new account
   {Fore.YELLOW}[2]{Style.RESET_ALL} See accounts
   {Fore.YELLOW}[3]{Style.RESET_ALL} Edit account password
          """)
    try:
        value = int(input("Enter a number what you need: "))
    except ValueError:
        print("Enter a number")
        continue
    if value == 1:
        service = input("Enter the name of service: ")
        login = input("Enter Login: ")
        password = input("Enter password: ")
        add_account(service, login, password)
        print(' ')
        input("Press enter to continue...")
        cls()
    elif value == 2:
        passwords = get_passwords()  
        services = list(passwords.keys())  
        
        for index, service in enumerate(services):
            print(f"[{index}] {service}")

        b = int(input("Enter the service account for which password you want to see: "))
        if 0 <= b < len(services):
            selected_service = services[b]
            print(' ')
            print(f'{Fore.RED}{selected_service}: {Style.RESET_ALL}')
            for index, account in enumerate(passwords[selected_service]):
                print(f'{Fore.YELLOW}[{index}]{Style.RESET_ALL} Login: {account['login']}')
            print(' ')
            index_acc = int(input("Enter the account what password you need: "))
            print(' ')
            print(f"Login: {passwords[selected_service][index_acc]['login']}\nPassword: {passwords[selected_service][index_acc]['password']}")
        print(' ')
        input("Press enter to continue...")
        cls()
    elif value == 3:
        passwords = get_passwords()
        services = list(passwords.keys())
     
        for index, service in enumerate(services):
            print(f"[{index}] {service}")
        
        b = int(input("Enter the service account for which you want to change the password: "))
        if 0 <= b < len(services):
            selected_service = services[b]
            print(selected_service)
            for index, account in enumerate(passwords[selected_service]):
                print(f'[{index}] Login: {account['login']}')
            index_acc = int(input("Enter the account index whose password you want to change:"))
            password = input("Enter your password or type 1 to generate it: ")
            try:
                if int(password) == 1:
                    length = int(input("Enter password length your need: "))
                    password = generate_password(length)
            except:
                pass
            edit_password(password=password, service=selected_service, index_acc=index_acc)
            print(' ')
            input("Press enter to continue...")
            cls()
