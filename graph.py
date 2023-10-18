from configparser import SectionProxy
from azure.identity import DeviceCodeCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.item.user_item_request_builder import UserItemRequestBuilder
from msgraph.generated.models.external_connectors.external_connection import ExternalConnection
from msgraph.generated.models.external_connectors.schema  import Schema
from msgraph.generated.models.external_connectors.property_  import Property_
from msgraph.generated.models.external_connectors.property_type import PropertyType
from msgraph.generated.models.external_connectors.access_type import AccessType
from msgraph.generated.models.external_connectors.acl import Acl
from msgraph.generated.models.external_connectors.acl_type import AclType
from msgraph.generated.models.external_connectors.external_activity import ExternalActivity
from msgraph.generated.models.external_connectors.external_activity_type import ExternalActivityType
from msgraph.generated.models.external_connectors.external_item import ExternalItem
from msgraph.generated.models.external_connectors.external_item_content import ExternalItemContent
from msgraph.generated.models.external_connectors.external_item_content_type import ExternalItemContentType
from msgraph.generated.models.external_connectors.properties  import Properties

class Graph:
    settings: SectionProxy
    device_code_credential: DeviceCodeCredential
    user_client: GraphServiceClient

    def __init__(self, config: SectionProxy):
        self.settings = config
        client_id = self.settings['clientId']
        tenant_id = self.settings['tenantId']
        graph_scopes = self.settings['graphUserScopes'].split(' ')

        self.device_code_credential = DeviceCodeCredential(client_id, tenant_id = tenant_id)
        self.user_client = GraphServiceClient(self.device_code_credential, graph_scopes)

    async def get_user(self):
        # Only request specific properties using $select
        query_params = UserItemRequestBuilder.UserItemRequestBuilderGetQueryParameters(
            select=['displayName', 'mail', 'userPrincipalName']
        )

        request_config = UserItemRequestBuilder.UserItemRequestBuilderGetRequestConfiguration(
            query_parameters=query_params
        )

        user = await self.user_client.me.get(request_configuration=request_config)
        return user
    
    async def create_connection(self):
        # create prompt for user to enter connection details
        connectionId = input("Enter Connection Id: ")
        connectionName = input("Enter Connection Name: ")
        connectionDescription = input("Enter Connection Description: ")

        new_connection = ExternalConnection(
            id=connectionId,
            name=connectionName,
            description=connectionDescription,
        )

        print("Creating connection...")
        connection = await self.user_client.external.connections.post(body=new_connection)
        print ("Connection created successfully! Connection name:", connection.name)

    async def create_schema(self, connectionId: str):
        schema = Schema(
            base_type = "microsoft.graph.externalItem",
            properties = [ 
                Property_(
                    name= "name",
                    type=PropertyType.String,
                    is_searchable= True,
                    is_retrievable= True,
                ),
                Property_(
                    name= "description",
                    type=PropertyType.String,
                    is_retrievable= True,
                ),
                Property_(
                    name= "htmlurl",
                    type=PropertyType.String,
                    is_searchable= True,
                    is_retrievable= True,
                ),
            ]
        )  
        print("Creating schema...")      
        await self.user_client.external.connections.by_external_connection_id(connectionId).schema.patch(schema)
        print ("Schema created successfully!")

    async def create_items(self, connectionId: str, repos: str):
        print("Creating items...", repos)
        for repo in repos:
            print ("Creating item for repo: ", repo["name"])
            request_body = ExternalItem(
                id = repo["name"],
                acl=[
                    Acl(
                        type=AclType.Everyone,
                        value=repo["name"],
                        access_type=AccessType.Grant
                    )
                ],
                properties=Properties(
                    additional_data={
                        "name": repo["name"],
                        "description": repo["description"],
                        "htmlurl": repo["html_url"]
                    }
                )
            )
            
            await self.user_client.external.connections.by_external_connection_id(connectionId).items.by_external_item_id(request_body.id).put(request_body)
            print ("Item created successfully!")
            