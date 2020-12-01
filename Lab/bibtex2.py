

def extract_author(str):
    
    if " " not in str:
        return(str, "")

    names = str.split()
    names2 = str.split(",")
    print(names2[0][len(names[0])])
    if len(names) == 2:
        return(names[1], names[0])
    elif names2[0][len(names[0])] == ",":
        surname = names2.pop(0)
        print(surname)
        first_names = " ".join(names2)
        first_names = first_names[1:len(first_names)]
        return(surname, first_names)
    elif len(names) == 3:
        surname = names.pop(len(names)-1)
        first_names = " ".join(names)
        print(surname)
        return(surname, first_names)

def extract_authors(str):
    return 0


extract_author("kenneth justin pearson")