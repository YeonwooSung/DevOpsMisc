#!/usr/bin/env python

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""DialogFlow API Detect Intent Python sample with audio file.
Examples:
  python detect_intent_audio.py -h
  python detect_intent_audio.py --agent AGENT \
  --session-id SESSION_ID --audio-file-path resources/hello.wav
"""

import argparse
import uuid

from google.cloud.dialogflowcx_v3.services.agents import AgentsClient
from google.cloud.dialogflowcx_v3.services.sessions import SessionsClient
from google.cloud.dialogflowcx_v3.types import audio_config
from google.cloud.dialogflowcx_v3.types import session

from pydub import AudioSegment

# [START dialogflow_detect_intent_audio]
def run_sample():
    # TODO(developer): Replace these values when running the function
    project_id = "r3test"
    # For more information about regionalization see https://cloud.google.com/dialogflow/cx/docs/how/region
    location_id = "asia-northeast1"
    # For more info on agents see https://cloud.google.com/dialogflow/cx/docs/concept/agent
    agent_id = "254d14dd-3328-4620-ada6-6b7a97bb10da"
    agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"
    # For more information on sessions see https://cloud.google.com/dialogflow/cx/docs/concept/session
    session_id = str(uuid.uuid4())

    audio_files = ['./test.mp3']
    #audio_files = [f'test{i}.mp3' for i in range(1,5)]
    # For more supported languages see https://cloud.google.com/dialogflow/es/docs/reference/language
    language_code = "ko"

    # run detect_intent_audio for all test cases
    for audio_file in audio_files:
        print(audio_file)
        detect_intent_audio(agent, session_id, audio_file, language_code)


def detect_intent_audio(agent, session_id, audio_file_path, language_code):
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

    sound = AudioSegment.from_file(audio_file_path, format="mp4")
    input_audio, sample_rate = sound.raw_data, sound.frame_rate

    input_audio_config = audio_config.InputAudioConfig(
        audio_encoding=audio_config.AudioEncoding.AUDIO_ENCODING_LINEAR_16,
        sample_rate_hertz=sound.frame_rate,
    )

    # with open(audio_file_path, "rb") as audio_file:
    #     input_audio = audio_file.read()
    #input_audio = AudioSegment.from_mp3(audio_file_path).raw_data
    #play_audio(sound)

    audio_input = session.AudioInput(config=input_audio_config, audio=input_audio)
    query_input = session.QueryInput(audio=audio_input, language_code=language_code)
    request = session.DetectIntentRequest(session=session_path, query_input=query_input)
    response = session_client.detect_intent(request=request)

    print("=" * 20)
    print(f"Query text: {response.query_result.transcript}")
    response_messages = [
        " ".join(msg.text.text) for msg in response.query_result.response_messages
    ]
    response_text = ' '.join(response_messages)
    print(f"Response text: {response_text}\n")


def play_audio(sound):
    import pyaudio
    from pydub.utils import make_chunks
    
    p = pyaudio.PyAudio()
    output = p.open(format=p.get_format_from_width(sound.sample_width),
                    channels=sound.channels,
                    rate=sound.frame_rate,
                    output=True) # frames_per_buffer=CHUNK_SIZE
    
    start = 0
    length = sound.duration_seconds
    end = start + length
    volume = 100
    playchunk = sound[start*1000.0:(start+length)*1000.0] - (60 - (60 * (volume/100.0)))
    millisecondchunk = 50 / 1000.0

    runtime = start
    keep_loop = True

    while keep_loop:
        for chunks in make_chunks(playchunk, millisecondchunk * 1000):
            runtime += millisecondchunk
            output.write(chunks._data)
            if runtime >= end:
                keep_loop = False
                break

# [END dialogflow_detect_intent_audio]

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(
    #     description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    # )
    # parser.add_argument(
    #     "--agent", help="Agent resource name.  Required.", required=True
    # )
    # parser.add_argument(
    #     "--session-id",
    #     help="Identifier of the DetectIntent session. " "Defaults to a random UUID.",
    #     default=str(uuid.uuid4()),
    # )
    # parser.add_argument(
    #     "--language-code",
    #     help='Language code of the query. Defaults to "en-US".',
    #     default="en-US",
    # )
    # parser.add_argument(
    #     "--audio-file-path", help="Path to the audio file.", required=True
    # )

    # args = parser.parse_args()

    # detect_intent_audio(
    #     args.agent, args.session_id, args.audio_file_path, args.language_code
    # )
    run_sample()
