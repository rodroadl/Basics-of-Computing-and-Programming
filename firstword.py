def firstword(phrase):
    space = phrase.find(' ')
    if (space == -1):
        return (phrase)
    else:
        return (phrase[:space])