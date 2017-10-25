#-*- coding=utf8 -*-
from pinyin import PinYin

if __name__ == "__main__":
    
    test = PinYin()
    test.load_word()
    string = "经查白文斌手机号码"
    print "out: %s" % str(test.hanzi2pinyin(string=string))
