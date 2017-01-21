from Shareback_App.src.service.base.BaseService import BaseService
from Shareback_App.src.util.FileOperations import FileOperations


class FileCopyService(BaseService):

    # Accepts list of files and paste to destination path
    def copy(self, file_arr, destination_path):
        operation = FileOperations(self.user_id)
        return operation.copy(file_arr, destination_path)