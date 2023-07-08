# VerbConjugator
Simple spanish verb conjugator

The function verbconjug takes two parameters: pronoun (the pronoun representing the subject) and verb (the verb to be conjugated).
The pronoun and verb are converted to lowercase to make them case-sensitive.

The code extracts the ending of the verb (last two characters) and the root of the verb (all characters except the last two).
It checks various conditions based on the pronoun and conjugates the verb accordingly.

If the pronoun is "yo" (I), the code returns the pronoun followed by the root of the verb with "o" added.
If the pronoun is "tu" (you singular informal), it checks the ending of the verb and returns the pronoun followed by the appropriate conjugation of the root.
If the pronoun is "nosotros" (we), it checks the ending of the verb and returns the pronoun followed by the appropriate conjugation of the root.
If the pronoun is "el" (he), "ella" (she), or "usted" (you singular formal), it checks the ending of the verb and returns the pronoun followed by the appropriate conjugation of the root.
If the pronoun is "ellos" (they masculine), "ellas" (they feminine), or "ustedes" (you plural), it checks the ending of the verb and returns the pronoun followed by the appropriate conjugation of the root.

There is a commented-out code block that provides an alternative shorter implementation for the "nosotros" pronoun.
