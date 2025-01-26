##----------------------------------------------------------##
## The main builder class for chrismas dellima v~south-east ##
##----------------------------------------------------------##

import colorama, datetime, os, random

class Builder:
    def __init__(self, startup=True, verbose=True, workingdir="./dBots"):
        self.pwd = workingdir
        self.verbose = verbose
        self.startup = startup


        self.bots = []
        self.bot_paths = []
        
        self.ok_bots = []

    def OKAY(self):
        try:
            for Thing in [os.listdir(self.pwd)]:
                self.bots += Thing
                #self.bot_paths += str(f"{self.pwd}/{self.bots[-1]}")

            if self.verbose == True:
                print(f"Listed({colorama.Fore.GREEN}{len(self.bots)}{colorama.Fore.RESET}) bots:")
                for BOT in range(len(self.bots)):
                    print(f"{colorama.Fore.WHITE}{BOT:-3}{colorama.Fore.RESET} {colorama.Fore.GREEN}{str(self.bots[BOT])}{colorama.Fore.RESET} {colorama.Fore.YELLOW}{self.pwd}/{self.bots[BOT]}{colorama.Fore.RESET}")
            else:
                print(f"Listed ({colorama.Fore.GREEN}{len(self.bots)}{colorama.Fore.RESET}) bots, turn os verbose to see them.")         

            print(f"{colorama.Fore.GREEN}bot-loaded{colorama.Fore.RESET}")

            #print(f"bots: {self.bots}, bot-paths: {self.bot_paths}")

            for Bot in range(len(self.bots)):
                bot_okay = False

                for File in os.listdir(f"{self.pwd}/{self.bots[Bot]}"):
                    if File == "bot.py":
                        bot_okay = True

                if bot_okay != True:
                    print(f"Bot: {colorama.Fore.RED}{self.bots[Bot]}{colorama.Fore.RESET} excluded, it does not have a {colorama.Fore.RED}{self.pwd}/{self.bots[Bot]}/bot.py {colorama.Fore.RESET}file")
                else:
                    print(f"Bot: {colorama.Fore.GREEN}{self.bots[Bot]}{colorama.Fore.RESET} loaded.")
                    if len(self.ok_bots) == 0:
                        self.ok_bots.append(self.bots[Bot])
                    else:
                        self.ok_bots.append(self.bots[Bot])


            if self.verbose == True:
                print(f"Loaded ({colorama.Fore.GREEN}{len(self.ok_bots)}{colorama.Fore.RESET}) bots:")
                for BOT in range(len(self.ok_bots)):
                    print(f"{colorama.Fore.WHITE}{BOT:-3}{colorama.Fore.RESET} {colorama.Fore.GREEN}{str(self.ok_bots[BOT])}{colorama.Fore.RESET}")
            else:
                print(f"Loaded ({colorama.Fore.GREEN}{len(self.bots)}{colorama.Fore.RESET}) bots, turn os verbose to see them.")                    
        
        except Exception as ex:
            print(f"{colorama.Fore.RED}bot-error: {ex}{colorama.Fore.RESET}")   

    def LISTBOTS(self):
            for BOT in range(len(self.ok_bots)):
                    print(f"{colorama.Fore.WHITE}{BOT:-3}{colorama.Fore.RESET} {colorama.Fore.GREEN}{str(self.ok_bots[BOT])}{colorama.Fore.RESET}")    
        
    def PLAYGAME(self):
        bot1 = random.choice(self.ok_bots)
        bot2 = random.choice(self.ok_bots)

        points1 = 0
        points2 = 0

        for x in range(5):
            if bot1 == bot2:
               bot2 = random.choice(self.ok_bots)

        bot1 = f"{self.pwd}/" + bot1 + "/bot.py"
        bot2 = f"{self.pwd}/" + bot2 + "/bot.py"

        print(f"\nPLAYGAME\n1: {colorama.Fore.GREEN}{bot1}{colorama.Fore.RESET} \n   .Vs\n2: {colorama.Fore.GREEN}{bot2}{colorama.Fore.RESET}")
        
        ###

        game_rounds = 100

        for x in range(game_rounds):
            os.system(f"python3 {bot1} genesis")
            os.system(f"python3 {bot2}")

            ans1 = ""
            ans2 = ""

            with open("./answer1.json", "r") as answerofbot1:
                ans1 = answerofbot1.read()

            with open("./answer2.json", "r") as answerofbot2:
                ans2 = answerofbot2.read() 

            ## results

            

            if ans1 == "1" and ans2 == "1":
                points1 += 3
                points2 += 3

            if ans1 == "1" and ans2 == "0":
                points1 += 0
                points2 += 5

            if ans1 == "0" and ans2 == "0":
                points1 += 1
                points2 += 1

            if ans1 == "0" and ans2 == "1":
                points1 += 5
                points2 += 0

        print(f"bot1: {points1}\nbot2: {points2}")

        json_data = {"rounds":game_rounds,f"{bot1}":points1,f"{bot2}":points2}

        ## ./all_bots_rating/$bot1
        
        rand_name = random_name()

        for x in os.listdir("./all_bots_rating"):
            if x == rand_name:
                rand_name = random_name(256)
                continue
        
        with open(f"./all_bots_rating/{rand_name}.json", "w") as rating:
            rating.write(str(json_data).replace("'",'"'))



        
        
def random_name(what=0):
    rand_name = ""

    if what >= 15:
        rand_name = ""
        for x in range(random.choice([5,8,10,13,16,20,23])):
            random_result_name = random.choice([0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"])
            rand_name = rand_name + str(random_result_name)
    else:
        for x in range(random.choice([4,7,9,12,15,19,22])):
            random_result_name = random.choice([0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"])
            rand_name = rand_name + str(random_result_name)

    return (rand_name)
        

