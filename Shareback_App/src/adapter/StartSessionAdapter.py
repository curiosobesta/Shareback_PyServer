from Shareback_App.src.Constants import Constants
from Shareback_App.src.adapter.base.BaseAdapter import BaseAdapter
from Shareback_App.src.adapter.dto.StartSessionResponseDTO import StartSessionResponseDTO
from Shareback_App.src.service.StartSessionService import StartSessionService


class StartSessionAdapter(BaseAdapter):
    def execute(self):
        # Prepare Input Arguments
        session_name = self.request.GET.get(Constants.SESSION_NAME, None)

        # Call Service
        session_id = StartSessionService(self.user_id).start(session_name)

        # Prepare Response
        response = StartSessionResponseDTO()
        response.session_id = session_id
        response.session_name = session_name

        return response