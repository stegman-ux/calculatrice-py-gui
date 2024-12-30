import tkinter as tk

# made by intrable 
# bad script




def addition():
    nombre1 = float(entry_addition.get())  # j'utilise la data type float pour accepter les nombre décimaux (exemple : 1.5). tandis que la data type int n'accepte pas les chiffres décimaux
    nombre2 = float(entry_addition2.get())
    resultat = nombre1 + nombre2
    addition_text.delete(1.0,tk.END)
    addition_text.insert(tk.END,resultat)
    





gui = tk.Tk()
gui.title("Calculatrice-gui")
gui.geometry("1700x1500")



########################################################################################### addition
label_addition = tk.Label(gui,text="ADDITION:")
label_addition.pack()

label_addi = tk.Label(gui,text="Premier nombre à additioner:",bg="yellow")
label_addi.pack()

entry_addition = tk.Entry(gui,width=5)
entry_addition.pack()

label_addit = tk.Label(gui,text="Deuxieme nombre à additioner:",bg="yellow")
label_addit.pack()

entry_addition2 = tk.Entry(gui,width=5)
entry_addition2.pack()



Button_addition = tk.Button(gui,text="Calculer",command=addition,bg="lightblue")
Button_addition.pack()

addition_text = tk.Text(gui,width=30,height=5)
addition_text.pack()



txt_pour_separer = tk.Label(gui,text="...............................................................................................................................................................................",bg="black") # pour separer la multiplication et l'adition. pour faire + jolie
txt_pour_separer.pack()
############################################################################################################################### multiplication


def multiplication():
    nombre1 = float(entry_multiplication.get())
    nombre2 = float(multiplication_addition2.get())
    resultat = nombre1 * nombre2
    multiplication_text.delete(1.0,tk.END)
    multiplication_text.insert(tk.END,resultat)


label_multi2 = tk.Label(gui,text="MULTIPLICATION:")
label_multi2.pack()

label_multi = tk.Label(gui,text="Premier nombre à multiplier:",bg="yellow")
label_multi.pack()

entry_multiplication = tk.Entry(gui,width=5)
entry_multiplication.pack()

label_multiplication = tk.Label(gui,text="Deuxieme nombre à multiplier::",bg="yellow")
label_multiplication.pack()

multiplication_addition2 = tk.Entry(gui,width=5)
multiplication_addition2.pack()



Button_multiplication = tk.Button(gui,text="Multiplier",command=multiplication,bg="lightblue")
Button_multiplication.pack()

multiplication_text = tk.Text(gui,width=30,height=5)
multiplication_text.pack()






txt_pour_separer2 = tk.Label(gui,text="...............................................................................................................................................................................",bg="black") # pour separer la multiplication et l'adition. pour faire + jolie
txt_pour_separer2.pack()


############################################################### SOUSTRACTION


def soustraction():
    nombre1 = float(entry_soustractio.get())
    nombre2 = float(entry_soustraction.get())
    resultat = nombre1 - nombre2
    soustraction_text.delete(1.0,tk.END)
    soustraction_text.insert(tk.END,resultat)


label_soustraction2 = tk.Label(gui,text="SOUSTRACTION:")
label_soustraction2.pack()

label_sou = tk.Label(gui,text="Premier nombre à soustraire:",bg="yellow")
label_sou.pack()

entry_soustractio = tk.Entry(gui,width=5)
entry_soustractio.pack()

label_soustraction = tk.Label(gui,text="Deuxieme nombre à soustraire:",bg="yellow")
label_soustraction.pack()

entry_soustraction = tk.Entry(gui,width=5)
entry_soustraction.pack()



Button_soustraction = tk.Button(gui,text="Soustraire",command=soustraction,bg="lightblue")
Button_soustraction.pack()

soustraction_text = tk.Text(gui,width=30,height=5)
soustraction_text.pack()

txt_pour_separer3 = tk.Label(gui,text="...............................................................................................................................................................................",bg="black") # pour separer la multiplication et l'adition. pour faire + jolie
txt_pour_separer3.pack()

######################################################################## division


def division():
    nombre1 = float(entry_division.get())
    nombre2 = float(entry_division2.get())
    resultat = nombre1 / nombre2
    division_text.delete(1.0,tk.END)
    division_text.insert(tk.END,resultat)


label_division = tk.Label(gui,text="DIVISION:")
label_division.pack()

label_divi = tk.Label(gui,text="Premier nombre à diviser:",bg="yellow")
label_divi.pack()

entry_division = tk.Entry(gui,width=5)
entry_division.pack()

label_division2 = tk.Label(gui,text="Deuxieme nombre à diviser:",bg="yellow")
label_division2.pack()

entry_division2 = tk.Entry(gui,width=5)
entry_division2.pack()



Button_division = tk.Button(gui,text="Diviser",command=division,bg="lightblue")
Button_division.pack()

division_text = tk.Text(gui,width=30,height=5)
division_text.pack()





gui.mainloop()