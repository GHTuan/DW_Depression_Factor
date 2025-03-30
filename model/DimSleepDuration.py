from model.BaseModel import BaseModel

class DIM_SLEEP_DURATION(BaseModel):
    __table_name__ = "dim_sleep_duration"
    def __init__(self):
        super().__init__(self.__table_name__)
