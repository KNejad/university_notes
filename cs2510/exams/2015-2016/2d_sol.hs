f :: [Char] -> Int

f "0" = 0
f "1" = 1
f "2" = 2
f "3" = 3
f "4" = 4
f "5" = 5
f "6" = 6
f "7" = 7
f "8" = 8
f "9" = 9
f "A" = 10
f "B" = 11
f "C" = 12
f "D" = 13
f "E" = 14
f "F" = 15

f(h:hs) = (16 * (f hs)) + f [h]