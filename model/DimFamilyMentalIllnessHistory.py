from model.BaseModel import BaseModel

class DIM_FAMILY_MENTAL_ILLNESS_HISTORY(BaseModel):
    __table_name__ = "dim_family_mental_illness_history"
    def __init__(self):
        super().__init__(self.__table_name__)
