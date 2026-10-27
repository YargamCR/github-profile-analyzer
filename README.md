# GitHub Profile Analyzer 🐙

A Python application that retrieves public GitHub profile information and analyzes repositories to provide useful insights about a developer's activity and projects.

## 🚀 Features

- **Profile Information:** Retrieve a user's username, name, followers, following, public repository count, and profile URL.
- **Total Stars:** Calculate the total stars across all public repositories.
- **Most-Starred Repository:** Identify the repository with the highest number of stars.
- **Language Statistics:** Count repositories by programming language.
- **Repository Ranking:** Display the top 5 repositories sorted by star count.
- **API Integration:** Fetch profile and repository data using the GitHub REST API.
- **Error Handling:** Handle invalid usernames, network errors, and empty repository lists.
- **Pagination:** Retrieve repositories across multiple API pages.

## 🛠️ Technologies Used

- Python
- Requests
- Git and GitHub
- GitHub REST API

## 📁 Project Structure

```text
github-profile-analyzer/
├── main.py
├── github_api.py
├── analyzer.py
├── utilities.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Responsibilities

| File | Description |
|---|---|
| `main.py` | Main application and results display. |
| `github_api.py` | Retrieves profile and repository data from GitHub. |
| `analyzer.py` | Calculates statistics and sorts repositories. |
| `utilities.py` | Provides reusable terminal helper functions. |
| `requirements.txt` | Lists project dependencies. |

## ⚙️ Requirements

- Python 3
- Internet connection
- Git (optional, for cloning the repository)
- A GitHub username to analyze

## 📦 Installation

### 1. Clone the repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/github-profile-analyzer.git
cd github-profile-analyzer
```

### 2. Create a virtual environment

**Linux / macOS (including Omarchy):**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

Enter a GitHub username when prompted.

## 💻 Example Usage

```text
==================================================
             GITHUB PROFILE ANALYZER
==================================================
Enter a GitHub username: YargamCR

Fetching data for YargamCR...
```

The application displays the profile information, total repository stars, most-starred repository, language statistics, and top 5 repositories.

*Note: Actual results
