Create 2–3 commits on any file (for example index.html or notes.txt).
Using git log --oneline, note the commit hash of the latest commit.
Revert the latest commit:
git revert HEAD
(or use the commit hash)
Run git log --oneline and observe the new revert commit.
Submit:

Screenshot of git log --oneline before revert
Screenshot of git log --oneline after revert
Repository link
<img width="951" height="290" alt="Screenshot 2026-09-06 164052" src="https://github.com/user-attachments/assets/885a062b-c293-4bff-9734-68655afbafec" />
<img width="667" height="917" alt="image" src="https://github.com/user-attachments/assets/272ee754-68d8-4568-9016-907db3f9399c" />
Create a commit that adds a new file.
Make one more commit after that.
Try to revert the commit that added the file.
A Modify/Delete conflict should appear.
Resolve it (either delete the file or keep it with required content).
Use:
git add .
git revert --continue
Submit:

Screenshot of the conflict (VS Code or terminal)
Screenshot after successful git revert --continue
Repository link
<img width="1657" height="905" alt="Screenshot 2026-09-11 173525" src="https://github.com/user-attachments/assets/871300dd-9738-4e83-aed1-bfc245ba5d44" />
<img width="672" height="380" alt="image" src="https://github.com/user-attachments/assets/76f39009-c60a-41f4-b89b-0a86285520a1" />
Demonstrate any two of the following commands with a real commit:
git revert --no-edit <commit_id>
git revert --no-commit <commit_id>
git revert --abort
Take screenshots of the commands and their results.
Theoretical Part (Write in Notebook)
Write short and correct answers for the following:

What does git revert do?
Why is git revert safer than git reset on a shared branch?
What is a Modify/Delete conflict? When can it occur during revert?
What is the difference between git revert --abort and git revert --quit?
Write one major difference each between:
git restore
git reset
git revert
Submit:

Screenshots of the two practical commands you tried
Clear photos of the written answers from your notebook
Repository link
<img width="1405" height="360" alt="Screenshot 2026-09-11 213103" src="https://github.com/user-attachments/assets/c66fe4f2-d503-4638-9200-fb36ab8401b2" />
<img width="1801" height="881" alt="image" src="https://github.com/user-attachments/assets/8fe57c42-b8c5-4dd8-8e22-1cb931f3b7ee" />
<img width="1467" height="272" alt="image" src="https://github.com/user-attachments/assets/91b1ee80-b8cf-4c52-960c-0297d4e51103" />
<img width="1371" height="197" alt="image" src="https://github.com/user-attachments/assets/ddc7878c-ba9d-4750-bc58-a99cf8a9d623" />
<img width="1395" height="177" alt="image" src="https://github.com/user-attachments/assets/fc20085d-ef04-47d3-9cb5-07a0dd4d154c" />





