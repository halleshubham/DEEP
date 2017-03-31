#-*- coding: utf-8 -*-
import sys
import codecs
import re
import os
from numeric_convert import num_convert
from grammer import parser1

num1 = {u'१': '1', u'२': '2', u'३': '3', u'४': '4', u'५': '5', u'६': '6', u'७': '7', u'८': '8', u'९': '9', u'०': '0'}

v = open('output.txt','r')

f = open('input1.txt', 'w')
num_lines = sum(1 for line in open('output.txt'))

for j in range(0, num_lines):
    string_in = v.readline().rstrip()
    if string_in.isdigit():
        for i in range(len(string_in)):
            for val in num1:
                if (string_in[i] == num1[val]):
                    f.write(val.encode('utf-8').rstrip("\n"))
        print >> f, "\n"

    else:

        print >> f, string_in.rstrip("\n")