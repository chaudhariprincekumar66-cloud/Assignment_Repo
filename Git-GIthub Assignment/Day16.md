Create or open your practice repository.
Make three simple commits (you can create/edit a file called notes.txt):
Commit 1: Add some text → commit message "First note"
Commit 2: Add more text → commit message "Second note"
Commit 3: Add more text → commit message "Third note"
Run:
git log --oneline
Reset to the previous commit using:
git reset HEAD~1
Run git log --oneline and git status again.
Observe what happened to the latest commit and the file changes.
Submit:

Screenshot of git log --oneline before reset
Screenshot of git log --oneline and git status after reset
Repository link
<img width="997" height="213" alt="Screenshot 2026-09-06 114052" src="https://github.com/user-attachments/assets/b5c73da3-ea50-4be2-b098-1a36e94078e5" />
<img width="955" height="173" alt="Screenshot 2026-09-06 114127" src="https://github.com/user-attachments/assets/a0ddb682-5353-428c-92f5-1d55202bbf4a" />
Create a new file demo.txt and make two commits on it.

Perform the following one by one (create fresh commits each time if needed):

A. Soft Reset

git reset --soft HEAD~1
git status
B. Mixed Reset

git reset --mixed HEAD~1
git status
C. Hard Reset

git reset --hard HEAD~1
git status
write the short answers in your own words in your notebook:

What is the difference between --soft, --mixed, and --hard?
Which one keeps changes staged?
Which one discards the changes completely?
When should you avoid --hard?
Submit:

Screenshots of git status after each type of reset (--soft, --mixed, --hard)
Photos of written answers.
Repository link
<img width="872" height="297" alt="Screenshot 2026-09-06 122008" src="https://github.com/user-attachments/assets/5a5624c1-7c9a-4c76-8106-d6a44cc9eb81" />
<img width="845" height="412" alt="Screenshot 2026-09-06 122105" src="https://github.com/user-attachments/assets/43a01bbc-ad02-4797-8c4f-749db65f06eb" />
<img width="545" height="421" alt="Screenshot 2026-09-06 122138" src="https://github.com/user-attachments/assets/a1524b62-2c76-46f5-8e5b-ab3f92ff1494" />
Make sure you have at least 2–3 commits on main.
Choose the latest commit and revert it:
git revert HEAD
(Save the commit message that Git opens)
Run:
git log --oneline
Observe that a new commit was created (the history was not deleted).
write the short answers in your own words in your notebook:
What does git revert do?
How is it different from git reset?
When is git revert safer than git reset?
Submit:

Screenshot of git log --oneline showing the revert commit
Photos of written answers.
Repository link
<img width="830" height="351" alt="Screenshot 2026-09-06 124743" src="https://github.com/user-attachments/assets/d3f30ff2-8b4c-4e0e-b77b-6a7fd6618a26" />
https://github.com/chaudhariprincekumar66-cloud/Assignment_Repo/new/main/Git-GIthub%20Assignment
Goal: Combine reset and revert knowledge and demonstrate safe practices.

Create a small project flow:
Make 3 commits on a file called project.txt.
Use git reset --soft HEAD~1 and then create a new improved commit.
Later, use git revert on one commit and show that history is preserved.
Write short answers in your notebook:
When should you use git reset --soft?
When should you use git reset --hard? (and why be careful)
When should you prefer git revert?
What do HEAD, HEAD~1, and HEAD~2 mean?
Submit:

Screenshot of final git log --oneline
Photos of written answers.
Repository link
<img width="1216" height="351" alt="Screenshot 2026-09-06 155137" src="https://github.com/user-attachments/assets/6a68778f-1548-4a6b-bb61-5c87c7c934e2" />
<img width="1253" height="312" alt="Screenshot 2026-09-06 155156" src="https://github.com/user-attachments/assets/2f826fdc-11a3-489b-aed1-0c6de05a3b22" />

