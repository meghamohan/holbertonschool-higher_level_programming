#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return ([replace if ele is search else ele for ele in my_list])
