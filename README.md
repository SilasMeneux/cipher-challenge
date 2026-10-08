# Cipher Challenge

A collaborative repository for solving **cipher challenges**.

The aim is to build a useful collection of scripts, tools, brute-forcers, documentation, and solutions that the team can reuse across different challenges.

## Repository Structure

```text
cipher-challenge/
├── Brute-Forcers/
│   └── Brute-force scripts and automated key/password searchers
│
├── Documentation/
│   └── Notes, cipher explanations, references, and useful information
│
├── General-Scripts/
│   └── Reusable scripts that don't belong to a specific cipher
│
├── Tools/
│   └── Useful utilities for analysing, decoding, encoding, or solving ciphers
│
└── README.md
```

## Languages

**Python is preferred** for most scripts because it is well suited to cryptography, text processing, and rapid development.

Other languages are completely fine when they are better suited to the task.

## Contribution Rules

### 1. Don't push unfinished work

Only push something once it is in a reasonably usable state.

Do not commit:

* Broken or incomplete scripts
* Temporary test files
* Debug output
* Random experiments
* IDE/editor configuration
* Generated files
* Personal notes that aren't useful to the team
* Large unnecessary files

If you're experimenting with something, keep it locally until it is worth sharing.

### 2. Use `.gitignore`

Every contributor should make sure unnecessary files are excluded from Git.

Examples include:

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo
.venv/
venv/
env/

# IDEs
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.temp
*.swp
```

Add project-specific entries when necessary.

**Do not use `.gitignore` to hide files that the project actually needs.**

### 3. Write informative commit messages

Commit messages should explain **what was changed**.

Good:

```text
Add Caesar cipher brute forcer
Add Vigenere frequency analysis tool
Document substitution cipher techniques
Fix XOR decoder key handling
```

Bad:

```text
update
stuff
changes
fix
test
asdf
```

A commit should give someone a reasonable idea of what happened without having to inspect the entire diff.

### 4. Keep scripts organised

Put files in the directory that best describes their purpose.

For example:

```text
Brute-Forcers/
    caesar_brute.py
    substitution_brute.py

Documentation/
    frequency-analysis.md
    vigenere.md

General-Scripts/
    clean-text.py
    character-frequency.py

Tools/
    hex-decoder.py
    xor-tool.py
```

If something doesn't clearly fit anywhere, discuss where it should go rather than creating another random folder.

### 5. Make scripts understandable

Scripts should be reasonably readable and, where useful, include:

* A short description of what they do
* Instructions for running them
* Required arguments
* Dependencies
* Example usage

For example:

```text
Usage:
    python3 xor-tool.py <input> <key>

Example:
    python3 xor-tool.py encrypted.txt SECRET
```

Avoid writing a complicated script that only you can understand.

## Working With Git

Before starting work:

```bash
git pull
```

After completing something useful:

```bash
git add .
git status
git commit -m "Add description of change"
git push
```

Check `git status` before committing to make sure you aren't accidentally adding files that don't belong in the repository.

### Important

**Do not push every small change.**

Work locally and commit when you have completed something meaningful.

A commit should represent a useful piece of work, not every time you save a file.

## Sharing Solutions

When solving a particular challenge, try to preserve anything that could be useful to the rest of the team.

This might include:

* A general-purpose solver
* A brute-forcer
* Frequency-analysis results
* Information about the cipher
* Useful observations
* A documented solution
* A tool that can be reused for similar challenges

Avoid committing challenge-specific junk unless it has some value for future challenges.

## Dependencies

If a Python script requires external packages, document them clearly.

For larger scripts, use a `requirements.txt` file:

```text
package-name
another-package
```

Then dependencies can be installed with:

```bash
pip install -r requirements.txt
```

Do not commit virtual environments or installed packages to the repository.

## General Principle

> **If it isn't finished, useful, or understandable, don't push it.**

The repository should become a useful shared toolkit over time, not a dump of everyone's experiments.
