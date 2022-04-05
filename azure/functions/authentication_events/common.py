
import abc
from enum import Enum
import json
from logging import exception
import typing


class AuthenticationEventRequestStatus(Enum):
    Failed = 'Failed'
    TokenInvalid = 'TokenInvalid'
    Successful = 'Successful'


class IAuthenticationEventResponse(abc.ABC):
    def __init__(self,
                 schema: str,
                 body: str):
        self.schema = schema
        self.body = body
        self.jsonBody = json.loads(body)
    pass
class IAuthenticationEventResponse(abc.ABC):
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
        response = IAuthenticationEventResponse(type())
        response.Schema = schema
        response.Body = body
        return response


class IAuthenticationEventActionable(abc.ABC):

    abc.abstractmethod

    def invalidate_actions():
        pass


class IAuthenticationEventAction(abc.ABC):
    def __init__(self,
                 actionType: str):
        self.actionType = actionType




action_type = typing.TypeVar("action_type", bound=IAuthenticationEventAction)
class IAuthenticationEventIActionableResponse(IAuthenticationEventResponse, typing.Generic[action_type]):
    def __init__(self,
                 schema: str,
                 body: str,
                 actions: list[action_type]):
        super().__init__(schema, body)
        self.actions = actions
       

        
class IAuthenticationEventData(abc.ABC):
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
        return IAuthenticationEventData(**jsonString)

    @staticmethod
    def create_instance(Type, json: str):
        data = IAuthenticationEventData(Type())
        return data if not json else data.from_json(json)


response_type = typing.TypeVar("response_type", bound=IAuthenticationEventResponse)
payload_type = typing.TypeVar("payload_type", bound=IAuthenticationEventData)


class IAuthenticationEventRequest(abc.ABC, typing.Generic[response_type, payload_type]):
    def __init__(self,
                 statusMessage: str,
                 requestStatus: AuthenticationEventRequestStatus,
                 response: response_type,
                 payload: payload_type):
        self.statusMessage = statusMessage
        self.requestStatus = requestStatus
        self.response = response
        self.payload = payload
        

    @abc.abstractmethod
    def create_instance(result: dict):
        pass

class Serializable(abc.ABC):
    @abc.abstractmethod
    def to_dict(self)->dict:
        pass
    @abc.abstractmethod
    def to_json(self)->str:
        pass