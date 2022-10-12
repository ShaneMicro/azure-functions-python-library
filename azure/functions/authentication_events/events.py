# A list of supported events and there type keys
import json
from multiprocessing.managers import ValueProxy

from azure.functions.authentication_events import _AuthEventResponse, _Serializable # NOQA E501
from .token_issuance_start import TokenIssuanceStartRequest


__events = {
    "onTokenIssuanceStartCustomExtension": TokenIssuanceStartRequest,
    "microsoft.graph.authenticationEvent.TokenIssuanceStart": TokenIssuanceStartRequest # NOQA E501
}


def deserialize(value):
    if value == "" or value is None:
        raise ValueError("The incoming request does not contain any data")

    incoming = json.loads(value)
    #TODO: check status
    
    if incoming.get("requestStatus") == "Failed":
        raise ValueError(incoming.get("statusMessage"))
    for key in __events:
        if incoming.get("type").lower() == key.lower():
            try:
                return __events[key].create_instance(result=incoming)
            except Exception:
                raise ValueError(
                    "authentication event trigger input must be a string or a "
                    f"valid json serializable ({value})"
                )

    raise ValueError(
        "Event type '%s' not supported, supported event types are '%s'"
        % (incoming.get("type"), "', '".join(key for key in __events))
    )
    


def serialize(obj):
    # only serialize if incoming object is of response type.
    if not isinstance(obj, _AuthEventResponse):
        raise ValueError("Object should be of valid response type")
    # only serialize if incoming object is serializable
    if not isinstance(obj, _Serializable):
        raise ValueError("Object was not of expected type Serializable")

    try:
        # convert incoming object to json string
        return obj.to_json()
    except TypeError:
        raise ValueError(
            "Authentication event trigger output must be json serializable "
            f"({obj})"
        )
