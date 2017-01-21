import json

from Shareback_App.src.Constants import Constants
from Shareback_App.src.adapter.base.BaseAdapter import BaseAdapter
from Shareback_App.src.adapter.dto.FileMkdirResponseDTO import FileMkdirResponseDTO
from Shareback_App.src.service.FileMkdirService import FileMkdirService


class FileMkdirAdapter(BaseAdapter):

    def execute(self):

        # Get Input Arguments
        file_arr = str(self.request.GET.get(Constants.DIRECTORY_PATH, None))
        file_arr = json.loads(file_arr)

        # Prepare Arguments
        file_arr = self.path_converter.to_abs_arr(file_arr)

        # Call Service
        result = FileMkdirService(self.user_id).mkdir(file_arr)

        # Prepare Response
        response = FileMkdirResponseDTO()
        response.result = result

        return response
