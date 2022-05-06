import unittest
import json
import azure.functions.authentication_events.token_issuance_start.preview_10_01_2021 as preview_10_01_2021  # noqa: E501
from azure.functions.authenticationevents import AuthenticationEventTriggerConverter  # noqa: E501
from azure.functions.meta import Datum
import azure.functions.authentication_events as _abc
from .resource import AuthenticationEventsResources


class TestauthenticationEvents(unittest.TestCase):
    def test_object_creation_payload(self):

        json_data = json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest = (
            preview_10_01_2021.TokenIssuanceStartRequest.create_instance(
                result=json_data
            )
        )

        self.assertEqual(
            onTokenIssuanceStartRequest.payload.apiSchemaVersion,
            "10-01-2021-preview"
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.customExtensionId,
            "10000000-0000-0000-0000-000000000001",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.eventListenerId,
            "10000000-0000-0000-0000-000000000001",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.type,
            "onTokenIssuanceStartCustomExtension",
        )

    def test_object_creation_payload_context(self):

        json_data = json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest = (
            preview_10_01_2021.TokenIssuanceStartRequest.create_instance(
                result=json_data
            )
        )

        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.correlationId,
            "20000000-0000-0000-0000-000000000002",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.client.ip, "127.0.0.1"
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.authProtocol.tenantId,
            "30000000-0000-0000-0000-000000000003",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.authProtocol.type,
            "OAUTH2.0"
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.clientServicePrincipal.id,  # noqa: E501
            "40000000-0000-0000-0000-000000000001",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.clientServicePrincipal.appDisplayName,  # noqa: E501
            "Test client app",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.clientServicePrincipal.displayName,  # noqa: E501
            "Test client application",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.clientServicePrincipal.appId,  # noqa: E501
            "40000000-0000-0000-0000-000000000002",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.clientServicePrincipal.servicePrincipalNames,  # noqa: E501
            ["40000000-0000-0000-0000-000000000002", "http://example.com/client/app1"],  # noqa: E501
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.resourceServicePrincipal.id,  # noqa: E501
            "40000000-0000-0000-0000-000000000003",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.resourceServicePrincipal.appId,  # noqa: E501
            "40000000-0000-0000-0000-000000000004",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.resourceServicePrincipal.appDisplayName,  # noqa: E501
            "Test resourceapp",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.resourceServicePrincipal.displayName,  # noqa: E501
            "Test resourceapplication",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.resourceServicePrincipal.servicePrincipalNames,  # noqa: E501
            ["40000000-0000-0000-0000-000000000004", "https://example.com/resource2"],  # noqa: E501
        )

    def test_object_creation_payload_context_user(self):

        json_data = json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest = (
            preview_10_01_2021.TokenIssuanceStartRequest.create_instance(
                result=json_data
            )
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.id,
            "60000000-0000-0000-0000-000000000006",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.ageGroup, "Adult"
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.country, "USA"
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.companyName,
            "Evo Sts Test"
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.department,
            "Dummy department",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.creationType,
            "Invitation"
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.department,
            "Dummy department",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.displayName,
            "Dummy display name",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.givenName,
            "Example"
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.mail,
            "test@example.com"
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.onPremisesSamAccountName,  # noqa: E501
            "testadmin",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.onPremisesSecurityIdentifier,  # noqa: E501
            "DummySID",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.onPremiseUserPrincipalName,  # noqa: E501
            "Dummy Name",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.preferredDataLocation,  # noqa: E501
            "DummyDataLocation",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.preferredLanguage,
            "DummyLanguage",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.surname, "Test"
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.userPrincipalName,
            "testadmin@example.com",
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.userType,
            "UserTypeCloudManaged",
        )

    def test_response_serialiation(self):

        json_data = json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest = (
            preview_10_01_2021.TokenIssuanceStartRequest.create_instance(
                result=json_data
            )
        )
        self.assertEqual(
            onTokenIssuanceStartRequest.payload.context.user.id,
            "60000000-0000-0000-0000-000000000006",
        )

        # get the json string from response
        result = onTokenIssuanceStartRequest.response.to_json()
        # convert the expected json string to json dict
        expected_result_dict = json.loads(AuthenticationEventsResources.response_data)  # noqa: E501
        # set actions in the json dict to empty list
        expected_result_dict["actions"] = []
        # get json string from the json dict
        expected_result_str = json.dumps(expected_result_dict)
        # validate json string from the to_json function to expected json string  # noqa: E501
        self.assertEqual(result, expected_result_str)

    def test_decode_function(self):
        datum = Datum(
            value=AuthenticationEventsResources.request_data,
            type="string")
        out = AuthenticationEventTriggerConverter.decode(datum, trigger_metadata=None)  # noqa: E501
        self.assertTrue(isinstance(out, preview_10_01_2021.TokenIssuanceStartRequest))  # noqa: E501

    def test_decode_event_type(self):
        data_dict = json.loads(AuthenticationEventsResources.request_data)
        data_dict["payload"]["type"] = "Negative test string"
        datum = Datum(value=json.dumps(data_dict), type="string")
        with self.assertRaisesRegex(Exception, "Event type not supported"):
            AuthenticationEventTriggerConverter.decode(datum, trigger_metadata=None)  # noqa: E501

    def test_decode_api_schema_version(self):
        data_dict = json.loads(AuthenticationEventsResources.request_data)
        data_dict["payload"]["apiSchemaVersion"] = "Negative test string"
        datum = Datum(value=json.dumps(data_dict), type="string")
        with self.assertRaisesRegex(Exception, "Version not supported"):
            AuthenticationEventTriggerConverter.decode(datum, trigger_metadata=None)  # noqa: E501

    def test_decode_payload_type(self):
        data_dict = json.loads(AuthenticationEventsResources.request_data)
        data_dict["payload"]["apiSchemaVersion"] = "Negative test string"
        datum = Datum(value=json.dumps(data_dict), type="object")
        with self.assertRaisesRegex(Exception, "unsupported authentication event trigger payload type:"):  # noqa: E501
            AuthenticationEventTriggerConverter.decode(datum, trigger_metadata=None)  # noqa: E501

    def test_encode_object_type(self):
        json_data = json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest = (
            preview_10_01_2021.TokenIssuanceStartRequest.create_instance(
                result=json_data
            )
        )
        with self.assertRaisesRegex(Exception, "Object should be of valid response type"):  # noqa: E501
            AuthenticationEventTriggerConverter.encode(obj=onTokenIssuanceStartRequest, expected_type="object")  # noqa: E501

    def test_encode_object_typ(self):
        response = _abc._IEventResponse(
            schema="test", body='{"test":"Not serializable"}'
        )
        with self.assertRaisesRegex(
            Exception, "Object was not of expected type Serializable"
        ):
            AuthenticationEventTriggerConverter.encode(
                obj=response, expected_type="object"
            )
