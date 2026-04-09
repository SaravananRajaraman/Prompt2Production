#!/bin/bash
# Script to sync documentation from main branch to website branch
# Usage: bash sync-branches.sh

set -e  # Exit on error

echo "🔄 Starting sync from main to website branch..."

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Error: Not in a git repository"
    exit 1
fi

# Get current branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "📌 Current branch: $CURRENT_BRANCH"

# Step 1: Fetch latest
echo "📋 Fetching latest from remote..."
git fetch origin

# Step 2: Checkout website branch
echo "📋 Switching to website branch..."
git checkout website

# Step 3: Pull latest website branch
echo "📋 Pulling latest website branch..."
git pull origin website

# Step 4: Sync README.md
echo "📋 Syncing README.md from main..."
git checkout origin/main -- README.md

# Step 5: Sync markdown files from main's docs/
echo "📋 Syncing documentation files from main..."
git ls-tree -r --name-only origin/main docs/ | grep '\.md$' | grep -v 'examples/' | while read file; do
    filename=$(basename "$file")
    echo "  📄 Syncing $file -> $filename"
    git checkout origin/main -- "$file"
    if [ -f "$file" ]; then
        mv -f "$file" "$filename" || cp "$file" "$filename"
    fi
done

# Step 6: Sync examples directory
echo "📋 Syncing examples directory..."
git checkout origin/main -- docs/examples/ 2>/dev/null || true

# Step 7: Remove .md files from docs/ (keep examples/)
echo "📋 Cleaning up docs/ directory..."
find docs/ -maxdepth 1 -name "*.md" -type f -delete 2>/dev/null || true

# Step 8: Check for changes
echo ""
if git diff --cached --quiet && git diff --quiet; then
    echo "✅ No changes to commit. Website branch is already up to date!"
    exit 0
fi

# Show changes
echo "📝 Changes detected:"
git status --short

# Step 9: Commit and push
echo ""
echo "📋 Staging changes..."
git add -A

echo "📋 Committing changes..."
git commit -m "chore: sync documentation from main branch"

echo "📋 Pushing to remote..."
git push origin website

# Step 10: Return to original branch if not website
if [ "$CURRENT_BRANCH" != "website" ]; then
    echo "📋 Returning to $CURRENT_BRANCH branch..."
    git checkout "$CURRENT_BRANCH"
fi

echo ""
echo "✅ Sync completed successfully!"
echo ""
echo "📊 Summary:"
echo "  ✓ Synced README.md from main"
echo "  ✓ Synced documentation files from main's docs/ to website root"
echo "  ✓ Synced examples directory"  
echo "  ✓ Preserved all website-specific files (_config.yml, assets/, _includes/, etc.)"
#!/bin/bash
# Script to sync documentation from main branch to website branch
# Usage: bash sync-branches.sh

set -e  # Exit on error

echo "🔄 Starting sync from main to website branch..."

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Error: Not in a git repository"
    exit 1
fi

# Get current branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "📌 Current branch: $CURRENT_BRANCH"

# Step 1: Fetch latest
echo "📋 Fetching latest from remote..."
git fetch origin

# Step 2: Checkout website branch
echo "📋 Switching to website branch..."
git checkout website

# Step 3: Pull latest website branch
echo "📋 Pulling latest website branch..."
git pull origin website

# Step 4: Sync README.md
echo "📋 Syncing README.md from main..."
git checkout origin/main -- README.md

# Step 5: Sync markdown files from main's docs/
echo "📋 Syncing documentation files from main..."
git ls-tree -r --name-only origin/main docs/ | grep '\.md$' | grep -v 'examples/' | while read file; do
    filename=$(basename "$file")
    echo "  📄 Syncing $file -> $filename"
    git checkout origin/main -- "$file"
    if [ -f "$file" ]; then
        mv -f "$file" "$filename" || cp "$file" "$filename"
    fi
done

# Step 6: Sync examples directory
echo "📋 Syncing examples directory..."
git checkout origin/main -- docs/examples/ 2>/dev/null || true

# Step 7: Remove .md files from docs/ (keep examples/)
echo "📋 Cleaning up docs/ directory..."
find docs/ -maxdepth 1 -name "*.md" -type f -delete 2>/dev/null || true

# Step 8: Check for changes
echo ""
if git diff --cached --quiet && git diff --quiet; then
    echo "✅ No changes to commit. Website branch is already up to date!"
    exit 0
fi

# Show changes
echo "📝 Changes detected:"
git status --short

# Step 9: Commit and push
echo ""
echo "📋 Staging changes..."
git add -A

echo "📋 Committing changes..."
git commit -m "chore: sync documentation from main branch"

echo "📋 Pushing to remote..."
git push origin website

# Step 10: Return to original branch if not website
if [ "$CURRENT_BRANCH" != "website" ]; then
    echo "📋 Returning to $CURRENT_BRANCH branch..."
    git checkout "$CURRENT_BRANCH"
fi

echo ""
echo "✅ Sync completed successfully!"
echo ""
echo "📊 Summary:"
echo "  ✓ Synced README.md from main"
echo "  ✓ Synced documentation files from main's docs/ to website root"
echo "  ✓ Synced examples directory"  
echo "  ✓ Preserved all website-specific files (_config.yml, assets/, _includes/, etc.)"
