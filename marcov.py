#!/user/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import random
import MeCab

def wakati(text):
    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    result = m.rstrip(" \n").split(" ")
    return result

if __name__ == "__main__":
    filename = "test.txt"
    src = open(filename, "r").read()
    wordlist = wakati(src)
    #print(wordlist) #wordlist 分かち書きした文章のリスト
    # Create table of Markov Chain
    markov = {}
    w1 = ""
    w2 = ""
    for word in wordlist:
        if w1 and w2:
            if (w1, w2) not in markov:
                markov[(w1, w2)] = [] 
            markov[(w1, w2)].append(word)
        w1, w2 = w2, word

# Generate Sentence
    count = 0
    sentence = ""
    w1, w2  = random.choice(list(markov.keys()))
    # print((w1,w2))
    # print(len(wordlist)) #18
    #while count < len(wordlist):
    while count < 50:
        #keyがmarkovのValue中に入ってない時 抜ける
        if ((w1, w2) in markov) == False:
            #print("inner")
            break
        else:
            tmp = random.choice(markov[(w1, w2)])
            sentence += tmp
            w1, w2 = w2, tmp
            count += 1

    print(sentence)
