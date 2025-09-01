# Agentic AI System

An enterprise-grade modular AI agent platform that orchestrates multiple AI providers to deliver automated research, content generation, and intelligent workflow execution.

## Overview

This system provides a production-ready framework for building AI-powered automation workflows. It combines the strengths of OpenAI, Anthropic, and web search capabilities to create sophisticated agent behaviors that can operate autonomously or integrate with existing business processes.

## Architecture

```
agentic-ai/
├── .env                          # Environment configuration
├── .gitignore                    # Version control exclusions
├── environment.yaml              # Python dependencies
├── README.md                     # Documentation
└── src/
    ├── agents/                   # AI agent implementations
    │   ├── research_agent.py     # Autonomous research agent
    │   └── __init__.py
    ├── api/                      # REST API layer
    │   ├── main.py              # FastAPI application
    │   └── __init__.py
    ├── core/                     # System configuration
    │   ├── config.py            # Environment management
    │   └── __init__.py
    ├── tests/                    # Test suite
    │   ├── test_tools.py        # Tool validation tests
    │   └── __init__.py
    ├── tools/                    # Utility functions
    │   ├── web_Search.py        # Web search integration
    │   └── __init__.py
    └── workflows/                # Business logic
        ├── content_creation.py   # Content generation pipeline
        └── __init__.py
```

## Quick Start

### Prerequisites

Before installation, ensure you have:
- **Python 3.8+**: Required for modern async/await syntax and type hints
- **Conda**: Package and environment management (recommended over pip for dependency isolation)
- **API Access**: Valid credentials for AI services

### Installation Process

**1. Environment Setup**

Create an isolated Python environment to prevent dependency conflicts:

```bash
conda env create -f environment.yaml
conda activate agentic
```

The conda environment ensures consistent dependency versions across development and production environments.

**2. API Configuration**

Create a `.env` file in the project root. This file stores sensitive credentials outside of your codebase:

```bash
# Required - OpenAI integration
OPENAI_API_KEY=sk-your-openai-key-here

# Required - Anthropic Claude integration  
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here

# Optional - Enhanced web search
TAVILY_API_KEY=tvly-your-tavily-key-here
```

**Why these keys are needed:**
- **OpenAI**: Powers GPT models for text generation and analysis
- **Anthropic**: Provides Claude models for reasoning and safety-focused tasks
- **Tavily**: Enables real-time web search and information retrieval

**3. Verification**

Confirm your setup is working correctly:

```bash
python -c "from src.core.config import settings; print(f'✓ {settings.PROJECT_NAME} v{settings.PROJECT_VERSION} configured')"
```

## System Components

### Research Agent (`src/agents/research_agent.py`)

Autonomous agent that conducts comprehensive research by:
- Formulating search strategies based on input topics
- Gathering information from multiple sources
- Synthesizing findings into structured reports
- Maintaining context across research sessions

**Use Case**: Market research, competitive analysis, technical documentation

### Content Creation Workflow (`src/workflows/content_creation.py`)

End-to-end content generation pipeline that:
- Analyzes content requirements and audience
- Generates drafts using appropriate AI models
- Applies quality checks and refinements
- Outputs publication-ready content

**Use Case**: Blog posts, marketing copy, technical documentation

### Web Search Tools (`src/tools/web_Search.py`)

Real-time information retrieval system that:
- Executes targeted web searches
- Filters and ranks results by relevance
- Extracts key information from web pages
- Handles rate limiting and error recovery

**Use Case**: Current events, market data, factual verification

### API Server (`src/api/main.py`)

RESTful API interface that:
- Exposes agent capabilities as HTTP endpoints
- Handles authentication and request validation
- Manages concurrent agent executions
- Provides webhook support for integrations

**Use Case**: Third-party integrations, microservice architecture

## API Key Setup Guide

### OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign in to your account
3. Navigate to API Keys section
4. Create new secret key
5. Copy the key (starts with `sk-`)
6. Add to your `.env` file

### Anthropic API Key

1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Sign in or create account
3. Go to API Keys section
4. Generate new key
5. Copy the key (starts with `sk-ant-`)
6. Add to your `.env` file

### Tavily API Key (Optional)

1. Visit [Tavily](https://tavily.com/)
2. Sign up for API access
3. Generate API key from dashboard
4. Copy the key (starts with `tvly-`)
5. Add to your `.env` file

## Usage Examples

### Basic Research Workflow

```bash
# Activate environment
conda activate agentic

# Run research agent with topic
python src/agents/research_agent.py
```

### API Server Deployment

```bash
# Start development server
python src/api/main.py

# Server will be available at http://localhost:8000
# API documentation at http://localhost:8000/docs
```

### Content Generation

```bash
# Execute content creation workflow
python src/workflows/content_creation.py
```

## Testing

The test suite validates system functionality and integration points:

```bash
# Run all tests
python -m pytest src/tests/ -v

# Run specific test file
python -m pytest src/tests/test_tools.py -v

# Run with coverage report
python -m pytest src/tests/ --cov=src --cov-report=html
```

## Configuration Management

The system uses a centralized configuration approach through `src/core/config.py`. This design:

- **Prevents credential leakage**: API keys never appear in source code
- **Enables environment-specific configs**: Different settings for dev/staging/production
- **Provides validation**: System fails fast if required credentials are missing
- **Centralizes access**: Single import point for all configuration values

## Deployment Considerations

### Security

- Ensure `.env` file is never committed to version control
- Use environment-specific API keys for different deployment stages
- Implement API key rotation policies
- Monitor API usage and set billing alerts

### Scaling

- The modular architecture supports horizontal scaling
- Each agent can run in separate containers
- API server supports load balancing
- Tools are stateless and thread-safe

### Monitoring

- Implement logging for all agent activities
- Monitor API rate limits and costs
- Track workflow execution times
- Set up alerts for system failures

## Troubleshooting

### Environment Issues

**Problem**: Import errors when running modules
**Solution**: Ensure you're in the project root directory and conda environment is activated

**Problem**: `ValueError: OPENAI_API_KEY environment variable not set`
**Solution**: Verify your `.env` file exists and contains valid API keys

### API Connectivity

**Problem**: API calls failing with authentication errors
**Solution**: Check that API keys are current and have sufficient credits/permissions

**Problem**: Rate limiting errors
**Solution**: Implement exponential backoff or reduce concurrent requests

### Performance

**Problem**: Slow response times
**Solution**: Check network connectivity and API service status

**Problem**: High memory usage
**Solution**: Monitor agent state management and implement cleanup routines

## Support and Maintenance

### Regular Maintenance Tasks

1. **Update Dependencies**: Review and update packages monthly
2. **API Key Rotation**: Rotate keys according to security policies
3. **Log Review**: Monitor system logs for errors or performance issues
4. **Backup Configuration**: Maintain secure backups of configuration files

### Getting Help

For technical support:
1. Check this documentation first
2. Review error logs for specific error messages
3. Verify environment configuration
4. Test individual components in isolation

## Development Guidelines

### Adding New Features

1. Follow the existing module structure
2. Import configuration from `src.core.config`
3. Add appropriate error handling
4. Include unit tests for new functionality
5. Update this documentation

### Code Quality Standards

- Use type hints for all function parameters and return values
- Implement proper error handling with informative messages
- Follow PEP 8 style guidelines
- Add docstrings for all public functions and classes

## Version Information

- **Current Version**: 1.0.0
- **Python Compatibility**: 3.8+
- **Last Updated**: 2025

This system is designed for production use and follows enterprise software development best practices.
