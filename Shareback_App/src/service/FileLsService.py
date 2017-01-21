from Shareback_App.src.service.base.BaseService import BaseService
from Shareback_App.src.util.FileOperations import FileOperations


class FileLsService(BaseService):

    # Accepts Directory array and returns List< Dir_Array[], File_Array[] >
    def ls(self, dir_arr):
        return FileOperations(self.user_id).ls(dir_arr)
