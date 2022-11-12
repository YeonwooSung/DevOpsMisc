import uuid

from google.cloud.dialogflowcx_v3.services.agents import AgentsClient
from google.cloud.dialogflowcx_v3.services.sessions import SessionsClient
from google.cloud.dialogflowcx_v3.types import audio_config
from google.cloud.dialogflowcx_v3.types import session

import pyaudio
from pydub import AudioSegment
from pydub.utils import make_chunks


def run_sample(stream_ver=True):
    """Run a sample Dialogflow API call"""
    project_id = "r3test"
    # For more information about regionalization see https://cloud.google.com/dialogflow/cx/docs/how/region
    location_id = "asia-northeast1"
    # For more info on agents see https://cloud.google.com/dialogflow/cx/docs/concept/agent
    agent_id = "254d14dd-3328-4620-ada6-6b7a97bb10da"
    agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"

    session_id = str(uuid.uuid4())
    audio_file_path = "test2.mp3"
    language_code = "ko"
    audio_encoding = "OUTPUT_AUDIO_ENCODING_MP3_64_KBPS"
    output_file = "./sts_output.mp3"
    if stream_ver:
        detect_intent_stream(agent, session_id, audio_file_path, language_code, audio_encoding, output_file)
    else:
        detect_intent_audio(agent, session_id, audio_file_path, language_code, audio_encoding, output_file)


def detect_intent_audio(agent, session_id, audio_file_path, language_code, audio_encoding, output_file, debug=False):
    """Returns the result of detect intent with an audio file as input.
    Using the same `session_id` between requests allows continuation
    of the conversation."""
    session_path = f"{agent}/sessions/{session_id}"
    print(f"Session path: {session_path}\n")
    client_options = None
    agent_components = AgentsClient.parse_agent_path(agent)
    location_id = agent_components["location"]
    if location_id != "global":
        api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
        print(f"API Endpoint: {api_endpoint}\n")
        client_options = {"api_endpoint": api_endpoint}
    session_client = SessionsClient(client_options=client_options)

    input_audio_config = audio_config.InputAudioConfig(
        audio_encoding=audio_config.AudioEncoding.AUDIO_ENCODING_LINEAR_16,
        sample_rate_hertz=24000,
    )

    with open(audio_file_path, "rb") as audio_file:
        input_audio = audio_file.read()

    audio_input = session.AudioInput(config=input_audio_config, audio=input_audio)
    synthesize_speech_config = audio_config.SynthesizeSpeechConfig(
        speaking_rate=1,
        pitch=0.0,
    )
    output_audio_config = audio_config.OutputAudioConfig(
        synthesize_speech_config=synthesize_speech_config,
        audio_encoding=audio_config.OutputAudioEncoding[audio_encoding],
    )

    query_input = session.QueryInput(audio=audio_input, language_code=language_code)
    request = session.DetectIntentRequest(
        session=session_path,
        query_input=query_input,
        output_audio_config=output_audio_config,
    )
    response = session_client.detect_intent(request=request)

    response_messages = [
        " ".join(msg.text.text) for msg in response.query_result.response_messages
    ]

    if debug:
        print("=" * 20)
        print(f"Query text: {response.query_result.transcript}")
        print(f"Response text: {' '.join(response_messages)}\n")
        print(
        'Speaking Rate: '
        f'{response.output_audio_config.synthesize_speech_config.speaking_rate}')
        print(
        'Pitch: '
        f'{response.output_audio_config.synthesize_speech_config.pitch}')
    with open(output_file, 'wb') as fout:
        fout.write(response.output_audio)
    print(f'Audio content written to file: {output_file}')


