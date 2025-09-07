#!/usr/bin/env python3
"""
Generic Agent Platform Converter

This tool converts generic agent definitions to platform-specific formats.
"""

import yaml
import json
import argparse
import sys
from pathlib import Path
from typing import Dict, Any

def load_agent_config(file_path: str) -> Dict[str, Any]:
    """Load agent configuration from YAML or JSON file."""
    with open(file_path, 'r') as f:
        if file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(f)
        else:
            return json.load(f)

def convert_to_github_copilot(agent_config: Dict[str, Any]) -> str:
    """Convert agent config to GitHub Copilot custom instructions format."""
    agent = agent_config['agent']
    metadata = agent['metadata']
    core = agent['core']
    platform_config = agent.get('platforms', {}).get('github_copilot', {})
    
    instructions = f"{metadata['name']} - {metadata['description']}\n\n"
    instructions += f"ROLE: {core['system_prompt'][:500]}...\n\n"
    
    if 'expertise' in core:
        instructions += "EXPERTISE:\n"
        for item in core['expertise'][:3]:  # Limit for space
            instructions += f"- {item}\n"
        instructions += "\n"
    
    if 'constraints' in core:
        instructions += "CONSTRAINTS:\n"
        for item in core['constraints'][:3]:
            instructions += f"- {item}\n"
        instructions += "\n"
    
    if 'output_format' in core:
        instructions += f"OUTPUT_FORMAT:\n{core['output_format'][:300]}...\n\n"
    
    if platform_config.get('file_patterns'):
        patterns = ', '.join(platform_config['file_patterns'])
        instructions += f"ACTIVATION: This agent activates when working with {patterns}\n"
    
    # Trim to GitHub Copilot's character limit
    return instructions[:1800] + "..." if len(instructions) > 2000 else instructions

def convert_to_chatgpt(agent_config: Dict[str, Any]) -> tuple[str, str]:
    """Convert agent config to ChatGPT custom instructions format."""
    agent = agent_config['agent']
    metadata = agent['metadata']
    core = agent['core']
    
    # Field 1: About you/Context
    field1 = f"I work with {metadata['name']} for {metadata['description']}\n\n"
    if 'expertise' in core:
        field1 += "MY FOCUS AREAS: " + ", ".join(core['expertise'][:5]) + "\n"
    
    # Field 2: Response style
    field2 = f"INSTRUCTIONS:\n{core['system_prompt'][:800]}...\n\n"
    
    if 'constraints' in core:
        field2 += "CONSTRAINTS:\n"
        for constraint in core['constraints'][:3]:
            field2 += f"- {constraint}\n"
        field2 += "\n"
    
    if 'output_format' in core:
        field2 += f"OUTPUT FORMAT:\n{core['output_format'][:400]}...\n"
    
    # Trim to ChatGPT's limits
    field1 = field1[:1400] + "..." if len(field1) > 1500 else field1
    field2 = field2[:1400] + "..." if len(field2) > 1500 else field2
    
    return field1, field2

def convert_to_open_webui(agent_config: Dict[str, Any]) -> Dict[str, Any]:
    """Convert agent config to Open WebUI format."""
    agent = agent_config['agent']
    metadata = agent['metadata']
    core = agent['core']
    platform_config = agent.get('platforms', {}).get('open_webui', {})
    capabilities = agent.get('capabilities', {})
    
    return {
        "name": metadata['name'],
        "description": metadata['description'],
        "system_prompt": core['system_prompt'],
        "model": "default",
        "temperature": 0.7,
        "max_tokens": 2048,
        "tools": platform_config.get('tools', []),
        "capabilities": {
            "file_operations": capabilities.get('can_read_files', False) or capabilities.get('can_write_files', False),
            "code_execution": capabilities.get('can_execute_code', False),
            "web_browsing": capabilities.get('can_browse_web', False)
        },
        "memory": {
            "enabled": True,
            "context_length": 4000
        },
        "metadata": {
            "version": metadata['version'],
            "author": metadata['author'],
            "tags": metadata.get('tags', [])
        }
    }

def convert_to_vscode_copilot(agent_config: Dict[str, Any]) -> str:
    """Convert agent config to VS Code Copilot Chat instructions format."""
    agent = agent_config['agent']
    metadata = agent['metadata']
    core = agent['core']
    platform_config = agent.get('platforms', {}).get('copilot_chat', {})
    
    instructions = f"{metadata['name']} Assistant\n\n"
    instructions += f"ROLE: {metadata['description']}\n\n"
    
    instructions += "WORKSPACE CONTEXT:\n"
    instructions += "You are working in a VS Code workspace with access to:\n"
    instructions += "- Current file content and selection\n"
    instructions += "- Workspace file structure\n"
    instructions += "- Git repository information\n"
    instructions += "- Terminal access\n\n"
    
    instructions += f"INSTRUCTIONS:\n{core['system_prompt'][:1000]}...\n\n"
    
    if 'expertise' in core:
        instructions += "EXPERTISE:\n"
        for item in core['expertise'][:4]:
            instructions += f"- {item}\n"
        instructions += "\n"
    
    if platform_config.get('file_patterns'):
        patterns = ', '.join(platform_config['file_patterns'])
        instructions += f"FILE TYPE ACTIVATION:\nActivate when working with: {patterns}\n\n"
    
    if platform_config.get('slash_commands'):
        instructions += "SLASH COMMANDS:\n"
        for cmd in platform_config['slash_commands']:
            instructions += f"{cmd} - Specialized command for this agent\n"
    
    return instructions

def main():
    parser = argparse.ArgumentParser(description='Convert generic agent configs to platform-specific formats')
    parser.add_argument('input_file', help='Input agent configuration file (YAML or JSON)')
    parser.add_argument('--platform', choices=['github-copilot', 'chatgpt', 'open-webui', 'vscode-copilot'], 
                       required=True, help='Target platform')
    parser.add_argument('--output', help='Output file (optional)')
    
    args = parser.parse_args()
    
    try:
        agent_config = load_agent_config(args.input_file)
        
        if args.platform == 'github-copilot':
            result = convert_to_github_copilot(agent_config)
            
        elif args.platform == 'chatgpt':
            field1, field2 = convert_to_chatgpt(agent_config)
            result = f"FIELD 1 (About You):\n{field1}\n\nFIELD 2 (Response Style):\n{field2}"
            
        elif args.platform == 'open-webui':
            result = json.dumps(convert_to_open_webui(agent_config), indent=2)
            
        elif args.platform == 'vscode-copilot':
            result = convert_to_vscode_copilot(agent_config)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(result)
            print(f"Converted configuration written to {args.output}")
        else:
            print(result)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
