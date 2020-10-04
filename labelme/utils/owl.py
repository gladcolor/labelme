from owlready2 import *

import ast

# onto = get_ontology(r'K:\temp\pizza_ontology.owl')

owl_file = r'X:\My Drive\Research\StreetGraph\documents\street_ontology.owl'

def loadOWL(owl_file):
    return get_ontology(owl_file).load()


onto = loadOWL(owl_file)

def getTextAttribtes(class_name):
    # r = onto.search("*status_maintainance")
    res = []
    try:
        res = onto[class_name].range   # =[<class 'str'>, OneOf(['test', 'test1'])]
        res = str(res[-1])
        res = res.replace("OneOf(", '')
        res = res.replace(")", '')
        res = ast.literal_eval(res)
        return res
    except:
        print("Cannot find class name.")
        return res
# l = list(onto.data_properties())

def getDomains(class_name):
    # r = onto.search("*status_maintainance")
    res = []
    try:
        res = onto[class_name].domain    # callback list
        # res = str(res)
        # res = ast.literal_eval(res)

        res = [x.name for x in res]

        return res
    except:
        print("Cannot find class name.")
        return res

# class_name = "status_maintainance"
# r = getTextAttribtes(class_name)


class_name = "status_maintainance"
class_name = "color"
r = getDomains(class_name)
print(str(r))

r = getTextAttribtes(class_name)
print(str(r))

# l = onto.data_properties()
# print(onto['status_maintainance'].domain)
#
# r = onto['status_maintainance'].range
# str_result = r[1]
# print(str(r[1]))



# print(onto['status_maintainance'].range)