# -*- coding: utf-8 -*-
import textwrap
from StringIO import StringIO
import sys
import codecs
import re
import os

import pyparsing
from keyword_convert import keyword_con
from grammar import parser1
from output import execution
import subprocess


def getMarNum(n):
    num1 = {u'१': '1', u'२': '2', u'३': '3', u'४': '4', u'५': '5', u'६': '6', u'७': '7', u'८': '8', u'९': '9',
            u'०': '0'}
    number = ""
    for i in range(len(n)):
        for val in num1:
            if (n[i] == num1[val]):
                  number = number + val.encode('utf-8')
    return number


os.remove('out.py')

v = open('input.txt', 'r')
f = open('out.py', 'w')
#e =  open('input2.txt','w+')

f.write("#-*- coding: utf-8 -*-\n")
num_lines = sum(1 for line in open('input.txt'))

for j in range(0, num_lines):
    string_in = v.readline().decode('utf-8')

    #here

    if (len(string_in) >= 4):
        if (string_in[0] + string_in[1] + string_in[2] + string_in[3] == '    '):
            print >> f, '\n    ',

    if (len(string_in) >= 8):
        if (string_in[4] + string_in[5] + string_in[6] + string_in[7] == '    '):
            print >> f, '    ',

    if (len(string_in) >= 12):
        if (string_in[8] + string_in[9] + string_in[10] + string_in[11] == '    '):
            print >> f, '    ',

    if (len(string_in) >= 16):
        if (string_in[12] + string_in[13] + string_in[14] + string_in[15] == '    '):
            print >> f, '    ',

    string_in = string_in.lstrip()

    try :
        par = parser1()
        par.parse(string_in)
    except pyparsing.ParseException :
        print "चुकीची मांडणी - ओळ क्रमांक: "+ str(getMarNum(str(j+1)))
    #print par.fstring
    #if(par.fstring[2] == '\u092e\u093e\u0939\u093f\u0924\u0940'):
    #This is a LOL code for getting the rawInpute
    #raw = open('raw.txt','r')
    #rawl = raw.readline().decode('utf-8')
    #rawl = rawl.rstrip("\n")
    i = 0

    key = keyword_con()

    for i in range(len(par.fstring)):
        # print string_in
        """if (len(string_in) >= 6):
            if (string_in[5] == '"'):
                print >> f, key.eng_equal(par.fstring[0]),

                print >> f, '"',
                ap = u' ' + par.fstring[1]
                ap = ap.encode('utf-8')
                print >> f, ap,
                print >> f, '"'
                break
        if (len(string_in) >= 12):
            if (string_in[11] == '"'):

                print >> f, key.eng_equal(par.fstring[0]),
                print >> f, key.eng_equal(par.fstring[1]),
                print >> f, key.eng_equal(par.fstring[2]),
                print >> f, '(',
                print >> f, '"',

                print >> f, rawl.encode('utf-8'),
                print >> f, '\\n"',
                print >> f, ')'
                break

        if (len(string_in) >= 13):
            if (string_in[12] == '"'):
                        print >> f, key.eng_equal(par.fstring[0]),
                        print >> f, key.eng_equal(par.fstring[1]),
                        print >> f, key.eng_equal(par.fstring[2]),
                        print >> f, '(',
                        print >> f, '"',

                        print >> f, rawl.encode('utf-8'),
                        print >> f, '\\n"',
                        print >> f, '))'
                        break
                # if tok[i] == find.eng_equal(tok[i]):
        """
        # print key.eng_equal(par.fstring[i]),

        if(type(key.eng_equal(par.fstring[i])) == int):
            print >> f, key.eng_equal(par.fstring[i]),
        else:
            print >> f, key.eng_equal(par.fstring[i]).encode('utf-8'),
    print >> f, '\n'

"""here

"""