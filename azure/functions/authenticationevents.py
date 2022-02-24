from http import client
from importlib import import_module
import json
from logging import exception
import pickle
from urllib import request



from xmlrpc.client import DateTime
from azure.functions import HttpRequest
from azure.functions import HttpResponse

import typing
import urllib
from enum import Enum, auto
import uuid

from . import meta

#Utilities
def _serialize_custom_object(obj):
    """Serialize a user-defined object to JSON.

    This function gets called when `json.dumps` cannot serialize
    an object and returns a serializable dictionary containing enough
    metadata to recontrust the original object.

    Parameters
    ----------
    obj: Object
        The object to serialize

    Returns
    -------
    dict_obj: A serializable dictionary with enough metadata to reconstruct
              `obj`

    Exceptions
    ----------
    TypeError:
        Raise if `obj` does not contain a `to_json` attribute
    """
    # 'safety' guard: raise error if object does not
    # support serialization
    if not hasattr(obj, "to_json"):
        raise TypeError(f"class {type(obj)} does not expose a `to_json` "
                        "function")
    # Encode to json using the object's `to_json`
    obj_type = type(obj)
    return {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__,
        "__data__": obj_type.to_json(obj)
    }


def _deserialize_custom_object(obj: dict) -> object:
    """Deserialize a user-defined object from JSON.

    Deserializes a dictionary encoding a custom object,
    if it contains class metadata suggesting that it should be
    decoded further.

    Parameters:
    ----------
    obj: dict
        Dictionary object that potentially encodes a custom class

    Returns:
    --------
    object
        Either the original `obj` dictionary or the custom object it encoded

    Exceptions
    ----------
    TypeError
        If the decoded object does not contain a `from_json` function

        testing
    """
    if ("__class__" in obj) and ("__module__" in obj) and ("__data__" in obj):
        class_name = obj.pop("__class__")
        module_name = obj.pop("__module__")
        obj_data = obj.pop("__data__")

        # Importing the class
        module = import_module(module_name)
        class_ = getattr(module, class_name)

        if not hasattr(class_, "from_json"):
            raise TypeError(f"class {type(obj)} does not expose a `from_json` "
                            "function")

        # Initialize the object using its `from_json` deserializer
        obj = class_.from_json(obj_data)
    return obj

class RequestStatus(Enum):
     Failed = auto()
     TokenInvalid = auto()
     Successful = auto()

class IEventResponse():
    def __init__(self, HttpResponseMessage: HttpResponse,
                 Schema : str,
                 Body: str,
                 JsonBody):
                 self.HttpResponseMessage=HttpResponseMessage
                 self.Schema= Schema
                 self.Body=Body
                 self.JsonBody=JsonBody

    
    def get_Body(self):
        return self.HttpResponseMessage.get_body        

    def set_Body(self,value):
        if self.HttpResponseMessage is None:
            self.HttpResponseMessage = HttpResponse()
            self.HttpResponseMessage.__set_body(value)

    def invalidate():
        pass


    def get_JsonBody(self):
        return json.dump(self.Body)

    def set_JsonBody(self, value):
        self.Body = str(value)

    def set_JsonValue(self, paths, value):
        payload = json.dumps(self.Body)
        current = payload
        last=""
        for path in paths:
            current=current[path]
            last=path
            if current is None:
                pass #Throw exception
        
        current[path] = value
        body = str(payload)
    
    @staticmethod
    def CreateInstance(type : type, schema : str, body : str):
        response =IEventResponse(type())
        response.Schema = schema
        response.Body = body
        return response

    def populate(result: dict):
        return demo1.TokenIssuanceStartResponse(Description="test")

class IEventData():
    def __init__(self):
        pass
    @classmethod
    def GetCustomJsonConverters():
        return
    @classmethod
    def FromJson(json:str) :
        jsonString = json.loads(json)
        return IEventData(**jsonString)

    @staticmethod
    def CreateInstance(Type,json:str):
        data = IEventData(Type())
        return data if not json else data.FromJson(json)

    def populate(payload: dict):
        context=Context.populate(payload.get('context'))
        # if payload.get('apiSchemaVersion') == '10-01-2021-preview':
        return demo1.TokenIssuanceStartData(EventId=payload.get('eventListenerId'),EventTime=payload.get('time'),EventType=payload.get('type'),EventVersion=payload.get('apiSchemaVersion'),Context=context)

        


