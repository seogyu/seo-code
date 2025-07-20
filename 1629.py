A,B,C = map(int,input().split())
def recu(b):
    if b == 1:
        return A % C
    if b % 2 == 0:
        r = recu(b//2)
        return r * r % C
    else:
        r = recu(b//2)
        return r*r*A%C
print(recu(B))