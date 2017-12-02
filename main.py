
import sys
import os

myPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'LDEngine')
if myPath not in sys.path:
    sys.path.insert(0, myPath)

import LDEngine.ldLib
from LDEngine.ldLib.Sprites.GenericEnemy import GenericEnemy

if __name__ == '__main__':

    print(sys.path)
    print("This is a test")