class IEventRequest():
    def __init__(self,
                HttpRequestMessage: HttpRequest,
                StatusMessage: str,
                RequestStatus: RequestStatus,
                response: IEventResponse,
                payload: IEventData,
                name: str):
        self._HttpRequestMessage=HttpRequestMessage
        self._StatusMessage=StatusMessage
        self._RequestStatus=RequestStatus
        self.response=response
        self.payload=payload
        self.name=name

    def ToString(self):
        return pickle.dumps(self)
    
    def InstanceCreated(args):
        pass

    def Failed(message: str):
        response=HttpResponse()
        response.status_code=400
        response.__set_body(message)
        return response

    def Completed(self, response: IEventResponse):
        try:
            if self._RequestStatus == RequestStatus.TokenInvalid:
                return HttpResponse(status_code=401)
            if self._RequestStatus == RequestStatus.Failed:
              return self.Failed()
            # response.Validate()
            return HttpResponse(status_code=200,body=response.JsonBody)
        except exception as ex:
            return self.Failed(ex.msg)

    def populate(result: dict):
        response=IEventResponse.populate(result=result)
        data=IEventData.populate(payload=result.get('payload'))
        tokenclaims=result.get('tokenClaims') 
        return demo1.TokenIssuanceStartRequest(payload=data,response=response,TokenClaims=tokenclaims)

class TokenIssuanceStartResponse(IEventResponse):
    def __init__(self,
                Description: str):
                self.Description=Description
    
    def get_Description(self):
        return self.Description
    
    def set_Description(self,value):
        self.Description=value

    def invalidate(self):
        self.set_JsonValue(["addition","description"], self.Description)

class AuthProtocol():
    def __init__(self,
                type: str,
                tenantId: str):
                self.type=type
                self.tenantId=tenantId

    def populate(authProtocol: dict):
        return AuthProtocol(**authProtocol)
class Client():
    def __init__(self,
                ip: str):
                self.ip=ip
    def populate(client: dict):
        return Client(**client)


class Role():
    def __init__(self,
                id: str,
                value: str):
                self.id=id
                self.value=value

class ServicePrincipalName():
    def __init__(self,
                url: str,
                uuid: uuid):
                self.url=url
                self.uuid=uuid

listOfServicePrincipalName= list[ServicePrincipalName]

class ServicePrincipal():
    def __init__(self,
                id: str,
                appId: str,
                appDisplayName: str,
                displayName: str,
                servicePrincipalNames: list[str]):
                self.id=id
                self.appId=appId
                self.appDisplayName=appDisplayName
                self.displayName=displayName
                self.servicePrincipalNames=servicePrincipalNames
    def populate(servicePrincipal: dict):
        return ServicePrincipal(**servicePrincipal)

class User():
    def __init__(self,
                ageGroup:str,
                companyName:str,
                country:str,
                createdDateTime:str,
                creationType:str,
                department:str,
                displayName:str,
                givenName:str,
                lastPasswordChangeDateTime:str,
                mail:str,
                onPremisesSamAccountName:str,
                onPremisesSecurityIdentifier:str,
                onPremiseUserPrincipalName:str,
                preferredDataLocation:str,
                preferredLanguage:str,
                surname:str,
                userPrincipalName:str,
                userType:str,
                id:str):
                self.id=id
                self.userType=userType
                self.userPrincipalName=userPrincipalName
                self.surname=surname
                self.preferredLanguage=preferredLanguage
                self.ageGroup=ageGroup
                self.companyName=companyName
                self.country=country
                self.createdDateTime=createdDateTime
                self.creationType=creationType
                self.department=department
                self.displayName=displayName
                self.givenName=givenName
                self.lastPasswordChangeDateTime=lastPasswordChangeDateTime
                self.mail=mail
                self.onPremisesSamAccountName=onPremisesSamAccountName
                self.onPremisesSecurityIdentifier=onPremisesSecurityIdentifier
                self.onPremiseUserPrincipalName=onPremiseUserPrincipalName
                self.preferredDataLocation=preferredDataLocation

    def populate(user: dict):
        return User(**user)

                

Roles=list[Role]


class Context():
    def __init__(self,
                CorrelationId:str,
                Client:Client,
                AuthProtocol:AuthProtocol,
                ClientServicePrincipal: ServicePrincipal,
                ResourceServicePrincipal: ServicePrincipal,
                Roles: Roles,
                User: User):
                self.User=User
                self.Roles=Roles
                self.ResourceServicePrincipal=ResourceServicePrincipal
                self.ClientServicePrincipal=ClientServicePrincipal
                self.AuthProtocol=AuthProtocol
                self.Client=Client
                self.CorrelationId=CorrelationId
    
    def populate(context: dict):
        user=User.populate(context.get('user'))
        client=Client.populate(context.get('client'))
        authProtocol=AuthProtocol.populate(context.get('authProtocol'))
        clientServicePrincipal=ServicePrincipal.populate(context.get('clientServicePrincipal'))
        resourceServicePrincipal=ServicePrincipal.populate(context.get('resourceServicePrincipal'))
        return Context(CorrelationId=context.get('correlationId'),User=user,Client=client,ClientServicePrincipal=clientServicePrincipal,ResourceServicePrincipal=resourceServicePrincipal,Roles=context.get('roles'),AuthProtocol=authProtocol)

