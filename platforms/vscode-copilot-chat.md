# Microsoft 365 Copilot Declarative Agent Platform Adapter

## Overview
Microsoft 365 Copilot supports declarative agents that can be deployed across the M365 ecosystem including Teams, Outlook, Word, Excel, PowerPoint, and other Microsoft applications.

## Setup Instructions

### Creating a Declarative Agent
1. Create a declarativeAgent.json file with your agent configuration
2. Deploy through Microsoft Teams Admin Center or App Studio
3. Register with Microsoft 365 Developer Portal
4. Configure permissions and capabilities

### Deployment Options
- **Teams App Package**: Include in a Teams app manifest
- **SharePoint**: Deploy to SharePoint sites
- **Microsoft 365 Admin Center**: Organization-wide deployment

## Template Structure

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.0/schema.json",
  "version": "v1.0",
  "name": "[AGENT_NAME]",
  "description": "[AGENT_DESCRIPTION]",
  "instructions": "[DETAILED_INSTRUCTIONS]",
  "conversation_starters": [
    {
      "text": "[STARTER_PROMPT_1]"
    },
    {
      "text": "[STARTER_PROMPT_2]"
    }
  ],
  "capabilities": {
    "web_search": {
      "enabled": true
    },
    "graph_connectors": {
      "enabled": true,
      "connections": []
    }
  },
  "actions": []
}
```

## Microsoft 365 Integration Points
- **Teams**: Chat interface and meeting integration
- **Outlook**: Email composition and calendar assistance  
- **Word**: Document creation and editing support
- **Excel**: Data analysis and formula assistance
- **PowerPoint**: Presentation creation and design
- **SharePoint**: Content management and search
- **OneDrive**: File organization and sharing

## Platform-Specific Features
- **Microsoft Graph Integration**: Access to user's M365 data and services
- **Cross-Application**: Works across all M365 applications
- **Conversation Starters**: Pre-defined prompts to guide user interactions
- **Graph Connectors**: Connect to external data sources
- **Actions**: Custom functions and API integrations
- **Adaptive Cards**: Rich UI components for responses
- **Enterprise Security**: Built-in compliance and security features

## Available Capabilities
```json
"capabilities": {
  "web_search": {
    "enabled": true
  },
  "graph_connectors": {
    "enabled": true,
    "connections": [
      {
        "connection_id": "external-data-source",
        "description": "Custom data connector"
      }
    ]
  }
}
```

## Custom Actions
```json
"actions": [
  {
    "id": "custom_action_1",
    "description": "Custom function description",
    "parameters": {
      "type": "object",
      "properties": {
        "param1": {
          "type": "string",
          "description": "Parameter description"
        }
      }
    }
  }
]
```

## Limitations
- Requires Microsoft 365 licensing
- Must be deployed through official channels
- Subject to Microsoft's app validation process
- Limited to Microsoft Graph API capabilities
- Requires appropriate permissions for data access

## Best Practices
1. Design for cross-application usage
2. Provide clear conversation starters
3. Leverage Microsoft Graph for data integration
4. Follow Microsoft's security and compliance guidelines
5. Test across different M365 applications
6. Use Adaptive Cards for rich responses
7. Implement proper error handling
8. Consider offline scenarios

## Deployment Checklist

### Pre-Deployment
- [ ] Create declarativeAgent.json file
- [ ] Validate JSON schema
- [ ] Test conversation starters
- [ ] Verify capabilities configuration
- [ ] Review security requirements

### Deployment Process  
- [ ] Package as Teams app (if applicable)
- [ ] Submit for app validation
- [ ] Configure admin consent
- [ ] Deploy to target audience
- [ ] Monitor usage and feedback

### Post-Deployment
- [ ] Monitor performance metrics
- [ ] Gather user feedback
- [ ] Update conversation starters based on usage
- [ ] Optimize instructions for better responses
- [ ] Plan feature enhancements
