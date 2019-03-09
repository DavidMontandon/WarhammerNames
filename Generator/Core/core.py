import os
from . import names as NG
from . import rules as RM

class Core:
    def __init__(self, source_path):
        self.__version = "0.0.1"
        self.__source_path = source_path
        self.__source_army_path = os.path.join(self.__source_path, "Armies")
        self.__source_rule_path = os.path.join(self.__source_path, "Rules")
        self.__generator = None 
        self.__rule = None

    def get_armies(self):
        files = os.listdir(self.__source_army_path)
        return files 

    def get_rules(self):
        files = os.listdir(self.__source_rule_path)
        return files 

    def set_generator(self, file_name):
        self.__generator = NG.NameGenerator(self.__source_army_path, file_name)

    def set_rule(self, file_name):
        self.__rule = RM.Rule(os.path.join(self.__source_rule_path, file_name))

    def get_random_name(self):
        if(self.__generator == None):
            return "<Please set an army generator first>"

        return self.__generator.generate_name()

    