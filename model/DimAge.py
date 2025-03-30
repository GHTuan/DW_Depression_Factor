from model.BaseModel import BaseModel

class DIM_AGE(BaseModel):
    __table_name__ = "dim_age"
    def __init__(self):
        super().__init__(self.__table_name__)
