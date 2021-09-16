import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calc import Calc

def test_01():
  assert Calc(2,3).add() == 5