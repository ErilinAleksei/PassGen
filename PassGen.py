import generate
import person

import sys
import os
import os.path

DEFAULT_NAME_FILE = 'passwords.dic'


def banner():
    banner = """\n\n                 _____               _____            
                |  __ \             / ____|           
                | |__) |_ _ ___ ___| |  __  ___ _ __  
                |  ___/ _` / __/ __| | |_ |/ _ \ '_ \ 
                | |  | (_| \__ \__ \ |__| |  __/ | | |
                |_|   \__,_|___/___/\_____|\___|_| |_|\n\n"""
    print(banner)
    

def sort_len(e):
    return len(e)


def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def pass_save_file(filename, list_pass):
    try:
        print("[+] Sorted...!\n")        
        list_pass.sort(key=sort_len)       
        with open(filename, 'wt') as f:         
            print("[+] Count passwords => {}\n".format(len(list_pass)))
            print("[+] Write to file...\n")
            for pwd in list_pass:
                f.write('{}\n'.format(pwd))                              
        return True
    except:
        return False


def menu_person():
    data = {}       
    data['firstname'] = str(input("Input Name: ")).lower()
    data['lastname'] = str(input("Input Surname: ")).lower()
    data['middlename'] = str(input("Input middle name: ")).lower()        
    data['nickname'] = str(input("Input nick Name: ")).lower()
    data['birthday'] = str(input("Input birthday(dd.mm.yyyy): ")).lower()
    data['company'] = str(input("Input company: ")).lower()
    data['pet'] = str(input("Input pet: ")).lower()    
    if len(data['firstname']) == 0 and len(data['lastname']) == 0 and len(data['middlename']) == 0 and len(data['nickname']) == 0 and len(data['birthday']) == 0 and len(data['company']) == 0 and len(data['pet']) == 0:
        print('[-] Passwords not generated!\n')
        return   
    if len(data['birthday']) > 0:        
        if person.Person().isdate(data['birthday']) == False:            
            print('[-] Invalid birthday\n')
            return
    passwd = person.Person().gen_pass(data)
    pass_save_file('{}.dic'.format(data['firstname']), passwd)
        
    
    
    


def menu_gen_pass():
    clear()
    passwd_list = []
    while True:
        print("0) Exit")            
        print("1) Generate passowrd form files")
        print("2) Generate passowrd from single word")
        value = int(input("> "))
        if value == 1:
            filename = str(input("Input file name: "))
            if os.path.isfile(filename):
                print("\n[+] Please wait password generation...\n")
                with open(filename, "r") as f:
                    for line in f: 
                        passwd_list.extend(generate.Passwords().names(line.strip()))
                        passwd_list.extend(generate.Passwords().digits(passwd_list))
                        passwd_list.extend(generate.Passwords().replace_chars(passwd_list))
                    pass_save_file(DEFAULT_NAME_FILE, list(set(passwd_list)))
            else:
                print("[-] File not found: {}".format(filename))
        elif value == 2:
            word = str(input("Input word: ")).lower()
            if len(word) > 0:
                print("\n[+] Please wait password generation...\n")
                passwd_list.extend(generate.Passwords().names(word))
                passwd_list.extend(generate.Passwords().digits(passwd_list))
                passwd_list.extend(generate.Passwords().replace_chars(passwd_list))
                pass_save_file(DEFAULT_NAME_FILE, list(set(passwd_list)))
        elif value == 0:
            return   
 

def menu_main():   
    while True:
        try:
            value = 0            
            print("0) Exit")
            print("1) Generate passowrd base person")
            print("2) Generate passowrd\n")
            value = int(input("> "))                     
            if value == 1:
                menu_person()
            elif value == 2:
                menu_gen_pass()          
            elif value == 0:                
                return None
            else:
                pass
        except KeyboardInterrupt:
            exit(0)

    
def main():
    banner()
    menu_main()

    
if __name__ == '__main__':
    main()
