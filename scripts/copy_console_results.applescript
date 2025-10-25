set delayOne to 0.2
set pageDelay to 2

-- bring "Google Chrome" to the front
tell application "Google Chrome" to activate
delay delayOne



tell application "System Events"
	

	
	do shell script "/usr/local/bin/cliclick rc:175,865"
	delay delayOne
	
	-- type the following: copy
	set emailtext to "copy"
	repeat with i from 1 to count characters of emailtext
		keystroke (character i of emailtext)
		delay 0.07
	end repeat
	delay delayOne
	
	-- enter key
	key code 36
	delay delayOne
	
	
	
	
end tell