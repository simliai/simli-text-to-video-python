# Text-to-Video Generator

A Python script that converts text to video using Simli.ai and ElevenLabs APIs to generate an AI presenter speaking your provided text.

## Prerequisites

- Python 3.x
- Required Python packages (install via pip):
  - requests
  - python-dotenv
  - webbrowser

## Setup

1. Clone this repository
2. Create a `.env` file in the root directory using the provided `env_sample` as a template
3. Add your API keys to the `.env` file:
   ```
   SIMLI_API_KEY="your_simli_api_key"
   ELEVENLABS_API_KEY="your_elevenlabs_api_key"
   ```

## Usage

1. Edit the `text` field in `text2video.py` to customize what the AI presenter will say
2. Run the script:
   ```
   python text2video.py
   ```
3. The script will:
   - Generate a video using the Simli.ai API
   - Create an HTML player file
   - Automatically open the video in your default web browser

## Configuration

You can customize various parameters in `text2video.py`:
- `faceId`: Choose different AI presenters
- `voice_settings`: Adjust voice parameters like stability and style
- `voiceName`: Select different ElevenLabs voices

## Note

Make sure to keep your API keys confidential and never commit them to version control.
