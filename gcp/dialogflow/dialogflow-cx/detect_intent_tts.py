#!/usr/bin/env python

# Copyright 2020-2022 Google LLC
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

# Detects intent and returns a synthesized Text-to-Speech (TTS) response

# [START dialogflow_cx_v3_detect_intent_synthesize_tts_response_async]
import uuid
import os

from google.cloud.dialogflowcx_v3.services.sessions import SessionsClient
from google.cloud.dialogflowcx_v3.types import audio_config
from google.cloud.dialogflowcx_v3.types import session

import pyaudio
from pydub import AudioSegment
from pydub.utils import make_chunks



def play_and_voice_audio_file(audio_file):
    cwd = os.getcwd()
    audio_file_path = f'{cwd}{audio_file}' if cwd.endswith('/') else f'{cwd}/{audio_file}'
    print(audio_file_path)

    file_stats = os.stat(audio_file_path)
    file_size = file_stats.st_size

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
    print('play ends')
    print(f'remove {audio_file}')
    os.system(f'rm -rf {audio_file}')


def run_sample():
    project_id = "r3test"
    # For more information about regionalization see https://cloud.google.com/dialogflow/cx/docs/how/region
    location_id = "asia-northeast1"
    # For more info on agents see https://cloud.google.com/dialogflow/cx/docs/concept/agent
    agent_id = "254d14dd-3328-4620-ada6-6b7a97bb10da"
    agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"
    texts = ["안녕!", "넌 누구야?", "오늘 날씨는?", "뭐라카노"]
    # For more supported languages see https://cloud.google.com/dialogflow/es/docs/reference/language
    language_code = "ko"

    # For more supported audio encodings see https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/OutputAudioConfig
    audio_encoding = "OUTPUT_AUDIO_ENCODING_MP3_64_KBPS"

    session_id = uuid.uuid4()

    idx = 0
    for text in texts:
        output_file = f'{session_id}_{idx}.mp3'
        idx += 1
        detect_intent_synthesize_tts_response(
            project_id,
            location_id,
            agent_id,
            text,
            audio_encoding,
            language_code,
            output_file,
            session_id,
        )

        play_and_voice_audio_file(output_file)


def detect_intent_synthesize_tts_response(
    project_id,
    location,
    agent_id,
    text,
    audio_encoding,
    language_code,
    output_file,
    session_id_str,
):
    """Returns the result of detect intent with synthesized response."""
    client_options = None
    if location != "global":
        api_endpoint = f"{location}-dialogflow.googleapis.com:443"
        print(f"API Endpoint: {api_endpoint}\n")
        client_options = {"api_endpoint": api_endpoint}
    session_client = SessionsClient(client_options=client_options)
    session_id = str(session_id_str)

    # Constructs the audio query request
    session_path = session_client.session_path(
        project=project_id,
        location=location,
        agent=agent_id,
        session=session_id,
    )
    text_input = session.TextInput(text=text)
    query_input = session.QueryInput(
        text=text_input,
        language_code=language_code
    )
    synthesize_speech_config = audio_config.SynthesizeSpeechConfig(
      speaking_rate=1,
      pitch=0.0,
    )
    output_audio_config = audio_config.OutputAudioConfig(
      synthesize_speech_config=synthesize_speech_config,
      audio_encoding=audio_config.OutputAudioEncoding[
        audio_encoding],
    )
    request = session.DetectIntentRequest(
        session=session_path,
        query_input=query_input,
        output_audio_config=output_audio_config,
    )

    response = session_client.detect_intent(request=request)
    print(
      'Speaking Rate: '
      f'{response.output_audio_config.synthesize_speech_config.speaking_rate}')
    print(
      'Pitch: '
      f'{response.output_audio_config.synthesize_speech_config.pitch}')
    with open(output_file, 'wb') as fout:
        fout.write(response.output_audio)
    print(f'Audio content written to file: {output_file}')



if __name__ == "__main__":
    run_sample()
