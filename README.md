# romantic-alexa
## Build an Artificial Assistant

### Full tutorial (video)
To watch the tutorial, click on the image below

[![Watch the video-- Build your own Alexa](https://img.youtube.com/vi/AWvsXxDtEkU/0.jpg)](https://www.youtube.com/watch?v=AWvsXxDtEkU "Build your own Alexa")

## Installation
### For windows users
(run those in command prompt/cmt/terminal)
For the robot to listen to our voice/speech
`pip install speechRecognition`

To speak out, or text to speech
`pip install pyttsx3`

For advance control on browser
`pip install pywhatkit`

To get wikipedia data
`pip install wikipedia`

To get funny jokes
`pip install pyjokes`

### For linux users
Learn all the above commands on terminal. Make sure to use `pip3`, because in linux `pip` refers for `python2` and `pip3` refers to `python3`.
Install these too - 
`pip3 install pyAudio`

In case any error pops up install this -
`pip3 install portAudio`

### For unbound variable error
Please use python versions 3.6.x only.
For downloading the optimim version of python, you can go to https://www.python.org/downloads/release/python-365/

### For execution stuck at 'listening...'
I have included the `listener.adjust_for_ambient_noise(source)` line above the `voice = listener.listen(source)` line.
This helps in cases where the background noise might have conflicts with the microphone input. 

#### Issues
If you encounter any problems feel free to open a new issue. Before that check other closed issues and check if your issue matches with any older issues.
