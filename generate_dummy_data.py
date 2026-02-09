import random
import datetime
import json

# Generate dummy data for GitHub issues, pull requests, labels, milestones, and assignees

def generate_dummy_data(num_issues=50, num_prs=25, num_labels=10, num_milestones=5, num_assignees=5):
    issues = []
    pull_requests = []
    labels = [f"Label {i+1}" for i in range(num_labels)]
    milestones = [f"Milestone {i+1}" for i in range(num_milestones)]
    assignees = [f"User {i+1}" for i in range(num_assignees)]

    # Generate issues
    for i in range(num_issues):
        created_at = datetime.datetime.utcnow() - datetime.timedelta(days=random.randint(1, 30))
        issues.append({
            "issue_number": i + 1,
            "title": f"Issue {i + 1} Title",
            "body": f"Detailed description for issue {i + 1}.",
            "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": created_at + datetime.timedelta(days=random.randint(1, 10)).strftime('%Y-%m-%d %H:%M:%S'),
            "closed_at": (created_at + datetime.timedelta(days=random.randint(1, 30)).strftime('%Y-%m-%d %H:%M:%S')),
            "labels": random.sample(labels, k=random.randint(1, 3)),
            "assignees": random.sample(assignees, k=random.randint(1, 2)),
            "milestone": random.choice(milestones)
        })

    # Generate pull requests
    for i in range(num_prs):
        created_at = datetime.datetime.utcnow() - datetime.timedelta(days=random.randint(1, 30))
        pull_requests.append({
            "pr_number": i + 1,
            "title": f"PR {i + 1} Title",
            "body": f"Detailed description for pull request {i + 1}.",
            "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "merged_at": (created_at + datetime.timedelta(days=random.randint(0, 10))).strftime('%Y-%m-%d %H:%M:%S'),
            "labels": random.sample(labels, k=random.randint(1, 3)),
            "assignees": random.sample(assignees, k=random.randint(1, 2)),
            "milestone": random.choice(milestones)
        })

    return json.dumps({"issues": issues, "pull_requests": pull_requests}, indent=4)

if __name__ == '__main__':
    dummy_data = generate_dummy_data()
    print(dummy_data)
