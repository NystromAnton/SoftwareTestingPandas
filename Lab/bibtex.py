def extract_author(str):
    commaSplit = str.split(',')
    if len(commaSplit) == 1:
        spaceSplit = str.split(' ')
        if len(spaceSplit) == 1:
            result = (str,'')
        else:
            result = (spaceSplit[len(spaceSplit)-1],' '.join(spaceSplit[0:(len(spaceSplit)-1)]))
    else:
        result = (commaSplit[0], commaSplit[1].strip())
    
    return result

def extract_authors(str):
    andSplit = str.split('and')
    result = len(andSplit)*[None]
    for i in range(len(andSplit)):
        result[i] = extract_author(andSplit[i].strip())
    return result