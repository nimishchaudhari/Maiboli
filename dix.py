#Arrays of dictionary of functions:


# en = ['print', 'for', 'if', 'elif', 'else', 'return', 'input', 'exec', 'float', 'int', 'len', 'max', 'min', 'range', 'round', 'str', 'sum', 'format', 'in', 'True', 'False', 'def', 'and', 'or', 'not', 'as', 'break', 'continue','end']
# mar = ['छापा ', 'तोपर्यंत', 'जर', 'किंवा', 'नाहीतर', 'परत   ', 'माहिती', 'चालवा', 'दशांश', 'पूर्णांक', 'लांबी', 'कमाल', 'किमान', 'रांग ', 'पूर्ण', 'ओळ ', 'बेरीज', 'स्वरूप', 'मध्ये', 'खरे ', 'खोटे ', 'व्याख्या', 'आणि', 'अथवा', 'नाही', 'जसे', 'खंडित', 'चालूठेवणे','शेवट']
# hin = ['छापें','के_लिए ','अगर','अन्यथा','अतिरिक्त','लौटाएं ', 'प्रवेश' ,'निष्पादन ','दशमलव','पूर्णांक','लम्बाई' ,'अधिकतम','न्यूनतम','सीमा','शून्यान्त','श्रृंखला' ,'योग' ,'प्रारूप','मध्य','सत्य','असत्य','परिभाषा','एवं','अथवा','नहीं','जैसे','विराम', 'जारी','समाप्त']
# gr = ['Τύπωσε', 'για', 'εάν', 'αλλιώς_αν', 'τότε', 'επέστρεψε', 'εισαγωγή', 'εκτέλεσε', 'Πραγματικός', 'Ακέραιος', 'len', 'Μέγιστος', 'ελάχιστος', 'εύρος', 'round', 'str', 'άθροισμα', 'format', 'στο', 'αληθής', 'ψευδής', 'def', 'και', 'ή', 'όχι', 'as', 'break', 'συνέχισε','τέλος']
# yrb = ['tẹjade', 'fun', 'ti', 'abiti', 'ajebe', 'dapada', 'agbewọle', 'ṣe', 'leefo', 'odidi', 'gigun', 'opọju', 'okereju', 'larin', 'yika', 'oro', 'aropo', 'soodi', 'ninu', 'looto', 'iro', 'itumo', 'ati', 'tabi', 'kiiṣe', 'bi', 'duro', 'tẹsiwaju', 'ipari']
# #arb = ['طباعة', 'for', 'if', 'elif', 'else', 'return', 'input', 'exec', 'float', 'int', 'len', 'max', 'min', 'range', 'round', 'str', 'sum', 'format', 'in', 'True', 'False', 'def', 'and', 'or', 'not', 'as', 'break', 'continue','end']
# urd = ['پرنٹ_کریں', 'کے_لئے', 'اگر', 'ورنہ_اگر', 'ورنہ', 'واپس', 'درج_کریں', 'چلائیں', 'فلوٹ', 'عدد', 'لمبائ', 'زیادہ_سے_زیادہ', 'کم_اذ_کم', 'سلسلہ', 'تقریباً', 'تار', 'جمح_کریں', 'فارمیٹ', 'اندر', 'درست', 'غلط', 'وضاحت_کریں', 'اور', 'یا', 'نہیں', 'کے_طور_پر', 'توڑیں', 'جاری_رکھیں', 'ختم_کریں']
# tamil= ['அச்சு','வரை ','என்றால்','வேறு','இல்லை_என்றால்','திருப்பவும் ', 'உள்ளீடு' ,'இயங்கு ','மித','எண்','நீளம்' ,'அதிகபட்சம்','குறைந்தபட்சம்','சரகம்','தோராயம்','வார்த்தை','கூட்டு','வடிவம்','இல்','மெய்','பொய்','செயல்','மற்றும்','அல்லது','இல்ல','என','முறிவு', 'தொடர்','முடிவு']
# spanish = ['imprime', 'para', 'si', 'sinosi', 'sino', 'devuelve', 'entrada', 'ejecuta', 'flotante', 'entero', 'largo', 'max', 'min', 'rango', 'redondea', 'str', 'suma', 'formatea', 'en', 'Verdadero', 'Falso', 'def', 'y', 'o', 'no', 'como', 'rompe', 'continua','fin']
# ger = ['druck', 'fuer', 'wenn', 'alternativ', 'sonst', 'ausgabe', 'eingabe', 'ausfuehren', 'dezimalzahl', 'ganze_zahl', 'laenge', 'max', 'min', 'bereich', 'runde', 'zeichenkette', 'summe', 'einsetzen', 'in', 'Wahr', 'Falsch', 'funktion', 'und', 'oder', 'nicht', 'wie', 'abbruch', 'weiter', 'ende']
# fr = ['afficher','pour','si','sinon_si','sinon','retourne','entrer','executer','flotant','entier','longueur','maximum','minimum','ensemble','arrondire','chaine_de_caractere','somme','formater','dans','Vrai','Faux','fonction','et','ou','non','comme','sortir','continuer','fin']
# pol = ['Wyświetl', 'Dla', 'Jeśli', 'Lub_jeśli', 'Jeśli_nie', 'Powróć', 'Zawartość', 'Wykonaj', 'Liczny rzeczywiste', 'Liczby całkowite', 'Długość', 'Max', 'Min', 'Zasięg', 'Zaokrąglenie', 'Napis', 'Suma', 'Format', 'W', 'Prawda', 'Fałsz', 'Definiuj', 'i', 'Lub', 'Nie', 'Jako', 'Przerwa', 'Kontynuuj', 'Koniec']
# ru = ['вывод', 'для', 'если', 'если_же', 'иначе', 'вернуть', 'ввод', 'выполнить', 'float', 'int', 'длина', 'максимум', 'минимум', 'диапозоне', 'округлить', 'строка', 'сумма', 'формат', 'в', 'Правда', 'Ложь', 'функция', 'и', 'или', 'не', 'как', 'прервать', 'пропустить', 'конец']
# mal = ['അച്ചടിക്കുക', 'വേണ്ടി', 'എങ്കിൽ', 'അല്ലെങ്കിൽ', 'അല്ലെങ്കിൽ', 'മടങ്ങുക', 'വിവരങ്ങള്‍', 'നിർവ്വഹിക്കുക', 'ദശാംശം', 'പൂര്‍ണ്ണസംഖ്യ', 'നീളം', 'പരമാവധി', 'കുറഞ്ഞത്', 'ശ്രേണി', 'പരിവൃത്തി', 'വാചകം', 'തുക', 'ഘടന', 'അകത്ത്', 'ശരി', 'തെറ്റ്', 'നിർവചനം', 'ഒപ്പം', 'അഥവാ', 'അല്ലാതെ', 'പോലെ', 'പൊട്ടിക്കുക', 'തുടരുക', 'അവസാനം']
# tamil= ['அச்சு','வரை ','என்றால்','வேறு','இல்லை_என்றால்','திருப்பவும் ', 'உள்ளீடு' ,'இயங்கு ','மித','எண்','நீளம்' ,'அதிகபட்சம்','குறைந்தபட்சம்','சரகம்','தோராயம்','வார்த்தை','கூட்டு','வடிவம்','இல்','மெய்','பொய்','செயல்','மற்றும்','அல்லது','இல்ல','என','முறிவு', 'தொடர்','முடிவு']

