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

The below codes are equivalent to this English code:
```python
def star(x):
    for i in range(0,x):
        for j in range(0,i+1):
            print("*", end='')
        print("")
x = 5
print(star(x))
```

Hindi
```bash

परिभाषा star(x):
    के_लिए i मध्य सीमा(0,x):
        के_लिए j मध्य सीमा(0,i+1):
            छापें('*', समाप्त='')
        छापें('')
x = 5
छापें(star(x))

```

Marathi
```bash

व्याख्या star(x):
    तोपर्यंत i मध्ये रांग(0,x):
        तोपर्यंत j मध्ये रांग(0,i+1):
            छापा('*', शेवट='')
        छापा('')
x = 5
छापा(star(x))

```

French
```bash

fonction star(x):
    pour i dans ensemble(0,x):
        pour j dans ensemble(0,i+1):
            afficher('*', fin='')
        afficher('')
x = 5
afficher(star(x))

```

Spanish
```bash

def star(x):
    para i en rango(0,x):
        para j en rango(0,i+1):
            imprime('*', fin='')
        imprime('')
x = 5
imprime(star(x))

```

Urdu
```bash

وضاحت_کریں star(x):
    کے_لئے i اندر سلسلہ(0,x):
        کے_لئے j اندر سلسلہ(0,i+1):
            پرنٹ_کریں('*', ختم_کریں='')
        پرنٹ_کریں('')
x = 5
پرنٹ_کریں(star(x))

```

German
```bash

funktion star(x):
    fuer i in bereich(0,x):
        fuer j in bereich(0,i+1):
            druck('*', ende='')
        druck('')
x = 5
druck(star(x))

```

Tamil
```bash

செயல் star(x):
    வரை i இல் சரகம்(0,x):
        வரை j இல் சரகம்(0,i+1):
            அச்சு('*', முடிவு='')
        அச்சு('')
x = 5
அச்சு(star(x))

```

Yoruba
```bash
itumo star(x):
    fun i ninu larin(0,x):
        fun j ninu larin(0,i+1):
            tẹjade("*", ipari='')
        tẹjade("")
x = 5
tẹjade(star(x))
```

Greek
```bash

def star(x):
    για i στο εύρος(0,x):
        για j στο εύρος(0,i+1):
            Τύπωσε('*', τέλος='')
        Τύπωσε('')
x = 5
Τύπωσε(star(x))
```

Output:
```bash
*
**
***
****
*****
```

## Maiboli Frontend (Next.js)

This project includes a Next.js frontend located in the `frontend` directory. This frontend now provides an interactive **Maiboli Playground**.

### Current Functionality Overview

The Maiboli Playground allows users to write Maiboli code in various supported languages (e.g., Marathi, Hindi, French, German, Spanish, Greek, English) and see it translated into Python. The translated Python code can then be executed directly in the browser. This client-side execution is made possible by the Skulpt library, which is an in-browser Python interpreter.

This setup enables the Maiboli Playground to run as a static website, making it easily deployable on platforms like GitHub Pages.

### Key Components

The client-side Maiboli implementation relies on the following core modules within the `frontend/src` directory:
-   `lib/maiboli-dictionary.ts`: Contains the keyword mappings from Maiboli language variants to standard Python keywords. This is the central place for defining language support.
-   `lib/maiboli-translator.ts`: Implements the logic to translate Maiboli code (using the dictionaries) into Python code. It handles string literals and ensures correct keyword substitution.
-   `lib/python-interpreter.ts`: A wrapper service for the Skulpt library, configured to execute Python code in the browser and capture its output or errors.
-   `app/page.tsx`: The main React component that provides the user interface for the Maiboli Playground, including the code editor, language selector, run button, and output display.

### How to Add/Update Languages

Contributions to expand language support are welcome! To add a new language or update an existing one:

1.  Edit the `frontend/src/lib/maiboli-dictionary.ts` file.
2.  To add a new language:
    *   Add a new entry to the main `dictionaries` object. Use a short language code as the key (e.g., `es` for Spanish, `ru` for Russian).
    *   The value should be an object where keys are the Maiboli keywords for your language and values are their corresponding standard Python keywords. Follow the pattern of existing languages like Marathi (`mar`) or French (`fr`).
    ```typescript
    // Example for adding Spanish (es):
    // es: {
    //   'imprime': 'print',
    //   'para': 'for',
    //   'si': 'if',
    //   // ... other keywords
    // },
    ```
3.  To update an existing language, simply modify its keyword mappings within its entry in the `dictionaries` object.
4.  After saving the changes to `maiboli-dictionary.ts`, the new language (or modifications) will automatically be available in the playground's language selector when you run the development server.

### Running Locally

1.  Navigate to the frontend directory:
    ```bash
    cd frontend
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Run the development server:
    ```bash
    npm run dev
    ```
    Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

### Deployment

The Next.js frontend is configured for static export and is automatically deployed to GitHub Pages whenever changes are pushed to the `main` branch.

The deployment is handled by a GitHub Actions workflow defined in `.github/workflows/deploy.yml`.

After the first successful deployment, you will need to configure GitHub Pages in your repository settings:
1. Go to your repository on GitHub.
2. Click on "Settings".
3. In the "Code and automation" section of the sidebar, click on "Pages".
4. Under "Build and deployment", for the "Source", select "GitHub Actions".
5. GitHub should automatically detect the artifact produced by the workflow. Save the changes.
Your site should then be available at `https://<your-username>.github.io/<repository-name>/` (or a custom domain if you have one configured).