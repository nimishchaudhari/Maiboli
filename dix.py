#Python file that has two lists that work as the dictionary
en = ['print', 'for     ', 'if', 'elif ', 'else  ', 'return', 'input ', 'exec ', 'float', 'int     ', 'len  ', 'max ', 'min  ', 'range', 'round', 'str', 'sum  ', 'format', 'in   ', 'True', 'False', 'def     ', 'and', 'or  ', 'not ', 'as ', 'break', 'continue ','end ']
en_pure = ['print', 'for', 'if', 'elif', 'else', 'return', 'input', 'exec', 'float', 'int', 'len', 'max', 'min', 'range', 'round', 'str', 'sum', 'format', 'in', 'True', 'False', 'def', 'and', 'or', 'not', 'as', 'break', 'continue','end']
en_mar = en
mar = ['छापा ', 'तोपर्यंत', 'जर', 'किंवा', 'नाहीतर', 'परत   ', 'माहिती', 'चालवा', 'दशांश', 'पूर्णांक', 'लांबी', 'कमाल', 'किमान', 'रांग ', 'पूर्ण', 'ओळ ', 'बेरीज', 'स्वरूप', 'मध्ये', 'खरे ', 'खोटे ', 'व्याख्या', 'आणि', 'अथवा', 'नाही', 'जसे', 'खंडित', 'चालूठेवणे','शेवट']

#fr = ['imprimer','']

#gr = ['Τύπωσε', 'για', 'εάν', 'αλλιώς_αν', 'τότε', 'επέστρεψε', 'εισαγωγή', 'εκτέλεσε', 'Πραγματικός', 'Ακέραιος', 'len', 'Μέγιστος', 'ελάχιστος', 'εύρος', 'round', 'str', 'άθροισμα', 'format', 'στο', 'αληθής', 'ψευδής', 'def', 'και', 'ή', 'όχι', 'as', 'break', 'συνέχισε','τέλος']
gr = ['Τύπωσε  ', 'για  ', 'εάν  ', 'αλλιώς_αν  ', 'τότε  ', 'επέστρεψε  ', 'εισαγωγή  ', 'εκτέλεσε  ', 'Πραγματικός  ', 'int      ', 'len  ', 'Μέγιστος  ', 'ελάχιστος  ', 'εύρος', 'round', 'str', 'άθροισμα  ', 'format', 'στο  ', 'αληθής  ', 'ψευδής  ', 'def  ', 'και', 'ή  ', 'όχι  ', 'as  ', 'break', 'συνέχισε  ', 'τέλος  '] 
#Greek
# useless one Yoruba - yrb = ['tẹjade', 'fun', 'ti', 'abiti', 'ajebe', 'dapada', 'agbewọle', 'ṣe', 'leefo', 'odidi', 'gigun', 'opọju', 'kereju', 'larin' 'yika' 'okun', 'aropo', 'soodi', 'formati' 'ninu', 'looto', 'iro', 'itumo', 'ati', 'tabi', 'kiiṣe', 'bi', 'duro', 'tẹsiwaju', 'ipari' ]



def create_spacings(dix1,dix2): #Dix 1 being the target lang, Dix2 being english
    index = 0
    for i in dix2:
        diff =len(dix1[index])-len(dix2[index]) 
        if diff<0:
            for x in range(0,abs(diff)):
                dix1[index] = dix2[index]+' '
        elif diff>0:
            for x in range(0,abs(diff)):
                dix1[index] = dix2[index]+' '
        else:
            pass
        index+=1
    print(dix1)
    return(dix1)
