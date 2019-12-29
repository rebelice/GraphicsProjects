import pyaudio
import wave

import numpy as np
import pygame
from pygame.locals import *


class Const():
	CHUNK = 2048
	FILENAME = 'simple.wav'

class MusicVisualizer(object):

	def display(self):
		# 展示逻辑
		while self.wavData != '':
			self.stream.write(self.wavData)
			# 读取每CHUNK的时域数据
			self.wavData = self.wav.readframes(Const.CHUNK)
			temp = np.fromstring(self.wavData, dtype=np.int16)
			# FFT，得到频域数据
			realData=np.real(np.fft.fft(temp))

			self.screen.fill((0, 0, 0)) 
			count=50
			# 绘制矩形
			for n in range(0,realData.size,count):
				hight=abs(int(realData[n]/10000))
				pygame.draw.rect(self.screen,(25,202,173),Rect((20*n/count,200),(20,-hight)))

			# 更新
			pygame.display.update()

	def __init__(self):
		# 读入文件
		self.wav = wave.open(Const.FILENAME, 'rb')
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(format=self.p.get_format_from_width(self.wav.getsampwidth()),
	  					  	 	  channels=self.wav.getnchannels(),
	  					  	 	  rate=self.wav.getframerate(),
							 	  output=True)

		self.wavData = self.wav.readframes(Const.CHUNK)

		pygame.display.set_caption('Music Visualizer')
		self.screen = pygame.display.set_mode((400, 200), 0, 32)

	def terminate(self):
		self.stream.stop_stream()
		self.stream.close()
		self.p.terminate()

if __name__ == '__main__':
	music = MusicVisualizer()
	music.display()
	music.terminate()