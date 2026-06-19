import os

def push_to_github():
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'auto ai app'")
    os.system("git branch -M main")
    os.system("git remote add origin https://github.com/YOUR_NAME/ai-factory.git")
    os.system("git push -u origin main")
