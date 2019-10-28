def fact_tail_rec(n, product = 1):
    # Base case
    if n == 0:
        return product
    # recursive call
    else:
        return fact_tail_rec(n-1, product * n)

print(fact_tail_rec(0))
print(fact_tail_rec(1))
print(fact_tail_rec(2))
print(fact_tail_rec(3))
print(fact_tail_rec(4))
print(fact_tail_rec(5))
