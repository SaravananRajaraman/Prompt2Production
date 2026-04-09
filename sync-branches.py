#!/usr/bin/env python3
"""
Script to sync documentation from main branch to website branch.
This script can be run manually to update the website branch with latest changes from main.

Usage:
    python sync_branches.py
    
Requirements:
    - Git must be installed and available in PATH
    - You must be in a git repository
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a shell command and handle errors."""
    print(f"📋 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Error: {result.stderr}")
            return False
        print(f"✅ {description} completed")
        return True
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def main():
    print("🔄 Starting sync from main to website branch...\n")
    
    # Check if we're in a git repository
    if not run_command("git rev-parse --git-dir", "Checking git repository"):
        return 1
    
    # Get current branch
    result = subprocess.run("git rev-parse --abbrev-ref HEAD", shell=True, capture_output=True, text=True)
    current_branch = result.stdout.strip()
    print(f"Current branch: {current_branch}\n")
    
    # Step 1: Fetch latest from origin
    if not run_command("git fetch origin", "Fetching latest from remote"):
        return 1
    
    # Step 2: Checkout website branch
    if not run_command("git checkout website", "Switching to website branch"):
        return 1
    
    # Step 3: Pull latest website branch
    if not run_command("git pull origin website", "Pulling latest website branch"):
        return 1
    
    # Step 4: Sync README.md from main
    if not run_command("git checkout origin/main -- README.md", "Syncing README.md from main"):
        return 1
    
    # Step 5: Sync markdown files from main's docs/ to website root
    print("🔄 Syncing documentation files...")
    
    # Get list of .md files from main's docs/
    result = subprocess.run(
        "git ls-tree -r --name-only origin/main docs/ | findstr /R \"\\.md$\"",
        shell=True,
        capture_output=True,
        text=True
    )
    
    md_files = [f.strip() for f in result.stdout.strip().split('\n') if f.strip() and 'examples' not in f]
    
    if md_files:
        for file in md_files:
            filename = os.path.basename(file)
            print(f"  Syncing {file} -> {filename}")
            
            # Checkout the file from main
            if subprocess.run(f"git checkout origin/main -- \"{file}\"", shell=True).returncode == 0:
                # Copy/move to root if not already there
                if file != filename:
                    if os.path.exists(file):
                        # If file exists in docs/, copy it to root
                        with open(file, 'r', encoding='utf-8') as src:
                            with open(filename, 'w', encoding='utf-8') as dst:
                                dst.write(src.read())
                print(f"    ✓ {filename} synced")
    
    # Step 6: Sync examples directory
    if not run_command("git checkout origin/main -- docs/examples/ || exit 0", "Syncing examples directory"):
        pass  # This is optional, don't fail if it doesn't exist
    
    # Step 7: Check for changes
    result = subprocess.run("git status --short", shell=True, capture_output=True, text=True)
    changes = result.stdout.strip()
    
    if not changes:
        print("\n✅ No changes to commit. Website branch is already up to date!")
        return 0
    
    print(f"\n📝 Changes detected:\n{changes}\n")
    
    # Step 8: Commit changes
    if not run_command("git add -A", "Staging changes"):
        return 1
    
    commit_msg = "chore: sync documentation from main branch"
    if not run_command(f'git commit -m "{commit_msg}"', "Committing changes"):
        return 1
    
    # Step 9: Push to origin
    if not run_command("git push origin website", "Pushing to remote"):
        return 1
    
    # Step 10: Return to original branch
    if current_branch != "website":
        run_command(f"git checkout {current_branch}", f"Returning to {current_branch} branch")
    
    print("\n✅ Sync completed successfully!")
    print("\n📊 Summary:")
    print("  • Synced README.md from main")
    print("  • Synced documentation files from main's docs/ to website root")
    print("  • Synced examples directory")
    print("  • Preserved all website-specific files (_config.yml, assets/, _includes/, etc.)")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
#!/usr/bin/env python3
"""
Script to sync documentation from main branch to website branch.
This script can be run manually to update the website branch with latest changes from main.

Usage:
    python sync_branches.py
    
Requirements:
    - Git must be installed and available in PATH
    - You must be in a git repository
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a shell command and handle errors."""
    print(f"📋 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Error: {result.stderr}")
            return False
        print(f"✅ {description} completed")
        return True
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def main():
    print("🔄 Starting sync from main to website branch...\n")
    
    # Check if we're in a git repository
    if not run_command("git rev-parse --git-dir", "Checking git repository"):
        return 1
    
    # Get current branch
    result = subprocess.run("git rev-parse --abbrev-ref HEAD", shell=True, capture_output=True, text=True)
    current_branch = result.stdout.strip()
    print(f"Current branch: {current_branch}\n")
    
    # Step 1: Fetch latest from origin
    if not run_command("git fetch origin", "Fetching latest from remote"):
        return 1
    
    # Step 2: Checkout website branch
    if not run_command("git checkout website", "Switching to website branch"):
        return 1
    
    # Step 3: Pull latest website branch
    if not run_command("git pull origin website", "Pulling latest website branch"):
        return 1
    
    # Step 4: Sync README.md from main
    if not run_command("git checkout origin/main -- README.md", "Syncing README.md from main"):
        return 1
    
    # Step 5: Sync markdown files from main's docs/ to website root
    print("🔄 Syncing documentation files...")
    
    # Get list of .md files from main's docs/
    result = subprocess.run(
        "git ls-tree -r --name-only origin/main docs/ | findstr /R \"\\.md$\"",
        shell=True,
        capture_output=True,
        text=True
    )
    
    md_files = [f.strip() for f in result.stdout.strip().split('\n') if f.strip() and 'examples' not in f]
    
    if md_files:
        for file in md_files:
            filename = os.path.basename(file)
            print(f"  Syncing {file} -> {filename}")
            
            # Checkout the file from main
            if subprocess.run(f"git checkout origin/main -- \"{file}\"", shell=True).returncode == 0:
                # Copy/move to root if not already there
                if file != filename:
                    if os.path.exists(file):
                        # If file exists in docs/, copy it to root
                        with open(file, 'r', encoding='utf-8') as src:
                            with open(filename, 'w', encoding='utf-8') as dst:
                                dst.write(src.read())
                print(f"    ✓ {filename} synced")
    
    # Step 6: Sync examples directory
    if not run_command("git checkout origin/main -- docs/examples/ || exit 0", "Syncing examples directory"):
        pass  # This is optional, don't fail if it doesn't exist
    
    # Step 7: Check for changes
    result = subprocess.run("git status --short", shell=True, capture_output=True, text=True)
    changes = result.stdout.strip()
    
    if not changes:
        print("\n✅ No changes to commit. Website branch is already up to date!")
        return 0
    
    print(f"\n📝 Changes detected:\n{changes}\n")
    
    # Step 8: Commit changes
    if not run_command("git add -A", "Staging changes"):
        return 1
    
    commit_msg = "chore: sync documentation from main branch"
    if not run_command(f'git commit -m "{commit_msg}"', "Committing changes"):
        return 1
    
    # Step 9: Push to origin
    if not run_command("git push origin website", "Pushing to remote"):
        return 1
    
    # Step 10: Return to original branch
    if current_branch != "website":
        run_command(f"git checkout {current_branch}", f"Returning to {current_branch} branch")
    
    print("\n✅ Sync completed successfully!")
    print("\n📊 Summary:")
    print("  • Synced README.md from main")
    print("  • Synced documentation files from main's docs/ to website root")
    print("  • Synced examples directory")
    print("  • Preserved all website-specific files (_config.yml, assets/, _includes/, etc.)")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
