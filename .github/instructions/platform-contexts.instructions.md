# Platform-Specific GitHub Copilot Instructions

*"Agent 99, these are your mission parameters for each platform infiltration."*

## When Working with GitHub Copilot Platform Files

### File: `platforms/github-copilot.md`
You are assisting with GitHub Copilot platform documentation. Focus on:
- VS Code settings integration (`Cmd+,` → "copilot instructions")
- Character limit optimization (~2000 characters)
- File pattern activation strategies
- Code suggestion enhancement techniques
- Chat integration best practices

**Key Considerations:**
- GitHub Copilot has excellent workspace context awareness
- File patterns are crucial for scoped agent activation
- Instructions appear in both chat and inline suggestions
- Users primarily work within VS Code environment

### File: `platforms/chatgpt.md`
You are assisting with ChatGPT platform documentation. Focus on:
- Two-field custom instruction format
- Character limits (~1500 per field)
- Persistent conversation context
- Custom GPT configuration options
- Field 1: User context, Field 2: Response instructions

**Key Considerations:**
- No automatic workspace context
- Instructions persist across conversations
- Limited integration with external tools
- Focus on conversational AI assistance

### File: `platforms/claude-projects.md`
You are assisting with Claude Projects platform documentation. Focus on:
- Project-based setup and configuration
- Custom instructions optimization (~2000 characters)
- Knowledge file integration strategies
- Conversation style configuration
- Claude-specific features and capabilities

**Key Considerations:**
- Excellent for research and analysis-focused agents
- Knowledge file integration for domain expertise
- Long context window for complex conversations
- Project-based persistent context
- Strong analytical and reasoning capabilities

### File: `platforms/open-webui.md`
You are assisting with Open WebUI platform documentation. Focus on:
- JSON configuration format
- Custom tool integration
- RAG (Retrieval Augmented Generation) setup
- Model selection strategies
- Workspace configuration options

**Key Considerations:**
- Most flexible platform with fewer limitations
- Supports custom tools and integrations
- Can handle longer, more complex agent definitions
- Often self-hosted with admin configuration options

### File: `platforms/vscode-copilot-chat.md`
You are assisting with VS Code Copilot Chat documentation. Focus on:
- Integration with VS Code workspace
- Slash command customization
- File and terminal access capabilities
- Debugging and code execution context
- Multi-file project understanding

**Key Considerations:**
- Full workspace awareness and file access
- Can execute code and access terminal
- Integrates with VS Code's debugging tools
- Excellent for development-focused agents

### File: `platforms/m365-copilot.md`
You are assisting with Microsoft 365 Copilot documentation. Focus on:
- Conversation starters configuration
- M365 service integration (Teams, Outlook, SharePoint)
- Graph connector capabilities
- Enterprise deployment considerations
- Compliance and security requirements

**Key Considerations:**
- Enterprise-focused with business context
- Integration with Microsoft ecosystem
- Compliance and governance requirements
- Focus on productivity and collaboration scenarios

## Conversion Tool Context

### File: `tools/convert_agent.py`
When working on the conversion tool, focus on:
- Platform-specific formatting logic
- Character limit enforcement
- Template rendering accuracy
- Error handling for malformed inputs
- Output validation

**Platform-Specific Conversion Rules:**
```python
# GitHub Copilot: Compact format with file patterns
def convert_to_github_copilot(agent_config):
    # Prioritize core instructions
    # Include 2-3 top expertise areas
    # Add file patterns if specified
    # Keep under 2000 characters

# ChatGPT: Two-field structure
def convert_to_chatgpt(agent_config):
    # Field 1: User context and domain
    # Field 2: Response style and constraints
    # Each field ~1500 characters max

# Open WebUI: Full JSON structure
def convert_to_open_webui(agent_config):
    # Can include complete agent definition
    # Add tool configurations
    # Include comprehensive examples
```

### File: `tools/validate_agent.py`
When working on the validation tool, focus on:
- Schema compliance checking
- Platform compatibility analysis
- Quality assessment metrics
- Warning and error categorization
- Improvement suggestions

**Validation Priorities:**
1. Required field presence
2. Character limit compliance per platform
3. Schema format validation
4. Content quality assessment
5. Platform-specific requirement checks

## Schema Development Context

### File: `schemas/agent-schema.yaml`
When working on the schema, consider:
- Backward compatibility with existing agents
- Platform capability representation
- Clear field documentation
- Optional vs required field balance
- Future extensibility

**Schema Evolution Guidelines:**
- Add new optional fields for new capabilities
- Maintain required field stability
- Document field purposes clearly
- Consider platform limitations
- Include validation examples

## Example Agent Context

### File: `examples/*.yaml`
When working with example agents, ensure:
- Real-world applicability
- Platform compatibility demonstration
- Quality instruction examples
- Appropriate constraint setting
- Clear metadata documentation

**Example Categories:**
- **Development Agents**: Code review, documentation, analysis
- **Content Agents**: Writing, editing, creative assistance
- **Analysis Agents**: Data analysis, research, planning
- **Specialized Agents**: Domain-specific expertise

## Testing and Quality Assurance

When assisting with testing:
1. **Schema Validation**: Ensure all agents pass validation
2. **Platform Conversion**: Test conversion to all platforms
3. **Character Limits**: Verify platform-specific constraints
4. **Real-World Testing**: Suggest practical testing scenarios
5. **Documentation Updates**: Keep all docs synchronized

*"Remember, in CONTROL we have a saying: 'The only thing better than a good agent is a well-tested agent that works on every platform.' And loving it!"*