def detect_intent_stream(agent, session_id, audio_file_path, language_code, audio_encoding, output_file, debug=True):
    """Returns the result of detect intent with streaming audio as input.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    session_path = f"{agent}/sessions/{session_id}"
    print(f"Session path: {session_path}\n")
    client_options = None
    agent_components = AgentsClient.parse_agent_path(agent)
    location_id = agent_components["location"]
    if location_id != "global":
        api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
        print(f"API Endpoint: {api_endpoint}\n")
        client_options = {"api_endpoint": api_endpoint}
    session_client = SessionsClient(client_options=client_options)

    input_audio_config = audio_config.InputAudioConfig(
        audio_encoding=audio_config.AudioEncoding.AUDIO_ENCODING_LINEAR_16,
        sample_rate_hertz=24000,
    )

    def request_generator():
        audio_input = session.AudioInput(config=input_audio_config)
        query_input = session.QueryInput(audio=audio_input, language_code=language_code)
        # voice_selection = audio_config.VoiceSelectionParams()
        # synthesize_speech_config = audio_config.SynthesizeSpeechConfig()

        # Sets the voice name and gender
        # voice_selection.name = "en-GB-Standard-A"
        # voice_selection.ssml_gender = (
        #     audio_config.SsmlVoiceGender.SSML_VOICE_GENDER_FEMALE
        # )
        synthesize_speech_config = audio_config.SynthesizeSpeechConfig(
            speaking_rate=1,
            pitch=0.0,
        )

        # synthesize_speech_config.voice = voice_selection

        # Sets the audio encoding
        output_audio_config = audio_config.OutputAudioConfig(
            synthesize_speech_config=synthesize_speech_config,
            audio_encoding=audio_config.OutputAudioEncoding[audio_encoding],
        )
        # output_audio_config.synthesize_speech_config = synthesize_speech_config

        # The first request contains the configuration.
        yield session.StreamingDetectIntentRequest(
            session=session_path,
            query_input=query_input,
            output_audio_config=output_audio_config,
        )


        #TODO: 여기서부터
        sound = AudioSegment.from_file(audio_file_path)

        p = pyaudio.PyAudio()
        output = p.open(format=p.get_format_from_width(sound.sample_width),
                        channels=sound.channels,
                        rate=sound.frame_rate,
                        output=True) # frames_per_buffer=CHUNK_SIZE
        
        start = 0
        length = sound.duration_seconds
        end = start + length
        volume = 100
        runtime = start
        keep_loop = True
        playchunk = sound[start*1000.0:(start+length)*1000.0] - (60 - (60 * (volume/100.0)))
        millisecondchunk = 50 / 1000.0
        while keep_loop:
            for chunks in make_chunks(playchunk, millisecondchunk * 1000):
                runtime += millisecondchunk
                # output.write(chunks._data)
                audio_input = session.AudioInput(audio=chunks._data)
                query_input = session.QueryInput(audio=audio_input)
                yield session.StreamingDetectIntentRequest(query_input=query_input)
                if runtime >= end:
                    keep_loop = False
                    break
        #TODO: 여기까지

        # # Here we are reading small chunks of audio data from a local
        # # audio file.  In practice these chunks should come from
        # # an audio input device.
        # with open(audio_file_path, "rb") as audio_file:
        #     while True:
        #         chunk = audio_file.read(4096)
        #         if not chunk:
        #             break
        #         # The later requests contains audio data.
        #         audio_input = session.AudioInput(audio=chunk)
        #         query_input = session.QueryInput(audio=audio_input)
        #         yield session.StreamingDetectIntentRequest(query_input=query_input)

    responses = session_client.streaming_detect_intent(requests=request_generator())

    print("=" * 20)
    for response in responses:
        print(f'Intermediate transcript: "{response.recognition_result.transcript}".')

    # Note: The result from the last response is the final transcript along
    # with the detected content.
    response = response.detect_intent_response
    print(f"Query text: {response.query_result.transcript}")
    response_messages = [
        " ".join(msg.text.text) for msg in response.query_result.response_messages
    ]
    print(f"Response text: {' '.join(response_messages)}\n")

    if debug:
        print("=" * 20)
        print(f"Query text: {response.query_result.transcript}")
        print(f"Response text: {' '.join(response_messages)}\n")
        print(
        'Speaking Rate: '
        f'{response.output_audio_config.synthesize_speech_config.speaking_rate}')
        print(
        'Pitch: '
        f'{response.output_audio_config.synthesize_speech_config.pitch}')
    with open(output_file, 'wb') as fout:
        fout.write(response.output_audio)


if __name__ == "__main__":
    run_sample()
