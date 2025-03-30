from model.BaseModel import BaseModel

class DIM_SUICIDAL_THOUGHTS(BaseModel):
    __table_name__ = "dim_suicidal_thoughts"
    def __init__(self):
        super().__init__(self.__table_name__)
