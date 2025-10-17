# Markdown Syntax

Complete guide to Markdown syntax supported by the Documentation MVP.

## Headings

Use ATX-style headings with `#` symbols:

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

## Emphasis

Create emphasis with asterisks or underscores:

*   _Italic text_ - `_Italic text_` or `*Italic text*`
*   **Bold text** - `**Bold text**` or `__Bold text__`
*   **_Bold and italic_** - `**_Bold and italic_**`

## Lists

### Unordered Lists

Use asterisks, plus signs, or hyphens:

```markdown
*   Item 1
*   Item 2
    *   Nested item
    *   Another nested item
*   Item 3
```

### Ordered Lists

Use numbers followed by periods:

```markdown
1.  First item
2.  Second item
3.  Third item
```

## Links

Create links with square brackets and parentheses:

```markdown
[Link text](https://example.com)
[Link with title](https://example.com "Title")
```

Example: [Documentation MVP](https://github.com/gitmvp-com/docs-mvp)

## Images

Similar to links, but with a leading exclamation mark:

```markdown
![Alt text](image-url.jpg)
![Alt text](image-url.jpg "Image title")
```

## Code

### Inline Code

Use backticks for inline code:

```markdown
Use the `print()` function in Python.
```

Example: Use the `print()` function in Python.

### Code Blocks

Use triple backticks with optional language identifier:

````markdown
```python
def hello():
    print("Hello, World!")
```
````

Supported languages: python, javascript, html, css, bash, yaml, json, and more.

## Tables

Create tables with pipes and hyphens:

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

Example:

| Feature | Status | Notes |
|---------|--------|-------|
| Markdown | ✓ | Fully supported |
| TOC | ✓ | YAML-based |
| Search | ✗ | Coming soon |

## Blockquotes

Use the `>` character:

```markdown
> This is a blockquote.
> It can span multiple lines.
```

Example:

> **Note:** This is an important note about Markdown syntax.

## Horizontal Rules

Create horizontal rules with three or more hyphens, asterisks, or underscores:

```markdown
---
```

---

## Definition Lists

Supported by the `extra` extension:

```markdown
Term 1
:   Definition 1

Term 2
:   Definition 2a
:   Definition 2b
```

## Abbreviations

Define abbreviations:

```markdown
The HTML specification is maintained by the W3C.

*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium
```

## Footnotes

Add footnotes:

```markdown
This is a statement with a footnote[^1].

[^1]: This is the footnote content.
```

## Escaping Characters

Escape special characters with backslashes:

```markdown
\* Not a list item
\# Not a heading
```

## Best Practices

1.  Use consistent heading hierarchy
2.  Add blank lines around blocks
3.  Use 4 spaces for indentation
4.  Prefer ATX-style headings
5.  Use backtick code fences
6.  Include alt text for images
7.  Test your Markdown rendering

## Related Topics

*   [Configuration](../configuration.md)
*   [Building Apps](../building-apps/intro.md)
