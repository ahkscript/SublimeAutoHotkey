; Inspired from Context Sensitive Help in Any Editor -- by Rajat
; https://www.autohotkey.com/docs/scripts/ContextSensitiveHelp.htm
C_Cmd = %1%
If (!C_Cmd)
	Exit

IfWinNotExist, AutoHotkey Help
{
	; Determine AutoHotkey's location:
	RegRead, ahk_dir, HKEY_LOCAL_MACHINE, SOFTWARE\AutoHotkey, InstallDir
	if ErrorLevel  ; Not found, so look for it in some other common locations.
	{
		if A_AhkPath
			SplitPath, A_AhkPath,, ahk_dir
		else IfExist ..\..\AutoHotkey.chm
			ahk_dir = ..\..
		else IfExist %A_ProgramFiles%\AutoHotkey\AutoHotkey.chm
			ahk_dir = %A_ProgramFiles%\AutoHotkey
		else
		{
			MsgBox Could not find the AutoHotkey folder.
			return
		}
	}
	Run %ahk_dir%\AutoHotkey.chm
	WinWait AutoHotkey Help
}
; The above has set the "last found" window which we use below:
WinActivate
WinWaitActive
StringReplace, C_Cmd, C_Cmd, #, {#}
SendInput, !n{home}+{end}%C_Cmd%{enter}
return
