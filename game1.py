# Jackie Loven
# 6 September 2014
# Last Edited 7 September 2014
# Text-Based Conversation

"""You can have a nice conversation with a computer."""

import re

#----- Functions -----#

def isItYes(user_input):
    # Tests if the user input is "yes". Returns 1 for yes, 0 for no.
    if "Ye" in user_input or "ye" in user_input or "yE" in user_input:
        return 1
    else:
        return 0

def youLikeTo(user_input):
    # If the user input is in form "I like to ..." it outputs "to ..."
    i_like, like_, to_hobby = user_input.partition("like ")
    return to_hobby

def youLike(user_input):
    # If the user input is in form "I do/like ...ing" it outputs "...ing" and anything after
    hobbying = user_input[user_input.rfind(' ', 0, user_input.index('ing')) + 1:]
    hobbying_sanitized = re.sub(r'[^\w\hobbying]','',hobbying)
    return hobbying

def hobbyInputParse(user_input):
    # Tests which type the user input is and returns proper spliced strings
    if "ing" in user_input:
            return youLike(user_input)
    else:
        return youLikeTo(user_input)


#----- User-Input Variables -----#

# Asks the user for their name and repeats it back without punctuation
input_name = raw_input("Hi! What's your name? ")
name_sanitized = re.sub("[^a-z']", "", input_name.lower())
final_name = name_sanitized[0].upper() + name_sanitized[1:]
print ("It\'s nice to meet you, {}!".format(final_name))

# Asks the user a yes or no question
input_hobby_yn = raw_input("Do you have any hobbies? ")


#----- Computer Responses -----#

# If the user reports they have a hobby, computer says it's cool - if not, it is disappointed
if isItYes(input_hobby_yn) == 1:
    print ("That\'s so cool! I like juggling.")
else:
    print ("Aw, come on! Don't you like cooking or running or doodling?")

# Prompts the user for their hobby and repeats it after parsing
input_hobby = raw_input("What do you like to do? ")
print ("Wow! You like {}?".format(hobbyInputParse(input_hobby)))





