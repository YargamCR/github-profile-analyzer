from analyzer import (
    get_language_stats,
    get_most_starred_repo,
    get_total_stars,
    sort_repositories_by_stars,
)
from github_api import get_user_profile, get_user_repositories
from utilities import clear_terminal, pause, print_header


def display_profile(profile):
    print_header("GITHUB PROFILE")

    print(f"Username: {profile.get('login', 'N/A')}")
    print(f"Name: {profile.get('name') or 'Not provided'}")
    print(f"Followers: {profile.get('followers', 0)}")
    print(f"Following: {profile.get('following', 0)}")
    print(f"Public repositories: {profile.get('public_repos', 0)}")
    print(f"Profile URL: {profile.get('html_url', 'N/A')}")


def display_analysis(repositories):
    print_header("REPOSITORY ANALYSIS")

    print(f"Repositories analyzed: {len(repositories)}")
    print(f"Total stars: {get_total_stars(repositories)}")

    most_starred = get_most_starred_repo(repositories)

    if most_starred is not None:
        print(f"\nMost-starred repository: {most_starred.get('name', 'Unknown')}")
        print(f"Stars: {most_starred.get('stargazers_count', 0)}")
        print(f"URL: {most_starred.get('html_url', 'N/A')}")
    else:
        print("\nThis user has no public repositories.")

    languages = get_language_stats(repositories)

    if languages:
        print("\nLanguages by repository count:")

        sorted_languages = sorted(
            languages.items(), key=lambda item: item[1], reverse=True
        )

        for language, count in sorted_languages:
            print(f"  {language}: {count}")

        most_used_language = max(languages, key=languages.get)

        print(
            f"\nMost-used language: {most_used_language} "
            f"({languages[most_used_language]} repositories)"
        )
    else:
        print("\nNo programming language data available.")

    print("\nTop 5 repositories by stars:")

    top_repositories = sort_repositories_by_stars(repositories)[:5]

    if top_repositories:
        for rank, repo in enumerate(top_repositories, start=1):
            print(
                f"{rank}. {repo.get('name', 'Unknown')} - "
                f"{repo.get('stargazers_count', 0)} stars"
            )
    else:
        print("No repositories to display.")


def main():
    clear_terminal()
    print_header("GITHUB PROFILE ANALYZER")

    username = input("Enter a GitHub username: ").strip()

    if not username:
        print("\nUsername cannot be empty.")
        return

    print(f"\nFetching data for {username}...")

    profile = get_user_profile(username)

    if profile is None:
        print(
            "\nCould not retrieve the profile. "
            "Check the username, your internet connection, "
            "and any error displayed above."
        )
        return

    repositories = get_user_repositories(username)

    if repositories is None:
        print("\nCould not retrieve the repositories. Please try again later.")
        return

    print()
    display_profile(profile)

    print()
    display_analysis(repositories)

    pause()


if __name__ == "__main__":
    main()
