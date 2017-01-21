import shutil

from Shareback_App.src.service.base.BaseService import BaseService
from Shareback_App.src.util.FileOperations import FileOperations


class FileMoveService(BaseService):

    # Accepts File Array and Move files
    def move(self, src_arr, dest_arr):
        return FileOperations(self.user_id).move(src_arr, dest_arr)