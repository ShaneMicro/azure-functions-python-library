import json

from .data import Context
from ...token_issuance_start import ITokenIssuanceAction
from ....authentication_events import (
    _IActionableResponse,
    _Serializable,
    _IEventData,
    _IEventRequest,
    RequestStatus,
    FailedRequest
)
from typing import List, Dict


class TokenIssuanceStartResponse(
    _IActionableResponse[ITokenIssuanceAction],
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

    def to_dict(self) -> dict:
        return {
            "actions": list(map(lambda a: a.to_dict(), self.actions)),
            "schema": self.schema,
            "body": self.body
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


class TokenIssuanceStartData(_IEventData):
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
    _IEventRequest[
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
        return TokenIssuanceStartRequest(
            statusMessage=result.get("statusMessage"),
            requestStatus=RequestStatus(result.get("requestStatus")),
            response=TokenIssuanceStartResponse.create_instance(response=result.get("response")),  # noqa: E501
            payload=TokenIssuanceStartData.create_instance(payload=result.get("payload")),  # noqa: E501
            tokenClaims=result.get("tokenClaims")
        )
