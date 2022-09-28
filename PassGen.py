import generate
import person

import sys
import getopt
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
        
def help():
    print("OPTIONS:");
    print("\t--person\tGenerate passowrd base person");
    print("\t--pass-file=\tGenerate passowrd form file");
    print("\t--pass-word=\tGenerate passowrd from single word");
    print("\t-h\tUsing help");
    print("EXAMPLES:");
    print("\tpassgen.py --person");
    print("\tpassgen.py --pass-word=password");
    print("\tpassgen.py --pass-file=dict.txt");
    
    
def gen_pass_person():
    clear()
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
    
    
def gen_pass_from_file(filename):
    clear()
    passwd_list = []
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

        
def gen_pass_word(word):
    clear()
    passwd_list = []
    if len(word) > 0:
        print("\n[+] Please wait password generation...\n")
        passwd_list.extend(generate.Passwords().names(word))
        passwd_list.extend(generate.Passwords().digits(passwd_list))
        passwd_list.extend(generate.Passwords().replace_chars(passwd_list))
        pass_save_file(DEFAULT_NAME_FILE, list(set(passwd_list)))
    else:
        print("Word not found")
        
        
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["person", "pass-file=", "pass-word="])
        for opt, arg in opts:
            if opt == "--person":                
                banner()
                gen_pass_person()
                return 0
            elif opt == "--pass-file":               
                banner()
                gen_pass_from_file(arg)
                return 0
            elif opt == "--pass-word":                
                banner()
                gen_pass_word(arg)
                return 0
            elif opt == "-h":
                help()
    except getopt.GetoptError as err:
        print(err)
    except KeyboardInterrupt:
        return
    return None

    
if __name__ == '__main__':
    main()
