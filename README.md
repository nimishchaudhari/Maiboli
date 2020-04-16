# Maiboli

This repository is the working module of **Maiboli - A multi-linguistic programming language solution**. 
This system is based on Python programming language and it covers up basic libraries required for one to learn programming as a concept, in their native language. This repository hosts the web service (under development) that shall host the same system on a server, allowing users to make ***REST API*** to access data.

This web service was built with the usage of [Swagger UI](https://editor.swagger.io/) which helped me by exporting the specification into a python flask kit.

A research paper sharing the insights of Maiboli as a programming method, can serve for the well being of common individuals not understanding English, but wishing to learn python programming is published [here](https://ieeexplore.ieee.org/document/8973043).

For any queries contact me [here](mailto:nimish.mailbox@gmail.com)
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
```bash
व्याख्या तारा(न): 
    तोपर्यंत आ in रांग(0, न): 
        तोपर्यंत बा मध्ये रांग(0, आ+1): 
            छापा("* ",शेवट='') 
        छापा("")
न = 5
तारा(न) 
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
