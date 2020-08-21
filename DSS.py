from konversi import *
i=0
state=0
pasien=[]
name=[]
priority={}
#bobot_c=[0.15,0.10,0.03,0.23,0.07,0.43]
def max_c(arr,c):
    temp=[]
    i=0
    for i in range (len(arr)): 
        val= arr[i][c]
        temp.append(val)
    val=max(temp)
    return val



while True:
    
    while(state==0):
        pasien.append([])
        
        pasien[i].append(0)
        
        print("pasien",i+1,"silahkan masukan data gejala")
        nama=input('masukan nama : ')
        sesak=int(input('apakah mengalami sesak nafas? 0-100 : '))
        demam=int(input('berapa suhu badan anda : '))
        demam= konversi_suhu(demam)
        batuk=int(input('apakah mengalami batuk kering? 0-100 : '))
        umur=int(input('masukan umur : '))
        umur= konversi_umur(umur)
        lama=int(input('sudah berapa hari mengalami gejala? : '))
        lama= konversi_lama(lama)
        penyakit=int(input("memiliki penyakit berat dan seberapa parah? 0-100 : "))
        pasien[i].append(0)
        name.append(nama)
        pasien[i][0]=sesak
        pasien[i].append(0)

        pasien[i][1]=demam
        pasien[i].append(0)

        pasien[i][2]=batuk
        pasien[i].append(0)

        pasien[i][3]=umur
        pasien[i].append(0)

        pasien[i][4]=lama
#        pasien[i].append(0)

        pasien[i][5]=penyakit
        

        stop=input(" tekan Y untuk input pasien berikutnya, lainnya untuk melakukan perhitungan alternatif : ")
   
        if(stop=="Y"):
            i+=1
        else:
            state=2

    #print("data pasien")
   
   # print("{},{},{},{},{},{},{}".format(nama,umur,demam,sesak,batuk,lama,penyakit))
    print("daftar pasien = ", pasien)
    print("menghitung")
    hsl=norm(pasien)
    print("hasil norm : ",hsl)
    metode=saw(hsl)
    print("hasil SAW : ",metode)
    print(name)
    print(len(name))
    for num in range (len(name)):
        priority[name[num]]=metode[num]

    print(priority)
    ranking={k: v for k, v in sorted(priority.items(),reverse=True, key=lambda item: item[1])}
    print(ranking)
    c=input("wait")    
  #  saw(arr)