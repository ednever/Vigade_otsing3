from random import *
def arvud_loendis():
    """Arvude vahetus, arvude genereerimine, arvude jagamine loenditeks, arvude keskmise leidmine, loendite sortimine ja arvude lisamine loendisse. 
    """
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>maxi:
        mini,maxi=vahetus(mini,maxi)
    s=[]
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    pos=neg=null=[]
    jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)

def vahetus(a:int,b:int)->int:
    """Arvude vahetus
    :param int a: Väikseim arv
    :param int b: Suurim arv
    :rtype: int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """Arvude genereerimine
    :param int n: Kokku arve
    :param list loend: Tühi loend
    :param int a: Väikseim arv
    :param int b: Suurim arv
    """
    for i in range(n):
        loend.append(randint(a,b))

def jagamine(loend:list,p:int,n:int,nol:int):
    """Arvude jagamine loenditeks
    :param list loend: Loend arvudest
    :param int p: Positiivsed arvud
    :param int n: Negatiivsed arvud
    :param int nol: Nullid
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend:list)->float:
    """Arvude keskmise leidmine
    :param list loend: Loend arvudest
    :rtype: float
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:int):
    """Arvude lisamine loendisse
    :param list loend: Loend arvudest
    :param int el: Arv, mida lisatakse
    """
    loend.append(el)
    loend.sort()