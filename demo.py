
from gtts import gTTS

import os

Text = "LOL This is really funny, anyways My name is Minal"
output = gTTS(text=Text, lang='en', slow=False)
output.save('output.mp3')

os.system("start output.mp3")
