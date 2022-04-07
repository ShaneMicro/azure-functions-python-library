
import json
from ...token_issuance_start import _ITokenIssuanceAction, Claim
from ....authentication_events import _Serializable


class ProvideClaimsForToken(_ITokenIssuanceAction, _Serializable):
    def __init__(self,
                 claims: list[Claim]):
        self.actionType = "ProvideClaimsForToken"
        self.claims = claims

    def to_dict(self):
        return {
            "actionType": self.actionType,
            "claims": list(map(lambda c: c.to_dict(), self.claims))
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def add_claim(self, id: str, values: list[str]):
        self.claims.append(Claim(Id=id, Values=values))
