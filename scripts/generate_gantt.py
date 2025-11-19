#!/usr/bin/env python3
"""
Commit Gantt Chart Generator
Generates a visual representation of git commits in a Gantt chart format.
This can be used to preview your commit timeline before syncing to GitHub Projects.
"""

import subprocess
import json
from datetime import datetime
from collections import defaultdict

def get_git_commits(branch='HEAD', limit=50):
    """Get git commits with detailed information."""
    cmd = [
        'git', 'log', branch,
        f'--max-count={limit}',
        '--pretty=format:%H|%an|%ae|%ad|%s',
        '--date=iso'
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        commits = []
        
        for line in result.stdout.strip().split('\n'):
            if not line:
                continue
            parts = line.split('|', 4)
            if len(parts) == 5:
                sha, author, email, date_str, message = parts
                commits.append({
                    'sha': sha[:7],
                    'author': author,
                    'email': email,
                    'date': date_str,
                    'message': message
                })
        
        return commits
    except subprocess.CalledProcessError as e:
        print(f"Error getting git commits: {e}")
        return []

def generate_gantt_text(commits):
    """Generate a text-based Gantt chart from commits."""
    if not commits:
        print("No commits found.")
        return
    
    print("\n" + "="*80)
    print("COMMIT GANTT CHART - Timeline View")
    print("="*80 + "\n")
    
    # Group commits by date
    commits_by_date = defaultdict(list)
    for commit in commits:
        date = datetime.fromisoformat(commit['date'].replace(' +', '+').replace(' -', '-'))
        date_str = date.strftime('%Y-%m-%d')
        commits_by_date[date_str].append(commit)
    
    # Print timeline
    for date in sorted(commits_by_date.keys(), reverse=True):
        print(f"\n📅 {date}")
        print("-" * 80)
        
        for commit in commits_by_date[date]:
            # Create visual bar
            bar_length = min(len(commit['message']), 40)
            bar = "█" * (bar_length // 4) if bar_length > 0 else "█"
            
            print(f"  [{commit['sha']}] {bar}")
            print(f"  └─ {commit['message'][:60]}")
            print(f"     Author: {commit['author']}")
            print()

def generate_gantt_markdown(commits, output_file='docs/COMMIT_TIMELINE.md'):
    """Generate a markdown file with commit timeline suitable for GitHub."""
    if not commits:
        print("No commits found.")
        return
    
    # Group commits by date
    commits_by_date = defaultdict(list)
    for commit in commits:
        date = datetime.fromisoformat(commit['date'].replace(' +', '+').replace(' -', '-'))
        date_str = date.strftime('%Y-%m-%d')
        commits_by_date[date_str].append(commit)
    
    # Generate markdown content
    content = [
        "# Commit Timeline",
        "",
        "This document shows a timeline of commits in this repository.",
        "",
        "## Timeline View",
        ""
    ]
    
    for date in sorted(commits_by_date.keys(), reverse=True):
        content.append(f"### {date}")
        content.append("")
        
        for commit in commits_by_date[date]:
            content.append(f"- **[{commit['sha']}]** {commit['message']}")
            content.append(f"  - Author: {commit['author']}")
            content.append(f"  - Email: {commit['email']}")
            content.append("")
    
    # Add Gantt chart format for GitHub Projects
    content.extend([
        "",
        "## Gantt Chart Format",
        "",
        "To view as a Gantt chart:",
        "1. Create a GitHub Project",
        "2. Add Roadmap view",
        "3. Create items from commits above",
        "4. Set start/end dates based on commit dates",
        "",
        "## Import to GitHub Projects",
        "",
        "Use the workflow in `.github/workflows/project-gantt-sync.yml` to automatically",
        "sync commits to your GitHub Project.",
        ""
    ])
    
    # Write to file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))
        print(f"\n✅ Markdown timeline written to: {output_file}")
    except Exception as e:
        print(f"❌ Error writing markdown file: {e}")

def generate_json_export(commits, output_file='commits_export.json'):
    """Export commits as JSON for potential import into project management tools."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(commits, f, indent=2)
        print(f"✅ JSON export written to: {output_file}")
    except Exception as e:
        print(f"❌ Error writing JSON file: {e}")

def main():
    """Main function to generate commit visualizations."""
    print("🔍 Fetching git commits...")
    
    # Get commits
    commits = get_git_commits(limit=50)
    
    if not commits:
        print("❌ No commits found or not in a git repository.")
        return
    
    print(f"✅ Found {len(commits)} commits\n")
    
    # Generate text-based Gantt chart
    generate_gantt_text(commits)
    
    # Generate markdown timeline
    generate_gantt_markdown(commits)
    
    # Optionally export to JSON
    # generate_json_export(commits, '/tmp/commits_export.json')
    
    print("\n" + "="*80)
    print("Next steps:")
    print("1. Review the timeline above")
    print("2. Check docs/COMMIT_TIMELINE.md for markdown version")
    print("3. Follow docs/GANTT_CHART_SETUP.md to sync with GitHub Projects")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
