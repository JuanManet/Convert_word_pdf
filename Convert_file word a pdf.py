import tkinter as tk
from tkinter import filedialog
from docx2pdf import convert

def convertir_a_pdf():
    archivo = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])

    
    if not archivo:
        return

    
    convert(archivo)

ventana = tk.Tk()
ventana.title("Conversor de .docx a .pdf")

boton = tk.Button(ventana, text="Convertir .docx a .pdf", command=convertir_a_pdf)
boton.pack()

ventana.mainloop()
