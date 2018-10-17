def swap_case(s):
    new_string =''
    for i in s:
        if i.islower() ==True:
            up =i.upper()
            new_string= new_string+up
        elif i.isupper()==True:
            low =i.lower()
            new_string= new_string+low
        else:
            new_string= new_string+i




    return new_string