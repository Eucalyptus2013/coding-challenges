#!/usr/local/bin/python

Morse_encoding={'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', \
                '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z'}


def PossibleTranslations(morse, translation, list_translations, dico):
    if len(morse)==0:
        #The translation is complete, now check the dictionary
        if translation in dico:
            list_translations.append(translation)
    else:
        #We look for all the continuous substrings starting at the first character
        #If the substring corresponds to a morse sign, we continue recursively with the complementary substring 
        for i in range(1,len(morse)+1):
            if morse[:i] in Morse_encoding:
                PossibleTranslations(morse[i:],translation+Morse_encoding[morse[:i]],list_translations,dico)   

               
def get_dict(name_file):
    f=open(name_file,'r')
    words=f.readlines()
    f.close()

    #Text processing
    for i in range(len(words)):
        words[i]=words[i].strip('\n').upper()
        
    return words

        
def PrintPossibleTranslations(morse, dico_file_name):
    temp=[]
    PossibleTranslations(morse,"",temp,get_dict(dico_file_name))

    for translation in temp:
        print(translation)
            
#Main
namefile=input("Enter the name of the dictionary file: ")
morse_input=input("Enter a morse word: ")
PrintPossibleTranslations(morse_input,namefile)


