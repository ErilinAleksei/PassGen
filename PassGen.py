#!/bin/python

EOF = -1

DEFAULT_NAME_FILE = 'passwords.dic'

def banner():
    banner = """\n\n                 _____               _____            
                |  __ \             / ____|           
                | |__) |_ _ ___ ___| |  __  ___ _ __  
                |  ___/ _` / __/ __| | |_ |/ _ \ '_ \ 
                | |  | (_| \__ \__ \ |__| |  __/ | | |
                |_|   \__,_|___/___/\_____|\___|_| |_|\n\n"""
    print(banner)


 
 
def passJoinNumber(listPass):
    passList = []    
    for pwd in listPass:
        num = ""
        for n in range(0, 10):
            num += str(n)
            passList.append('{}{}'.format(num, pwd))
            passList.append('{}{}'.format(pwd, num))
            passList.append('{}-{}'.format(num, pwd))
            passList.append('{}-{}'.format(pwd, num))
            passList.append('{}_{}'.format(num, pwd))
            passList.append('{}_{}'.format(pwd, num))
            passList.append('{}{}{}'.format(num, pwd, num))
            passList.append('{}-{}-{}'.format(num, pwd, num))
            passList.append('{}_{}_{}'.format(num, pwd, num))
        num = ""
        for n in range(1, 10):
            num += str(n)
            passList.append('{}{}'.format(num, pwd))
            passList.append('{}{}'.format(pwd, num))
            passList.append('{}-{}'.format(num, pwd))
            passList.append('{}-{}'.format(pwd, num))
            passList.append('{}_{}'.format(num, pwd))
            passList.append('{}_{}'.format(pwd, num))
            passList.append('{}{}{}'.format(num, pwd, num))
            passList.append('{}-{}-{}'.format(num, pwd, num))
            passList.append('{}_{}_{}'.format(num, pwd, num))
        num = ""
        for n in range(9, -1, -1):
            num += str(n)
            passList.append('{}{}'.format(num, pwd))
            passList.append('{}{}'.format(pwd, num))
            passList.append('{}-{}'.format(num, pwd))
            passList.append('{}-{}'.format(pwd, num))
            passList.append('{}_{}'.format(num, pwd))
            passList.append('{}_{}'.format(pwd, num))
            passList.append('{}{}{}'.format(num, pwd, num))
            passList.append('{}-{}-{}'.format(num, pwd, num))
            passList.append('{}_{}_{}'.format(num, pwd, num))
        
    return passList
    

