from src.services.movie_service import MovieServ
from src.services.client_service import ClientServ
from src.repository.movie_repo import RepositoryMovies
from src.repository.client_repo import RepositoryClients
from src.repository.movie_repo import RepositoryException
from src.repository.client_repo import RepositoryException_c
from src.domain.rental import Rental
from src.services.rental_service import RepoServ
from src.repository.rent_repo import RepositoryRental
from src.repository.rent_repo import RepositoryException_r
from src.services.undo_service import UndoService
from src.services.undo_service import UndoServiceExc
from datetime import date

class Ui:
    def __init__(self,movie_serv,client_serv,rent_serv,undo_serv):
            self._rent_serv = RepoServ(rent_serv, client_serv, movie_serv,undo_serv,rent_serv._file)
            self._movie_serv=MovieServ(movie_serv,self._rent_serv,undo_serv)
            self._client_serv=ClientServ(client_serv,self._rent_serv,undo_serv)
            self._undo_serv=undo_serv

    def __print_menu(self):
        print("1. Add a movie")
        print("2. Display the list of movies")
        print("3. Remove a movie")
        print("4. Update a movie")
        print("5. Add a client")
        print("6. Display the list of clients")
        print("7. Remove a client")
        print("8. Update a client")
        print("9. Rent a movie")
        print("10. Return a movie")
        print("11. Show the rent list")
        print("12. Search for clients or movies using any one of their fields")
        print("13. Most rented movies")
        print("14. Most active clients")
        print("15. Late rentals")
        print("16. Undo")
        print("17. Redo")
        print("18. Exit")

    def _print_movies(self):
        movies = self._movie_serv.get_all()
        index=1
        for m in movies:
            print(str(index)+")"+str(m))
            index=index+1
    def _print_rent(self):
        rents = self._rent_serv.get_all()
        index=1
        for r in rents:
            print(str(index)+")"+str(r))
            index=index+1
    def _print_clients(self):
        clients = self._client_serv.get_all()
        index = 1
        for c in clients:
            print(str(index)+")"+str(c))
            index = index + 1
    def _print_search(self,l):
        if len(l)==0:
            print("No item found!")
        else:
            index = 1
            for c in l:
                print(str(index) + ")" + str(c))
                index = index + 1
    def start(self):
        while True:
            try:
                self.__print_menu()
                opt = input()
                if opt == "1":
                    id = input("Give the id of the movie: ")
                    title = input("Give the title of the movie: ")
                    description = input("Give the description of the movie: ")
                    genre=  input("Give the genre of the movie: ")

                    self._movie_serv.add(id,title,description, genre)

                elif opt == "2":
                    self._print_movies()
                elif opt=="3":
                    poz=input("Give the movie's id you want to remove: ")
                    self._movie_serv.remove(poz)
                elif opt=="4":
                    p=input("Give the movie's id you want to update: ")
                    title=input("Give the new title: ")
                    descp=input("Give the new description: ")
                    gen=input("Give the new genre: ")
                    self._movie_serv.update(p,title,descp,gen)
                elif opt=="5":
                    idc = input("Give the id of the client: ")
                    name = input("Give the name of the client: ")
                    self._client_serv.add(idc,name)
                elif opt=="6":
                    self._print_clients()
                elif opt=="7":
                    poz_c=input("Give the client's id you want to remove: ")
                    self._client_serv.remove(poz_c)
                elif opt=="8":
                    pc = input("Give the client's id you want to update: ")
                    name = input("Give the new name: ")
                    self._client_serv.update(pc,name)
                elif opt=="9":
                    r=int(input("Give the id of the rent: "))
                    c=input("Who wants to rent?(Give the id of the client): ")
                    m=input("What movie do you want to rent?(Give the id of the movie): ")
                    day=int(input("Now please enter the date, first the day: "))
                    month=int(input("\t\t\t\t\t\t then the month: "))
                    year=int(input("\t\t\t\t\t\t then the year: "))
                    d=date(year, month, day)
                    self._rent_serv.rent(r,m,c,d)
                    print("The rent was successful!")
                elif opt=="10":
                    ri=int(input("Give the id of the rent: "))
                    c=input("We also need the id of the client: ")
                    da=date.today()
                    self._rent_serv.return_s(ri,c,da)
                    print("The return was successful!")
                elif opt=="11":
                    self._print_rent()
                elif opt=="12":
                    print("1. Search for clients")
                    print("2. Search for movies")
                    op=input()
                    if op=="1":
                        print("1. Search using ids")
                        print("2. Search using names")
                        o=input()
                        inp=input("Please enter your input: ")
                        self._print_search(self._client_serv.search(o,inp))
                    elif op=="2":
                        print("1. Search using ids")
                        print("2. Search using titles")
                        print("3. Search using description")
                        print("4. Search using genre")
                        o=input()
                        inp = input("Please enter your input: ")
                        self._print_search(self._movie_serv.search(o, inp))
                    else:
                        print("Bad command!")
                elif opt=="13":
                    self._print_search(self._movie_serv.most_rented_movies())
                elif opt=="14":
                    self._print_search(self._client_serv.most_active_clients())
                elif opt=="15":
                    self._print_search(self._rent_serv.late_rentals())
                elif opt=="16":
                    self._undo_serv.undo()
                elif opt=="17":
                    self._undo_serv.redo()
                elif opt == "18":
                    return
                else:
                    print("Bad selection!")
            except RepositoryException as re:
                print(re)
            except RepositoryException_c as rc:
                print(rc)
            except RepositoryException_r as rr:
                print(rr)
            except UndoServiceExc as ue:
                print(ue)
            except ValueError as ve:
                print(ve)

