from src.repository.client_repo import RepositoryClients
from src.domain.client import Client
import pickle
class ClientsBinFileRepository(RepositoryClients):
    def __init__(self,file_name):

        self._file_name = file_name
        super().__init__(self._file_name)
        self._load_file()

    # self._file_name = file_name

    def _load_file(self):
        f = open(self._file_name, "rb")  # rt -> read, binary
        self._data = pickle.load(f)
        f.close()

    def _save_file(self):
        f = open(self._file_name, "wb")  # wb -> write, binary
        pickle.dump(self._data, f)
        f.close()

    def add_r(self, entity):
        c = super().add_r(entity)
        # super().add(entity)
        self._save_file()
        return c

    def remove_r(self, poz):
        c = super().remove_r(poz)
        self._save_file()
        return c

    def uptdate_r(self, id, name):
        c = super().uptdate_r(id, name)
        self._save_file()
        return c