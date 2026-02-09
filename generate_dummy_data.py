import requests
import random
import string

# Configuration for GitHub API
GITHUB_API_URL = 'https://api.github.com'
REPO_OWNER = 'swornima-shakya-citytech'
REPO_NAME = 'sample-citytech-project'

# Function to generate random string
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to create dummy issues
def create_dummy_issues(num_issues):
    for _ in range(num_issues):
        issue_title = f'Issue {random_string()}'
        issue_body = f'This is a dummy issue for testing purposes.'
        requests.post(f'{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues', json={
            'title': issue_title,
            'body': issue_body
        })

# Function to create dummy PRs
def create_dummy_prs(num_prs):
    for _ in range(num_prs):
        pr_title = f'PR {random_string()}'
        pr_body = f'This is a dummy PR for testing purposes.'
        requests.post(f'{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls', json={
            'title': pr_title,
            'body': pr_body,
            'head': 'feature-branch',
            'base': 'main'
        })

# Function to create dummy labels
def create_dummy_labels():
    labels = ['bug', 'feature', 'documentation', 'enhancement']
    for label in labels:
        requests.post(f'{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/labels', json={
            'name': label,
            'color': random_string(6)
        })

# Function to create dummy milestones
def create_dummy_milestones():
    for _ in range(5):
        milestone_title = f'Milestone {random_string()}'
        requests.post(f'{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/milestones', json={
            'title': milestone_title
        })

# Function to assign random assignees
def assign_dummy_assignees(num_assignees):
    for _ in range(num_assignees):
        assignee = random_string()  # Replace with actual GitHub usernames
        requests.post(f'{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues/1/assignees', json={
            'assignees': [assignee]
        })

# Main execution
if __name__ == '__main__':
    create_dummy_issues(50)
    create_dummy_prs(25)
    create_dummy_labels()
    create_dummy_milestones()
    assign_dummy_assignees(5)
