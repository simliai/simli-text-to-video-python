import requests
from dotenv import load_dotenv
import os
import json
import webbrowser
from urllib.parse import urljoin

# Load environment variables from .env file
load_dotenv()

url = "https://api.simli.ai/textToVideoStream"

payload = {
    "ttsAPIKey": os.getenv("ELEVENLABS_API_KEY"),
    "simliAPIKey": os.getenv("SIMLI_API_KEY"),
    "faceId": "tmp9i8bbq7c",
    "requestBody": {
        "audioProvider": "ElevenLabs",
        "text": """Ladies and gentlemen, picture this: You're stuck in traffic, watching the minutes tick by, when suddenly – whoosh! A gleaming yellow vehicle shaped like a banana glides effortlessly above all the chaos. That could be you in the Bananair, the world's first hover-capable fruit-shaped vehicle!

            Using our patented magnetic levitation technology, the Bananair floats three feet above any road surface. Its aerodynamic peel-shaped chassis isn't just for show – it reduces air resistance by 40% compared to traditional vehicles. The ergonomic interior seats four adults comfortably, with a premium potassium-colored leather trim that'll make every ride feel first-class.

            Worried about safety? Our triple-redundant stabilization system ensures you'll never slip up, even in the worst weather conditions. And with zero direct road contact, you can say goodbye to flat tires forever! The Bananair runs on clean electric power, with a range of 300 miles per charge. The best part? It parks vertically to save space – just tip it up like a real banana!

            For just $199,999, you too can be part of the fruit-ure of transportation. The Bananair: Because life is better at the top. Pre-order yours today!""",
        "voiceName": "pMsXgVXv3BLzUgSXRplE",
        "model_id": "eleven_turbo_v2",
        "voice_settings": {
            "stability": 0.1,
            "similarity_boost": 0.3,
            "style": 0.2
        }
    }
}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)
response_data = response.json()
print(response_data)

if response.status_code == 200:
    hls_url = response_data.get('hls_url')
    if hls_url:
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Video Player</title>
            <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
            <style>
                .container {{
                    max-width: 800px;
                    margin: 20px auto;
                    text-align: center;
                }}
                video {{
                    width: 100%;
                    margin: 20px 0;
                }}
                #playButton {{
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    margin-bottom: 20px;
                }}
                #playButton:hover {{
                    background-color: #45a049;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <button id="playButton">Click to Play Video</button>
                <video id="video" controls playsinline></video>
            </div>
            <script>
                document.addEventListener('DOMContentLoaded', function() {{
                    var video = document.getElementById('video');
                    var playButton = document.getElementById('playButton');
                    var videoSrc = '{hls_url}';
                    var hls;
                    
                    if (Hls.isSupported()) {{
                        hls = new Hls();
                        hls.loadSource(videoSrc);
                        hls.attachMedia(video);
                    }} else if (video.canPlayType('application/vnd.apple.mpegurl')) {{
                        video.src = videoSrc;
                    }}

                    playButton.addEventListener('click', function() {{
                        video.play()
                            .then(() => {{
                                console.log('Playback started');
                                playButton.style.display = 'none';
                            }})
                            .catch(e => console.error('Playback failed:', e));
                    }});
                }});
            </script>
        </body>
        </html>
        """
        
        # Save and open the HTML file
        with open('video_player.html', 'w') as f:
            f.write(html_content)
        
        # Open in default browser using file:// protocol for local files
        webbrowser.open('file://' + os.path.realpath('video_player.html'))
    else:
        print("No stream URL found in response")
else:
    print(f"Error: {response.status_code}")
    print(response.text)