# Formbricks Survey Integration

This directory contains scripts and data for creating technical assessment surveys in Formbricks.

## Files

### Scripts
- `formbricks_assitant.py` - Main script for creating surveys via Formbricks API
- `assessment_conv.py` - Script for converting original JSON assessments to Formbricks format

### Data Files
- `basic_v2_formbricks.json` - Basic level assessment (57 questions)
- `medium_v2_formbricks.json` - Medium level assessment (60 questions)
- `advanced_v2_formbricks.json` - Advanced level assessment (43 questions)
- `funnel_registration_formbricks.json` - Registration funnel

### Documentation
- `Form_requirements.md` - Complete API documentation and requirements
- `.env` - Environment variables (API keys, etc.)

### Archive
- `archive/` - Contains previous versions of JSON files

## Usage

```bash
# Create a survey
python3 formbricks_assitant.py

# Convert assessments
python3 assessment_conv.py
```

See `Form_requirements.md` for detailed documentation.