#!----------!Global Variables!----------!#
#"Do you think God stays in heaven because he, too, lives in fear of what he created?"
#Because I made my poem All Star by Smash Mouth. I GET it.
#'Poem' credits to Smash Mouth
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
Line_Break = '''#!!!----------!Poems!----------!!!#'''
lines_list = poem.split("\n")
print(lines_list)
print(Line_Break)

#!----------!Functions!----------#

#Prints the lines of the 'poem' but in reverse. All stylish like.
def lines_printed_backwards():
    '''This function takes in a list of strings containing the lines of your poem as arguments and will print the poem lines out in reverse with the line numbers reversed.'''
    reverse = lines_list.reverse()
    for i in range(len(lines_list)):
        print(lines_list[i])

#Prints the lines of the 'poem' but randomized. Chaotic Evil.
def lines_printed_random():
    '''Your code should implement the lines_printed_random() function which will randomly select lines from a list of strings and print them out in random order. '''
    random = lines_list.random()
    for i in range(len(lines_list)):
        print(lines_list[i])

    pass


def custom_funciton():
    '''Does something of your choosing'''

#!----------!Function Calls!----------!#
lines_printed_backwards()
print(Line_Break)


#!----------!Test Code!----------!#
#TODO: Get poem string into list of lines
#def lines_printed_backwards():
#def lines_printed_random():
#def custom_funciton():
