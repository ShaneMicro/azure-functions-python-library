
import abc
from enum import Enum
import json
from logging import exception
import typing


class AuthenticationEventRequestStatus(Enum):
    Failed = 'Failed'
    TokenInvalid = 'TokenInvalid'
    Successful = 'Successful'


class _IAuthenticationEventResponse(abc.ABC):
    def __init__(self,
                 schema: str,
                 body: str):
        self.schema = schema
        self.body = body
        self.jsonBody = json.loads(body)
    pass


class _IAuthenticationEventResponse(abc.ABC):
    def __init__(self,
                 schema: str,
                 body: str):
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


class _IAuthenticationEventActionable(abc.ABC):

    abc.abstractmethod

    def invalidate_actions():
        pass


class _IAuthenticationEventAction(abc.ABC):
    def __init__(self,
                 actionType: str):
        self.actionType = actionType


_action_type = typing.TypeVar("_action_type", bound=_IAuthenticationEventAction)


class _IAuthenticationEventIActionableResponse(_IAuthenticationEventResponse, typing.Generic[_action_type]):
    def __init__(self,
                 schema: str,
                 body: str,
                 actions: list[_action_type]):
        super().__init__(schema, body)
        self.actions = actions


class _IAuthenticationEventData(abc.ABC):
    def __init__(self,
                 eventListenerId: str,
                 time: str,
                 apiSchemaVersion: str,
                 eventType: str,
                 customExtensionId: str):
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


_response_type = typing.TypeVar(
    "_response_type", bound=_IAuthenticationEventResponse)
_payload_type = typing.TypeVar("_payload_type", bound=_IAuthenticationEventData)


class _IAuthenticationEventRequest(abc.ABC, typing.Generic[_response_type, _payload_type]):
    def __init__(self,
                 statusMessage: str,
                 requestStatus: AuthenticationEventRequestStatus,
                 response: _response_type,
                 payload: _payload_type):
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
