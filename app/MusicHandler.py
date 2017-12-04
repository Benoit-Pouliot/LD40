import pygame, os


class MusicHandler:
    def __init__(self, musicName):
        self.musicName = musicName

    def update(self, musicName):
        if self.musicName != musicName:
            self.stop()
            self.musicName = musicName
            self.play()

    def play(self):
        pygame.mixer.music.load(os.path.join('music', self.musicName))
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)

    def stop(self):
        pygame.mixer.music.stop()
