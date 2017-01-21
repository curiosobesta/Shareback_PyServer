from Shareback_App.src.adapter.dto.base.BaseResponse import BaseResponse
from Shareback_App.src.util.MyEncoder import MyEncoder


class FeedbackInsertResponseDTO(BaseResponse):

    def set_result(self, result):
        self.result = result

    def __init__(self):
        self.result = None

    def __str__(self):
        return MyEncoder().encode(self)