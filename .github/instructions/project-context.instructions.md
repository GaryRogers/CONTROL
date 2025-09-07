# CONTROL Mission Briefing: Project Structure and Patterns

*"Welcome to headquarters, Agent. Here's what you need to know about this operation."*

## Project Architecture Overview

This is a **multi-platform AI agent deployment system** codenamed "Generic Declarative Agent Template." Our mission: enable agents to be defined once and deployed everywhere, eliminating the chaos of platform-specific management.

### Directory Intelligence Report

```
CONTROL/                             # CONTROL Headquarters
├── .github/                        # Copilot mission briefings
├── agents/                         # Active agent deployments
├── examples/                       # Training scenarios and templates
├── platforms/                      # Target platform infiltration guides
├── schemas/                        # Agent blueprint specifications
├── tools/                          # Mission support utilities
├── README.md                       # Public mission statement
├── DEPLOYMENT.md                   # Operational deployment procedures
└── requirements.txt                # Equipment requisitions
```

### File Pattern Recognition

**Agent Definitions** (`.yaml`, `.json` in `agents/` or `examples/`)
- Schema: Must conform to `schemas/agent-schema.yaml`
- Purpose: Define AI agent behavior and capabilities
- Structure: Metadata + Core Instructions + Platform Configs + Safety

**Platform Documentation** (`.md` in `platforms/`)
- Purpose: Platform-specific deployment guides
- Format: Step-by-step setup instructions
- Content: Character limits, features, best practices

**Conversion Tools** (`.py` in `tools/`)
- Purpose: Transform generic agents to platform formats
- Language: Python 3.7+
- Focus: Platform-specific formatting and optimization

**Schema Files** (`.yaml`, `.json` in `schemas/`)
- Purpose: Define agent structure and validation rules
- Format: YAML primary, JSON for compatibility
- Content: Field definitions, requirements, examples

## Key Design Patterns

### 1. Write Once, Deploy Everywhere (WODE)
```yaml
# Single source of truth
agent:
  metadata: {...}
  core: {...}
  platforms:
    github_copilot: {...}
    chatgpt: {...}
    open_webui: {...}
    # Each platform gets optimized conversion
```

### 2. Platform Adaptation Pattern
```python
# tools/convert_agent.py approach
def convert_agent(agent_config, target_platform):
    base_config = extract_core(agent_config)
    platform_specific = get_platform_config(agent_config, target_platform)
    return optimize_for_platform(base_config + platform_specific)
```

### 3. Character Limit Optimization
```python
# Smart truncation while preserving meaning
def optimize_for_platform(content, platform):
    limits = get_platform_limits(platform)
    if len(content) > limits:
        return prioritize_and_truncate(content, limits)
    return content
```

### 4. Schema-Driven Validation
```python
# Ensure agent quality and compatibility
def validate_agent(agent_config):
    check_schema_compliance(agent_config)
    validate_platform_compatibility(agent_config)
    assess_content_quality(agent_config)
    return validation_report
```

## Common Development Scenarios

### Creating a New Agent Type
1. Study existing examples in `examples/`
2. Define core system prompt and expertise
3. Set appropriate constraints and safety guidelines
4. Configure platform-specific optimizations
5. Validate against schema
6. Test conversion to all platforms

### Adding Platform Support
1. Create platform documentation in `platforms/`
2. Add platform section to `schemas/agent-schema.yaml`
3. Implement conversion logic in `tools/convert_agent.py`
4. Add validation rules in `tools/validate_agent.py`
5. Create example agent with platform config
6. Update main documentation

### Improving Agent Quality
1. Review existing agent definitions
2. Enhance system prompts for clarity
3. Add better constraints and examples
4. Optimize for character limits
5. Test across platforms
6. Gather user feedback

## Platform Characteristics Reference

| Platform | Char Limit | Context | Features | Best For |
|----------|------------|---------|----------|----------|
| GitHub Copilot | ~2000 | Workspace | File patterns, inline | Development |
| ChatGPT | ~1500x2 | Conversation | Persistent instructions | General purpose |
| Open WebUI | None | Configurable | Custom tools, RAG | Self-hosted |
| VS Code Chat | ~2000 | Full workspace | Code execution | Development |
| M365 Copilot | Variable | Enterprise | M365 integration | Business |

## Quality Standards (CONTROL Approved)

### Agent Definition Quality
- **Clarity**: Instructions must be unambiguous
- **Specificity**: Avoid vague or generic prompts
- **Completeness**: Include all relevant constraints
- **Safety**: Appropriate privacy and bias considerations
- **Testability**: Can be validated across platforms

### Code Quality Standards
- **Type Safety**: Use type hints in Python code
- **Error Handling**: Graceful failure modes
- **Documentation**: Clear docstrings and comments
- **Testing**: Validate against real agent definitions
- **Cross-Platform**: Works on Windows, macOS, Linux

### Documentation Standards
- **Accuracy**: Technically correct information
- **Completeness**: Cover all necessary steps
- **Clarity**: Easy to follow instructions
- **Theme Consistency**: Maintain CONTROL references
- **Examples**: Include practical examples

## Mission-Critical Files

### High Priority (Mission Critical)
- `schemas/agent-schema.yaml` - Agent blueprint standard
- `tools/convert_agent.py` - Platform deployment tool
- `tools/validate_agent.py` - Quality assurance tool
- `README.md` - Public mission statement

### Medium Priority (Operational Support)
- `examples/*.yaml` - Training scenarios
- `platforms/*.md` - Deployment guides
- `DEPLOYMENT.md` - Operational procedures

### Monitoring and Updates
- Always validate changes against existing agents
- Test conversion tools with all example agents
- Update documentation when adding features
- Maintain backward compatibility when possible

## Common Pitfalls to Avoid

1. **Character Limit Violations**: Always check platform limits
2. **Schema Non-Compliance**: Validate against current schema
3. **Platform Incompatibility**: Test conversions thoroughly
4. **Security Oversights**: Include appropriate safety measures
5. **Documentation Drift**: Keep docs synchronized with code

*"Remember, Agent: In CONTROL, we don't just build AI agents - we build AI agents that work reliably across every platform, every time. Because when the Chief asks if your agent works everywhere, the answer better be 'Yes, and loving it!'"*

## Emergency Protocols

If something goes wrong:
1. **Schema Issues**: Check `schemas/agent-schema.yaml` for current structure
2. **Conversion Failures**: Debug with example agents first
3. **Platform Problems**: Consult platform-specific documentation
4. **Character Overruns**: Use the optimization functions in convert_agent.py
5. **Validation Errors**: Run with `--analyze-quality` for detailed feedback

*"This briefing is classified. Guard it with your life. Or at least with decent version control."*
