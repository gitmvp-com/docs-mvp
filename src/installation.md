# Installation

Detailed installation instructions for the Documentation MVP.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.8 or higher** - Download from [python.org](https://www.python.org/)
*   **pip** - Python package manager (included with Python)
*   **Git** - Version control system (optional, for cloning)

## Installation Steps

### 1. Clone the Repository

If you have Git installed:

```bash
git clone https://github.com/gitmvp-com/docs-mvp.git
cd docs-mvp
```

Or download the ZIP file from GitHub and extract it.

### 2. Create a Virtual Environment (Recommended)

Create an isolated Python environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This will install:

*   **Flask 3.0.0** - Web framework
*   **Markdown 3.5.1** - Markdown parser
*   **PyYAML 6.0.1** - YAML parser
*   **Werkzeug 3.0.1** - WSGI utilities

### 4. Configure the Application

Copy the sample configuration file:

```bash
cp config.sample.yml config.yml
```

Edit `config.yml` to customize your settings (optional).

### 5. Run the Application

Start the development server:

```bash
python app.py
```

You should see output like:

```
Starting Documentation MVP Server...
Visit http://localhost:5000 to view the documentation
 * Running on http://0.0.0.0:5000
```

### 6. View the Documentation

Open your web browser and navigate to:

```
http://localhost:5000
```

## Troubleshooting

### Port Already in Use

If port 5000 is already in use, you can change it in `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=8080)
```

### Module Not Found Errors

Make sure you've activated your virtual environment and installed all dependencies:

```bash
pip install -r requirements.txt
```

### Permission Errors

On some systems, you may need to use `pip3` and `python3` instead of `pip` and `python`.

## Next Steps

Now that you have the application running, learn about [Configuration](configuration.md) options.
