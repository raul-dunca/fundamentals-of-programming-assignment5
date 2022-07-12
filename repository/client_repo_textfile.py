from src.repository.client_repo import RepositoryClients
from src.domain.client import Client
class ClientTextFileRepository(RepositoryClients):
    def __init__(self,file_name):
        self._file_name = file_name
        super().__init__(self._file_name)
        self._load_file()
    def _load_file(self):
        f = open(self._file_name, "rt")  # rt -> read, text-mode
        for line in f.readlines():
            _id,name = line.split(maxsplit=1, sep=',')
            self.add_r(Client(int(_id),name.rstrip()))
        f.close()

    def _save_file(self):
        f = open(self._file_name, "wt")  # wt -> write, text-mode
        for cl in self._data:
            f.write(str(cl.idc) + ',' + cl.name  + "\n")

        f.close()

    def add_r(self, entity):
        c=super().add_r(entity)
        # super().add(entity)
        self._save_file()
        return c
    def remove_r(self, poz):
        c=super().remove_r(poz)
        self._save_file()
        return c
    def uptdate_r(self,id,name):
        c=super().uptdate_r(id,name)
        self._save_file()
        return c
