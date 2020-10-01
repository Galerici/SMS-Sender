#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s



banner = """

| You have the right to send a message to the phone address you want once a day. 
| Your message has a limited number of characters, you will see this after you write your message.
| If you do not enter your phone address correctly, you may get an error.

"""

print(banner)

sor = input("Phone Adress Exp:+905555555555 >>> ")

mesaj = input("Your message >>> ")

arlk = mesaj[0:70]

print("\n| The part of your message that can be sent is as follows.\n"+arlk)

drlm = input("\n| Send Your Message?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|You made a mistake.")

