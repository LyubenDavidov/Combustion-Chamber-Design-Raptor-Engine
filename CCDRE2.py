# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:17:47 2020

@author: Svejen Davidov
"""

import tkinter as tk
import numpy as np








WIDTH = 600;
HEIGHT = 500;


    

h_c = 4.54*10**3;  #[W/m^2*K]

h_g = 2.28*10**3; #[W/m^2*K]

T_g = 3550; #[K]

T_m = 110; #[K]






T = np.array([])
K = np.array([])


   

    
def smjatane(tt1,kk1,tt2, kk2): 
    global T_f
    T_f = np.array([3550])
    output1.delete(0,10)
    output2.delete(0,10)
    output3.delete(0,10)
    for u in range(0,6):
        tf = T_f[u]
        b = np.array([[h_g*tf],[0.0], [0.0],[h_c*T_m]])              
        A = np.array([[h_g,0,0,1],[(kk1/tt1),-(kk1/tt1),0,-1],[0,(kk2/tt2),-(kk2/tt2),-1],[0,0,h_c,-1]])         
        inv_A = np.linalg.inv(A) #tuka moje da e greshkata
        x = np.dot(inv_A,b)
        T_f = np.append(T_f, float(0.5*T_g+0.5*float(x[0])))
    output1.insert(0, round(float(x[0])))
    output2.insert(0, round(float(x[1])))
    output3.insert(0, round(float(x[2])))
    del T_f

 

    
    
    

    

root = tk.Tk()

root.title('Combustion Chamber Design Raptor Engine')
photo = tk.PhotoImage(file = "logo_small.png")
root.iconphoto(False, photo)

root.geometry("600x500")
root.resizable(0, 0)


canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='space1.png')
background_label=tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)




frame1 = tk.Frame(root, bg = '#3c5bb0', bd=5)
frame1.place(relx=0.95, rely=0.5, relwidth=0.30, relheight=0.5, anchor = 'e')

entry1 = tk.Entry(frame1, font=("Calibri 10"))
entry1.place(relwidth=0.5, relheight=0.075)

label1 = tk.Label(frame1, text = "t1 [m]", bg = '#80c1ff')
label1.place(relx=0.55, relheight=0.075, relwidth=0.45)

entry2 = tk.Entry(frame1, font=("Calibri 10"))
entry2.place(rely=0.2, relwidth=0.5, relheight=0.075)

label2 = tk.Label(frame1, text = "k1 [W/m*K]", bg = '#80c1ff')
label2.place(relx=0.55, rely=0.2, relheight=0.075, relwidth=0.45)


entry3 = tk.Entry(frame1, font=("Calibri 10"))
entry3.place(rely=0.4, relwidth=0.5, relheight=0.075)

label3 = tk.Label(frame1, text = "t2 [m]", bg = '#80c1ff')
label3.place(relx=0.55, rely=0.4, relheight=0.075, relwidth=0.45)

entry4 = tk.Entry(frame1, font=("Calibri 10"))
entry4.place(rely=0.6, relwidth=0.5, relheight=0.075)

label4 = tk.Label(frame1, text = "k2 [W/m*K]", bg = '#80c1ff')
label4.place(relx=0.55, rely=0.6, relheight=0.075, relwidth=0.45)





button = tk.Button(frame1, text = "CALCULATE", command=lambda: smjatane(float(entry1.get()),float(entry2.get()),float(entry3.get()),float(entry4.get())))
button.place(relx=0.05,rely=0.8, relheight=0.1, relwidth=0.9)







lower_frame = tk.Frame(root, bg='#3c5bb0', bd=5)
lower_frame.place(relx=0.05, rely=0.5, relwidth=0.5, relheight=0.5, anchor = 'w')


label = tk.Label(lower_frame, text = "Calculated values in Kelvin", bg = '#bdecfc')
label.place(relx=0.1, rely=0, relheight=0.1, relwidth=0.8)



label = tk.Label(lower_frame, text = "T-wall inside", bg = '#80c1ff')
label.place(relx=0.025, rely=0.2, relheight=0.1, relwidth=0.45)

output1 = tk.Entry(lower_frame, font=("Calibri 12"))
output1.place(relx=0.525, rely=0.2, relheight=0.1, relwidth=0.45)

label = tk.Label(lower_frame, text = "T-wall conctact", bg = '#80c1ff')
label.place(relx=0.025, rely=0.4, relheight=0.1, relwidth=0.45)

output2 = tk.Entry(lower_frame, font=("Calibri 12"))
output2.place(relx=0.525, rely=0.4, relwidth=0.45, relheight=0.1)

label = tk.Label(lower_frame, text = "T-wall outside", bg = '#80c1ff')
label.place(relx=0.025, rely=0.6, relheight=0.1, relwidth=0.45)

output3 = tk.Entry(lower_frame, font=("Calibri 12"))
output3.place(relx=0.525, rely=0.6, relwidth=0.45, relheight=0.1)




lowest_frame = tk.Frame(root, bg='#3c5bb0', bd=5)
lowest_frame.place(relx=0.5, rely=0.95, relwidth=0.9, relheight=0.1, anchor = 's')

label = tk.Label(lowest_frame, text = "Important notice: t1,k1 represent the inner material\n Don't put 0 or negative values", bg = '#80c1ff')
label.place(relheight=1, relwidth=1)





root.mainloop()
