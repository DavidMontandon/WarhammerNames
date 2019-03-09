# -*- coding: utf-8 -*
import sys, os, getopt
from Generator.Core import names as NG
from Generator.Ui.Text import engine

def main(argv):
    cur_folder = os.getcwd()

    e = engine.TextEngine(os.path.join(cur_folder, "Source"))
    e.run()

if __name__ == "__main__":
    main(sys.argv[1:])  