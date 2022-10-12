import json
import typing
from .authentication_events import events
from . import meta


# Authentication Event Trigger
class AuthenticationEventTriggerConverter(
    meta.InConverter,
    meta.OutConverter,
    binding="authenticationEventsTrigger",
    trigger=True,
):
    @classmethod
    def check_input_type_annotation(cls, pytype):
        # Activity Trigger's arguments should accept any types
        return True

    @classmethod
    def check_output_type_annotation(cls, pytype):
        # The activity trigger should accept any JSON serializable types
        return True

    @classmethod
    def decode(cls, data: meta.Datum, *, trigger_metadata) -> typing.Any:
        # result=demo1.TokenIssuanceStartRequest()
        data_type = data.type

        # Durable functions extension always returns a string of json
        # See durable functions library's call_activity_task docs
        if data_type in ["string", "json"]:
            try:
                # callback = _deserialize_custom_object
                return events.deserialize(data.value)
            except json.JSONDecodeError:
                response = data.value
        else:
            raise NotImplementedError(
                "unsupported authentication event trigger event type: "
                f"{data_type}"
            )  # noqa: E501

        return response

    @classmethod
    def encode(
        cls, obj: typing.Any, *, expected_type: typing.Optional[type]
    ) -> meta.Datum:
        return meta.Datum(type="json", value=events.serialize(obj))

    @classmethod
    def has_implicit_output(cls) -> bool:
        return True
