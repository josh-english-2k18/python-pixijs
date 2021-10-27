#
# python-experiment.py
#
# Experiment to determine if a python transpiler can work with PixiJS.
#

class GameEngine:
    def __init__(self):
        self.pixijs = __new__ (PIXI.Application())
        document.body.appendChild(self.pixijs.view)
        self._addDisplayText()

    def handle(self):
        return self.pixijs

    def test(self):
        #document.getElementById('test').innerHTML = self.pixijs
        document.getElementById('test').innerHTML = 'PixiJS'

    def _font(self):
        font = {}
        font.fontFamily = 'Arial'
        font.fontSize = 18
        font.fill = 0x2A5FFF
        font.align = 'center'
        return font

    def _addDisplayText(self):
        self.displayText = __new__ (PIXI.Text('(empty)', self._font()))
        self.pixijs.stage.addChild(self.displayText);

    def setDisplayText(self, text=''):
        self.displayText.text = text

engine = GameEngine()

