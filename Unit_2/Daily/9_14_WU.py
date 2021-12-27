# part 1
k = 1
a = 2
t1 = 5
t2 = 8
l = 3

q = (k*a*(t1-t2))/l
print(q)
# part 2
m = int(input("Enter an integer> "))
n = int(input("Enter an integer> "))
m = m + 5
n = 3 * n
print("m =", m, "\nn =", n)

for i in range(2, 41, 2):
    if i % 40 != 0:
        print(i, end=", ")
    else:
        print(i)
