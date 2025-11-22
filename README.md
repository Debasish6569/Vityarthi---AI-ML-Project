# AI Symptom Checker (10-Question Diagnostic Interview)

**Name:** Debasish Kumar Sahoo  
**Registration Number:** 25BAI10173  
**Subject:** Fundamentals of AI/ML

## Project Overview

This project implements a rule-based conversational medical assistant using the Google Gemini API. The system conducts a structured **10-question diagnostic interview** designed to gather symptoms and basic medical information from a user. After all ten responses are collected, the system generates a probable assessment along with a disclaimer.

This project demonstrates practical application of:
- Prompt engineering  
- Multi-turn conversational AI  
- System instructions in LLM-based applications  
- Error handling and API integration  

This is **not a real medical diagnostic tool** and is created strictly for academic purposes.

---

## Features

- Uses Gemini 2.5 Flash model via Google Generative AI API  
- Implements a strict 10-question medical interview workflow  
- Custom system instructions that enforce conversational rules  
- Provides an assessment only after the 10th response  
- Handles invalid API key errors gracefully  
- Fully terminal-based interaction  

---

## Requirements

Install the required library:

```zsh
pip install google-genai
