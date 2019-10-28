def fact_lin_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_lin_rec(n-1)

print(fact_lin_rec(0))
print(fact_lin_rec(1))
print(fact_lin_rec(2))
print(fact_lin_rec(3))
print(fact_lin_rec(4))
print(fact_lin_rec(5))
