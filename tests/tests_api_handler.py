
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from apis import api_handler
# setting path

def tests_query_demandado():
    api_handler.query_demandado('1791251237001')

def tests_query_demandante():
    api_handler.query_demandado('0992339411001')