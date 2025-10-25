-- Paste and Execute Console Command
-- Uses clipboard for JavaScript command input

set delayOne to 0.2
set pageDelay to 2

tell application "Google Chrome" to activate
delay delayOne

tell application "System Events"

	-- Click at coordinates (210,1423) to focus the console
	do shell script "/usr/local/bin/cliclick c:210,1423"
	delay delayOne

	-- Paste the JavaScript command from clipboard
	keystroke "v" using command down
	delay delayOne

	-- Press Enter to execute
	key code 36
	delay pageDelay

end tell

-- Console command executed