from model.BaseModel import BaseModel

class DIM_WORK_SATISFACTION(BaseModel):
    __table_name__ = "dim_work_satisfaction"
    def __init__(self):
        super().__init__(self.__table_name__)
