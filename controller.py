# Create a Controller class to connect the GUI and the model
from functools import partial
ERROR_MSG = 'ERROR'

class Controller:
    """PyCalc's Controller."""
    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.getDisplayText())
        self._view.setDisplayText(result)
        
    def _calculate_b_B(self):
        
        data = self._view.getDisplayText()
        result = data * 8
        self._view.setDisplayText(data)
        
    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.getDisplayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.getDisplayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        # self._view.buttons['b-B'].clicked.connect(self._calculate_b_B)
        # self._view.buttons['B-b'].clicked.connect(self._calculateResult)
        # self._view.buttons['B-KB'].clicked.connect(self._calculateResult)
        # self._view.buttons['KB-B'].clicked.connect(self._calculateResult)
        # self._view.buttons['KB-MB'].clicked.connect(self._calculateResult)
        # self._view.buttons['MB-KB'].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)