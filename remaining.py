def remainingwords(phrase):
    space = phrase.find(' ')
    if (space == -1):
        return ''
    else:
        return (phrase[space + 1:])