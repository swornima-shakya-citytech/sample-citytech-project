import requests
import random
import string
import os

# Configuration for GitHub API
GITHUB_API_URL = 'https://api.github.com'
REPO_OWNER = 'swornima-shakya-citytech'
REPO_NAME = 'sample-citytech-project'

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # Replace with your token

HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Function to generate random string
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to create dummy issues
def create_dummy_issues(num_issues):
    for _ in range(num_issues):
        issue_title = f'Issue {random_string()}'
        issue_body = f'This is a dummy issue for testing purposes.'
        response = requests.post(
            f'{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues',
            headers=HEADERS,
            json={'title': issue_title, 'body': issue_body}
        )
        print(response.status_code, response.json())

# Function to create dummy PRs
def create_dummy_prs(num_prs):
    for _ in range(num_prs):
        pr_title = f'PR {random_string()}'
        pr_body = f'This is a dummy PR for testing purposes.'
        response = requests.post(
            f'{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls',
            headers=HEADERS,
            json={'title': pr_title, 'body': pr_body, 'head': 'feature-branch', 'base': 'main'}
        )
        print(response.status_code, response.json())

# Function to create dummy labels
def create_dummy_labels():
    labels = [
        ('bug', 'ff0000'),
        ('feature', '00ff00'),
        ('documentation', '0000ff'),
        ('enhancement', 'ffff00')
    ]
    for label, color in labels:
        response = requests.post(
            f'{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/labels',
            headers=HEADERS,
            json={'name': label, 'color': color}
        )
        print(response.status_code, response.json())

# Function to create dummy milestones
def create_dummy_milestones():
    for _ in range(5):
        milestone_title = f'Milestone {random_string()}'
        response = requests.post(
            f'{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/milestones',
            headers=HEADERS,
            json={'title': milestone_title}
        )
        print(response.status_code, response.json())

# Function to assign random assignees
def assign_dummy_assignees(num_assignees):
    for _ in range(num_assignees):
        assignee = random_string()  # Replace with actual GitHub usernames
        response = requests.post(
            f'{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues/1/assignees',
            headers=HEADERS,
            json={'assignees': [assignee]}
        )
        print(response.status_code, response.json())

# Main execution
if __name__ == '__main__':
    # create_dummy_issues(50)
    create_dummy_prs(2)
    print('Dummy issues and PRs created.')
    create_dummy_labels()
    print('Dummy labels created.')
    # create_dummy_milestones()
    # print('Dummy milestones created.')
    # assign_dummy_assignees(5)
    print('Dummy data generation completed.')
