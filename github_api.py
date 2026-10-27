import requests

BASE_URL = "https://api.github.com"


def get_user_profile(username):
    url = f"{BASE_URL}/users/{username}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            return None

        response.raise_for_status()
        return response.json()

    except requests.RequestException as error:
        print(f"\nGitHub API error while fetching profile: {error}")
        return None


def get_user_repositories(username):
    url = f"{BASE_URL}/users/{username}/repos"

    repositories = []
    page = 1

    while True:
        params = {"per_page": 100, "page": page}

        try:
            response = requests.get(url, params=params, timeout=10)

            response.raise_for_status()
            page_repositories = response.json()

        except requests.RequestException as error:
            print(f"\nGitHub API error while fetching repositories: {error}")
            return None

        if not page_repositories:
            break

        repositories.extend(page_repositories)

        if len(page_repositories) < 100:
            break

        page += 1

    return repositories
