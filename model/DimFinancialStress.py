from model.BaseModel import BaseModel

class DIM_FINANCIAL_STRESS(BaseModel):
    __table_name__ = "dim_financial_stress"
    def __init__(self):
        super().__init__(self.__table_name__)
