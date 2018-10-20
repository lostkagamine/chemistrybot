# chemistrybot
# (C) ry00001#3487, 2018
# spacechem (C) Zachtronics 2011

import discord
import json
import decodifier

with open('code.txt') as file:
    meme = decodifier.decode(file.read())
    print(meme)
