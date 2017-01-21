import json

from Shareback_App.src.Constants import Constants
from Shareback_App.src.adapter.base.BaseAdapter import BaseAdapter
from Shareback_App.src.adapter.dto.FileLsResponseDTO import FileLsResponseDTO
from Shareback_App.src.service.FileLsService import FileLsService


class FileLsAdapter (BaseAdapter):

    def execute(self):
        # Get Input Arguments
        file_arr = str(self.request.GET.get(Constants.FILE_PATH_ARRAY, None))
        file_arr = json.loads(file_arr)

        # Prepare Arguments
        file_arr = self.path_converter.to_abs_arr(file_arr)

        # Call Service
        result = FileLsService(self.user_id).ls(file_arr)

        # Prepare Response
        response = FileLsResponseDTO()
        response.result = result

        return response
