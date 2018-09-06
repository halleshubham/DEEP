#-*- coding: utf-8 -*-
import subprocess
from subprocess import *
from StringIO import StringIO
import sys
#def executePy(fileName):
    # type: (object, object) -> object

from numeric_convert import num_convert


class execution():

    def star(self):
        '''num = [u'१', u'२', u'३', u'४', u'५', u'६', u'७', u'८', u'९', u'०']
        n = num_convert()
        v = open('programMarathiInput.txt', 'r')
        f = open('programInput.txt', 'w')
        num_lines = sum(1 for line in open('programMarathiInput.txt'))

        for j in range(0, num_lines):
            string_in = v.readline().rstrip().decode('utf-8')
            for i in range(len(num)):
            #print key_in[0]
                if string_in[0] == num[i]:
                    print >> f, n.num_equal(string_in)'''

        with open("output.txt", "w+") as output:
            with open("programInput.txt","r+") as input:
                with open("errors.txt","w+") as error:
                    #try:
                        subprocess.call(["python", "./out.py"],stderr=error, stdin=input, stdout=output)
                    #except subprocess.CalledProcessError as cpe:
                        #print cpe.output