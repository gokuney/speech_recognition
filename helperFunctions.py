def transcribe(audio , sr , r):
	try:
		print r.recognize_google(audio)
		return [ 1 , r.recognize_google(audio)]
	except sr.UnknownValueError:
		return [ 0 , "Did not get the audio" ]
	except sr.RequestError as e:
		return [0 , "Google Service error"]