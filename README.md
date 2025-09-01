# Agentic AI System

A modular AI agent system designed for research, content creation, and automated workflows using multiple AI providers.

## Project Structure

```
D:\Agentic-AI>
├── .env                          # Environment variables and API keys
├── .gitignore                    # Git ignore file
├── environment.yaml              # Conda environment configuration
├── README.md                     # This file
└── src/
    ├── agents/
    │   ├── research_agent.py     # Research automation agent
    │   └── __init__.py
    ├── api/
    │   ├── main.py              # API server entry point
    │   └── __init__.py
    ├── core/
    │   ├── config.py            # Configuration management
    │   └── __init__.py
    ├── tests/
    │   ├── test_tools.py        # Unit tests for tools
    │   └── __init__.py
    ├── tools/
    │   ├── web_Search.py        # Web search functionality
    │   └── __init__.py
    └── workflows/
        ├── content_creation.py   # Content generation workflows
        └── __init__.py
```

## Prerequisites

- Python 3.8 or higher
- Conda package manager
- API keys for required services

## Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Agentic-AI
```

### Step 2: Create Conda Environment

```bash
conda env create -f environment.yaml
conda activate agentic
```

### Step 3: Configure Environment Variables

Create a `.env` file in the project root directory with the following structure:

```
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

**Required API Keys:**
- **OPENAI_API_KEY**: Obtain from [OpenAI Platform](https://platform.openai.com/api-keys)
- **ANTHROPIC_API_KEY**: Obtain from [Anthropic Console](https://console.anthropic.com/)
- **TAVILY_API_KEY**: Optional - for enhanced web search capabilities

### Step 4: Verify Installation

```bash
python -c "from src.core.config import settings; print('Configuration loaded successfully')"
```

## Usage

### Starting the API Server

```bash
python src/api/main.py
```

### Running Research Agent

```bash
python src/agents/research_agent.py
```

### Content Creation Workflow

```bash
python src/workflows/content_creation.py
```

## Running Tests

```bash
python -m pytest src/tests/
```

## Configuration

The system uses environment variables for configuration management. All settings are centralized in `src/core/config.py`.

Key configuration options:
- API keys for various AI services
- Project metadata
- Service endpoints

## Modules Overview

### Core (`src/core/`)
- **config.py**: Centralized configuration and environment variable management

### Agents (`src/agents/`)
- **research_agent.py**: Automated research and data gathering agent

### API (`src/api/`)
- **main.py**: REST API server for external integrations

### Tools (`src/tools/`)
- **web_Search.py**: Web search and information retrieval tools

### Workflows (`src/workflows/`)
- **content_creation.py**: Automated content generation pipelines

### Tests (`src/tests/`)
- **test_tools.py**: Unit tests for tool functionality

## Security Considerations

- Never commit the `.env` file to version control
- Store API keys securely
- Rotate API keys regularly
- Use environment-specific configurations for different deployment stages

## Troubleshooting

### Common Issues

**Missing API Keys Error:**
```
ValueError: OPENAI_API_KEY environment variable not set.
```
**Solution:** Ensure your `.env` file exists and contains the required API keys.

**Conda Environment Issues:**
```bash
# Remove and recreate environment
conda env remove -n agentic
conda env create -f environment.yaml
conda activate agentic
```

**Import Errors:**
Ensure you're running commands from the project root directory and the conda environment is activated.

## Development

### Adding New Modules

1. Create new module in appropriate directory under `src/`
2. Add `__init__.py` file if creating a new package
3. Import and configure in relevant workflow files
4. Add corresponding tests in `src/tests/`

### Code Structure Guidelines

- Keep modules focused and single-purpose
- Use the centralized configuration system
- Follow existing import patterns
- Add appropriate error handling

## Support

For technical issues or questions:
1. Check the troubleshooting section above
2. Verify all prerequisites are met
3. Ensure API keys are correctly configured
4. Review error logs for specific issues

## License

This project is proprietary software developed for client use.
