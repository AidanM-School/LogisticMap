import numpy as np
import matplotlib.pyplot as plt

def f(x,r):
    return r*x*(1-x)

def logmap(x=.5,r=3.95,n=1000):
    xs=[]
    x = f(x, r)
    val=900
    while x not in xs and len(xs)<n:
        xs.append(x)
        x = f(x, r)
    if x in xs:
        val=xs.index(x)
    return xs[val:]

def rmap():
    rs = list(np.linspace(2,4,1000))
    xs=[]
    for r in rs:
        xs.append(logmap(r=r))
    return rs,xs

def main():
    rs,xs=rmap()
    for i,r in enumerate(rs):
        plt.scatter([r for x in xs[i]],xs[i],c='blue',s=.04)
    plt.show()

main()