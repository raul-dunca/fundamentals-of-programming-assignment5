from src.repository.movie_repo import RepositoryMovies
from src.domain.movie import Movie
import pickle
class MovieBinFileRepository(RepositoryMovies):
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
        m=super().add_r(entity)
        self._save_file()
        return m
    def remove_r(self,poz):
        m=super().remove_r(poz)
        self._save_file()
        return m
    def uptdate_r(self,id,title,desc,genre):
        m=super().uptdate_r(id,title,desc,genre)
        self._save_file()
        return m