# Google Cloud Platform

## Compute Engine

### Startup script

In GCP, you could add a startup script to the compute engine so that whenever the compute engine has been started, the script will be executed. By doing this, you could automate the setup of the compute engine.

- [Startup script](./compute_engine/gcp_startup_script.sh)

## Cloud Function

Please refer to [this page](./cloud_function).

## Dialogflow

Dialogflow is Google's natural language understanding tool for building conversational experiences, such as voice apps and chatbots, powered by AI.

### Dialogflow CX

- [detect intent by audio input](./dialogflow/dialoglow-cx/detect_intent_audio.py)
- [detect intent by text input](./dialoglow/dialoglow-cx/detect_intent.py)
- [detect intent by text input, and return audio by using tts](./dialogflow/dialoglow-cx/detect_intent_tts.py)
- [detect intent by audio input, and return audio by using tts](./dialogflow/dialoglow-cx/detect_intent_sts.py)

### Dialogflow ES

- [detect intent with tts](./dialogflow/dialogflow-es/detect_text_to_speech.py)
- [simple chatbot by using dialogflow es](./dialogflow/dialogflow-es/main.py)
