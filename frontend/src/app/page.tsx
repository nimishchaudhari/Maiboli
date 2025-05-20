'use client'; // Important for using hooks

import { useState, useEffect } from 'react';
import { dictionaries } from '../lib/maiboli-dictionary'; // Adjusted path
import { translateMaiboliToPython } from '../lib/maiboli-translator'; // Adjusted path
import { executePythonCode } from '../lib/python-interpreter'; // Adjusted path

export default function MaiboliEditorPage() {
  const [maiboliCode, setMaiboliCode] = useState('');
  // Get initial language or set a default
  const languageCodes = Object.keys(dictionaries);
  const [selectedLanguage, setSelectedLanguage] = useState(languageCodes.includes('mar') ? 'mar' : languageCodes[0] || 'en');
  const [output, setOutput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isClient, setIsClient] = useState(false); // To ensure Skulpt only runs client-side

  useEffect(() => {
    setIsClient(true); // Skulpt relies on window object, so only enable execution client-side
  }, []);

  const handleRunCode = async () => {
    if (!isClient) {
      setOutput('Python interpreter is not available during server-side rendering. Please wait a moment.');
      return;
    }
    setIsLoading(true);
    setOutput(''); // Clear previous output

    try {
      const translatedPythonCode = translateMaiboliToPython(maiboliCode, selectedLanguage);
      
      // Initial output shows translated code
      let currentOutput = `Translated Python Code:\n${translatedPythonCode}\n\nRunning Python...\n`;
      setOutput(currentOutput);

      const result = await executePythonCode(translatedPythonCode);

      if (result.error) {
        currentOutput += `\nError (Execution):\n${result.error}`;
      } else {
        currentOutput += `\nOutput:\n${result.output}`;
      }
      setOutput(currentOutput);

    } catch (e: any) {
      // This catch block handles errors from translateMaiboliToPython or other unexpected errors
      setOutput(`Error (Translation/Setup):\n${e.message}`);
    }
    setIsLoading(false);
  };
  
  // Update placeholder text when language changes
  const placeholderText = `# Enter your ${selectedLanguage.toUpperCase()} code here...\n${
    selectedLanguage === 'mar' ? "व्याख्या star(x):\n  तोपर्यंत i मध्ये रांग(0,x):\n    तोपर्यंत j मध्ये रांग(0,i+1):\n      छापा('*', शेवट='')\n    छापा('')\nx = 5\nstar(x)" : 
    selectedLanguage === 'hin' ? "परिभाषा star(x):\n  के_लिए i मध्य सीमा(0,x):\n    के_लिए j मध्य सीमा(0,i+1):\n      छापें('*', समाप्त='')\n    छापें('')\nx = 5\nstar(x)" :
    selectedLanguage === 'fr' ? "fonction star(x):\n  pour i dans ensemble(0,x):\n    pour j dans ensemble(0,i+1):\n      afficher('*', fin='')\n    afficher('')\nx = 5\nstar(x)" :
    "print('Hello, world!')" // Default example
  }`;


  return (
    <main className="flex min-h-screen flex-col items-center p-4 md:p-8 bg-gray-900 text-gray-100">
      <div className="w-full max-w-5xl space-y-6">
        <header className="text-center">
          <h1 className="text-4xl font-bold text-indigo-400">Maiboli Playground</h1>
          <p className="text-gray-400 mt-2">
            Write Maiboli code in your chosen language, see it translated to Python, and run it directly in your browser!
          </p>
        </header>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Left Column: Controls and Maiboli Input */}
          <div className="space-y-6">
            <div>
              <label htmlFor="language-select" className="block text-sm font-medium text-gray-300 mb-1">
                Select Language:
              </label>
              <select
                id="language-select"
                value={selectedLanguage}
                onChange={(e) => setSelectedLanguage(e.target.value)}
                className="block w-full p-3 border border-gray-700 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 bg-gray-800 text-white sm:text-sm"
              >
                {languageCodes.map(langCode => (
                  <option key={langCode} value={langCode}>
                    {langCode.toUpperCase()}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label htmlFor="maiboli-code" className="block text-sm font-medium text-gray-300 mb-1">
                Enter Maiboli Code ({selectedLanguage.toUpperCase()}):
              </label>
              <textarea
                id="maiboli-code"
                rows={15}
                className="block w-full p-3 border border-gray-700 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 bg-gray-800 text-white sm:text-sm font-mono"
                value={maiboliCode}
                onChange={(e) => setMaiboliCode(e.target.value)}
                placeholder={placeholderText}
              />
            </div>
          </div>

          {/* Right Column: Output */}
          <div>
            <label htmlFor="output-display" className="block text-sm font-medium text-gray-300 mb-1">
              Output:
            </label>
            <pre
              id="output-display"
              className="w-full p-3 bg-gray-950 text-white rounded-md shadow-sm min-h-[calc(20rem+70px)] text-sm whitespace-pre-wrap break-words overflow-auto border border-gray-700" // Adjusted min-height and break-words
            >
              {output || "// Output will appear here after running the code."}
            </pre>
          </div>
        </div>

        <button
          onClick={handleRunCode}
          disabled={isLoading || !isClient}
          className="w-full px-6 py-3 text-lg font-semibold text-white bg-indigo-600 border border-transparent rounded-md shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 focus:ring-offset-gray-900 disabled:opacity-60 disabled:cursor-not-allowed transition-colors duration-150"
        >
          {isLoading ? 'Running...' : 'Run Code'}
        </button>
         { !isClient && (
            <p className="text-center text-xs text-yellow-400 mt-2">
                Initializing Python interpreter... If the run button remains disabled, please refresh.
            </p>
        )}
      </div>
      <footer className="mt-12 text-center text-sm text-gray-500">
        <p>&copy; {new Date().getFullYear()} Maiboli Project. Powered by Next.js & Skulpt.</p>
      </footer>
    </main>
  );
}
