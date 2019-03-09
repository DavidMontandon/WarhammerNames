import random
import os
import xml.etree.ElementTree as ET

class NameGenerator:
    def __init__(self, source, file):
        self.__version = "0.0.3"
        self.__source_path = source
        self.__file = file 
        self.__prefixes = [] 
        self.__suffixes = [] 
        self.__middles = [] 
        self.__combinations = []
        self.__load_main_xml(self.__source_path, file)

    def generate_name(self):
        random.random()
        name = ""
        con = self.__combinations[random.randint(0, len(self.__combinations)-1)]

        for c in con.get_order():
            if(c == "prefix"):
                name = name + self.__prefixes[random.randint(0, len(self.__prefixes)-1)].get_text()
            elif(c == "suffix"):
                name = name + self.__suffixes[random.randint(0, len(self.__suffixes)-1)].get_text()
            elif(c == "middle"):
                name = name + self.__middles[random.randint(0, len(self.__middles)-1)].get_text()

        return name

    def __load_main_xml(self, path, file):
        xml_file_name = os.path.join(path, file)
        with open(xml_file_name, "r") as xml_file:
            tree =  ET.parse(xml_file)

        root = tree.getroot() 

        for pre in root.findall("./prefixes/prefix"):
            r = Radical(pre.text)
            self.__prefixes.append(r)

        for suf in root.findall("./suffixes/suffix"):
            r = Radical(suf.text)
            self.__suffixes.append(r)

        for mid in root.findall("./middles/middle"):
            r = Radical(mid.text)
            self.__middles.append(r)

        for con in root.findall("./combinations/combination"):
            c = Combination(con)
            self.__combinations.append(c)
            
class Combination:
    def __init__(self, xml):
        self.__order = []
        for r in xml:
            if(r.tag == "prefix"):
                self.__order.append("prefix")
            elif(r.tag == "suffix"):
                self.__order.append("suffix")
            elif(r.tag == "middle"):
                self.__order.append("middle")

    def get_order(self):
        return self.__order 

class Radical:
    def __init__(self, text):
        self.__text = text

    def get_text(self):
        return self.__text

    
    
