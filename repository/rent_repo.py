from datetime import date
from py import PogoList,sort_function,filter
class RepositoryException_r(Exception):
    """
    Writing (Exception) tells Python that RepoExc... is an Exception
    """
    pass
class RepositoryRental:
    def __init__(self,file):
        self._data=PogoList()
        self._file=file
    def unreturn_r(self,new):
        pos = int(0)
        for i in range(0,len(self._data)):
            if(int(new.idr)==int(self._data[i].idr)):
                pos=i
        self._data[pos]._returned_date= None

    def rent_r(self,new,clients,movies):
        k=int(0)
        b=int(0)
        for i in range(0,len(clients.get_all_r())):

            if(int(new.id_cl)==int(clients[i].idc)):
                k=k+1
        for i in range(0, len(movies.get_all_r())):
            if (int(new.id_mov) == int(movies[i].id)):
                 b=b+1
        for i in range(len(self._data)):
            if new.idr == self._data[i].idr:
                raise RepositoryException_r("Rental with id: " + str(new.idr) + " already in repo")
        if k==0:
            raise RepositoryException_r("Client id can't be found")
        if b==0:
            raise RepositoryException_r("Movie id can't be found")
        self._data.append(new)
        return new
    def return_r(self,new):

        b = int(0)
        k=int(0)
        pos=int(0)
        for i in range(0,len(self._data)):
            if(int(new.idr)==int(self._data[i].idr)):
                b = b + 1
                pos=i
        for i in range(0,len(self._data)):
            if(int(new.id_cl)==int(self._data[i].id_cl)):
                k = k + 1

        if b!=1:
            raise RepositoryException_r("Rental id can't be found")
        if k<1:
            raise RepositoryException_r("Rental id and client id don't match")
        if(self._data[pos]._returned_date=="None" or self._data[pos]._returned_date==None or self._data[pos]._returned_date==""):
            self._data[pos]._returned_date=date.today()
            return self._data[pos]
        else:
            raise RepositoryException_r("This movie was already returned!!")



    def delete(self, objectId):
        """
        Remove the object with given objectId from repository
        objectId - The objectId that will be removed
        Returns the object that was removed
        Raises RepositoryException if object with given objectId is not contained in the repository
        """

        ob=int(-1)
        for i in range(len(self._data)):
            if objectId == self._data[i].idr:
                ob=i
        if(ob==-1):
            return
        else:
            del self._data[ob]
    def filter_cond(self,x,d):
        if (x.returned_date==None or x.returned_date=="" or x.returned_date=="None") and (d<0):
            return True
        else:
            return False
    def late_rentals_r(self):
        ok=int(0)
        l=PogoList()
        nr_days=PogoList()
        for i in range(len(self._data)):
            ok=int(0)
            d=int(0)
            d=(self._data[i].due_date)-date.today()
            d=int(d.days)

            if (self._data[i].returned_date==None or self._data[i].returned_date=="" or self._data[i].returned_date=="None") and (d<0):
                for j in range (len(l)):
                    if str(self._data[i].id_mov)== str(l[j]):
                        ok=1
                        nr_days[j]-=d
                if(ok!=1):
                    nr_days.append(-d)
                    l.append(self._data[i].id_mov)

        return self.late_rentals_sort_r(nr_days,l)

    def comparison_function(self, a, b):
        if a < b:
            return True
        else:
            return False
    def late_rentals_sort_r(self,nr_day,list):
        result = PogoList()
        check = PogoList()
        for i in range(len(nr_day)):
            result.append(0)
            check.append(0)
        l = sort_function(nr_day, self.comparison_function)
        for i in range(len(nr_day)):
            for j in range(len(nr_day)):
                if nr_day[i] == l[j] and check[j] == 0:
                    check[j] = 1
                    result[j] = list[i]
                    break

        return result
    def get_all_r(self):
        return self._data
    def __getitem__(self, item):
        return self._data[item]






