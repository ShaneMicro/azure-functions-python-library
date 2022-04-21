request_data = '{"response":{"actions":[],"schema":"{\\r\\n  \\"$schema\\": \\"http://json-schema.org/draft-04/schema\\",\\r\\n  \\"type\\": \\"object\\",\\r\\n  \\"properties\\": {\\r\\n    \\"type\\": {\\r\\n      \\"type\\": \\"string\\",\\r\\n      \\"enum\\": [ \\"onTokenIssuanceStartCustomExtension\\" ]\\r\\n    },\\r\\n    \\"apiSchemaVersion\\": {\\r\\n      \\"type\\": \\"string\\",\\r\\n      \\"enum\\": [ \\"10-01-2021-preview\\" ]\\r\\n    },\\r\\n    \\"actions\\": {\\r\\n      \\"type\\": \\"array\\",\\r\\n      \\"minItems\\": 1,\\r\\n      \\"maxItems\\": 1,\\r\\n      \\"items\\": {\\r\\n        \\"type\\": \\"object\\",\\r\\n        \\"properties\\": {\\r\\n          \\"type\\": {\\r\\n            \\"type\\": \\"string\\",\\r\\n            \\"enum\\": [ \\"ProvideClaimsForToken\\" ]\\r\\n          }\\r\\n        },\\r\\n        \\"allOf\\": [\\r\\n          {\\r\\n            \\"anyOf\\": [\\r\\n              {\\r\\n                \\"not\\": {\\r\\n                  \\"properties\\": { \\"type\\": { \\"enum\\": [\\"ProvideClaimsForToken\\"] } }\\r\\n                }\\r\\n              },\\r\\n              { \\r\\n                \\"properties\\": { \\"claims\\": {\\"$ref\\": \\"#/definitions/claimsForToken\\"} },\\r\\n                \\"required\\": [\\"claims\\"]\\r\\n              }\\r\\n            ]\\r\\n          }\\r\\n        ],\\r\\n        \\"required\\": [\\r\\n          \\"type\\"\\r\\n        ]\\r\\n      }\\r\\n    }\\r\\n  },\\r\\n  \\"required\\": [\\r\\n    \\"type\\",\\r\\n    \\"apiSchemaVersion\\",\\r\\n    \\"actions\\"\\r\\n  ],\\r\\n\\r\\n  \\"definitions\\": {\\r\\n    \\r\\n    \\"claimsForToken\\": {\\r\\n      \\"type\\": \\"array\\",\\r\\n      \\"items\\": {\\r\\n        \\"$ref\\": \\"#/definitions/claim\\"\\r\\n      }\\r\\n    },\\r\\n\\r\\n    \\"claim\\": {\\r\\n      \\"type\\": \\"object\\",\\r\\n      \\"properties\\": {\\r\\n        \\"id\\": {\\r\\n          \\"type\\": \\"string\\"\\r\\n        },\\r\\n        \\"value\\": {\\r\\n          \\"oneOf\\": [\\r\\n            {\\r\\n              \\"type\\": \\"string\\"\\r\\n            },\\r\\n            {\\r\\n              \\"type\\": \\"array\\",\\r\\n              \\"items\\": {\\r\\n                \\"type\\": \\"string\\"\\r\\n              }\\r\\n            }\\r\\n          ]\\r\\n        }\\r\\n      },\\r\\n      \\"required\\": [\\r\\n        \\"id\\",\\r\\n        \\"value\\"\\r\\n      ]\\r\\n    }\\r\\n  }\\r\\n  \\r\\n}","body":"{\\r\\n  \\"type\\": \\"onTokenIssuanceStartCustomExtension\\",\\r\\n  \\"apiSchemaVersion\\": \\"10-01-2021-preview\\",\\r\\n  \\"actions\\": []\\r\\n}"},"payload":{"context":{"correlationId":"20000000-0000-0000-0000-000000000002","client":{"ip":"127.0.0.1"},"authProtocol":{"type":"OAUTH2.0","tenantId":"30000000-0000-0000-0000-000000000003"},"clientServicePrincipal":{"id":"40000000-0000-0000-0000-000000000001","appId":"40000000-0000-0000-0000-000000000002","appDisplayName":"Test client app","displayName":"Test client application","servicePrincipalNames":["40000000-0000-0000-0000-000000000002","http://example.com/client/app1"]},"resourceServicePrincipal":{"id":"40000000-0000-0000-0000-000000000003","appId":"40000000-0000-0000-0000-000000000004","appDisplayName":"Test resourceapp","displayName":"Test resourceapplication","servicePrincipalNames":["40000000-0000-0000-0000-000000000004","https://example.com/resource2"]},"roles":[{"id":"50000000-0000-0000-0000-000000000005","value":"DummyRole"}],"user":{"ageGroup":"Adult","companyName":"Evo Sts Test","country":"USA","createdDateTime":"0001-01-01T00:00:00+00:00","creationType":"Invitation","department":"Dummy department","displayName":"Dummy display name","givenName":"Example","id":"60000000-0000-0000-0000-000000000006","lastPasswordChangeDateTime":"0001-01-01T00:00:00+00:00","mail":"test@example.com","onPremisesSamAccountName":"testadmin","onPremisesSecurityIdentifier":"DummySID","onPremiseUserPrincipalName":"Dummy Name","preferredDataLocation":"DummyDataLocation","preferredLanguage":"DummyLanguage","surname":"Test","userPrincipalName":"testadmin@example.com","userType":"UserTypeCloudManaged"}},"eventListenerId":"10000000-0000-0000-0000-000000000001","time":"2021-05-17T00:00:00+00:00","type":"onTokenIssuanceStartCustomExtension","apiSchemaVersion":"10-01-2021-preview","customExtensionId":"10000000-0000-0000-0000-000000000001"},"tokenClaims":null,"requestStatus":"Successful","statusMessage":"Ready"}'  # noqa: E501
response_data = '{"actions": [{"actionType": "ProvideClaimsForToken", "claims": [{"id": "DateOfBirth", "value": "01/01/2000"}, {"id": "CustomRoles", "value": ["Writer", "Editor"]}]}], "schema": "{\\r\\n  \\"$schema\\": \\"http://json-schema.org/draft-04/schema\\",\\r\\n  \\"type\\": \\"object\\",\\r\\n  \\"properties\\": {\\r\\n    \\"type\\": {\\r\\n      \\"type\\": \\"string\\",\\r\\n      \\"enum\\": [ \\"onTokenIssuanceStartCustomExtension\\" ]\\r\\n    },\\r\\n    \\"apiSchemaVersion\\": {\\r\\n      \\"type\\": \\"string\\",\\r\\n      \\"enum\\": [ \\"10-01-2021-preview\\" ]\\r\\n    },\\r\\n    \\"actions\\": {\\r\\n      \\"type\\": \\"array\\",\\r\\n      \\"minItems\\": 1,\\r\\n      \\"maxItems\\": 1,\\r\\n      \\"items\\": {\\r\\n        \\"type\\": \\"object\\",\\r\\n        \\"properties\\": {\\r\\n          \\"type\\": {\\r\\n            \\"type\\": \\"string\\",\\r\\n            \\"enum\\": [ \\"ProvideClaimsForToken\\" ]\\r\\n          }\\r\\n        },\\r\\n        \\"allOf\\": [\\r\\n          {\\r\\n            \\"anyOf\\": [\\r\\n              {\\r\\n                \\"not\\": {\\r\\n                  \\"properties\\": { \\"type\\": { \\"enum\\": [\\"ProvideClaimsForToken\\"] } }\\r\\n                }\\r\\n              },\\r\\n              { \\r\\n                \\"properties\\": { \\"claims\\": {\\"$ref\\": \\"#/definitions/claimsForToken\\"} },\\r\\n                \\"required\\": [\\"claims\\"]\\r\\n              }\\r\\n            ]\\r\\n          }\\r\\n        ],\\r\\n        \\"required\\": [\\r\\n          \\"type\\"\\r\\n        ]\\r\\n      }\\r\\n    }\\r\\n  },\\r\\n  \\"required\\": [\\r\\n    \\"type\\",\\r\\n    \\"apiSchemaVersion\\",\\r\\n    \\"actions\\"\\r\\n  ],\\r\\n\\r\\n  \\"definitions\\": {\\r\\n    \\r\\n    \\"claimsForToken\\": {\\r\\n      \\"type\\": \\"array\\",\\r\\n      \\"items\\": {\\r\\n        \\"$ref\\": \\"#/definitions/claim\\"\\r\\n      }\\r\\n    },\\r\\n\\r\\n    \\"claim\\": {\\r\\n      \\"type\\": \\"object\\",\\r\\n      \\"properties\\": {\\r\\n        \\"id\\": {\\r\\n          \\"type\\": \\"string\\"\\r\\n        },\\r\\n        \\"value\\": {\\r\\n          \\"oneOf\\": [\\r\\n            {\\r\\n              \\"type\\": \\"string\\"\\r\\n            },\\r\\n            {\\r\\n              \\"type\\": \\"array\\",\\r\\n              \\"items\\": {\\r\\n                \\"type\\": \\"string\\"\\r\\n              }\\r\\n            }\\r\\n          ]\\r\\n        }\\r\\n      },\\r\\n      \\"required\\": [\\r\\n        \\"id\\",\\r\\n        \\"value\\"\\r\\n      ]\\r\\n    }\\r\\n  }\\r\\n  \\r\\n}", "body": "{\\r\\n  \\"type\\": \\"onTokenIssuanceStartCustomExtension\\",\\r\\n  \\"apiSchemaVersion\\": \\"10-01-2021-preview\\",\\r\\n  \\"actions\\": []\\r\\n}"}'  # noqa: E501
