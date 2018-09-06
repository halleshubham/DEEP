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
        alphanums = u''.join(unichr(x) for x in xrange(0x0900, 0x0970))
        number = Word(nums)
        plus = Literal("+")
        minus = Literal("-")
        mult = Literal("*")
        div = Literal("/")
        plusorminus = Literal('+') ^ Literal('-')
        integer = Combine(Optional(plusorminus) + number)

        # for array decl
        pattern_array = Word(alphas) + Literal("=") + Literal("[") + ZeroOrMore(Word(nums)) + ZeroOrMore(
            Literal(",") + Word(nums)) + Literal("]")

        array_access = Word(alphas) + Optional(Literal("[") + (Word(alphas) ^ Word(nums)) + Literal("]"))

        #printn = (array_access ^ (Optional(Literal("-"))) + (Word(alphas) ^ Word(nums)) + ZeroOrMore((Literal("+") ^ Literal("-") ^
        #                        Literal("/") ^ Literal("*")^ Literal("%")) + (Word(alphas)^Word(nums))))


        # for normal expressions
        pattern_expr = Word(alphas) + "=" + (Optional(Literal("-"))) + (Word(alphas) ^ Word(nums)) + ZeroOrMore(
                        (Literal("+") ^ Literal("-") ^ Literal("/") ^ Literal("*") ^ Literal("%")) + (Word(alphas) ^ Word(nums)))


        printn = (Optional(Literal("-"))) + (Word(alphas) ^ Word(nums)) + ZeroOrMore((Literal("+") ^ Literal("-") ^ Literal("/") ^ Literal("*") ^ Literal("%")) + (Word(alphas) ^ Word(nums)))


        # for print function
        #expp = OneOrMore(Literal("+") + Word(alphas))
        #pattern_print = u"छापा" + (expp^QuotedString('"'))
        pattern_print = u"छापा" + (printn ^ QuotedString('"')) #+ ZeroOrMore(
                        #(Literal("+") ^ Literal("-") ^ Literal("/") ^ Literal("*") ^ Literal("%")) + (Word(alphas) ^ Word(nums)))


        # for for loop
        pattern_for = u"साठी" + Word(alphas) + u'\u0906\u0924' + u'\u092e\u0927\u094d\u092f\u0947' + "(" + (
            number ^ (Word(alphas) )) + Optional(",") + Optional(
            (number ^ (Word(alphas) + (Literal("+") ^ Literal("-") ^ Literal("/") ^ Literal("*") ^ Literal("%")) + number ^ (Word(alphas))))) + Literal(")") + Literal(":")
        #pattern_for = u"साठी" + Word(alphas) + u'\u0906\u0924' + u'\u092e\u0927\u094d\u092f\u0947' + "(" + (
         #                   number ^ (Word(alphas) + "(" + Word(alphas) + ")")) + Optional(",") + Optional(
          #                  (number ^ (Word(alphas) + "(" + Word(alphas) + ")"))) + Literal(")") + Literal(":")



        # for while loop
        pattern_while = u"जोपर्यंत" + Literal("(") + (Word(alphas) ^ number) + ZeroOrMore((Word("<>") ^ "==" ^ "!=" ^ "<=" ^ ">=") +
                                                                                          Optional(Word(alphas)^Word(nums)^printn) +
                                                                                          Optional(u'आणि')) +  Literal(")") + Literal(":")

        # for if condition
        pattern_if = u"जर" + Literal("(") + Word(alphas) + ZeroOrMore((Word("<>") ^ "==" ^ "!=" ^ "<=" ^ ">=" ^ "=" ^ Literal("+") ^
                                                                       Literal("-") ^ Literal("/") ^ Literal("*") ^ Literal("%")) +
                                                                      Optional(Word(alphas) ^ Word(nums) ^ printn)) + Literal(")") + Literal(":")


        # for elif condition
        pattern_elif = u"किंवाजर" + Literal("(") + Word(alphas) + ZeroOrMore((Word("<>") ^ "==" ^ "!=" ^ "<=" ^ ">=" ^ "=" ^ Literal("+") ^
                                                                              Literal("-") ^ Literal("/") ^ Literal("*") ^ Literal("%")) +
                                                                             Optional(Word(alphas) ^ Word(nums) ^ printn)) + Literal(")") + Literal(":")


        # for else
        pattern_else = u"नाहीतर" + Literal(":")

        # RaWInput
        pattern_rawin = Word(alphas) + Literal("=") + u"माहिती" + Literal("(") + QuotedString('"') + Literal(")")

        # typecasted raw_input
        typecastint = u"संख्या" + Literal("(") + (u"माहिती" + Literal("(") + Literal(")")) + Literal(")")

        typecaststring = u"ओळ" + Optional(Literal("(") + number + Literal(")")) + Optional(
            Literal("(") + u"माहिती" + Literal("(") + Literal(")")) + Literal(")")

        # RAWInput for numbers
        pattern_typecast = Word(alphas) + Literal("=") + (typecastint ^ typecaststring)

        # raw = open('raw.txt','w+')
        # We had to do this because the code was not working, actually was not returning all the items, couldn't figure out why..
        # a = u''+self.fstring[4]
        # print >>raw, a.encode('utf-8')

        statement = (pattern_print ^ pattern_rawin ^ pattern_typecast ^ typecastint ^
                     typecaststring ^ pattern_expr ^ pattern_elif ^ pattern_else ^
                     pattern_for ^ pattern_if ^ pattern_while ^ pattern_array) +StringEnd()
        # for indent
        pattern_indent = ZeroOrMore(u"    ")
        statementWithIndent = pattern_indent + statement

        self.fstring = statement.parseString(tok)
