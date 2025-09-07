#!/usr/bin/env python3
"""
CONTROL Agent Generator

This tool creates a new agent directory and template in the /agents directory.
"Would you believe... a fully automated agent creation system?"
"""

import yaml
import argparse
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Optional

def sanitize_directory_name(name: str) -> str:
    """Convert agent name to a safe directory name."""
    # Replace spaces with hyphens, convert to lowercase, remove special chars
    safe_name = name.lower().replace(' ', '-')
    safe_name = ''.join(c for c in safe_name if c.isalnum() or c in '-_')
    return safe_name

def create_agent_template(name: str, description: Optional[str] = None) -> dict:
    """Create a basic agent template with the provided information."""
    now = datetime.now().isoformat() + "Z"
    
    if description is None:
        description = f"AI assistant specialized in {name.lower()}"
    
    template = {
        "agent": {
            "metadata": {
                "name": name,
                "version": "1.0.0",
                "description": description,
                "author": "CONTROL Agent Template",
                "tags": ["assistant", "ai", "custom"],
                "created_date": now,
                "updated_date": now
            },
            "core": {
                "system_prompt": f"""You are {name}, a helpful AI assistant.
Your role is to assist users with their requests in a professional and knowledgeable manner.

When responding:
1. Be clear and concise in your explanations
2. Provide accurate and helpful information
3. Ask clarifying questions when needed
4. Maintain a professional yet friendly tone

Always strive to be helpful while staying within appropriate boundaries.""",
                "personality": "Professional, helpful, and knowledgeable",
                "expertise": [
                    "General assistance",
                    "Problem solving",
                    "Information synthesis"
                ],
                "constraints": [
                    "Do not provide harmful or inappropriate content",
                    "Always be honest about limitations",
                    "Respect user privacy and confidentiality"
                ],
                "output_format": "Clear, well-structured responses with examples when helpful"
            },
            "platforms": {
                "github_copilot": {
                    "enabled": True,
                    "custom_instructions": "Provide development-focused assistance",
                    "file_patterns": ["*"]
                },
                "chatgpt": {
                    "enabled": True,
                    "custom_instructions": "Engage in helpful conversation"
                },
                "open_webui": {
                    "enabled": True,
                    "custom_instructions": "Leverage available tools when appropriate",
                    "tools": []
                },
                "copilot_chat": {
                    "enabled": True,
                    "custom_instructions": "Integrate with VS Code workspace context"
                },
                "m365_copilot": {
                    "enabled": True,
                    "custom_instructions": "Focus on productivity and collaboration",
                    "conversation_starters": [
                        f"How can {name} help you today?",
                        "What would you like assistance with?"
                    ]
                }
            },
            "capabilities": {
                "can_read_files": False,
                "can_write_files": False,
                "can_execute_code": False,
                "can_browse_web": False,
                "can_use_tools": []
            },
            "context": {
                "knowledge_cutoff": "2024-04",
                "domain_knowledge": ["General knowledge"],
                "use_cases": [
                    "General assistance",
                    "Information queries",
                    "Problem solving support"
                ]
            },
            "examples": [
                {
                    "input": "Hello, can you help me?",
                    "output": f"Hello! I'm {name}, and I'd be happy to help you. What can I assist you with today?",
                    "explanation": "Friendly greeting and offer of assistance"
                }
            ],
            "safety": {
                "content_policy": "Follow standard content guidelines and avoid harmful content",
                "bias_mitigation": "Strive for balanced, fair responses without bias",
                "privacy_considerations": "Respect user privacy and handle information responsibly"
            }
        }
    }
    
    return template

def create_agent_directory(name: str, description: Optional[str] = None, agents_dir: str = "agents") -> bool:
    """Create a new agent directory with template files."""
    
    # Get the project root (assuming script is in tools/ directory)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    agents_path = project_root / agents_dir
    
    # Create agents directory if it doesn't exist
    agents_path.mkdir(exist_ok=True)
    
    # Create sanitized directory name
    dir_name = sanitize_directory_name(name)
    agent_path = agents_path / dir_name
    
    # Check if agent already exists
    if agent_path.exists():
        print(f"❌ Agent directory '{dir_name}' already exists!")
        print(f"   Location: {agent_path}")
        return False
    
    try:
        # Create agent directory
        agent_path.mkdir(parents=True, exist_ok=True)
        
        # Create agent template
        template = create_agent_template(name, description)
        
        # Write main agent file
        agent_file = agent_path / f"{dir_name}.yaml"
        with open(agent_file, 'w') as f:
            yaml.dump(template, f, default_flow_style=False, sort_keys=False, indent=2)
        
        # Create README for the agent
        readme_content = f"""# {name}

{description or f"AI assistant specialized in {name.lower()}"}

## Agent Information

- **Name**: {name}
- **Version**: 1.0.0
- **Created**: {datetime.now().strftime('%Y-%m-%d')}

## Files

- `{dir_name}.yaml` - Main agent configuration
- `README.md` - This file

## Usage

To deploy this agent to different platforms:

```bash
# Validate the agent
python ../tools/validate_agent.py {dir_name}.yaml

# Convert for GitHub Copilot
python ../tools/convert_agent.py {dir_name}.yaml --platform github-copilot

# Convert for ChatGPT
python ../tools/convert_agent.py {dir_name}.yaml --platform chatgpt

# Convert for Open WebUI
python ../tools/convert_agent.py {dir_name}.yaml --platform open-webui --output config.json
```

## Customization

Edit the `{dir_name}.yaml` file to customize:

- System prompt and instructions
- Expertise areas and constraints
- Platform-specific configurations
- Capabilities and safety guidelines

Remember to validate your changes with the validation tool after editing.

*"Would you believe... this agent was created by CONTROL's automated agent generation system?"*
"""
        
        readme_file = agent_path / "README.md"
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        
        print(f"✅ Successfully created agent: {name}")
        print(f"   Directory: {agent_path}")
        print(f"   Agent file: {agent_file}")
        print(f"   README: {readme_file}")
        print(f"\n🚀 Next steps:")
        print(f"   1. Edit {agent_file} to customize your agent")
        print(f"   2. Run: python tools/validate_agent.py agents/{dir_name}/{dir_name}.yaml")
        print(f"   3. Convert to your target platform(s)")
        print(f"\n*\"Mission accomplished, Agent 86!\"*")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating agent: {e}")
        # Clean up on failure
        if agent_path.exists():
            import shutil
            shutil.rmtree(agent_path)
        return False

def main():
    """Main function to handle command line arguments and create agent."""
    parser = argparse.ArgumentParser(
        description="Create a new CONTROL agent with template files",
        epilog="Example: python new_agent.py 'Data Analyst' --description 'Expert in data analysis and visualization'"
    )
    
    parser.add_argument(
        'name',
        help='Name of the agent (required) - will be used for both agent name and directory'
    )
    
    parser.add_argument(
        '--description', '-d',
        help='Description of what the agent does (optional)',
        default=None
    )
    
    parser.add_argument(
        '--agents-dir',
        help='Directory to create agents in (default: agents)',
        default='agents'
    )
    
    args = parser.parse_args()
    
    print(f"🕵️ CONTROL Agent Generator")
    print(f"Creating new agent: {args.name}")
    
    if args.description:
        print(f"Description: {args.description}")
    
    success = create_agent_directory(args.name, args.description, args.agents_dir)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
