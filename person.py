import generate
import datetime


class Person():
    def __init__(self):
        pass


    def gen_pass(self, data):
        birthday = {}
        pass_list = []
        fname = []
        lname = []
        mname = []
        nickname = []
        company = []
        pet = []
        if len(data['birthday']) > 0:
            birthday['day'], birthday['mon'], birthday['year'] = data['birthday'].split('.')        
        print("\n[+] Please wait password generation...\n")
        
         # Generating first name passwords
        if len(data['firstname']) > 0:      
            print("\n[+] Generating first name passwords...\n")
            fname = generate.Passwords().names(data['firstname'])
            pass_list.extend(fname)
            pass_list.extend(generate.Passwords().digits(fname))
            if len(birthday) > 0 :
                pass_list.extend(self.join_birthday(fname, birthday))
                
            
        
        # Generating last name passwords
        if len(data['lastname']) > 0:
            print("\n[+] Generating last name passwords...\n")
            lname = generate.Passwords().names(data['lastname'])
            pass_list.extend(lname)
            pass_list.extend(generate.Passwords().digits(lname))
            if len(birthday) > 0 :
                pass_list.extend(self.join_birthday(lname, birthday))
            
            
        
        # Generating middle name passwords
        if len(data['middlename']) > 0:
            print("\n[+] Generating middle name passwords...\n")
            mname = generate.Passwords().names(data['middlename'])
            pass_list.extend(mname)
            pass_list.extend(generate.Passwords().digits(mname))
            if len(birthday) > 0 :
                pass_list.extend(self.join_birthday(mname, birthday))
            
        
        # Generating nick name passwords
        if len(data['nickname']) > 0:
            print("\n[+] Generating nick name passwords...\n")
            nickname = generate.Passwords().names(data['nickname'])
            pass_list.extend(nickname)
            pass_list.extend(generate.Passwords().digits(nickname))
            if len(birthday) > 0 :
                pass_list.extend(self.join_birthday(nickname, birthday))
            
            
        
        # Generating company passwords
        if len(data['company']) > 0:
            print("\n[+] Generating company passwords...\n")
            company = generate.Passwords().names(data['company'])
            pass_list.extend(company)
            pass_list.extend(generate.Passwords().digits(company))
            if len(birthday) > 0 :
                pass_list.extend(self.join_birthday(company, birthday))
            
            
        
        # Generating pet passwords
        if len(data['pet']) > 0:
            print("\n[+] Generating pet passwords...\n")
            pet = generate.Passwords().names(data['pet'])
            pass_list.extend(pet)
            pass_list.extend(generate.Passwords().digits(pet))
            if len(birthday) > 0 :
                pass_list.extend(self.join_birthday(pet, birthday))
            

        # replace chars
        print("\n[+] Generating replace chars...\n")
        pass_list.extend(generate.Passwords().replace_chars(pass_list))

        # join names
        if len(fname) > 0 and len(lname) > 0:
            print("\n[+] Generating join names...\n")
            pass_list.extend(self.join_names(fname, lname))
            if len(birthday) > 0 :
                pass_list.extend(self.names_join_birthday(fname, lname, birthday))
        if len(data['firstname']) > 0 and len(data['lastname']) > 0 and len(data['middlename']) > 0 and len(birthday) > 0:
            pass_list.extend(self.initials(data['firstname'], data['lastname'], data['middlename'], birthday))
        return list(set(pass_list))
            
    
    def isdate(self, date):
        try:            
            datetime.datetime.strptime(date, '%d.%m.%Y')        
            return True
        except ValueError:
            return False


    def names_join_birthday(self, firstName, lastName, birthday):
        pass_list = []
        for pwdFirst in firstName:
            for pwdLast in lastName:
                pass_list.append('{}{}{}'.format(pwdFirst, birthday['year'], pwdLast))          
                pass_list.append('{}{}{}'.format(pwdLast, birthday['year'], pwdFirst))              
                pass_list.append('{}{}{}{}'.format(pwdFirst, birthday['day'], birthday['mon'], pwdLast))          
                pass_list.append('{}{}{}{}'.format(pwdLast, birthday['day'], birthday['mon'], pwdFirst))                           
                pass_list.append('{}{}{}{}'.format(pwdFirst, birthday['mon'], birthday['day'], pwdLast))          
                pass_list.append('{}{}{}{}'.format(pwdLast, birthday['mon'], birthday['day'], pwdFirst))          
        return pass_list


    def join_names(self, firstName, lastName):
        pass_list = []
        for pwdFirst in firstName:
            for pwdLast in lastName:
                pass_list.append('{}{}'.format(pwdFirst, pwdLast))
                pass_list.append('{}{}'.format(pwdLast, pwdFirst))
                pass_list.append('{}{}{}'.format(pwdFirst, pwdLast, pwdFirst))
                pass_list.append('{}{}{}'.format(pwdLast, pwdFirst, pwdLast))
        return pass_list


    def join_birthday(self, list_pass, birthday):
        pass_list = []        
        if len(list_pass) > 0 and len(birthday) > 0:            
            for pwd in list_pass:                
                pass_list.append('{}{}'.format(birthday['day'], pwd))                
                pass_list.append('{}{}'.format(pwd, birthday['day']))                           
                pass_list.append('{}{}'.format(birthday['mon'], pwd))                
                pass_list.append('{}{}'.format(pwd, birthday['mon']))                            
                pass_list.append('{}{}'.format(birthday['year'], pwd))                
                pass_list.append('{}{}'.format(pwd, birthday['year']))                           
                pass_list.append('{}{}'.format(birthday['year'][-2:], pwd))                
                pass_list.append('{}{}'.format(pwd, birthday['year'][-2:]))                               
                pass_list.append('{}{}{}{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))
                pass_list.append('{}.{}.{}{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))
                pass_list.append('{}-{}-{}{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))
                pass_list.append('{}_{}_{}{}'.format(birthday['day'], birthday['mon'], birthday['year'], pwd))                           
                pass_list.append('{}{}{}{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
                pass_list.append('{}{}.{}.{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
                pass_list.append('{}{}-{}-{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))
                pass_list.append('{}{}_{}_{}'.format(pwd, birthday['day'], birthday['mon'], birthday['year']))                  
        return pass_list


    def initials(self, firstName, lastName, middleName, birthday):
        pass_list = []
        pwd = []
        
        pwd.append('{}{}{}'.format(firstName[0], lastName[0], middleName))
        pwd.append('{}{}{}'.format(firstName[0], middleName[0], lastName))    
             
        pwd.append('{}{}{}'.format(lastName[0], firstName[0], middleName))
        pwd.append('{}{}{}'.format(lastName[0], middleName[0], firstName))        
        
        pwd.append('{}{}{}'.format(middleName[0], firstName[0], lastName))
        pwd.append('{}{}{}'.format(middleName[0], lastName[0], firstName))        

        pass_list.extend(pwd)
        for p in pwd:
            pass_list.extend(generate.Passwords().names(p))
        pass_list.extend(self.join_birthday(pass_list, birthday))
        pass_list.extend(generate.Passwords().replace_chars(pass_list))
        return pass_list  
