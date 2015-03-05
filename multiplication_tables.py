## multiplication_tables.py
## Challenge #23

for i in range(1,13):
    a = ''
    for j in range(1,13):
        a += str(i*j).rjust(4)
    print a