#Arrays with adjustments
fr = ['afficher                      ', 'pour                          ', 'si                            ', 'sinon_si                      ', 'sinon                         ', 'retourne                      ', 'entrer                        ', 'executer                      ', 'flotant                       ', 'entier                        ', 'longueur                      ', 'maximum                       ', 'minimum                       ', 'ensemble                      ', 'arrondire                     ', 'chaine_de_caractere           ', 'somme                         ', 'formater                      ', 'dans                          ', 'Vrai                          ', 'Faux                          ', 'fonction                      ', 'et                            ', 'ou                            ', 'non                           ', 'comme                         ', 'sortir                        ', 'continuer                     ', 'fin                           ']

en = ['print                         ', 'for                           ', 'if                            ', 'elif                          ', 'else                          ', 'return                        ', 'input                         ', 'exec                          ', 'float                         ', 'int                           ', 'len                           ', 'max                           ', 'min                           ', 'range                         ', 'round                         ', 'str                           ', 'sum                           ', 'format                        ', 'in                            ', 'True                          ', 'False                         ', 'def                           ', 'and                           ', 'or                            ', 'not                           ', 'as                            ', 'break                         ', 'continue                      ', 'end                           ']

gr = ['Τύπωσε                        ', 'για                           ', 'εάν                           ', 'αλλιώς_αν                     ', 'τότε                          ', 'επέστρεψε                     ', 'εισαγωγή                      ', 'εκτέλεσε                      ', 'Πραγματικός                   ', 'int                           ', 'len                           ', 'Μέγιστος                      ', 'ελάχιστος                     ', 'εύρος                         ', 'round                         ', 'str                           ', 'άθροισμα                      ', 'format                        ', 'στο                           ', 'αληθής                        ', 'ψευδής                        ', 'def                           ', 'και                           ', 'ή                             ', 'όχι                           ', 'as                            ', 'break                         ', 'συνέχισε                      ', 'τέλος                         ']

