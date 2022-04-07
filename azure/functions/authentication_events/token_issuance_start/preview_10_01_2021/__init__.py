import json

from .data import Context
from ...token_issuance_start import _ITokenIssuanceAction
from ....authentication_events import _IAuthenticationEventIActionableResponse, _Serializable, _IAuthenticationEventData, _IAuthenticationEventRequest, AuthenticationEventRequestStatus, _response_type, _payload_type


class TokenIssuanceStartResponse(_IAuthenticationEventIActionableResponse[_ITokenIssuanceAction], _Serializable):
    def __init__(self,
                 schema: str,
                 body: str,
                 actions: list[_ITokenIssuanceAction]):

        super().__init__(schema=schema, body=body, actions=actions)

    def create_instance(response: dict):
        return TokenIssuanceStartResponse(schema=response.get('schema'), body=response.get('body'), actions=[])

    def to_dict(self):
        return {
            "actions": list(map(lambda a: a.to_dict(), self.actions)),
            "schema": self.schema,
            "body": self.body
        }

    def to_json(self):
        return json.dumps(self.to_dict())


class TokenIssuanceStartData(_IAuthenticationEventData):
    def __init__(self,
                 eventListenerId: str,
                 time: str,
                 apiSchemaVersion: str,
                 eventType: str,
                 context: Context,
                 customExtensionId: str):
        self.context = context
        super().__init__(eventListenerId=eventListenerId, time=time, eventType=eventType,
                         apiSchemaVersion=apiSchemaVersion, customExtensionId=customExtensionId)

    def create_instance(payload: dict):
        return TokenIssuanceStartData(eventListenerId=payload.get('eventListenerId'), time=payload.get('time'), eventType=payload.get('type'), apiSchemaVersion=payload.get('apiSchemaVersion'), context=Context.populate(payload.get('context')), customExtensionId=payload.get('customExtensionId'))


class TokenIssuanceStartRequest(_IAuthenticationEventRequest[TokenIssuanceStartResponse, TokenIssuanceStartData]):
    def __init__(self,
                 statusMessage: str,
                 requestStatus: AuthenticationEventRequestStatus,
                 response: _response_type,
                 payload: _payload_type,
                 tokenClaims: dict[str, str]):

        super().__init__(statusMessage=statusMessage,
                         requestStatus=requestStatus, response=response, payload=payload)
        self.tokenClaims = tokenClaims

    def create_instance(result: dict):
        response = TokenIssuanceStartResponse.create_instance(
            response=result.get('response'))
        data = TokenIssuanceStartData.create_instance(
            payload=result.get('payload'))
        tokenclaims = result.get('tokenClaims')
        return TokenIssuanceStartRequest(statusMessage=result.get("statusMessage"), requestStatus=AuthenticationEventRequestStatus(result.get("requestStatus")), response=response, payload=data, tokenClaims=tokenclaims)
