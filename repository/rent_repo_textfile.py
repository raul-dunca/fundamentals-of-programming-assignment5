from src.repository.rent_repo import RepositoryRental
from src.domain.rental import Rental
from datetime import date
class RentalTextFileRepository(RepositoryRental):
    def __init__(self,file_name,cl_list,mov_list):
        self._file_name = file_name
        self.clients=cl_list
        self.movie=mov_list
        super().__init__(file_name)

        self._load_file()
    def _load_file(self):
        f = open(self._file_name, "rt")  # rt -> read, text-mode
        for line in f.readlines():
            _id,cl,mov,retur,due,returned = line.split(maxsplit=5, sep=',')
            year,month,day=retur.split(maxsplit=2,sep='-')
            retur=date(int(year),int(month),int(day))
            year, month, day = due.split(maxsplit=2, sep='-')
            due = date(int(year), int(month), int(day))
            returned=returned.rstrip()
            if returned=="" or returned=="None" or returned==None:
                pass

            else:
                year, month, day = returned.split(maxsplit=2, sep='-')
                returned = date(int(year), int(month), int(day))
            self.rent_r(Rental(int(_id),mov,cl,retur,due,returned),self.clients,self.movie)
        f.close()

    def _save_file(self):
        f = open(self._file_name, "wt")  # wt -> write, text-mode
        for rentals in self._data:
            f.write(str(rentals.idr) + ',' + str(rentals.id_cl)+','+str(rentals.id_mov)+','+ str(rentals.rented_date)+','+ str(rentals.due_date)+','+str(rentals.returned_date)  + "\n")

        f.close()

    def rent_r(self,new,clients,movies):

        r=super().rent_r(new,clients,movies)
        # super().add(entity)
        self._save_file()
        return r
    def delete(self, objectId):
        super().delete(objectId)
        self._save_file()
    def return_r(self,new):
        d=super().return_r(new)
        self._save_file()
        return d
    def unreturn_r(self,new):
        super().unreturn_r(new)
        self._save_file()