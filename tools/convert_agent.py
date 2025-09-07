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

def convert_to_m365_copilot(agent_config: Dict[str, Any]) -> Dict[str, Any]:
    """Convert agent config to Microsoft 365 Copilot declarative agent format."""
    agent = agent_config['agent']
    metadata = agent['metadata']
    core = agent['core']
    platform_config = agent.get('platforms', {}).get('m365_copilot', {})
    capabilities = agent.get('capabilities', {})
    
    # Generate conversation starters from examples or create defaults
    conversation_starters = []
    if 'examples' in agent and agent['examples']:
        for example in agent['examples'][:3]:  # Max 3 starters
            conversation_starters.append({"text": example['input']})
    
    # Add custom conversation starters if provided
    if platform_config.get('conversation_starters'):
        for starter in platform_config['conversation_starters'][:3]:
            conversation_starters.append({"text": starter})
    
    # Default starters if none provided
    if not conversation_starters:
        conversation_starters = [
            {"text": f"How can you help me with {metadata['description'].lower()}?"},
            {"text": "What are your main capabilities?"},
            {"text": "Can you provide an example of how you work?"}
        ]
    
    declarative_agent = {
        "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.0/schema.json",
        "version": "v1.0",
        "name": metadata['name'],
        "description": metadata['description'],
        "instructions": core['system_prompt'],
        "conversation_starters": conversation_starters[:4],  # M365 limit
        "capabilities": {
            "web_search": {
                "enabled": capabilities.get('can_browse_web', False)
            },
            "graph_connectors": {
                "enabled": True,
                "connections": []
            }
        },
        "actions": []
    }
    
    # Add metadata
    if metadata.get('version') or metadata.get('author'):
        declarative_agent["metadata"] = {
            "version": metadata.get('version'),
            "author": metadata.get('author'),
            "tags": metadata.get('tags', [])
        }
    
    return declarative_agent

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

def convert_to_claude_projects(agent_config: Dict[str, Any]) -> Dict[str, Any]:
    """Convert agent config to Claude Projects format."""
    agent = agent_config['agent']
    metadata = agent['metadata']
    core = agent['core']
    platform_config = agent.get('platforms', {}).get('claude_projects', {})
    
    # Build main instructions (similar to ChatGPT but single field)
    instructions = f"You are {metadata['name']}, {metadata['description']}\n\n"
    
    # Add core system prompt
    instructions += f"ROLE AND INSTRUCTIONS:\n{core['system_prompt']}\n\n"
    
    # Add personality if specified
    if 'personality' in core:
        instructions += f"COMMUNICATION STYLE: {core['personality']}\n\n"
    
    # Add expertise areas
    if 'expertise' in core:
        instructions += "AREAS OF EXPERTISE:\n"
        for item in core['expertise']:
            instructions += f"• {item}\n"
        instructions += "\n"
    
    # Add constraints
    if 'constraints' in core:
        instructions += "IMPORTANT CONSTRAINTS:\n"
        for constraint in core['constraints']:
            instructions += f"• {constraint}\n"
        instructions += "\n"
    
    # Add output format if specified
    if 'output_format' in core:
        instructions += f"PREFERRED OUTPUT FORMAT:\n{core['output_format']}\n\n"
    
    # Add platform-specific customizations
    if platform_config.get('custom_instructions'):
        instructions += f"CLAUDE-SPECIFIC GUIDANCE:\n{platform_config['custom_instructions']}\n\n"
    
    # Trim to Claude's character limit (~2000 chars)
    if len(instructions) > 2000:
        instructions = instructions[:1900] + "...\n\n[Instructions truncated due to length limits]"
    
    # Build Claude Projects configuration
    claude_config = {
        "project_name": metadata['name'],
        "project_description": platform_config.get('project_description', metadata['description']),
        "custom_instructions": instructions,
        "conversation_style": platform_config.get('conversation_style', "professional"),
        "knowledge_files": platform_config.get('knowledge_files', []),
        "metadata": {
            "version": metadata['version'],
            "author": metadata.get('author', ''),
            "tags": metadata.get('tags', []),
            "created_date": metadata.get('created_date'),
            "updated_date": metadata.get('updated_date')
        }
    }
    
    return claude_config

def main():
    parser = argparse.ArgumentParser(description='Convert generic agent configs to platform-specific formats')
    parser.add_argument('input_file', help='Input agent configuration file (YAML or JSON)')
    parser.add_argument('--platform', choices=['github-copilot', 'chatgpt', 'claude-projects', 'open-webui', 'vscode-copilot', 'm365-copilot'], 
                       required=True, help='Target platform')
    parser.add_argument('--output', help='Output file (optional)')
    
    args = parser.parse_args()
    
    try:
        agent_config = load_agent_config(args.input_file)
        result = ""
        
        if args.platform == 'github-copilot':
            result = convert_to_github_copilot(agent_config)
            
        elif args.platform == 'chatgpt':
            field1, field2 = convert_to_chatgpt(agent_config)
            result = f"FIELD 1 (About You):\n{field1}\n\nFIELD 2 (Response Style):\n{field2}"
            
        elif args.platform == 'claude-projects':
            result = json.dumps(convert_to_claude_projects(agent_config), indent=2)
            
        elif args.platform == 'open-webui':
            result = json.dumps(convert_to_open_webui(agent_config), indent=2)
            
        elif args.platform == 'vscode-copilot':
            result = convert_to_vscode_copilot(agent_config)
            
        elif args.platform == 'm365-copilot':
            result = json.dumps(convert_to_m365_copilot(agent_config), indent=2)
        
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
