from ...authentication_events import _IEventAction, _Serializable
import json
from typing import List


# All actions for the token issuance start event should extended this class, as it looks the correct action to the correct event.  # noqa: E501
class ITokenIssuanceAction(_IEventAction, _Serializable):
    def __init__(self, actionType):
        # This will be the 'Name' of the action in the JSON.
        self.actionType = actionType


# A class representing a claim
class Claim(_Serializable):
    def __init__(self, id: str, values: List[str]):
        # The id of the claim (i.e. Name).
        self.id = id
        # The value of the claim.
        self.values = values

    # method used to convert object to json dict
    def to_dict(self) -> dict:
        return {"id": self.id, "value": self.values}

    # method used to convert object to json string
    def to_json(self) -> str:
        return json.dumps(self.to_dict())
