## bot1

import random, json, sys

pre_data = {}

def gen_res(pre_data):
    if pre_data[0] == "0":
        return random.choice([0,0,0,0,1])
    else:
        return random.choice([1,1,1,1,0])

is_genesis = "d"

if len(sys.argv) == 1:
    is_genesis = "genesis"

if is_genesis == "genesis":
   pre_data = [random.choice([0,0,0,1])]
else:
    with open(("./log.json")) as jsonfile:
        pre_data = json.load(jsonfile)





new_data = gen_res(pre_data)

pre_data += str(new_data)

#for x in pre_data:
#    print(x)

with open("./log.json", "w") as jsonfilex:
    #json.dump(str(pre_data),"./log.json",indent=4)
    jsonfilex.write(str(pre_data).replace("'",'"'))

with open("./answer_bot1.json","w") as myanswer:
    myanswer.write(str(new_data))

    