from model.BaseModel import BaseModel

class DIM_DIETARY_HABITS(BaseModel):
    __table_name__ = "dim_dietary_habits"
    def __init__(self):
        super().__init__(self.__table_name__)
