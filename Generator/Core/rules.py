from ..Enum import army
import xml.etree.ElementTree as ET

class Rule:
    def __init__(self, file):
        self.__file = file 
        self.__load_main_xml(file)
        self.__detachments = []

    def __load_main_xml(self, file):
        with open(file, "r") as xml_file:
            tree =  ET.parse(xml_file)

        root = tree.getroot() 

        for det in root.findall("./detachments/detachment"):
            d = Detachment(det)
            self.__detachments.append(d)

class Detachment:
    def __init__(self, xml):
        self.__required = []
        self.__optional = []
        self.__cp = 0
        self.__load_xml

    def __load_xml(self, xml):
        return 

class Condition:
    def __init__(self):
        self.__type = army.ArmyType.HQ
        self.__min = 1
        self.__max = 2