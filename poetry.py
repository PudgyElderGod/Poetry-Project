#!----------!Global Variables!----------!#
#"Do you think God stays in heaven because he, too, lives in fear of what he created?"
#Because I made my poem All Star by Smash Mouth. I GET it.
#'Poem' credits to Smash Mouth
#I'm so sorry for this

import random
import re

poem = '''Somebody once told me the world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb with her finger and her thumb
In the shape of an "L" on her forehead
Well the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go
You'll never shine if you don't glow
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold
It's a cool place and they say it gets colder
You're bundled up now, wait till you get older
But the meteor men beg to differ
Judging by the hole in the satellite picture
The ice we skate is getting pretty thin
The water's getting warm so you might as well swim
My world's on fire, how about yours?
That's the way I like it and I never get bored
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
All that glitters is gold
Only shooting stars break the mold
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show, on get paid
And all that glitters is gold
Only shooting stars
Somebody once asked could I spare some change for gas?
I need to get myself away from this place
I said yep what a concept
I could use a little fuel myself
And we could all use a little change
Well, the years start coming and they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go (go!)
You'll never shine if you don't glow
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold
And all that glitters is gold
Only shooting stars break the mold'''

#!----------!Open File Stretch Challenge!----------!#
f = open("allstar.txt", "r")
file_poem = f.readlines()
f.close

#!----------!Line Breaks!----------!#
lines_list = poem
Line_Apology = '''#!!!------!I'm so sorry!------!!!#
#!!!---!Why Am I Like This!---!!!#
#!!!------!I'm so sorry!------!!!#'''
Line_Break1 = '''#!!!------!Reverse Poems!------!!!#
#!!!----!Poems But Reverse!----!!!#
#!!!------!Reverse Poems!------!!!#'''
Line_Break2 = '''#!!!-------!RandomPoems!-------!!!#
#!!-!Poems That Are Randomized!-!!#
#!!!-------!RandomPoems!-------!!!#'''
Line_Break3 = '''#!!!-----!Remove a letter!-----!!!# '''
print(Line_Apology)
print(lines_list, sep="\n")
print(Line_Break1)

#!----------!Functions!----------#
#Prints the lines of the 'poem' but in reverse. All stylish like.
def lines_printed_backwards():
    '''This function takes in a list of strings containing the lines of your poem as arguments and will print the poem lines out in reverse with the line numbers reversed.'''
    lines_list = file_poem
    reverse = lines_list.reverse()
    print(*lines_list, sep="\n")
    # for i in range(len(lines_list)):
    #     print(lines_list[i])

#Prints the lines of the 'poem' but randomized. Chaotic Evil.
def lines_printed_random():
    '''Your code should implement the lines_printed_random() function which will randomly select lines from a list of strings and print them out in random order. '''
    lines_list = file_poem
    random.shuffle(lines_list)
    print(*lines_list, sep="\n")

#Custom Function
#Replaces letters for other letters.
#Makes the entirely thing completely awful.
def replace_letters():
    #Refreshes the poem.
    f = open("allstar.txt", "r")
    file_poem = f.readlines()
    f.close
    #The function itself.
    replacement=poem.replace("e", "a").replace("o", "u").replace("me", "somebody")
    lines_list=replacement.splitlines()
    print(*lines_list, sep="\n")

#Just wanted to see if I could do this.
def replace_custom_letters():
    #Refreshes the poem
    f = open("allstar.txt", "r")
    file_poem = f.readlines()
    f.close
    #Actual Function
    i1=input("Enter a letter you want replaced:")
    i2=input("Enter the letter you want to replace it with:")
    print("#!!!----!Time To Get Wild!----!!!#")
    replacement=poem.replace(i1, i2)
    lines_list=replacement.splitlines()
    print(*lines_list, sep="\n")





#!----------!Function Calls!----------!#
lines_printed_backwards()
print(Line_Break2)
lines_printed_random()
print(Line_Break3)
# replace_letters()
# print(Line_Break1)
replace_custom_letters()


#!----------!Test Code!----------!#
#def custom_funciton():
#The Percy Bysshe Shelley version, of course. I'm not a monster.
test_poem = """I met a traveller from an antique land
Who said: Two vast and trunkless legs of stone
Stand in the desert. Near them, on the sand,
Half sunk, a shattered visage lies, whose frown,
And wrinkled lip, and sneer of cold command,
Tell that its sculptor well those passions read
Which yet survive, stamped on these lifeless things,
The hand that mocked them and the heart that fed:
And on the pedestal these words appear:
'My name is Ozymandias, king of kings:
Look on my works, ye Mighty, and despair!'
Nothing beside remains. Round the decay
Of that colossal wreck, boundless and bare
The lone and level sands stretch far away."""

Line_Break_Test = """#!---------!Test Code!---------!#
#!------!Code That Tests!------!#
#!---------!Test Code!---------!#
"""

#Test Functions#
def test_lines_printed_backwards():
    lines_list = test_poem.split("\n")
    reverse = lines_list.reverse()
    print(*lines_list, sep="\n")

def test_lines_printed_random():
    lines_list = test_poem.split("\n")
    random.shuffle(lines_list)
    print(*lines_list, sep="\n")

def test_custom_function():
    i1=input("Enter a letter you want replaced:")
    i2=input("Enter the letter you want to replace it with:")
    print("#!!!----!Time To Get Wild!----!!!#")
    replacement=test_poem.replace(i1, i2)
    lines_list=replacement.splitlines()
    print(*lines_list, sep="\n")

#Test Calls
# test_lines_printed_backwards()
# print(Line_Break_Test)
# test_lines_printed_random()
# print(Line_Break_Test)
# test_custom_function()
# print(Line_Break_Test)
