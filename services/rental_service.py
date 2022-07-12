import copy
from src.domain.rental import Rental
from random import randint
from datetime import date
from random import shuffle
from src.services.undo_service import Call, CascadedOperation,Operation
from py import PogoList,sort_function,filter
class RepositoryException_r(Exception):
    """
    Writing (Exception) tells Python that RepoExc... is an Exception
    """
    pass

class RepoServ:
    def __init__(self,rental_repo,cl_serv,mov_serv,undo_serv,file):
        self._repo=rental_repo
        self._clients=cl_serv
        self._movies=mov_serv
        self._undo_service=undo_serv
        l=copy.deepcopy(self._clients.get_all_r())
        if file=="memory":
            try:
                for i in range(20):
                    shuffle(l)
                    m=randint(0,19)
                    self._rent(randint(1000,9999),self._movies[m].id,l[0].idc,date(randint(2020,2021),randint(1,11),randint(1,28)))
                    del l[0]
            except RepositoryException_r as re:
                pass
    def _unreturn(self,ri,c):
        self._repo.unreturn_r(Rental(rent_id=ri,cl_id=c))
    def rent(self,r,m,c,d):
        rent = self._repo.rent_r(Rental(rent_id=r,mov_id=m,cl_id=c,re_date=d),self._clients,self._movies)
        undo_call = Call(self.delete_rental, rent.idr)
        redo_call = Call(self._rent, rent.idr,rent.id_mov, rent.id_cl, rent.rented_date)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))
        self._undo_service.record(cope)

    def _rent(self,r,m,c,d):
        self._repo.rent_r(Rental(rent_id=r, mov_id=m, cl_id=c, re_date=d), self._clients, self._movies)
    def return_s(self,ri,c,da):
        rent=self._repo.return_r(Rental(rent_id=ri,cl_id=c,return_date=da))
        undo_call = Call(self._unreturn, rent.idr,rent.id_cl)
        redo_call = Call(self._return_s, rent.idr, rent.id_cl,rent.returned_date)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))
        self._undo_service.record(cope)
    def _return_s(self,ri,c,da):
        self._repo.return_r(Rental(rent_id=ri,cl_id=c,return_date=da))
    def get_all(self):
       return  self._repo.get_all_r()

    def old_filter_rentals(self, client_id, movie_id):
        """
        Return a list of rentals performed by the provided client for the provided car
        client - The client performing the rental. None means all clients
        cars - The rented car. None means all cars
        """
        result = []
        for rental in self._repo.get_all_r():
            if client_id is not None and int(rental.id_cl) != int(client_id):
                continue
            if movie_id is not None and int(rental.id_mov) != int(movie_id):
                continue
            result.append(rental)

        return result
    def f_1(self,x,id):
        if int(x.id_cl)==int(id):
            return True
        else:
            return False

    def f_2(self, x, id):
        if int(x.id_mov) == int(id):
            return True
        else:
            return False
    def filter_rentals(self,client_id, movie_id):
        result = []
        if client_id!=None:
            result=filter(self._repo.get_all_r(),self.f_1,client_id)
        else:
            result=filter(self._repo.get_all_r(), self.f_2, movie_id)
        return result
    def late_rentals(self):
        l= self._repo.late_rentals_r()
        movies=self._movies.get_all_r()
        for j in range(len(l)):
            for i in range(len(movies)):
                if(str(l[j])==str(movies[i].id)):
                    l[j]=str(movies[i])
                    break

        return l
    def delete_rental(self, rental_id):

        self._repo.delete(rental_id)




