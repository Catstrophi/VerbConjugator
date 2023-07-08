"""
Verb Conjugator - changing the ending of the verb to fit the pronoun
Should test you on how good are you at managing your if and else statements as well
    as basic string manipulation/methods

We want to make this case-sensitive, so we don't need lots of ors to determine it
    We can just use the .lower() function. This changes the string to all lower case

Instead of printing it we can return it. there are many ways to do this:
    You can assign the finalWord to a variable and then return the variable at the end,
        or you can just return it after the if statement like I did here.

For getting the root word(word without the ending) and the ending, you can just store it in a variable
    called root and end respectively. This can save you some lines of code and overall makes your code looks
        neater and easier to change

Along with this we also don't want 3 if statements per or 15 in total,
for most of this we can simplify them to 1 or 2.
    For example for yo, the ending are the same no matter what
        we just need to make sure if the pronoun is
    Same thing can be said for tu, el, ellos, etc., their only specific case
        is the ending -ar, other than that they are the same
    You can also use cases to do this, which is easier, but you haven't learned it yet

There is a special case for nosotros:
    When you do it you can you 3 if statements for each of the 3 endings, or you can just
        remove the last letter of the ending and just add mos.
            For example: hablar
                Instead of removing ar and adding amos, you can just remove the r and add mos
                    This works for -ar, -er, -ir
        This just depends on how you are going to be graded on

The rest of the code is pretty self-explanatory, we are just finding the pronoun and verb, changing it, and formatting
    the return statement so when we print it, its prints in the format of: pronoun + conjugated verb

At the very end to easier test if the code works you can just but it in a while True loop
    with inputs for both the pronoun and verb and run it.
        After that you can just remove it
"""

def verbconjug(pronoun, verb):
    # Making the pronouns and verbs case-sensitive
    pronoun = pronoun.lower()
    verb = verb.lower()

    # Getting the ending and the word without the ending
    end = verb[-2:]
    root = verb[:-2]

    # If pronoun is yo
    if pronoun == "yo":
        return pronoun + " " + root + "o"

    # If pronoun is tu
    if pronoun == "tu":
        if end == "ar":
            return pronoun + " " + root + "as"
        else:
            return pronoun + " " + root + "es"

    # If pronoun is nosotros
    if pronoun == "nosotros":
        if end == "ar":
            return pronoun + " " + root + "amos"
        elif end == "er":
            return pronoun + " " + root + "emos"
        else:
            return pronoun + " " + root + "imos"

    """
    # If you want to shorten code for nosotros
    if pronoun == "nosotros":
        # Just remove the r from each and add the mos would work to
        return pronoun + " " + verb[-1:] + "mos"
    """

    # If pronoun is el or ella or usted
    if pronoun == "el" or pronoun == "ella" or pronoun == "usted":
        if end == "ar":
            return pronoun + " " + root + "a"
        else:
            return pronoun + " " + root + "e"

    # If pronoun is ellos or ellas or ustedes
    if pronoun == "ellos" or pronoun == "ellas" or pronoun == "ustedes":
        if end == "ar":
            return pronoun + " " + root + "an"
        else:
            return pronoun + " " + root + "en"

# Running and printing the function
print(verbconjug("yo", "hablar"))

"""
# Testing easier for all cases
while True:
    p = input("Please enter your pronoun: ")
    v = input("Please enter your verb: ")
    print(verbconjug(p, v))
"""
