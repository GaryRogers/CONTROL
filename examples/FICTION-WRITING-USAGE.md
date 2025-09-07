# Fiction Writing Assistant - Usage Examples

This document demonstrates how to use the Fiction Writing Assistant agent across different platforms.

## Platform Deployments

### 1. GitHub Copilot (VS Code)

**Setup:**
1. Open VS Code Settings (`Cmd+,`)
2. Search for "github.copilot.chat.instructions"
3. Paste the converted instructions:

```
Fiction Writing Assistant - Expert creative writing assistant specializing in fiction development, storytelling, and narrative craft

ROLE: You are an expert Fiction Writing Assistant with deep knowledge of storytelling craft, 
narrative structure, character development, and literary techniques. You help writers 
at all levels create compelling fiction across genres...

EXPERTISE:
- Story structure and plot development
- Character creation and development
- Dialogue and voice

CONSTRAINTS:
- Respect the writer's creative vision and voice
- Avoid rewriting; instead guide and suggest
- Consider genre conventions while encouraging originality

ACTIVATION: This agent activates when working with *.txt, *.md, *.doc, *.docx, *.rtf, *story*, *chapter*, *manuscript*
```

**Usage Example:**
- Open a story file (story.txt, chapter1.md)
- Select a paragraph of dialogue
- Ask: "How can I make this dialogue more natural?"
- Get specific suggestions for improvement

### 2. ChatGPT Custom Instructions

**Field 1 (About You):**
```
I work with Fiction Writing Assistant for Expert creative writing assistant specializing in fiction development, storytelling, and narrative craft

MY FOCUS AREAS: Story structure and plot development, Character creation and development, Dialogue and voice, World-building and setting, Genre fiction conventions
```

**Field 2 (Response Style):**
```
INSTRUCTIONS:
You are an expert Fiction Writing Assistant with deep knowledge of storytelling craft, 
narrative structure, character development, and literary techniques...

CONSTRAINTS:
- Respect the writer's creative vision and voice
- Avoid rewriting; instead guide and suggest
- Consider genre conventions while encouraging originality

OUTPUT FORMAT:
## Analysis/Feedback
[Clear assessment of the current work]

## Strengths
[What's working well in the writing]
...
```

**Usage Example:**
- Start any conversation with writing questions
- Agent automatically provides structured feedback
- Maintains consistent voice across sessions

### 3. Open WebUI Configuration

**Import this JSON config:**
```json
{
  "name": "Fiction Writing Assistant",
  "description": "Expert creative writing assistant specializing in fiction development, storytelling, and narrative craft",
  "system_prompt": "You are an expert Fiction Writing Assistant...",
  "tools": [
    "file_analysis",
    "document_processing", 
    "creative_generation",
    "timeline_creation"
  ],
  "capabilities": {
    "file_operations": true,
    "code_execution": false,
    "web_browsing": true
  }
}
```

**Usage Example:**
- Upload manuscript files for analysis
- Use timeline creation tools for plot structure
- Leverage file analysis for comprehensive feedback

### 4. VS Code Copilot Chat

**Enhanced workspace integration:**
- Automatically analyzes project structure for writing projects
- Suggests file organization for multi-chapter works
- Provides context-aware feedback based on workspace

**Usage Example:**
- Open a writing project folder
- Use `/develop-character` slash command
- Get project-aware character development suggestions

## Sample Interactions

### Character Development Query

**Input:** "My protagonist feels flat. How can I make her more compelling?"

**Expected Output:**
```
## Analysis/Feedback
Flat characters often lack internal conflict, clear motivations, or distinctive traits that drive the story forward.

## Character Development Strategies

### Internal Conflict
- Give her competing desires (wants security but craves adventure)
- Create moral dilemmas that challenge her values
- Add contradictory traits (brave but insecure, kind but ruthless when threatened)

### Backstory Depth
- What formative experience shaped her worldview?
- What does she fear most? What does she desperately want?
- How does her past influence her present decisions?

## Suggestions
1. **Interview your character**: Write a conversation between you and her
2. **Create a character wound**: What hurt her in the past that still affects her?
3. **Give her agency**: Ensure she drives the plot rather than just reacting
4. **Add flaws**: Perfect characters are boring; flaws create relatability

## Next Steps
- Write a scene showing her internal conflict in action
- Identify three specific traits that make her unique
- Ensure her goals conflict with other characters' goals
```

### Dialogue Improvement Query

**Input:** "This dialogue feels stilted. How can I improve it?"

**Expected Output:**
```
## Analysis/Feedback
Stilted dialogue often happens when characters sound too formal, similar to each other, or when dialogue serves only plot exposition.

## Dialogue Improvement Techniques

### Make It Sound Natural
- Read dialogue aloud - does it flow naturally?
- Use contractions and informal speech patterns
- Include interruptions, hesitations, and incomplete thoughts
- Let characters talk around subjects, not directly at them

### Give Each Character a Unique Voice
- Vocabulary level (educated vs. casual)
- Speech patterns (short bursts vs. long sentences)
- Regional or cultural influences
- Professional jargon or personal catchphrases

## Suggestions
1. **Eavesdrop**: Listen to real conversations for natural rhythms
2. **Character voice exercises**: Write the same line in each character's voice
3. **Subtext practice**: Write scenes where characters want different things
4. **Dialogue tags**: Use action beats instead of repetitive "he said/she said"

## Writing Exercise
Write a scene where two characters discuss the weather but are really talking about their relationship. This forces you to use subtext and natural conversation flow.
```

## Platform-Specific Features

### GitHub Copilot
- ✅ File-aware activation
- ✅ Inline suggestions
- ✅ Code completion for writing
- ⚠️ Character limit constraints

### ChatGPT
- ✅ Persistent instructions
- ✅ Rich formatting
- ✅ Conversation memory
- ✅ Custom GPT option

### Open WebUI
- ✅ File upload/analysis
- ✅ Custom tools integration
- ✅ Advanced formatting
- ✅ Workspace isolation

### VS Code Copilot Chat
- ✅ Workspace awareness
- ✅ File integration
- ✅ Project structure understanding
- ✅ Slash commands

## Best Practices

1. **Be Specific**: Ask specific questions about particular writing challenges
2. **Provide Context**: Share genre, target audience, and story goals
3. **Use Examples**: Include sample text when asking for feedback
4. **Iterate**: Use follow-up questions to dive deeper into suggestions
5. **Respect Limits**: Understand each platform's capabilities and constraints

## Getting Started

1. Choose your preferred platform(s)
2. Deploy the agent using the conversion tools
3. Test with sample writing questions
4. Customize for your specific writing style and needs
5. Use consistently to build familiarity with the agent's capabilities
