import re

string = input()
pattern = re.compile(r'^([^L][^R])*[^L]?$')
if pattern.match(string):
    print("Yes")
else:
    print("No")

# def test_入力例1():
#     assert answer("RUDLUDR") == "Yes"
#
# def test_入力例2():
#     assert answer("DULL") == "No"
#
# def test_入力例3():
#     assert answer("UUUUUUUUUUUUUUU") == "Yes"
#
# def test_入力例4():
#     assert answer("ULURU") == "No"
#
# def test_入力例5():
#     assert answer("RDULULDURURLRDULRLR") == "Yes"
