# Platform Deployment Guide

This guide provides detailed instructions for deploying your generic agents to each supported platform.

## GitHub Copilot

### Setup Process
1. **Open VS Code Settings**
   - Use `Cmd+,` (macOS) or `Ctrl+,` (Windows/Linux)
   - Or go to Code → Preferences → Settings

2. **Find Copilot Settings**
   - Search for "copilot instructions" in the settings search bar
   - Look for "GitHub Copilot: Chat Instructions"

3. **Add Agent Instructions**
   - Convert your agent using: `python tools/convert_agent.py your-agent.yaml --platform github-copilot`
   - Paste the output into the instructions field
   - Save settings

### Character Limit Considerations
- Maximum ~2000 characters
- Prioritize core instructions
- Use file patterns to scope activation
- Keep examples concise

### Testing
- Open a file matching your agent's file patterns
- Start a chat with GitHub Copilot
- Verify the agent responds according to your instructions

## ChatGPT

### Setup Process
1. **Access Custom Instructions**
   - Click your profile icon in ChatGPT
   - Select "Settings & Beta"
   - Go to "Personalization" section

2. **Configure Instructions**
   - Convert your agent: `python tools/convert_agent.py your-agent.yaml --platform chatgpt`
   - Copy Field 1 content to "What would you like ChatGPT to know about you?"
   - Copy Field 2 content to "How would you like ChatGPT to respond?"

3. **Enable Custom Instructions**
   - Toggle "Custom instructions" to ON
   - Save changes

### Character Limits
- Each field has ~1500 character limit
- Balance context vs. instructions
- Use concise, specific language
- Prioritize most important behaviors

### Testing
- Start a new conversation
- Ask a question relevant to your agent's expertise
- Verify responses follow your defined patterns

## Open WebUI

### Setup Process
1. **Access Admin Panel or Workspace Settings**
   - Log into your Open WebUI instance
   - Navigate to Workspaces or Admin settings

2. **Create New Agent/Workspace**
   - Convert your agent: `python tools/convert_agent.py your-agent.yaml --platform open-webui --output config.json`
   - Import the JSON configuration
   - Or manually enter the settings

3. **Configure Tools and Capabilities**
   - Enable required tools (web search, code execution, etc.)
   - Set model preferences
   - Configure memory settings

### Configuration Options
```json
{
  "name": "Your Agent Name",
  "system_prompt": "Your agent's system prompt",
  "tools": ["web_search", "code_execution"],
  "model": "preferred-model",
  "temperature": 0.7
}
```

### Testing
- Create a new conversation in the workspace
- Test various capabilities (file upload, code execution, etc.)
- Verify tool integrations work as expected

## VS Code Copilot Chat

### Setup Process
1. **Open VS Code Settings**
   - Use `Cmd+,` (macOS) or `Ctrl+,` (Windows/Linux)
   - Search for "github.copilot.chat.instructions"

2. **Add Workspace-Aware Instructions**
   - Convert your agent: `python tools/convert_agent.py your-agent.yaml --platform vscode-copilot`
   - Paste into the GitHub Copilot Chat Instructions field

3. **Optional: Create Custom Extension**
   - For advanced slash commands
   - Use VS Code extension development tools

### Workspace Integration
- Agent automatically receives workspace context
- Can reference specific files and line numbers
- Understands git status and project structure

### Testing
- Open your project workspace
- Start Copilot Chat
- Ask workspace-specific questions
- Verify file and project awareness

## Microsoft 365 Copilot

### Setup Process
1. **Create Declarative Agent JSON**
   - Convert your agent: `python tools/convert_agent.py your-agent.yaml --platform m365-copilot`
   - Save as `declarativeAgent.json`

2. **Deploy via Teams Admin Center**
   - Package as Teams app (optional)
   - Upload to Microsoft 365 Admin Center
   - Configure permissions and scope

3. **Alternative: SharePoint Deployment**
   - Deploy to specific SharePoint sites
   - Configure for document libraries
   - Set up Graph connector permissions

### M365 Integration Features
- **Cross-Application**: Works in Teams, Outlook, Word, Excel, PowerPoint
- **Microsoft Graph**: Access to user's M365 data
- **Conversation Starters**: Pre-defined prompts guide interactions
- **Adaptive Cards**: Rich response formatting
- **Enterprise Security**: Built-in compliance and governance

### Testing
- Test in Teams chat
- Try in Word/Excel integration
- Verify conversation starters work
- Check Microsoft Graph permissions

## Deployment Checklist

### Pre-Deployment
- [ ] Validate agent configuration
- [ ] Test on multiple platforms
- [ ] Verify character limits
- [ ] Check platform-specific features
- [ ] Review safety guidelines

### During Deployment
- [ ] Follow platform-specific setup steps
- [ ] Test basic functionality
- [ ] Verify agent personality and behavior
- [ ] Check capability constraints
- [ ] Document any platform-specific modifications

### Post-Deployment
- [ ] Conduct comprehensive testing
- [ ] Gather user feedback
- [ ] Monitor performance
- [ ] Document issues and solutions
- [ ] Plan improvement iterations

## Troubleshooting

### Common Issues

**Agent not activating:**
- Check character limits
- Verify instructions are saved
- Restart IDE/platform if needed
- Check file pattern matching

**Inconsistent behavior:**
- Review prompt clarity
- Check for conflicting instructions
- Verify platform capabilities
- Test with simpler examples

**Platform-specific problems:**
- Check platform documentation
- Verify feature availability
- Review error messages
- Contact platform support

### Platform-Specific Tips

**GitHub Copilot:**
- Clear instructions work better than complex ones
- File patterns help with context
- Restart VS Code after changes

**ChatGPT:**
- Use both instruction fields effectively
- Test in new conversations
- Consider creating Custom GPTs for complex agents

**Open WebUI:**
- Verify tool permissions
- Check model compatibility
- Test file upload capabilities

**VS Code Copilot Chat:**
- Leverage workspace awareness
- Use specific file references
- Test with different project types
