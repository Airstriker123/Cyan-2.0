# GitHub Project Gantt Chart - Quick Reference

## 🚀 Quick Setup (5 minutes)

### 1. Create GitHub Project
- Go to https://github.com/users/Airstriker123/projects
- Click "New Project" → Choose "Roadmap" template
- Name it "Cyan 2.0 Development"

### 2. Get Project Number
- Open your project
- Check URL: `https://github.com/users/Airstriker123/projects/[NUMBER]`
- Note this number

### 3. Create Personal Access Token
- Go to https://github.com/settings/tokens
- Click "Generate new token (classic)"
- Select scopes: `repo`, `project`
- Copy the token

### 4. Add to Repository
- Go to repository Settings → Secrets → Actions
- Add secret: `PROJECT_TOKEN` = your token

### 5. Update Workflow
Edit `.github/workflows/project-gantt-sync.yml`:
```yaml
project-url: https://github.com/users/Airstriker123/projects/YOUR_NUMBER
```

### 6. Enable Gantt View
- Open project → Click "+" next to views
- Select "New view" → "Roadmap"
- This is your Gantt chart!

## 🎯 Usage

### Automatic (Recommended)
- Just commit and push to main/master/develop
- Workflow runs automatically
- Commits appear in project

### Manual
```bash
# Run locally to preview
python3 scripts/generate_gantt.py

# Trigger workflow manually
# Go to Actions → Sync Commits to GitHub Project → Run workflow
```

## 📊 Viewing the Gantt Chart

1. Open your GitHub Project
2. Switch to "Roadmap" view
3. See commits as timeline bars
4. Drag to adjust dates
5. Group by status/priority

## 🔧 Customization

### Add Custom Fields
In your project:
- Click "+" to add field
- Choose type: Text, Number, Date, Single select, etc.
- Use for priority, category, effort, etc.

### Filter & Sort
- Use project filters to show specific commits
- Sort by date, author, status
- Create custom views for different perspectives

## 📝 Tips

1. **Meaningful commits**: Use clear messages - they become task titles
2. **Use labels**: Tag commits with feature/bugfix/docs
3. **Set milestones**: Group related work
4. **Update dates**: Adjust timeline in project view
5. **Add assignees**: Track who's working on what

## 🔍 Troubleshooting

### Workflow fails
- Check Actions tab for errors
- Verify PROJECT_TOKEN is set
- Ensure project URL is correct

### Commits not showing
- Check project URL format
- Verify token permissions
- Try manual workflow trigger

### No Gantt chart
- Ensure using Projects v2 (not classic)
- Switch to "Roadmap" view
- Add Start/End date fields

## 📚 Full Documentation
See [GANTT_CHART_SETUP.md](GANTT_CHART_SETUP.md) for complete details.

## ⚡ Example Workflow

```bash
# 1. Make changes
git add .
git commit -m "Add new feature"

# 2. Push (triggers workflow)
git push origin main

# 3. View in project
# → Open GitHub Project
# → Switch to Roadmap view
# → See commit appear in timeline!
```

---

**Need help?** Check the full setup guide or open an issue.
