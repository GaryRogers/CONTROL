# Generic Declarative Agent Template

A comprehensive template system for creating consistent AI agents that work across multiple platforms including GitHub Copilot, ChatGPT, Open WebUI, and VS Code Copilot Chat.

## 🎯 Overview

This template provides a standardized way to define AI agents that can be deployed across different platforms while maintaining consistency in behavior, expertise, and response quality. Instead of maintaining separate agent definitions for each platform, you define once and deploy everywhere.

## 🏗️ Project Structure

```
generic-declarative-agent/
├── agents/                 # Your custom agent definitions
├── examples/              # Example agent configurations
│   ├── code-reviewer-agent.yaml
│   ├── documentation-writer-agent.yaml
│   ├── project-analyzer-agent.yaml
│   └── fiction-writing-assistant.yaml
├── platforms/             # Platform-specific documentation
│   ├── github-copilot.md
│   ├── chatgpt.md
│   ├── open-webui.md
│   └── vscode-copilot-chat.md
├── schemas/               # Agent definition schemas
│   ├── agent-schema.yaml
│   └── agent-schema.json
├── tools/                 # Utility scripts
│   ├── convert_agent.py
│   └── validate_agent.py
└── README.md
```

## 🚀 Quick Start

### 1. Define Your Agent

Create a new agent configuration file in the `agents/` directory:

```yaml
# agents/my-custom-agent.yaml
agent:
  metadata:
    name: "My Custom Agent"
    version: "1.0.0"
    description: "Brief description of what this agent does"
    author: "Your Name"
    tags: ["tag1", "tag2"]
    
  core:
    system_prompt: |
      You are a helpful AI assistant specialized in [your domain].
      Your role is to [describe the main purpose].
      
      When responding:
      1. [Instruction 1]
      2. [Instruction 2]
      3. [Instruction 3]
      
    personality: "Professional, helpful, and knowledgeable"
    expertise: 
      - "Area 1"
      - "Area 2"
    constraints:
      - "Don't do X"
      - "Always do Y"
      
  platforms:
    github_copilot:
      enabled: true
      custom_instructions: "Platform-specific guidance"
      file_patterns: ["*.js", "*.py"]
    
    chatgpt:
      enabled: true
      custom_instructions: "ChatGPT-specific guidance"
    
    # ... other platforms
```

### 2. Validate Your Agent

```bash
python tools/validate_agent.py agents/my-custom-agent.yaml --check-compatibility --analyze-quality
```

### 3. Deploy to Platforms

#### GitHub Copilot
```bash
python tools/convert_agent.py agents/my-custom-agent.yaml --platform github-copilot
```
Copy the output to your GitHub Copilot Chat instructions in VS Code settings.

#### ChatGPT
```bash
python tools/convert_agent.py agents/my-custom-agent.yaml --platform chatgpt
```
Copy Field 1 and Field 2 to your ChatGPT custom instructions.

#### Open WebUI
```bash
python tools/convert_agent.py agents/my-custom-agent.yaml --platform open-webui --output openwebui-config.json
```
Import the JSON configuration into your Open WebUI workspace.

#### VS Code Copilot Chat
```bash
python tools/convert_agent.py agents/my-custom-agent.yaml --platform vscode-copilot
```
Add the output to your VS Code Copilot Chat instructions setting.

## 📋 Agent Schema Reference

### Required Fields

- **metadata.name**: Agent name
- **metadata.version**: Semantic version (e.g., "1.0.0")
- **metadata.description**: Brief description
- **core.system_prompt**: Main instructions for the agent

### Optional Fields

- **metadata.author**: Creator name
- **metadata.tags**: Array of tags for categorization
- **core.personality**: Agent's communication style
- **core.expertise**: Areas of knowledge
- **core.constraints**: What the agent shouldn't do
- **core.output_format**: Preferred response structure
- **platforms**: Platform-specific configurations
- **capabilities**: What the agent can do
- **examples**: Input/output examples
- **safety**: Safety and privacy guidelines

## 🎨 Example Agents

### Code Reviewer
Specializes in reviewing code for quality, security, and best practices.
- **File**: `examples/code-reviewer-agent.yaml`
- **Use Cases**: Pull request reviews, code quality assessments
- **Platforms**: All platforms supported

### Documentation Writer
Expert in creating clear, comprehensive technical documentation.
- **File**: `examples/documentation-writer-agent.yaml`
- **Use Cases**: README files, API docs, user guides
- **Platforms**: All platforms supported

