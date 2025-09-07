# Claude Projects Platform Adapter

*"Would you believe... Claude Projects is like having Agent 99 as your personal research assistant?"*

## Overview
Claude Projects allows you to create dedicated workspaces with custom instructions, knowledge bases, and persistent conversation context. Perfect for specialized agents that need domain-specific knowledge or long-term project continuity.

## Setup Instructions

### Creating a Claude Project
1. **Access Claude.ai**
   - Go to [claude.ai](https://claude.ai)
   - Sign in to your Anthropic account

2. **Create New Project**
   - Click "Create Project" or the "+" button
   - Enter your project name (use your agent's name)
   - Add project description

3. **Add Custom Instructions**
   - In project settings, find "Custom Instructions"
   - Paste your converted agent instructions
   - Save the project

4. **Upload Knowledge Files (Optional)**
   - Add relevant documents, PDFs, or text files
   - Claude will reference these during conversations
   - Maximum file size: 25MB per file

### Claude API Integration
For programmatic access, include custom instructions in your API calls:

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1000,
    system="[Your converted agent instructions here]",
    messages=[{"role": "user", "content": "Hello"}]
)
```

## Template Structure

### Project Configuration
```json
{
  "project_name": "Agent Name",
  "project_description": "Brief description of agent purpose",
  "custom_instructions": "You are [Agent Name]...",
  "conversation_style": "professional",
  "knowledge_files": ["document1.pdf", "reference2.txt"]
}
```

### Custom Instructions Format
```text
You are [AGENT_NAME], [AGENT_DESCRIPTION]

ROLE AND INSTRUCTIONS:
[Main system prompt and detailed instructions]

COMMUNICATION STYLE: [Personality description]

AREAS OF EXPERTISE:
• [Expertise area 1]
• [Expertise area 2]
• [Expertise area 3]

IMPORTANT CONSTRAINTS:
• [Constraint 1]
• [Constraint 2]
• [Constraint 3]

PREFERRED OUTPUT FORMAT:
[Description of preferred response structure]

CLAUDE-SPECIFIC GUIDANCE:
[Any Claude-specific customizations]
```

## Character Limits and Best Practices

### Character Limits
- **Custom Instructions**: ~2,000 characters maximum
- **Project Description**: ~500 characters recommended
- **Knowledge Files**: 25MB per file, unlimited files per project

### Optimization Tips
1. **Prioritize Core Instructions**: Put the most important guidance first
2. **Use Bullet Points**: More efficient than long paragraphs
3. **Leverage Knowledge Files**: Move detailed reference material to uploaded files
4. **Be Specific**: Claude works best with clear, specific instructions
5. **Test Iteratively**: Claude's context window allows for longer conversations to test behavior

### Knowledge File Strategy
- **Reference Documents**: Technical specs, style guides, example outputs
- **Domain Knowledge**: Industry-specific information, terminology
- **Examples**: Sample inputs/outputs, conversation examples
- **Context Materials**: Background information, project history

## Claude-Specific Features

### Conversation Style Options
- **Professional**: Formal, business-appropriate tone
- **Casual**: Relaxed, friendly conversation style  
- **Technical**: Precise, detailed technical communication
- **Creative**: Imaginative, expressive responses
- **Academic**: Scholarly, research-oriented approach

### Best Use Cases for Claude Projects
- **Research Agents**: Leverage Claude's analytical capabilities
- **Writing Assistants**: Benefit from Claude's strong language skills
- **Code Analysis**: Detailed code review and architecture analysis
- **Document Processing**: Work with uploaded reference materials
- **Long-form Content**: Take advantage of Claude's context window

### Integration with CONTROL Agents
```bash
# Convert agent to Claude Projects format
python tools/convert_agent.py agents/my-agent/my-agent.yaml --platform claude-projects

# Save to file for easy project setup
python tools/convert_agent.py agents/my-agent/my-agent.yaml --platform claude-projects --output claude-config.json
```

## Example Workflow

### 1. Agent Conversion
```bash
# Convert your CONTROL agent
python tools/convert_agent.py agents/research-assistant/research-assistant.yaml --platform claude-projects
```

### 2. Project Setup
1. Create new Claude Project
2. Name it after your agent (e.g., "Research Assistant")
3. Paste the converted instructions
4. Upload any relevant knowledge files

### 3. Testing and Refinement
1. Start conversation to test agent behavior
2. Refine instructions based on responses
3. Update project configuration as needed
4. Leverage Claude's long context for complex tasks

## Advanced Configuration

### Multi-Agent Projects
- Create separate projects for different agent specializations
- Use consistent naming conventions
- Cross-reference agents in knowledge files

### Knowledge Base Management
- Organize files by category (reference, examples, templates)
- Keep files updated with latest information
- Use descriptive filenames for easy identification

### Conversation Management
- Use project conversations for ongoing work
- Create new conversations for different topics
- Archive completed conversations for reference

## Troubleshooting

### Common Issues
- **Instructions Too Long**: Prioritize core guidance, move details to knowledge files
- **Inconsistent Behavior**: Make instructions more specific and detailed
- **Knowledge Files Not Referenced**: Explicitly mention files in instructions
- **Context Lost**: Start new conversation if context becomes unclear

### Quality Assurance
- Test agent with various input types
- Verify knowledge file integration
- Check response consistency across conversations
- Validate adherence to constraints and guidelines

*"Remember, Agent 86: Claude Projects is like having your own personal CONTROL laboratory. Use it wisely, and even the Chief will be impressed with your intelligence gathering capabilities!"*

## CONTROL Integration Notes

This platform adapter maintains the fun CONTROL theme while providing serious technical guidance for Claude Projects integration. The format follows our established patterns while highlighting Claude's unique strengths in research, analysis, and knowledge integration.

*"Mission accomplished. Claude Projects integration is now operational and ready for field deployment!"*
