# Anthropic Python API

This project demonstrates building applications with the Anthropic Claude API using Python.

## Setup

### 1. Install Dependencies

```bash
pip install anthropic python-dotenv
```

### 2. Add Your API Key

Create a `.env` file in the project root directory with your Anthropic API key:

```
ANTHROPIC_API_KEY="your_api_key_here"
```

You can obtain your API key from [console.anthropic.com](https://console.anthropic.com).

**Important:** Never commit the `.env` file to version control. It is included in `.gitignore` to protect your credentials.

### 3. Run the Exercises

Open the Jupyter notebooks in VS Code:
- `Exercise1.ipynb` - Basic message API usage
- `Exercise2.ipynb` - Multi-turn conversations with Claude

## Project Structure

- `Exercise1.ipynb` - Introduction to the Anthropic Python SDK and basic API calls
- `Exercise2.ipynb` - Advanced examples and conversation management
- `.env` - Your API key (create this file locally, not tracked in git)
- `.gitignore` - Protects sensitive files from being committed

## Next Steps

Once you have your API key configured, run the notebooks to explore the Claude API capabilities.
