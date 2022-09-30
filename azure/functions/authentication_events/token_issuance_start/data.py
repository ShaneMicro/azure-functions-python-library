from typing import List


# # Protocol class for data
# class AuthProtocol:
#     def __init__(self, type: str, tenantId: str):
#         # The type
#         self.type = type
#         # The tenant identifier.
#         self.tenantId = tenantId

#     # static method to create instance of the object from dict

#     @staticmethod
#     def populate(authProtocol: dict = None):
#         if authProtocol is not None:
#             return AuthProtocol(**authProtocol)


# Client class for data.
class Client:
    def __init__(self, ip: str, locale: str, market: str):
        # The Ip Address
        self.ip = ip
        self.locale = locale
        self.market = market

    # static method to create instance of the object from dict

    @staticmethod
    def populate(client: dict = None):
        if client is not None:
            return Client(**client)


class ServicePrincipalName:
    def __init__(self, url: str, uuid: str):
        self.url = url
        self.uuid = uuid


listOfServicePrincipalName = List[ServicePrincipalName]


# ResourceServicePrincipal class for data.
class ServicePrincipal:
    def __init__(
        self,
        id: str,
        appId: str,
        appDisplayName: str,
        displayName: str,
    ):
        # The identifier for the service principal.
        self.id = id
        # The application display name.
        self.appId = appId
        # The application display name.
        self.appDisplayName = appDisplayName
        # The display name.
        self.displayName = displayName
        

    # static method to create instance of the object from dict

    @staticmethod
    def populate(servicePrincipal: dict = None):
        if servicePrincipal is not None:
            return ServicePrincipal(**servicePrincipal)


# User class for data.
class User:
    def __init__(
        self,
        companyName: str,
        country: str,
        displayName: str,
        givenName: str,
        mail: str,
        onPremisesSamAccountName: str,
        onPremisesSecurityIdentifier: str,
        onPremiseUserPrincipalName: str,
        preferredDataLocation: str,
        preferredLanguage: str,
        surname: str,
        userPrincipalName: str,
        userType: str,
        id: str,
    ):
        # User data
        self.id = id
        self.userType = userType
        self.userPrincipalName = userPrincipalName
        self.surname = surname
        self.preferredLanguage = preferredLanguage
        self.companyName = companyName
        self.country = country
        self.displayName = displayName
        self.givenName = givenName
        self.mail = mail
        self.onPremisesSamAccountName = onPremisesSamAccountName
        self.onPremisesSecurityIdentifier = onPremisesSecurityIdentifier
        self.onPremiseUserPrincipalName = onPremiseUserPrincipalName
        self.preferredDataLocation = preferredDataLocation

    # static method to create instance of the object from dict
    @staticmethod
    def populate(user: dict = None):
        if user is not None:
            return User(**user)


# Context class for data.
class AuthenticationContext:
    def __init__(
        self,
        client: Client,
        authProtocol: str,
        clientServicePrincipal: ServicePrincipal,
        resourceServicePrincipal: ServicePrincipal,
        user: User,
        correlationId: str = None,
    ):
        # Data pertaining to the user requesting a token.
        self.user = user
        # The resource service principal.
        self.resourceServicePrincipal = resourceServicePrincipal
        # The client service principal.
        self.clientServicePrincipal = clientServicePrincipal
        # The authorization protocol.
        self.authProtocol = authProtocol
        # The client.
        self.client = client
        # Unique identifier for the request.
        if correlationId is not None:
            self.correlationId = correlationId

    # static method to create instance of the object from dict
    @staticmethod
    def populate(context: dict = None):
        if context is not None:
            return AuthenticationContext(
                correlationId=context.get("correlationId"),
                user=User.populate(context.get("user")),
                client=Client.populate(context.get("client")),
                clientServicePrincipal=ServicePrincipal.populate(
                    context.get("clientServicePrincipal")
                ),
                resourceServicePrincipal=ServicePrincipal.populate(
                    context.get("resourceServicePrincipal")
                ),
                authProtocol=context.get("authProtocol")
            )
