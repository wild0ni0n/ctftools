from itertools import chain, product
import hashlib
import re

charset = "abcdefghijklmnopqrstuvwxyz1234567890"
maxlength = 4

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


regr = re.compile("hogehoge")

for c in list(bruteforce(charset, maxlength)):
    h = hashlib.sha1(c.encode()).hexdigest()
    r = c + " " + h
    if(regr.search(h, 0)):
        r = r + "   BINGO!!!!!"
        print(r)
        exit()
    print(r)