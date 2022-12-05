class mylist(object):
    start="0"
    args=None
    __name__="mylist"
    def __init__(self,*args):
        if args:
            for i in args:
                self.append(i)
    def append(self,value):
        start=int(getattr(self,"start"))
        setattr(self,str(start),value)
        self.start=str(start+1)
    def copy(self):
        c=mylist()
        for i in range(int(getattr(self,"start"))):
            c.append(getattr(self,str(i)))
        return c
    def insert(self,pos,value):
        if pos>=int(self.start):
            self.append(value)
        elif pos<int(self.start):
            for i in range(int(self.start)-1,pos-1,-1):
                old=getattr(self,str(i))
                setattr(self,str(i+1),old)
            setattr(self,str(pos),value)
            setattr(self,"start",int(self.start)+1)
    def extend(self,elem):
        start=int(self.start)
        if elem.__name__=="mylist":
            start2=int(elem.start)
            for i in range(start2):
                self.append(getattr(elem,str(i)))
    def disp(self,*args):
        if args:
            pass
        else:
            for i in range(int(self.start)):
                if i==int(self.start)-1 and i == 0:    
                    print("|",getattr(self,str(i)),"|",end="\n")
                elif i==0:
                    print("|",getattr(self,str(i)),",",end="")
                else:
                    if i==int(self.start)-1:
                        print(getattr(self,str(i)),"|",end="\n")
                    else:
                        print(getattr(self,str(i)),",",end="")
    def len(self):
        return int(self.start)
