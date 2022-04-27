from ...authentication_events import _IEventAction, _Serializable
import json
from typing import List


class ITokenIssuanceAction(_IEventAction, _Serializable):
    def __init__(self, actionType):
        self.actionType = actionType


class Claim(_Serializable):
    def __init__(self, id: str, values: List[str]):
        self.id = id
        self.values = values

    def to_dict(self) -> dict:
        return {"id": self.id, "value": self.values}

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
