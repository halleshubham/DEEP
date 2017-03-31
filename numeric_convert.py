#-*- coding: utf-8 -*-

import sys
import codecs



#num_in = raw_input("Enter mar number")
class num_convert():
    num = {1: u'१', 2: u'२', 3: u'३', 4: u'४', 5: u'५', 6: u'६', 7: u'७', 8: u'८', 9: u'९', 0: u'०'}

    def num_equal(self, num_in):
        number = 0

        #print num_in[0]
        s = []
        '''
        for i in range(0,len(num_in)/3):
            v =  num_in[0+i*3] + num_in[1+i*3] + num_in[2+i*3]
            s.append(v)
        for k in range(0,len(s)):
            for val in self.num:
                if s[k] == self.num[val]:
                    number= number*10 + val
'''
        for i in range(len(num_in)):
            v = num_in[i]
            s.append(v)
        for k in range(0, len(s)):
            for val in self.num:
                if s[k] == self.num[val]:
                    number = number * 10 + val
        return number