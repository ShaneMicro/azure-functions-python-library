import abc
from enum import Enum
import json
import typing

from typing import List, Dict


# The status of the request.
class RequestStatus(Enum):
    # The request failed for any reason, see the response message.
    Failed = "Failed"
    # The request was success but the token being used on the incoming called is NOT valid.  # noqa: E501
    TokenInvalid = "TokenInvalid"
    # All's well!
    Successful = "Successful"


# Event response class that houses attributes returned from the authentication events trigger.  # noqa: E501
class _AuthEventResponse(abc.ABC):
    def __init__(self, ODataType: str = None, body: str = None):
        # The schema the of expected response.
        self.ODataType = ODataType
        # A template of the body of the expected response.
        self.body = body
        if body is not None:
            # A JSON representation of the body.
            self.jsonBody = json.loads(body)


# A class representing an action for an event.
class _AuthEventAction(abc.ABC):
    def __init__(self, actionType: str):
        #  Must be overridden, this will be the 'Name' of the action in the JSON.  # noqa: E501
        self.actionType = actionType


action_type = typing.TypeVar("action_type", bound=_AuthEventAction)


# Class that binds a response that has actions
class _ActionableResponse(_AuthEventResponse, typing.Generic[action_type]):
    def __init__(
        self, actions: List[action_type], ODataType: str = None, body: str = None
    ):
        super().__init__(ODataType=ODataType, body=body)
        # Collections of actions pertaining to the event.
        self.actions = actions


# Event data class pertaining to the expected payload, this class houses the common attributes for data events.  # noqa: E501
class _AuthEventData(abc.ABC):
    def __init__(
        self,
        tenantId: str = None,
        authenticationEventListenerId: str = None,
        customAuthenticationExtensionId: str = None
    ):
        # tenant Id
        self.tenantId = tenantId
        # Unique Id for the event.
        self.authenticationEventListenerId = authenticationEventListenerId
        # The unique internal Id of the registered custom extension.
        self.customAuthenticationExtensionId = customAuthenticationExtensionId

response_type = typing.TypeVar("response_type", bound=_AuthEventResponse)  # noqa: E501
payload_type = typing.TypeVar("payload_type", bound=_AuthEventData)


# Abstract base event class to house common event request attributes.
class _AuthEventRequest(abc.ABC, typing.Generic[response_type, payload_type]):
    def __init__(
        self,
        requestStatus: RequestStatus,
        response: response_type,
        payload: payload_type,
        statusMessage: str = None,
        queryParameters:  Dict[str, str] = None,
    ):
        # A user friendly message (containing errors), that the authentication event returns.  # noqa: E501
        self.statusMessage = statusMessage
        # The status of the current request, see RequestStatus.
        self.requestStatus = requestStatus
        # Related IEventResponse
        self.response = response
        # Related IEventData
        self.payload = payload
        # Related Query Parameters
        self.queryParameter = queryParameters

    @staticmethod
    @abc.abstractmethod
    def create_instance(result: dict):
        pass


class _CloudEventRequest(
    _AuthEventRequest,
        typing.Generic[response_type, payload_type]):
    def __init__(
        self,
        requestStatus: RequestStatus,
        response: response_type,
        payload: payload_type,
        statusMessage: str = None,
        queryParameters: Dict[str, str] = None,
        type: str = None,
        source: str = None,
        time: str = None,
        oDataType: str = None,
    ):
        self.type = type
        self.source = source
        self.time = time
        self.oDataType = oDataType

        super().__init__(
            requestStatus, response, payload, statusMessage, queryParameters
        )


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


# Constructs a FailedRequest .
class FailedRequest(_ActionableResponse, _Serializable):
    # Class method for creating a failed request .
    def __init__(self, error: str):
        self.error = error

    # Create a JSON - serializable representation of the failed request.
    @staticmethod
    def handle(error: Exception):
        return FailedRequest(str(error))

    # Converts to object to a dictionary
    def to_dict(self) -> dict:
        return {"error": self.error}

    # Returns a string representation of the failed request.
    def to_json(self) -> str:
        return json.dumps(self.to_dict())
