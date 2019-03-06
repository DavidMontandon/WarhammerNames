import os
from . import names as NG

class Core:
    def __init__(self, source_path):
        self.__version = "0.0.1"
        self.__source_path = source_path
        self.__generator = None 

    def get_display_source(self):
        files = os.listdir(self.__source_path)
        return files 

    def set_generator(self, file_name):
        self.__generator = NG.NameGenerator(self.__source_path, file_name)

    def get_random_name(self):
        return self.__generator.generate_name()

    