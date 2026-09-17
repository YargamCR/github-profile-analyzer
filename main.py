import github_api
import utilities

utilities.clear_terminal()


def menu(opt, user):
    match opt:

        case 1:
            cont = 1
            repos = github_api.get_user_repositories(user)
            utilities.clear_terminal()
            print(
                f"========================================\nVIEW REPOSITORIES({user})\n========================================")
            for i, repository in enumerate(repos):
                print(f"{i+1}.{repository['name']}")
                cont = cont + 1
            print("\n\n========================================\n\n")

            input("Press enter to continue...")
            utilities.clear_terminal()
            user_search(user)
        case 2:
            print("")
        case 3:
            print("")
        case 4:
            print("")
        case 5:
            print("")


def user_search(user):
    profile = github_api.get_user_profile(user)
    # USER NOT FOUND ERROR 404
    if profile == 404:
        return False
    # USER FOUND
    else:
        name = profile["name"]
        if name is None:
            name = "Not provided"
        print(f"Username: {profile['login']}")
        print(f"Name: {name}")
        print(f"Public repositories: {profile['public_repos']}")
        print(f"Followers: {profile['followers']}")
        print(f"Following: {profile['following']}")
        print(f"Profile: {profile['html_url']}")
        print("\n\n========================================\n\n")


while True:
    print("========================================\nGITHUB PROFILE ANALYZER\n========================================")
    username = input("Enter GitHub username:")
    if user_search(username) is False:
        break
    else:
        while True:
            print("1. View repositories\n2. Sort repositories by stars\n3. View language statistics\n4. Save report\n5. Search another user\n6. Exit")
            option = int(input("-----> "))
            print("\n\n========================================\n\n")
            if option > 1 and option < 5:
                print("Wrong option, please try again...")
            elif option == 6:
                break
            else:
                menu(option, username)
    if option == 6:
        print("Closing App...")
        break
