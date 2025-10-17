#!/usr/bin/env python3
"""
Documentation MVP - Simple Markdown documentation viewer

A Flask application that renders Markdown files with table of contents navigation.
Based on the OutSystems/docs-odc repository architecture.
"""

import os
import yaml
from flask import Flask, render_template, abort
import markdown
from pathlib import Path

app = Flask(__name__)

# Configuration
CONFIG_FILE = 'config.yml'
TOC_FILE = 'toc.yml'


def load_config():
    """Load configuration from YAML file"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return yaml.safe_load(f)
    # Fallback to sample config
    with open('config.sample.yml', 'r') as f:
        return yaml.safe_load(f)


def load_toc():
    """Load table of contents from YAML file"""
    with open(TOC_FILE, 'r') as f:
        return yaml.safe_load(f)


def parse_toc_structure(toc_data):
    """Parse TOC YAML into a navigable structure"""
    nav_items = []
    
    i = 0
    while i < len(toc_data):
        item = toc_data[i]
        
        if isinstance(item, dict) and 'href' in item:
            nav_item = {
                'href': item['href'],
                'title': get_page_title(item['href']),
                'children': []
            }
            
            # Check if next item is topics
            if i + 1 < len(toc_data) and isinstance(toc_data[i + 1], dict) and 'topics' in toc_data[i + 1]:
                nav_item['children'] = parse_toc_structure(toc_data[i + 1]['topics'])
                i += 1
            
            nav_items.append(nav_item)
        
        i += 1
    
    return nav_items


def get_page_title(file_path):
    """Extract title from markdown file or use filename"""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            if first_line.startswith('#'):
                return first_line.lstrip('#').strip()
    
    # Fallback to filename
    return Path(file_path).stem.replace('-', ' ').title()


def render_markdown(content):
    """Render Markdown content to HTML using the same extensions as parent repo"""
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.meta',
            'markdown.extensions.toc',
        ]
    )
    return md.convert(content)


@app.route('/')
def index():
    """Home page - redirect to first doc"""
    config = load_config()
    toc_data = load_toc()
    navigation = parse_toc_structure(toc_data)
    
    # Get first page
    if navigation:
        first_page = navigation[0]['href']
        return render_page(first_page)
    
    return render_template('layout.html', 
                         title='Documentation',
                         content='<h1>Welcome to Documentation MVP</h1><p>No documentation files found.</p>',
                         navigation=navigation,
                         config=config)


@app.route('/docs/<path:page_path>')
def render_page(page_path):
    """Render a documentation page"""
    config = load_config()
    toc_data = load_toc()
    navigation = parse_toc_structure(toc_data)
    
    # Ensure .md extension
    if not page_path.endswith('.md'):
        page_path += '.md'
    
    # Security: prevent directory traversal
    if '..' in page_path:
        abort(404)
    
    file_path = page_path
    
    if not os.path.exists(file_path):
        abort(404)
    
    # Read and render markdown
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    html_content = render_markdown(content)
    title = get_page_title(file_path)
    
    return render_template('page.html',
                         title=title,
                         content=html_content,
                         navigation=navigation,
                         current_page=page_path,
                         config=config)


@app.template_filter('active_page')
def is_active_page(nav_href, current_page):
    """Check if navigation item is the current page"""
    return nav_href == current_page


if __name__ == '__main__':
    print('Starting Documentation MVP Server...')
    print('Visit http://localhost:5000 to view the documentation')
    app.run(debug=True, host='0.0.0.0', port=5000)
