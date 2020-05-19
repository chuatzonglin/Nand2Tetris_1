// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(LOOP_CLEAN_SCREEN)
	@i
	M = 0
(LOOP_CLEAR_RAM)
	@8128
	D = A
	@i
	D = D - M
	@LOOP
	D; JEQ
	
	@i
	D = M

	@SCREEN
	A = A + D
	M = 0

	@i
	M = M + 1

	@LOOP_CLEAR_RAM
	0;JMP


(LOOP)
	@KBD
	D = M
	@LOOP
	D; JEQ

	@i
	M = 0
(LOOP_BLACK_SCREEN)
	@8128
	D = A
	@i
	D = D - M
	@SCREEN_BLACKED
	D; JEQ
	
	@i
	D = M

	@SCREEN
	A = A + D
	M = -1

	@i
	M = M + 1

	@LOOP_BLACK_SCREEN
	0;JMP

(SCREEN_BLACKED)

	@KBD
	D = M
	@LOOP
	D; JNE

	@LOOP_CLEAN_SCREEN
	0;JMP