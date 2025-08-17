#!/usr/bin/env python3
"""
Session Generator Script
Generates new session files from the template based on Session 4 structure.

Usage:
    python scripts/generate_session.py --config configs/session_05_config.json
    python scripts/generate_session.py --interactive
"""

import argparse
import json
import os
import sys
from pathlib import Path
import re

def load_template():
    """Load the session template."""
    template_path = Path("docs/templates/session-template.md")
    if not template_path.exists():
        raise FileNotFoundError(f"Template file not found: {template_path}")
    
    with open(template_path, 'r') as f:
        return f.read()

def load_config(config_file):
    """Load configuration from JSON file."""
    with open(config_file, 'r') as f:
        return json.load(f)

def interactive_config():
    """Collect configuration interactively from user."""
    print("=== Session Generator - Interactive Mode ===\n")
    
    config = {}
    
    # Basic session info
    config['SESSION_NUMBER'] = input("Session number (e.g., 5): ")
    config['SESSION_TITLE'] = input("Session title: ")
    config['WEEK_NUMBER'] = input("Week number: ")
    config['ELEMENT_CODE'] = input("Element code (e.g., ICTPRG430 Element 2.2): ")
    config['DURATION'] = input("Duration in hours (e.g., 4): ")
    config['PHASE_NAME'] = input("Phase name: ")
    
    # Session description
    config['SESSION_DESCRIPTION'] = input("Session description (what students will do): ")
    config['SESSION_COMPONENTS'] = input("Session components summary: ")
    config['SESSION_OVERVIEW'] = input("Session overview paragraph: ")
    
    # Learning objectives
    print("\nEnter 5 learning objectives:")
    for i in range(1, 6):
        config[f'OBJECTIVE_{i}'] = input(f"Objective {i}: ")
    
    # Session structure components
    print("\nEnter 5 session structure components:")
    for i in range(1, 6):
        config[f'COMPONENT_{i}_NAME'] = input(f"Component {i} name: ")
        config[f'COMPONENT_{i}_DESCRIPTION'] = input(f"Component {i} description: ")
    
    # Navigation
    prev_session = int(config['SESSION_NUMBER']) - 1
    next_session = int(config['SESSION_NUMBER']) + 1
    config['PREV_SESSION_NUMBER'] = f"{prev_session:02d}"
    config['NEXT_SESSION_NUMBER'] = f"{next_session:02d}"
    config['PREV_WEEK'] = str(int(config['WEEK_NUMBER']) - 1)
    config['NEXT_WEEK'] = str(int(config['WEEK_NUMBER']) + 1)
    
    return config

def replace_placeholders(template, config):
    """Replace all placeholders in template with values from config."""
    result = template
    
    for key, value in config.items():
        placeholder = f"{{{{{key}}}}}"
        result = result.replace(placeholder, str(value))
    
    return result

def generate_navigation_config(session_num, session_title, components):
    """Generate navigation configuration for mkdocs.yml."""
    session_file = f"sessions/session-{session_num:02d}.md"
    
    nav_config = f"""  - Week {session_num} - {session_title}:
    - Session {session_num}: {session_file}"""
    
    for i, (name, _) in enumerate(components, 1):
        anchor = name.lower().replace(' ', '-').replace(':', '').replace('&', '').replace(',', '')
        anchor = re.sub(r'[^\w-]', '', anchor)  # Remove special characters
        nav_config += f"\n    - {name}: '{session_file[:-3]}/#{anchor}'"
    
    nav_config += f"\n    - Resources: downloads.md\n    - Assessment: assessment.md"
    
    return nav_config

