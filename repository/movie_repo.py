from src.domain.movie import Movie
from random import randint
from random import choice
from datetime import date
from copy import deepcopy
from py import PogoList,sort_function,filter
class RepositoryException(Exception):
    """
    Writing (Exception) tells Python that RepoExc... is an Exception
    """
    pass

class RepositoryMovies:
    def __init__(self,file):
        self._data=PogoList()
        random_titles=["The Witcher","American Pie","Cars","Cars 2","Cars 3","Toy Story","Monsters University","Kung Fu Panda","The Hangover","The War with Grandpa","Dirty Grandpa","Spider-man One","Spider-man Two","Spider-man Three","Miami Bici","The Notebook","Titanic","A Star is Born","Jumanji: Welcome to the Jungle","Baywatch","The Karate Kid","The Godfather","The Godfather: Part II","Fight Club","Inception","The Matrix","Interstellar","Parasite","Terminator","Back to the Future","Casablanca","WALL-E","Avengers: Infinity War", "Avengers: Endgame","J0ker","The Hunger Games","The Father"]
        random_genre=["Horror","Action","Comedy","Drama","Fantasy","Mystery","Romance","Thriller","Adventure","Science fiction"]
        random_description=["A boy is bitten by a mutant spider and receives superpowers","The protagonist falls in love with the neighbour","A group of teenagers living on the edge","The protagonist tries to fulfill his grandpa last wishes","Two friends moved to Las Vegas to live their best life's","All the characters are cars and the protagonist is trying win a race","An ordinary man has a great business idea and becomes successful","The protagonist and his family moves to a new house and find out it is haunted","The protagonist wants to become the strongest ninja in the village and take the title of hokage","A bunch of players are put in a free for all arena, fighting for their life","The protagonist finds a paranormal notebook that can kill people if you write their name in it","An ordinary man is accused unfair for a crime he didn't commit"]
        k=int(0)
        if file=="memory":
            try:
               # while k<20:
                    for i in range(20):
                           self.add_r(Movie(randint(1000,9999),str(choice(random_titles)),str(choice(random_description)),str(choice(random_genre))))
                          # k=k+1
            except RepositoryException as re:
                pass

    def add_r(self, entity):
        """
        first we check if the entity id already exists is fo we raise an error, otherwise weh check if
        the id has a good format(a number of four digits). If the entity id respects all the conditions
        we add the entity(new movie) to the movie list
        """


        for i in range(len(self._data)):
            if entity.id==self._data[i].id:
                raise RepositoryException("Movie with id: " + str(entity.id) + " already in repo")
        if int(entity.id)//10000==0 and int(entity.id)//1000!=0:
            self._data.append(entity)
            return entity
        else:
            raise RepositoryException("Invalid id!")
    def remove_r(self,poz):
        """
            if the id exists we delete the movie with that id, otherwise we raise an error
        """
        k=int(0)
        for i in range(len(self._data)):
            if(int(poz)==int(self._data[i].id)):
                obj=self._data[i]
                del self._data[i]
                k=k+1
                break
        if k==0:
            raise RepositoryException("Can't find id!")
        return obj

    def uptdate_r(self,id,title,desc,genre):
        """
        first we check if the id given exists in our list of movies, if so we update the title, description and genre
         of the movie otherwise we raise an error
        """
        k = int(0)
        for i in range(len(self._data)):
            if (int(id) == int(self._data[i].id)):
                    obj=Movie(self._data[i].id,self._data[i].title,self._data[i].description,self._data[i].genre)
                    self._data[i].title = title

                    self._data[i].description = desc

                    self._data[i].genre = genre
                    k = k + 1
                    break
        if k == 0:
            raise RepositoryException("Can't find id!")
        else:
            return obj

    def search_r(self, option, input):
        search_list = PogoList()
        n = len(input)
        if option == "1" or option == "2" or option=="3" or option=="4":
            for i in range(len(self._data)):
                k = int(0)
                for j in range(0, n):
                    if option == "1":

                        if str(input[j]) in str(self._data[i].id):
                            k = k + 1
                    elif option=="2":
                        if (str(input[j]) in str(self._data[i].title)) or (str(input[j].lower()) in str(self._data[i].title)) or (str(input[j].upper()) in str(self._data[i].title)):
                            k = k + 1
                    elif option=="3":
                        if (str(input[j]) in str(self._data[i].description)) or (str(input[j].lower()) in str(self._data[i].description)) or (str(input[j].upper()) in str(self._data[i].description)):
                            k = k + 1
                    else:
                        if (str(input[j]) in str(self._data[i].genre)) or (str(input[j].lower()) in str(self._data[i].genre)) or (str(input[j].upper()) in str(self._data[i].genre)):
                            k = k + 1
                if (k == n):
                    search_list.append(self._data[i])
            return search_list
        else:
            raise RepositoryException("Invalid option!")
    def old_search_r(self, option, input):
        search_list = PogoList()
        n = len(input)
        if option == "1" or option == "2" or option=="3" or option=="4":
            for i in range(len(self._data)):
                k = int(0)
                for j in range(0, n):
                    if option == "1":
                        if str(input[j]) in str(self._data[i].id):
                            k = k + 1
                    elif option=="2":
                        if (str(input[j]) in str(self._data[i].title)) or (str(input[j].lower()) in str(self._data[i].title)) or (str(input[j].upper()) in str(self._data[i].title)):
                            k = k + 1
                    elif option=="3":
                        if (str(input[j]) in str(self._data[i].description)) or (str(input[j].lower()) in str(self._data[i].description)) or (str(input[j].upper()) in str(self._data[i].description)):
                            k = k + 1
                    else:
                        if (str(input[j]) in str(self._data[i].genre)) or (str(input[j].lower()) in str(self._data[i].genre)) or (str(input[j].upper()) in str(self._data[i].genre)):
                            k = k + 1
                if (k == n):
                    search_list.append(self._data[i])
            return search_list
        else:
            raise RepositoryException("Invalid option!")
    def most_rented_movies_r(self,rent_list):
        day_list=PogoList()
        for i in range(0,len(self._data)):
            day_list.append(0)
        k=int(0)

        for i in range(len(rent_list)):
            for j in range(len(self._data)):
                if str(rent_list[i].id_mov)==str(self._data[j].id):
                    k=j
                    if (rent_list[i].returned_date==None or rent_list[i].returned_date=="None" or rent_list[i].returned_date==""):
                        d=date.today()-rent_list[i].rented_date
                        day_list[k]+=d.days

                    else:

                        d=rent_list[i].returned_date-rent_list[i].rented_date
                        day_list[k] +=d.days


        return self.most_rented_movies_sort_r(day_list)
    def comparison_function(self,a,b):
        if a <b :
            return True
        else:
            return False

    def most_rented_movies_sort_r(self,day_list):
        result=PogoList()
        check=PogoList()
        for i in range(len(day_list)):
            result.append(0)
            check.append(0)
        l=sort_function(day_list, self.comparison_function)
        for i in range(len(day_list)):
            for j in range(len(day_list)):
                if day_list[i]==l[j] and check[j]==0:
                    check[j]=1
                    result[j]=self._data[i]
                    break
        return result
    def old_most_rented_movies_sort_r(self,day_list):
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
    a=RepositoryMovies()
    a.add_r(Movie("1234","God of War","A man gains incredible powers and tries to save his family","Action"))
    assert a._data[-1].id=="1234"
    assert a._data[-1].title=="God of War"
    assert a._data[-1].description == "A man gains incredible powers and tries to save his family"
    assert a._data[-1].genre == "Action"
    b=RepositoryMovies()
    try:
        b.add_r(Movie("932813","El Dorado","Just a cowboy living his best life","Comedy"))
        assert False
    except RepositoryException as re:
        assert str(re) == "Invalid id!"

