## Urdu Audio Dataset Generation Helper
This tool is a simple gui that lets you view your urdu sentence and record it with ease, it stores each audio file witht he respective ID for the sentence. At the moment it's specifically made for NUCES NLP Urdu dataset file and there are no plans of expanding it.

## Features
- Record, Redo and Save audio files
- Convert Urdu text to Roman Urdu for easier readability (Unstable)
- Easy shortcuts like `s key` to record/redo/stop  `n key` or `d key` to move to next sentence

## Please run the following commands for windows installs:
You need the same version of chrome driver as your [chrome browser version](https://chromedriver.chromium.org/downloads)
```
pip install -r requirements.txt
pipwin install pyaudio
```
#### or if you want to install the libraries individually
```
pip install wave
pip install pipwin
pipwin install pyaudio
pip install selenium
```


## To run the program 
```
python app.py
```

## Troubleshooting
Incase the program doesn't start recording your audio and gives and exception or error. It's most probably related to a sampling rate not being set to that pythons expecting.


- Go into your microphones advanced settings
- Choose the advanced tab and set your sampling rate to 44100
