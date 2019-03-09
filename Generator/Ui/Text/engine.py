import os
from ...Core import core


class TextEngine:
    def __init__(self, folder):
        self.__folder = folder     
        self.__generator = None
        self.__core = core.Core(self.__folder)

    def run(self):
        self.__get_list_armies()
        choice = str(input("Enter your choice : ")).upper()
        self.set_generator(choice)
        print(self.__core.get_random_name())
        print(self.__core.get_random_name())
        print(self.__core.get_random_name())
        print(self.__core.get_random_name())
        print(self.__core.get_random_name())

        self.__get_list_rules()
        choice = str(input("Enter your choice : ")).upper()
        self.set_rule(choice)
        
    def __get_list_rules(self):
        files = self.__core.get_rules()
        i = 1

        for f in files:
            print("{id}. {file}".format(id=i, file=f))    
            i += 1

    def __get_list_armies(self):
        files = self.__core.get_armies()
        i = 1

        for f in files:
            print("{id}. {file}".format(id=i, file=f))    
            i += 1

    def set_generator(self, choice):
        files = self.__core.get_armies()
        self.__core.set_generator(files[int(choice)-1])

    def set_rule(self, choice):
        files = self.__core.get_rules()
        self.__core.set_rule(files[int(choice)-1])
