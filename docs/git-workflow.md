# Team Git Workflow & Best Practices

This guide outlines the standard Git practices and branching strategy for the **SahkaarX Portfolio** repository.

---

## 1. Branching Strategy

We follow a feature-branch workflow based on `main`:

- `main`: The stable production branch. Directly pushing to `main` is prohibited.
- `feature/<feature-name>`: Dedicated branch for new features, modules, or enhancements.
- `fix/<bug-name>`: Dedicated branch for resolving bugs or issues.
- `docs/<doc-topic>`: Dedicated branch for documentation updates.

### Creating a Feature Branch
Always branch off the latest `main`:
```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
```

---

## 2. Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <short summary>

[optional body explaining rationale]

[optional footer(s)]
```

### Common Types:
- `feat`: A new feature or capability.
- `fix`: A bug fix.
- `docs`: Documentation-only changes.
- `chore`: Maintenance tasks, config, dependency updates.
- `refactor`: Code changes that neither fix a bug nor add a feature.
- `test`: Adding or correcting tests.

### Examples:
- `feat(portfolio): initialize structured directory layout`
- `docs(readme): add setup and git workflow documentation`
- `chore(git): add comprehensive .gitignore file`

---

## 3. Pull Request (PR) Workflow

1. **Commit and Push:** Push your feature branch to the remote:
   ```bash
   git push -u origin feature/your-feature-name
   ```
2. **Open PR:** Navigate to GitHub and open a Pull Request targeting `main`.
3. **Fill PR Template:** Provide a clear summary of changes, rationale, and testing steps.
4. **Code Review:** Require at least one peer review approval.
5. **Merge:** Use "Squash and Merge" or "Rebase and Merge" to keep a clean history.
