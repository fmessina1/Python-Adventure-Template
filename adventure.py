__author__ = 'Les Pounder'

"""
    The lines below import modules of code into our GAME,
    in particular these import time functions allow us to pause and stop the game,
    and random provides a method of choosing random numbers or characters.

    To run this file in your terminal, type: `python3 adventure.py`
"""
from time import *
from random import *
import os,sys
from art import *

"""
    Simple function that clears the terminal screen
"""
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def title():
    # TODO change the title of the game, each of these three lines should have new text
    print(text2art('Earth', font='alpha'))
    print(text2art('  Lab', font='alpha'))
    print(text2art(' Hero', font='alpha'))

def north():
    print ("To go to math class on the third floor press n then enter")

def east():
    print ("To go to the gym and play basketball press e then enter")

def south():
    print ("to go to the cafeteria and eat lunch press s then enter")

def west():
    print ("To go to meet with a teacher about a homework assignment press w then enter")


def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global HP
    global MP
    #Our variable "name" is used to store our name, captured by keyboard input.
    name = input("Hi, what's your name?")
    #randint is a great way of adding some variety to your players statistics through randomness
    HP = randint(5,20)
    MP = randint(5,20)

def villager():
    #This will create a randomly named Villager to interact with
    global npcname
    global response
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = ["Hi, are you new to the school? Where are you going?"]
    npcnamechoice = ["Frankie", "Peter", "Wyatt", "Emma"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print ("\n["+npcname+":] Hello, my name is "+npcname+", Would you like to talk to me?\n")
    shuffle(responses)
    print ("Press y to talk to the student")
    if input() == "y":
        print ("%s: %s" % (npcname, responses[0]))
    else:
        print ("%s: Goodbye" % npcname)

def enemy():
    global enemyHP
    global enemyMP
    global enemyname
    enemyHP = randint(5,20)
    enemyMP = randint(5,20)
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemyname = "friend"
    print ("\nSuddenly you see a very nice kid approaching you "+enemyname+"....")
    #print enemyname
    # TODO change messages to "friend"
    print ("Your enemy has %s confidence Points" % str(enemyHP))
    print ("Your enemy has %s grade Points" % str(enemyMP))


"""
    We now use our functions in the game code, we call functions title() and setup() for our character.
"""
clear_screen()
title()
setup()
global name
global HP
global MP
global move
global enemyHP
print ("Welcome to Brooklyn Friends School" %s" % name)
#Sleep is Python's way of pausing the game for a specified number of seconds
sleep(2)
#Below we are using the helper functions to join a string of text to an integer via the str() helper.
print ("\nYour confidence is" + " " + str(HP))
print ("Your grade is" + " " + str(MP))



print ("Would you like to travel to your new school for your first day? Press y then enter to continue")
#Below we use input to ask for user input, and if it is equal to y, then the code underneath is run.
if input() == "y":
    print ("You wake up eat breakfast and are ready for your first day")
    print ("Would you like to take your bookds and bookbag? Press y then enter to continue")
    if input() == "y":
        #This is a list, and it can store many items, and to do that we "append" items to the list.
        weapons = []
        weapons.append("books")
        weapons.append("bookbag")
        print ("You are now carrying your %s and your %s" % (weapons[0], weapons[1]))
        # TODO maybe change the word "Armed" to something more befitting books?
        print ("Armed with your %s and %s you swing open the door to your home ready for your new beginning ar your new school." % (weapons[0], weapons[1]))
    else:
        print ("You choose not to take your books and go to school")
        print ("You go to school unprepared and get in trouble with your teachers.")
else:
    print ("You decide to stay at home and lose out on an outstanding oppourtunity to gain knowledge.")
    print ("Game Over")
    sys.exit(0)

print ("You can see your school right when you leave your house, it's conveniently right across the street. You begin your new journey of high school by walking to the Brooklyn Friends School building.")

#Remember those functions we created at the start of the code? Well here we are using them in the game.
print ("\n")
north()
east()
west()
move = input("Where would you like to go?")
if move == 'n':
    print ("\nYou walk up the stairs and stop at the third floor. You open the door which leads to the third floor and walk through it. You walk  down the hall searching for your math class.")
    print ("A student is in your path and greets you. He asks, what class are you in? You respnd saying Joel's math class.")
    print ("He kindly leads you to your math class")
    print ("You enjoy your first math class and you're very happy that you've made your first friend.")
#elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
elif move == 'e':
    print ("\nYou have decided to join the basketball team at your new high school. You walk over to the lowere gym which is in the middle school building. You walk downstairs to the gym excited for your first practice.")
    print ("You are greeted by your coach and he kindly welcomes you to your new team. The guys on the team welcome you very nicely and you're very excited for the upcoming season at school.")
elif move == 'w':
    print ("\nAfter a great first day at school that went by very quickly you're confused about your english homework. You visit Sarah Levy's office to review the homework.")
    print ("She warmly welcomes you and you review the homework. You're very grateful fo rthe kind teachers at your new school.\n")
elif move == 's':
    print ("\nYou are very hungry and decide to go get something to eat at the school's cafeteria.")
    print ("Whule in line waiting for food you meet a new friend. You bond over lunch and you're ecstatic about meeting your new friend")

villager()
enemy()
sleep(3)

fight = input("Do you want to be friends" )

if fight == "y":
    while HP > 0:
#This loop will only work while our characters HP is greater than 0.
        hit = randint(0,5)
        print ("You start to talk which gives you %s of confidence" % str(hit))
        enemyHP = enemyHP - hit
        print (enemyHP)
        enemyhit = randint(0,5)
        print ("After bonding for a while you and your new friend do homework and you gain %s of grades" % str(enemyhit))
        HP = HP - enemyhit
        print (HP)
else:
    print ("You turn and leave your new friends")

print ("This is just the beginning of an amazing four years at Brooklyn Friends, you are now on your own to continue high school.")

# TODO change this art to print something else?
print ("   _       _                 _")
print ("  /_\   __| |_   _____ _ __ | |_ _   _ _ __ ___")
print (" //_\\ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ ")
print ("/  _  \ (_| |\ V /  __/ | | | |_| |_| | | |  __/")
print ("\_/ \_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|)")

print ("                     _ _")
print ("  __ ___      ____ _(_) |_ ___")
print (" / _` \ \ /\ / / _` | | __/ __|")
print ("| (_| |\ V  V / (_| | | |_\__ \ ")
print (" \__,_| \_/\_/ \__,_|_|\__|___/)")

print (" _   _  ___  _   _")
print ("| | | |/ _ \| | | |")
print ("| |_| | (_) | |_| |")
print (" \__, |\___/ \__,_|")
print (" |___/")
