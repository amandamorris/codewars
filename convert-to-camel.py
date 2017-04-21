def to_camel_case(text):
    """Converts a string to camel case, returns the converted string
        # returns "theStealthWarrior"
        to_camel_case("the-stealth-warrior") 

        # returns "TheStealthWarrior"
        to_camel_case("The_Stealth_Warrior")
"""
    
    if not text:
        return ""

    newstring = text[0]  # capitalization preserved for first char
    prec_dash = False  # keep track of whether the preceding char was a dash
    
    for char in text[1:]:  # iterate through the rest of the string
        if char == "-" or char == "_":  # if dash:
            prec_dash = True
            continue  # don't add char, go to next iteration of loop
        elif prec_dash:  # if prev char is dash, capitalize next char
            newstring += char.upper()
            prec_dash = False
        else:
            newstring += char.lower()  # otherwise lowercase next char
    return newstring
