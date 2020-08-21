p=[]
normalisasi=[]
bobot_c=[0.15,0.10,0.03,0.23,0.07,0.43]
def konversi_suhu(value):
    hasil = round((((value-36)/(42-36))*100),3)
    return hasil
def konversi_umur(value):
    hasil= round((((value-1)/(80-1))*100),3)
    return hasil
def konversi_lama(value):
    hasil= round((((value-1)/(14-1))*100),3)
    return hasil
def max_c(arr,c):
    temp=[]
    i=0
    for i in range (len(arr)): 
        val= arr[i][c]
        temp.append(val)
    val=max(temp)
    #print("nilai max c adalah",val)
    return val
def norm(arr):
    for x in range(len(arr[0])):
        for i in range (len(arr)):
            c=x
            val=arr[i][c]/max_c(arr,c)
          #  print("norm  : " ,val)
            normalisasi.append([])
            normalisasi[i].append(0)
            normalisasi[i][c] = val
        ##! cleaning data
    for i in range( (len(arr)),((len(arr))*(len(arr[0])))  ):
        normalisasi.pop()
    return normalisasi
def saw(arr,bobot=bobot_c):
    
    for i in range(len(arr)):
        n=0
        for j in range(len(arr[0])):
             n += arr[i][j] * bobot_c[j]
        p.append(n)
        print(p)
    return p

#######!37 37 38 40 39 ###
# a= [[60,16.666,30,49.367,46.153,25],\
#       [50,16.666,20,51.898,92.307,50],\
#         [70,33.333,45,44.303,69.230,25],\
#             [40,66.666,30,32.911,100,0],\
#                 [40,50,70,46.835,84.615,50]]
# #a= [[60,16.666,30,49.367,46.153,25,"a"],[50,16.666,20,51.898,92.307,50,"b"],[70,33.333,45,44.303,69.230,25,"c"],[40,66.666,30,32.911,100,0,"d"],[40,50,70,46.835,84.615,50,"e"]]
# pasien={}
# nama=["a","b","c","d","e"]
# # hsl=max_c1(a)
# # print(hsl,1)  
# hsl=norm(a)
# #print(hsl)
# p=saw(hsl)
# #print(hsl[0][0]*bobot_c[0])
# #print(len(hsl[0]))
# print("Hasil norm = ", hsl)
# print("Hasil SAW = ",p)
# for num in range (len(nama)):
#     pasien[nama[num]]=p[num]

# print(pasien)
# ###! SORTING IN DICTIONARY
# pasien={k: v for k, v in sorted(pasien.items(),reverse=True, key=lambda item: item[1])}
# print(pasien)