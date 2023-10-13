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


### README TUGAS 4
**Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?**
- Formulir bawaan yang disediakan oleh Django. Formulir ini digunakan untuk membuat formulir pendaftaran (signup) untuk pengguna (user) dalam aplikasi web yang menggunakan Django. Dengan menggunakan `UserCreationForm` kita dapat dengen cepat membuat formulir yang memungkinkan pengguna untuk mendaftar akun dengan nama pengguna (username) dan kata sandi (password), serta memvalidasi data masukan dengan mudah.

- Kelebihan dari `UserCreationForm`:
    1. Mudah digunakan
        - Dapat menggunakannya dengan mudah tanpa perlu menulis kode tambahan untuk membuat formulir pendaftaran dasar.
    2. Validasi Terintegrasi
        - Memiliki validasi bawaan yang bertujuan untuk memeriksa apakah input yang dimasukkan oleh pengguna sesuai dengan ketentuan yang telah ditetapkan, termasuk proses konfirmasi kata sandi.
    3. Fungsionalitas Terkait Pengguna
        - Dapat digunakan untuk mengelola tugas terkait pengguna lainnya, seperti mengubah kata sandi atau alamat email pengguna.

- Kekurangan dari `UserCreationForm`:
    1. Kustomisasi Terbatas
        - Formulir ini menyediakan fitur dasar, dan jika Anda menginginkan formulir pendaftaran yang lebih disesuaikan dengan kebutuhan khusus Anda, Anda harus menambahkan kode tambahan untuk mengadaptasinya.
    2. Terbatas pada Basis Data Bawaan
        - Dibuat dengan fokus pada integrasi dengan model pengguna standar Django. Jika Anda memiliki keperluan yang lebih kompleks atau menggunakan model pengguna yang berbeda, Anda mungkin harus mengkustomisasi atau membuat formulir pendaftaran sesuai dengan kebutuhan Anda.
    3. Kemungkinan Overhead
        - Pada beberapa kesempatan, jika Anda hanya membutuhkan sebagian kecil dari kemampuan yang disediakan oleh UserCreationForm, penggunaannya bisa menjadi berlebihan dan mengakibatkan penambahan kode yang tidak perlu.

**Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**
- Autentikasi : proses verifikasi identitas pengguna yang mencoba mengakses sistem atau aplikasi. Bertujuan untuk memastikan pengguna yang mengklaim identitas adalah identitas mereka yang sebenarnya.
- Otorisasi : Proses yang terjadi setelah pengguna berhasil mengidentifikasi dirinya, yang melibatkan pemberian hak akses kepada pengguna dalam aplikasi berdasarkan peran atau izin yang dimilikinya.  
    
Keduanya penting karena gabungan antara autentikasi dan otorisasi adalah esensial dalam mengembangkan aplikasi web yang aman dan efisien. Autentikasi menegaskan identitas pengguna yang masuk ke dalam aplikasi, sementara otorisasi mengontrol hak akses pengguna agar sesuai dengan peran dan izin yang mereka miliki dalam aplikasi.

**Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**
- Cookies adalah metode penyimpanan data kecil yang dikirim oleh server web ke peramban (browser) pengguna dan disimpan di perangkat klien sebagai file teks. Dalam konteks aplikasi web, cookies digunakan untuk menyimpan informasi simpel yang memungkinkan identifikasi dan pelacakan pengguna selama sesi mereka saat berinteraksi dengan situs web atau aplikasi.

- Django memanfaatkan cookies untuk mengelola data sesi pengguna dengan cara:
    * Penyimpanan Data Sesi : Data sesi pengguna dapat disimpan dalam cookies atau dalam penyimpanan lain yang lebih aman seperti basis data.
    * Penanganan Cookies : Django secara otomatis mengelola cookies yang digunakan untuk menyimpan informasi sesi.
    * Konfigurasi Cookies: Anda dapat mengonfigurasi berbagai aspek cookies sesi dalam pengaturan Django, 
    * Penggunaan Data Sesi: Data sesi pengguna dapat diakses dan dimanipulasi dengan mudah dalam tampilan Django atau dalam kode aplikasi Anda.

**Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**
- Penggunaan cookies dalam pengembangan web dapat menjadi aman jika dikelola dengan baik, namun ada beberapa risiko potensial yang harus diwaspadai. Dengan pengelolaan yang baik dan tindakan keamanan yang tepat, cookies dapat digunakan dengan aman dalam pengembangan web. Namun, selalu penting untuk mempertimbangkan aspek keamanan dan privasi saat merancang dan mengimplementasikan cookies dalam aplikasi web Anda, misalnya seperti menggunakan protokol https, menggunakan atribut secure dan HttpOnly lalu memahami dan mematuhi regulasi privasi data.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
- Buka `views.py` yang ada di main dan buat fungsi `register` dengan parameter `request`.
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```  

- Buat `register.html` pada main/templates lalu diisi dengan kode yang sesuai template.
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

- Impor fungsi yang sudah dibuat dan tambahkan path url ke dalam urlpatterns

- Buat fungsi `login user` dengan parameter `request`. lalu isi dengan kode yang sesuai template dan routing ke url.

- Tambahkan fungsi logout pada `views.py` pada subdirektori `main`.
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

- Tambahkan potongan kode di bawah pada `main.html` dan routing url.
```
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```

- Akun dummy:
    * Aerith : luminous12
    * Palazo : munbazzz3

- Tambahkan user di `models.py`, lalu modifikasi fungsi create_item pada `views.py`. lalu siapkan parameter commit = false.

- Isi bidang user dengan objek User dari nilai balik request.user untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang masuk

- Buka `views.py` pada direktori main dan import `HttpResponseRedirect`, `reverse` dan `datetime`.

- Tambahkan potongan kode `'last_login': request.COOKIES['last_login']` pada fungsi show_main.

- Ubah fungsi logout_user
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

- Pada berkas `main.html` tambahkan potongan kode
```
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

### README TUGAS 5
**Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.**
- Penggunaan Selector Element (h1, div):
    * Penggunaan ini bermanfaat untuk mengidentifikasi dan memilih elemen berdasarkan jenis atau nama elemen HTML yang digunakan. Ini cocok digunakan saat Anda ingin menerapkan gaya atau perubahan tertentu pada semua elemen dengan jenis yang sama, seperti mengubah semua elemen (h1) atau (div).

- Penggunaan Selector Class (nama class):
    * Penggunaan ini berguna untuk memilih elemen berdasarkan nama kelas yang telah diberikan pada elemen-elemen tersebut. Ini berguna ketika Anda ingin mengubah tampilan atau perilaku dari sekelompok elemen yang memiliki class yang sama. Anda dapat mengaplikasikan perubahan dengan mudah ke semua elemen tersebut.

- Penggunaan Selector ID:
    * Penggunaan ini berguna untuk memilih elemen berdasarkan ID unik yang diberikan pada elemen tertentu. Biasanya, ini digunakan ketika Anda perlu menargetkan elemen yang sangat spesifik dan elemen tersebut hanya ada satu kali dalam halaman web. Selector ID digunakan untuk memastikan bahwa perubahan atau manipulasi yang dilakukan hanya berlaku pada elemen yang spesifik tersebut dan tidak digunakan berulang kali.

**Jelaskan HTML5 Tag yang kamu ketahui.**
- `<head>` : Elemen ini digunakan untuk memuat informasi tentang dokumen, seperti judul (title), meta data, dan tautan ke berkas eksternal seperti CSS dan JavaScript.
- `<title>` : Ini adalah tag yang digunakan untuk menentukan judul dokumen yang akan ditampilkan di bilah judul browser.
- `<link>` : Digunakan untuk menautkan dokumen HTML ke berkas-berkas eksternal, seperti berkas CSS.
- `<div>` : Ini adalah elemen umum yang digunakan untuk mengelompokkan dan mengatur konten dalam halaman web.
- `<p>` : Digunakan untuk menampilkan paragraf teks.
- `<a>`: Elemen ini digunakan untuk membuat tautan atau hyperlink ke halaman web lain atau sumber daya lain.
- `<header>`: Digunakan untuk mengelompokkan elemen-elemen yang biasanya berada di bagian atas halaman web, seperti logo, judul, dan menu navigas

**Jelaskan perbedaan antara margin dan padding.**
- Margin digunakan untuk mengatur jarak atau ruang di sekitar elemen, yang memengaruhi jarak antara elemen dan elemen lain di sekitarnya. Ini tidak mempengaruhi tampilan atau isi dari elemen itu sendiri, melainkan hanya menambahkan jarak tambahan di sekelilingnya.

- Sementara itu, padding digunakan untuk mengatur ruang di dalam elemen itu sendiri, yang memengaruhi jarak antara batas elemen dan kontennya. Padding memengaruhi ruang di dalam elemen tersebut, di antara batas elemen dan kontennya sendiri, sehingga mengubah ukuran sebenarnya dari elemen tersebut.

**Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**
1. Pendekatan Desain:
    - Bootstrap: Bootstrap memiliki desain yang telah ditentukan sebelumnya (pre-designed) dengan komponen-komponen UI yang sudah dibuat. 
    - Tailwind CSS: Tailwind CSS adalah framework yang lebih "utility-first." Ini berarti Anda membangun komponen Anda sendiri dengan menggabungkan kelas-kelas utilitas yang tersedia dalam framework.

2. Kompleksitas:
    - Bootstrap: Bootstrap cenderung lebih berisi fitur dan kompleks. Ini menghadirkan komponen-komponen UI yang lengkap dengan desain bawaan.
    - Tailwind CSS: Tailwind CSS lebih ringan dan memberikan Anda kendali yang lebih besar dalam mengatur desain.

3. Kustomisasi:
    - Bootstrap: Kustomisasi dalam Bootstrap memerlukan penyesuaian CSS yang lebih dalam. Mengubah tampilan komponen Bootstrap yang ada bisa lebih rumit.
    - Tailwind CSS: Tailwind CSS dirancang untuk kustomisasi yang mudah. Anda dapat mengubah tampilan komponen dengan menambahkan atau menghapus kelas-kelas utilitas.  

Anda dapat memilih Bootstrap ketika Anda membutuhkan desain yang dapat dibangun dengan cepat menggunakan komponen UI yang sudah tersedia, terutama untuk proyek-proyek yang memerlukan tampilan yang sudah ditentukan sebelumnya dan memiliki batasan waktu. Di sisi lain, Tailwind CSS cocok digunakan ketika Anda memerlukan fleksibilitas yang tinggi dalam merancang desain yang sangat kustom sesuai dengan kebutuhan proyek Anda. 

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
- Menambahkan kode pada `<head>` di `base.hmtl`:
        ```<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">```
- Modifikasi `create.product`, `edit_product`, `login`, `main` dan `register` untuk memperbagus tampilan, seperti menggunakan navbar, cards dan button.
- contoh:
    ```
    {% extends 'base.html' %} 

    {% block content %}

    <nav class="navbar" style="background-color: #e3f2fd;">
        <div class="container-fluid">
        <a class="navbar-brand" href="#">Add New Product</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
            <a class="nav-link active" aria-current="page" href="{% url 'main:show_main'%}">Home</a>
            <a class="nav-link" href="{% url 'main:logout' %}">Logout</a>
            </div>
        </div>
        </div>
    </nav>

    <div class="card border-primary mb-3" style="width: fit-content,">
        <div class="card-body">
            <form method="POST">
                {% csrf_token %}
                <table>
                    {{ form.as_table }}
                    <tr>
                        <td></td>
                        <td>
                            <input class="btn btn-primary" type="submit" value="Add Product">
                        </td>
                    </tr>
                </table>
            </form>
        </div>
    </div>

    {% endblock %}
    ```


### README TUGAS 6
**Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
- Asynchronous Programming (Pemrograman Asinkron):
    1. Tugas-tugas dieksekusi secara bersamaan, tidak perlu menunggu.
    2. Cocok untuk operasi I/O berat seperti jaringan.
    3. Program tetap responsif dan tidak terhenti saat menunggu operasi selesai.

- Synchronous Programming (Pemrograman Sinkron):
    1. Tugas-tugas dieksekusi satu per satu dalam urutan tertentu.
    2. Program menunggu tugas selesai sebelum melanjutkan.
    3. Cocok untuk tugas sederhana yang cepat.

**Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
- Paradigma event-driven programming (pemrograman berbasis peristiwa) adalah sebuah pendekatan dalam pemrograman di mana program merespons peristiwa atau kejadian tertentu yang terjadi, seperti interaksi pengguna, input perangkat, atau pesan sistem. Maksud dari paradigma ini adalah bahwa program tidak berjalan secara linier dari atas ke bawah seperti dalam pemrograman sinkron, melainkan menunggu dan merespons peristiwa yang terjadi. Contohnya dadlam tugas ini adalah `add_product` dan `delete`

