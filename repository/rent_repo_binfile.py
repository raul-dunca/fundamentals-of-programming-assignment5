from src.repository.rent_repo import RepositoryRental
from src.domain.rental import Rental
import pickle
class RentalBinFileRepository(RepositoryRental):
    def __init__(self, file_name, cl_list, mov_list):
        self._file_name = file_name
        self.clients = cl_list
        self.movie = mov_list
        super().__init__(file_name)
        self._load_file()
    def _load_file(self):
        f = open(self._file_name, "rb")  # rt -> read, binary
        self._data = pickle.load(f)
        f.close()

    def _save_file(self):
        f = open(self._file_name, "wb")  # wb -> write, binary
        pickle.dump(self._data, f)
        f.close()

    def rent_r(self, new, clients, movies):
        r = super().rent_r(new, clients, movies)
        # super().add(entity)
        self._save_file()
        return r

    def delete(self, objectId):
        super().delete(objectId)
        self._save_file()

    def return_r(self, new):
        d = super().return_r(new)
        self._save_file()
        return d

    def unreturn_r(self, new):
        super().unreturn_r(new)
        self._save_file()