import asyncio
import configparser
import json
from graph import Graph
import requests
import json

async def main():
    print('Python Graph Connector\n')

    # Load settings
    config = configparser.ConfigParser()
    config.read(['config.cfg', 'config.dev.cfg'])
    azure_settings = config['azure']

    graph: Graph = Graph(azure_settings)

    user = await graph.get_user()
    print('Hello,', user.display_name)

    choice = -1

    while choice != 0:
        print('Please choose one of the following options:')
        print('0. Exit')
        print('1. Create External Connection')
        print('2. Create Schema')
        print('3. Load GitHub Repositories')
        try:
            choice = int(input())
        except ValueError:
            choice = -1

        try:
            if choice == 0:
                print('Goodbye...')
            elif choice == 1:
                await graph.create_connection()
            elif choice == 2:
                connectionId = input("Please enter the connection id: ")
                await graph.create_schema(connectionId)
            elif choice == 3:
                connectionId = input("Please enter the connection id: ")
                username = input("Please enter your GitHub username: ")
                repos = github_repos(username)
                await graph.create_items(connectionId, repos)
            else:
                print('Invalid choice!\n')
        except Exception as ex:
            print('Error:', ex, '\n')

def github_repos(username):
        data = {"type": "all", "sort":"full_name", "direction": "asc"}
        output = requests.get("https://api.github.com/users/{}/repos".format(username), data=json.dumps(data))
        output = json.loads(output.text)
        return output
# Run main
asyncio.run(main())