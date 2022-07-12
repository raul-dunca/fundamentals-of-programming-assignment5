#from src.domain.movie import Movie
#from src.domain.client import Client
from random import randint
from calendar import monthrange
from datetime import date
class Rental:
    def __init__(self,rent_id,mov_id=None,cl_id=None,re_date=None, due_date=None, return_date=None):
        self._rent_id=rent_id
        if(mov_id!=None):
            self._movie_id=mov_id
        if(cl_id!=None):
            self._client_id=cl_id

        if(re_date!=None):
            self._rented_date=re_date
            r = str(re_date)
            year, month, day = r.split("-", maxsplit=2)
            num_days = monthrange(int(year), int(month))[1]
            nr = randint(3, 30)
            if int(nr)+int(day)>num_days and int(month)==12:
                day = (int(nr) + int(day)) % num_days
                month=int(1)
                year=int(year)+1
            elif(int(nr)+int(day)>num_days and int(month)<12):
                day=(int(nr)+int(day))%num_days
                month=int(month)+1
            else:
                day=(int(nr)+int(day))
            due_date=date(int(year),int(month),int(day))
            self._due_date=due_date

            if (int(self._rented_date.year)==2020):
                return_date=date(int(2021),randint(1,11),randint(1,28))

        self._returned_date=return_date

    @property
    def idr(self):
        return self._rent_id

    @property
    def id_cl(self):
        return self._client_id

    @property
    def id_mov(self):
        return self._movie_id

    @property
    def rented_date(self):
        return self._rented_date

    @property
    def due_date(self):
        return self._due_date

    @property
    def returned_date(self):
        return self._returned_date

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "The rental with the id: " + str(self._rent_id) + " has the following details: client with the id: "+str(self._client_id)+" rented the movie with the id: "+str(self._movie_id)+" in "+str(self._rented_date)+" and the due date is : "+str(self._due_date)+", return date: "+str(self._returned_date)
