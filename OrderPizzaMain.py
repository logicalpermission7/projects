
from pizzapi import *


Elvis = Customer("Elvis", "Bueno", "elvisbueno1010@gmail.com", "9316141937")
my_local_dominoes = StoreLocator.find_closest_store_to_customer(Elvis)
my_local_dominoes
