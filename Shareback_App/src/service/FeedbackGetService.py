from Shareback_App.TableConstants import FeedbackConstants as FeedbackTable
from Shareback_App.models import Feedbacks
from Shareback_App.src.service.base.BaseService import BaseService


class FeedbackGetService(BaseService):

    def get_comments(self, session_id):
        print("Entering "+__name__+".get_comments()")
        comments = Feedbacks.objects.values_list(FeedbackTable.comment, flat=True).filter(session_id=session_id)
        print("Exiting " + __name__ + ".get_comments()")
        return list(comments)


