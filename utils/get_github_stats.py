import requests


def get_github_stats(username):
    try:
        # Fetch the data using the CORS proxy
        url = f'https://github-contributions-api.jogruber.de/v4/{username}'
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(f'Failed to fetch data: {response.status_code}')

        # Parse the JSON data
        data = response.json()

        return data
    except Exception as e:
        print('Error:', e)
