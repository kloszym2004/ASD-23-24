from zad1testy import Node, runtests

#

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
                q=p.next
                p.next=q.next
                q.next=p
                g.next=q
                g=g.next
                sort = False
            else:
                p=p.next
                g=g.next
    return(start.next)

def merge(p,l):
    q=p
    r=p.next
    dump=None
    if l>2:
        for _ in range (0,((l-1)//2)-1,1):
            r=r.next
        tmp=r
        r=r.next
        tmp.next = None
        q,dump=merge(q,((l-1)//2)+1)
        r,dump=merge(r,l-((l-1)//2)-1)
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
    while gk.next!=None:
        gk=gk.next
    return(gs.next,gk)

def SortH(p,k):
    if k>5:
        if k==dlugosc_listy(p):k-=1
        q=Node()
        start=q
        r=p
        q.next=r
        s=p.next.next.next
        t=p.next.next.next.next
        for _ in range(k-3):
            s=s.next
            t=t.next
        while t!=None:
            q.next=None
            s.next=None
            r,s=merge(r,k+1)
            q.next=r
            s.next=t
            q,r,s,t=q.next,r.next,s.next,t.next
        r,s=merge(r,k+1)
        q.next=r
        s.next=t
        p=start.next
    else:
        p=bubble(p,k)
    return(p)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )