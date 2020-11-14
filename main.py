import pandas as pd 

def trapesium(x,a,b,c,d): # Fungsi keanggotaan trapesium
    if ((x<=a) or (x>=d)):
        nilai = 0
    elif ((x>a) and (x<b)):
        nilai = (x-a)/(b-a)
    elif ((x>=b) and (x<=c)):
        nilai = 1
    elif ((x>c) and (x<=d)):
        nilai = -(x-d)/(d-c)

    return nilai

def segitiga(x,a,b,c):
    if ((x<=a) or (x>=c)):
        nilai = 0
    elif ((x>a) and (x<=b)):
        nilai = (x-a)/(b-a)
    elif ((x>b) and (x<=c)):
        nilai = -(x-c)/(c-b)

    return nilai

def rendah(x,nilai_fuzzy): # Variabel linguistik
    a = 0.0
    b = 0.0
    c = 5.0
    d = 8.0
    nilai_fuzzy['rendah'] = round(trapesium(x,a,b,c,d),2)

    return nilai_fuzzy

def sedang(x,nilai_fuzzy): # Variabel linguistik
    a = 5.0
    b = 8.0
    c = 13.0
    nilai_fuzzy['sedang'] = round(segitiga(x,a,b,c),2)
    
    return nilai_fuzzy

def tinggi(x,nilai_fuzzy): # Variabel linguistik
    a = 10.0
    b = 13.0
    c = 20 # c lebih dari nilai maksimum penghasilan agar tidak 0
    d = 20 # d lebih dari nilai maksimum penghasilan agar tidak 0
    nilai_fuzzy['tinggi'] = round(trapesium(x,a,b,c,d),2)

    return nilai_fuzzy

def sedikit(x,nilai_fuzzy): # Variabel linguistik
    a = 0.0
    b = 0.0
    c = 2.0
    d = 3.0
    nilai_fuzzy['sedikit'] = round(trapesium(x,a,b,c,d),2)

    return nilai_fuzzy

def cukup(x,nilai_fuzzy): # Variabel linguistik
    a = 2.0
    b = 3.0
    c = 4.0
    d = 5.0
    nilai_fuzzy['cukup'] = round(trapesium(x,a,b,c,d),2)

    return nilai_fuzzy

def banyak(x,nilai_fuzzy): # Variabel linguistik
    a = 4.0
    b = 5.0
    c = 6.0
    d = 8.0
    nilai_fuzzy['banyak'] = round(trapesium(x,a,b,c,d),2)

    return nilai_fuzzy

def sangat_banyak(x,nilai_fuzzy): # Variabel linguistik
    a = 6.0
    b = 8.0
    c = 12.0 # c dari nilai maksimum pengeluaran agar tidak 0
    d = 12.0 # d dari nilai maksimum pengeluaran agar tidak 0
    nilai_fuzzy['sangat_banyak'] = round(trapesium(x,a,b,c,d),2)

    return nilai_fuzzy

def fuzzification(pengeluaran,penghasilan):
    fuzzy_penghasilan = {}
    fuzzy_pengeluaran = {}
    i = 1
    x = 1
    for data in penghasilan.values:
        fuzzy = {}
        fuzzy_penghasilan[i] = rendah(float(data), fuzzy)
        fuzzy_penghasilan[i] = sedang(float(data), fuzzy)
        fuzzy_penghasilan[i] = tinggi(float(data), fuzzy)
        i+=1
    for data in pengeluaran.values:
        fuzzy = {}
        fuzzy_pengeluaran[x] = sedikit(float(data), fuzzy)
        fuzzy_pengeluaran[x] = cukup(float(data), fuzzy)
        fuzzy_pengeluaran[x] = banyak(float(data), fuzzy)
        fuzzy_pengeluaran[x] = sangat_banyak(float(data), fuzzy)
        x+=1

    return fuzzy_pengeluaran,fuzzy_penghasilan

def inference(nilai_pengeluaran,nilai_penghasilan):
    nilai_kelayakan = {}
    i = 1
    # Conjuction
    while i <=100: 
        layak = {}
        diterima = []
        ditolak = []
        if ((nilai_penghasilan[i]['rendah']!=0) and (nilai_pengeluaran[i]['sedikit']!=0)):
            diterima.append(min(nilai_penghasilan[i]['rendah'],nilai_pengeluaran[i]['sedikit']))

        if ((nilai_penghasilan[i]['rendah']!=0) and (nilai_pengeluaran[i]['cukup']!=0)):
            diterima.append(min(nilai_penghasilan[i]['rendah'],nilai_pengeluaran[i]['cukup']))

        if ((nilai_penghasilan[i]['rendah']!=0) and (nilai_pengeluaran[i]['banyak']!=0)):
            diterima.append(min(nilai_penghasilan[i]['rendah'],nilai_pengeluaran[i]['banyak']))

        if ((nilai_penghasilan[i]['rendah']!=0) and (nilai_pengeluaran[i]['sangat_banyak']!=0)):
            diterima.append(min(nilai_penghasilan[i]['rendah'],nilai_pengeluaran[i]['sangat_banyak']))

        if ((nilai_penghasilan[i]['sedang']!=0) and (nilai_pengeluaran[i]['sedikit']!=0)):
            diterima.append(min(nilai_penghasilan[i]['sedang'],nilai_pengeluaran[i]['sedikit']))

        if ((nilai_penghasilan[i]['sedang']!=0) and (nilai_pengeluaran[i]['cukup']!=0)):
            diterima.append(min(nilai_penghasilan[i]['sedang'],nilai_pengeluaran[i]['cukup']))

        if ((nilai_penghasilan[i]['sedang']!=0) and (nilai_pengeluaran[i]['banyak']!=0)):
            ditolak.append(min(nilai_penghasilan[i]['sedang'],nilai_pengeluaran[i]['banyak']))

        if ((nilai_penghasilan[i]['sedang']!=0) and (nilai_pengeluaran[i]['sangat_banyak']!=0)):
            ditolak.append(min(nilai_penghasilan[i]['sedang'],nilai_pengeluaran[i]['sangat_banyak']))

        if ((nilai_penghasilan[i]['tinggi']!=0) and (nilai_pengeluaran[i]['sedikit']!=0)):
            ditolak.append(min(nilai_penghasilan[i]['tinggi'],nilai_pengeluaran[i]['sedikit']))

        if ((nilai_penghasilan[i]['tinggi']!=0) and (nilai_pengeluaran[i]['cukup']!=0)):
            ditolak.append(min(nilai_penghasilan[i]['tinggi'],nilai_pengeluaran[i]['cukup']))

        if ((nilai_penghasilan[i]['tinggi']!=0) and (nilai_pengeluaran[i]['banyak']!=0)):
            ditolak.append(min(nilai_penghasilan[i]['tinggi'],nilai_pengeluaran[i]['banyak']))

        if ((nilai_penghasilan[i]['tinggi']!=0) and (nilai_pengeluaran[i]['sangat_banyak']!=0)):
            diterima.append(min(nilai_penghasilan[i]['tinggi'],nilai_pengeluaran[i]['sangat_banyak']))

        layak['diterima'] = diterima
        layak['ditolak'] = ditolak
        nilai_kelayakan[i] = layak
        i+=1

    # Disjunction
    for i in nilai_kelayakan: 
         # Mengisi nilai 0 pada array kosong
        if (nilai_kelayakan[i]['ditolak']==[]):
            nilai_kelayakan[i]['ditolak'] = [0]
        elif(nilai_kelayakan[i]['diterima']==[]):
            nilai_kelayakan[i]['diterima'] = [0]
    
        nilai_kelayakan[i]['diterima'] = max(nilai_kelayakan[i]['diterima'])
        nilai_kelayakan[i]['ditolak'] = max(nilai_kelayakan[i]['ditolak'])

    return nilai_kelayakan

def defuzzification(nilai_kelayakan): # Center of Gravity dengan rentang nilai kelayakan [0..100]
    hasil = {}
    for i in nilai_kelayakan:
        if ((nilai_kelayakan[i]['diterima'] !=0) and (nilai_kelayakan[i]['ditolak'] == 0)):
            temp = (60*((60-50)/(80-50))) + (65*((65-50)/(80-50))) +(70+80)*nilai_kelayakan[i]['diterima']
            hasil[i] = round(temp/((60-50)/(80-50))+((65-50)/(80-50))+(nilai_kelayakan[i]['diterima']*2),2)
        elif ((nilai_kelayakan[i]['ditolak'] !=0) and (nilai_kelayakan[i]['diterima'] == 0)):
            temp = (10+20+30+40+50)*nilai_kelayakan[i]['ditolak'] + (60*(-(60-80)/(80-50))) + (65*(-(65-80)/(80-50))) + (70*(-(70-80)/(80-50)))
            hasil[i] = round(temp/(-(60-80)/(80-50))+(-(65-80)/(80-50))+(nilai_kelayakan[i]['ditolak']*5),2)
        else:
            hasil[i] = round(((10+20+30+40+50+60)*nilai_kelayakan[i]['ditolak']) + ((70+80+90+100)*nilai_kelayakan[i]['diterima']) / (6*(nilai_kelayakan[i]['ditolak'])) + (4*(nilai_kelayakan[i]['diterima'])),2)
    return hasil

if __name__=="__main__":
    data_mahasiswa = pd.read_excel('./Mahasiswa.xls')
    penghasilan = pd.DataFrame(data_mahasiswa, columns=['Penghasilan'])
    pengeluaran = pd.DataFrame(data_mahasiswa, columns=['Pengeluaran'])
    
    nilai_pengeluaran, nilai_penghasilan = fuzzification(pengeluaran, penghasilan) # Fuzzification
    nilai_kelayakan = inference(nilai_pengeluaran,nilai_penghasilan) # Inference
    hasil = defuzzification(nilai_kelayakan) # Defuzzification

    layak_beasiswa = sorted(hasil.items(),key=lambda x: x[1])

    print(layak_beasiswa)

    # Buat excel
    excel = []
    for i in range(len(layak_beasiswa)):
        excel.append(layak_beasiswa[i][0])
    myexcel = []
    for i in reversed(excel[-20:]):
        myexcel.append(i)
    df = pd.DataFrame(myexcel)
    df.to_excel("Bantuan.xls",index=False,header=False)

    
    
    
    
    
