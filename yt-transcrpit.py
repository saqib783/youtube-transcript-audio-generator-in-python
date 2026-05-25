from flask import Flask, request, render_template_string, send_file
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import edge_tts
import asyncio
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>YouTube Tool</title>
</head>
<body style="font-family: Arial; text-align:center; margin-top:50px;">

    <h2>YouTube Transcript + Voice Tool</h2>

    <form method="POST">
        <input type="text" name="url" placeholder="Enter YouTube URL"
        style="width:400px; padding:10px;">
        <button type="submit">Generate</button>
    </form>

    {% if text %}
        <h3>Done ✅</h3>
        <a href="/download/text">Download Transcript</a><br><br>
        <a href="/download/audio">Download MP3</a>
    {% endif %}

</body>
</html>
"""

def get_video_id(url):
    query = urlparse(url)

    if query.hostname == 'youtu.be':
        return query.path[1:]

    if query.hostname in ('youtube.com', 'www.youtube.com'):
        return parse_qs(query.query)['v'][0]



async def text_to_speech(text):
    communicate = edge_tts.Communicate(
        text,
        voice="en-US-GuyNeural"
    )
    await communicate.save("output.mp3")



def process_video(url):

    video_id = get_video_id(url)

 
    api = YouTubeTranscriptApi()

    transcript_data = api.fetch(video_id)

    text = ""

    for item in transcript_data:
        text += item.text + " "

   
    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write(text)

   
    asyncio.run(text_to_speech(text))

    return text



@app.route("/", methods=["GET", "POST"])
def home():

    text = None

    if request.method == "POST":
        url = request.form["url"]
        text = process_video(url)

    return render_template_string(HTML, text=text)


@app.route("/download/text")
def download_text():
    return send_file("transcript.txt", as_attachment=True)


@app.route("/download/audio")
def download_audio():
    return send_file("output.mp3", as_attachment=True)



if __name__ == "__main__":
    app.run(debug=True)