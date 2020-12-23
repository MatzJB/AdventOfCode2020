
def return_terms_of_sum(elts, sum):
    for elt1 in elts:
        for elt2 in elts:
            if elt1 + elt2 == sum:
                return (elt1, elt2)
sum = 2020

with open('input.txt') as f:
    tmp = f.readlines()

elts = [int(elt.strip()) for elt in tmp]

(a,b) = return_terms_of_sum(elts, sum)
print(f'product: {a*b}')