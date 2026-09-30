def get_total_stars(repositories):
    total = 0

    for repos in repositories:
        total += repos["stargazers_count"]

    return total


def get_most_starred_repo(repositories):

    most_starred = 0

    for repos in repositories:
        most_starred = max(most_starred, repos["stargazers_count"])
        if most_starred == 0:
            return None
        else:
            return print(
                f"Most starred repository: {repos['name']}\nStars: {most_starred}"
            )


def get_language_stats(repositories):
    languages = {}
    python_cont = 0
    C_cont = 0
    java_cont = 0
    for repos in repositories:
        if repos["language"] is not None:
            if "Python" in repos["language"]:
                python_cont = python_cont + 1
            elif "C#" in repos["language"]:
                C_cont = C_cont + 1
            elif "JavaScript" in repos["language"]:
                java_cont = java_cont + 1
    languages.update(
        {
            "Python": python_cont,
            "C#": C_cont,
            "JavaScript": java_cont,
        }
    )
    if python_cont < C_cont and python_cont < java_cont:
        return "Python"
    elif C_cont < python_cont and C_cont < java_cont:
        return "C#"
    elif java_cont < python_cont and java_cont < C_cont:
        return "JavaScript"


def sort_repositories_by_stars(repositories):
    sorted_repos = [""]
    sorted_repositories = [
        {"Repository": index, "nombre": repositories}
        for index, repositories in enumerate(sorted_repos, start=1)
    ]

    return sorted_repositories
