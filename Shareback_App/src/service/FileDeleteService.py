from Shareback_App.src.service.base.BaseService import BaseService
from Shareback_App.src.util.FileOperations import FileOperations


class FileDeleteService(BaseService):

    # Accepts file array and remove files
    def delete(self, file_arr):
        return FileOperations(self.user_id).delete(file_arr)