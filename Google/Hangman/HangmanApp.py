# File: HangmanCanvas.py
# ------------------------
# This file keeps track of the Hangman display.
import kivy
import os
from pprint import pprint
from inspect import getmembers

from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle, Line
from HangmanLexicon import HangmanLexicon
from HangmanSolver import HangmanSolver

Config.set('graphics', 'resizable', False)

# Constants for the simple version of the picture (in pixels)
SCAFFOLD_HEIGHT = 360
BEAM_LENGTH = 144
ROPE_LENGTH = 18
HEAD_RADIUS = 36
BODY_LENGTH = 144
ARM_OFFSET_FROM_HEAD = 28
UPPER_ARM_LENGTH = 72
LOWER_ARM_LENGTH = 44
HIP_WIDTH = 36
LEG_LENGTH = 108
FOOT_LENGTH = 28


class DrawBoard(Widget):
    lines = {}

    def __init__(self, **kwargs):
        super(DrawBoard, self).__init__(**kwargs)
        self.setPoints()
        self.clearDraw()

    def drawPiece(self, error):
        points = DrawBoard.lines[error]
        with self.canvas:
            Color(1,1,1,1)
            if error == 1:
                Line(circle=points, width=3)
            else:
                Line(points=points, width=3)

    def clearDraw(self):
        with self.canvas:
            Color(0,0,0,1)
            Rectangle(pos=self.pos, size=self.size)
        self.drawPiece(0)       

    def setPoints(self):
        x, y = self.pos
        s_x, s_y = x + 100, y + 50
        
        scaffold_y = s_y + SCAFFOLD_HEIGHT
        scaffold_x = s_x + BEAM_LENGTH
        scaffold_y_end = scaffold_y - ROPE_LENGTH
        bodyCenter_x = s_x + BEAM_LENGTH
        centerHead_y = scaffold_y_end - HEAD_RADIUS
        endHead_y = centerHead_y - HEAD_RADIUS
        endBody_y = endHead_y - BODY_LENGTH
        armBase_y = endHead_y - ARM_OFFSET_FROM_HEAD
        luArm_x = bodyCenter_x - UPPER_ARM_LENGTH
        ruArm_x = bodyCenter_x + UPPER_ARM_LENGTH
        armEnd_y = armBase_y - LOWER_ARM_LENGTH
        luLeg_x = bodyCenter_x - HIP_WIDTH
        ruLeg_x = bodyCenter_x + HIP_WIDTH
        endLeg_y = endBody_y - LEG_LENGTH
        lFoot_x = luLeg_x - FOOT_LENGTH
        rFoot_x = ruLeg_x + FOOT_LENGTH

        DrawBoard.lines = {
            0: [s_x, s_y, s_x, scaffold_y,
                scaffold_x, scaffold_y,
                scaffold_x, scaffold_y_end],
            1: [bodyCenter_x, centerHead_y, HEAD_RADIUS], #circle params
            2: [bodyCenter_x, endHead_y, bodyCenter_x, endBody_y],
            3: [bodyCenter_x, armBase_y, luArm_x, armBase_y, luArm_x, armEnd_y],
            4: [bodyCenter_x, armBase_y, ruArm_x, armBase_y, ruArm_x, armEnd_y],
            5: [bodyCenter_x, endBody_y, luLeg_x, endBody_y,
                luLeg_x, endLeg_y, lFoot_x, endLeg_y],
            6: [bodyCenter_x, endBody_y, ruLeg_x, endBody_y,
                ruLeg_x, endLeg_y, rFoot_x, endLeg_y]
        }

class PlayScreen(GridLayout):

    def __init__(self, **kwargs):
        super(PlayScreen, self).__init__(**kwargs)
        # Set buttons grid
        self.buttonsGrid = GridLayout(pos=(0,0), cols=2,
                                      size_hint_y=None, height=50)
        self.startButton = Button(multiline=False, size_hint_y=None, height=50,
                                  text="Start Game!")
        self.startButton.bind(on_press=self.startGame)
        self.restartButton = Button(multiline=False, size_hint_y=None, height=50,
                                    text="Restart")
        self.restartButton.bind(on_press=self.startGame)
        self.buttonsGrid.add_widget(self.startButton)
        self.buttonsGrid.add_widget(self.restartButton)
        # Set left grid
        self.output = Label(text="Welcome to Hangman!")
        self.input = TextInput(multiline=False, size_hint_y=None, height=30)
        self.input.bind(on_press=self.check)
        self.input.bind(on_text_validate=self.guessLetter) 
        self.leftGrid = GridLayout(pos=(0,0), rows=3)
        self.leftGrid.add_widget(self.output)
        self.leftGrid.add_widget(self.buttonsGrid)
        self.leftGrid.add_widget(self.input)
        # Set right grid
        self.drawBoard = DrawBoard(pos=(self.width/2,50),
                                   size=(self.width/2, self.height))
        # Set main Grid
        self.add_widget(self.leftGrid)
        self.add_widget(self.drawBoard)

    def startGame(self, instance):
        self.solver = HangmanSolver(HangmanLexicon())
        curr = self.solver.getCurrent()
        self.drawBoard.clearDraw()
        self.output.text = \
            "Current puzzle (%i letters):\n\n%s" %(len(curr), curr)

    def guessLetter(self, instance):
        if not hasattr(self, 'solver') or self.solver is None:
            self.output.text = "Start a new game first!"
            return
        gameRes, guessRes, output = self.solver.makeAMove(instance.text)
        self.output.text = output + "\n\n" + self.solver.getCurrent() \
                           + "\n\n" + self.solver.getGuesses()
        instance.text = ''
        self.input.focus = True ## check

        if guessRes == -1:
            self.drawBoard.drawPiece(self.solver.getErrors())

        if gameRes == 1:
            self.output.text = "Congratulations, you won! =D"
            self.solver = None
        if gameRes == -1:
            self.output.text = (
                "That's a shame, you lost! =/\n"
                "Answer was %s" %self.solver.getAnswer())
            self.solver = None

    def check(self, instance):
        pprint(getmembers(instance))


class HangmanApp(App):
    def build(self):
        game = PlayScreen(cols=2, size=(800, 600))
        
        return game

if __name__ == '__main__':
    HangmanApp().run()