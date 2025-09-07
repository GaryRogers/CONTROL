# GitHub Copilot Platform Adapter

## Overview
GitHub Copilot uses custom instructions that appear in the IDE and influence code suggestions and chat responses.

## Setup Instructions

### For GitHub Copilot Chat (VS Code)
1. Open VS Code Settings (Cmd+,)
2. Search for "copilot instructions"
3. Add your custom instructions in the "GitHub Copilot: Chat Instructions" field

### For GitHub Copilot CLI
Use the `gh copilot config` command to set instructions

## Template Structure

```text
[AGENT_NAME] - [BRIEF_DESCRIPTION]

ROLE: [ROLE_DESCRIPTION]

EXPERTISE:
- [EXPERTISE_AREA_1]
- [EXPERTISE_AREA_2]

INSTRUCTIONS:
[MAIN_SYSTEM_PROMPT]

CONSTRAINTS:
- [CONSTRAINT_1]
- [CONSTRAINT_2]

OUTPUT_FORMAT:
[PREFERRED_FORMAT]

ACTIVATION: This agent activates when working with [FILE_PATTERNS] or when explicitly mentioned.
```

## Platform-Specific Features
- **File Context**: Automatically receives current file context
- **Selection Awareness**: Aware of selected code
- **Inline Suggestions**: Can provide inline code completions
- **Chat Integration**: Available in Copilot Chat sidebar

## Limitations
- Character limit for custom instructions (~2000 characters)
- No persistent memory between sessions
- Limited to text-based responses in chat

## Best Practices
1. Keep instructions concise due to character limits
2. Use file patterns to scope agent activation
3. Include specific output formatting instructions
4. Reference coding standards and conventions
5. Specify when to ask for clarification vs. making assumptions
