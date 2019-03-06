import os
from ...Core import core


class TextEngine:
    def __init__(self, folder):
        self.__folder = folder     
        self.__generator = None
        self.__core = core.Core(self.__folder)


    def run(self):
        self.__get_list()
        choice = str(input("Enter your choice : ")).upper()
        self.set_generator(choice)
        print(self.__core.get_random_name())
        print(self.__core.get_random_name())
        print(self.__core.get_random_name())
        print(self.__core.get_random_name())
        print(self.__core.get_random_name())

    def __get_list(self):
        files = self.__core.get_display_source()
        i = 1

        for f in files:
            print("{id}. {file}".format(id=i, file=f))    
            i += 1


    def set_generator(self, choice):
        files = self.__core.get_display_source()
        self.__core.set_generator(files[int(choice)-1])