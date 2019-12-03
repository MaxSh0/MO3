from sympy import diff, symbols, cos, sin
from NewtonRafson import *
x1,x2,x3,x4,l, alph = symbols('x1 x2 x3 x4 l alph')
from poiskOtr_zolSech import getInterval,goldMethod
#func = diff((x + y) ** 2 + (x + z) ** 2 + l,x)
#print(func.subs({x:1,y:1,z:1,l:4}))
##result = 4*(x1-5)**2+(x2-6)**2
##print(diff(result,x1))
def main():
    countIteration =0
    print('Метод штрафных функций')
    print('Выберите нужную функцию...\n1. x1^2+x2^2\n2. x2^2+x2^2\n3. x1^2+x2^2\n4. 4/x1+9/x2+x1+x2\n')
    indexFunc = int(input())
    print('Введите координаты начальной точки:')
    curPoint = []
    points = []
    for i in range(0,2):
            curPoint.append(float(input('Введите координату Х' + str(i) + ':')))
    epsilon = float(input('Введите погрешность e:'))
    alpha = float(input('Введите alpha:'))
    betta = float(input('Введите betta:'))
    while 1:
        print(str(countIteration)+'я итерация:\n')
        print('текущая точка:\n'+str(curPoint))
        countIteration = countIteration+1
        points.append(curPoint)
        #penaltyFunc = getPenaltyFunc(indexFunc,curPoint)
        penaltyFunc = getP(indexFunc,curPoint)
        teta = getStartFunc(indexFunc) + alph*penaltyFunc
        #curPoint = gradMethod(teta.subs({alph:alpha}), curPoint, epsilon)
        curPoint = NR(teta.subs({alph:alpha}), curPoint, epsilon)
        valuePenalty = getPenaltyFunc(indexFunc,curPoint)
        if alpha* valuePenalty< epsilon:
            break
        alpha = alpha*betta
    print('\nОТВЕТ')
    print(curPoint)


def getPenaltyFunc(indexRestriction, curPoint):
    restrictions = getRestriction(indexRestriction)
    if(indexRestriction == 1):
        penaltyFunc= math.fabs(restrictions[0].subs({x1:curPoint[0], x2:curPoint[1]}))**2
    elif (indexRestriction ==2 ):
        penaltyFunc =max(0, restrictions[0].subs({x1:curPoint[0], x2:curPoint[1]}))**2+math.fabs(restrictions[1].subs({x1:curPoint[1], x2:curPoint[1]}))**2
    elif(indexRestriction ==3):
        penaltyFunc =max(0, restrictions[0].subs({x1:curPoint[0], x2:curPoint[1]}))**2+max(0, restrictions[1].subs({x1:curPoint[0], x2:curPoint[1]}))**2
    elif(indexRestriction ==4):
        penaltyFunc =max(0, restrictions[0].subs({x1:curPoint[0], x2:curPoint[1]}))**2+ max(0, restrictions[1].subs({x1:curPoint[0], x2:curPoint[1]}))**2+ max(0, restrictions[2].subs({x1:curPoint[0], x2:curPoint[1]}))**2
    return penaltyFunc

def getP(indexRestriction, curPoint):
    restrictions = getRestriction(indexRestriction)
    if(indexRestriction == 1):
        penaltyFunc= restrictions[0]**2
    elif (indexRestriction ==2 ):
        penaltyFunc =(restrictions[0]**2 if restrictions[0].subs({x1:curPoint[0], x2:curPoint[1]}) > 0 else 0) + restrictions[1]**2
    elif(indexRestriction ==3):
        penaltyFunc =(restrictions[0]**2 if restrictions[0].subs({x1:curPoint[0], x2:curPoint[1]}) > 0 else 0) + (restrictions[1]**2 if restrictions[1].subs({x1:curPoint[0], x2:curPoint[1]}) > 0 else 0)

    elif(indexRestriction ==4):
        penaltyFunc =(restrictions[0]**2 if restrictions[0].subs({x1:curPoint[0], x2:curPoint[1]}) > 0 else 0) + (restrictions[1]**2 if restrictions[1].subs({x1:curPoint[0], x2:curPoint[1]}) > 0 else 0) + (restrictions[2]**2 if restrictions[2].subs({x1:curPoint[0], x2:curPoint[1]}) > 0 else 0)
    return penaltyFunc


def getStartFunc(indexFunc):
    if (indexFunc == 1 or indexFunc == 2 or indexFunc == 3):
        result = x1**2+x2**2
    elif (indexFunc == 4):
        result = 4/x1+9/x2+x1+x2 
    return result

def getRestriction(indexRestriction):
    result = []
    if(indexRestriction == 1):
        result= [x1+x2-2]
    elif (indexRestriction ==2 ):
        result =[x2+x1-2,x1 - 1]
    elif(indexRestriction ==3):
        result =[x2+x1-2,1-x1]
    elif(indexRestriction ==4):
        result =[x1+x2-6,-x1,-x2]
    return result

def getValueFunc(func,point):
    if(len(point)==2):
        return func.subs({x1:point[0],x2:point[1]})
    if(len(point)==4):
        return func.subs({x1:point[0],x2:point[1],x3:point[2],x4:point[3]})

def gradMethod(func, startPoint, epsilon):
    print('---------------------------\nМетод градиентного спуска\n-------------------\n')
    #curPoint = []
    #for i in range(0,2):
    #        curPoint.append(float(input('Введите координату Х' + str(i) + ':')))
    valueGrad = [0,0]
    curPoint =startPoint
    countArgs =2
    countIteration =0
    points = []
    #epsilon = float(input('Введите погрешность e:'))
    grad = getGrad(func)
    while 1:
        points.append(curPoint)
        sum = 0
        countIteration+=1
        #print(str(countIteration)+'я итерация... Текущая точка - '+str(curPoint))
        #print(curPoint)
        #print('\n')
        if countArgs == 2:
            for i in range(0,countArgs):
                valueGrad[i]=grad[i].subs({x1:curPoint[0],x2:curPoint[1]})
        elif countArgs == 4:
            for i in range(0,countArgs):
                valueGrad[i] = grad[i].subs({x1:curPoint[0],x2:curPoint[1],x3:curPoint[2],x4:curPoint[3]})
        for i in range(0,countArgs):
            sum+= valueGrad[i] ** 2
        
        if sum ** .5 <= epsilon:
            break

        func_l = func.subs(x1,curPoint[0]-valueGrad[0]*l)
        func_l = func_l.subs(x2,curPoint[1]-valueGrad[1]*l)
        a,b=getInterval(func_l,-5,5)
        #_l=math.fabs(goldMethod(func_l,a,b))
        _l=goldMethod(func_l,a,b)

        for j in range(0,countArgs):
            curPoint[j]=(curPoint[j]-valueGrad[j]*l).subs({l:_l})
   #print('\n')
    #print('--------------Искомая точка минимума-------------:\n')
    #print(curPoint)
    return curPoint
    #print('\n--------------Значение функции в точке минимума-------------:\n')
    #print(getValueFunc(getStartFunc(indexFunc),curPoint))
        

def getGrad(func):
    result = [diff(func,x1),diff(func,x2)]
    return result

main()