def get_total_stars(repositories):
    total = 0

    for repo in repositories:
        total += repo.get("stargazers_count", 0)

    return total


def get_most_starred_repo(repositories):
    if not repositories:
        return None

    most_starred = repositories[0]

    for repo in repositories:
        if repo.get("stargazers_count", 0) > most_starred.get("stargazers_count", 0):
            most_starred = repo

    return most_starred


def get_language_stats(repositories):
    languages = {}

    for repo in repositories:
        language = repo.get("language")

        if language is not None:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1

    return languages


def sort_repositories_by_stars(repositories):
    return sorted(
        repositories, key=lambda repo: repo.get("stargazers_count", 0), reverse=True
    )
