from src.repository.client_repo import RepositoryClients
from src.repository.movie_repo import RepositoryMovies
from src.repository.rent_repo import RepositoryRental
from src.services.rental_service import RepoServ
from src.domain.client import Client
from src.services.undo_service import Call, CascadedOperation,Operation
class ClientServ:
    def __init__(self, client_repo,rental_serv,undo_service):
        self.__repo = client_repo
        self._rental_service=rental_serv
        self._undo_service=undo_service
    def add(self, id,name):
        client = self.__repo.add_r(Client(id, name))
        undo_call = Call(self._remove,client.idc)
        redo_call = Call(self._add, client.idc,client.name)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))
        self._undo_service.record(cope)
    def _add(self, id, name):
        self.__repo.add_r(Client(id, name))
    def get_all(self):
        return self.__repo.get_all_r()
    def remove(self,id):
        client = self.__repo.remove_r(id)
        undo_call = Call(self._add, client.idc, client.name)
        redo_call = Call(self._remove, client.idc)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))


        """
        Add all rentals to cascaded operation
        """

        rentals = self._rental_service.filter_rentals(id, None)
        for rent in rentals:
            #self._rental_service.delete_rental(rent.idr)

            undo_cll = Call(self._rental_service._rent, rent.idr, rent.id_mov, rent.id_cl, rent.rented_date)
            redo_cll = Call(self._rental_service.delete_rental, rent.idr)
            cope.add(Operation(undo_cll, redo_cll))
            self._rental_service.delete_rental(rent.idr)
        self._undo_service.record(cope)
        return client

    def _remove(self,id):
        client = self.__repo.remove_r(id)
        rentals = self._rental_service.filter_rentals(id, None)
        for rent in rentals:
            self._rental_service.delete_rental(rent.idr)

    def update(self,id,name):
        client = self.__repo.uptdate_r(id,name)
        undo_call = Call(self._update, client.idc, client.name)
        redo_call = Call(self._update, id, name)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))
        self._undo_service.record(cope)

    def _update(self,id,name):
        return self.__repo.uptdate_r(id,name)
    def search(self,option,input):
        return self.__repo.search_r(option,input)
    def most_active_clients(self):
        return self.__repo.most_active_clients_r(self._rental_service.get_all())

def test_add():
    a=ClientServ(RepositoryClients(),RepoServ(RepositoryRental(),RepositoryClients(),RepositoryMovies()))
    a.add("12344","Ocon")
    l=a.get_all()
    assert l[-1].idc=="12344"
    assert l[-1].name=="Ocon"


#test_add()

def test_remove():
    a=ClientServ(RepositoryClients(),RepoServ(RepositoryRental(),RepositoryClients(),RepositoryMovies()))
    a.add("12345", "Charles")
    a.add("41414", "Carlos")
    a.remove("12345")
    l = a.get_all()
    assert l[-1].idc == "41414"
    assert l[-1].name == "Carlos"



#test_remove()

def test_update():
    a=ClientServ(RepositoryClients(),RepoServ(RepositoryRental(),RepositoryClients(),RepositoryMovies()))
    a.add("12345", "Charles")
    a.update("12345", "Carlos")
    l=a.get_all()
    assert l[-1].idc == "12345"
    assert l[-1].name == "Carlos"
#test_update()


import unittest
from src.repository.client_repo import RepositoryException_c
class ClientServiceTest(unittest.TestCase):
    def setUp(self):
        self._serv=ClientServ(RepositoryClients(),RepoServ(RepositoryRental(),RepositoryClients(),RepositoryMovies()))
        self._serv.add("12345","Will")
    def test_serv_add(self):
        l=self._serv.get_all()
        self.assertEqual(l[-1].idc,"12345")
        self.assertEqual(l[-1].name, "Will")
        self.assertRaises(RepositoryException_c, self._serv.add, "1234241","Pog")
        self.assertRaises(RepositoryException_c, self._serv.add, "12345", "Pog")

    def test_serv_remove(self):
        self._serv.add("54321","Rigby")
        self.assertRaises(RepositoryException_c, self._serv.remove, "12345566")
        self._serv.remove("12345")
        l=self._serv.get_all()
        self.assertEqual(l[-1].idc, "54321")
        self.assertEqual(l[-1].name, "Rigby")

    def test_serv_update(self):
        self.assertRaises(RepositoryException_c,self._serv.update,"1234124","Will")
        self._serv.update("12345","Ocon")
        l=self._serv.get_all()
        self.assertEqual(l[-1].name,"Ocon")
    def tearDown(self):
        self._serv = None