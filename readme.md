# Meeting Notes

Transcribe your meetings notes - or any other audio file - with OpenAI's whisper model.

## Installation 

Install project dependencies:

```bash
pip install -r requirements.txt
```

Set your OpenAI API key 
```bash
export OPENAI_API_KEY=<token>
```

## Usage

This script accepts the input and output file names as command-line arguments. Here's how you can use it:

```bash
python app.py input.m4a output.txt
```