from model.BaseModel import BaseModel

class FROM_SOURCE(BaseModel):
    __table_name__ = "from_source"
    def __init__(self):
        super().__init__(self.__table_name__)
