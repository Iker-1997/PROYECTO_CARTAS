from inn_tur import *
from mazos.mazos import *
from lucha import *

for z in range(0, mano_aliada):
    if mano_aliada[z]["type"] == "infantry" and mazo_enemiga[z]["type"] == "lancer" or mano_aliada[z]["type"] == "lancer" and mano_enemiga[z]["type"] == "chivalry" or mazo_aliada[z]["type"] == "chivalry"  and mazo_enemiga[z]["type"] == "infantry":
        modificador = mano_aliada[z]["attack"] * 2
        print(modificador)

for y in range(0, mano_enemiga):
    if mano_enemiga[y]["type"] == "infantry" and mazo_aliada[y]["type"] == "lancer" or mano_enemiga[y]["type"] == "lancer" and mano_aliada[y]["type"] == "chivalry" or mazo_enemiga[y]["type"] == "chivalry" and mazo_aliada[y]["type"] == "infantry":
        modificador2 = mano_enemiga[y]["attack"] * 2
        print(modificador2)