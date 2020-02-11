#!/usr/bin/env python

import random
import os
import colorama
from colorama import Fore


def play_again():
  global Win
  global Start_Game

  Attempts = 0 

  while not Win and Start_Game == True:
      User_Guess = int(input("Take a wild guess:"))
      Attempts += 1
      if User_Guess == Random_number:
        Win = True

      elif User_Guess > Random_number:
        print("Lower.")

      elif User_Guess < Random_number:
          print("Higher.")
          
      elif User_Guess == ' ':
        print('numbers only...')

  retry = input("would you like to play again?[Y/N]\n> ")
  if retry.lower() == "y":
    Win = False
    play_again()


Random_number = random.randint(0, 100)
Attempts = 0
Win = False
Start_Game = True

uname = str(input("Hello, your name is..."))

Game_choice = str(input("Would you like to play a game, " + uname + "?[Y/N]"))
try:

  if Game_choice.lower() == "y":
      print("Yay! Ok, the game is simple.")
      print("I will think of a number between 0 and 100 and you have to guess the number I thought up with the least number of tries.")
  else:
      print("Ok then, maybe next time...\n\nSike u still gonna play")
      
      print("I will think of a number between 0 and 100 and you have to guess the number I thought up with the least number of tries.")
      

  while not Win and Start_Game == True:
      User_Guess = int(input("Take a wild guess:"))
      Attempts += 1
      if User_Guess == Random_number:
        Win = True

      elif User_Guess > Random_number:
        print("Lower.")

      elif User_Guess < Random_number:
          print("Higher.")
          
      elif User_Guess == ' ':
        print('numbers only...') 
#  Guess_Again = int(input("Try again:"))
except ValueError:
  print('[-] Numbers only bruh...\n [-] Exiting')
  os._exit(1)

if Win == True:
  print(Fore.GREEN + "You Win! And it only took", Attempts, "tries!")

  print(Fore.RESET)

  retry = input("would you like to play again?[Y/N]\n> ")
  if retry.lower() == "y":
    Win = False
    play_again()
    

#else:
#	print("ok,then... maybe next time")