def passJoinBirthday(listPass, birthday):
    passList = []
    if len(listPass) > 0 and len(birthday) > 0:
        for pwd in listPass:
            passList.append('{}{}'.format(birthday['year'], pwd))
            passList.append('{}-{}'.format(birthday['year'], pwd))
            passList.append('{}_{}'.format(birthday['year'], pwd))
            passList.append('{}{}'.format(pwd, birthday['year']))
            passList.append('{}-{}'.format(pwd, birthday['year']))
            passList.append('{}_{}'.format(pwd, birthday['year']))
            if birthday['year'].find('1') != EOF:
                passList.append('{}{}'.format(birthday['year'].replace('1', '!'), pwd))
                passList.append('{}-{}'.format(birthday['year'].replace('1', '!'), pwd))
                passList.append('{}_{}'.format(birthday['year'].replace('1', '!'), pwd))
                passList.append('{}{}'.format(pwd, birthday['year'].replace('1', '!')))
                passList.append('{}-{}'.format(pwd, birthday['year'].replace('1', '!')))
                passList.append('{}_{}'.format(pwd, birthday['year'].replace('1', '!')))
            passList.append('{}{}{}{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))
            passList.append('{}.{}.{}{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))
            passList.append('{}-{}-{}{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))
            passList.append('{}_{}_{}{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))
            passList.append('{}{}{}-{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))
            passList.append('{}{}{}_{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))
            passList.append('{}.{}.{}-{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))
            passList.append('{}.{}.{}_{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))
            passList.append('{}-{}-{}-{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))
            passList.append('{}_{}_{}_{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))            
            passList.append('{}{}{}{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
            passList.append('{}{}.{}.{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
            passList.append('{}{}-{}-{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
            passList.append('{}{}_{}_{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
            passList.append('{}-{}{}{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
            passList.append('{}_{}{}{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
            passList.append('{}-{}.{}.{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
            passList.append('{}_{}.{}.{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
            passList.append('{}-{}-{}-{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
            passList.append('{}_{}_{}_{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
    return passList
    
    
def passJoinNames(firstName, lastName):
    passList = []
    for pwdFirst in firstName:
        for pwdLast in lastName:
            passList.append('{}{}'.format(pwdFirst, pwdLast))
            passList.append('{}{}'.format(pwdLast, pwdFirst))
            passList.append('{}-{}'.format(pwdFirst, pwdLast))
            passList.append('{}-{}'.format(pwdLast, pwdFirst))
            passList.append('{}_{}'.format(pwdFirst, pwdLast))
            passList.append('{}_{}'.format(pwdLast, pwdFirst))
    return passList
  
def passJoinNamesBirthday(firstName, lastName, birthday):
    passList = []
    for pwdFirst in firstName:
        for pwdLast in lastName:
            passList.append('{}{}{}'.format(pwdFirst, birthday['year'], pwdLast))           
            passList.append('{}_{}_{}'.format(pwdFirst, birthday['year'], pwdLast))           
            passList.append('{}-{}-{}'.format(pwdFirst, birthday['year'], pwdLast))
            passList.append('{}{}{}'.format(pwdLast, birthday['year'], pwdFirst))           
            passList.append('{}_{}_{}'.format(pwdLast, birthday['year'], pwdFirst))           
            passList.append('{}-{}-{}'.format(pwdLast, birthday['year'], pwdFirst))
            passList.append('{}{}{}{}'.format(pwdFirst, birthday['day'], birthday['mon'], pwdLast))           
            passList.append('{}_{}{}_{}'.format(pwdFirst, birthday['day'], birthday['mon'], pwdLast))           
            passList.append('{}-{}{}-{}'.format(pwdFirst, birthday['day'], birthday['mon'], pwdLast))
            passList.append('{}{}{}{}'.format(pwdLast, birthday['day'], birthday['mon'], pwdFirst))           
            passList.append('{}_{}{}_{}'.format(pwdLast, birthday['day'], birthday['mon'], pwdFirst))           
            passList.append('{}-{}{}-{}'.format(pwdLast, birthday['day'], birthday['mon'], pwdFirst))            
            passList.append('{}{}{}{}'.format(pwdFirst, birthday['mon'], birthday['day'], pwdLast))           
            passList.append('{}_{}{}_{}'.format(pwdFirst, birthday['mon'], birthday['day'], pwdLast))           
            passList.append('{}-{}{}-{}'.format(pwdFirst, birthday['mon'], birthday['day'], pwdLast))
            passList.append('{}{}{}{}'.format(pwdLast, birthday['mon'], birthday['day'], pwdFirst))           
            passList.append('{}_{}{}_{}'.format(pwdLast, birthday['mon'], birthday['day'], pwdFirst))           
            passList.append('{}-{}{}-{}'.format(pwdLast, birthday['mon'], birthday['day'], pwdFirst))
    return passList
    
    
def passNames(names):    
    pwdNames = []   
    passList = []
    pwdNames.append(names)
    pwdNames.append(names.title())   
    pwdNames.append(names[::-1].title()[::-1])      
    pwdNames.append(names.upper())
    pwdNames.append(names[::-1])  
    pwdNames.append(names[::-1].title())          
    pwdNames.append(names[::-1].upper())  
    for pwd in pwdNames:        
        passList.append(pwd)               
        if pwd.find('s') != EOF:
            passList.append(pwd.replace('s', '$'))
        if pwd.find('S') != EOF:
            passList.append(pwd.replace('S', '$'))
        if pwd.find('a') != EOF:
            passList.append(pwd.replace('a', '@'))
        if pwd.find('A') != EOF:
            passList.append(pwd.replace('A', '@'))
        if pwd.find('i') != EOF:
            passList.append(pwd.replace('i', '!'))
        if pwd.find('I') != EOF:
            passList.append(pwd.replace('I', '!'))          
    return passList
    
    
def passSaveFile(fileName, passList):
    try:
        print("Sorted...!\n")
        passList.sort()  
        totalPass = len(passList)
        countWritePass = 0
        with open(fileName, 'wt') as f:        
            for pwd in passList:
                f.write('{}\n'.format(pwd))
                countWritePass += 1
                print('Write to file...!\t{}/{}\n'.format(countWritePass, totalPass))                
        return True
    except:
        return False
    

def isDate(date):
    d, m, y = date.split('.')
    if int(d) <= 31 and int(d) >= 1 and int(m) <= 12 and int(m) >= 1 and len(y) == 4:
        return True
    return False


def main():
    try:
        data = {}    
        birthday = {}
        passList = []
        nickname = []
        fname = []
        lname = []
        jName = []  
        banner()
        data['firstname'] = str(input("Input first Name: ")).lower()
        data['lastname'] = str(input("Input last Name: ")).lower()
        data['nickname'] = str(input("Input nick Name: ")).lower()
        data['birthday'] = str(input("Input birthday(dd.mm.yyyy): ")).lower()
        if len(data['firstname']) == 0 and len(data['lastname']) == 0 and len(data['nickname']) == 0 and len(data['birthday']) == 0:
            print('Passwords not generated!')
            exit(0)
        if len(data['birthday']) > 0:
            if isDate(data['birthday']) == False:
                print('Invalid birthday')
                exit()
            else:
                birthday['day'], birthday['mon'], birthday['year'] = data['birthday'].split('.')
        print("Generating passwords...!\n")
        
        # Generating first name passwords
        if len(data['firstname']) > 0:
            fname = passNames(data['firstname'])
            for p in fname:
                passList.append(p)
            for p in passJoinBirthday(fname, birthday):
                passList.append(p)
            for p in passJoinNumber(fname):
                passList.append(p)
        
        # Generating last name passwords
        if len(data['lastname']) > 0:
            lname = passNames(data['lastname'])
            for p in lname:
                passList.append(p)
            for p in passJoinBirthday(lname, birthday):
                passList.append(p) 
            for p in passJoinNumber(lname):
                passList.append(p)
        
        # Generating nick name passwords
        if len(data['nickname']) > 0:
            nickname = passNames(data['nickname'])
            for p in nickname:
                passList.append(p)  
            for p in passJoinBirthday(nickname, birthday):
                passList.append(p)
            for p in passJoinNumber(nickname):
                passList.append(p)
            
        # Generating joins passwords
        if len(fname) > 0 and len(lname) > 0 and len(birthday) > 0:
            jName = passJoinNames(fname, lname) 
            for p in jName:
                passList.append(p)
            for p in passJoinBirthday(jName, birthday):
                passList.append(p)
            for p in passJoinNumber(jName):
                passList.append(p)
            for p in passJoinNamesBirthday(fname, lname, birthday):
                passList.append(p)
        passSaveFile(DEFAULT_NAME_FILE, passList)
    except:
        exit(0)


if __name__ == '__main__':
    main()