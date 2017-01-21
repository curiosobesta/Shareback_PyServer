from Shareback_App.src.Constants import Constants
from Shareback_App.src.adapter.base.BaseAdapter import BaseAdapter
from Shareback_App.src.adapter.dto.PreviousSessionsResponseDTO import PreviousSessionsResponseDTO
from Shareback_App.src.service.PreviousSessionsSerivce import PreviousSessionsService


class PreviousSessionsAdapter(BaseAdapter):

    def execute(self):

        # Prepare Input Arguments
        request_no = int(
            self.request.GET.get(Constants.SESSION_ID, None)
        )

        # Call service
        sessions_list = PreviousSessionsService(self.user_id).get_list(request_no)

        # Prepare Response
        response_dto = PreviousSessionsResponseDTO()
        response_dto.session_list = sessions_list

        return response_dto
