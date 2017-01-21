import json

from Shareback_App.src.Constants import Constants
from Shareback_App.src.adapter.base.BaseAdapter import BaseAdapter
from Shareback_App.src.adapter.dto.FileDeleteResponseDTO import FileDeleteResponseDTO
from Shareback_App.src.service.FileDeleteService import FileDeleteService


class FileDeleteAdapter(BaseAdapter):

    def execute(self):

        # Get Input Arguments
        file_arr = json.loads(
            str(self.request.GET.get(Constants.FILE_PATH_ARRAY, None))
        )

        # Prepare Input Arguments
        file_arr = self.path_converter.to_abs_arr(file_arr)

        # Call Service
        result = FileDeleteService(self.user_id).delete(file_arr)

        # Prepare Response
        response = FileDeleteResponseDTO()
        response.result = result

        return response
