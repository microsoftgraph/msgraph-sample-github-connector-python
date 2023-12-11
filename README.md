---
page_type: sample
description: This sample demonstrates how to use the Microsoft Graph connector API to create a custom connector that indexes issues and repositories from GitHub.
products:
- ms-graph
- github
- copilot-m365
languages:
- python
---

# Microsoft Graph Python GitHub connector sample

![License.](https://img.shields.io/badge/license-MIT-green.svg)

Microsoft Graph connectors let you add your own data to the semantic search index and have it power various Microsoft 365 experiences. This TypeScript application shows you how to use the [Microsoft Graph connector](https://learn.microsoft.com/graph/connecting-external-content-connectors-overview) API to create a custom connector that indexes issues and repositories from GitHub. This connector sample powers experiences such as Microsoft Search, Copilot in Teams, the Microsoft 365 App, and more.

## Experiences

The Microsoft Graph connector experiences that will be enabled in the sample include:

- [Microsoft Search](https://learn.microsoft.com/graph/connecting-external-content-experiences#microsoft-search)
- [Context IQ in Outlook on the web](https://learn.microsoft.com/graph/connecting-external-content-experiences#context-iq-in-outlook-on-the-web-preview)
- [Microsoft 365 Copilot](https://learn.microsoft.com/graph/connecting-external-content-experiences#microsoft-365-copilot-limited-preview)
- [Microsoft 365 app: Quick Access & My Content](https://learn.microsoft.com/graph/connecting-external-content-experiences#microsoft-365-app)
- Type Down Suggestions (Query formulation)
- Simplified admin experience in the Teams admin center (Microsoft 356 App)

## Prerequisites
- Install [Python](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/)
- A Microsoft work or school account with the Global administrator role. If you don't have a Microsoft account, you can [sign up for the Microsoft 365 Developer Program](https://developer.microsoft.com/microsoft-365/dev-program) to get a free Microsoft 365 subscription
- A [GitHub account](https://github.com)
- Enable the [simplified admin experience in the Teams admin center](https://learn.microsoft.com/graph/connecting-external-content-deploy-teams)

## Register an app in Azure portal

1. Go to the [Azure Active Directory admin center](https://aad.portal.azure.com/) and sign in with an administrator account.
1. In the left pane, select **Azure Active Directory**, and under **Manage**, select **App registrations**.
1. Select **New registration**.
1. Complete the Register an application form with the following values, and then select **Register**.
    - **Name**: `GitHub Connector`
    - **Supported account types**: **Accounts in this organizational directory only**
    - **Redirect URI**: Leave blank

1. On the GitHub Connector **overview page**, copy the values of **Application (client) ID** and **Directory (tenant) ID**. You will need both in the following section.

## Run the application

1. Install Azure Identity and Microsoft Graph SDK:
    ```bash
    python3 -m pip install azure-identity
    python3 -m pip install msgraph-sdk
    ```
1. Select **config.sfg** from the project root, replace `<your-client-id>` with your **Application (client) ID** and replace `<your-tenant-id>` with your **Directory (tenant) ID**.
1. Run the app:
    ```bash
    python3 main.py
    ```

3. **Create a connection:** Select *1. Create External Connection* from the menu, this step will require you to enter `connection id`,`connection name` and `connection description` to create the connector.
4. **Create a schema:** Select *2. Create Schema* from the menu, this step will require you to enter the `connection id` of the connector you created earlier and create a schema for your connector.
5. **Load data:** Select *3. Load GitHub Repositories* from the menu, this step will require you to enter `connection id` of your connector and `GitHub account name` to load public GitHub repositories of the account in the connector.

## Enable the connector in the Admin Center

1. Open the [Microsoft admin center](https://admin.microsoft.com) in your browser.
1. Select **Settings**, **Search and intelligence**, then **Data sources**. 
1. Search for your GitHub Connector name, then select **Create Result type** under the Required actions:
    1. Enter a name for the result type
    1. Select content source as your connector
    1. (Optional) Set rules for the result type
    1. Launch Layout Designer and select **Result with url and description**, then select **Get started**
    1. Enter **name** for the title property, **htmlurl** for the titleLink property and **description** for the description property, then select **Create layout**.
    1. Paste the JSON script that you created with Layout Designer and select **Next**.
    1. Select **Add result type**.
1. Select **Include Connector Results** under the Requred actions.
1. Search for your repository name in Microsoft SharePoint, Microsoft Office, or Microsoft Search in Bing, you should be able to see your GitHub repository result card with name, url and description.

## Code of conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
