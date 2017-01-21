from Shareback_App.src.Constants import Constants
from Shareback_App.src.adapter.base.BaseAdapter import BaseAdapter
from Shareback_App.src.adapter.dto.FeedbackGetResponseDTO import FeedbackGetResponseDTO
from Shareback_App.src.service.FeedbackGetService import FeedbackGetService


class FeedbackGetAdapter(BaseAdapter):

    def execute(self):
        # Prepare Input Arguments
        session_id = self.request.GET.get(Constants.SESSION_ID, None)

        # Call service
        comments = FeedbackGetService(self.user_id).get_comments(session_id)

        # Prepare Response
        response_dto = FeedbackGetResponseDTO()
        response_dto.session_id = session_id
        response_dto.comments = comments

        return response_dto
