# youtube-transcript-audio-generator

# YouTube Transcript & Voice Tool 🚀

A web-based automation tool built with Flask that extracts transcript text from any YouTube video via its URL and converts that text into downloadable audio format. This project is optimized to showcase full-stack automation capabilities for engineering portfolios.

---

## 📸 Application Preview
Here is the user interface of the tool in action:

![YouTube Transcript and Voice Tool Interface](https://github.com/saqib783/youtube-transcript-audio-generator-in-python/blob/a798d0f67c05204d9c29d871aa0d1d3624691e1a/Screenshot%20(1884).png)

---

## 🌟 Features
* **Web UI Integration:** Clean frontend design built on a local Flask server (`127.0.0.1:5000`).
* **URL Parsing:** Safely parses incoming YouTube URLs to extract the required video ID string.
* **Transcript Extraction:** Connects directly with YouTube servers to pull full video scripts.
* **Audio Generation:** Seamless text-to-speech mechanism to output transcript files directly into standard `.mp3` format.

---

## 🛠️ Built With & Dependencies
This application requires standard built-in core components along with third-party web frameworks:
* **Python 3.x** - Core implementation language.
* `Flask` - Python web framework to run the local host UI server.
* `youtube-transcript-api` - Unofficial API library to catch subtitles from YouTube clips.
* `os` *(Built-in)* - Internal operating system library used for file creation pathways and routing.
* `urllib.parse` *(Built-in)* - Standard core URL parsing utility used to isolate specific query parameters from raw web addresses.

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally on your system.

### 1. Installation
Clone the repository using the official link:
```bash
git clone https://github.com/saqib783/youtube-transcript-audio-generator-in-python.git
cd youtube-transcript-audio-generator-in-python
```

### 2. Install Required Python Packages
Run the pip setup command in your terminal to fetch the non-standard required modules (`os` and `urllib.parse` are pre-included with Python natively and do not require manual pip installation):
```bash
pip install flask youtube-transcript-api gtts
```
*(Note: Replace `gtts` with whichever specific speech-processing module you used in your script, such as `pyttsx3`)*

### 3. Usage
Initialize your web script locally:
```bash
python yt-transcrpit.py
```
Open your web browser and navigate to the address shown in your server terminal:
```text
http://127.0.0
```
Paste your target YouTube video link into the entry bar, hit **Generate**, and check your target folder for output files once complete!

---

## 📺 Video Explanation
I built this project for my portfolio and explained the entire code structure step-by-step on YouTube. 
👉 [Watch the full code breakdown here](https://youtu.be/feAEMsyif5Q)

---

## 💼 Connect With Me
* **GitHub Repository:** [saqib783 / youtube-transcript-audio-generator-in-python](https://github.com/saqib783/youtube-transcript-audio-generator-in-python)
* **Instagram:** [SaqibRashid.devops](https://www.instagram.com/saqibrashid.devops/)
