import abc
from enum import Enum
import json
import typing

from typing import List, Optional


class RequestStatus(Enum):
    Failed = "Failed"
    TokenInvalid = "TokenInvalid"
    Successful = "Successful"


class _IAuthenticationEventResponse(abc.ABC):
    def __init__(self, schema: Optional[str], body: Optional[str] = None):
        self.schema = schema
        self.body = body
        if body is not None:
            self.jsonBody = json.loads(body)


class _IAuthenticationEventAction(abc.ABC):
    def __init__(self, actionType: str):
        self.actionType = actionType


action_type = typing.TypeVar("action_type", bound=_IAuthenticationEventAction)


class _IAuthenticationEventIActionableResponse(
    _IAuthenticationEventResponse, typing.Generic[action_type]
):
    def __init__(
        self,
        schema: Optional[str],
        body: Optional[str],
        actions: List[action_type]
    ):
        super().__init__(schema, body)
        self.actions = actions


class _IAuthenticationEventData(abc.ABC):
    def __init__(
        self,
        eventListenerId: Optional[str],
        time: Optional[str],
        apiSchemaVersion: Optional[str],
        eventType: Optional[str],
        customExtensionId: Optional[str],
    ):
        self.type = eventType
        self.apiSchemaVersion = apiSchemaVersion
        self.time = time
        self.eventListenerId = eventListenerId
        self.customExtensionId = customExtensionId


response_type = typing.TypeVar(
    "response_type", bound=_IAuthenticationEventResponse
)  # noqa: E501
payload_type = typing.TypeVar("payload_type", bound=_IAuthenticationEventData)


class _IAuthenticationEventRequest(
    abc.ABC, typing.Generic[response_type, payload_type]
):
    def __init__(
        self,
        statusMessage: Optional[str],
        requestStatus: RequestStatus,
        response: response_type,
        payload: payload_type,
    ):
        self.statusMessage = statusMessage
        self.requestStatus = requestStatus
        self.response = response
        self.payload = payload

    @abc.abstractmethod
    @staticmethod
    def create_instance(result: dict):
        pass


class _Serializable(abc.ABC):
    @abc.abstractmethod
    def to_dict(self) -> dict:
        pass

    @abc.abstractmethod
    def to_json(self) -> str:
        pass
