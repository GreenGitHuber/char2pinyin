# -*- coding:utf-8 -*-
# encoding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from pinyin import PinYin

if __name__ == "__main__":
    
    test = PinYin()
    test.load_word()
    raw = open(r"../zhaospam_af_jieba.txt")
    line = raw.readline()
    str = ''
    while line:
        string = test.hanzi2pinyin_split(string=line,split=" ")
        str += string
        line = raw.readline()
    raw.close()
    f=open("zhaospam_to_pinyin.txt",'wb')
    f.write(str)
    f.close()
    # pinyin_str = test.hanzi2pinyin_split(string=string, split=" ")
    # joint_str = string pinyin_str
    # print "out: %s" % str(test.hanzi2pinyin(string=string))
    # print "out: %s" % test.hanzi2pinyin_split(string=string, split="-")
    # print joint_str
    # print string
