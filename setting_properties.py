from src.repository.movie_repo import RepositoryMovies
from src.repository.movie_repo import RepositoryException
from src.repository.client_repo import RepositoryClients
from src.repository.client_repo import RepositoryException_c
from src.repository.movie_repo_textfile import MovieTextFileRepository
from src.repository.client_repo_textfile import ClientTextFileRepository
from src.services.undo_service import UndoService
from src.repository.rent_repo import RepositoryRental
from src.repository.rent_repo_textfile import RentalTextFileRepository
from src.repository.client_repo_binfile import ClientsBinFileRepository
from src.repository.movie_repo_binfile import MovieBinFileRepository
from src.repository.rent_repo_binfile import RentalBinFileRepository
from src.repository.rent_repo import RepositoryException_r
from src.ui.ui import Ui
repository=""
movies=""
clients=""
rentals=""
f = open("settings.propeties", "rt")
for line in f.readlines():
    r,repo = line.split(maxsplit=1, sep=' = ')
    if r=="repository":
        repository=repo.strip()
    elif r=="movies":
        movies=repo.strip()
    elif r=="clients":
        clients=repo.strip()
    elif r=="rentals":
        rentals=repo.strip()
if repository=="memory":
    m=RepositoryMovies(repository)
    c=RepositoryClients(repository)
    r=RepositoryRental(repository)
    u = UndoService()
    console = Ui(m, c,r,u)
    console.start()
elif repository=="text file":
    try:
        m = MovieTextFileRepository(movies)
        c = ClientTextFileRepository(clients)
        r=RentalTextFileRepository(rentals,c,m)
        u = UndoService()
        console = Ui(m, c,r,u)
        console.start()
    except RepositoryException as re:
        print(re)
    except RepositoryException_c as rc:
        print(rc)
    except RepositoryException_r as rr:
        print(rr)
    except FileNotFoundError as fe:
        print(fe)
elif repository=="bin file":
    try:
        m = MovieBinFileRepository(movies)
        c = ClientsBinFileRepository(clients)
        r = RentalBinFileRepository(rentals,c,m)
        u = UndoService()
        console = Ui(m, c, r, u)
        console.start()
    except RepositoryException as re:
        print(re)
    except RepositoryException_c as rc:
        print(rc)
    except RepositoryException_r as rr:
        print(rr)
    except FileNotFoundError as fe:
        print(fe)
else:
    print("no bueno!")