s = "RUDLUDR"  # Yes
# s = "DULL" # No
# s = "UUUUUUUUUUUUUUU" # Yes
# s = "ULURU" # No
# s = "RDULULDURURLRDULRLR" # Yes

odd = [R, U, D]
even = [L, U, D]

if (a + b) % 3 == 0 or b % 3 == 0 or a % 3 == 0:
    print("Yes")
else:
    print("No")
