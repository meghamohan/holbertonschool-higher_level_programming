#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ArithmeticError:
        div ='None'
    finally:
        print("Inside result: {}".format(div))
    return div
        
