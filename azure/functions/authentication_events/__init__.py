import abc
from enum import Enum
import json
import typing

from typing import List


# The status of the request.
class RequestStatus(Enum):
    # The request failed for any reason, see the response message.
    Failed = "Failed"
    # The request was success but the token being used on the incoming called is NOT valid.  # noqa: E501
    TokenInvalid = "TokenInvalid"
    # All's well!
    Successful = "Successful"


# Event response class that houses attributes returned from the authentication events trigger.  # noqa: E501
class _IEventResponse(abc.ABC):
    def __init__(self, schema: str = None, body: str = None):
        # The schema the of expected response.
        self.schema = schema
        # A template of the body of the expected response.
        self.body = body
        if body is not None:
            # A JSON representation of the body.
            self.jsonBody = json.loads(body)


# A class representing an action for an event.
class _IEventAction(abc.ABC):
    def __init__(self, actionType: str):
        #  Must be overridden, this will be the 'Name' of the action in the JSON.  # noqa: E501
        self.actionType = actionType


action_type = typing.TypeVar("action_type", bound=_IEventAction)


# Class that binds a response that has actions
class _IActionableResponse(
    _IEventResponse, typing.Generic[action_type]
):
    def __init__(
        self,
        actions: List[action_type],
        schema: str = None,
        body: str = None
    ):
        super().__init__(schema, body)
        # Collections of actions pertaining to the event.
        self.actions = actions


# Event data class pertaining to the expected payload, this class houses the common attributes for data events.  # noqa: E501
class _IEventData(abc.ABC):
    def __init__(
        self,
        eventListenerId: str = None,
        time: str = None,
        apiSchemaVersion: str = None,
        eventType: str = None,
        customExtensionId: str = None,
    ):
        # The event type (e.g. OnTokenIssuanceStart).
        self.type = eventType
        # The version of the event being targeted.
        self.apiSchemaVersion = apiSchemaVersion
        # Date and time of the event.
        self.time = time
        # Unique Id for the event.
        self.eventListenerId = eventListenerId
        # The unique internal Id of the registered custom extension.
        self.customExtensionId = customExtensionId


response_type = typing.TypeVar(
    "response_type", bound=_IEventResponse
)  # noqa: E501
payload_type = typing.TypeVar("payload_type", bound=_IEventData)


# Abstract base event class to house common event request attributes.
class _IEventRequest(
    abc.ABC, typing.Generic[response_type, payload_type]
):
    def __init__(
        self,
        requestStatus: RequestStatus,
        response: response_type,
        payload: payload_type,
        statusMessage: str = None,
    ):
        # A user friendly message (containing errors), that the authentication event returns.  # noqa: E501
        self.statusMessage = statusMessage
        # The status of the current request, see RequestStatus.
        self.requestStatus = requestStatus
        # Related IEventResponse
        self.response = response
        # Related IEventData
        self.payload = payload

    @staticmethod
    @abc.abstractmethod
    def create_instance(result: dict):
        pass


# base class extended to ensure objects are serializable.
class _Serializable(abc.ABC):
    # method used to create json dict from object.
    @abc.abstractmethod
    def to_dict(self) -> dict:
        pass

    # method used to create json string from object.
    @abc.abstractmethod
    def to_json(self) -> str:
        pass


class FailedRequest(_IActionableResponse, _Serializable):
    def __init__(self, error: str):
        self.error = error

    @staticmethod
    def handle(error: Exception):
        return FailedRequest(str(error))

    def to_dict(self) -> dict:
        return {"error": self.error}

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
