import sys
import requests
from datetime import datetime
from prettytable import PrettyTable #type: ignore

# ANSI escape sequences for coloring
CLOSED_COLOR = "\033[92m"  # Green
OPEN_COLOR = "\033[94m"     # Blue
NOT_MERGED_COLOR = "\033[91m"  # Red
RESET_COLOR = "\033[0m"     # Reset to default

# Check if the user provided the repository name and owner
if len(sys.argv) != 2:
    print("Usage: python3 git1.py <owner/repo>")
    print("Example: python3 git1.py octocat/Hello-World")
    sys.exit(1)

# Repository
repo = sys.argv[1]

# GitHub API URL to fetch pull requests
api_url = f"https://api.github.com/repos/{repo}/pulls?state=all"

# Fetch pull requests using requests
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 404:
    print(f"Repository '{repo}' not found or does not exist.")
    sys.exit(1)
elif response.status_code != 200:
    print(f"Failed to fetch pull requests from {repo}. HTTP Status Code: {response.status_code}")
    sys.exit(1)

# Parse the JSON response
pull_requests = response.json()

# Check if there are no pull requests
if not pull_requests:
    print(f"No pull requests found for repository: {repo}")
else:
    # Create a table using PrettyTable to display the results
    table = PrettyTable()
    table.field_names = ["PR Number", "Title", "Author", "State", "Created At", "Merged At"]

    # Function to format the date to 'YYYY-MM-DD'
    def format_date(date_str):
        if date_str:
            return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
        return "Not Available"

    # Display PR number, title, author, state, created_at, and merged_at
    print(f"Fetching pull requests for repository: {repo}")
    print("-----------------------------------")

    for pr in pull_requests:
        pr_number = pr.get('number')
        title = pr.get('title')
        author = pr.get('user', {}).get('login')
        state = pr.get('state')  # Can be 'open' or 'closed'
        created_at = format_date(pr.get('created_at'))  # Format created_at date
        merged_at = format_date(pr.get('merged_at')) if pr.get('merged_at') else "Not Merged"

        # Highlight state with color
        if state == 'closed':
            state_display = f"{CLOSED_COLOR}{state}{RESET_COLOR}"
        elif state == 'open':
            state_display = f"{OPEN_COLOR}{state}{RESET_COLOR}"
        elif merged_at == 'Not Merged':
            state_display = f"{NOT_MERGED_COLOR}{merged_at}{RESET_COLOR}"

        # Add the row to the table
        table.add_row([pr_number, title, author, state_display, created_at, merged_at])

    # Print the table
    print(table)