mar = ['छापा                          ', 'तोपर्यंत                      ', 'जर                            ', 'किंवा                         ', 'नाहीतर                        ', 'परत                           ', 'माहिती                        ', 'चालवा                         ', 'दशांश                         ', 'पूर्णांक                      ', 'लांबी                         ', 'कमाल                          ', 'किमान                         ', 'रांग                          ', 'पूर्ण                         ', 'ओळ                            ', 'बेरीज                         ', 'स्वरूप                        ', 'मध्ये                         ', 'खरे                           ', 'खोटे                          ', 'व्याख्या                      ', 'आणि                           ', 'अथवा                          ', 'नाही                          ', 'जसे                           ', 'खंडित                         ', 'चालूठेवणे                     ', 'शेवट                          ']

hin = ['छापें                         ', 'के_लिए                        ', 'अगर                           ', 'अन्यथा                        ', 'अतिरिक्त                      ', 'लौटाएं                        ', 'प्रवेश                        ', 'निष्पादन                      ', 'दशमलव                         ', 'पूर्णांक                      ', 'लम्बाई                        ', 'अधिकतम                        ', 'न्यूनतम                       ', 'सीमा                          ', 'शून्यान्त                     ', 'श्रृंखला                      ', 'योग                           ', 'प्रारूप                       ', 'मध्य                          ', 'सत्य                          ', 'असत्य                         ', 'परिभाषा                       ', 'एवं                           ', 'अथवा                          ', 'नहीं                          ', 'जैसे                          ', 'विराम                         ', 'जारी                          ', 'समाप्त                        ']

yrb = ['tẹjade                        ', 'fun                           ', 'ti                            ', 'abiti                         ', 'ajebe                         ', 'dapada                        ', 'agbewọle                      ', 'ṣe                            ', 'leefo                         ', 'odidi                         ', 'gigun                         ', 'opọju                         ', 'okereju                       ', 'larin                         ', 'yika                          ', 'oro                           ', 'aropo                         ', 'soodi                         ', 'ninu                          ', 'looto                         ', 'iro                           ', 'itumo                         ', 'ati                           ', 'tabi                          ', 'kiiṣe                         ', 'bi                            ', 'duro                          ', 'tẹsiwaju                      ', 'ipari                         ']

arb = ['طباعة                         ', 'for                           ', 'if                            ', 'elif                          ', 'else                          ', 'return                        ', 'input                         ', 'exec                          ', 'float                         ', 'int                           ', 'len                           ', 'max                           ', 'min                           ', 'range                         ', 'round                         ', 'str                           ', 'sum                           ', 'format                        ', 'in                            ', 'True                          ', 'False                         ', 'def                           ', 'and                           ', 'or                            ', 'not                           ', 'as                            ', 'break                         ', 'continue                      ', 'end                           ']

urd = ['پرنٹ_کریں                     ', 'کے_لئے                        ', 'اگر                           ', 'ورنہ_اگر                      ', 'ورنہ                          ', 'واپس                          ', 'درج_کریں                      ', 'چلائیں                        ', 'فلوٹ                          ', 'عدد                           ', 'لمبائ                         ', 'زیادہ_سے_زیادہ                ', 'کم_اذ_کم                      ', 'سلسلہ                         ', 'تقریباً                       ', 'تار                           ', 'جمح_کریں                      ', 'فارمیٹ                        ', 'اندر                          ', 'درست                          ', 'غلط                           ', 'وضاحت_کریں                    ', 'اور                           ', 'یا                            ', 'نہیں                          ', 'کے_طور_پر                     ', 'توڑیں                         ', 'جاری_رکھیں                    ', 'ختم_کریں                      ']

sp = ['imprime                       ', 'para                          ', 'si                            ', 'sinosi                        ', 'sino                          ', 'devuelve                      ', 'entrada                       ', 'ejecuta                       ', 'flotante                      ', 'entero                        ', 'largo                         ', 'max                           ', 'min                           ', 'rango                         ', 'redondea                      ', 'str                           ', 'suma                          ', 'formatea                      ', 'en                            ', 'Verdadero                     ', 'Falso                         ', 'def                           ', 'y                             ', 'o                             ', 'no                            ', 'como                          ', 'rompe                         ', 'continua                      ', 'fin                           ']

