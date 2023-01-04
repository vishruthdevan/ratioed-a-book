# TODO create an algorithm from the following method of finding fractions from decimals
# https://math.stackexchange.com/questions/1981310/how-to-find-fraction-from-decimal

from math import floor
from decimal import Decimal
import decimal

precision = 221
context = decimal.Context(prec=precision)
decimal.setcontext(context)
N = Decimal(0.43078081068076000040079082084076000072082000082072076079075088000067084076076088000083068087083000078069000083071068000079081072077083072077070000064077067000083088079068082068083083072077070000072077067084082083081088014)

num = 0
den = 0
