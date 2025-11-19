# Cyan 2.0

no custom installs required + faster load times!

## GitHub Project Gantt Chart

This repository includes automation for tracking commits in a GitHub Project with Gantt chart visualization.

### Quick Start

1. **View Setup Guide**: See [docs/GANTT_CHART_SETUP.md](docs/GANTT_CHART_SETUP.md) for complete instructions
2. **Create Project**: Set up a GitHub Project (Beta/v2) with Roadmap view
3. **Configure Workflow**: Update `.github/workflows/project-gantt-sync.yml` with your project URL
4. **Add Token**: Add `PROJECT_TOKEN` to repository secrets
5. **Enable**: Push commits to main/master/develop branches to auto-track in your project

### Features

- ✅ Automatic commit tracking in GitHub Projects
- ✅ Gantt chart visualization via Roadmap view
- ✅ Commit details preserved (author, date, SHA)
- ✅ Manual workflow trigger option
- ✅ Fallback to issue creation

For detailed setup instructions, see the [Gantt Chart Setup Guide](docs/GANTT_CHART_SETUP.md).
