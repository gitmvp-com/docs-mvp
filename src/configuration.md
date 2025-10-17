# Configuration

Learn how to configure the Documentation MVP to suit your needs.

## Configuration Files

The application uses two main YAML configuration files:

1.  **config.yml** - Application settings
2.  **toc.yml** - Table of contents structure

## config.yml

The main configuration file controls various aspects of the documentation system.

### Build Settings

```yaml
build:
    title: Documentation MVP
    input-folder: src
    output-folder: build
    related-title: See Also
```

#### Options:

*   **title** - The name of your documentation site
*   **input-folder** - Directory containing Markdown source files
*   **output-folder** - Directory for generated output (future use)
*   **related-title** - Title for related links sections

### Publish Settings

```yaml
publish:
    url: http://localhost:5000/
    root_path: docs
    skip_edit_links: True
```

#### Options:

*   **url** - Base URL for the documentation site
*   **root_path** - Root path for documentation URLs
*   **skip_edit_links** - Whether to hide edit links

## toc.yml

The table of contents file defines the navigation structure using a hierarchical YAML format.

### Basic Structure

```yaml
# Section Title (comment)
- href: src/getting-started.md
- topics:
    - href: src/installation.md
    - href: src/configuration.md
```

### Nested Topics

You can create multi-level navigation:

```yaml
# Main Section
- href: src/main-section.md
- topics:
    # Subsection
    - href: src/subsection/intro.md
    - topics:
        # Deep topic
        - href: src/subsection/details.md
```

### How It Works

1.  Each `href` defines a documentation page
2.  `topics` contains child pages
3.  Comments (starting with `#`) are ignored but help organize the file
4.  The navigation sidebar reflects this structure

## Editor Configuration

The `.editorconfig` file ensures consistent formatting:

```ini
[*.{md,yml}]
charset = utf-8
indent_style = space
indent_size = 4
insert_final_newline = true
```

Most modern editors automatically recognize this file.

## Markdown Linting

The `.markdownlint.json` file defines linting rules for Markdown files:

*   ATX-style headings (`#` prefix)
*   Asterisk-style unordered lists
*   4-space indentation for nested lists
*   Backtick code fences

## Customizing Styles

Edit `static/style.css` to customize the appearance:

*   Colors and fonts
*   Sidebar width and styling
*   Content area layout
*   Code block themes

## Next Steps

Learn about [Building Apps](building-apps/intro.md) with documentation.