**Jelaskan penerapan asynchronous programming pada AJAX.**
- Dalam konteks AJAX, pemrograman asinkron memungkinkan eksekusi operasi seperti pengambilan data dari server untuk berjalan secara mandiri tanpa menghentikan aliran eksekusi kode utama. Hal ini memastikan bahwa aplikasi web dapat tetap merespons dengan cepat dan efisien. Untuk mencapai hal ini, metode yang digunakan melibatkan penggunaan fungsi callback, promise, atau async/await untuk mengelola respon yang diterima dari server.

**Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.**
- Fetch API:
    * Fetch API adalah bagian dari spesifikasi JavaScript yang terbaru dan merupakan metode bawaan dalam browser modern.
    * Ini lebih ringan daripada jQuery karena hanya fokus pada pengambilan dan pengiriman data melalui HTTP, yang membuat ukuran file lebih kecil.
    * Mendukung Promise, sehingga memungkinkan penanganan yang lebih baik terhadap respons asinkron.
    * Lebih modern dan sesuai dengan standar web saat ini.
- jQuery:
    * jQuery adalah library JavaScript yang cukup besar yang memiliki banyak fitur selain AJAX, seperti manipulasi DOM, animasi, dan efek.
    * Memiliki dukungan lintas browser yang baik, yang memudahkan pengembang dalam menangani perbedaan antara browser.
    * Cocok digunakan dalam proyek yang lebih besar dengan banyak fitur, karena dapat menghemat waktu pengembangan.

Jika proyek Anda sederhana dan terutama memerlukan komunikasi data dengan server, menggunakan Fetch API adalah opsi yang optimal. Ini akan membantu mengurangi kelebihan beban dan ukuran keseluruhan kode.

Tetapi, jika Anda sedang mengembangkan proyek yang lebih besar dan memerlukan berbagai fitur, atau jika Anda sudah berpengalaman dengan penggunaan jQuery, maka memilih jQuery mungkin akan menjadi alternatif yang lebih nyaman.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
1. Buat fungsi `add_product_ajax` pada berkas `views.py`
    ```
    @csrf_exempt
    def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user

        new_product = Product(name=name, price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
    ```
    
2. Tambahkan path url dan impor fungsi ke `urls.py
    ```
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax')
    ```

3. Hapus kode table sebelumnya `main.html` dan tambahkan script di bagian bawah file `main.html`
    ```
    <script>
        async function getProducts() {
            return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
        }
        async function refreshProducts() {
        document.getElementById("product_table").innerHTML = ""
        const products = await getProducts()
        let htmlString = `<tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Price</th>
            <th>Description</th>
            <th>Date Added</th>
            <th></th>
        </tr>`
        products.forEach((item) => {
            htmlString += `\n
            <body>
            <tr>
            <td>${item.fields.name}</td>
            <td>
                <a href="decrement/${item.pk}">
                        <button class="btn custom-btn btn-sm">-</button>
                    </a>
                ${item.fields.amount}
                <a href="increment/${item.pk}">
                        <button class="btn custom-btn btn-sm">+</button>
                    </a>
            </td>
            <td>${item.fields.price}</td>
            <td>${item.fields.description}</td>
            <td>
                ${item.fields.date_added}
            </td>
            <td>
                <a href="delete/${item.pk}">
                        <button class="btn custom-btn btn-sm">Delete</button>
                    </a>
                    <a href="edit-product/${item.pk}">
                        <button class="btn custom-btn btn-sm">Edit</button>
                    </a>
                </td>
            </tr>
        </tbody>` 
        })
        
        document.getElementById("product_table").innerHTML = htmlString
    }

    refreshProducts()

    function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
    }

    document.getElementById("button_add").onclick = addProduct
    </script>
    ```

4. Tambahkan modal untuk membuat form menambahkan product.
    ```
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="form" onsubmit="return false;">
                        {% csrf_token %}
                        <div class="mb-3">
                            <label for="name" class="col-form-label">Name:</label>
                            <input type="text" class="form-control" id="name" name="name"></input>
                        </div>
                        <div class="mb-3">
                            <label for="price" class="col-form-label">Price:</label>
                            <input type="number" class="form-control" id="price" name="price"></input>
                        </div>
                        <div class="mb-3">
                            <label for="amount" class="col-form-label">Amount:</label>
                            <input type="number" class="form-control" id="amount" name="amount"></input>
                        </div>
                        <div class="mb-3">
                            <label for="description" class="col-form-label">Description:</label>
                            <textarea class="form-control" id="description" name="description"></textarea>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                </div>
            </div>
        </div>
    </div>

    ```

5. Tambahkan button untuk tombol ajax add product.
    ```
    <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
            </div>
    ```