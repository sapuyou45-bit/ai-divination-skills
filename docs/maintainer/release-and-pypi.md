# Releasing and publishing to PyPI

This project ships a release each time a tag matching `v*` is pushed. The release workflow lives at `.github/workflows/release.yml`.

## What runs automatically on a tag

1. Checkout at the tag.
2. Build sdist + wheel with `python -m build`.
3. Upload both artifacts.
4. Create a GitHub Release named after the tag with auto-generated notes.
5. (Optional, gated) Publish to PyPI when the `PYPI_API_TOKEN` secret is configured — see below.

## Cutting a release

1. Decide the next version per [SemVer](https://semver.org/).
2. Update `pyproject.toml`, `setup.py`, `CHANGELOG.md`, and prepend a `RELEASE_NOTES.md` entry.
3. Open a PR titled `chore: bump version to vX.Y.Z and add release notes`.
4. After merge, locally:
   ```bash
   git checkout main && git pull --ff-only
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```
5. Watch the release workflow at https://github.com/sapuyou45-bit/ai-divination-skills/actions/workflows/release.yml.

## Enabling PyPI publishing

The release workflow has a `pypi-publish` job that runs only when the `PYPI_API_TOKEN` repository secret is set. To enable it once:

1. Generate a PyPI API token scoped to the `ai-divination-skills` project at https://pypi.org/manage/account/token/.
   - First-time release: scope it to "Entire account", run the first release, then rotate to a project-scoped token.
2. Add the token to the repo:
   ```bash
   gh secret set PYPI_API_TOKEN -R sapuyou45-bit/ai-divination-skills
   ```
   Paste the `pypi-AgEIcHl…` value when prompted.
3. Push the next tag (e.g. `v0.5.2`). The `pypi-publish` job will now run after the build job and upload to PyPI.

To publish manually from a clean checkout instead:

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine upload dist/*
```

## Yanking or fixing a bad release

- Delete the GitHub Release and the tag (`git push origin :refs/tags/vX.Y.Z`) if nothing else depends on it yet.
- For PyPI, never delete — use `pip` `yank` via the PyPI web UI to discourage installs without breaking pinned users.
