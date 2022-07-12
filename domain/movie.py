class Movie:
    def __init__(self,i,t,d,g):
        self._id = i
        self._title = t
        self._description = d
        self._genre = g

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def genre(self):
        return self._genre

    @title.setter
    def title(self,new):
        self._title=new

    @description.setter
    def description(self, new):
        self._description = new

    @genre.setter
    def genre(self, new):
        self._genre = new
    def __str__(self):
        return "Movie with the id: "+str(self.id)+", the title: "+str(self._title)+", the description: "+str(self._description)+" and the genre: "+str(self._genre)