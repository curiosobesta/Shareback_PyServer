from abc import ABCMeta, abstractmethod

from Shareback_App.src.util.FilePathConverter import FilePathConverter


class BaseAdapter(metaclass=ABCMeta):

    def __init__(self, request):
        self.request = request
        self.user_id = "NOT INITIALIZED"
        self.path_converter = FilePathConverter(self.user_id)

    @abstractmethod
    def execute(self):
        raise NotImplementedError()
