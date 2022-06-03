import json
from ..token_issuance_start import ITokenIssuanceAction, Claim
from typing import List


# Class for the Provide Claims for token action.
class ProvideClaimsForToken(ITokenIssuanceAction):
    def __init__(self, claims: List[Claim]):
        # The 'Name' of the action in the JSON.
        self.actionType = "ProvideClaimsForToken"
        # Collection of claims to add to the token.
        self.claims = claims

    # create json dict of the object
    def to_dict(self) -> dict:
        return {
            "actionType": self.actionType,
            "claims": list(map(lambda c: c.to_dict(), self.claims)),
        }

    # creates json string of the object
    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    # append claim to the list of claims
    def add_claim(self, id: str, values: List[str]):
        self.claims.append(Claim(id=id, values=values))
