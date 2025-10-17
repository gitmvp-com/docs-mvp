# Reference

Complete reference documentation for the Documentation MVP.

## Overview

This reference section provides detailed technical information about the documentation system.

## Topics Covered

*   [Markdown Syntax](markdown-syntax.md) - Complete Markdown syntax guide
*   Configuration options
*   Python-Markdown extensions
*   Template customization
*   Deployment options

## Python-Markdown Extensions

The system uses the following Markdown extensions:

### markdown.extensions.extra

Meta-extension that includes:

*   Abbreviations
*   Attribute lists
*   Definition lists
*   Fenced code blocks
*   Footnotes
*   Tables

### markdown.extensions.meta

Supports metadata in the front-matter section:

```markdown
title: Page Title
author: John Doe
date: 2024-01-15

# Content starts here
```

### markdown.extensions.toc

Generates table of contents and adds automatic bookmarks to headings.

## System Requirements

*   Python 3.8 or higher
*   Flask 3.0.0
*   Markdown 3.5.1
*   PyYAML 6.0.1
*   Modern web browser

## Architecture

The system consists of:

*   **Flask Application** (`app.py`) - Web server and routing
*   **Templates** - Jinja2 HTML templates
*   **Static Assets** - CSS stylesheets
*   **Source Files** - Markdown documentation
*   **Configuration** - YAML config files

## API Reference

### Configuration Functions

*   `load_config()` - Load application configuration
*   `load_toc()` - Load table of contents
*   `parse_toc_structure()` - Parse TOC into navigation

### Rendering Functions

*   `render_markdown()` - Convert Markdown to HTML
*   `get_page_title()` - Extract page title

## Next Steps

Explore the [Markdown Syntax](markdown-syntax.md) guide for detailed information about writing documentation.
