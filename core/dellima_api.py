##----------------------------------------------##
## The main api class for the devs v~south-east ##
##----------------------------------------------##

import os, datetime, random, colorama

def GenUuid(what=0):
    rand_name = ""

    if what > 0:
        rand_name = ""
        for x in range(random.choice([what])):
            random_result_name = random.choice([0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F","dumb","minecraft"])
            rand_name = rand_name + str(random_result_name)
    else:
        for x in range(random.choice([10])):
            random_result_name = random.choice([0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F","noob"])
            rand_name = rand_name + str(random_result_name)

    return (rand_name)
    
verbose = True

class Api:
    def __init__(self, name="Bob99", application="UseLess-App", uuid=GenUuid(), verboseX=False):
        self.name = name
        self.uuid = uuid

        self.application = application
        
        self.profile = "default"
        self.profiles = {
            "default":{
                "path":""
            },
            "testing":{
                "path":"/home/hmza/perv/chrismas_dellima/"
            }
        }

        self.verbose = verboseX

    def ListThemBots(self, profile="default"):
        global_path = ""
        try:
            pathX = self.profiles[profile]["path"]
            printx(f"profile {colorama.Fore.GREEN}{profile}{colorama.Fore.RESET} loaded.")
            if pathX != "":
                printx(f"path {colorama.Fore.GREEN}{pathX}{colorama.Fore.RESET} loaded.")
                global_path = pathX
            else:
                printx(f"path {colorama.Fore.RED}{pathX}{colorama.Fore.RESET}is empty.")
                return 0
        except:
            printx(f"profile {colorama.Fore.RED}{profile}{colorama.Fore.RESET} not found.")

        bots = []
        bots_ok = []

        printx(f"looking for dir containing bots(dBots) in path {colorama.Fore.GREEN}{global_path}{colorama.Fore.RESET}")   
        for filesx in os.listdir(global_path):
            if filesx == "dBots":
                printx(f"{colorama.Fore.GREEN}INFO{colorama.Fore.RESET} found a dir {colorama.Fore.GREEN}dBots{colorama.Fore.RESET} in {colorama.Fore.GREEN}{global_path}{colorama.Fore.RESET}")
            
                printx(f"looking for bots in path {colorama.Fore.GREEN}{global_path}dBots{colorama.Fore.RESET}")
                for filesxx in os.listdir(f"{global_path}dBots/"):
                    #if os.path.isdir(filesxx):
                        #bots.append(f"{global_path}/dBots/{filesxx}")
                        for filesxxx in os.listdir(f"{global_path}/dBots/{filesxx}"):
                            printx(f"{colorama.Fore.GREEN}info{colorama.Fore.RESET} found a potential bot in path {colorama.Fore.GREEN}{global_path}dBots/{filesxx}{colorama.Fore.RESET}")
                            if filesxxx == "bot.py":
                                bots.append(f"{global_path}/dBots/{filesxx}/bot.py")
                                bots_ok.append(f"{global_path}/dBots/{filesxx}/bot.py")
                                printx(f"{colorama.Fore.GREEN}INFO{colorama.Fore.RESET} found an actual bot in path {colorama.Fore.GREEN}{global_path}/dBots/{filesxx}/bot.py{colorama.Fore.RESET}")    

        printx(f"total: {colorama.Fore.GREEN}{len(bots)}{colorama.Fore.RESET} bots found, {colorama.Fore.GREEN}{len(bots_ok)}{colorama.Fore.RESET} bots contain bot.py")
        
        return {"bots":bots,"bots_ok":bots_ok}


def printx(item=""):
    if verbose == True:
        print(item)
        