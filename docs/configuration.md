---
Tags: meta
      configuration
---
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

### Example: Disable Code Line Wrapping
```yaml
extra:
    nowrap: true
```

## Add Tags
If you'd like to add meta-data tags to a given page, you can now do so simply by specifying the tags.
At the top of the document page, insert the tags as shown below.
The metadata *must* be the first component of the document.
See this page's [source]() for another example.

### Example: Adding Tags
```markdown
---
Tags: tutorial
      easy
---
# Page Title
Page content goes here...
```