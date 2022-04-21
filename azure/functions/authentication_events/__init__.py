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
    def __init__(self, schema: str, body: str):
        self.schema = schema
        self.body = body
        self.jsonBody = json.loads(body)

    def invalidate():
        pass

    @staticmethod
    def create_instance(type: type, schema: str, body: str):
        response = _IAuthenticationEventResponse(type())
        response.Schema = schema
        response.Body = body
        return response


class _IAuthenticationEventAction(abc.ABC):
    def __init__(self, actionType: str):
        self.actionType = actionType


action_type = typing.TypeVar("action_type", bound=_IAuthenticationEventAction)


class _IAuthenticationEventIActionableResponse(
    _IAuthenticationEventResponse, typing.Generic[action_type]
):
    def __init__(self, schema: str, body: str, actions: List[action_type]):
        super().__init__(schema, body)
        self.actions = actions


class _IAuthenticationEventData(abc.ABC):
    def __init__(
        self,
        eventListenerId: str,
        time: str,
        apiSchemaVersion: str,
        eventType: str,
        customExtensionId: str,
    ):
        self.type = eventType
        self.apiSchemaVersion = apiSchemaVersion
        self.time = time
        self.eventListenerId = eventListenerId
        self.customExtensionId = customExtensionId

    @classmethod
    def from_json(json: str):
        jsonString = json.loads(json)
        return _IAuthenticationEventData(**jsonString)

    @staticmethod
    def create_instance(Type, json: str):
        data = _IAuthenticationEventData(Type())
        return data if not json else data.from_json(json)


response_type = typing.TypeVar("response_type", bound=_IAuthenticationEventResponse)  # noqa: E501
payload_type = typing.TypeVar("payload_type", bound=_IAuthenticationEventData)


class _IAuthenticationEventRequest(
    abc.ABC, typing.Generic[response_type, payload_type]
):
    def __init__(
        self,
        statusMessage: str,
        requestStatus: RequestStatus,
        response: response_type,
        payload: payload_type,
    ):
        self.statusMessage = statusMessage
        self.requestStatus = requestStatus
        self.response = response
        self.payload = payload

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
