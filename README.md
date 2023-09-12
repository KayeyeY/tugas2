
LINK REPO : https://github.com/KayeyeY/tugas2.git

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
- Membuat sebuah proyek Django baru, 
    * Sesuai dengan tutorial yang diberikan, dengan menginisiasi direktori lokal, kemudian aktifkan virtual environment dengan perintah env\Scripts\activate.bat.
    * Di direktori yang sama, buat berkas requirement.txt dan pasang dependencies, jangan lupa jalankan virtual environment.
    * Buat proyek Django dengan perintah "django-admin startproject (nama direktori)".
    * Pada bagian settings.py tambahkan ["*"] pada allowed host.
    * 





**Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**
- MVC (Model-View-Controller):
    (MODEL)
    Mewakili data dan logika bisnis aplikasi. Ini bertanggung jawab untuk mengelola data dan logika yang berkaitan dengan data.
    (VIEW)
    Bertanggung jawab untuk menampilkan data kepada pengguna. Ini adalah antarmuka pengguna yang berinteraksi dengan pengguna dan menampilkan informasi dari Model.
    (CONTROLLER)
    Bertindak sebagai perantara antara Model dan View. Ini mengontrol alur aplikasi, menerima input dari pengguna, memproses permintaan, dan memperbarui Model atau View sesuai kebutuhan.
- MVT (Model-View-Template):
    (MODEL)
    Sama seperti dalam MVC, ini mewakili data dan logika bisnis aplikasi.
    (VIEW)
    Bertanggung jawab untuk menampilkan data kepada pengguna, sama seperti dalam MVC.
    (TEMPLATE)
    Template berisi markup HTML dengan kode logika yang minimal. Template digunakan untuk menghasilkan tampilan akhir yang akan ditampilkan kepada pengguna. Template terutama digunakan dalam kerangka kerja Django untuk aplikasi web Python.
- MVVM (Model-View-ViewModel):
    (MODEL)
    Sama seperti dalam MVC, ini mewakili data dan logika bisnis aplikasi.
    (VIEW)
    Bertanggung jawab untuk menampilkan data kepada pengguna, tetapi dalam MVVM, View lebih pasif daripada dalam MVC. View hanya berisi tampilan dan tidak memiliki logika bisnis yang signifikan.
    (TEMPLATE)
    Bertindak sebagai perantara antara Model dan View. Ini mengelola tampilan data yang akan ditampilkan oleh View dan menyediakan metode untuk interaksi dengan Model. ViewModel juga memungkinkan pengikatan data dua arah antara Model dan View.