#test_add_r()

def test_remove_r():
    a=RepositoryMovies()
    a.add_r(Movie("1234","God of War","A man gains incredible powers and tries to save his family","Action"))
    a.add_r(Movie("1412", "Amongus", "A group of crewmates find out they have 2 impostors among them", "Drama"))
    try:
        a.remove_r("123431")
        assert False
    except RepositoryException as re:
        assert str(re) == "Can't find id!"
    a.remove_r("1234")
    assert a._data[-1].id == "1412"
    assert a._data[-1].title == "Amongus"
    assert a._data[-1].description == "A group of crewmates find out they have 2 impostors among them"
    assert a._data[-1].genre == "Drama"
#test_remove_r()

def test_update_r():
    a = RepositoryMovies()
    a.add_r(Movie("1234", "God of War", "A man gains incredible powers and tries to save his family", "Action"))
    try:
        a.remove_r("123431")
        assert False
    except RepositoryException as re:
        assert str(re) == "Can't find id!"
    a.uptdate_r("1234","Amongus","A group of crewmates find out they have 2 impostors among them","Drama")
    assert a._data[-1].id == "1234"
    assert a._data[-1].title == "Amongus"
    assert a._data[-1].description == "A group of crewmates find out they have 2 impostors among them"
    assert a._data[-1].genre == "Drama"
#test_update_r()



import unittest
class MovieRepositoryTest(unittest.TestCase):
    def setUp(self):
        self._repo=RepositoryMovies()
        self.mov=Movie("1234","Will","A x-mas movie","Drama")
        self._repo.add_r(self.mov)
    def test_repo_add(self):
        self.assertEqual(self._repo[-1].id,"1234")
        self.assertEqual(self._repo[-1].title, "Will")
        self.assertEqual(self._repo[-1].description, "A x-mas movie")
        self.assertEqual(self._repo[-1].genre, "Drama")
        self.assertRaises(RepositoryException, self._repo.add_r, Movie("1234241","Pog","A movie about twitch chat","Horror"))
        self.assertRaises(RepositoryException, self._repo.add_r, Movie("1234", "Dunarea","Just Dunarea","Action"))

    def test_repo_remove(self):
        self._repo.add_r(Movie("5432","Pog","A movie about twitch chat","Horror"))
        self.assertRaises(RepositoryException, self._repo.remove_r, "12345566")
        self._repo.remove_r("1234")
        self.assertEqual(self._repo[-1].id, "5432")
        self.assertEqual(self._repo[-1].title, "Pog")
        self.assertEqual(self._repo[-1].description, "A movie about twitch chat")
        self.assertEqual(self._repo[-1].genre, "Horror")
    def test_repo_update(self):
        self.assertRaises(RepositoryException,self._repo.uptdate_r,"1234124","Dunarea","Just Dunarea","Action")
        self._repo.uptdate_r("1234","Dunarea","Just Dunarea","Action")
        self.assertEqual(self._repo[-1].title,"Dunarea")
        self.assertEqual(self._repo[-1].description, "Just Dunarea")
        self.assertEqual(self._repo[-1].genre, "Action")
    def tearDown(self):
        self._repo = None