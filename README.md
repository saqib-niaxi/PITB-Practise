# Team Collaboration Repo

This repository is used to collaborate with a friend on tasks assigned by the team lead.

## Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable, production-ready code |
| `staging` | Pre-production testing before merging to main |
| `dev` | Active development and integration |

## Workflow

1. Pull the latest changes from `dev`
2. Create a new branch for each task: `feature/<task-name>` or `fix/<task-name>`
3. Complete the task on your branch
4. Open a Pull Request (PR) into `dev`
5. After review and approval, merge to `staging` for testing
6. Once tested, merge `staging` into `main`

## Getting Started

```bash
# Clone the repo
git clone <repo-url>

# Switch to dev branch
git checkout dev

# Create a new branch for your task
git checkout -b feature/your-task-name

# After completing the task, push and open a PR
git push origin feature/your-task-name
```
