from poiskOtr_zolSech import *
from sympy import *
import math
import copy

x1,x2,x3,x4,l = symbols('x1 x2 x3 x4 l')


def getGrad(func):
    result = [diff(func,x1),diff(func,x2)]
    return result


def Gesse(grad):
    gesse=[]
    countArgs=len(grad)
    for i in range(0,countArgs):
        gesse.append([])
        for j in range(0,countArgs):
            gesse[i].append(diff(grad[i],'x'+str(j+1)))
    return gesse

def getValueFunc(func,point):
    if(len(point)==2):
        return func.subs({x1:point[0],x2:point[1]})
    if(len(point)==4):
        return func.subs({x1:point[0],x2:point[1],x3:point[2],x4:point[3]})

def getBestPoint(func, points):
    minValue=points[0]
    for i in range(0, len(points)):
        if(func.subs({x1:points[i][0],x2:points[i][1]}) <func.subs({x1:minValue[0],x2:minValue[1]})):
            minValue = points[i]
    return minValue

def NR(func, startPoint, epsilon, ogr):
    countIteration = 0
    countArgs=2
    sum = 0
    _l=0
    points = []
    curPoint = startPoint
    grad = []
    valueGrad = [0,0,0,0]

    print('---------------Метод Ньютона-Рафсона...-------------')
    #print('Выбирите нужную функцию...\n1.Функция Химмельблау №1\n2.Функция Химмельблау №2\n3.Функция Вуда\n4.Функция Пауэлла\n')
    #indexFunc = int(input())
    #print('Введите координаты начальной точки:')
    #if indexFunc == 1 or indexFunc == 2:
    #    for i in range(0,2):
    #        curPoint.append(float(input('Введите координату Х' + str(i) + ':')))
    #    countArgs = 2
    #elif indexFunc == 3 or indexFunc == 4:
    #    for i in range(0,4):
    #        curPoint.append(float(input('Введите координату Х' + str(i) + ':')))
    #    countArgs = 4
    #epsilon = float(input('Введите погрешность e:'))
    grad = getGrad(func)
    gesse=Gesse(grad)
    #obrValueGesse=Matrix
    obrValueGesse=[]
    valueGesse=[]
    obrValueGesseM=[]
    valueGesseM=[]
    for i  in range(0,countArgs):
        obrValueGesse.append([])
        valueGesse.append([])
        for j  in range(0,countArgs):
            obrValueGesse[i].append(0)
            valueGesse[i].append(0)
    while 1:
        points.append(curPoint)
        print(str(countIteration)+'я итерация...')
        sum = 0
        countIteration+=1
        
        if countArgs == 2:
            for i in range(0,countArgs):
                valueGrad[i]=grad[i].subs({x1:curPoint[0],x2:curPoint[1]})
        elif countArgs == 4:
            for i in range(0,countArgs):
                valueGrad[i] = grad[i].subs({x1:curPoint[0],x2:curPoint[1],x3:curPoint[2],x4:curPoint[3]})
        for i in range(0,countArgs):
            sum+= valueGrad[i] ** 2
        
        if sum ** .5 < epsilon:
            break
        for i in range(0,countArgs):
            for j in range(0,countArgs):
                valueGesse[i][j]=gesse[i][j].subs({x1:curPoint[0],x2:curPoint[1],x3:curPoint[-2],x4:curPoint[-1]})
        valueGesseM=Matrix(valueGesse)
        obrValueGesseM= -valueGesseM.inv() 
        valueGradM=Matrix(valueGrad)
        if countArgs==2:
            Pk=obrValueGesseM*Matrix([valueGrad[0],valueGrad[1]])
        elif countArgs==4:
            Pk=obrValueGesseM*Matrix([valueGrad[0],valueGrad[1],valueGrad[2],valueGrad[3]])

        func_l = func.subs(x1,curPoint[0]+Pk[0]*l)
        func_l = func_l.subs(x2,curPoint[1]+Pk[1]*l)
        
        a,b=getInterval1(func_l,0,0.5)
        _l=math.fabs(goldMethod(func_l,a,b))

        for j in range(0,countArgs):
            curPoint[j]=(curPoint[j]+Pk[j]*l).subs({l:_l})

        for j in range(0,len(ogr)):
            if(ogr[i].subs({x1:curPoint[0],x2:curPoint[1]}) > 0):
                return getBestPoint(func, points)

    #print('\n\n\n')
    print('--------------Искомая точка минимума-------------:\n')
    print(curPoint)
    #print('\n--------------Значение функции в точке минимума-------------:\n')
    #print(getValueFunc(getStartFunc(indexFunc),curPoint))
    return curPoint

