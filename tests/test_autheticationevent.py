
import unittest
import json
import azure.functions.authentication_events.token_issuance_start.preview_10_01_2021 as preview_10_01_2021 
from azure.functions.authenticationevents import AuthenticationEventTriggerConverter
from azure.functions.meta import Datum
import azure.functions.authentication_events as _abc
from .resource import AuthenticationEventsResources

class TestAuthenticationEvents(unittest.TestCase):
    
    def test_object_creation_payload(self):
        
        json_data=json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest=preview_10_01_2021.TokenIssuanceStartRequest.create_instance(result=json_data)
        
        self.assertEqual(onTokenIssuanceStartRequest.payload.apiSchemaVersion,'10-01-2021-preview')
        self.assertEqual(onTokenIssuanceStartRequest.payload.customExtensionId,"10000000-0000-0000-0000-000000000001")
        self.assertEqual(onTokenIssuanceStartRequest.payload.eventListenerId,"10000000-0000-0000-0000-000000000001")
        self.assertEqual(onTokenIssuanceStartRequest.payload.type,"onTokenIssuanceStartCustomExtension")

    def test_object_creation_payload_context(self):
        
        json_data=json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest=preview_10_01_2021.TokenIssuanceStartRequest.create_instance(result=json_data)

        self.assertEqual(onTokenIssuanceStartRequest.payload.context.correlationId,"20000000-0000-0000-0000-000000000002")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.client.ip,"127.0.0.1")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.authProtocol.tenantId,"30000000-0000-0000-0000-000000000003")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.authProtocol.type,"OAUTH2.0")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.clientServicePrincipal.id,"40000000-0000-0000-0000-000000000001")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.clientServicePrincipal.appDisplayName,"Test client app")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.clientServicePrincipal.displayName,"Test client application")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.clientServicePrincipal.appId,"40000000-0000-0000-0000-000000000002")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.clientServicePrincipal.servicePrincipalNames,["40000000-0000-0000-0000-000000000002","http://example.com/client/app1"])
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.resourceServicePrincipal.id,"40000000-0000-0000-0000-000000000003")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.resourceServicePrincipal.appId,"40000000-0000-0000-0000-000000000004")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.resourceServicePrincipal.appDisplayName,"Test resourceapp")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.resourceServicePrincipal.displayName,"Test resourceapplication")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.resourceServicePrincipal.servicePrincipalNames,["40000000-0000-0000-0000-000000000004","https://example.com/resource2"])

    def test_object_creation_payload_context_user(self):
        
        json_data=json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest=preview_10_01_2021.TokenIssuanceStartRequest.create_instance(result=json_data)
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.id,"60000000-0000-0000-0000-000000000006")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.ageGroup,"Adult")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.country,"USA")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.companyName,"Evo Sts Test")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.department,"Dummy department")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.creationType,"Invitation")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.department,"Dummy department")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.displayName,"Dummy display name")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.givenName,"Example")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.mail,"test@example.com")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.onPremisesSamAccountName,"testadmin")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.onPremisesSecurityIdentifier,"DummySID")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.onPremiseUserPrincipalName,"Dummy Name")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.preferredDataLocation,"DummyDataLocation")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.preferredLanguage,"DummyLanguage")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.surname,"Test")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.userPrincipalName,"testadmin@example.com")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.userType,"UserTypeCloudManaged")

    def test_response_serialiation(self):
        
        json_data=json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest=preview_10_01_2021.TokenIssuanceStartRequest.create_instance(result=json_data)
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.id,"60000000-0000-0000-0000-000000000006")

        #get the json string from response
        result=onTokenIssuanceStartRequest.response.to_json()
        #convert the expected json string to json dict
        expected_result_dict=json.loads(AuthenticationEventsResources.response_data)
        #set actions in the json dict to empty list
        expected_result_dict['actions']=[]
        #get json string from the json dict
        expected_result_str=json.dumps(expected_result_dict)
        #validate json string from the to_json function to expected json string
        self.assertEqual(result,expected_result_str)

    def test_decode_function(self):
        datum = Datum(value=AuthenticationEventsResources.request_data,type='string')
        out=AuthenticationEventTriggerConverter.decode(datum, trigger_metadata=None)
        self.assertTrue(isinstance(out,preview_10_01_2021.TokenIssuanceStartRequest))

    def test_decode_event_type(self):
        data_dict=json.loads(AuthenticationEventsResources.request_data)
        data_dict['payload']['type']='Negative test string'
        datum = Datum(value=json.dumps(data_dict),type='string')
        with self.assertRaisesRegex(Exception,"Event type not supported") as context:
            AuthenticationEventTriggerConverter.decode(datum, trigger_metadata=None)

    def test_decode_api_schema_version(self):
        data_dict=json.loads(AuthenticationEventsResources.request_data)
        data_dict['payload']['apiSchemaVersion']='Negative test string'
        datum = Datum(value=json.dumps(data_dict),type='string')
        with self.assertRaisesRegex(Exception,"Version not supported") as context:
            AuthenticationEventTriggerConverter.decode(datum, trigger_metadata=None)

    def test_decode_api_schema_version(self):
        data_dict=json.loads(AuthenticationEventsResources.request_data)
        data_dict['payload']['apiSchemaVersion']='Negative test string'
        datum = Datum(value=json.dumps(data_dict),type='object')
        with self.assertRaisesRegex(Exception,"unsupported authentication event trigger payload type:") as context:
            AuthenticationEventTriggerConverter.decode(datum, trigger_metadata=None)

    def test_encode_object_type(self):
        json_data=json.loads(AuthenticationEventsResources.request_data)
        onTokenIssuanceStartRequest=preview_10_01_2021.TokenIssuanceStartRequest.create_instance(result=json_data)
        with self.assertRaisesRegex(Exception,"Object should be of valid response type") as context:
            AuthenticationEventTriggerConverter.encode(obj=onTokenIssuanceStartRequest,expected_type='object')

    def test_encode_object_typ(self):
        response=_abc._IAuthenticationEventResponse(schema="test",body='{"test":"Not serializable"}')
        with self.assertRaisesRegex(Exception,"Object was not of expected type Serializable") as context:
            AuthenticationEventTriggerConverter.encode(obj=response,expected_type='object')

    
        



        



        

