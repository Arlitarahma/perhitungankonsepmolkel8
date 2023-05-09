import streamlit as st

st.image('A4458525-070D-4EBE-9C29-57B2DCAAB245.JPG')
tab1,tab2,tab3=st.tabs(['Identitas Kelompok','Materi Konsep Mol','Perhitungan'])

with tab1:
    st.subheader('Oleh Kelompok 8')
    st.subheader('Anggota:')
    
    st.write('1. Allyssa Qutratu''ain (2219031)')

    st.write('2. Arlita Rahma Herdiyana (2219038)')

    st.write('3. Nadya Syaharani Qodriah Darajat (2219122)')

    st.write('4. Nurazizah (2219138)')

    st.write('5. Zahratul Hayati Amalia (2219185)')
    
with tab2:
    st.image('https://i.postimg.cc/hGzq5k30/Screenshot-2023-05-05-161344.png',width=None)
    st.subheader('Pengertian Mol dan Konsep Mol')
    st.write('Mol merupakan jumlah tertentu untuk menyatakan banyaknya suatu zat yang berukuran kecil. Konsep mol merupakan perhitungan kuantitas yang berkaitan dengan jumlah atom, molekul, ion, atau electron dalam suatu zat. Menurut satuan Sistem Internasional (SI), satuan dasar dari kuantitas ini disebut mol. "Satu mol menyatakan jumlah zat suatu sistem yang mengandung sejumlah besaran elementer (atom, molekul, dan ion) yang setara dengan banyaknya atom yang terdapat dalam 12 gram tepat isotop Karbon 12 (C-12)"')
    st.subheader('Volume Mol')
    st.write('Volume molar adalah penentuan mol suatu zat yang berfasa gas')
    st.write(':blue[Hubungan Mol dengan Volume Gas]')
    st.write('Pada suhu dan tekanan tertentu akan selalu berlaku bahwa semakin besar volume suatu gas maka jumlah partikel dalam gas tersebut juga akan semakin banyak yang artinya jumlah mol gas akan semakin besar. Hubungan volume gas dengan mol secara umum ditunjukkan oleh suatu persamaan yang biasa dikenal sebagai persamaan gas ideal. Volume gas sangat dipengaruhi oleh tekanan (P) dan temperatur (T).')
    st.write(':blue[Persamaan Gas Ideal]')
    st.latex(r'PV=nRT')
    st.latex(r'Jumlah\space Mol\space (n)= \dfrac {PV} {RT}')
    st.write('''Keterangan:

P = tekanan (atm);

V = volume (liter);

n = jumlah mol;

R = konstanta gas ideal (0,082 L.atm/mol.K);

T = suhu gas (K)

a. Keadaan STP ((Standard Temperature Pressure)
   
Pada keadaan STP (Standard Temperature Pressure), yaitu pada suhu 0 ⁰C dan tekanan 1 atmosfer, maka volume satu mol gas sembarang adalah 22,4 liter.''')
    st.latex(r'Jumlah\space Mol\space (n) = \dfrac {Volume\space STP\space (L)} {22,4\space (L)}')
    st.write('''b.	Keadaan RTP (Room Temperature and Pressure) 
    
Pada keadaan RTP  (Room Temperature and Pressure), yaitu pada suhu ruangan dan tekanan 1 atmosfer, maka volume satu mol gas sembarang adalah 24 liter.''')
    st.latex(r'Jumlah\space Mol\space (n)= \dfrac {Volume\space RTP\space (L)} {24\space (L)}')
    st.subheader('Massa Molar')
    st.write('''Massa molar adalah massa 1 mol zat sebanyak Ar unsurnya atau Mr senyawanya yang dinyatakan dalam (gram/mol).''')
    st.write(':blue[Hubungan Mol dengan Massa Suatu Zat]')
    st.write('''Satu mol zat apapun menunjukkan jumlah partikel yang sama, tetapi kalau  diukur massanya maka 1 mol zat yang berbeda umumnya memiliki massa yang berbeda.''') 
    st.latex(r'Jumlah\space Mol\space (n)= \dfrac {Massa\space (g)} {Ar/Mr}')
    st.subheader('Jumlah Partikel')
    st.write('Jumlah partikel dalam konsep mol merujuk pada jumlah partikel dalam satu mol suatu zat.')
    st.write(':blue[Hubungan Mol dengan Jumlah Partikel]')
    st.write('Satu mol zat apapun akan memiliki jumlah partikel yang sama, yaitu sebesar 6,02x10²³ partikel.')
    st.latex(r'Jumlah\space Mol\space (n)= \dfrac {Jumlah\space Partikel} {6,02 ×10^{23}}')
    st.subheader('Molaritas')
    st.write('Molaritas merupakan salah satu ukuran konsentrasi larutan. Molaritas suatu larutan menyatakan jumlah mol suatu zat per liter larutan.') 
    st.write(':blue[Hubungan Mol dengan Molaritas]')
    st.write('Banyaknya zat yang terdapat dalam suatu larutan dapat diketahui dengan menggunakan konsentrasi larutan yang dinyatakan dalam molaritas (M). Molaritas menyatakan banyaknya mol zat dalam 1 L larutan.')
    st.latex(r'Jumlah\space Mol\space (n)= {Molaritas\space (M) \cdot Volume\space (L)} ')

with tab3:
    hitung=st.selectbox('Hubungan Mol dengan', ['Volume Gas (L)','Massa (g)','Jumlah Partikel (x)','Molaritas (M)'])
    if hitung=='Volume Gas (L)':
        dihitung1=st.selectbox('Yang Akan Dihitung',['Mol (n)','Volume (L)'])
        if dihitung1=='Mol (n)':
            keadaanmol=st.radio('Keadaan',['Keadaan Standar (STP)','Keadaan Pada Suhu Kamar (RTP)'])
            if keadaanmol=='Keadaan Standar (STP)':
                vmol1=st.number_input(f'Masukkan Volume (L)')
                molstp=vmol1/22.4
                if st.button('Hitung'):
                    st.success(f'Nilai Mol adalah {molstp} Mol')
            elif keadaanmol=='Keadaan Pada Suhu Kamar (RTP)':
                vmol2=st.number_input('Masukkan Volume (L)')
                molrtp=vmol2/24
                if st.button('Hitung'):
                    st.success(f'Nilai Mol adalah {molrtp} Mol')
        elif dihitung1=='Volume (L)':
            keadaanvolume=st.radio('Keadaan',['Keadaan Standar (STP)','Keadaan Pada Suhu Kamar (RTP)'])
            if keadaanvolume=='Keadaan Standar (STP)':
                nstp=st.number_input('Masukkan Mol (n)')
                vstp=nstp*22.4
                if st.button('Hitung'):
                    st.success(f'Nilai Volume adalah {vstp} Liter')
            elif keadaanvolume=='Keadaan Pada Suhu Kamar (RTP)':
                nrtp=st.number_input('Masukkan Mol (n)')
                vrtp=nrtp*24
                if st.button('Hitung'):
                    st.success(f'Nilai Mol adalah {vrtp} Liter')
            
    elif hitung=='Massa (g)':
        dihitung2=st.selectbox('Yang Akan Dihitung',['Mol (n)','Massa (g)'])
        if dihitung2=='Mol (n)':
            m=st.number_input('Masukkan Massa (g)')
            armr1=st.number_input('Masukkan Ar/Mr')
            molmassa=m/armr1
            if st.button('Hitung'):
                    st.success(f'Nilai Mol adalah {molmassa} Mol')
        elif dihitung2=='Massa (g)':
            nmassa=st.number_input('Masukkan Mol (n)')
            armr2=st.number_input('Masukkan Ar/Mr')
            massa=nmassa*armr2
            if st.button('Hitung'):
                    st.success(f'Nilai Massa adalah {massa} gram')
                    
    elif hitung=='Jumlah Partikel (x)':
        dihitung3=st.selectbox('Yang Akan Dihitung',['Mol (n)','Jumlah Partikel (x)'])
        if dihitung3=='Mol (n)':
            x=st.number_input('Masukkan Jumlah partikel')
            moljp=x/(6.02*10**23)
            if st.button('Hitung'):
                    st.success(f'Nilai Mol adalah {moljp} Mol')
        elif dihitung3=='Jumlah Partikel (x)':
            njp=st.number_input('Masukkan Mol (n)')
            jp=njp*(6.02*10**23)
            if st.button('Hitung'):
                    st.success(f'Jumlah Partikel adalah {jp} x')
                
    elif hitung=='Molaritas (M)':
        dihitung4=st.selectbox('Yang Akan Dihitung',['Mol (n)','Molaritas (M)'])
        if dihitung4=='Mol (n)':
            jumlah_digit1=4
            M=st.number_input('Masukkan Molaritas',format='%'+str(jumlah_digit1)+'f')
            vmolaritas1=st.number_input('Masukkan Volume')
            nM=M*vmolaritas1
            if st.button('Hitung'):
                st.success(f'Nilai Mol adalah {nM} Mol')
        elif dihitung4=='Molaritas (M)':
            nmolaritas=st.number_input('Masukkan Mol (n)')
            vmolaritas2=st.number_input('Masukkan Volume (L)')
            molaritas=nmolaritas/vmolaritas2
            if st.button('Hitung'):
                st.success(f'Nilai Molaritas adalah {molaritas} M')
            
        
        