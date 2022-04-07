
import unittest
import json
import azure.functions.authentication_events.token_issuance_start.preview_10_01_2021 as preview_10_01_2021 

class TestDurableFunctions(unittest.TestCase):
    
    def test_object_creation(self):
        
        data='{"response":{"actions":[],"schema":"{\\r\\n  \\"$schema\\": \\"http://json-schema.org/draft-04/schema\\",\\r\\n  \\"type\\": \\"object\\",\\r\\n  \\"properties\\": {\\r\\n    \\"type\\": {\\r\\n      \\"type\\": \\"string\\",\\r\\n      \\"enum\\": [ \\"onTokenIssuanceStartCustomExtension\\" ]\\r\\n    },\\r\\n    \\"apiSchemaVersion\\": {\\r\\n      \\"type\\": \\"string\\",\\r\\n      \\"enum\\": [ \\"10-01-2021-preview\\" ]\\r\\n    },\\r\\n    \\"actions\\": {\\r\\n      \\"type\\": \\"array\\",\\r\\n      \\"minItems\\": 1,\\r\\n      \\"maxItems\\": 1,\\r\\n      \\"items\\": {\\r\\n        \\"type\\": \\"object\\",\\r\\n        \\"properties\\": {\\r\\n          \\"type\\": {\\r\\n            \\"type\\": \\"string\\",\\r\\n            \\"enum\\": [ \\"ProvideClaimsForToken\\" ]\\r\\n          }\\r\\n        },\\r\\n        \\"allOf\\": [\\r\\n          {\\r\\n            \\"anyOf\\": [\\r\\n              {\\r\\n                \\"not\\": {\\r\\n                  \\"properties\\": { \\"type\\": { \\"enum\\": [\\"ProvideClaimsForToken\\"] } }\\r\\n                }\\r\\n              },\\r\\n              { \\r\\n                \\"properties\\": { \\"claims\\": {\\"$ref\\": \\"#/definitions/claimsForToken\\"} },\\r\\n                \\"required\\": [\\"claims\\"]\\r\\n              }\\r\\n            ]\\r\\n          }\\r\\n        ],\\r\\n        \\"required\\": [\\r\\n          \\"type\\"\\r\\n        ]\\r\\n      }\\r\\n    }\\r\\n  },\\r\\n  \\"required\\": [\\r\\n    \\"type\\",\\r\\n    \\"apiSchemaVersion\\",\\r\\n    \\"actions\\"\\r\\n  ],\\r\\n\\r\\n  \\"definitions\\": {\\r\\n    \\r\\n    \\"claimsForToken\\": {\\r\\n      \\"type\\": \\"array\\",\\r\\n      \\"items\\": {\\r\\n        \\"$ref\\": \\"#/definitions/claim\\"\\r\\n      }\\r\\n    },\\r\\n\\r\\n    \\"claim\\": {\\r\\n      \\"type\\": \\"object\\",\\r\\n      \\"properties\\": {\\r\\n        \\"id\\": {\\r\\n          \\"type\\": \\"string\\"\\r\\n        },\\r\\n        \\"value\\": {\\r\\n          \\"oneOf\\": [\\r\\n            {\\r\\n              \\"type\\": \\"string\\"\\r\\n            },\\r\\n            {\\r\\n              \\"type\\": \\"array\\",\\r\\n              \\"items\\": {\\r\\n                \\"type\\": \\"string\\"\\r\\n              }\\r\\n            }\\r\\n          ]\\r\\n        }\\r\\n      },\\r\\n      \\"required\\": [\\r\\n        \\"id\\",\\r\\n        \\"value\\"\\r\\n      ]\\r\\n    }\\r\\n  }\\r\\n  \\r\\n}","body":"{\\r\\n  \\"type\\": \\"onTokenIssuanceStartCustomExtension\\",\\r\\n  \\"apiSchemaVersion\\": \\"10-01-2021-preview\\",\\r\\n  \\"actions\\": []\\r\\n}"},"payload":{"context":{"correlationId":"20000000-0000-0000-0000-000000000002","client":{"ip":"127.0.0.1"},"authProtocol":{"type":"OAUTH2.0","tenantId":"30000000-0000-0000-0000-000000000003"},"clientServicePrincipal":{"id":"40000000-0000-0000-0000-000000000001","appId":"40000000-0000-0000-0000-000000000002","appDisplayName":"Test client app","displayName":"Test client application","servicePrincipalNames":["40000000-0000-0000-0000-000000000002","http://example.com/client/app1"]},"resourceServicePrincipal":{"id":"40000000-0000-0000-0000-000000000003","appId":"40000000-0000-0000-0000-000000000004","appDisplayName":"Test resourceapp","displayName":"Test resourceapplication","servicePrincipalNames":["40000000-0000-0000-0000-000000000004","https://example.com/resource2"]},"roles":[{"id":"50000000-0000-0000-0000-000000000005","value":"DummyRole"}],"user":{"ageGroup":"Adult","companyName":"Evo Sts Test","country":"USA","createdDateTime":"0001-01-01T00:00:00+00:00","creationType":"Invitation","department":"Dummy department","displayName":"Dummy display name","givenName":"Example","id":"60000000-0000-0000-0000-000000000006","lastPasswordChangeDateTime":"0001-01-01T00:00:00+00:00","mail":"test@example.com","onPremisesSamAccountName":"testadmin","onPremisesSecurityIdentifier":"DummySID","onPremiseUserPrincipalName":"Dummy Name","preferredDataLocation":"DummyDataLocation","preferredLanguage":"DummyLanguage","surname":"Test","userPrincipalName":"testadmin@example.com","userType":"UserTypeCloudManaged"}},"eventListenerId":"10000000-0000-0000-0000-000000000001","time":"2021-05-17T00:00:00+00:00","type":"onTokenIssuanceStartCustomExtension","apiSchemaVersion":"10-01-2021-preview","customExtensionId":"10000000-0000-0000-0000-000000000001"},"tokenClaims":null,"requestStatus":"Successful","statusMessage":"Ready"}'
        json_data=json.loads(data)
        onTokenIssuanceStartRequest=preview_10_01_2021.TokenIssuanceStartRequest.create_instance(result=json_data)
        
        self.assertEqual(onTokenIssuanceStartRequest.payload.apiSchemaVersion,'10-01-2021-preview')
        self.assertEqual(onTokenIssuanceStartRequest.payload.customExtensionId,"10000000-0000-0000-0000-000000000001")
        self.assertEqual(onTokenIssuanceStartRequest.payload.eventListenerId,"10000000-0000-0000-0000-000000000001")
        self.assertEqual(onTokenIssuanceStartRequest.payload.type,"onTokenIssuanceStartCustomExtension")

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
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.id,"60000000-0000-0000-0000-000000000006")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.ageGroup,"Adult")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.country,"USA")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.companyName,"Evo Sts Test")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.department,"Dummy department")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.creationType,"Invitation")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.department,"Dummy department")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.displayName,"Dummy display name")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.createdDateTime,"0001-01-01T00:00:00Z")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.givenName,"Example")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.lastPasswordChangeDateTime,"0001-01-01T00:00:00Z")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.mail,"test@example.com")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.onPremisesSamAccountName,"testadmin")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.onPremisesSecurityIdentifier,"DummySID")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.onPremiseUserPrincipalName,"Dummy Name")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.preferredDataLocation,"DummyDataLocation")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.preferredLanguage,"DummyLanguage")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.surname,"Test")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.userPrincipalName,"testadmin@example.com")
        self.assertEqual(onTokenIssuanceStartRequest.payload.context.user.userType,"UserTypeCloudManaged")

        result=onTokenIssuanceStartRequest.response.to_json()

        # self.assertEqual(result, )

