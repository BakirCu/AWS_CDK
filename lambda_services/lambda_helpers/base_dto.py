from abc import ABC


class BaseDto(ABC):

    def to_json(self):
        pass
    
    def from_dict(self, dict):
        pass
