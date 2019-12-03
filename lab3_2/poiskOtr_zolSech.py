from sympy import diff, symbols, cos, sin
import math
l = symbols('l')

def getInterval1(func, x0, h):
    a = 0
    b = 0 #bounds
    xk = []
    fxk = []
    k = 1
    step = 2
    while True:
        #step 1,2
        if step == 2:
            if(func.subs({l:x0}) > func.subs({l:x0 + h})):
            #if f(x0) > f(x0 + h):
                a = x0
                xk.append(x0 + h)
                fxk.append(func.subs({l:x0 + h}))
                k = 2
                step = 4
            else:
                step = 3

        #step 3
        if step == 3:
            if(func.subs({l:x0 - h}) >= func.subs({l:x0})):
            #if f(x0 - h) >= f(x0):
                a = x0 - h
                b = x0 + h
                step = 6
            else:
                b = x0
                xk.append(x0 - h)
                fxk.append(func.subs({l:x0 - h}))
                h = -h
                k = 2
                step = 4

        #step 4
        if step == 4:
            xk.append(x0 + (2 ** (k - 1)) * h)
            fxk.append(func.subs({l:xk[k - 1]}))
            step = 5

        #step 5
        if step == 5:
            if fxk[k - 1] >= fxk[k - 2]:
                if h > 0:
                    b = xk[k - 1]
                else:
                    a = xk[k - 1]
                step = 6
            else:
                if h > 0:
                    a = xk[k - 2]
                else:
                    b = xk[k - 2]
                k += 1
                step = 4
        #step 6
        if step == 6:
            return a,b



def getInterval(func,x0,h):
    a = 0
    b = 0
    k = 0
    arrX = []
    #for i in range(0,500):
    #    arrX.append(0)
    #arrX[0] = x0
    arrX.append(x0)
    if(func.subs({l:x0}) > func.subs({l:x0 + h})):
        #a = x_1
        a=x0
        #arrX[1] = (x0 + h)
        arrX.append(x0 + h)
        k = 2
    else:
        if(func.subs({l:x0 - h}) >= func.subs({l:x0})):
            a = x0 - h
            b = x0 + h
            return a,b
        else :
            b = x0
            #arrX[1] = (x0 - h)
            arrX.append(x0 - h)
            h = -h
            k = 2

    while 1:
        #print(k)
        #arrX[k] = x0 + (2 ** (k - 1)) * h
        arrX.append(int(x0 + (2 ** (k - 1)) * h))
        if func.subs({l:arrX[k - 1]}) <= func.subs({l:arrX[k]}):
            if (h > 0):
                b = arrX[k]
            else:
                a = arrX[k]
            return a,b
        else:
            if h > 0:
                a = arrX[k - 1]
            else:
                b = arrX[k - 1]
            k+=1



def goldMethod(func,a,b):
    eps = 1e-3
    tay = 1.618
    res = 0
    f1 = 0
    f2 = 0
    x1 = a + (b - a) / (tay * tay)
    x2 = a + (b - a) / tay
    f1 = func.subs({l:x1})
    f2 = func.subs({l:x2})
    while 1:
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = func.subs({l:x2})
            x2 = a + (b - a) / tay
            f2 = func.subs({l:x2})
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (b - a) / (tay * tay)
            f1 = func.subs({l:x1})

        if math.fabs(b-a)<eps:
            return (a + b) / 2

  