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
from typing import List, Dict, Optional


class TokenIssuanceStartResponse(
    _IAuthenticationEventIActionableResponse[ITokenIssuanceAction],
    _Serializable
):
    def __init__(
        self,
        actions: List[ITokenIssuanceAction],
        schema: Optional[str] = None,
        body: Optional[str] = None
    ):
        super().__init__(schema=schema, body=body, actions=actions)

    @staticmethod
    def create_instance(response: Optional[dict] = None):
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
        eventListenerId: Optional[str],
        time: Optional[str],
        apiSchemaVersion: Optional[str],
        eventType: Optional[str],
        customExtensionId: Optional[str],
        context: Optional[Context] = None
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
    def create_instance(payload: Optional[dict] = None):
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
        statusMessage: Optional[str],
        requestStatus: RequestStatus,
        response: TokenIssuanceStartResponse,
        payload: TokenIssuanceStartData,
        tokenClaims: Optional[Dict[str, str]],
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
