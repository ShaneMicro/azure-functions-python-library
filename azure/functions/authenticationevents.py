import json
import typing
from azure.functions.authentication_events.token_issuance_start import preview_10_01_2021  # noqa: E501
from azure.functions import authentication_events as _abc
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
                    if response.get("payload").get('type') == 'onTokenIssuanceStartCustomExtension':  # noqa: E501
                        if response.get('payload').get("apiSchemaVersion") == "10-01-2021-preview":  # noqa: E501
                            try:
                                return preview_10_01_2021.TokenIssuanceStartRequest.create_instance(result=response)  # noqa: E501
                            except Exception:
                                raise ValueError('authentication event trigger input must be a string or a 'f'valid json serializable ({data.value})')  # noqa: E501
                        else:
                            raise ValueError('Version not supported')
                    else:
                        raise ValueError('Event type not supported')
                else:
                    raise ValueError('request data does not contain payload')

            except json.JSONDecodeError:
                response = data.value
        else:
            raise NotImplementedError(
                f'unsupported authentication event trigger payload type: {data_type}')  # noqa: E501

        return response

    @classmethod
    def encode(cls, obj: typing.Any, *,
               expected_type: typing.Optional[type]) -> meta.Datum:
        # only serialize if incoming object is of response type.
        if not isinstance(obj, _abc._IAuthenticationEventResponse):
            raise ValueError('Object should be of valid response type')
        # only serialize if incoming object is serializable
        if not isinstance(obj, _abc._Serializable):
            raise ValueError('Object was not of expected type Serializable')

        try:
            # convert incoming object to json string
            result = obj.to_json()
        except TypeError:
            raise ValueError(
                f'authentication event trigger output must be json serializable ({obj})')  # noqa: E501

        return meta.Datum(type='json', value=result)

    @classmethod
    def has_implicit_output(cls) -> bool:
        return True
