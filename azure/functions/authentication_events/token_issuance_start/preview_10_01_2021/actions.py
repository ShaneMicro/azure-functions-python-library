import json
from ...token_issuance_start import ITokenIssuanceAction, Claim
from typing import List


class ProvideClaimsForToken(ITokenIssuanceAction):
    def __init__(self, claims: List[Claim]):
        self.actionType = "ProvideClaimsForToken"
        self.claims = claims

    def to_dict(self) -> dict:
        return {
            "actionType": self.actionType,
            "claims": list(map(lambda c: c.to_dict(), self.claims)),
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def add_claim(self, id: str, values: List[str]):
        self.claims.append(Claim(id=id, values=values))
