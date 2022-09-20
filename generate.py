EOF = -1

CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '<', '>', '?']

class Passwords:
    def __init__(self):
        pass   
    
    
    def all_index(self, string, ch):
        length = len(string)
        indexs = []
        for index in range(length):
            if string.startswith(ch, index):
                indexs.append(index)
        return indexs


    def names(self, name):
        pwd_names = []
        pass_list = []        
        pwd_names.append(name.lower())        
        
        for i in range(len(name)):
            w = ""
            for j in range(len(name)):
                if i == j:
                    w += name[j].upper()
                else:
                    w += name[j]
            pwd_names.append(w)
        
        for i in range(len(name)):
            w = ""
            for j in range(len(name)):
                if j <= i:
                    w += name[j].upper()
                else:
                    w += name[j]
            pwd_names.append(w)

        for i in range(len(name)):
            w = ""
            for j in range(len(name)):
                if i <= j:
                    w += name[j].upper()
                else:
                    w += name[j]
            pwd_names.append(w)
            
        w = ""
        for i in range(len(name)):
            if i == 0 or i == len(name) - 1:
                w += name[i].upper()
            else:
                w += name[i]
        pwd_names.append(w)

        if len(name) > 3:
            w = ""
            for i in range(len(name)):
                if (i + 1) % 2 == 0:
                    w += name[i].upper()
                else:
                    w += name[i]
            pwd_names.append(w)
                    
        for pwd in pwd_names:
            pass_list.append(pwd)
            pass_list.append(pwd[::-1])
        pass_list.extend(self.chars(pass_list))
        
        return list(set(pass_list))


    def digits(self, listPass):
        pass_list = []
        for pwd in listPass:            
            for p in range(0, 10):
                num = ""
                for n in range(p, 9):
                    num += str(n)
                    pass_list.append('{}{}'.format(num, pwd))
                    pass_list.append('{}{}'.format(pwd, num))                    
                    pass_list.append('{}{}{}'.format(num, pwd, num))
                    
            for p in range(0, 10):
                num = str(p)
                for _ in range(0, 9):
                    num += str(p)
                    pass_list.append('{}{}'.format(num, pwd))
                    pass_list.append('{}{}'.format(pwd, num))                    
                    pass_list.append('{}{}{}'.format(num, pwd, num))
                    
            num = "9"
            for n in range(8, -1, -1):
                num += str(n)
                pass_list.append('{}{}'.format(num, pwd))
                pass_list.append('{}{}'.format(pwd, num))                        
        return list(set(pass_list))


    def chars(self, listPass):
        pass_list = []
        for pwd in listPass:            
            for ch in CHARS:
                pass_list.append('{}{}'.format(pwd, ch))
                pass_list.append('{}{}'.format(ch, pwd))
                pass_list.append('{}{}{}'.format(ch, pwd, ch))
        return list(set(pass_list))

            
    def replace_chars(self, listPass):
        pass_list = []        
        for pwd in listPass:        
            for index in self.all_index(pwd, 's'):
                pass_list.append("{}{}{}".format(pwd[:index], '$', pwd[index + 1:]))
            if pwd.find('s') != EOF:
                pass_list.append(pwd.replace('s', '$'))
            for index in self.all_index(pwd, 'S'):
                pass_list.append("{}{}{}".format(pwd[:index], '$', pwd[index + 1:]))
            for index in self.all_index(pwd, 's'):
                pass_list.append("{}{}{}".format(pwd[:index], '5', pwd[index + 1:]))
            if pwd.find('s') != EOF:
                pass_list.append(pwd.replace('s', '5'))
            for index in self.all_index(pwd, 'S'):
                pass_list.append("{}{}{}".format(pwd[:index], '5', pwd[index + 1:]))
            if pwd.find('S') != EOF:
                pass_list.append(pwd.replace('S', '5'))
            for index in self.all_index(pwd, 'o'):
                pass_list.append("{}{}{}".format(pwd[:index], '0', pwd[index + 1:]))
            if pwd.find('o') != EOF:
                pass_list.append(pwd.replace('o', '!'))
            for index in self.all_index(pwd, 'O'):
                pass_list.append("{}{}{}".format(pwd[:index], '0', pwd[index + 1:]))
            if pwd.find('O') != EOF:
                pass_list.append(pwd.replace('O', '!'))
            for index in self.all_index(pwd, 'a'):
                pass_list.append("{}{}{}".format(pwd[:index], '@', pwd[index + 1:]))
            if pwd.find('a') != EOF:
                pass_list.append(pwd.replace('a', '@'))
            for index in self.all_index(pwd, 'A'):
                pass_list.append("{}{}{}".format(pwd[:index], '@', pwd[index + 1:]))
            if pwd.find('A') != EOF:
                pass_list.append(pwd.replace('A', '@'))
            for index in self.all_index(pwd, 'i'):
                pass_list.append("{}{}{}".format(pwd[:index], '!', pwd[index + 1:]))
            if pwd.find('i') != EOF:
                pass_list.append(pwd.replace('i', '!'))
            for index in self.all_index(pwd, 'I'):
                pass_list.append("{}{}{}".format(pwd[:index], '!', pwd[index + 1:]))
            if pwd.find('I') != EOF:
                pass_list.append(pwd.replace('I', '!'))
            for index in self.all_index(pwd, '1'):
                pass_list.append("{}{}{}".format(pwd[:index], '!', pwd[index + 1:]))
            if pwd.find('1') != EOF:
                pass_list.append(pwd.replace('1', '!'))
        return list(set(pass_list))
