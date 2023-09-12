
LINK REPO : https://github.com/KayeyeY/tugas2.git

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
- Membuat sebuah proyek Django baru
    * Sesuai dengan tutorial yang diberikan, dengan menginisiasi direktori lokal, kemudian aktifkan virtual environment dengan perintah env\Scripts\activate.bat.
    * Di direktori yang sama, buat berkas requirement.txt dan pasang dependencies, jangan lupa jalankan virtual environment.
    * Buat proyek Django dengan perintah "django-admin startproject (nama direktori)".
    * Pada bagian settings.py tambahkan ["*"] pada allowed host.
    * "python manage.py runserver" untuk menjalankan server Django pada berkas manage.py.

- Membuat aplikasi dengan nama main pada proyek tersebut.
    * "python manage.py startapp main" jalankan perintah pada powershell file.
    * Buka berkas settings.py dan tambahkan 'main' pada variabel installed apps.
    * Buat berkas baru dengan nama "main.html" pada direktori baru dengan nama 'templates' lalu diisi dengan data yang ingin ditampilan pada main.html.

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    * Buat berkas baru dengan nama 'urls.py' di direktori main.   
    from django.urls import path  
    from main.views import show_main  

    app_name = 'main'  

    urlpatterns = [  
        path('', show_main, name='show_main'),  
    ]  
    * Berkas urls.py pada aplikasi main bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main. Impor path dari django.urls untuk mendefinisikan pola URL. Fungsi show_main dari modul main views sebagai tampilan yang akan ditampilkan ketika URL terkait diakses. Nama app_name diberikan untuk memberikan nama unik pada pola URL dalam aplikasi.  
    * Pada direktori proyek, buka file urls.py dan tambahkan 'incude' pada 'from django.urls import path' yang bukan main, lalu tambahkan rute url pada 'urlpatterns'.
    * Run server untuk mengujicoba
- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.  
name sebagai nama item dengan tipe CharField.  
amount sebagai jumlah item dengan tipe IntegerField.  
description sebagai deskripsi item dengan tipe TextField.  
* untuk menambahkan item tersebut kita dapat memodifikasi file models dan menambahkan ketentuan di atas beserta dengan tipe itemnya.
* Cara tersebut juga dapat kita lakukan jika kita ingin menambahkan item - item tambahan dengan tipe yang berbeda.







**Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**
- MVC (Model-View-Controller):
    * (MODEL)
    Mewakili data dan logika bisnis aplikasi. Ini bertanggung jawab untuk mengelola data dan logika yang berkaitan dengan data.
    * (VIEW)
    Bertanggung jawab untuk menampilkan data kepada pengguna. Ini adalah antarmuka pengguna yang berinteraksi dengan pengguna dan menampilkan informasi dari Model.
    * (CONTROLLER)
    Bertindak sebagai perantara antara Model dan View. Ini mengontrol alur aplikasi, menerima input dari pengguna, memproses permintaan, dan memperbarui Model atau View sesuai kebutuhan.
- MVT (Model-View-Template):
    * (MODEL)
    Sama seperti dalam MVC, ini mewakili data dan logika bisnis aplikasi.
    * (VIEW)
    Bertanggung jawab untuk menampilkan data kepada pengguna, sama seperti dalam MVC.
    * (TEMPLATE)
    Template berisi markup HTML dengan kode logika yang minimal. Template digunakan untuk menghasilkan tampilan akhir yang akan ditampilkan kepada pengguna. Template terutama digunakan dalam kerangka kerja Django untuk aplikasi web Python.
- MVVM (Model-View-ViewModel):
    * (MODEL)
    Sama seperti dalam MVC, ini mewakili data dan logika bisnis aplikasi.
    * (VIEW)
    Bertanggung jawab untuk menampilkan data kepada pengguna, tetapi dalam MVVM, View lebih pasif daripada dalam MVC. View hanya berisi tampilan dan tidak memiliki logika bisnis yang signifikan.
    * (TEMPLATE)
    Bertindak sebagai perantara antara Model dan View. Ini mengelola tampilan data yang akan ditampilkan oleh View dan menyediakan metode untuk interaksi dengan Model. ViewModel juga memungkinkan pengikatan data dua arah antara Model dan View.