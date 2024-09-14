import os
import fade

ascii_art =  """  

  ██████   ██████ █████  █████ █████       ███████████ █████    ███████████    ███████       ███████    █████      
   ░░██████ ██████ ░░███  ░░███ ░░███       ░█░░░███░░░█░░███    ░█░░░███░░░█  ███░░░░░███   ███░░░░░███ ░░███       
    ░███░█████░███  ░███   ░███  ░███       ░   ░███  ░  ░███    ░   ░███  ░  ███     ░░███ ███     ░░███ ░███       
    ░███░░███ ░███  ░███   ░███  ░███           ░███     ░███        ░███    ░███      ░███░███      ░███ ░███       
    ░███ ░░░  ░███  ░███   ░███  ░███           ░███     ░███        ░███    ░███      ░███░███      ░███ ░███       
    ░███      ░███  ░███   ░███  ░███      █    ░███     ░███        ░███    ░░███     ███ ░░███     ███  ░███      █
    █████     █████ ░░████████   ███████████    █████    █████       █████    ░░░███████░   ░░░███████░   ███████████
   ░░░░░     ░░░░░   ░░░░░░░░   ░░░░░░░░░░░    ░░░░░    ░░░░░       ░░░░░       ░░░░░░░       ░░░░░░░    ░░░░░░░░░░░ 
                                                                                                                     
                                                                                                                     
                                                                                                                       """
ascii_art = fade.purpleblue(ascii_art)

menu = """          [01] --> Ip Pinger 
          [02] --> Ddos Tools 
          [03] --> Nitro Generator
          [04] --> Ip Info
          [05] ->  Obfuscator     """

menu = fade.purpleblue(menu)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(ascii_art)
    print()
    print(menu)
    choice = input("""┌──(User@MULTI TOOL)-[~Menu]│
└─$>""")
    
    if choice == "1":
        os.system("python program/ippinger.py")
    elif choice == "2":
        os.system("python program/ddos.py")
    elif choice == '3':
        os.system("python program/nitrogen.py")
    elif choice == '4':
        os.system("python program/ipinfo.py")
    elif choice == '5':
        os.system("python program/obfuscator.py")
    else:
        print('Mauvais choix...')
        os.system('cls' if os.name == 'nt' else 'clear')
        main()  # Relance le menu après une erreur

if __name__ == "__main__":
    main()
