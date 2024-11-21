class fraction:
    def _init_(self,n,d):
        self.num=n
        self.dum=d
    def _str_(self): #for printing the class's object in a specific way
        print(self.n,"/",self.d)
    def _add_(self,other): #method to sum 2 diff objects
        temp_num=(self.num * other.dum)+(self.num * self.dum)
        temp_dum=self.dum * other.dum
        # if we do this two classes ex: hello and yoo we can add by doing hello+yoo
        return '{}/{}'.format(temp_num,temp_dum)