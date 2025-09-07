# Agent Development Workflow

*"This is Agent 86 reporting for duty. Here's how we handle agent development in CONTROL."*

## Quick Reference for Agent Creation

### 1. New Agent Checklist
```yaml
agent:
  metadata:
    name: ""                    # Required: Clear, descriptive name
    version: "1.0.0"           # Required: Semantic versioning
    description: ""            # Required: Brief purpose description
    author: ""                 # Your name/organization
    tags: []                   # Categorization tags
    
  core:
    system_prompt: |           # Required: Main instructions
      You are a [role] specialized in [domain].
      Your purpose is to [main objective].
      
      When responding:
      1. [Specific instruction]
      2. [Specific instruction]
      3. [Specific instruction]
      
    personality: ""            # Communication style
    expertise: []              # Areas of knowledge
    constraints: []            # What NOT to do
    output_format: ""          # Preferred response structure
```

### 2. Platform Configuration Template
```yaml
  platforms:
    github_copilot:
      enabled: true
      custom_instructions: "Platform-specific guidance"
      file_patterns: ["*.py", "*.js", "*.md"]
      
    chatgpt:
      enabled: true
      custom_instructions: "ChatGPT-specific adaptations"
      
    open_webui:
      enabled: true
      custom_instructions: "Open WebUI specific features"
      tools: ["web_search", "file_upload"]
      
    copilot_chat:
      enabled: true
      custom_instructions: "VS Code specific context"
      slash_commands: ["/analyze", "/review"]
```

### 3. Quality Validation Commands
```bash
# Basic validation
python tools/validate_agent.py agents/your-agent.yaml

# Full compatibility check
python tools/validate_agent.py agents/your-agent.yaml --check-compatibility --analyze-quality

# Strict mode (fails on warnings)
python tools/validate_agent.py agents/your-agent.yaml --strict
```

### 4. Platform Conversion Quick Reference
```bash
# GitHub Copilot (for VS Code settings)
python tools/convert_agent.py agents/your-agent.yaml --platform github-copilot

# ChatGPT custom instructions
python tools/convert_agent.py agents/your-agent.yaml --platform chatgpt

# Open WebUI JSON configuration
python tools/convert_agent.py agents/your-agent.yaml --platform open-webui --output config.json

# VS Code Copilot Chat
python tools/convert_agent.py agents/your-agent.yaml --platform copilot-chat

# M365 Copilot
python tools/convert_agent.py agents/your-agent.yaml --platform m365-copilot
```

## Common Agent Patterns

### Code-Focused Agents
- Set `file_patterns` for relevant file types
- Include programming language expertise
- Focus on code quality, security, performance
- Examples: Code reviewer, documentation writer, project analyzer

### Content Creation Agents
- Broader platform support (less file-pattern dependent)
- Focus on writing style and audience
- Include creativity and structure guidelines
- Examples: Fiction writing, technical writing, marketing content

### Analysis Agents
- Emphasize analytical thinking and methodology
- Include specific frameworks or approaches
- Focus on structured output formats
- Examples: Business analyst, data scientist, researcher

## Character Limit Management

### GitHub Copilot (~2000 chars)
- Prioritize core instructions
- Use bullet points for constraints
- Include 2-3 key expertise areas
- Use file patterns to scope activation

### ChatGPT (~1500 chars per field)
- Field 1: Context about user and domain
- Field 2: Response style and constraints
- Keep examples very brief
- Focus on personality and approach

### Open WebUI (No strict limit)
- Can include full schema
- Add comprehensive examples
- Include tool configurations
- Most flexible platform

## Testing Your Agents

### 1. Schema Validation
Always run validation before deployment:
```bash
python tools/validate_agent.py agents/your-agent.yaml --check-compatibility
```

### 2. Platform Testing
Convert and test on each target platform:
```bash
# Test GitHub Copilot format
python tools/convert_agent.py agents/your-agent.yaml --platform github-copilot

# Check character count
python tools/convert_agent.py agents/your-agent.yaml --platform github-copilot | wc -c
```

### 3. Real-World Testing
- Deploy to one platform first
- Test with representative tasks
- Gather feedback and iterate
- Expand to other platforms

## Troubleshooting Common Issues

### Agent Not Activating
- Check file patterns match your use case
- Verify platform-specific setup steps
- Ensure instructions are clear and specific

### Responses Too Generic
- Add more specific expertise areas
- Include concrete examples in system prompt
- Refine constraints to focus behavior
- Consider platform-specific customizations

### Character Limit Exceeded
- Prioritize core instructions
- Move detailed examples to constraints
- Use abbreviations where appropriate
- Consider platform-specific versions

## Version Control Best Practices

### Semantic Versioning
- **1.0.0**: Initial stable release
- **1.1.0**: New features or capabilities
- **1.0.1**: Bug fixes or minor improvements
- **2.0.0**: Breaking changes to agent behavior

### Change Documentation
- Update `metadata.updated_date` with changes
- Document significant changes in comments
- Keep backup copies of working versions
- Test thoroughly before version bumps

*"Remember, Agent 86: In CONTROL, we believe in precision, reliability, and just a touch of style. Now get out there and create some world-class AI agents!"*
