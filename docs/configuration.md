---
Tags:     meta
          configuration
Comments: true
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

## Disqus Integration
You can also add a [Disqus]() comment section to individual pages of your site.
You'll need to have already [registered](https://disqus.com/admin/create/) a Disqus site.
If you want to enable a Disqus integration, in the `extra` setion of your mkdocs.yml specify `disqus: <your Disqus site name>` - make sure to replace <your Disqus site name> with the name proceeding `.disqus.com`.

You'll also have to specify `Comments: True` in the metadata for pages you want comments on.
As with adding Tags to the metadata for a page, the metadata *must* be the first component of the document.

### Example: Disqus Integration
```yaml
extra:
    disqus: psinder
```

### Example: Enable Comments 
```markdown
---
Comments: True
---
# Page Title
Page content goes here...
```