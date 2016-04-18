import speech_recognition as sr;
import helperFunctions as hf;
import datetime as dt
import os
"""
PRE SETUP 
 --- This is required to create files, etc for the process
"""

# create a file for this session

# get time and set it as filename
file = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".CALL_LOG"


#lets wrap the logic into a function to emulate goto functionality

def main(file , sr, hf):

	print "Select type of recognition you want : \n 1. Press 1 for Microphone \n 2. Press 2 for File  "
	# Get input from user

	choice = raw_input("")

	if choice == "1":

		print "You chose mic"

		# Setup the mic 

	 	r = sr.Recognizer()
	 	with sr.Microphone() as source:
	  		print("Hit enter once you are done with the recording \n")
	  		audio = r.listen(source)

	 	# We have the file ready, now call the transcribe function
	 	response = hf.transcribe(audio , sr , r)

	 	# Treat response accordingly 
	 	if response[0] == 1: 
	 		#means success

	 		#append output to file
	 		with open(file , "a") as callLog:
				callLog.write( response[1] +  "\n")
			print "wrote \n"
			print "wrote to file, going back to options \n"
			main(file , sr, hf)


	 		
	  	else:
	 
	 		#means failure
			print "An error occured, error description \n"
	 		print response[1]

	 	# End treat response

	else:

		print "You chose File"

		

		AUDIO_FILE =  os.path.dirname(os.path.realpath('__file__')) + "/" + "sample.wav"
		r = sr.Recognizer()
		with sr.AudioFile(AUDIO_FILE) as source:
			audio = r.record(source) 

		# Audio is ready, now call the transcribe function
		response = hf.transcribe(audio , sr , r)

		if response[0] == 1:

	    	#append output to file
		 	with open(file , "a") as cl:
				cl.write( response[1] + "\n" )
			print "wrote to file, going back to options \n Text was -> " + response[1]
			main(file , sr, hf)

		else:
		
	 		#means failure
			print "An error occured, error description \n"
	 		print response[1]





	 	




# Call the main function 
main(file , sr, hf)
