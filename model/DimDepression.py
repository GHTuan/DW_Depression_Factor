from model.BaseModel import BaseModel

class DIM_DEPRESSION(BaseModel):
    __table_name__ = "dim_depression"
    def __init__(self):
        super().__init__(self.__table_name__)
