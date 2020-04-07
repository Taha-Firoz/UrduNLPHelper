## Please run the following commands for windows installs:
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
