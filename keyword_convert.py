#-*- coding: utf-8 -*-
from array import *
from pyparsing import Word
import sys
import codecs
import re
from keyword_list import mar_symbols
from keyword_list import mar_keyword, mar_builtin_method, mar_sys, mar_variable
from numeric_convert import num_convert
#key_in = raw_input("Enter mar number")


class keyword_con():
    def eng_equal(self,key_in):
        num = [u'१', u'२', u'३', u'४', u'५', u'६', u'७', u'८', u'९', u'०']
        #print num[0]
        k = mar_keyword()
        b = mar_builtin_method()
        n = num_convert()
        s = mar_sys()
        v = mar_variable()
        sy = mar_symbols()


        if  k.keyword.has_key(key_in):
            #print key_in
            return k.keyword[key_in]

        elif b.keyword.has_key(key_in):
            #print key_in
            return b.keyword[key_in]

        elif s.keyword.has_key(key_in):
            return s.keyword[key_in]

        elif v.keyword.has_key(key_in):
            return v.keyword[key_in]

        elif sy.keyword.has_key(key_in):
            return sy.keyword[key_in]

        else:
            #return ""
            for i in range(len(num)):
            #print key_in[0]
                if key_in[0] == num[i]:
                    return n.num_equal(key_in)




