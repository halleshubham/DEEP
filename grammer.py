#-*- coding: UTF-8 -*-
import sys, locale, codecs, re
from pyparsing import *
from keyword_list import mar_variable

# Code for marathi-print "marathiString"
class parser1():
    fstring = {}
    def parse(self, tok):

        m = mar_variable()
        alphas = u''.join(unichr(x) for x in xrange(0x0900, 0x0960))
        nums = u''.join(unichr(x) for x in xrange(0x0966, 0x0970))
        number = Word(nums)
        plus = Literal("+")
        minus = Literal("-")
        mult = Literal("*")
        div = Literal("/")
        plusorminus = Literal('+') | Literal('-')
        integer = Combine(Optional(plusorminus) + number)

        printn = (Optional(Literal("-"))) + (Word(alphas) | Word(nums)) + ZeroOrMore((Literal("+") | Literal("-") | Literal("/") | Literal("*") | Literal("%")) + (Word(alphas) | Word(nums)))

        #print num
        def expr():
            # for normal expressions
            pattern_print = Word(alphas) + "=" + (Optional(Literal("-"))) + (Word(alphas) | Word(nums)) + ZeroOrMore(
                        (Literal("+") | Literal("-") | Literal("/") | Literal("*") | Literal("%")) + (Word(alphas) | Word(nums)))
            self.fstring = pattern_print.parseString(tok)

        #printn = (Optional(Literal("-"))) + (Word(alphas) | Word(nums)) + ZeroOrMore((Literal("+") | Literal("-") | Literal("/") | Literal("*") | Literal("%")) + (Word(alphas) | Word(nums)))

        def print_func():
            # for print function
            pattern_print = Word(alphas) + (printn ^ QuotedString('"')) + Optional((plus ^ minus ^ mult ^ div)) + Optional(
                            Word(alphas))
            self.fstring = pattern_print.parseString(tok)


        def for_loop():
            # for for loop
            pattern_for = Word(alphas) + Word(alphas) + u'\u0906\u0924' + u'\u092e\u0927\u094d\u092f\u0947' + "(" + (
                            number ^ (Word(alphas) + "(" + Word(alphas) + ")")) + Optional(",") + Optional(
                            (number ^ (Word(alphas) + "(" + Word(alphas) + ")"))) + ")" + ":"
            self.fstring = pattern_for.parseString(tok)

        def while_loop():
            # for while loop
            pattern_while = Word(alphas) + "(" + (Word(alphas) ^ number) + ZeroOrMore((Word("<>") ^ "==" ^ "!=" ^ "<=" ^ ">=") + Optional(Word(alphas)^Word(nums)^printn) + Optional(u'आणि')) +  ")" + ":"
            self.fstring = pattern_while.parseString(tok)

        def if_cond():
            # for if condition
            pattern_if = Word(alphas) + "(" + Word(alphas) + ZeroOrMore((Word("<>") ^ "==" ^ "!=" ^ "<=" ^ ">=" ^ "=" ^ Literal("+") ^ Literal("-") ^ Literal("/") ^ Literal("*") ^ Literal("%")) + Optional(Word(alphas) ^ Word(nums) ^ printn)) + ")" + ":"
            self.fstring = pattern_if.parseString(tok)

        def elif_cond():
            # for elif condition
            pattern_elif = Word(alphas) + "(" + Word(alphas) + ZeroOrMore((Word("<>") ^ "==" ^ "!=" ^ "<=" ^ ">=" ^ "=" ^ Literal("+") ^ Literal("-") ^ Literal("/") ^ Literal("*") ^ Literal("%")) + Optional(Word(alphas) ^ Word(nums) ^ printn)) + ")" + ":"
            self.fstring = pattern_elif.parseString(tok)

        def else_cond():
            # for else
            pattern_else = Word(alphas) + ":"
            self.fstring =  pattern_else.parseString(tok)


        #RaWInput Ke liye likha toh hai, par dont know whether working or not..

        def rawIn():
            pattern_rawin = Word(alphas)+ "=" + Word(alphas) + "(" + QuotedString('"') +")"
            self.fstring = pattern_rawin.parseString(tok)
            raw = open('raw.txt','w+')
            #We had to do this because the code was not working, actually was not returning all the items, couldn't figure out why..
            a = u''+self.fstring[4]
            print >>raw, a.encode('utf-8')

        def rawInN():
            pattern_rawin = Word(alphas)+ "=" + Word(alphas) + "(" + QuotedString('"') +")"
            self.fstring = pattern_rawin.parseString(tok)
            raw = open('raw.txt','w+')
            #We had to do this because the code was not working, actually was not returning all the items, couldn't figure out why..
            a = u''+self.fstring[4]
            print >>raw, a.encode('utf-8')


        if (len(tok) >= 4):
            if (tok[0]+tok[1]+tok[2]+tok[3] == u"छापा"):
                print_func()
            elif (tok[0]+tok[1]+tok[2]+tok[3] == u"साठी"):
                for_loop()

        if(len(tok)>=7):
            #if(tok[0]+tok[1]+tok[2]+tok[3]+tok[4]+tok[5]+tok[6]+tok[7] == u"जोपर्यंत"):
                #while_loop()
            if (tok[0] + tok[1] + tok[2] + tok[3] + tok[4] + tok[5] + tok[6] == u"किंवाजर"):
                elif_cond()
        if(len(tok)>=6):
            if (tok[0] + tok[1] + tok[2] + tok[3] + tok[4] + tok[5] == u"नाहीतर"):
               else_cond()

        if(len(tok)>=10):
            if (tok[4] + tok[5] + tok[6] + tok[7] + tok[8] + tok[9] == u"माहिती"):
               rawIn()

        if (len(tok) >= 11):
            if (tok[4] + tok[5] + tok[6] + tok[7] + tok[8] + tok[9] + tok[10] == u"माहितीक"):
               rawInN()
        if(len(tok)>=2):
            if (tok[0]+tok[1] == u"जर"):
                if_cond()

        if(len(tok) >= 1):
            if m.keyword.has_key(tok[0]):
                expr()





        '''
                        if(len(tok)>=10):
                            if( tok[0] + tok[1] + tok[2] + tok[3] + tok[4] + tok[5] + tok[6]+tok[7]+tok[8]+tok[9]+tok[10]==u"कच्चीमाहिती"):
                                rawIn()
                        '''

        #!!! Work on Indentation !!!
        # elif (tok[0]+tok[1]+tok[2]+tok[3] == u"    ")
        #    indent_p()