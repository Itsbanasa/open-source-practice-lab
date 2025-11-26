# Contributing Guide

Welcome! This repository is designed specifically for beginners to practice open-source contributions. Follow this step-by-step guide to make your first contribution.

## Prerequisites

Before you start, make sure you have:

1.  **A GitHub Account**: [Sign up here](https://github.com/join) if you don't have one.
2.  **Git Installed**:
    *   **Windows**: Download and install [Git for Windows](https://gitforwindows.org/).
    *   **Mac**: Run `git --version` in Terminal. If not installed, it will prompt you to install it.
    *   **Linux**: Run `sudo apt install git` (Ubuntu/Debian) or `sudo dnf install git` (Fedora).
3.  **Git Configured**:
    Open your terminal (Command Prompt, PowerShell, or Terminal) and run:
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```

---

## Step-by-Step Contribution Workflow

### Step 1: Fork the Repository
A "fork" is your own copy of this repository on GitHub.
1.  Click the **Fork** button at the top right of this page.
2.  Select your account as the destination.

### Step 2: Clone Your Fork
Now, bring your copy to your local computer.
1.  Go to **your forked repository** on GitHub.
2.  Click the green **Code** button and copy the URL (HTTPS).
3.  Open your terminal and run:
    ```bash
    git clone https://github.com/YOUR-USERNAME/open-source-practice-lab.git
    ```
4.  Enter the folder:
    ```bash
    cd open-source-practice-lab
    ```

### Step 3: Create a New Branch
Always work on a new branch, not `main`. Name it after the issue you are fixing.
```bash
# Example: git checkout -b fix-typo-intro
git checkout -b <your-branch-name>
```

### Step 4: Make Changes
1.  Open the project in your code editor (like VS Code).
2.  Find an issue to work on (look for comments like `# Issue #...` in the code or check the Issues tab on GitHub).
3.  Make your changes to fix the issue.

### Step 5: Test Your Changes
Make sure you didn't break anything!
1.  Install dependencies (if you haven't already):
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the tests:
    ```bash
    pytest
    ```
    *Note: Some tests might fail if you haven't fixed those specific issues yet. That's okay! Focus on the issue you are solving.*

### Step 6: Commit Your Changes
Save your changes with a message explaining what you did.
```bash
git add .
git commit -m "Fix Issue #1: Corrected typo in intro.md"
```

### Step 7: Push to GitHub
Upload your branch to your forked repository.
```bash
git push origin <your-branch-name>
```

### Step 8: Open a Pull Request (PR)
1.  Go to the original repository on GitHub (not your fork).
2.  You should see a yellow banner saying **"Compare & pull request"**. Click it.
3.  If you don't see the banner, go to the **Pull requests** tab and click **New pull request**.
4.  Add a title and description. Mention the issue you fixed (e.g., "Closes #1").
5.  Click **Create pull request**.

---

## Congratulations!
You've just made an open-source contribution. A maintainer will review your code, maybe ask for some changes, and then merge it!
