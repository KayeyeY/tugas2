# Nama : Kevin Yehezkiel Manurung
# NPM : 2206826974
# Kelas : PBP E

## LINK REPO
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
    * Impor path dari django.urls untuk mendefinisikan pola URL. Nama app_name diberikan untuk memberikan nama unik pada pola URL dalam aplikasi.  
    * Pada direktori proyek, buka file urls.py dan tambahkan 'incude' pada 'from django.urls import path' yang bukan main, lalu tambahkan rute url pada 'urlpatterns'.
    * Run server untuk mengujicoba

- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.    
    * untuk menambahkan item tersebut kita dapat memodifikasi file models dan menambahkan ketentuan di atas beserta dengan tipe itemnya.

-  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML.  
    * Menambahkan function show_main dengan app, name dan class yang akan di return oleh main.html yang sudah dimodifikasi dengan {{name of variables}} di main.html

- Routing urls.py main untuk memetakan fungsi views.py.
    * impor konfigurasi lalu add app_name = 'main' ke urls.py


**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
<img src="diagram/Screenshot 2023-09-13 103337.png">


**Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
- Virtual environment memungkinkan untuk membuat lingkungan kerja yang terisolasi untuk setiap proyek sehinnga proyek tidak akan bentrok atau berinterferensi dengan dependensi proyek lain. Ini penting karena setiap proyek mungkin memerlukan versi yang berbeda dari pustaka tertentu atau memiliki kebutuhan khusus. Kita bisa tetap membuat aplikasi tanpa menggunakan virtual environment namun, sangat disarankan untuk menggunakan virtual environment karena akan mempermudah pengelolaan dependensi, memastikan isolasi proyek yang bersih, dan menghindari potensi masalah yang mungkin muncul karena bentrokan versi dependensi. 


**Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**
- MVC (Model-View-Controller):
    * Dengan MVT, Django memisahkan konsep tampilan (View) dan tampilan (Template) dengan jelas. Ini memungkinkan pengembang untuk merancang tampilan web yang lebih fleksibel dan memisahkan kode logika dari tampilan, sehingga memudahkan pemeliharaan dan pengembangan aplikasi web
- MVT (Model-View-Template):
    * Template berisi markup HTML dengan kode logika yang minimal. Template digunakan untuk menghasilkan tampilan akhir yang akan ditampilkan kepada pengguna. Template terutama digunakan dalam kerangka kerja Django untuk aplikasi web Python.
- MVVM (Model-View-ViewModel):
    * MVVM adalah memisahkan logika bisnis aplikasi dari tampilan sehingga pengembang dapat bekerja secara terpisah pada kedua aspek ini. Ini juga memfasilitasi pengikatan data dua arah, yang memungkinkan perubahan dalam Model secara otomatis tercermin dalam tampilan, dan sebaliknya.

- Perbedaan antara MVC dan MVT memiliki perbedaan di mana MVC controller memiliki peran yang lebih aktif dalam mengontrol aplikasi. sementara MVVM adalah pola desain dengan viewmodel sebagai perantara antara model dan view. MVC dan MVVM sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), sementara MVT khusus untuk pengembangan web dengan Django.





