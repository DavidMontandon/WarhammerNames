import os
import random
import xml.etree.ElementTree as ET

class NameGenerator:
    def __init__(self, path, source, file):
        self.__version = "0.0.1"
        self.__path = path 
        self.__source_path = self.__get_full_file_path(path, source)
        self.__file = file 
        self.__prefixes = [] 
        self.__suffixes = [] 
        self.__load_main_xml(self.__source_path, file)

    def generate_name(self):
        random.random()
        pre = self.__prefixes[random.randint(0, len(self.__prefixes)-1)].get_text()
        suf = self.__suffixes[random.randint(0, len(self.__suffixes)-1)].get_text()
        return pre + suf


    def __load_main_xml(self, path, file):
        xml_file_name = self.__get_full_file_path(path, file)
        with open(xml_file_name, "r") as xml_file:
            tree =  ET.parse(xml_file)

        root = tree.getroot() 

        for pre in root.findall("./prefixes/prefix"):
            r = Radical(pre.text)
            self.__prefixes.append(r)

        for pre in root.findall("./suffixes/suffix"):
            r = Radical(pre.text)
            self.__suffixes.append(r)

    def __get_full_file_path(self, path, file):
        return os.path.join(path, file)

class Radical:
    def __init__(self, text):
        self.__text = text

    def get_text(self):
        return self.__text

    
    
