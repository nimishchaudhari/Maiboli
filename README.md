# Maiboli

This repository is the working module of **Maiboli - A multi-linguistic programming language solution**. 
This system is based on Python programming language and it covers up basic libraries required for one to learn programming as a concept, in their native language. This repository hosts the web service (under development) that shall host the same system on a server, allowing users to make ***REST API*** to access data.

This web service was built with the usage of [Swagger UI](https://editor.swagger.io/) which helped me by exporting the specification into a python flask kit.

A research paper sharing the insights of Maiboli as a programming method, can serve for the well being of common individuals not understanding English, but wishing to learn python programming is published [here](https://ieeexplore.ieee.org/document/8973043).

For any queries contact me [here](mailto:nimish.mailbox@gmail.com)
**Requirements:**
=======
## Language Support
- Marathi

In progress:
- Greek
- Yoruba
- Arabic
- Urdu
- Hindi


## Requirements:

For Maiboli solution:
```bash
Python3
Tkinter
```
For Hosting the web service:
```bash
Flask
connexion
pythonutil
setuptools
flask_testing
coverage
nose
pluggy
py
randomize
```

## Sample code:
Task: To do a star pattern using loops

### Marathi
```bash
व्याख्या तारा(न): 
    तोपर्यंत आ in रांग(0, न): 
        तोपर्यंत बा मध्ये रांग(0, आ+1): 
            छापा("* ",शेवट='') 
        छापा("")
न = 5
तारा(न) 
```

### Hindi
```bash
परिभाषा star(x):
    के_लिए i मध्य सीमा(0,x):
        के_लिए j मध्य सीमा(0,i+1):
            छापें("*", समाप्त='')
        छापें("")
x = 5
छापें(star(x))

```


### Français
```bash
fonction star(x):
    pour i dans ensemble(0,x):
        pour j dans ensemble(0,i+1):
            afficher("*", fin='')
        afficher("")
x = 5
afficher(star(x))
```


### Spanish
```bash
def star(x):
    para i en rango(0,x):
        para j en rango(0,i+1):
            imprime("*", fin='')
        imprime("")
x = 5
imprime(star(x))

```


### Urdu
```bash
وضاحت_کریں star(x):
    کے_لئے i اندر سلسلہ(0,x):
        کے_لئے j اندر سلسلہ(0,i+1):
            پرنٹ_کریں("*", ختم_کریں='')
        پرنٹ_کریں("")
x = 5
پرنٹ_کریں(star(x))

```
### German
```bash
funktion star(x):
    fuer i in bereich(0,x):
        fuer j in bereich(0,i+1):
            druck("*", ende='')
        druck("")
x = 5
druck(star(x))
```
### Tamil
```bash
விவரி star(x):
    வரை i இல் சரகம்(0,x):
        வரை j இல் சரகம்(0,i+1):
            அச்சு("*", முடிவு='')
        அச்சு("")
x = 5
அச்சு(star(x))
```
### Yoruba
```bash
itumo star(x):
    fun i ninu larninu(0,x):
        fun j ninu larninu(0,i+1):
            tẹjade("*", ipari='')
        tẹjade("")
x = 5
tẹjade(star(x))
```
### Greek
```bash
def star(x):
    για i στο εύρος(0,x):
        για j στο εύρος(0,i+1):
            Τύπωσε("*", τέλος='')
        Τύπωσε("")
x = 5
Τύπωσε(star(x))
```

The above code is equivalent to this in English:
```python
def star(x):
    for i in range(0,x):
        for j in range(0,i+1):
            print("*", end='')
        print("")
x = 5
print(star(x))
```
Output:
```bash
*
**
***
****
*****
```