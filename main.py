""" File Encryption and Decryption app built using kivy python Gui and kivy language,the logic is in this module, the presentation is in cryptee.kv file"""
import kivy
from kivy.uix.label import Label
from kivy.uix.textinput  import TextInput
from kivy.uix. button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.filechooser import FileChooserIconView
from kivy.properties import(StringProperty,NumericProperty,ObjectProperty)
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager,Screen
from plyer.platforms.android import tts,stt,audio
import time






"""
class AppPop provides application feedback to the user a subclass of the FloatLayout
"""

class AppPop(FloatLayout):
	cancel=ObjectProperty()
	
	

class MsgLabel(Label):
	pass
	
class SuccessLabel(Label):
	pass



"""
class LoadEncFile,a class declaration for the presentation of the FieChooserIconView implemented in cryptee.kv as <LoadEncFile>:  
"""	
	
class LoadEncFile(FloatLayout):
	
	load=ObjectProperty()
	cancel=ObjectProperty()
	
"""
Screen class declaration for the text2 speech implemented in tsst.kv as a subclass 
"""


class Text2Speech(Screen):
	pass

"""
ApScreen, a class declaration for the ScreenManager, the root widget of the application
"""

class ApScreen(ScreenManager):
	
	pathfile=StringProperty("")
	pwd=StringProperty(" ")
	path=StringProperty("")
	loadfile=ObjectProperty()
	savefile=ObjectProperty()
	mode=StringProperty("")
	result=StringProperty("")
	
	def dismiss_pop(self):
		 #dismiss all popup widget instance
		 self.pop.dismiss()
	
	def show_load(self):
		#display Popup for FileChooserIconView, argument is mode either text2speech or or speech2text
		content= LoadEncFile(load=self.load,cancel=self.dismiss_pop)
		self.pop=Popup(title="Open File",content=content,size_hint=(0.9,0.9))
		self.pop.open()
		
			
		
		
	
	def load(self,path,filename):
		#method that set the filepath of the file to comvert to speech or vice versa, argument are path directory of the file,filename name of the file amd mode
		path=path
		file=filename[0]
		filepath=os.path.join(path,file)
		self.ids.f_input1.text=filepath
		
		self.dismiss_pop()
		
	def validatepath(self,filepath):
		#method to validate filepath,argument filepath return boolean, True if path is valid and false otherwise
		if os.path.isfile(filepath):
			return True
		else:
			return False
	
	
	
	
	def processText(self,text,):
		# method to encrypt and decrypt file depending on the mode. Argument are filepath and password, return string succesful if no error
			self.ids.t_msg.text="Processing"
			ts=text
			if ts==" ":
				self.ids.t_msg.text="Text cannot be blank"
			else:
				
				speech=self.speak(str(ts))
				
				self.ids.t_msg.text=speech
	
	def processRecord(self,record):
		pass
	def processFile(self,filepath):
		self.ids.f_msg.text="Proceesing ..Please wait"
		if self.validatepath(filepath):
			
			extf=os.path.basename(filepath).split(".")
			if extf[-1]=="txt":
				filr=open(filepath,"r")
				txt=filr.read()
				tx=txt
				
				speech=self.speak(tx)
				self.ids.f_msg.text=speech
				
			

			else:
				self.ids.f_msg.text="Select a txt file"
		else:
			self.ids.f_msg.text="Select a file"
		
		
				
				
	
		


	def speak(self,msg):
		texts=tts.instance()
		texts.speak(msg)
		return "Start Listening"
		
	
		
	
			 
	

"""
TsStApp, the entry point into the application, a subclass of kivy.app.App. It overide the parent build method with additional that contains the logic of the application. 
"""						
			
class TsStApp(App):
	def build(self):
		return ApScreen()
		
	
	
			 
					
		
			

Factory.register("MsgL",cls=MsgLabel)		
Factory.register("Load",cls=LoadEncFile)

	

if __name__=="__main__":
		TsStApp().run()
		
		
		
	
	
	

		
		