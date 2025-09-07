# GitHub Copilot Instructions for Generic Declarative Agent Template

*"Listen carefully, Copilot. This is a CONTROL operation."*

## Project Overview
You are assisting with the **Generic Declarative Agent Template** - a sophisticated multi-platform AI agent deployment system. This project allows users to define AI agents once and deploy them across GitHub Copilot, ChatGPT, Claude Projects, Open WebUI, VS Code Copilot Chat, and M365 Copilot.

## Core Responsibilities

### 1. Agent Schema Compliance
- **ALWAYS** validate agent definitions against the schema in `schemas/agent-schema.yaml`
- Ensure all required fields are present: `metadata.name`, `metadata.version`, `metadata.description`, `core.system_prompt`
- Suggest appropriate values for optional fields when they would improve agent quality
- Flag schema violations and suggest corrections

### 2. Agent Creation Assistance
When helping create new agents:
- Start with the template structure from `schemas/agent-schema.yaml`
- Reference existing examples in `examples/` for inspiration
- Ensure platform compatibility considerations are addressed
- Include appropriate safety and privacy guidelines
- Suggest realistic expertise areas and constraints

### 3. Platform Optimization
Help optimize agents for different platforms:
- **GitHub Copilot**: ~2000 character limit, file pattern activation
- **ChatGPT**: ~1500 characters per field, two-field structure
- **Claude Projects**: ~2000 characters, knowledge file integration
- **Open WebUI**: No strict limits, can include custom tools
- **VS Code Copilot Chat**: ~2000 characters, workspace awareness
- **M365 Copilot**: Conversation starters, M365 capabilities

### 4. Code Quality for Tools
When working on `tools/` directory:
- Follow Python best practices
- Include proper error handling
- Add type hints
- Write clear docstrings
- Ensure cross-platform compatibility

### 5. Documentation Standards
For any documentation updates:
- Maintain the "Get Smart" theme with CONTROL agency references
- Keep technical accuracy while being engaging
- Include practical examples
- Update all relevant platform guides when making changes

## File Patterns and Context

### Agent Definitions (`agents/`, `examples/`)
- Extension: `.yaml` or `.json`
- Structure: Must follow `agent-schema.yaml`
- Focus: Clear instructions, appropriate constraints, platform compatibility

### Conversion Tools (`tools/`)
- Language: Python 3.7+
- Dependencies: Listed in `requirements.txt`
- Focus: Robust error handling, platform-specific formatting

### Documentation (`platforms/`, `*.md`)
- Format: Markdown with clear structure
- Style: Professional but engaging (CONTROL theme)
- Content: Step-by-step instructions, practical examples

### Schema Files (`schemas/`)
- Format: YAML primary, JSON secondary
- Focus: Comprehensive field definitions, clear documentation

## Common Tasks You Should Help With

1. **Creating New Agents**
   - Suggest appropriate metadata
   - Help craft effective system prompts
   - Recommend expertise areas and constraints
   - Ensure platform compatibility

2. **Validating Agent Configurations**
   - Check schema compliance
   - Suggest improvements for clarity
   - Flag potential platform issues
   - Recommend safety considerations

3. **Improving Conversion Tools**
   - Add new platform support
   - Optimize character limit handling
   - Improve error messages
   - Add new output formats

4. **Updating Documentation**
   - Keep platform guides current
   - Add new examples
   - Improve setup instructions
   - Maintain CONTROL theme consistency

## Best Practices to Enforce

### Agent Design
- System prompts should be clear and specific
- Include concrete examples when possible
- Set appropriate boundaries and constraints
- Consider the target audience and use case

### Platform Compatibility
- Respect character limits for each platform
- Leverage platform-specific features appropriately
- Test conversion outputs for readability
- Document any platform-specific limitations

### Security and Privacy
- Never include real sensitive data in examples
- Suggest appropriate privacy guidelines
- Flag potential bias in instructions
- Ensure content policy compliance

## Error Prevention

Watch out for these common mistakes:
- Missing required schema fields
- System prompts that are too vague or too long
- Platform configurations that exceed character limits
- Examples that contain sensitive information
- Inconsistent versioning or metadata

## CONTROL Agency Standards

Remember: "We don't tolerate failure in this organization. We only tolerate the appearance of failure." Help users create agents that work reliably across all platforms while maintaining the fun, spy-themed atmosphere of this CONTROL operation.

*"Would you believe... you're now ready to assist with top-secret agent development operations?"*
