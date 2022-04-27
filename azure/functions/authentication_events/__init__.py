import abc
from enum import Enum
import json
import typing

from typing import List


class RequestStatus(Enum):
    Failed = "Failed"
    TokenInvalid = "TokenInvalid"
    Successful = "Successful"


class _IAuthenticationEventResponse(abc.ABC):
    def __init__(self, schema: str = None, body: str = None):
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
        actions: List[action_type],
        schema: str = None,
        body: str = None
    ):
        super().__init__(schema, body)
        self.actions = actions


class _IAuthenticationEventData(abc.ABC):
    def __init__(
        self,
        eventListenerId: str = None,
        time: str = None,
        apiSchemaVersion: str = None,
        eventType: str = None,
        customExtensionId: str = None,
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
        requestStatus: RequestStatus,
        response: response_type,
        payload: payload_type,
        statusMessage: str = None,
    ):
        self.statusMessage = statusMessage
        self.requestStatus = requestStatus
        self.response = response
        self.payload = payload

    @staticmethod
    @abc.abstractmethod
    def create_instance(result: dict):
        pass


class _Serializable(abc.ABC):
    @abc.abstractmethod
    def to_dict(self) -> dict:
        pass

    @abc.abstractmethod
    def to_json(self) -> str:
        pass
