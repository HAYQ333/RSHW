# Student Assignments Repository

## Overview

Welcome to the Student Assignments Repository!

This repository is intended for collecting, managing, and reviewing students' assignments and practical exercises. Each student is expected to work independently in their own Git branch and submit completed work for review.

## Repository Structure

Each student should maintain their work in a separate branch.

Example branch structure:

```text
main
 ├── student-firstname-lastname
 ├── student-firstname-lastname
 └── student-firstname-lastname
```

If assignments are organized into directories, use a structure similar to:

```text
repository/
├── README.md
├── assignments/
│   ├── assignment-01/
│   ├── assignment-02/
│   └── assignment-03/
└── ...
```

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create Your Personal Branch

Each student must create a separate branch using this naming convention:

```text
student-firstname-lastname
```

Example:

```bash
git switch -c john-smith
```

**Important:** Do not work directly on the `main` branch.

### 3. Complete Your Assignment

- Complete your assignments in your personal branch.
- Follow the specified assignment requirements.
- Keep your work organized and maintain a clear directory structure.
- Do not modify or delete other students' work.
- Avoid committing temporary files, generated files, or unnecessary build artifacts.

### 4. Commit Your Changes

Use clear and meaningful commit messages.

Example:

```bash
git add .
git commit -m "Add assignment 01 solution"
```

### 5. Push Your Branch

Push your branch to the remote repository:

```bash
git push -u origin john-smith
```

Replace `john-smith` with your own branch name.

### 6. Submit Your Work

Once your assignment is completed:

1. Open the repository on GitHub.
2. Navigate to the **Pull requests** tab.
3. Click **New pull request**.
4. Select your personal branch as the source branch.
5. Select `main` as the target branch.
6. Provide a meaningful title and description.
7. Submit the Pull Request for review.

Do not merge your Pull Request unless explicitly instructed.

## Collaboration Guidelines

Please follow these rules throughout the course:

1. **One student – one branch:** Each student must use their own branch.
2. **No direct commits to main:** Submit assignment changes through Pull Requests.
3. **Keep branches up to date:** Synchronize your branch with the latest changes when necessary.
4. **Meaningful commits:** Use descriptive commit messages.
5. **Organized submissions:** Follow the agreed directory and file naming conventions.
6. **Respect others' work:** Do not modify another student's branch or files.
7. **Review before submission:** Ensure that your work is complete and all required files are included.

## Useful Git Commands

| Command | Description |
|---|---|
| `git status` | Check the current working tree status |
| `git branch` | List local branches |
| `git switch -c branch-name` | Create and switch to a new branch |
| `git add .` | Stage changes |
| `git commit -m "message"` | Commit changes |
| `git push -u origin branch-name` | Push a branch to the remote repository |
| `git pull` | Fetch and integrate remote changes |
| `git log --oneline` | View commit history |

## Submission Checklist

Before submitting your Pull Request, verify that:

- [ ] You are working in your personal branch.
- [ ] All required assignment files are included.
- [ ] Your work follows the assignment requirements.
- [ ] Your commits have meaningful messages.
- [ ] Your changes have been pushed to GitHub.
- [ ] Your Pull Request targets the `main` branch.

## Questions and Support

If you encounter any issues with Git, GitHub, repository access, or assignment submissions, contact the instructor for assistance.

**Good luck with your assignments!**
