#Morse code translation

##How to use the program
It is a Python v3 program. Enter the name of the dictionary file and the morse word and you get the result.

##How the program works
1. We get the list of words from the dictionary file
2. We use a recursive algorithm. We look for all the continuous substrings starting at the first character of the morse word. If the substring corresponds to a morse sign, we add the translated letter to the translation and we continue recursively with the complementary substring. When we are in the situation where all the morse word has been translated (and so the complementary substring is of length 0), we add the translation to the list of translations only if the translation is in the dictionary file. When we initially call the function, we use an empty list of translations and the translation is "".