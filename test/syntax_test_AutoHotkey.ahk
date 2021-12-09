; SYNTAX TEST "Packages/AutoHotkey/AutoHotkey.sublime-syntax"

; 1 Test overall source match
;^^^^^^^^^^^^^^^^^^^^^^^^^^^^ source.ahk

q := "q `"within`" q" ; Match escaped double-quotes
;    ^^^^^^^^^^^^^^^^ string.quoted.double.ahk
;    ^                punctuation.definition.string.ahk
;                   ^ punctuation.definition.string.ahk
;       ^             constant.character.escape.ahk
;               ^     constant.character.escape.ahk
