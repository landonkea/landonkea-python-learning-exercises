# RELEASING.md

How releases work in this repo, and the branch convention that leads up to
them. Written down mostly so future-me doesn't have to reconstruct it from
memory in six months.

## Branches

Three long-lived branches, in order:

1. **`dev`**, day-to-day work lands here first. This is where a new
   exercise idea from `FEATURE_IDEAS.md` gets built and poked at.
2. **`staging`**, once something on `dev` feels done, it moves here. This
   is the "about to ship" branch, mostly useful as a checkpoint before it
   hits `main`.
3. **`main`**, the stable branch. Everything here has already gone through
   `dev` and `staging`. Tags for actual releases get cut from here.

`.github/workflows/ai-attribution-check.yml` already runs against all three
(`main`, `master`, `dev`, `staging`), so the workflow was ahead of the docs
explaining why those branches exist. This file is that explanation.

For a repo this size, the per-exercise feature branches (`16-fstrings`,
`17-sorting`, and so on, same pattern as `01-greet` through `15-string-methods`)
still merge into `dev` with a PR the way exercises 1 through 15 merged into
`main`. `dev` -> `staging` -> `main` is a slower-moving, coarser-grained
promotion on top of that, not a replacement for it.

## Tags and channels

One workflow, `.github/workflows/release.yml`, handles both a pre-release
and a stable release, and it decides which one from the tag name alone:

- `v1.0.0` (no hyphen) is a **stable** release.
- `v1.0.0-rc.1` or `v1.0.0-pre.1` (hyphen in the tag) is a **pre-release**.
  GitHub shows these with a "Pre-release" badge and they don't show up as
  the repo's "latest release."

This is a standard semantic-versioning pattern (the same idea as
`1.0.0-beta.1` in npm or `1.0.0rc1` in Python's own versioning), so there
was no reason to invent a different one here.

There's deliberately no second workflow file for pre-releases. A tag push
is a tag push regardless of which branch it was cut from, so the same
`release.yml` handles a `-rc.1` tag off `staging` and a stable tag off
`main` by reading the tag name, not by watching for pushes to a specific
branch. Splitting that into two workflow files would just mean keeping
two copies of the same `gh release create` step in sync.

## Cutting a release

1. Get the code you want to ship onto `main` (via `staging`, via `dev`, as
   above).
2. Tag it and push the tag:
   ```bash
   git tag v1.1.0
   git push origin v1.1.0
   ```
3. `release.yml` picks up the tag push, sees no hyphen, and runs
   `gh release create v1.1.0 --title "v1.1.0 (stable)" --generate-notes`.
   `--generate-notes` builds the release body from merged PRs and commits
   since the previous tag, so there's no changelog to hand-write.

For a pre-release, same steps, just tag from `staging` with a suffix:
```bash
git tag v1.1.0-rc.1
git push origin v1.1.0-rc.1
```
`release.yml` sees the hyphen, adds `--prerelease` to the `gh release
create` call, and the release shows up on GitHub marked as such.

## Why bother with this on a learning repo

Mostly so the release mechanics themselves are one more thing to have
practiced, same reason `07-add-list-tasks.py` through `15_string_methods.py`
exist: better to learn tags, `gh release create`, and a pre-release/stable
split here, on a repo where a mistake costs nothing, than for the first
time on something that matters.
