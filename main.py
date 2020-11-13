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
    c = 10.0
    d = 13.0
    nilai_fuzzy['sedang'] = round(trapesium(x,a,b,c,d),2)
    
    return nilai_fuzzy

def tinggi(x,nilai_fuzzy): # Variabel linguistik
    a = 10.0
    b = 13.0
    c = 20 # lebih dari nilai maksimum penghasilan data mahasiswa agar tidak 0
    d = 20 # lebih dari nilai maksimum penghasilan data mahasiswa agar tidak 0
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
    c = 12.0 # lebih dari nilai maksimum pengeluaran data mahasiswa agar tidak 0
    d = 12.0 # lebih dari nilai maksimum pengeluaran data mahasiswa agar tidak 0
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
        if (nilai_kelayakan[i]['ditolak']==[]): # Fill empty value
            nilai_kelayakan[i]['ditolak'] = [0]
        elif(nilai_kelayakan[i]['diterima']==[]): # Fill empty value
            nilai_kelayakan[i]['diterima'] = [0]

        nilai_kelayakan[i]['diterima'] = max(nilai_kelayakan[i]['diterima'])
        nilai_kelayakan[i]['ditolak'] = max(nilai_kelayakan[i]['ditolak'])

    return nilai_kelayakan

# def defuzzification(nilai_kelayakan):
#     return 

# def rumus(l, tl):
#     return ((tl * 35) + (l * 70)) / (tl + l)

if __name__=="__main__":
    data_mahasiswa = pd.read_excel('./Mahasiswa.xls')
    penghasilan = pd.DataFrame(data_mahasiswa, columns=['Penghasilan'])
    pengeluaran = pd.DataFrame(data_mahasiswa, columns=['Pengeluaran'])
    
    nilai_pengeluaran, nilai_penghasilan = fuzzification(pengeluaran, penghasilan)
    nilai_kelayakan = inference(nilai_pengeluaran,nilai_penghasilan)
    #hasil = defuzzification(nilai_kelayakan)
    
    
    
