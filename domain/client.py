class Client:
    def __init__(self,i,n):
        self._id = i
        self._name=n

    @property
    def idc(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        self._name=new_name

    def __str__(self):
        return "Client with the id: "+str(self.idc)+" and the name: "+str(self._name)