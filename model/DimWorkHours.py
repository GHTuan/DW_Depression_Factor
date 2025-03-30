from model.BaseModel import BaseModel

class DIM_WORK_HOURS(BaseModel):
    __table_name__ = "dim_work_hours"
    def __init__(self):
        super().__init__(self.__table_name__)
