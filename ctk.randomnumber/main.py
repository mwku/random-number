import random
import os
import pygame
from gtts import gTTS


class rand():
    def __init__(self):
        self.count = 5

        self.number_index = []
        self.randnumber = []
        self.replynumber = []

        self.startnumber = 1
        self.endnumber = 35

        self.number_index = [int(i)for i in range(1, 36)]

        self.read_ = True  # bool

    def run(self):
        if len(self.number_index) >= self.count:
            self.randnumber = random.sample(self.number_index, self.count)
            for i in self.randnumber:
                self.number_index.remove(i)
            return True
        else:
            self.number_index = []
            for i in range(self.startnumber, self.endnumber+1):
                self.number_index.append(i)
            self.randnumber = random.sample(self.number_index, self.count)
            for i in self.randnumber:
                self.number_index.remove(i)
            return False

    def clear(self):
        self.number_index = []
        for i in range(self.startnumber, self.endnumber+1):
            self.number_index.append(i)

    def count_change(self, newcount):
        self.count = int(newcount)

    def startnumber_change(self, newnumber):
        self.startnumber = int(newnumber)
        self.clear()

    def endnumber_change(self, newnumber):
        self.endnumber = int(newnumber)
        self.clear()

    def read(self):
        for i in self.randnumber:
            tts = gTTS(text=str(i), lang='en', tld="us")
            tts.save("output.mp3")
            pygame.init()
            pygame.mixer.music.load("output.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            pygame.mixer.music.unload()
            os.remove("output.mp3")
