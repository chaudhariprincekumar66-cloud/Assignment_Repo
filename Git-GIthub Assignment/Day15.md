Create a new file named profile.txt and write 3–4 lines about your favorite programming topic.
Run git status and note that the file is untracked.
Try the command:
git restore profile.txt
Observe that it does not work (because the file is untracked). 4. Stage the file:

git add profile.txt
Unstage it using:
git restore --staged profile.txt
Run git status again and confirm the file is back to untracked / unstaged.
Now stage and commit the file properly:
git add profile.txt
git commit -m "Add profile.txt"
Submit:

Screenshot of git status when the file was untracked
Screenshot after using git restore --staged
Repository link
<img width="1078" height="358" alt="Screenshot 2026-09-03 195916" src="https://github.com/user-attachments/assets/f6bd4ea5-80bb-44d0-8289-8cca39afc518" />
<img width="1052" height="250" alt="Screenshot 2026-09-03 195940" src="https://github.com/user-attachments/assets/01c577da-56ba-484c-90ee-d9bb5720472f" />
<img width="1077" height="305" alt="Screenshot 2026-09-03 200202" src="https://github.com/user-attachments/assets/6b6d7439-821a-413f-a2d5-36fb2d0509c5" />
Create a file named config.env with sample secret data:
DB_PASSWORD=SuperSecretPass999
API_KEY=sk-test-abc123xyz789
Intentionally add and commit it (to practice the fix):
git add config.env
git commit -m "Accidentally commit config.env"
Create a folder named vendor and put any dummy file inside it.

Create a .gitignore file and add:

vendor/
config.env
Stop tracking config.env but keep the file on your computer:
git rm --cached config.env
Run git status and observe that config.env is staged for removal from Git (but the file still exists locally).

Commit the fix:

git add .gitignore
git commit -m "Stop tracking config.env and add .gitignore"
git push origin main
Confirm on GitHub that config.env is no longer visible in the repository, while the file still exists on your local machine.

Create a file named why-gitignore.txt and answer:

Why should we ignore folders like vendor or node_modules?
Why should we ignore files like config.env or .env?
What does git rm --cached do?
Why should we not add .gitignore inside .gitignore?
Submit:

Screenshot of git status after using git rm --cached
Screenshot showing that config.env is ignored / removed from GitHub
Content of why-gitignore.txt
Repository link (make sure config.env is not visible on GitHub)
<img width="1082" height="82" alt="Screenshot 2026-09-03 235734" src="https://github.com/user-attachments/assets/67c613be-a5f2-43d7-ba8b-d5a48f735e71" />
<img width="1108" height="265" alt="Screenshot 2026-09-03 235802" src="https://github.com/user-attachments/assets/fcf8ec26-0331-4aca-94f3-485f56020ce1" />
Make sure profile.txt is committed on main.
Delete the file using normal system command:
rm profile.txt
Run git status and observe the output.
Recover the file using:
git restore profile.txt
Now delete it properly with Git:
git rm profile.txt
Run git status again and observe the difference.
Commit the deletion:
git commit -m "Remove profile.txt using git rm"
Create a short file named delete-difference.txt and write in your own words:
What is the difference between rm and git rm?
When should you use git rm?
Submit:

Screenshots of git status after rm and after git rm
Content of delete-difference.txt
Repository link
<img width="1082" height="82" alt="Screenshot 2026-09-03 235734" src="https://github.com/user-attachments/assets/18393b2d-b2bc-43e4-907f-72fb6c6acdfe" />