class TokenIssuanceStartData(IEventData):
    def __init__(self,
                EventId: uuid,
                EventTime: DateTime,
                EventVersion: str,
                EventType: str,
                Context: str):
                self.Context=Context
                self.EventType=EventType
                self.EventVersion=EventVersion
                self.EventTime=EventTime
                self.EventId=EventId



class TokenIssuanceStartRequest(IEventRequest):
    def __init__(self,
                response: TokenIssuanceStartResponse,
                payload: TokenIssuanceStartData,
                TokenClaims: dict[str,str]):
                self.TokenClaims=TokenClaims
                self.response=response
                self.payload=payload

    def InstanceCreated(self,args: list):
        self.TokenClaims=args[0]


class demo1():
    class TokenIssuanceStartResponse(IEventResponse):
        def __init__(self,
                    Description: str):
                    self.Description=Description
        
        def get_Description(self):
            return self.Description
        
        def set_Description(self,value):
            self.Description=value

        def invalidate(self):
            self.set_JsonValue(["addition","description"], self.Description)

    class TokenIssuanceStartData(IEventData):
        def __init__(self,
                    EventId: str,
                    EventTime: DateTime,
                    EventVersion: str,
                    EventType: str,
                    Context: Context):
                    self.Context=Context
                    self.EventType=EventType
                    self.EventVersion=EventVersion
                    self.EventTime=EventTime
                    self.EventId=EventId



    class TokenIssuanceStartRequest(IEventRequest):
        def __init__(self,
                    response: TokenIssuanceStartResponse,
                    payload: TokenIssuanceStartData,
                    TokenClaims: dict[str,str]):
                    self.TokenClaims=TokenClaims
                    self.response=response
                    self.payload=payload

        def InstanceCreated(self,args: list):
            self.TokenClaims=args[0]

    #def populte()

def populate(result: dict):
     
     payload=result.get('payload')
     contextDict=payload.get('context')
     userDict=contextDict.get('user')
     user=User(**userDict)
     authProtocolDict=contextDict.get('authProtocol')
     a=AuthProtocol(**authProtocolDict)
     clientServicePrincipalDict=contextDict.get('clientServicePrincipal')
     clientServicePrincipal=ServicePrincipal(**clientServicePrincipalDict)
     resourceServicePrincipalDict=contextDict.get('resourceServicePrincipal')
     resourceServicePrincipal=ServicePrincipal(**resourceServicePrincipalDict)
     clientDict=contextDict.get('client')
     client=Client(**clientDict)

     context=Context(CorrelationId=contextDict.get('correlationId'),User=user,Client=client,ClientServicePrincipal=clientServicePrincipal,ResourceServicePrincipal=resourceServicePrincipal,Roles=contextDict.get('roles'),AuthProtocol=a)
     
     data=demo1.TokenIssuanceStartData(EventId=payload.get('eventListenerId'),EventTime=payload.get('time'),EventType=payload.get('type'),EventVersion=payload.get('apiSchemaVersion'),Context=context)
     response=demo1.TokenIssuanceStartResponse(Description="test")
     
     tokenclaims=result.get('tokenClaims') 
     request=demo1.TokenIssuanceStartRequest(payload=data,response=response,TokenClaims=tokenclaims)
     resp=result.get('response')
     statusMessage=result.get('statusMessage')
     
    
        
          

        
# Authentication Event Trigger
class AuthenticationEventTriggerConverter(meta.InConverter,
                               meta.OutConverter,
                               binding='authenticationEventTrigger',
                               trigger=True):
    @classmethod
    def check_input_type_annotation(cls, pytype):
        # Activity Trigger's arguments should accept any types
        return True

    @classmethod
    def check_output_type_annotation(cls, pytype):
        # The activity trigger should accept any JSON serializable types
        return True

    @classmethod
    def decode(cls,
               data: meta.Datum, *,
               trigger_metadata) -> typing.Any:
        # result=demo1.TokenIssuanceStartRequest()
        data_type = data.type

        # Durable functions extension always returns a string of json
        # See durable functions library's call_activity_task docs
        if data_type in ['string', 'json']:
            try:
                # callback = _deserialize_custom_object
                result = json.loads(data.value)
                # populate(result=result)
                test=IEventRequest.populate(result=result)
            except json.JSONDecodeError:
                # String failover if the content is not json serializable
                result = data.value
            except Exception:
                raise ValueError(
                    'authentication event trigger input must be a string or a '
                    f'valid json serializable ({data.value})')
        else:
            raise NotImplementedError(
                f'unsupported authentication event trigger payload type: {data_type}')

        return result

    @classmethod
    def encode(cls, obj: typing.Any, *,
               expected_type: typing.Optional[type]) -> meta.Datum:
        try:
            callback = _serialize_custom_object
            result = json.dumps(obj, default=callback)
        except TypeError:
            raise ValueError(
                f'authentication event trigger output must be json serializable ({obj})')

        return meta.Datum(type='json', value=result)

    @classmethod
    def has_implicit_output(cls) -> bool:
        return True


