


def return_zero():
    return 0

def double(x):
    return 2*x

def triple(x):
    return 3*x

def if1(x):
    if x==0:
        return 'zero'
    if x>0:
        return 'positive'
    if x<0:
        return 'negative'

def if2(x):
    if x==0:
        return 'zero'
    elif x>0:
        return 'positive'
    elif x<0:
        return 'negative'

def loop1(x):
    result = 0
    for n in range(1, x+1):
        result = result + 1
    return result

def loop_sum(x):
    result = 0
    for n in range(1, x+1):
        result = result + n
    return result

def myjoin(lst, sep):
    rstring = ''
    for i in lst:
        rstring = rstring + i + sep
    return rstring[0:len(rstring)-len(sep)]