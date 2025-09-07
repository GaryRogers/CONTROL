#!/usr/bin/env python3
"""
Agent Validator

Validates generic agent configurations against the schema.
"""

import yaml
import json
import jsonschema
import argparse
import sys
from pathlib import Path

def load_schema():
    """Load the JSON schema for agent validation."""
    schema_path = Path(__file__).parent.parent / "schemas" / "agent-schema.json"
    with open(schema_path, 'r') as f:
        return json.load(f)

def load_agent_config(file_path: str):
    """Load agent configuration from YAML or JSON file."""
    with open(file_path, 'r') as f:
        if file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(f)
        else:
            return json.load(f)

def validate_agent(agent_config, schema):
    """Validate agent configuration against schema."""
    try:
        jsonschema.validate(agent_config, schema)
        return True, []
    except jsonschema.ValidationError as e:
        return False, [str(e)]
    except jsonschema.SchemaError as e:
        return False, [f"Schema error: {str(e)}"]

def check_platform_compatibility(agent_config):
    """Check platform-specific compatibility issues."""
    warnings = []
    agent = agent_config.get('agent', {})
    
    # Check character limits for different platforms
    core = agent.get('core', {})
    system_prompt = core.get('system_prompt', '')
    
    # GitHub Copilot limits
    if len(system_prompt) > 1500:
        warnings.append("GitHub Copilot: System prompt may be too long (>1500 chars)")
    
    # ChatGPT limits
    if len(system_prompt) > 1200:
        warnings.append("ChatGPT: System prompt may be too long for custom instructions (>1200 chars)")
    
    # Check for required platform configurations
    platforms = agent.get('platforms', {})
    for platform_name, config in platforms.items():
        if config.get('enabled', False):
            if not config.get('custom_instructions'):
                warnings.append(f"{platform_name}: Enabled but no custom_instructions provided")
    
    return warnings

def analyze_agent_quality(agent_config):
    """Analyze agent configuration quality and provide suggestions."""
    suggestions = []
    agent = agent_config.get('agent', {})
    
    # Check metadata completeness
    metadata = agent.get('metadata', {})
    if not metadata.get('author'):
        suggestions.append("Consider adding author information in metadata")
    if not metadata.get('tags'):
        suggestions.append("Consider adding tags for better categorization")
    
    # Check core configuration
    core = agent.get('core', {})
    if not core.get('expertise'):
        suggestions.append("Consider defining expertise areas for better context")
    if not core.get('constraints'):
        suggestions.append("Consider defining constraints to guide agent behavior")
    
    # Check examples
    if not agent.get('examples'):
        suggestions.append("Consider adding examples to demonstrate expected behavior")
    
    # Check safety considerations
    if not agent.get('safety'):
        suggestions.append("Consider adding safety guidelines and considerations")
    
    return suggestions

def main():
    parser = argparse.ArgumentParser(description='Validate generic agent configurations')
    parser.add_argument('input_file', help='Input agent configuration file (YAML or JSON)')
    parser.add_argument('--strict', action='store_true', help='Strict validation mode')
    parser.add_argument('--check-compatibility', action='store_true', help='Check platform compatibility')
    parser.add_argument('--analyze-quality', action='store_true', help='Analyze configuration quality')
    
    args = parser.parse_args()
    
    try:
        # Load schema and agent config
        schema = load_schema()
        agent_config = load_agent_config(args.input_file)
        
        # Validate against schema
        is_valid, errors = validate_agent(agent_config, schema)
        
        print(f"Validating: {args.input_file}")
        print("=" * 50)
        
        if is_valid:
            print("✅ Schema validation: PASSED")
        else:
            print("❌ Schema validation: FAILED")
            for error in errors:
                print(f"  - {error}")
            if args.strict:
                sys.exit(1)
        
        # Platform compatibility check
        if args.check_compatibility or not args.strict:
            warnings = check_platform_compatibility(agent_config)
            if warnings:
                print("\n⚠️  Platform Compatibility Warnings:")
                for warning in warnings:
                    print(f"  - {warning}")
            else:
                print("\n✅ Platform compatibility: OK")
        
        # Quality analysis
        if args.analyze_quality or not args.strict:
            suggestions = analyze_agent_quality(agent_config)
            if suggestions:
                print("\n💡 Quality Suggestions:")
                for suggestion in suggestions:
                    print(f"  - {suggestion}")
            else:
                print("\n✅ Configuration quality: Excellent")
        
        # Summary
        agent = agent_config.get('agent', {})
        metadata = agent.get('metadata', {})
        platforms = agent.get('platforms', {})
        enabled_platforms = [name for name, config in platforms.items() if config.get('enabled', False)]
        
        print(f"\n📊 Summary:")
        print(f"  Agent: {metadata.get('name', 'Unknown')}")
        print(f"  Version: {metadata.get('version', 'Unknown')}")
        print(f"  Enabled Platforms: {', '.join(enabled_platforms) if enabled_platforms else 'None'}")
        
    except FileNotFoundError:
        print(f"Error: File {args.input_file} not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
