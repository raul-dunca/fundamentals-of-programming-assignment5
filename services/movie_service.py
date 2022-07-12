from src.repository.client_repo import RepositoryClients
from src.repository.movie_repo import RepositoryMovies
from src.services.rental_service import RepoServ
from src.repository.rent_repo import RepositoryRental
from src.domain.movie import Movie
from src.services.undo_service import Call, CascadedOperation,Operation

class MovieServ:
    def __init__(self, movie_repo,rental_serv,undo_service):
        self._repo = movie_repo
        self._rental_service = rental_serv
        self._undo_service = undo_service
    def add(self, id,title,description,genre):
        movie= self._repo.add_r(Movie(id,title,description,genre))
        undo_call = Call(self._remove, movie.id)
        redo_call = Call(self._add, movie.id, movie.title, movie.description,movie.genre)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))

        self._undo_service.record(cope)
    def _add(self, id, title, description, genre):
        self._repo.add_r(Movie(id, title, description, genre))
    def get_all(self):
        return self._repo.get_all_r()

    def remove(self, id):

        movie= self._repo.remove_r(id)
        undo_call = Call(self._add, movie.id, movie.title, movie.description,movie.genre)
        redo_call = Call(self._remove, movie.id)

        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))

        #        for j in range(len(self._rental_service._badpersons)):
        #            if int(l[i].id_cl)!=int(self._rental_service._badpersons[j]):
        #                    new_bad.append(self._rental_service._badpersons[j])
        #self._rental_service._badpersons=copy.deepcopy(new_bad)

        """
        Add all rentals to cascaded operation
        """
        rentals = self._rental_service.filter_rentals(None, id)

        for rent in rentals:
            self._rental_service.delete_rental(rent.idr)
            undo_call = Call(self._rental_service._rent, rent.idr,rent.id_mov, rent.id_cl, rent.rented_date)
            redo_call = Call(self._rental_service.delete_rental, rent.idr)
            cope.add(Operation(undo_call, redo_call))

        self._undo_service.record(cope)
        return movie

    def _remove(self,id):

        movie = self._repo.remove_r(id)

        l = self._rental_service.get_all()

        for i in range(len(l)):
            if int(movie.id) == int(l[i].id_mov):
                try:
                    self._rental_service._badpersons.remove(l[i].id_cl)
                except:
                    pass

        """
        rentals = self._rental_service.filter_rentals(None, id)
        for rent in rentals:
            self._rental_service.delete_rental(rent.idr)
         """
    def update(self,index,title,desc,genre):
        movie = self._repo.uptdate_r(index,title,desc,genre)
        undo_call = Call(self._update, movie.id, movie.title,movie.description,movie.genre)
        redo_call = Call(self._update, index, title,desc,genre)
        cope = CascadedOperation()
        cope.add(Operation(undo_call, redo_call))
        self._undo_service.record(cope)
    def _update(self,index,title,desc,genre):
        self._repo.uptdate_r(index,title,desc,genre)
    def search(self,option,input):
        return self._repo.search_r(option,input)
    def most_rented_movies(self):
        return self._repo.most_rented_movies_r(self._rental_service.get_all())
















def test_add():
    a=MovieServ(RepositoryMovies(),RepoServ(RepositoryRental(),RepositoryClients(),RepositoryMovies()))
    a.add("1234","God of War","A man gains incredible powers and tries to save his family","Action")
    l=a.get_all()
    assert l[-1].id=="1234"
    assert l[-1].title=="God of War"
    assert l[-1].description == "A man gains incredible powers and tries to save his family"
    assert l[-1].genre == "Action"


#test_add()

def test_remove():
    a=MovieServ(RepositoryMovies(),RepoServ(RepositoryRental(),RepositoryClients(),RepositoryMovies()))
    a.add("1234", "God of War", "A man gains incredible powers and tries to save his family", "Action")
    a.add("1412", "Amongus", "A group of crewmates find out they have 2 impostors among them", "Drama")
    a._remove("1234")
    l = a.get_all()
    assert l[-1].id == "1412"
    assert l[-1].title == "Amongus"
    assert l[-1].description == "A group of crewmates find out they have 2 impostors among them"
    assert l[-1].genre == "Drama"



#test_remove()

def test_update():
    a=MovieServ(RepositoryMovies(),RepoServ(RepositoryRental(),RepositoryClients(),RepositoryMovies()))
    a._add("1234", "God of War", "A man gains incredible powers and tries to save his family", "Action")
    a.update("1234","Amongus","A group of crewmates find out they have 2 impostors among them","Drama")
    l = a.get_all()
    assert l[-1].id == "1234"
    assert l[-1].title == "Amongus"
    assert l[-1].description == "A group of crewmates find out they have 2 impostors among them"
    assert l[-1].genre == "Drama"
#test_update()


import unittest
from src.repository.movie_repo import RepositoryException
class MovieRepositoryTest(unittest.TestCase):
    def setUp(self):
        self._serv=MovieServ(RepositoryMovies(),RepoServ(RepositoryRental(),RepositoryClients(),RepositoryMovies()))
        self._serv._add("1234","Will","A x-mas movie","Drama")
    def test_repo_add(self):
        l=self._serv.get_all()
        self.assertEqual(l[-1].id,"1234")
        self.assertEqual(l[-1].title, "Will")
        self.assertEqual(l[-1].description, "A x-mas movie")
        self.assertEqual(l[-1].genre, "Drama")
        self.assertRaises(RepositoryException, self._serv._add, "1234241","Pog","A movie about twitch chat","Horror")
        self.assertRaises(RepositoryException, self._serv._add, "1234", "Dunarea","Just Dunarea","Action")

    def test_repo_remove(self):
        self._serv.add("5432","Pog","A movie about twitch chat","Horror")
        self.assertRaises(RepositoryException, self._serv._remove, "12345566")
        self._serv._remove("1234")
        l=self._serv.get_all()
        self.assertEqual(l[-1].id, "5432")
        self.assertEqual(l[-1].title, "Pog")
        self.assertEqual(l[-1].description, "A movie about twitch chat")
        self.assertEqual(l[-1].genre, "Horror")
    def test_repo_update(self):
        self.assertRaises(RepositoryException,self._serv.update,"1234124","Dunarea","Just Dunarea","Action")
        self._serv.update("1234","Dunarea","Just Dunarea","Action")
        l=self._serv.get_all()
        self.assertEqual(l[-1].title,"Dunarea")
        self.assertEqual(l[-1].description, "Just Dunarea")
        self.assertEqual(l[-1].genre, "Action")
    def tearDown(self):
        self._repo = None