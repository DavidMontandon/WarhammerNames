# -*- coding: utf-8 -*
import sys, os, getopt
from Generator import names as NG

def main(argv):
    cur_folder = os.getcwd()
    gen = NG.NameGenerator(cur_folder, "Source", "DeathGuard.xml")
    print(gen.generate_name())
    print(gen.generate_name())
    print(gen.generate_name())
    print(gen.generate_name())
    print(gen.generate_name())

if __name__ == "__main__":
    main(sys.argv[1:])  