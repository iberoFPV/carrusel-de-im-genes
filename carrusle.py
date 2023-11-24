from tkinter import *
# Hay que instalar una extension para trabajar con imagenes (Pillow) (Conda install Pillow)
from PIL import ImageTk, Image
# Importamos ttk desde tkinter para mejorar el estilo de los botones
from tkinter import ttk  

root = Tk()
root.title('Imagenes')

# Deshabilitar la capacidad de cambiar el tamaño de la ventana
root.resizable(False, False)
# Cambiar el color de fondo del root a un gris oscuro
root.configure(bg="#2d2d2d") 

# Cargamos las imagenes
img1 = ImageTk.PhotoImage(Image.open('carrusel_de_imagenes/images/image_1.png').resize((300, 700)))
img2 = ImageTk.PhotoImage(Image.open('carrusel_de_imagenes/images/image_2.png').resize((300, 700)))
img3 = ImageTk.PhotoImage(Image.open('carrusel_de_imagenes/images/image_3.png').resize((300, 700)))
img4 = ImageTk.PhotoImage(Image.open('carrusel_de_imagenes/images/image_4.png').resize((300, 700)))
img5 = ImageTk.PhotoImage(Image.open('carrusel_de_imagenes/images/image_5.png').resize((300, 700)))
img6 = ImageTk.PhotoImage(Image.open('carrusel_de_imagenes/images/image_6.png').resize((300, 700)))
img7 = ImageTk.PhotoImage(Image.open('carrusel_de_imagenes/images/image_7.png').resize((300, 700)))
img8 = ImageTk.PhotoImage(Image.open('carrusel_de_imagenes/images/image_8.png').resize((300, 700)))
img9 = ImageTk.PhotoImage(Image.open('carrusel_de_imagenes/images/image_9.png').resize((300, 700)))

# Crearemos una lista con todas las imagenes
lista = [img1, img2, img3, img4, img5, img6, img7, img8, img9]

# Construimos interfaz
l = Label(root, image=img1)
l.grid(row=0, column=0, columnspan=3)

# Cambiamos al tema 'clam'
ttk.Style().theme_use("clam")

# Funciones pressed
def on_enter(event):
    btn_atras.state(['pressed'])

def on_leave(event):
    btn_atras.state(['!pressed'])

# Creamos la función adelante
def adelante(img_num):
    # Definicion de etiquetas de los botones
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget() # Olvida lo que hay en pantalla de root
    l = Label(root, image=lista[img_num])
    btn_atras = ttk.Button(root, text='<--', command=lambda: atras(img_num - 1))
    btn_adelante = ttk.Button(root, text='-->', command=lambda: adelante(img_num + 1))

    # Validacion para no salirse de rango en la ultima imagen
    if img_num == 8:
        btn_adelante = ttk.Button(root, text='N/A', state=DISABLED)

    # Renderizamos los botones
    l.grid(row=0, column=0, columnspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)

# Creamos funcion atras
def atras(img_num):
    # Definicion de etiquetas de los botones
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget() # Olvida lo que hay en pantalla de root
    l = Label(root, image=lista[img_num])
    btn_atras = ttk.Button(root, text='<--', command=lambda: atras(img_num - 1))
    btn_adelante = ttk.Button(root, text='-->', command=lambda: adelante(img_num + 1))

    # Validacion para no salirse de rango en la ultima imagen
    if img_num == 0:
        btn_atras = ttk.Button(root, text='N/A', state=DISABLED)

    # Renderizamos los botones
    l.grid(row=0, column=0, columnspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)

# Estilos de boton
style = ttk.Style()
style.configure("TButton", foreground="White", background="#555555")

# Configurar el color del botón al pasar el ratón sobre él
style.map("TButton",
            background=[('active', '#555555'), ('disabled', '#2d2d2d')],
            foreground=[('active', 'white')])

# Botones
btn_atras = ttk.Button(root, text='N/A', style="TButton", state=DISABLED)
btn_adelante = ttk.Button(root, text='-->', style="TButton", command=lambda: adelante(1))

# Configurar eventos del ratón
btn_atras.bind("<Enter>", on_enter)
btn_atras.bind("<Leave>", on_leave)

btn_atras.grid(row=1, column=0)
btn_adelante.grid(row=1, column=2)



root.mainloop()
