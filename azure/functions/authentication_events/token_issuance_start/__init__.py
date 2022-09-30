import json

from .data import AuthenticationContext

from .. import (
    _ActionableResponse,
    _AuthEventAction,
    _Serializable,
    _AuthEventData,
    _CloudEventRequest,
    RequestStatus,
)
from .. import FailedRequest  # noqa: F401

from typing import List, Dict


# All actions for the token issuance start event should extended this class, as it looks the correct action to the correct event.  # noqa: E501
class TokenIssuanceAction(_AuthEventAction, _Serializable):
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
        return {self.id: self.values}

    # method used to convert object to json string
    def to_json(self) -> str:
        return json.dumps(self.to_dict())


# The main response class that is related to the request, this extends IActionable as the response  # noqa: E501
# contains actions, we only allow actions that inherit the TokenIssuanceStartAction.  # noqa: E501
class TokenIssuanceStartResponse(
    _ActionableResponse[TokenIssuanceAction], _Serializable
):
    def __init__(
        self,
        actions: List[TokenIssuanceAction],
        ODataType: str = None,
        body: str = None
    ):
        super().__init__(ODataType=ODataType, body=body, actions=actions)

    # static method to create instance of the object from dict

    @staticmethod
    def create_instance(response: dict = None):
        if response is not None:
            return TokenIssuanceStartResponse(
                ODataType=response.get("oDataType"),
                body=response.get("body"),
                actions=[]
            )

    def to_dict(self) -> dict:
        return {"data": {
            "@odata.type": self.ODataType,
            "actions": list(map(lambda a: a.to_dict(), self.actions)),
        }}

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


# The main data class related to the request.
class TokenIssuanceStartData(_AuthEventData):
    def __init__(
        self,
        authenticationEventListenerId: str = None,
        customAuthenticationExtensionId: str = None,
        tenantId: str = None,
        authenticationContext: AuthenticationContext = None,
    ):
        # The main context of the data.
        self.authenticationContext = authenticationContext
        super().__init__(
            tenantId=tenantId,
            customAuthenticationExtensionId=customAuthenticationExtensionId,
            authenticationEventListenerId=authenticationEventListenerId
        )

    # static method to create instance of the object from dict
    @staticmethod
    def create_instance(payload: dict = None):
        if payload is not None:
            return TokenIssuanceStartData(
                authenticationEventListenerId=payload.get("authenticationEventListenerId"),
                authenticationContext=AuthenticationContext.populate(
                    payload.get("authenticationContext")
                ),
                customAuthenticationExtensionId=payload.get("customAuthenticationExtensionId"),
                tenantId=payload.get("tenantId")
            )


# The main request class, this will relate it's response and payload.
class TokenIssuanceStartRequest(
    _CloudEventRequest[TokenIssuanceStartResponse, TokenIssuanceStartData]
):
    def __init__(
        self,
        requestStatus: RequestStatus,
        response: TokenIssuanceStartResponse,
        payload: TokenIssuanceStartData,
        statusMessage: str = None,
        tokenClaims: Dict[str, str] = None,
        queryParameters: Dict[str, str] = None,
        type: str = None,
        source: str = None,
        oDataType: str = None,
    ):

        super().__init__(
            statusMessage=statusMessage,
            requestStatus=requestStatus,
            response=response,
            payload=payload,
            queryParameters=queryParameters,
            type=type,
            source=source,
            oDataType=oDataType,
        )
        # A dictionary of token claims.
        self.tokenClaims = tokenClaims

    # static method to create instance of the object from dict

    @staticmethod
    def create_instance(result: dict):
        return TokenIssuanceStartRequest(
            type=result.get("type"),
            source=result.get("source"),
            oDataType=result.get("@odata.type"),
            statusMessage=result.get("statusMessage"),
            requestStatus=RequestStatus(result.get("requestStatus")),
            response=TokenIssuanceStartResponse.create_instance(
                response=result.get("response")
            ),  # noqa: E501
            payload=TokenIssuanceStartData.create_instance(
                payload=result.get("payload")
            ),  # noqa: E501
            tokenClaims=result.get("tokenClaims"),
            queryParameters=result.get("queryParameters"),
        )
