#!/usr/bin/python3
# 5-text_indentation

"""A function that print empt line after . : ? and ,"""
def text_indentation(text):
    """Function print text separated by two empty line 
    printed after a .:?or , is detected
    args:
    size must be a str else, a TypeError is raised"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
