##-------------------------------------------------------##
## The main entrypoint for chrismas dellima v~south-east ##
##-------------------------------------------------------##

import datetime, sys, os

from core.dellima_builder import Builder as B
from core.dellima_api import Api as API

def main(start=True, verbose=True, workingdir="./dBots"):
    if start == True:
        game = B(startup=True,verbose=True,workingdir="./dBots")
        #game.OKAY()
        #print(f"-===-===-===-===-===-===-===-===-===-")
        #game.LISTBOTS()
        #game.PLAYGAME()

        #Apix = API()
        #Apix.ListThemBots(profile="testing")

        #exit(0)

        while True:
            x = input(">>")

            if x == "cls":
                os.system("clear")

            if x == "gameok":
                game.OKAY()
            
            if x == "bots":
                game.LISTBOTS()

            if x == "playgame":
                game.PLAYGAME()

main()

        