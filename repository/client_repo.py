from src.domain.client import Client
from random import randint
from random import choice
from datetime import date
from copy import deepcopy
from py import PogoList,sort_function,filter
class RepositoryException_c(Exception):
    """
    Writing (Exception) tells Python that RepoExc... is an Exception
    """
    pass

class RepositoryClients:
    def __init__(self,file):
        """
        first we initialise our client list with 20 random entries
        """
        self._data=PogoList()
        random_names=["Jhon","Karl","Jimmy","Raul","Suzan","Sara","Paul","Costel","Luke","Ana","Haris","Kyle","Laurence","Liam","Gary","Ronnie","Theodore","Tyler","Felix","Max","Ben","Lucas","Robin","Will","Pierre","Carlos","Esteban","Billy","Kira","Ross","Kevin","Travis","Taylor","Ariana"]
        if file=="memory":
            try:
                for i in range(0,20):
                    self.add_r(Client(randint(10000,99999),choice(random_names)))
            except RepositoryException_c as re:Q
                pass
    def add_r(self, entity):
        """
        here is the add function, we verify if the entity id is already use, if so we raise an error, otherwise
        we check if the entity id has a good format (a number of 5 digits), if the id passes all the checks
        we add the entity(the new client) to the list of clients
        """
        for i in range(len(self._data)):
            if entity.idc == self._data[i].idc:
                raise RepositoryException_c("Client with id: " + str(entity.idc) + " already in repo")
        if int(entity.idc)//100000==0 and int(entity.idc)//10000!=0:
            self._data.append(entity)
        else:
            raise RepositoryException_c("Invalid id!")
        return entity
    def remove_r(self, poz):
        """
        if the id exists we delete the client with that id, otherwise we raise an error
        """
        k = int(0)
        for i in range(len(self._data)):
            if (int(poz) == int(self._data[i].idc)):
                obj=self._data[i]
                del self._data[i]
                k = k + 1
                break
        if k == 0:
            raise RepositoryException_c("Can't find id!")
        return obj
    def uptdate_r(self,id,name):
        """
        first we check if the id given exists in our list of clients, if so we update the name of the client
        otherwise we raise an error
        """
        k = int(0)
        for i in range(len(self._data)):
            if (int(id) == int(self._data[i].idc)):
                if name != None:
                    obj=Client(self._data[i].idc,self._data[i].name)

                    self._data[i].name = name
                    k = k + 1
                    break
        if k == 0:
            raise RepositoryException_c("Can't find id!")
        else:
            return obj
    def search_r(self,option,input):
        search_list=PogoList()
        n=len(input)
        if option=="1" or option=="2":
            for i in range(len(self._data)):
                k=int(0)
                for j in range(0,n):
                    if option=="1":
                        if str(input[j]) in str(self._data[i].idc):
                            k=k+1
                    else:
                        if (str(input[j]) in str(self._data[i].name)) or (str(input[j].lower()) in str(self._data[i].name)) or (str(input[j].upper()) in str(self._data[i].name)):
                            k=k+1
                if(k==n):
                    search_list.append(self._data[i])
            return search_list
        else:
            raise RepositoryException_c("Invalid option!")

    def most_active_clients_r(self,rentals_list):
        day_list=[]
        for i in range(0,len(self._data)):
            day_list.append(0)
        k = int(0)
        for i in range(len(rentals_list)):
            for j in range(len(self._data)):
                if str(rentals_list[i].id_cl) == str(self._data[j].idc):
                    k = j
                    if (rentals_list[i].returned_date == None or rentals_list[i].returned_date=="None" or rentals_list[i].returned_date==""):
                        d = date.today() - rentals_list[i].rented_date
                        day_list[k] += d.days

                    else:
                        d = rentals_list[i].returned_date - rentals_list[i].rented_date
                        day_list[k] += d.days
        return self.most_active_cleints_sort_r(day_list)
    def comparison_function(self,a,b):
        if a <b :
            return True
        else:
            return False
    def most_active_cleints_sort_r(self,day_list):
        result = PogoList()
        check = PogoList()
        for i in range(len(day_list)):
            result.append(0)
            check.append(0)
        l = sort_function(day_list, self.comparison_function)
        for i in range(len(day_list)):
            for j in range(len(day_list)):
                if day_list[i] == l[j] and check[j] == 0:
                    check[j] = 1
                    result[j] = self._data[i]
                    break
        return result

    def old_most_active_cleints_sort_r(self,day_list):
        l=[]
        l=deepcopy(self._data)
        for i in range(len(self._data)):
            for j in range(len(self._data)-1):
                if(day_list[i]>day_list[j]):
                    l[i],l[j]=l[j],l[i]
                    day_list[i],day_list[j]=day_list[j],day_list[i]
        return l
    def get_all_r(self):
        return self._data
    def __getitem__(self, item):
        return self._data[item]

def test_add_r():
    a=RepositoryClients()
    a.add_r(Client("12344","Ocon"))
    assert a._data[-1].name=="Ocon"
    assert a._data[-1].idc=="12344"
    b=RepositoryClients()
    try:
        b.add_r(Client("123445","Charles"))
        assert False
    except RepositoryException_c as re:
        assert str(re) == "Invalid id!"
#test_add_r()

def test_remove_r():
    a=RepositoryClients()
    a.add_r(Client("12345","Charles"))
    a.add_r(Client("41414","Carlos"))
    try:
        a.remove_r("12343141")
        assert False
    except RepositoryException_c as re:
        assert str(re) == "Can't find id!"
    a.remove_r("12345")
    assert a._data[-1].idc == "41414"
    assert a._data[-1].name == "Carlos"

#test_remove_r()

def test_update_r():
    a = RepositoryClients()
    a.add_r(Client("12345","Charles"))
    try:
        a.uptdate_r("12344131")
        assert False
    except RepositoryException_c as re:
        assert str(re) == "Can't find id!"
    a.uptdate_r("12345","Carlos")
    assert a._data[-1].idc == "12345"
    assert a._data[-1].name == "Carlos"
#test_update_r()



import unittest
class ClientRepositoryTest(unittest.TestCase):
    def setUp(self):
        self._repo=RepositoryClients()
        self.cl=Client("12345","Will")
        self._repo.add_r(self.cl)
    def test_repo_add(self):
        self.assertEqual(self._repo[-1].idc,"12345")
        self.assertEqual(self._repo[-1].name, "Will")
        self.assertRaises(RepositoryException_c, self._repo.add_r, Client("1234241","Pog"))
        self.assertRaises(RepositoryException_c, self._repo.add_r, Client("12345", "Pog"))

    def test_repoTve(self):
        self._repo.add_r(Client("54321","Rigby"))
        self.assertRaises(RepositoryException_c, self._repo.remove_r, "12345566")
        self._repo.remove_r("12345")
        self.assertEqual(self._repo[-1].idc, "54321")
        self.assertEqual(self._repo[-1].name, "Rigby")

    def test_repo_update(self):
        self.assertRaises(RepositoryException_c,self._repo.uptdate_r,"1234124","Will")
        self._repo.uptdate_r("12345","Ocon")
        self.assertEqual(self._repo[-1].name,"Ocon")
    def tearDown(self):
        self._repo = None
