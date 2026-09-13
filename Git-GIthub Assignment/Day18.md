Create a new repository called reflog-practice-part1
Create 3 commits:
C0: README.md with project title
C1: index.html with <h1>Welcome</h1>
C2: style.css with basic styling
Accidentally delete C1 and C2 using git reset --hard <C0-commit-hash>
Use git reflog to find the lost C2 commit
Recover C2 (and C1) using detached HEAD + branch + merge
Verify all commits are restored
Deliverables
✅ Screenshot of: git log --oneline BEFORE reset
✅ Screenshot of: git log --oneline AFTER reset (showing lost commits)
✅ Screenshot of: git reflog output (highlighting the commit you recovered)
✅ Screenshot of: git log --oneline AFTER recovery (showing all commits restored)
✅ Push final repository to GitHub
<img width="897" height="173" alt="Screenshot 2026-09-11 235942" src="https://github.com/user-attachments/assets/63d499bb-ac56-4e43-adda-da63028a127d" />
<img width="1073" height="477" alt="Screenshot 2026-09-12 000025" src="https://github.com/user-attachments/assets/a8bef78c-3621-4f77-a6ec-7ea43487b131" />
<img width="1415" height="160" alt="Screenshot 2026-09-11 235959" src="https://github.com/user-attachments/assets/a3941e10-0af3-4beb-8561-d66dc74a0007" />
Create a new repository called reflog-practice-part2
Create 3 commits:
C0: README.md with just title
C1: app.js with basic function
C2: utils.js with helper functions
Realize you need to add description to README (C0) without losing C1 and C2
Create a branch at C0: git switch -c rework/readme-update <C0-hash>
Update README.md with description, commit
Merge the branch back to main
Verify C0, C1, and C2 are all preserved
Deliverables
✅ Screenshot of: git log --oneline BEFORE creating branch
✅ Screenshot of: git branch output (showing both branches)
✅ Screenshot of: git log --oneline --graph (showing merge)
✅ Screenshot of: Final README.md content
✅ Push final repository to GitHub
<img width="1032" height="377" alt="Screenshot 2026-09-13 152301" src="https://github.com/user-attachments/assets/ad75a15c-5af3-41a2-a029-cd25c410a84a" />
<img width="975" height="280" alt="Screenshot 2026-09-13 152414" src="https://github.com/user-attachments/assets/2c6d32a0-8461-49db-82c0-14a4391f34be" />
<img width="1032" height="377" alt="Screenshot 2026-09-13 152301" src="https://github.com/user-attachments/assets/38762512-350a-41c4-a63b-a24f52a2b251" />
<img width="1091" height="267" alt="Screenshot 2026-09-13 152245" src="https://github.com/user-attachments/assets/bd53fbc3-048d-4541-9999-9ecc1762a8c1" />
<img width="1213" height="368" alt="Screenshot 2026-09-13 152225" src="https://github.com/user-attachments/assets/0c49ba70-8178-465b-9a23-c5f74320603c" />
<img width="985" height="133" alt="Screenshot 2026-09-13 152032" src="https://github.com/user-attachments/assets/54b0f303-027c-4840-bdec-bfcfb13c95bf" />


