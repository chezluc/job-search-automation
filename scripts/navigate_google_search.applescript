set delayOne to 0.2
set pageDelay to 2

-- bring "Google Chrome" to the front
tell application "Google Chrome" to activate
delay delayOne


tell application "System Events"

    do shell script "/usr/local/bin/cliclick c:501,506"
    delay delayOne


    repeat 10 times
        -- page down key
        key code 121
        delay delayOne

    end repeat



    set clicknextX to 568
    set clicknextY to 572

    do shell script "/usr/local/bin/cliclick c:" & clicknextX & "," & clicknextY
    delay delayOne




end tell