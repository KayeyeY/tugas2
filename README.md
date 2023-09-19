# Nama : Kevin Yehezkiel Manurung
# NPM : 2206826974
# Kelas : PBP E

## LINK REPO
LINK REPO : https://github.com/KayeyeY/tugas2.git

### README TUGAS 2
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

### README TUGAS 3
**Apa perbedaan antara form POST dan form GET dalam Django?**
- Form POST maupun form GET untuk mengirim data dari browser ke server, namun keduanya memiliki beberapa perbedaan.
    1. Metode pengiriman data:  
        * POST: Data dikirim sebagai bagian dari body permintaan HTTP, yang tidak terlihat dalam URL.
        * GET: Data dikirimkan sebagai bagian dari URL sebagai parameter query string.
    2. Keamanan:  
        * POST: Cocok untuk mengirim data sensitif atau data yang harus diamankan.
        * GET: Kurang aman karena data terlihat dalam URL dan dapat dilihat oleh pengguna atau pihak ketiga.
    3. Ukuran data:  
        * POST: Tidak ada batasan bawaan pada ukuran data yang dapat dikirimkan dalam form POST.
        * GET: Ada batasan ukuran data dalam form GET (sekitar 2048 karakter).

**Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**
- XML: 
    * Menyusun data dalam hierarki yang sangat fleksibel.
    * Membutuhkan lebih banyak waktu dan sumber daya untuk menguraikan data XML dibandingkan dengan JSON karena struktur markup yang lebih rumit.
    * Berguna untuk konfigurasi aplikasi dan integrasi lintas platform
- JSON:
    * Format yang terdiri dari pasangan nama-kunci dan nilai yang digunakan untuk mengatur data.
    * Diproses lebih efisien oleh browser dan sebagian besar bahasa pemrograman karena formatnya yang kompak dan struktur datanya yang sederhana.
    * Ideal untuk komunikasi web dan API
- HTML:
    * Digunakan untuk membuat konten web yang dapat ditampilkan di browser.
    * Mengatur tampilan dan interaksi konten

**Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**
1. Kompak dan Ringkas
    - JSON memiliki format yang sederhana dan ringkas, yang membuatnya sangat efisien dalam hal penggunaan bandwidth. 
2. Struktur Data yang Mudah Dipahami
    - SON mengadopsi format objek yang mirip dengan banyak bahasa pemrograman, membuatnya mudah dipahami oleh pengembang. 
3. Kecepatan Penguraian (Parsing)
    - Karena struktur data yang sederhana, JSON dapat dengan cepat dan mudah diurai (parsed) oleh browser dan banyak bahasa pemrograman.
4. Kompatibilitas dengan JavaScript
    - JSON dapat langsung diurai menjadi objek JavaScript dalam kode JavaScript di browser.
5. Mendukung Berbagai Jenis Data
    - JSON dapat digunakan untuk mengirimkan berbagai jenis data.
6. Dukungan yang Luas
    - JSON didukung oleh sebagian besar bahasa pemrograman, sehingga memungkinkan interoperabilitas yang lebih baik
7. Dukungan Terintegrasi
    - Banyak perpustakaan (libraries) dan framework di dunia pengembangan web menyediakan dukungan bawaan untuk JSON.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
- Membuat input form untuk menambahkan objek model pada app sebelumnya.
    1. Membuat folder baru `templates` pada root folder dan buat base.html  yang berguna sebagai template dasar.
    2. Ubah `main.html` pada subdirektori `templates` yang ada pada direktori `main`.
    3. Buat berkas baru `forms.py` pada direktori `main` lalu tambahkan objek yang sudah dibuat pada bagian fields
    4. Tambahkan import `from main.forms import ProductForm` dan `from django.urls import reverse` pada `views.py`
    5. Buat fungsi baru create_product dan ubah fungsi show_main. Setelah itu import create product di `urls.py`
    6. Tambahkan path url ke urlpatterns pada `urls.py` di main
    7. Buat berkas HTML `create_product.html` di main/templates. Lalu isi dengan kode yang sesuai

- Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
    1. Buat parameter request `show_xml` dan bua variabel di dalam fungsi yang menyimpan hasil query dari data yang ada di product. Tambahkan return function HttpResponse dan parameter data hasil query.
    2. Import fungsi yang sudah di buat pada urls.py
    3. Tambahkan path url pada urlpatterns untuk mengakses fungsi yang sudah diimpor.
    4. Ulangi langkah 1-3 untuk JSON.
    5. Buka `views.py` pada folder main dan buat fungsi baru "show_xml_by_id" dan "show_json_by_id".
    6. Buat parameter yang menyimpan hasil query dari data dengan id yang ada di product.
    7. Tambahkan "applicaion/xml" untuk XML dan "application/json" untuk JSON.
    8. Impor fungsi yang sudah dibuat pada `urls.py` di folder main.
    9. Tambahkan path url ke dalam urlpatterns agar fungsi yang sudah diimpor bisa diakses.


**Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**
<img src="diagram/Screenshot 2023-09-19 225515.png">
<img src="diagram/Screenshot 2023-09-19 225902.png">
<img src="diagram/Screenshot 2023-09-19 225927.png">
<img src="diagram/Screenshot 2023-09-19 225956.png">
<img src="diagram/Screenshot 2023-09-19 230206.png">








