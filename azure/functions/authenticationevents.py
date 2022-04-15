from importlib import import_module
import json
from logging import exception
from re import T
from this import d 
import typing
import azure.functions.authentication_events.token_issuance_start.preview_10_01_2021 as preview_10_01_2021
import azure.functions.authentication_events as _abc


from . import meta

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
                response = json.loads(data.value)

                if "payload" in response:
                    if response.get("payload").get('type') =='onTokenIssuanceStartCustomExtension':
                        if response.get('payload').get("apiSchemaVersion") == "10-01-2021-preview":
                            try:
                                return preview_10_01_2021.TokenIssuanceStartRequest.create_instance(result=response)
                            except Exception:
                                raise ValueError('authentication event trigger input must be a string or a 'f'valid json serializable ({data.value})')
                        else:
                            raise ValueError('Version not supported')
                    else:
                        raise ValueError('Event type not supported')
                else:
                    raise ValueError('request data does not contain payload')

            
                
            except json.JSONDecodeError:
                result = data.value  
        else:
            raise NotImplementedError(
                f'unsupported authentication event trigger payload type: {data_type}')

        return response

    @classmethod
    def encode(cls, obj: typing.Any, *,
               expected_type: typing.Optional[type]) -> meta.Datum:
        
        if not isinstance(obj,_abc._IAuthenticationEventResponse):
            raise ValueError('Object should be of valid response type')
        if not isinstance(obj,_abc._Serializable):
            raise ValueError('Object was not of expected type Serializable')
       
        try:
            result = obj.to_json()
        except TypeError:
            raise ValueError(
                f'authentication event trigger output must be json serializable ({obj})')

        return meta.Datum(type='json', value=result)

    @classmethod
    def has_implicit_output(cls) -> bool:
        return True
