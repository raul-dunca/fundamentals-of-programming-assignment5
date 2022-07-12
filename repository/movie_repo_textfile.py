from src.repository.movie_repo import RepositoryMovies
from src.domain.movie import Movie
class MovieTextFileRepository(RepositoryMovies):
    def __init__(self,file_name):
        self._file_name = file_name
        super().__init__(self._file_name)
        self._load_file()
       # self._file_name = file_name

    def _load_file(self):
        f = open(self._file_name, "rt")  # rt -> read, text-mode
        for line in f.readlines():
            _id,title,description,genre = line.split(maxsplit=3, sep=',')
            self.add_r(Movie(int(_id),title,description, genre.rstrip()))


        f.close()

    def _save_file(self):
        f = open(self._file_name, "wt")  # wt -> write, text-mode
        for mov in self._data:
            f.write(str(mov.id) + ',' + mov.title + ',' + mov.description+',' + mov.genre + "\n")

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
