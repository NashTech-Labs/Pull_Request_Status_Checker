# Pull Request Status Checker

This Python script fetches and displays the status of pull requests (PRs) for a specified GitHub repository. It provides details such as PR number, title, author, state (open/closed), and the dates they were created and merged, all formatted in a readable table.

## Features

1. Fetches pull requests from a GitHub repository.
2. Displays PRs with their current status: open, closed, or not merged.

## Requirements

 - Python 3.x
 - requests library
 - prettytable library

## Installation

1. **Clone the repository:**
 
    ```bash
    git clone https://github.com/NashTech-Labs/Pull_Request_Status_Checker/.git
    cd Pull_Request_Status_Checker
    ```

2. **Install required packages:**
    
    If you are in an externally managed environment, you may need to create a virtual environment first:
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    Then, install the necessary libraries:

    pip install requests prettytable
    ```

## Usage

Run the script from the command line by specifying the GitHub repository in the format owner/repo:

   ```bash
        python3 PR_status.py <owner/repo>
        ex: 
        To check the PR status for the repository NashTech-Labs/linux-installation-scripts, use the command:

        python3 PR_status.py NashTech-Labs/linux-installation-scripts
   ```

# Output

The script will output a table with the following columns:

 PR Number: The number assigned to the pull request.
 Title: The title of the pull request.
 Author: The GitHub username of the author who created the PR.
 State: The current state of the PR (open, closed, or not merged), highlighted.
 Created At: The date when the PR was created.
 Merged At: The date when the PR was merged (if applicable).
