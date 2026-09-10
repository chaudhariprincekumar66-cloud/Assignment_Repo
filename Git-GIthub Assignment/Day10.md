Goal: Practice merging a feature branch into main locally.

Create a new branch:
git checkout -b feature-local-merge
Create a file named local-merge.txt and write 3–4 lines about what you learned today about local merge.
Stage and commit:
git add .
git commit -m "Add local-merge notes"
Switch back to main:
git checkout main
Merge the feature branch:
git merge feature-local-merge
Push main:
git push origin main
Run git log --oneline -5 and take a screenshot of the history.
Submit: Screenshot of git log --oneline after the merge + confirmation that the file is on GitHub main.