### Project Analyzer
Analyzes project architecture, dependencies, and structure.
- **File**: `examples/project-analyzer-agent.yaml`
- **Use Cases**: Architecture reviews, dependency audits
- **Platforms**: All platforms supported

### Fiction Writing Assistant
Creative writing specialist for storytelling and narrative craft.
- **File**: `examples/fiction-writing-assistant.yaml`
- **Use Cases**: Novel writing, character development, plot structure
- **Platforms**: All platforms supported

## 🔧 Tools

### Agent Converter (`convert_agent.py`)
Converts generic agent definitions to platform-specific formats.

```bash
# Convert to GitHub Copilot format
python tools/convert_agent.py agents/my-agent.yaml --platform github-copilot

# Convert to ChatGPT format
python tools/convert_agent.py agents/my-agent.yaml --platform chatgpt

# Save to file
python tools/convert_agent.py agents/my-agent.yaml --platform open-webui --output config.json
```

### Agent Validator (`validate_agent.py`)
Validates agent configurations and provides quality feedback.

```bash
# Basic validation
python tools/validate_agent.py agents/my-agent.yaml

# With compatibility and quality checks
python tools/validate_agent.py agents/my-agent.yaml --check-compatibility --analyze-quality

# Strict mode (fails on warnings)
python tools/validate_agent.py agents/my-agent.yaml --strict
```

## 📚 Platform-Specific Guides

### GitHub Copilot
- **Character Limit**: ~2000 characters
- **Context**: Automatic file and workspace context
- **Features**: Inline suggestions, chat integration
- **Setup**: VS Code Settings → GitHub Copilot Chat Instructions

### ChatGPT
- **Character Limit**: ~1500 characters per field
- **Context**: No automatic workspace context
- **Features**: Persistent instructions, custom GPTs
- **Setup**: Settings → Personalization → Custom Instructions

### Open WebUI
- **Character Limit**: No strict limit
- **Context**: Configurable workspace access
- **Features**: Custom tools, model selection, RAG
- **Setup**: Workspace configuration or admin panel

### VS Code Copilot Chat
- **Character Limit**: ~2000 characters
- **Context**: Full workspace awareness
- **Features**: File integration, terminal access
- **Setup**: VS Code Settings → GitHub Copilot Chat Instructions

## 💡 Best Practices

### Agent Design
1. **Be Specific**: Clear, specific instructions work better than vague ones
2. **Include Examples**: Provide concrete examples of expected behavior
3. **Set Boundaries**: Define what the agent should and shouldn't do
4. **Consider Context**: Different platforms have different capabilities
5. **Iterative Improvement**: Start simple and refine based on usage

### Platform Optimization
1. **Respect Limits**: Each platform has character/token limits
2. **Leverage Features**: Use platform-specific capabilities when available
3. **Test Thoroughly**: Validate behavior across all target platforms
4. **Version Control**: Track changes and improvements
5. **Documentation**: Keep platform-specific notes

### Deployment Strategy
1. **Start Small**: Deploy to one platform first, then expand
2. **Monitor Performance**: Track how well agents perform
3. **Gather Feedback**: Get user feedback for improvements
4. **Regular Updates**: Keep agents current with evolving needs
5. **Backup Configs**: Maintain copies of working configurations

## 🔒 Security and Privacy

### Content Policy
- Do not include sensitive information in agent definitions
- Use placeholder examples rather than real data
- Be mindful of potential bias in instructions
- Follow platform-specific content policies

### Privacy Considerations
- Agents should not request sensitive personal information
- Include privacy guidelines in safety sections
- Be transparent about agent capabilities and limitations
- Respect user data and workspace confidentiality

## 🤝 Contributing

### Adding New Platforms
1. Create platform documentation in `platforms/`
2. Add platform-specific fields to the schema
3. Update the converter tool with new platform support
4. Add platform to validation checks
5. Create example configurations

### Improving Examples
1. Test agents thoroughly across platforms
2. Document real-world use cases
3. Include failure modes and edge cases
4. Provide clear setup instructions
5. Maintain version compatibility

### Tools Enhancement
1. Add new validation rules
2. Improve error messages
3. Support additional output formats
4. Add automated testing
5. Enhance documentation

## 📄 License

[Choose appropriate license - MIT, Apache 2.0, etc.]

## 🙋‍♂️ Support

- **Issues**: Report problems via GitHub issues
- **Discussions**: Join community discussions
- **Documentation**: Refer to platform-specific guides
- **Examples**: Check the examples directory for reference

---

**Note**: This template is designed to be flexible and extensible. As new AI platforms emerge or existing ones evolve, the template can be updated to accommodate new features and capabilities.
