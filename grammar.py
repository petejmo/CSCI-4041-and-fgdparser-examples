# -*- coding: utf-8 -*-
import nltk

#gram = open('grammar.txt', 'r')

#tree_grammar = nltk.CFG.fromstring(gram)

#parser = nltk.ChartParser(tree_grammar, nltk.parse.chart.BU_STRATEGY)

# def process(sent ):
#    tok_sent = list(sent.split())
#    last_parse = None
#    for p in parser.parse(tok_sent):
#        last_parse = p
#    return last_parse

tree_grammar = nltk.CFG.fromstring(
                                   """
                                   S -> WP NP VP | NP VP | WP VP PP | WP Prep |WP NP VP PP | WP VP
                                   WP -> Wh AuxP | Wh T | Wh AuxP T | Wh T AuxP
                                   Wh -> "what" | "What" | "which" | "Who" | "whom" | "who" | "Which"
                                   AuxP -> Aux | Aux Aux
                                   Aux -> "do" | "did" | "is" | "will" | "have" | "be" | "does" | "are"
                                   NP -> PRO | Det N | Adj N | N PP | N | POSS AdjP | POSS N
                                   VP -> Vi | Vt NP | Vt T | Prep Vi | Vt T Adv | Vt PP | Vt PRO \
                                   | Vt T AdvP | VP ConJ VP | Vt T AdjP | Vt T NP
                                   Vi -> "walk" | "walks" | "arriving" | "killed"
                                   Vt -> "see" | "sees" | "know" | "knows" | "want" | "bury" | "find" \
                                   | "wowed" | "reading" | "eat" | "download" | "install" | "drink" \
                                   | "seen" | "carry" | "teaches" | "driving" | "wrote" \
                                   | "kill" | "love" | "cherish" | "resent" | "harass" | "made" \
                                   | "drive" | "like" | "wearing"
                                   AdvP -> Adv VP
                                   Adv -> "there" | "while" | "since" | "now"
                                   AdjP -> Adj NP
                                   Adj -> "favorite" | "every"
                                   Det -> "the" | "a"
                                   PP -> Prep NP | Prep Aux T | T Prep
                                   Prep -> "to" | "about" | "while" | "that" | "this" | "inside"
                                   N -> "woman" | "women" | "man" | "men" | "dog" | "trip" | "john" \
                                   | "book" | "scientist" | "morning" | "class" | "train" \
                                   | "jenny" | "amanda" | "mayor" | "kids" | "glasses" | "uncle" \
                                   | "cat" | "tonight"
                                   T -> "t"
                                   PRO -> "I" | "me" | "he" | "him" | "she" | "her" | "they" | "them" \
                                   | "you"
                                   POSS -> "your"
                                   ConJ -> "and" | "or"
                                   """
                                   )

parser = nltk.ChartParser(tree_grammar, nltk.parse.chart.BU_STRATEGY)

def process(sent):
    tok_sent = list(sent.split())
    last_parse = None
    for p in parser.parse(tok_sent):
        last_parse = p
        print(p.pretty_print())
