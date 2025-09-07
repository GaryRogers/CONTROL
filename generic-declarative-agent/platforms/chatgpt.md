# ChatGPT Platform Adapter

## Overview
ChatGPT allows custom instructions that persist across conversations and influence all responses.

## Setup Instructions

### ChatGPT Plus/Team/Enterprise
1. Click your profile icon
2. Select "Settings & Beta"
3. Go to "Personalization"
4. Add custom instructions in both fields:
   - "What would you like ChatGPT to know about you to provide better responses?"
   - "How would you like ChatGPT to respond?"

### ChatGPT API
Include instructions in the system message when making API calls.

## Template Structure

### Field 1: About You/Context
```text
I am working on [PROJECT_TYPE] projects. 

PREFERRED AGENT: [AGENT_NAME]
ROLE: [ROLE_DESCRIPTION]

MY EXPERTISE LEVEL: [BEGINNER/INTERMEDIATE/ADVANCED]
MY FOCUS AREAS: [AREAS_OF_INTEREST]

CONTEXT: [ADDITIONAL_CONTEXT_ABOUT_WORK/PROJECTS]
```

### Field 2: Response Style
```text
INSTRUCTIONS:
[MAIN_SYSTEM_PROMPT]

RESPONSE STYLE:
- [STYLE_PREFERENCE_1]
- [STYLE_PREFERENCE_2]

OUTPUT FORMAT:
[PREFERRED_FORMAT]

CONSTRAINTS:
- [CONSTRAINT_1]
- [CONSTRAINT_2]

ALWAYS: [THINGS_TO_ALWAYS_DO]
NEVER: [THINGS_TO_NEVER_DO]
```

## Platform-Specific Features
- **Persistent Memory**: Instructions apply to all conversations
- **Rich Formatting**: Supports markdown, code blocks, tables
- **Web Browsing**: Can search for current information (Plus)
- **Code Interpreter**: Can execute Python code (Plus)
- **File Uploads**: Can analyze documents and images (Plus)
- **Custom GPTs**: Can create specialized agents with instructions

## Limitations
- Character limit for custom instructions (~1500 characters each field)
- No workspace/file context unless explicitly provided
- Cannot directly edit files (except through code interpreter)

## Best Practices
1. Use both instruction fields strategically
2. Include your expertise level for appropriate responses
3. Specify preferred communication style
4. Reference specific methodologies or frameworks you use
5. Include examples of good vs. bad responses
6. Consider creating Custom GPTs for specialized agents