ger = ['druck                         ', 'fuer                          ', 'wenn                          ', 'alternativ                    ', 'sonst                         ', 'ausgabe                       ', 'eingabe                       ', 'ausfuehren                    ', 'dezimalzahl                   ', 'ganze_zahl                    ', 'laenge                        ', 'max                           ', 'min                           ', 'bereich                       ', 'runde                         ', 'zeichenkette                  ', 'summe                         ', 'einsetzen                     ', 'in                            ', 'Wahr                          ', 'Falsch                        ', 'funktion                      ', 'und                           ', 'oder                          ', 'nicht                         ', 'wie                           ', 'abbruch                       ', 'weiter                        ', 'ende                          ']

tam = ['அச்சு                         ', 'வரை                           ', 'என்றால்                       ', 'வேறு                          ', 'இல்லை_என்றால்                 ', 'திருப்பவும்                   ', 'உள்ளீடு                       ', 'இயங்கு                        ', 'மித                           ', 'எண்                           ', 'நீளம்                         ', 'அதிகபட்சம்                    ', 'குறைந்தபட்சம்                 ', 'சரகம்                         ', 'தோராயம்                       ', 'வார்த்தை                      ', 'கூட்டு                        ', 'வடிவம்                        ', 'இல்                           ', 'மெய்                          ', 'பொய்                          ', 'செயல்                         ', 'மற்றும்                       ', 'அல்லது                        ', 'இல்ல                          ', 'என                            ', 'முறிவு                        ', 'தொடர்                         ', 'முடிவு                        ']

pol = ['Wyświetl                      ', 'Dla                           ', 'Jeśli                         ', 'Lub_jeśli                     ', 'Jeśli_nie                     ', 'Powróć                        ', 'Zawartość                     ', 'Wykonaj                       ', 'Liczny rzeczywiste            ', 'Liczby całkowite              ', 'Długość                       ', 'Max                           ', 'Min                           ', 'Zasięg                        ', 'Zaokrąglenie                  ', 'Napis                         ', 'Suma                          ', 'Format                        ', 'W                             ', 'Prawda                        ', 'Fałsz                         ', 'Definiuj                      ', 'i                             ', 'Lub                           ', 'Nie                           ', 'Jako                          ', 'Przerwa                       ', 'Kontynuuj                     ', 'Koniec                        ']

ru = ['вывод                         ', 'для                           ', 'если                          ', 'если_же                       ', 'иначе                         ', 'вернуть                       ', 'ввод                          ', 'выполнить                     ', 'float                         ', 'int                           ', 'длина                         ', 'максимум                      ', 'минимум                       ', 'диапозоне                     ', 'округлить                     ', 'строка                        ', 'сумма                         ', 'формат                        ', 'в                             ', 'Правда                        ', 'Ложь                          ', 'функция                       ', 'и                             ', 'или                           ', 'не                            ', 'как                           ', 'прервать                      ', 'пропустить                    ', 'конец                         ']

mal = ['അച്ചടിക്കുക                   ', 'വേണ്ടി                        ', 'എങ്കിൽ                        ', 'അല്ലെങ്കിൽ                    ', 'അല്ലെങ്കിൽ                    ', 'മടങ്ങുക                       ', 'വിവരങ്ങള്                         ', 'നിർവ്വഹിക്കുക                 ', 'ദശാംശം                        ', 'പൂര്\u200dണ്ണസംഖ്യ                 ', 'നീളം                          ', 'പരമാവധി                       ', 'കുറഞ്ഞത്                      ', 'ശ്രേണി                        ', 'പരിവൃത്തി                     ', 'വാചകം                         ', 'തുക                           ', 'ഘടന                           ', 'അകത്ത്                        ', 'ശരി                           ', 'തെറ്റ്                        ', 'നിർവചനം                       ', 'ഒപ്പം                         ', 'അഥവാ                          ', 'അല്ലാതെ                       ', 'പോലെ                          ', 'പൊട്ടിക്കുക                   ', 'തുടരുക                        ', 'അവസാനം                        ']

class lang_setup():
    list_of_avail_lang = [hin,mar,fr,sp,urd,ger,tam,yrb,gr,tam,pol,ru,mal]
    list_of_lang = ['hin','mar','fr','sp','urd','ger','tam','yrb','gr','tam','pol','ru','mal']
obj = lang_setup()

def select_dictionary(lang):
    if lang in obj.list_of_lang:
        index = obj.list_of_lang.index(lang)
        return obj.list_of_avail_lang[index]
    else:
        return en


def revised_create_spacings(dix): #Dix 1 being the target lang, Dix2 being english
    length = 30
    #print(dix)
    op=[]
    for i in dix:
        diff =length-len(i) 
        if diff>0:
            for _ in range(0,abs(diff)):
                i = i+' '
            #print(i)
            op.append(i)
        elif diff<0:
            print(" Dude, this is a sentennce, won't work over 30 len, you need to re do shit")
        else:
            pass
    return(op)

"""
DEPRECATED
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
"""


