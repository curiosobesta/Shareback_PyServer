import shutil
from os.path import dirname, join

from Shareback_App.src.service.base.BaseService import BaseService
from Shareback_App.src.util.FileOperations import FileOperations


class FileRenameService(BaseService):

    # Accepts List of File Paths and List of New Names
    # Sample Input ['/user/sagar/old_file.txt'], ['new_file.txt]
    def rename(self, file_path, new_name):
        return FileOperations(self.user_id).rename(file_path, new_name)