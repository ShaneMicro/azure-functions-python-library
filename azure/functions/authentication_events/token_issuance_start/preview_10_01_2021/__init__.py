import json

from .data import Context
from ...token_issuance_start import ITokenIssuanceAction
from ....authentication_events import (
    _IAuthenticationEventIActionableResponse,
    _Serializable,
    _IAuthenticationEventData,
    _IAuthenticationEventRequest,
    RequestStatus,
)
from typing import List, Dict


class TokenIssuanceStartResponse(
    _IAuthenticationEventIActionableResponse[ITokenIssuanceAction],
    _Serializable
):
    def __init__(
        self,
        actions: List[ITokenIssuanceAction],
        schema: str = None,
        body: str = None
    ):
        super().__init__(schema=schema, body=body, actions=actions)

    @staticmethod
    def create_instance(response: dict = None):
        if response is not None:
            return TokenIssuanceStartResponse(
                schema=response.get("schema"),
                body=response.get("body"),
                actions=[]
            )

    def to_dict(self):
        return {
            "actions": list(map(lambda a: a.to_dict(), self.actions)),
            "schema": self.schema,
            "body": self.body,
        }

    def to_json(self):
        return json.dumps(self.to_dict())


class TokenIssuanceStartData(_IAuthenticationEventData):
    def __init__(
        self,
        eventListenerId: str = None,
        time: str = None,
        apiSchemaVersion: str = None,
        eventType: str = None,
        customExtensionId: str = None,
        context: Context = None
    ):
        self.context = context
        super().__init__(
            eventListenerId=eventListenerId,
            time=time,
            eventType=eventType,
            apiSchemaVersion=apiSchemaVersion,
            customExtensionId=customExtensionId,
        )

    @staticmethod
    def create_instance(payload: dict = None):
        if payload is not None:
            return TokenIssuanceStartData(
                eventListenerId=payload.get("eventListenerId"),
                time=payload.get("time"),
                eventType=payload.get("type"),
                apiSchemaVersion=payload.get("apiSchemaVersion"),
                context=Context.populate(payload.get("context")),
                customExtensionId=payload.get("customExtensionId"),
            )


class TokenIssuanceStartRequest(
    _IAuthenticationEventRequest[
        TokenIssuanceStartResponse,
        TokenIssuanceStartData]
):
    def __init__(
        self,
        requestStatus: RequestStatus,
        response: TokenIssuanceStartResponse,
        payload: TokenIssuanceStartData,
        statusMessage: str = None,
        tokenClaims: Dict[str, str] = None,
    ):

        super().__init__(
            statusMessage=statusMessage,
            requestStatus=requestStatus,
            response=response,
            payload=payload,
        )
        self.tokenClaims = tokenClaims

    @staticmethod
    def create_instance(result: dict):
        response = TokenIssuanceStartResponse.create_instance(
            response=result.get("response")
        )
        data = TokenIssuanceStartData.create_instance(payload=result.get("payload"))  # noqa: E501
        tokenclaims = result.get("tokenClaims")
        return TokenIssuanceStartRequest(
            statusMessage=result.get("statusMessage"),
            requestStatus=RequestStatus(result.get("requestStatus")),
            response=response,
            payload=data,
            tokenClaims=tokenclaims,
        )
