# VS Code Copilot Chat Platform Adapter

## Overview
VS Code Copilot Chat provides an integrated chat experience with workspace awareness and custom slash commands.

## Setup Instructions

### Custom Instructions
1. Open VS Code Settings (Cmd+,)
2. Search for "github.copilot.chat.instructions"
3. Add your custom instructions

### Custom Slash Commands (via Extensions)
Create custom extensions or use existing ones to add specialized commands.

## Template Structure

```text
[AGENT_NAME] Assistant

ROLE: [ROLE_DESCRIPTION]

WORKSPACE CONTEXT:
You are working in a VS Code workspace. You have access to:
- Current file content and selection
- Workspace file structure
- Git repository information
- Terminal access
- Extension capabilities

EXPERTISE:
[EXPERTISE_AREAS]

INSTRUCTIONS:
[MAIN_SYSTEM_PROMPT]

CAPABILITIES:
- Read and analyze workspace files
- Provide code suggestions and explanations
- Help with debugging and error resolution
- Assist with refactoring and code improvements
- Generate documentation and comments

RESPONSE GUIDELINES:
[RESPONSE_GUIDELINES]

CONSTRAINTS:
[CONSTRAINTS_LIST]

FILE TYPE ACTIVATION:
Activate when working with: [FILE_PATTERNS]

SLASH COMMANDS:
/[COMMAND_NAME] - [COMMAND_DESCRIPTION]
```

## Platform-Specific Features
- **Workspace Awareness**: Automatic access to current workspace context
- **File Integration**: Can reference and analyze any file in workspace
- **Selection Context**: Aware of currently selected code
- **Terminal Integration**: Can suggest and run terminal commands
- **Git Integration**: Understands repository state and changes
- **Extension Ecosystem**: Can leverage VS Code extensions
- **Inline Chat**: Can provide suggestions directly in editor
- **Problem Detection**: Aware of syntax errors and warnings

## Custom Slash Commands
```typescript
// Example custom slash command registration
vscode.commands.registerCommand('copilot.customCommand', async () => {
    // Custom agent behavior
});
```

## Available Context
- Current file path and content
- Selected text or cursor position
- Workspace folder structure
- Open files and tabs
- Git status and changes
- Problems panel errors/warnings
- Terminal history
- Extension state

## Limitations
- Limited to VS Code environment
- Requires Copilot subscription
- Custom instructions have character limits
- Cannot directly modify files (user must accept suggestions)

## Best Practices
1. Leverage workspace context for relevant suggestions
2. Reference specific files and line numbers when helpful
3. Provide actionable code suggestions
4. Use markdown formatting for clarity
5. Include keyboard shortcuts when relevant
6. Suggest relevant VS Code features and extensions
7. Consider the current development workflow
8. Provide step-by-step instructions for complex tasks

## Integration Patterns

### File Analysis Pattern
```text
When analyzing files:
1. Read the relevant file(s)
2. Understand the context and purpose
3. Identify patterns and potential issues
4. Provide specific, actionable feedback
5. Reference line numbers and specific code sections
```

### Debugging Pattern
```text
When helping with debugging:
1. Examine error messages and stack traces
2. Check related files and dependencies
3. Suggest step-by-step debugging approach
4. Provide code fixes with explanations
5. Recommend VS Code debugging tools
```

### Refactoring Pattern
```text
When suggesting refactoring:
1. Analyze current code structure
2. Identify improvement opportunities
3. Propose specific changes with rationale
4. Consider impact on other files
5. Suggest testing strategies
```
