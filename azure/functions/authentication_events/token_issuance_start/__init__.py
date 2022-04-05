
from ...authentication_events import _IAuthenticationEventAction, _Serializable
import json


class _ITokenIssuanceAction(_IAuthenticationEventAction):
    def __init__(self,
                 actionType):
        self.actionType = actionType


class Claim(_Serializable):
    def __init__(self,
                 id: str,
                 values: list[str]):
        self.id = id
        self.values = values

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.values
        }

    def to_json(self):
        return json.dumps(self.to_dict())
