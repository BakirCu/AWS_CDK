from data_access.entity.base_entity import BaseEntity

class CarEntity(BaseEntity):
    def __init__(self, id: int, type: str) -> None:
        self.id = id
        self.type = type
   
    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def to_json(self):
        return self.__dict__

    @staticmethod
    def from_dict(data: dict) -> object:
        id = data.get("id")
        type = data.get("type")
        return CarEntity(id=id, type=type)
