# Configuration

## Alternate "Edit on..." Repo Branch
If you'd like the "Edit on..." link in the footer to point to a branch *other* than master, in the `extra` section of your mkdocs.yml specify `repo_branch: branchName`.

###Example: "Edit on..." Dev Branch
```yaml
extra:
    repo_branch: dev
```

## Disable Code Line Wrapping
If you do **not** want code lines to wrap (they do by default), in the `extra` section of your mkdocs.yml specify `nowrap: true`.
This will cause a scroll bar to be added to code blocks which would otherwise wrap.
```yaml
extra:
    nowrap: true
```