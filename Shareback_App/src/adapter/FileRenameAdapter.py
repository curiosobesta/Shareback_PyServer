from Shareback_App.src.Constants import Constants
from Shareback_App.src.adapter.base.BaseAdapter import BaseAdapter
from Shareback_App.src.adapter.dto.FileRenameResponseDTO import FileRenameResponseDTO
from Shareback_App.src.service.FileRenameService import FileRenameService


class FileRenameAdapter(BaseAdapter):
    def execute(self):
        # Get Input Arguments
        src = str(self.request.GET.get(Constants.FILE_PATH, None))
        new_name = str(self.request.GET.get(Constants.NEW_NAME, None))

        # Prepare Arguments
        src = self.path_converter.to_abs(src)

        # Call Service
        result = FileRenameService(self.user_id).rename(src, new_name)

        # Prepare Response
        response = FileRenameResponseDTO()
        response.result = result

        return response
