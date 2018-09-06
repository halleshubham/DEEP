#-*- coding: UTF-8 -*-
from numeric_convert import num_convert

class con():
    num = [u'१', u'२', u'३', u'४', u'५', u'६', u'७', u'८', u'९', u'०']
    def convertnum(self):
        n = num_convert()
        v = open('programMarathiInput.txt', 'r')
        f = open('programInput.txt', 'w+')

        num_lines = sum(1 for line in open('programMarathiInput.txt'))
        flag = 0
        for j in range(0, num_lines):
            key_in = v.readline().decode('utf-8')
            #print key_in
            for i in range(len(self.num)):
                if key_in[0] == self.num[i]:
                    flag = 1;
                    #print str(n.num_equal(key_in))
                    print >> f, str(n.num_equal(key_in))


            if(flag == 0):
                print >> f, key_in.encode('utf-8')
        #return "\"" + key_in + "\""

c = con()
c.convertnum()