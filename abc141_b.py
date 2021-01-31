# https://atcoder.jp/contests/abc141/submissions/19842912

import re

s = input()

p = re.compile(r'^([^L][^R])*[^L]?$')

if p.match(s):
    print("Yes")
else:
    print("No")
