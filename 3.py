# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

import math

print('p(k=70) = ', math.factorial(144) / (math.factorial(70) *
      math.factorial(74)) * math.pow(0.5, 70) * math.pow(0.5, 74))
