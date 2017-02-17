module Lib
    ( hateblo
    ) where

import Text.Pandoc.JSON

hateblo :: IO ()
hateblo = toJSONFilter (behead <$> shiftHeader)
  where behead (Header n _ xs) | n >= 5 = Para xs
        behead x = x

        shiftHeader (Header n attr xs) | n >= 2 = Header (n + 1) attr xs
        shiftHeader x = x