def create_config_template(session_num):
    """Create a configuration template file for a session."""
    config_template = {
        "SESSION_NUMBER": str(session_num),
        "SESSION_TITLE": "Your Session Title Here",
        "WEEK_NUMBER": str(session_num),
        "ELEMENT_CODE": "ICTPRG430 Element X.X",
        "DURATION": "4",
        "PHASE_NAME": "Phase Name",
        "SESSION_DESCRIPTION": "describe what students will learn and do",
        "SESSION_COMPONENTS": "theory, hands-on exercises, and practical applications",
        "SESSION_OVERVIEW": "Detailed overview paragraph goes here.",
        
        # Learning objectives
        "OBJECTIVE_1": "First learning objective",
        "OBJECTIVE_2": "Second learning objective", 
        "OBJECTIVE_3": "Third learning objective",
        "OBJECTIVE_4": "Fourth learning objective",
        "OBJECTIVE_5": "Fifth learning objective",
        
        # Session structure
        "COMPONENT_1_NAME": "Theory Session",
        "COMPONENT_1_DESCRIPTION": "Core theoretical concepts",
        "COMPONENT_2_NAME": "Hands-on Exercise",
        "COMPONENT_2_DESCRIPTION": "Practical implementation",
        "COMPONENT_3_NAME": "Live Demonstration", 
        "COMPONENT_3_DESCRIPTION": "Instructor demonstration",
        "COMPONENT_4_NAME": "Extension Activity",
        "COMPONENT_4_DESCRIPTION": "Advanced concepts",
        "COMPONENT_5_NAME": "Lab Setup",
        "COMPONENT_5_DESCRIPTION": "Environment configuration",
        
        # Content sections
        "SECTION_1_TITLE": "Main Concept Introduction",
        "SECTION_1_CONTENT": "Content for first major section",
        "SECTION_2_TITLE": "Advanced Topics", 
        "SECTION_2_CONTENT": "Content for second major section",
        "SECTION_3_TITLE": "Practical Applications",
        "SECTION_3_CONTENT": "Content for third section",
        "SECTION_4_TITLE": "Implementation Details",
        "SECTION_4_CONTENT": "Content for fourth section",
        "SECTION_5_TITLE": "Best Practices",
        "SECTION_5_CONTENT": "Content for fifth section",
        
        # Hands-on section
        "HANDS_ON_TITLE": "Hands-on Exercise: Your Exercise Title",
        "HANDS_ON_DESCRIPTION": "Description of the hands-on activity",
        "TASK_TITLE": "Create Your Implementation",
        "TASK_DESCRIPTION": "Detailed task description",
        "STEP_1": "First implementation step",
        "STEP_2": "Second implementation step", 
        "STEP_3": "Third implementation step",
        "STEP_4": "Fourth implementation step",
        "STEP_5": "Fifth implementation step",
        "CODE_TEMPLATE": "# Your code template here\nclass ExampleClass:\n    pass",
        "EXTENSION_CHALLENGE": "Advanced challenge description",
        
        # Navigation
        "PREV_WEEK": str(session_num - 1),
        "NEXT_WEEK": str(session_num + 1),
        "PREV_SESSION_NUMBER": f"{session_num-1:02d}",
        "NEXT_SESSION_NUMBER": f"{session_num+1:02d}",
        "NEXT_SESSION_TITLE": "Next Session Title"
    }
    
    return config_template

def main():
    parser = argparse.ArgumentParser(description='Generate session files from template')
    parser.add_argument('--config', help='JSON configuration file path')
    parser.add_argument('--interactive', action='store_true', help='Interactive configuration mode')
    parser.add_argument('--create-config', type=int, help='Create configuration template for session number')
    parser.add_argument('--output', help='Output file path (default: auto-generated)')
    
    args = parser.parse_args()
    
    if args.create_config:
        # Create a configuration template
        config_template = create_config_template(args.create_config)
        config_file = f"configs/session_{args.create_config:02d}_config.json"
        
        os.makedirs("configs", exist_ok=True)
        with open(config_file, 'w') as f:
            json.dump(config_template, f, indent=2)
        
        print(f"Configuration template created: {config_file}")
        print("Edit this file with your session details, then run:")
        print(f"python scripts/generate_session.py --config {config_file}")
        return
    
    # Load configuration
    if args.config:
        config = load_config(args.config)
    elif args.interactive:
        config = interactive_config()
    else:
        print("Error: Must specify either --config or --interactive")
        parser.print_help()
        return
    
    # Load and process template
    template = load_template()
    session_content = replace_placeholders(template, config)
    
    # Determine output file
    if args.output:
        output_file = args.output
    else:
        session_num = config.get('SESSION_NUMBER', '00')
        output_file = f"docs/sessions/session-{session_num}.md"
    
    # Write session file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(session_content)
    
    print(f"✅ Session file generated: {output_file}")
    
    # Generate navigation configuration
    session_num = int(config.get('SESSION_NUMBER', 0))
    session_title = config.get('SESSION_TITLE', 'Session Title')
    components = [
        (config.get('COMPONENT_1_NAME', 'Component 1'), ''),
        (config.get('COMPONENT_2_NAME', 'Component 2'), ''),
        (config.get('COMPONENT_3_NAME', 'Component 3'), ''),
        (config.get('COMPONENT_4_NAME', 'Component 4'), ''),
        (config.get('COMPONENT_5_NAME', 'Component 5'), ''),
    ]
    
    nav_config = generate_navigation_config(session_num, session_title, components)
    
    print("\n📋 Add this to your mkdocs.yml navigation:")
    print(nav_config)
    
    print(f"\n🎯 Next steps:")
    print(f"1. Review and edit the generated file: {output_file}")
    print(f"2. Add the navigation configuration to mkdocs.yml")
    print(f"3. Create any required resource files in docs/files/")
    print(f"4. Add download links to docs/downloads.md")

if __name__ == "__main__":
    main()
