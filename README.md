# Documentation MVP

A simplified Markdown-based documentation viewer with table of contents navigation.

## Features

- Markdown file rendering with Python-Markdown
- YAML-based table of contents
- Simple web interface for browsing docs
- Markdown linting support
- Configuration via YAML

## Tech Stack

This MVP uses the same core dependencies as the parent repository:

- **Python-Markdown** - For converting Markdown to HTML
- **PyYAML** - For configuration and TOC parsing
- **Flask** - Simple web server
- Markdown extensions:
  - `markdown.extensions.extra` - Meta-extension for additional features
  - `markdown.extensions.meta` - Metadata support
  - `markdown.extensions.toc` - Table of contents generation

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/gitmvp-com/docs-mvp.git
cd docs-mvp
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure the application (optional):

```bash
cp config.sample.yml config.yml
# Edit config.yml with your preferred settings
```

4. Run the development server:

```bash
python app.py
```

5. Open your browser and navigate to:

```
http://localhost:5000
```

## Project Structure

```
docs-mvp/
├── app.py                  # Main Flask application
├── config.sample.yml       # Sample configuration file
├── config.yml             # Your configuration (create from sample)
├── toc.yml                # Table of contents structure
├── requirements.txt       # Python dependencies
├── .editorconfig          # Editor configuration
├── .markdownlint.json     # Markdown linting rules
├── src/                   # Markdown source files
│   └── getting-started.md # Sample documentation
├── templates/             # HTML templates
│   ├── layout.html        # Base template
│   └── page.html          # Page template
└── static/                # Static assets
    └── style.css          # Styles
```

## Writing Documentation

All documentation should be written in Markdown following the basic syntax.

### Supported Markdown Extensions

- **Extra** - Adds support for definition lists, tables, code blocks, etc.
- **Meta** - Read metadata from front-matter sections
- **TOC** - Automatic bookmarks in headings

### Editor Settings

Before editing any Markdown document:

- When the tab key is pressed, insert **4 spaces** instead of a `Tab` character
- Use soft-wrapping to avoid carriage returns inside paragraphs

An `.editorconfig` file is provided for automatic configuration in supported editors.

## Table of Contents

The `toc.yml` file defines the navigation structure. Example:

```yaml
- href: getting-started.md
- topics:
    - href: installation.md
    - href: configuration.md
```

## Configuration

Create a `config.yml` file from `config.sample.yml` and customize:

```yaml
build:
    title: My Documentation
    input-folder: src
    output-folder: build
```

## Contributing

Contributions are welcome! Please ensure your Markdown follows the linting rules defined in `.markdownlint.json`.

## License

MIT License
