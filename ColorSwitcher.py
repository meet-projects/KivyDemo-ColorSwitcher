import kivy
kivy.require('1.8.0')

from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

class SpecialWidget(Widget):
	pass

class ColorSwitcherApp(App):
	def build(self):
		self.root = SpecialWidget()
		self.red = 1
		self.green = 1
		self.blue = 1
		return self.root
	
	def change_color(self):
		with self.root.canvas.before:
			Color(self.red,self.green,self.blue)
			Rectangle(pos=self.root.pos,size=self.root.size)
		self.update_colors()
	
	def update_colors(self):
		if(self.red == 1 and self.green == 1):
			self.red = 0
			self.green = 1
		elif(self.green==1 and self.blue == 1):
			self.green = 0
			self.red = 1
		elif(self.red==1 and self.blue==1):
			self.green=1
			self.blue=0
		else:
			self.red=1
			self.green=1
			self.blue=1
	pass


if __name__=='__main__':
	ColorSwitcherApp().run()