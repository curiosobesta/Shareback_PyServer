from Shareback_App.src.service.base.BaseService import BaseService
from Shareback_App.src.util.FileOperations import FileOperations


class FileMkdirService(BaseService):

    # Accepts Directory Array and Create Directories
    def mkdir(self, dir_arr):
        return FileOperations(self.user_id).mkdir(dir_arr)