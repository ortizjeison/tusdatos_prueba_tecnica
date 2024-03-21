import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from apis import info_juicio
# setting path

def test_info_juicio():
    info_juicio.get_info_juicio("13284202406765")