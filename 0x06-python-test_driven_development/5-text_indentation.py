#!/usr/bin/python3
def text_indentation(text):
    '''
    This is the 5-text_indentation module
    This function that prints a text with 2 new lines
    after each of those characters: ., ? and :
    There should be no space at the beginning or
     at the end of each printed line
    text must be a string, otherwise raise a TypeError exception
    with the message text must be a string
    '''
    if(not isinstance(text, str) or text is None):
        raise TypeError("text must be a string")
    txt1 = text.replace('.', '.\n\n')
    txt1 = txt1.replace('?', '?\n\n')
    txt1 = txt1.replace(':', ':\n\n')
    print("\n".join([txt2.strip() for txt2 in txt1.split("\n")]), end="")
