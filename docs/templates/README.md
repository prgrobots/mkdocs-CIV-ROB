# Session Template System

This directory contains the template system for generating consistent course sessions based on the successful Session 4 structure.  Some changes may be in the actual session_4.md that will be more current.

Adapt requested session to the new content and ignore the template where necessary 

## 🎯 **Template Features**

The template system provides:
- **Consistent structure** across all sessions
- **Automated navigation generation** for mkdocs.yml
- **Placeholder-based content** for easy customization
- **Professional formatting** with proper markdown structure

## 📁 **Files**

- `session-template.md` - Main session template with placeholders
- `README.md` - This documentation file

## 🚀 **Quick Start**

### 1. Create a Configuration Template

```bash
python scripts/generate_session.py --create-config 5
```

This creates `configs/session_05_config.json` with all placeholders.

### 2. Edit the Configuration

Edit the JSON file with your session-specific content:

```json
{
  "SESSION_NUMBER": "5",
  "SESSION_TITLE": "Your Session Title",
  "WEEK_NUMBER": "5",
  "ELEMENT_CODE": "ICTPRG430 Element 2.2",
  ...
}
```

### 3. Generate the Session

```bash
python scripts/generate_session.py --config configs/session_05_config.json
```

This creates the session file and provides navigation configuration.

## 📋 **Template Structure**

The template follows the proven Session 4 structure:

1. **Session Header** - Week, element, duration, phase
2. **Session Introduction** - Overview of what students will do
3. **Learning Objectives** - 5 specific, measurable outcomes
4. **Session Structure** - 5 main components with descriptions
5. **Session Overview** - Detailed introduction paragraph
6. **Pre-Session Preparation** - Required reading and setup
7. **Theory Sections** - 5 numbered main content sections
8. **Hands-on Exercise** - Practical implementation activity
9. **Live Demonstration** - Instructor-led coding examples
10. **Extension Activity** - Advanced concepts and challenges
11. **Research Activities** - Out-of-class investigation topics
12. **Lab Section** - Practical setup or enhancement work
13. **Key Takeaways** - Summary of main concepts
14.  **Knowledge Check** - Simple question with hidden answers.
15. **Next Session Preview** - What's coming next
16. **Resources** - Downloads and further reading
17. **Navigation** - Links to previous/next sessions

## 🎨 **Customization**

### Essential Placeholders

These placeholders must be customized for each session:

- `{{SESSION_NUMBER}}` - Session number (e.g., "5")
- `{{SESSION_TITLE}}` - Main topic title
- `{{WEEK_NUMBER}}` - Corresponding week number
- `{{ELEMENT_CODE}}` - Learning element reference
- `{{PHASE_NAME}}` - Course phase name

### Content Placeholders

- `{{SESSION_DESCRIPTION}}` - What students will do
- `{{OBJECTIVE_1}}-{{OBJECTIVE_5}}` - Learning objectives
- `{{SECTION_1_TITLE}}-{{SECTION_5_TITLE}}` - Main section titles
- `{{HANDS_ON_TITLE}}` - Exercise title
- `{{DEMONSTRATION_TITLE}}` - Demo section title

### Component Structure

Each session has 5 main components:
- `{{COMPONENT_1_NAME}}` - Usually "Theory Session"
- `{{COMPONENT_2_NAME}}` - Usually "Hands-on Exercise"  
- `{{COMPONENT_3_NAME}}` - Usually "Live Demonstration"
- `{{COMPONENT_4_NAME}}` - Usually "Extension Activity"


## 🔧 **Advanced Usage**

### Interactive Mode

Generate sessions interactively:

```bash
python scripts/generate_session.py --interactive
```

### Custom Output Location

Specify output location:

```bash
python scripts/generate_session.py --config configs/session_05_config.json --output custom/location.md
```

### Navigation Generation

The script automatically generates navigation configuration for mkdocs.yml:

```yaml
- Week 5 - Advanced Class Features & Magic Methods:
  - Session 5: sessions/session-05.md
  - Theory Session: 'sessions/session-05/#python-magic-methods'
  - Hands-on Exercise: 'sessions/session-05/#hands-on-exercise-enhanced-robot-class'
  - Live Demonstration: 'sessions/session-05/#live-demonstration-property-decorators-in-action'
  - Extension Activity: 'sessions/session-05/#extension-activity-robot-position-operators'
  - Lab Enhancement: 'sessions/session-05/#lab-enhancement-advanced-robot-features'
  - Resources: downloads.md
  - Assessment: assessment.md
```

## 📚 **Best Practices**

### 1. Consistent Naming
- Use consistent component names across sessions
- Follow the established 5-component structure
- Maintain numbering conventions

### 2. Content Guidelines
- Keep learning objectives specific and measurable
- Ensure hands-on exercises are practical and relevant
- Include proper attribution for borrowed content
- Provide working code examples

### 3. Navigation Setup
- Always copy the generated navigation to mkdocs.yml
- Test anchor links after generation
- Ensure file paths are correct

### 4. Resource Management
- Create corresponding download files
- Update downloads.md with new resources
- Include proper file size estimates

## 🎓 **Session Quality Checklist**

Before finalizing a session:

- [ ] All placeholders replaced with meaningful content
- [ ] Navigation links tested and working
- [ ] Code examples syntax-checked
- [ ] Download files created and linked
- [ ] Proper attribution included where needed
- [ ] Consistent formatting throughout
- [ ] Learning objectives align with content
- [ ] Extension challenges are appropriate difficulty

## 📂 **Example Configuration Files**

See `configs/session_05_config.json` for a complete example of how to configure a session on "Advanced Class Features & Magic Methods".

## 🔄 **Template Updates**

To update the template system:

1. Modify `docs/templates/session-template.md`
2. Test with existing configuration files
3. Update this documentation
4. Regenerate example sessions to verify compatibility

## 💡 **Tips**

- **Start with a copy** of an existing config file for similar sessions
- **Use descriptive titles** that clearly indicate the session focus
- **Keep code examples simple** but illustrative of key concepts
- **Include real robotics applications** to maintain course relevance
- **Test generated sessions** with MkDocs serve before committing

This template system ensures consistency, saves time, and maintains the high quality established in Session 4 across your entire course.
