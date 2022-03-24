from abc import ABC, abstractmethod
from cProfile import label
import json
import typing
import azure.functions._abc as _abc
from xmlrpc.client import DateTime
import uuid


class ITokenIssuanceAction(_abc.IAuthenticationEventAction):
    def __init__(self,
                 actionType):
        self.actionType = actionType


class Claim(_abc.Serializable):
    def __init__(self,
                 id: str,
                 values: list[str]):
        self.id = id
        self.values = values

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.values
        }

    def to_json(self):
        return json.dumps(self.to_dict())


class ProvideClaimsForToken(ITokenIssuanceAction, _abc.Serializable):
    def __init__(self,
                 claims: list[Claim]):
        self.actionType = "ProvideClaimsForToken"
        self.claims = claims

    def to_dict(self):
        return {
            "actionType": self.actionType,
            "claims": dict(map(lambda c: c.to_dict(), self.claims))
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def add_claim(self, id: str, values: list[str]):
        self.claims.append(Claim(Id=id, Values=values))

    def build_action_body(self):
        temp: dict
        for item in self.claims:
            temp[item.Id] = item.Values
        return json.dumps(temp)


class AuthProtocol():
    def __init__(self,
                 type: str,
                 tenantId: str):
        self.type = type
        self.tenantId = tenantId

    def populate(authProtocol: dict):
        return AuthProtocol(**authProtocol)


class Client():
    def __init__(self,
                 ip: str):
        self.ip = ip

    def populate(client: dict):
        return Client(**client)


class Role():
    def __init__(self,
                 id: str,
                 value: str):
        self.id = id
        self.value = value


class ServicePrincipalName():
    def __init__(self,
                 url: str,
                 uuid: uuid):
        self.url = url
        self.uuid = uuid


listOfServicePrincipalName = list[ServicePrincipalName]


class ServicePrincipal():
    def __init__(self,
                 id: str,
                 appId: str,
                 appDisplayName: str,
                 displayName: str,
                 servicePrincipalNames: list[str]):
        self.id = id
        self.appId = appId
        self.appDisplayName = appDisplayName
        self.displayName = displayName
        self.servicePrincipalNames = servicePrincipalNames

    def populate(servicePrincipal: dict):
        return ServicePrincipal(**servicePrincipal)


class User():
    def __init__(self,
                 ageGroup: str,
                 companyName: str,
                 country: str,
                 createdDateTime: str,
                 creationType: str,
                 department: str,
                 displayName: str,
                 givenName: str,
                 lastPasswordChangeDateTime: str,
                 mail: str,
                 onPremisesSamAccountName: str,
                 onPremisesSecurityIdentifier: str,
                 onPremiseUserPrincipalName: str,
                 preferredDataLocation: str,
                 preferredLanguage: str,
                 surname: str,
                 userPrincipalName: str,
                 userType: str,
                 id: str):
        self.id = id
        self.userType = userType
        self.userPrincipalName = userPrincipalName
        self.surname = surname
        self.preferredLanguage = preferredLanguage
        self.ageGroup = ageGroup
        self.companyName = companyName
        self.country = country
        self.createdDateTime = createdDateTime
        self.creationType = creationType
        self.department = department
        self.displayName = displayName
        self.givenName = givenName
        self.lastPasswordChangeDateTime = lastPasswordChangeDateTime
        self.mail = mail
        self.onPremisesSamAccountName = onPremisesSamAccountName
        self.onPremisesSecurityIdentifier = onPremisesSecurityIdentifier
        self.onPremiseUserPrincipalName = onPremiseUserPrincipalName
        self.preferredDataLocation = preferredDataLocation

    def populate(user: dict):
        return User(**user)


Roles = list[Role]


class Context():
    def __init__(self,
                 correlationId: str,
                 client: Client,
                 authProtocol: AuthProtocol,
                 clientServicePrincipal: ServicePrincipal,
                 resourceServicePrincipal: ServicePrincipal,
                 roles: Roles,
                 user: User):
        self.user = user
        self.roles = roles
        self.resourceServicePrincipal = resourceServicePrincipal
        self.clientServicePrincipal = clientServicePrincipal
        self.authProtocol = authProtocol
        self.client = client
        self.correlationId = correlationId

    def populate(context: dict):
        return Context(correlationId=context.get('correlationId'),
                       user=User.populate(context.get('user')),
                       client=Client.populate(context.get('client')),
                       clientServicePrincipal=ServicePrincipal.populate(
                           context.get('clientServicePrincipal')),
                       resourceServicePrincipal=ServicePrincipal.populate(
                           context.get('resourceServicePrincipal')),
                       roles=context.get('roles'),
                       authProtocol=AuthProtocol.populate(context.get('authProtocol')))


class preview_10_01_2021():
    class TokenIssuanceStartResponse(_abc.IAuthenticationEventIActionableResponse[ITokenIssuanceAction],_abc.Serializable):
        def __init__(self,
                     schema: typing.Optional[str],
                     body: typing.Optional[str],
                     actions: list[ITokenIssuanceAction]):

            super().__init__(schema=schema, body=body, actions=actions)

        def create_instance(response: dict):
            return preview_10_01_2021.TokenIssuanceStartResponse(schema=response.get('schema'), body=response.get('body'), actions=[])

        def to_dict(self):
            return {
                "actions": dict(map(lambda a:a.to_dict(),self.actions)),
                "schema": self.schema,
                "body":self.body
            }

        def to_json(self):
           return json.dumps(self.to_dict())

    class TokenIssuanceStartData(_abc.IAuthenticationEventData):
        def __init__(self,
                     eventListenerId: typing.Optional[str],
                     time: typing.Optional[str],
                     apiSchemaVersion: typing.Optional[str],
                     etype: typing.Optional[str],
                     context: Context,
                     customExtensionId: typing.Optional[str]):
            self.context = context
            super().__init__(eventListenerId=eventListenerId, time=time, etype=etype,
                             apiSchemaVersion=apiSchemaVersion, customExtensionId=customExtensionId)

        def create_instance(payload: dict):
            return preview_10_01_2021.TokenIssuanceStartData(eventListenerId=payload.get('eventListenerId'), time=payload.get('time'), etype=payload.get('type'), apiSchemaVersion=payload.get('apiSchemaVersion'), context=Context.populate(payload.get('context')), customExtensionId=payload.get('customExtensionId'))

    class TokenIssuanceStartRequest(_abc.IAuthenticationEventRequest[TokenIssuanceStartResponse, TokenIssuanceStartData]):
        def __init__(self,
                     statusMessage: str,
                     requestStatus: _abc.AuthenticationEventRequestStatus,
                     response: _abc.response_type,
                     payload: _abc.payload_type,
                     tokenClaims: dict[str, str]):

            super().__init__(statusMessage=statusMessage, requestStatus=requestStatus,
                             response=response, payload=payload, name="")
            self.tokenClaims = tokenClaims

        def create_instance(result: dict):
            response = preview_10_01_2021.TokenIssuanceStartResponse.create_instance(
                response=result.get('response'))
            data = preview_10_01_2021.TokenIssuanceStartData.create_instance(
                payload=result.get('payload'))
            tokenclaims = result.get('tokenClaims')
            return preview_10_01_2021.TokenIssuanceStartRequest(statusMessage=result.get("statusMessage"), requestStatus=_abc.AuthenticationEventRequestStatus(result.get("requestStatus")), response=response, payload=data, tokenClaims=tokenclaims)
