#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.  
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
^Left::
send,{Blind}{Home}
return

^Right::
send,{Blind}{End}
return

^+Left::
send,{Blind}{Shift down}{Home}{Shift up}
return

^+Right::
send,{Blind}{Shift down}{End}{Shift up}
return