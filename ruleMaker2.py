# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:58:07 2018

@author: peter
"""
import nltk


#useful for printing out trees; change index below
#my_corpus = nltk.corpus.BracketParseCorpusReader("C:/Users/peter/Desktop/CompLing_Project", ['qtreebank.txt'])
#print(my_corpus.parsed_sents()[0])

allrules = []

qtreebank = open("C:/Users/peter/Desktop/CompLing_Project/qtreebank.txt", 'r')


#executes all the functions and returns the grammar
def main():
    global allrules
    #maingrammar = ''''''
    x = qtreebank.readline()
    #while there are more parsed_sents
    while (x != ""):
        #makes the parsed_sent a list for easier manipulation
        line = nltk.re.findall(r'[\w]+|\(|\)|[,.:!?]', x)
        initial = initRules(line)
        allrules.extend(composeRules(initial))

     #next two for loops just eliminate redundant lines
    for y in range(0, len(allrules)):
        allrules[y] = ' '.join(allrules[y])
    allrules = set(allrules)
    allrules2 = []
    for y in allrules:
        y  = y.split(' ')
        allrules2.append(y)
    #allrules = set(allrules)
    allrules = allrules2
    print(allrules)
    x = qtreebank.readline()




#searches through each parsed sentence and creates lists of tuples of pseudorules
#these rules are all unary, and binary rules must be composed by composeRules
# pseudorule example: NP -> Det N comes out as NP -> Det and NP -> N
def initRules(listline):
    #makes listlines a list of lists, only so elements are not primitive data-type later
    for x in range(0, len(listline)):
        listline[x] = [listline[x]]
    #print(listline)

    #basic algorithm: new tags are placed in symbols, and index goes back
    #and forth thru symbols based off tree depth (determined by parenthesis)
    symbols = []
    index = -2
    x = 0
    prerules = []
    try:
        while x < len(listline):
            if listline[x][0] == '(':
                index+= 1
            elif listline[x][0] == ')':
                index -= 1
                #removes tag because we have left that tag's depth
                if len(symbols) != 0:
                    symbols.pop()
            elif len(symbols) != 0:
                symbols.append(listline[x])
                #special case for terminal nodes since qtreebank syntax differs here
                if listline[x + 1][0] != ')' and listline[x + 1][0] != '(' :
                    prerules.append((symbols[index], listline[x]))
                    prerules.append((listline[x], listline[x + 1]))
                    x += 1
                else:
                    prerules.append((symbols[index], listline[x]))
            else:
                symbols.append(listline[x])
            x+= 1
    #a few sentences error, I think due to weird puncuation or maybe deeper algorithm error
    # This skips them.
    except IndexError:
        print("Index Error!!")
        return 0
    return prerules


#creates binary rules out of pseudo-rule data, and returns list of rules derived from the sentence
def composeRules(initrules):
    grammar = []
    if initrules == 0:
        return ''
    #print(initrules)
    removelist = []
    #this loop composes binary rules
    for x in range(0, len(initrules)):
        composed = [initrules[x][0][0], initrules[x][1][0]]
        binaryrule = False
        for y in range(x+1, len(initrules)):
            #this creates the binary rule if antecedent of two pseudo rules are the same
            if initrules[x][0] is initrules[y][0]:
                composed.append(initrules[y][1][0])
                removelist.append(initrules[x])
                removelist.append(initrules[y])
                binaryrule = True
        if binaryrule:
            grammar.append(composed)

    #removes binary rules since they've been added already,
    for y in removelist:
        #print("this is y: ", y)
        try:
            initrules.remove(y)
        except:
            print("can't remove that for some reason")

    #returns unary rules; these are "left over"
    for x in initrules:
        grammar.append([x[0][0] , x[1][0]])

    return grammar

#used for formatting rules
def formatRules(rule):
    finalrule = ""
    finalrule = "\n" + rule[0] + " -> " + rule[1]
    if len(rule) != 2:
        finalrule += " " + rule[2]
    return finalrule


main()
