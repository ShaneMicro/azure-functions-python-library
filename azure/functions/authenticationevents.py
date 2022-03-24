from abc import ABC, abstractmethod
from http import client
from importlib import import_module
import json
from logging import exception
from re import T
from this import d 
import azure.functions._abc as _abc
import azure.functions._authenticationevents as _authenticationevents
import typing
import urllib
from enum import Enum, auto
import uuid

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
                if response.get("payload").get('type') =='onTokenIssuanceStartCustomExtension' and response.get('payload').get("apiSchemaVersion") == "10-01-2021-preview":
                    return _authenticationevents.preview_10_01_2021.TokenIssuanceStartRequest.create_instance(result=response)
            
                # test=IEventRequest.populate(result=result)
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

        return response

    @classmethod
    def encode(cls, obj: typing.Any, *,
               expected_type: typing.Optional[type]) -> meta.Datum:
        try:
            if not isinstance(obj,_abc.Serializable):
                raise ValueError('Object was not of expected type Serializable')
            result = obj.to_json()
           
        except TypeError:
            raise ValueError(
                f'authentication event trigger output must be json serializable ({obj})')

        return meta.Datum(type='json', value=result)

    @classmethod
    def has_implicit_output(cls) -> bool:
        return True


