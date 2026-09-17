import requests


def get_user_profile(username):
    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url, timeout=5)
    except requests.RequestException:
        print("There was a problem connecting to the API.")
    if response.status_code == 404:
        print("User not found!")
        return 404
    elif response.status_code == 200:
        return response.json()


def get_user_repositories(username):

    try:
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url, timeout=5)
        return response.json()
    except requests.RequestException:
        print("There was a problem connecting to the API.")
        return
