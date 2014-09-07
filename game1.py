# Jackie Loven
# 6 September 2014
# Text-Based Game

"""This is my first trial of a Python script."""

# Functions
def isItYes(user_input):
    if user_input[:2] == "Ye" or user_input[:2] == "ye":
        return 1
    else:
        return 0


def youLikeTo(user_input):
    i_like, like_, to_hobby = user_input.partition("like ")
    return to_hobby

def youLike(user_input):
    i_like, like_, hobbying = user_input.partition("like ")
    return hobbying

def hobbyInputParse(user_input):
    if "ing" in user_input:
            return youLike(user_input)
    else:
        return youLikeTo(user_input)


# User-Input Variables
input_name = raw_input("Hi! What's your name? ")
print ("It\'s nice to meet you, {}!".format(input_name))

input_hobby_yn = raw_input("Do you have any hobbies? ")


# Computer Responses
if isItYes(input_hobby_yn) == 1:
    print ("That\'s so cool! I like juggling.")
else:
    print ("Aw, come on! Don't you like cooking or music or doodling?")


input_hobby = raw_input("What do you like to do? ")
print ("Wow! You like {}?".format(hobbyInputParse(input_hobby)))





