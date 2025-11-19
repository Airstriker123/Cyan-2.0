# GitHub Project Gantt Chart Setup

This guide explains how to set up a GitHub Project with Gantt chart visualization to track your commits.

## Overview

This repository includes automation to sync commits to a GitHub Project, which can be visualized as a Gantt chart using GitHub's Roadmap view.

## Prerequisites

- GitHub account with access to this repository
- GitHub Projects (Beta/v2) enabled
- Personal Access Token (PAT) with appropriate permissions

## Setup Instructions

### 1. Create a GitHub Project

1. Go to your GitHub profile or organization
2. Click on "Projects" tab
3. Click "New Project"
4. Choose "Table" or "Roadmap" template
5. Name it (e.g., "Cyan 2.0 Development Roadmap")

### 2. Configure Project Fields

To enable Gantt chart visualization, add the following fields to your project:

1. **Title** (default text field)
2. **Status** (default single select):
   - Todo
   - In Progress
   - Done
3. **Start Date** (date field)
4. **End Date** (date field)
5. **Priority** (single select):
   - High
   - Medium
   - Low
6. **Assignees** (default field)

### 3. Get Your Project URL

1. Open your project
2. Copy the URL from your browser (e.g., `https://github.com/users/Airstriker123/projects/1`)
3. Note the project number at the end

### 4. Create Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "Cyan Project Automation")
4. Select the following scopes:
   - `repo` (Full control of private repositories)
   - `project` (Full control of projects)
   - `write:org` (if using organization project)
5. Click "Generate token"
6. Copy the token (you won't see it again!)

### 5. Add Token to Repository Secrets

1. Go to your repository → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `PROJECT_TOKEN`
4. Value: Paste your Personal Access Token
5. Click "Add secret"

### 6. Update Workflow Configuration

Edit `.github/workflows/project-gantt-sync.yml`:

```yaml
project-url: https://github.com/users/YOUR_USERNAME/projects/YOUR_PROJECT_NUMBER
```

Replace:
- `YOUR_USERNAME` with your GitHub username
- `YOUR_PROJECT_NUMBER` with your project number

### 7. Enable Gantt Chart View

1. Open your GitHub Project
2. Click on the "+" icon next to your existing views
3. Select "New view"
4. Choose "Roadmap" view type
5. Configure the view:
   - Group by: Status
   - Sort by: Start date
   - Show fields: Title, Status, Start Date, End Date
6. Save the view

## Usage

### Automatic Tracking

Once set up, the workflow will automatically:
- Trigger on every push to main/master/develop branches
- Extract commit information (title, author, date, SHA)
- Create a new item in your GitHub Project
- Alternatively create an issue if project API fails

### Manual Workflow Trigger

You can manually trigger the workflow:
1. Go to Actions tab
2. Select "Sync Commits to GitHub Project"
3. Click "Run workflow"
4. Select branch and run

### Viewing as Gantt Chart

1. Open your GitHub Project
2. Switch to the "Roadmap" view you created
3. You'll see commits displayed in a timeline/Gantt chart format
4. Drag and adjust dates as needed

## Tips for Better Gantt Charts

1. **Use meaningful commit messages**: These become the task titles
2. **Add labels**: Use labels like `feature`, `bugfix`, `enhancement` for better organization
3. **Set milestones**: Group related commits under milestones
4. **Update dates**: Adjust start/end dates in the project view to reflect actual work periods
5. **Use status**: Move items through Todo → In Progress → Done as work progresses

## Alternative: Manual Project Integration

If the automated workflow doesn't work or you prefer manual control:

1. Create issues for each major commit or feature
2. Add the `commit-tracking` label
3. Add issues to your project
4. Set start and end dates manually
5. View in Roadmap (Gantt chart) view

## Troubleshooting

### Workflow not running
- Check that the workflow file is in `.github/workflows/`
- Verify branch names match your repository
- Check Actions tab for error messages

### Items not appearing in project
- Verify `PROJECT_TOKEN` is set correctly in repository secrets
- Check project URL is correct in workflow file
- Ensure token has necessary permissions
- Review Actions logs for specific errors

### Gantt chart not showing properly
- Ensure Start Date and End Date fields exist in your project
- Check that items have dates assigned
- Switch to Roadmap view to see Gantt chart
- Make sure project is using Projects (Beta/v2), not classic projects

## Project Structure

```
.github/
└── workflows/
    └── project-gantt-sync.yml    # Workflow to sync commits to project
docs/
└── GANTT_CHART_SETUP.md          # This documentation
```

## Example Roadmap View

Your Gantt chart will display:
```
Status: In Progress
┌─────────────────────────────────────────┐
│ [Commit] Initial setup      ████████    │
│ [Commit] Add new feature    ████████    │
│ [Commit] Fix bug            ████        │
└─────────────────────────────────────────┘
      Jan        Feb        Mar
```

## Additional Resources

- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Roadmap View Guide](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout)

## Support

For issues or questions about this setup:
1. Check the Actions tab for workflow errors
2. Review GitHub Projects documentation
3. Open an issue in this repository

---

*Last updated: November 2025*
