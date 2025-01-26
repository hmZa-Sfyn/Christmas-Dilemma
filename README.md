## Chrismas Dellima

`A simple game-like thing, inspired by ` __chrismas_dellima__ `, programmed in python language.`

---

```bash
┌──(hmza㉿hmza)-[~/perv/chrismas_dellima]
└─$ python3 /home/hmza/perv/chrismas_dellima/dellima.py
>>gameok
Listed(2) bots:
  0 bot2 ./dBots/bot2
  1 bot1 ./dBots/bot1
bot-loaded
Bot: bot2 loaded.
Bot: bot1 loaded.
Loaded (2) bots:
  0 bot2
  1 bot1
>>bots
  0 bot2
  1 bot1
>>playgame

PLAYGAME
1: ./dBots/bot2/bot.py 
   .Vs
2: ./dBots/bot1/bot.py
bot1: 147
bot2: 402
>>
```

### 52422085E6126A516A8E65.json
```bash
{"rounds": 100, "./dBots/bot2/bot.py": 147, "./dBots/bot1/bot.py": 402}
```

### More

#### DirTree

```bash
.
├── all_bots_rating
├── answer1.json
├── answer2.json
├── answer_bot1.json
├── core
│   ├── dellima_api.py
│   ├── dellima_builder.py
│   ├── __init__.py
│   └── __pycache__
│       ├── dellima_api.cpython-312.pyc
│       ├── dellima_builder.cpython-312.pyc
│       └── __init__.cpython-312.pyc
├── dBots
│   ├── bot1
│   │   └── bot.py
│   └── bot2
│       └── bot.py
├── dellima.py
├── log.json
└── README.md

7 directories, 14 files
```

### Api  `Not Complete!`
```python
Apix = API()
        Apix.ListThemBots(profile="testing")
```

```bash
profile testing loaded.
path /home/hmza/perv/chrismas_dellima/ loaded.
looking for dir containing bots(dBots) in path /home/hmza/perv/chrismas_dellima/
INFO found a dir dBots in /home/hmza/perv/chrismas_dellima/
looking for bots in path /home/hmza/perv/chrismas_dellima/dBots
info found a potential bot in path /home/hmza/perv/chrismas_dellima/dBots/bot2
INFO found an actual bot in path /home/hmza/perv/chrismas_dellima//dBots/bot2/bot.py
info found a potential bot in path /home/hmza/perv/chrismas_dellima/dBots/bot1
INFO found an actual bot in path /home/hmza/perv/chrismas_dellima//dBots/bot1/bot.py
total: 2 bots found, 2 bots contain bot.py

```
