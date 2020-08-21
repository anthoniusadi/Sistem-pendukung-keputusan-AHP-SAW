from tkinter import *
import tkinter.messagebox
from konversi import *

root = Tk()
i=0
root.geometry("1020x650")
name=[]

##! kriteria
# age=[]
# fever=[]
# breath=[]
# how_long=[]
# disease=[]
# cough=[]
pasien=[[]]
txtget=[]
##!event untuk nama
tmp=0
def event_input():
    global i
    txtget.append([])
    txtget[i].append(0)
    ##! fill1 nama
    name.append(fill1.get())
    txtget[i].append(0)
   
   
    #!fill3 sesak nafas 
    temp = fill3.get()
    txtget[i][0]=int(temp)
    txtget[i].append(0)
   
    #!fill4 demam converted!!
    temp=fill4.get() 
    temp=konversi_suhu(int(temp))   
    txtget[i][1]=temp
    txtget[i].append(0) 
   
    #!fill5 batuk kering   
    temp=fill5.get()
    txtget[i][2]=int(temp)
    txtget[i].append(0)

    ##!fill2 umur converted!!
    temp=fill2.get()
    temp=konversi_umur(int(temp))
    txtget[i][3]=temp
    txtget[i].append(0)
    
    #!fill6 lama gejala convert dulu
    temp=fill6.get()    
    temp =  konversi_lama(int(temp))
    txtget[i][4]=temp
    
    #!fill7 penyakit bawaan
    temp=fill7.get()
    txtget[i][5]=int(temp) 

    fill1.delete(0,END)
    fill2.delete(0,END)
    fill3.delete(0,END)
    fill4.delete(0,END)
    fill5.delete(0,END)
    fill6.delete(0,END)
    fill7.delete(0,END)
    tkinter.messagebox.showinfo("Input Data","Successful")
    print("pasien ",i," inserted")
    
    i+=1
    return txtget
##! FUNGSI NORMALISASI 
def normalized(arr):
    hasil_norm=norm(arr)
    print("Hasil normalisasi : ", hasil_norm)
    normalisasi_value=Text(hasil,width=50,height=15,wrap=WORD)
    normalisasi_value.insert(END,hasil_norm)
    normalisasi_value.grid(row=0)
    hasil_saw=saw(hasil_norm)
    tmp=hasil_saw
#    print("Hasil akhir : ", tmp)
    saw_value=Text(hasil,width=50 , height=5,wrap=WORD)
    saw_value.insert(END,hasil_saw)
    saw_value.grid(row=1)
    
    priority={}
    print("tmp 1 = ",tmp[1])
    for num in range (len(name)):
        priority[name[num]]=tmp[num]
    print(priority)
    ranking={k: v for k, v in sorted(priority.items(),reverse=True, key=lambda item: item[1])}
    print(ranking)
    rank_value=Text(rank,width=25,height=15,wrap=WORD)
    rank_value.insert(END,ranking)
    rank_value.grid(row=0)
    return tmp

def show():
    y=Text(txt,width=50,height=15,wrap=WORD)
    x=Text(txt,width=50,height=5,wrap=WORD)
    x.insert(END,name)
    y.insert(END,txtget)
    print(txtget)
    print(name)
    y.grid(row=0)
    x.grid(row=1)

def out():
    pass    
judul = Label(root,text="Program DSS untuk menentukan prioritas pasien Covid-19")
nama = Label(root,text ="Nama")
umur = Label(root,text="Umur")

keterangan = Label(root,text="Silahkan isi gejala")
sesak = Label(root,text="Sesak nafas")
demam = Label(root,text="Demam")
batuk = Label(root,text="Batuk kering")
lama = Label(root,text="Lama gejala")
penyakit = Label(root,text="Penyakit bawaan")

tombol_input = Button(root,text="input data",command=event_input)

keterangan2 = Label(root,text="Lakukan Normalisasi kemudian Hitung")
tombol_norm = Button(root,text="Generate",command=lambda:normalized(txtget))
tombol_hitung = Button(root,text="Exit",command=out)
tombol_show = Button(root,text="tampilkan data pasien",command=show)

fill1=Entry(root)
fill2=Entry(root)
fill3=Entry(root)
fill4=Entry(root)
fill5=Entry(root)
fill6=Entry(root)
fill7=Entry(root)



judul.grid(row=0)
nama.grid(row=1)
umur.grid(row=2)
keterangan.grid(row=3,column=1)
sesak.grid(row=4)
demam.grid(row=5)
batuk.grid(row=6)
lama.grid(row=7)
penyakit.grid(row=8)

tombol_input.grid(row=8,column=2)
keterangan2.grid(row=9,column=0)
tombol_norm.grid(row=10,column=1)
tombol_hitung.grid(row=10,column=2)
tombol_show.grid(row=10,column=0)


fill1.grid(row=1,column=1)
fill2.grid(row=2,column=1)
fill3.grid(row=4,column=1)
fill4.grid(row=5,column=1)
fill5.grid(row=6,column=1)
fill6.grid(row=7,column=1)
fill7.grid(row=8,column=1)
txt=Text(root,width=50,height=15,wrap=WORD)
hasil=Text(root,width=50,height=15,wrap=WORD)
rank=Text(root,width=25,height=15,wrap=WORD)

txt.grid(row=16,column=0)
hasil.grid(row=16,column=1)
rank.grid(row=16,column=2)
root.mainloop()