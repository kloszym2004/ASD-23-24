from zad1testy import Node, runtests

# Algorytm sortuje listę k-chaotyczną wykorzystując dwa różne sortowania zależnie od wartości k:
# dla k<=5  ->  Sortowanie bąbelkowe
# dla k>5   ->  Sortowanie przez scalanie
# Złożoność czasową dla :
# k = Θ(1)      ->  O = n
# k = Θ(log n)  ->  O = nlogn
# k = Θ(n)      ->  O = nlogn
#chyba

def dlugosc_listy(p):
    sum=0
    while p!=None:
        sum+=1
        p=p.next
    return sum

def bubble(p,k):
    g=Node()
    g.next=p
    start=g
    for _ in range (k):
        g=start
        p=g.next
        while p.next!=None:
            if p.val>p.next.val:
                p.val,p.next.val,p,g=p.next.val,p.val,p.next,g.next
            else:
                p,g=p.next,g.next
    return(start.next)

def merge(p,l):
    q=p
    r=p.next
    if l>2:
        for _ in range (0,((l-1)//2)-1,1):
            r=r.next
        tmp=r
        r=r.next
        tmp.next = None
        q=merge(q,((l-1)//2)+1)
        r=merge(r,l-((l-1)//2)-1)
    elif l==2:
        q.next=None
    gs=Node()
    gk=gs
    while q!=None and r!=None:
        if r.val<q.val:
            gk.next=r
            r=r.next
            gk=gk.next
        else:
            gk.next=q
            q=q.next
            gk=gk.next
    if q==None:gk.next=r
    else:gk.next=q
    return(gs.next)

def SortH(p,k):
    if k>5:
        l=dlugosc_listy(p)
        p=merge(p,l)
    else:
        p=bubble(p,k)
    return(p)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
