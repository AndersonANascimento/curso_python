
def maiorElem(l=[]):
    return max(l)

def menorElem(l=[]):
    return min(l)

def somatorio(l=[]):
    return sum(l)

def frequencia(x, l=[]):
    return l.count(x)

def inverte(l=[]):
    l.reverse()
    return l

l = [4, -2, 5, 0.9, 1, 5, 5]
l2 = l[:]


print maiorElem(l)
print menorElem(l)
print somatorio(l)
print frequencia(5, l)
print inverte(l)
print l2
