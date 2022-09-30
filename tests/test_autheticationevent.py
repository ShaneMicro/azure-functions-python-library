import unittest
import json
import azure.functions.authentication_events.token_issuance_start as token_issuance_start  # noqa: E501
from azure.functions.authenticationevents import (
    AuthenticationEventTriggerConverter,
)  # noqa: E501
from azure.functions.meta import Datum
import azure.functions.authentication_events as _abc
from .resource import AuthenticationEventsResources
from azure.functions.authentication_events import events


class TestAuthenticationEvents(unittest.TestCase):
    def test_object_creation_payload(self):
        onTokenIssuanceStartRequest = events.deserialize(
            AuthenticationEventsResources.request_data
        )
        self.assertEqual(onTokenIssuanceStartRequest.queryParameter.get('code'),"mNEwqtM0t7ZzNDn4IoJGy51dNlZb-7Pu0hJPFzzBi703AzFus9_flQ==")
        self.assertEqual(onTokenIssuanceStartRequest.queryParameter.get('functionName'),"onTokenIssuanceString")

        self.assertEqual(
            onTokenIssuanceStartRequest.queryParameter.get("code"),
            "mNEwqtM0t7ZzNDn4IoJGy51dNlZb-7Pu0hJPFzzBi703AzFus9_flQ==",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.queryParameter.get("functionName"),
            "onTokenIssuanceString",
        )

        self.assertEqual(
            onTokenIssuanceStartRequest.payload.customAuthenticationExtensionId,
            "10000000-0000-0000-0000-000000000002",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationEventListenerId,
            "10000000-0000-0000-0000-000000000001",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.type,
            "microsoft.graph.authenticationEvent.TokenIssuanceStart",
        )

    def test_object_creation_payload_context(self):
        onTokenIssuanceStartRequest = events.deserialize(
            AuthenticationEventsResources.request_data
        )

        self.assertEqual(
            onTokenIssuanceStartRequest.payload
            .authenticationContext.correlationId,
            "20000000-0000-0000-0000-000000000002",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext
            .client.ip,
            "127.0.0.1",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.clientServicePrincipal.id,  # noqa: E501
            "40000000-0000-0000-0000-000000000001",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.clientServicePrincipal.appDisplayName,  # noqa: E501
            "Testclientapp",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.clientServicePrincipal.displayName,  # noqa: E501
            "Testclientapplication",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.clientServicePrincipal.appId,  # noqa: E501
            "40000000-0000-0000-0000-000000000002",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.resourceServicePrincipal.id,  # noqa: E501
            "40000000-0000-0000-0000-000000000003",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.resourceServicePrincipal.appId,  # noqa: E501
            "40000000-0000-0000-0000-000000000004",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.resourceServicePrincipal.appDisplayName,  # noqa: E501
            "Testresourceapp",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.resourceServicePrincipal.displayName,  # noqa: E501
            "Testresourceapplication",
        )
        

    def test_object_creation_payload_context_user(self):

        json_data = json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest = (
            token_issuance_start.TokenIssuanceStartRequest.create_instance(
                result=json_data
            )
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.user.id,
            "60000000-0000-0000-0000-000000000006",
        )
        
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext
            .user.country,
            "USA",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext
            .user.companyName,
            "NickGomez",
        )
    
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext
            .user.displayName,
            "Dummydisplayname",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext
            .user.givenName,
            "Example",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext
            .user.mail,
            "test@example.com",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.user.onPremisesSamAccountName,  # noqa: E501
            "testadmin",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.user.onPremisesSecurityIdentifier,  # noqa: E501
            "DummySID",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.user.onPremiseUserPrincipalName,  # noqa: E501
            None,
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.user.preferredDataLocation,  # noqa: E501
            "DummyDataLocation",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext
            .user.preferredLanguage,
            "DummyLanguage",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext
            .user.surname,
            "Test",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext
            .user.userPrincipalName,
            "testadmin@example.com",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext
            .user.userType,
            "UserTypeCloudManaged",
        )

    def test_response_serialization(self):

        json_data = json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest = (
            token_issuance_start.TokenIssuanceStartRequest.create_instance(
                result=json_data
            )
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.authenticationContext.user.id,
            "60000000-0000-0000-0000-000000000006",
        )

        # get the json string from response
        result = onTokenIssuanceStartRequest.response.to_json()
        # convert the expected json string to json dict
        expected_result_dict = json.loads(
            AuthenticationEventsResources.response_data
        )  # noqa: E501
        # set actions in the json dict to empty list
        expected_result_dict["data"]["actions"] = []
        # get json string from the json dict
        expected_result_str = json.dumps(expected_result_dict)
        # validate json string from the to_json function to expected json string  # noqa: E501
        self.assertEqual(result, expected_result_str)

    def test_decode_function(self):
        datum = Datum(
            value=AuthenticationEventsResources.request_data, type="string")
        out = AuthenticationEventTriggerConverter.decode(
            datum, trigger_metadata=None
        )  # noqa: E501
        self.assertTrue(
            isinstance(out, token_issuance_start.TokenIssuanceStartRequest)
        )  # noqa: E501

    def test_decode_event_type(self):
        data_dict = json.loads(AuthenticationEventsResources.request_data)
        data_dict["type"] = "Negative test string"
        datum = Datum(value=json.dumps(data_dict), type="string")
        with self.assertRaisesRegex(
            Exception, AuthenticationEventsResources.negative_event_type
        ):
            AuthenticationEventTriggerConverter.decode(
                datum, trigger_metadata=None
            )  # noqa: E501

    def test_decode_payload_type(self):
        data_dict = json.loads(AuthenticationEventsResources.request_data)
        data_dict["payload"]["apiSchemaVersion"] = "Negative test string"
        datum = Datum(value=json.dumps(data_dict), type="object")
        with self.assertRaisesRegex(
            Exception,
            "unsupported authentication event trigger event type: object"
        ):  # noqa: E501
            AuthenticationEventTriggerConverter.decode(
                datum, trigger_metadata=None
            )  # noqa: E501

    def test_encode_object_type(self):
        json_data = json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest = (
            token_issuance_start.TokenIssuanceStartRequest.create_instance(
                result=json_data
            )
        )
        with self.assertRaisesRegex(
            Exception, "Object should be of valid response type"
        ):  # noqa: E501
            AuthenticationEventTriggerConverter.encode(
                obj=onTokenIssuanceStartRequest, expected_type="object"
            )  # noqa: E501

    def test_encode_object_typ(self):
        response = _abc._AuthEventResponse(
            ODataType="test", body='{"test":"Not serializable"}'
        )
        with self.assertRaisesRegex(
            Exception, "Object was not of expected type Serializable"
        ):
            AuthenticationEventTriggerConverter.encode(
                obj=response, expected_type="object"
            )
