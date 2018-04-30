import sublime, sublime_plugin
import subprocess
import os
import re
from ctypes import *

# The ahkbuild command is called as target by AutoHotkey.sublime-build
class ahkrun(sublime_plugin.WindowCommand):
	def run(self):
		filepath = self.window.active_view().file_name()

		AutoHotKeyExePathList = sublime.load_settings("AutoHotkey.sublime-settings").get("AutoHotKeyExePath")
		AutoHotKeyExePath = ""
		for AutoHotKeyExePath in AutoHotKeyExePathList:
			if os.path.isfile(AutoHotKeyExePath):
				# print ("Found AutoHotKeyExePath=" + AutoHotKeyExePath)
				break
			else:
				# print ("Not Found AutoHotKeyExePath=" + AutoHotKeyExePath)
				continue
		# Also try old settings format where path is stored as a named-key in a dictionary.
		if not os.path.isfile(AutoHotKeyExePath):
			AutoHotKeyExePath = sublime.load_settings("AutoHotkey.sublime-settings").get("AutoHotKeyExePath")["default"]

		cmd = [AutoHotKeyExePath, "/ErrorStdOut", filepath]
		regex = "(.*) \(([0-9]*)\)() : ==> (.*)"
		self.window.run_command("exec", {"cmd": cmd, "file_regex": regex})

class ahkcompile(sublime_plugin.WindowCommand):
	def run(self):
		filepath = self.window.active_view().file_name()

		Ahk2ExePathList = sublime.load_settings("AutoHotkey.sublime-settings").get("Ahk2ExePath")
		Ahk2ExePath = ""
		for Ahk2ExePath in Ahk2ExePathList:
			if os.path.isfile(Ahk2ExePath):
				# print ("Found Ahk2ExePath=" + Ahk2ExePath)
				break
			else:
				# print ("Not Found Ahk2ExePath=" + Ahk2ExePath)
				continue
		# Also try old settings format where path is stored as a named-key in a dictionary.
		if not os.path.isfile(Ahk2ExePath):
			Ahk2ExePath = sublime.load_settings("AutoHotkey.sublime-settings").get("Ahk2ExePath")["default"]

		cmd = [Ahk2ExePath, "/in", filepath]
		self.window.run_command("exec", {"cmd": cmd})

# http://www.autohotkey.com/board/topic/23575-how-to-run-dynamic-script-through-a-pipe/
# The ahkrunpiped command will run the code in the current buffer by piping it as a temporary string to the AutoHotkey.exe executable. This enables you to run and test AutoHotkey scripts without needing to save them to a file first.
class ahkrunpiped(sublime_plugin.TextCommand):
	def get_code(self):
		# check if there's a selection
		code_sel = self.view.substr(self.view.sel()[0])
		if len(code_sel) != 0:
			return {'code': code_sel, "sel": True}

		# return full code if there is no selection
		code_full = self.view.substr(sublime.Region(0, self.view.size()))
		if len(code_full) != 0:
			return {'code': code_full, "sel": False}

		return False


	def run_code(self, code):
		PIPE_ACCESS_OUTBOUND = 0x00000002
		PIPE_UNLIMITED_INSTANCES = 255
		INVALID_HANDLE_VALUE = -1

		pipename = "AHK_" + str(windll.kernel32.GetTickCount())
		pipe = "\\\\.\\pipe\\" + pipename

		__PIPE_GA_ = windll.kernel32.CreateNamedPipeW(c_wchar_p(pipe),
		                                              PIPE_ACCESS_OUTBOUND,
		                                              0,
		                                              PIPE_UNLIMITED_INSTANCES,
		                                              0,
		                                              0,
		                                              0,
		                                              None)

		__PIPE_ = windll.kernel32.CreateNamedPipeW(c_wchar_p(pipe),
		                                           PIPE_ACCESS_OUTBOUND,
		                                           0,
		                                           PIPE_UNLIMITED_INSTANCES,
		                                           0,
		                                           0,
		                                           0,
		                                           None)

		if (__PIPE_ == INVALID_HANDLE_VALUE or __PIPE_GA_ == INVALID_HANDLE_VALUE):
			print("Failed to create named pipe.")
			return False

		pid = subprocess.Popen([self.ahkpath, pipe], cwd=os.path.expanduser("~")).pid
		if not pid:
			print('Could not open file: "' + pipe + '"')
			return False

		windll.kernel32.ConnectNamedPipe(__PIPE_GA_, None)
		windll.kernel32.CloseHandle(__PIPE_GA_)
		windll.kernel32.ConnectNamedPipe(__PIPE_, None)

		script = chr(0xfeff) + code
		written = c_ulong(0)

		fSuccess = windll.kernel32.WriteFile(__PIPE_,
		                                     script,
		                                     (len(script)+1)*2,
		                                     byref(written),
		                                     None)
		if not fSuccess:
			return False

		windll.kernel32.CloseHandle(__PIPE_)
		return pid


class ahkrunpipedCommand(ahkrunpiped):
	def run(self, edit, version='default', pathToAhkExe = 'AHK_L_v1'):
		AutoHotKeyExePathList = sublime.load_settings("AutoHotkey.sublime-settings").get(pathToAhkExe)
		AutoHotKeyExePath = ""
		for AutoHotKeyExePath in AutoHotKeyExePathList:
			if os.path.isfile(AutoHotKeyExePath):
				self.ahkpath = AutoHotKeyExePath
				# print ("Found AutoHotKeyExePath=" + AutoHotKeyExePath)
				break
			else:
				# print ("Not Found AutoHotKeyExePath=" + AutoHotKeyExePath)
				continue
		# For backwards compatability with old User .sublime-settings files, also try old settings format where path is stored as a key-value pair in a dictionary.
		if not os.path.isfile(AutoHotKeyExePath):
			self.ahkpath = sublime.load_settings("AutoHotkey.sublime-settings").get("AutoHotKeyExePath")["default"]

		# Peform case-insensitive search
		re.I
		# Continue only if syntax used is AutoHotkey or Plain text
		if not re.search("(AutoHotkey|AHK|Plain text)", self.view.settings().get('syntax')):
			print("ahkrunpiped[cancelled] - Not an AHK code")
			return False

		filename = self.view.file_name()
		x = self.get_code()
		if filename:
			if x['sel']:
				self.run_code(x['code'])
			else:
				subprocess.Popen([self.ahkpath, filename], cwd=os.path.dirname(filename))
			print("ahkrunpiped[file" +
			     ("/selection] - " if x['sel'] else "] - '") +
			     filename + "'")
		else:
			pid = self.run_code(x['code'])
			print("ahkrunpiped[unsaved" +
			     ("/selection] - " if x['sel'] else "] - ") +
			     str(pid) + "[PID]")

		# cleanup
		if hasattr(self, "ahkpath"): del self.ahkpath