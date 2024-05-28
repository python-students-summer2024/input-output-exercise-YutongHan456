"""
A little assignment to practice printing text 
output to the Python command line.
Do not run this file... run main.py instead.
"""


def print_with_line_break():
    """
    Prints out the text, 'Hello world!' with a line break at the end
    """
    # write your code here
    print("Hello world!\n")


def print_without_line_break():
    """
    Prints out the text, 'Hello world!' without a line break at the end
    """
    # write your code here
    print("Hello world!")


def print_with_separator_dash_and_with_line_break():
    """
    Prints out the following words, with dashes "-" between them
    and a line break at the end:
    "Twas", "brillig", "and", "the", "slithy", "toves"
    """
    # write your code here
    # you must supply each word as a separate argument to the print() function
    print("Twas","-","brillig","-","and","-","the","-","slithy","-","toves\n")


def print_with_separator_dash_and_without_line_break():
    """
    Prints out the following words, with dashes "-" between them
    and without a line break at the end:
    "Twas", "brillig", "and", "the", "slithy", "toves"
    """
    # write your code here
    # you must supply each word as a separate argument to the print() function
    twas_print = "Twas"
    brillig_print = "brillig"
    and_print = "and"
    the_print = "the"
    slithy_print = "slithy"
    toves_print = "toves"
    symble_print = "-"
    print(twas_print,symble_print,brillig_print,symble_print,and_print,symble_print,the_print,symble_print,slithy_print,symble_print,toves_print)

