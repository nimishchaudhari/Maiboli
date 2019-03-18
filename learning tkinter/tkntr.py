import tkinter as tk

#root widget 
root = tk.Tk()

mar= tk.PhotoImage(file = "marathi-image.jpeg")

window = tk.Label(root, image = mar).pack(side="right")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional imamarge file
formats to be added easily."""
w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")
root.mainloop()


#window = tk.Label(root,text = "Maiboli")

root.mainloop()