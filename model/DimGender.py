from model.BaseModel import BaseModel

class DIM_GENDER(BaseModel):
    __table_name__ = "dim_gender"
    def __init__(self):
        super().__init__(self.__table_name__)
