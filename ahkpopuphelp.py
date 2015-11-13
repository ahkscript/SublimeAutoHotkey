import sublime, sublime_plugin
import os
import re
import json


class AhkPopupHelpCommand(sublime_plugin.TextCommand):
	'''
	Displays a Popup help when the caret is placed on a AutoHotkey command, directive or function
	'''
	def run(self, edit):
		'''
		Runs the AhkPopupHelpCommand class
		'''

		scopes = self.view.scope_name( self.view.sel()[0].begin() )
		if scopes.find('source.ahk') != 0:
			print ('[AHK Popup Help] Not AutoHotkey code')
			return
		if int(sublime.version()) < 3070:
			print ('[AHK Popup Help] Sublime Text version not supported')
			return

		r,c = self.view.rowcol(self.view.sel()[0].begin())
		line = self.view.substr( self.view.line( self.view.sel()[0] ) )

		#fp = re.sub('.*[ \t,=\+\-\*\?\:\(\%\\\/\!\<\>\.]', '', line[0:c])
		fp = re.sub('.*[^a-zA-Z#]', '', line[0:c])
		line = (fp+line[c:]).strip()
		keyword = re.findall('^[a-zA-Z#]+\(?', line)[0].lower()

		folderpath = sublime.packages_path() + '\\AutoHotkey\\'
		if not os.path.isfile(folderpath + 'AutoHotkey.sublime-completions'):
			print ('[AHK Popup Help] Completions file not found')
			return
		ptr = open(folderpath + 'AutoHotkey.sublime-completions')
		obj = json.loads(ptr.read())
		ptr.close()

		display = ''
		if keyword[-1:] == '(':
			keyword += ')'
		for k in obj['completions']:
			if keyword == k['trigger'].lower():
				display = k['contents']
				break

		if display:
			display = re.sub('\}', '', re.sub('\$\{\d\:', '', display))
			self.view.show_popup(display, max_width=900)