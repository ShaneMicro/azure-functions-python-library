from typing import List


class AuthProtocol:
    def __init__(self, type: str, tenantId: str):
        self.type = type
        self.tenantId = tenantId

    @staticmethod
    def populate(authProtocol: dict = None):
        if authProtocol is not None:
            return AuthProtocol(**authProtocol)


class Client:
    def __init__(self, ip: str):
        self.ip = ip

    @staticmethod
    def populate(client: dict = None):
        if client is not None:
            return Client(**client)


class Role:
    def __init__(self, id: str, value: str):
        self.id = id
        self.value = value


class ServicePrincipalName:
    def __init__(self, url: str, uuid: str):
        self.url = url
        self.uuid = uuid


listOfServicePrincipalName = List[ServicePrincipalName]


class ServicePrincipal:
    def __init__(
        self,
        id: str,
        appId: str,
        appDisplayName: str,
        displayName: str,
        servicePrincipalNames: List[str],
    ):
        self.id = id
        self.appId = appId
        self.appDisplayName = appDisplayName
        self.displayName = displayName
        self.servicePrincipalNames = servicePrincipalNames

    @staticmethod
    def populate(servicePrincipal: dict = None):
        if servicePrincipal is not None:
            return ServicePrincipal(**servicePrincipal)


class User:
    def __init__(
        self,
        ageGroup: str,
        companyName: str,
        country: str,
        createdDateTime: str,
        creationType: str,
        department: str,
        displayName: str,
        givenName: str,
        lastPasswordChangeDateTime: str,
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
        self.id = id
        self.userType = userType
        self.userPrincipalName = userPrincipalName
        self.surname = surname
        self.preferredLanguage = preferredLanguage
        self.ageGroup = ageGroup
        self.companyName = companyName
        self.country = country
        self.createdDateTime = createdDateTime
        self.creationType = creationType
        self.department = department
        self.displayName = displayName
        self.givenName = givenName
        self.lastPasswordChangeDateTime = lastPasswordChangeDateTime
        self.mail = mail
        self.onPremisesSamAccountName = onPremisesSamAccountName
        self.onPremisesSecurityIdentifier = onPremisesSecurityIdentifier
        self.onPremiseUserPrincipalName = onPremiseUserPrincipalName
        self.preferredDataLocation = preferredDataLocation

    @staticmethod
    def populate(user: dict = None):
        if user is not None:
            return User(**user)


Roles = List[Role]


class Context:
    def __init__(
        self,
        client: Client,
        authProtocol: AuthProtocol,
        clientServicePrincipal: ServicePrincipal,
        resourceServicePrincipal: ServicePrincipal,
        user: User,
        correlationId: str = None,
        roles: Roles = None,
    ):
        self.user = user
        self.resourceServicePrincipal = resourceServicePrincipal
        self.clientServicePrincipal = clientServicePrincipal
        self.authProtocol = authProtocol
        self.client = client
        if correlationId is not None:
            self.correlationId = correlationId
        if roles is not None:
            self.roles = roles

    @staticmethod
    def populate(context: dict = None):
        if context is not None:
            return Context(
                correlationId=context.get("correlationId"),
                user=User.populate(context.get("user")),
                client=Client.populate(context.get("client")),
                clientServicePrincipal=ServicePrincipal.populate(
                    context.get("clientServicePrincipal")
                ),
                resourceServicePrincipal=ServicePrincipal.populate(
                    context.get("resourceServicePrincipal")
                ),
                roles=context.get("roles"),
                authProtocol=AuthProtocol.populate(context.get("authProtocol")),  # noqa: E501
            )
