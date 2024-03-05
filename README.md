# Laporan Proyek Machine Learning - Muhammad Adin Palimbani
>### ***"Job Recommender System "***

## Project Overview
Sejak pandemi COVID-19 terjadi di tahun 2020, sebagian besar negara mengahadapi masalah akut dalam menyediakan pekerjaan bagi kaum muda. Penurunan aktivitas ekonomi secara drastus membuat bisnis menjadi rapuh secara finansial yang menyebabkan banyak orang diberhentikan dari pekerjaan mereka. [Kondisi ini juga membuat perusahaan tidak mampu memperkerjakan karyawan baru dan mempersulit para pencari kerja dalam mendapatkan pekerjaan mereka](https://www.thejakartapost.com/news/2016/11/01/productive-indonesians-struggle-to-find-jobs.html). 

Pada tahun 2020, Organisasi Perburuhan International menempatkan tingkat pengangguran kaum muda Indonesia sebagai tertinggi kedua di Asia Tenggara. Meskipun jumlah lulusan perguruan tinggi di Indonesia meningkat setiap tahun, angkat pengangguran di kalangan anak muda juga meningkat dan lebih tinggi setelah pandemi. [Situasi ini menunjukkan bahwa sebagian besar pencari kerja muda dengan pendidikan tinggi mengalami kesulitan dalam mencari pekerjaan](https://myedusolveindonesia.medium.com/tackling-youth-unemployment-issue-in-indonesia-16d8d1fd8dc4). Tidak hanya itu, menurut studi Willis Towers Watson terkait Talent Management and Rewards, 8 dari 10 perusahaan di Indonesia mengalami kesulitan menemukan lulusan perguruan tinggi dengan keterampilan yang dibutuhkan perusahaan mereka. Oleh karena itu, berdasarkan kedua permasalahan di atas, tingkat pengangguran kaum muda dapat dianggap sebagai salah satu masalah terbesar di Indonesia. 

Di era digital saat ini, baik pemberi kerja maupun pencari kerja dihadapkan pada data yang semakin melimpah dan proses rekrutmen yang memakan waktu. Profil kandidat sangat beragam sehingga sulit bagi perekrut untuk menemukan kompetensi yang relevan dengan kualifikasi yang dibutuhkan oleh perusahaan. Oleh karena itu, penting untuk mengidentifikasi fitur-fitur dari setiap kandidat yang relevan dengan kualifikasi atau keterampilan suatu perusahaan. [Sistem rekomendasi pekerjaan](https://www.sciencedirect.com/science/article/pii/S1877050920318020) adalah solusi teknologi Machine Learning yang mampu menyarankan pekerjaan atau kandidat yang relevan berdasarkan perilaku dan kebutuhan pencari kerja serta persyaratan suatu perusahaan. Dengan sistem rekomendasi ini, pelamar dapat menerima pekerjaan online yang dipersonalisasi dan perekrut diharapkan dapat menemukan kandidat yang paling relevan dengan keterampilan dan kualifikasi yang sesuai dengan kebutuhan mereka.


## Business Understanding
Proyek ini bertujuan untuk mengembangkan sistem rekomendasi pekerjaan yang dibuat untuk membantu para pencari kerja dalam menemukan pekerjaan yang sesuai dengan minat dan preferensi mereka. Selain itu, para pemberi kerja atau recruiter dari suatu perusahaan dapat menemukan target pekerja yang sesuai dengan kualifikasi dan keterampilan yang dibutuhkan suatu perusahaan. Dengan memanfaatkan model Machine Learning sistem rekomendasi, data user dan data perusahaan dari situs Job Posting yang telah diekstrak, diharapkan sistem ini dapat terus berkembang dan memberikan kemudahan bagi para pemberi kerja dan pencari kerja dalam mendapatkan perkerjaan dan pekerja yang sesuai dengan kriteria atau kualifasikasi yang relevan. 

### Problem Statement
Berdasarkan uraian latar belakang masalah yang telah dijelaskan sebelumnya, berikut rumusan masalah dari proyek ini:
1. Bagaimana proses pembuatan sistem rekomendasi pekerjaan berdasarkan data historis dari pekerjaan yang ditawarkan, detail profil perusahaan, keterampilan user dan kualifikasi perusahaan?
2. Bagaimana proses pembuatan sistem rekomendasi pekerjaan berdasarkan data kolaboratif dari pengguna lain dengan kualifikasi yang dicari?

### Goals
1. Membuat sistem rekomendasi pekerjaan berdasarkan data historis
2. Membuat sistem rekomenasi pekerjaan berdasarkan data kolaboratif

### Solution Statements
Untuk mengembangkan sistem rekomendasi pekerjaan yang baik, pada proyek ini menggunakan 2 Algoritma sistem rekomendasi dengan personalisasi, yaitu Content-Based Filtering (CBF) dan Collaborative Filtering (CF). Pada kategori Collaborative filtering, terdapat beberapa teknik yaitu Memory Based; seperti user based dan item based, dan Model Based; seperti matrix factorization dan pendekatan deep learning. Berikut penjelasan dari kedua algoritma tersebut:

- [Content Based Filtering](https://medium.com/data-folks-indonesia/recommendation-system-dengan-python-content-based-filtering-part-2-222a8c365add) <br>
Sistem rekomendasi berbasis konten merupakan algortihma yang berkerja dengan merekomendasikan item yang mirip dengan item yang disukai pengguna di masa lalu. Misal, pada kasus ini, jika pengguna menyukai pekerjaan sebagai Data Scientist, sistem akan merekomendasikan jenis pekerjaan yang berhubungan dengan Data atau keterampilan yang relevan dengan data Scientist. Tidak hanya itu, sistem juga akan merekomendasikan jenis pekerjaan yang sama dengan jenis perkerjaan yang telah anda lihat seperti Data Scientist. Algoritma CBF ini mempelajari profil minat pekerjaan user baru berdasarkan data dari jenis pekerjaan yang pernah disukai di masa lalu atau sedang dilihat di masa kini. Semakin banyak informasi yang diberikan pengguna, semakin baik akurasi sistem rekomendasi. 

- [Collaborative Filtering](https://de-drishti.medium.com/personalized-job-recommendation-system-using-collaborative-filtering-6d663046692a) <br>
Algortima CF bergantung pada pendapat komunitas pengguna. Collaborative filtering tidak memerlukan atribut untuk setiap itemnya seperti pada CBF. Collaborative filtering dibagi menjadi 2 kategori yaitu model based; metode berbasis model machine learning dan memory based; metode berbasis memori. Memory based berkerja dengan menentukan ukuran kesamaan atau similarity measures antara pengguna atau item (jenis pekerjaan) serta menemukan yang paling mirip. Memory based dibagi menjadi 2 jenis yakni User Based dan Item Based. <br>

  1. User Based: Adin dan Galih memberikan rating tinggi untuk jenis pekerjaan di bidang IT. Jika Adin menyukai pekerjaan Data Scientist, maka galih juga kemungkinan besar akan menyukai jenis pekerjaan tersebut.
  2. Item-Based: Adin dan Galih menyukai jenis pekerjaan sebagai Data Scientist dan Software Engineer. Kemudian, Agnia (pengguna baru) ternyata juga suka jenis pekerjaan sebagai Data Scientist sehingga sistem akan merekomendasikan jenis pekerjaan Software Engineer kepada Agnia (pengguna baru) karena dianggap mirip (similar) dengan Data Scientist. <br>
 
  Selain itu, algortima CF model based melibatkan model Machine Leanring. Metode ini mengekstrak informasi dari kumpulan data kemudian menggunakan model probabilitas untuk membuat rekomendasi. Sistem rekomendasi CF model based ini dapat dibuat tanpa harus menggunakan dataset yang lengkap sehingga penambahan pengguna baru tidak akan mengubah model. Metodei ini dibagi menjadi 3 jenis yakni Cluster Based Algorithms, Matrix Factorization dan Deep Learning atau Neural Network. <br>

  1. Cluster Based Algorithm: Algoritma ini berkerja dengan mengelompokkan pengguna sesuai dengan kesamaan preferensi jenis pekerjaan mereka. Jenis algoritma yang digunakan ialah K-Means Clustering.
  2. Matrix Factorization: Algoritma ini berkerja dengan mengurangi dimensi matriks melalu pembentukan dekomposisi matriks; cara mereduksi matriks menjadi bagian bagian penyusunnya.
  3. Deep Learning atau Neural Network: Algoritma ini bekerja dengan cara membuat kandidat (Candidate Generation) dan menentukan ranking. Candidate generation mengambil data peristiwa dari histori aktivitas pengguna saat mencari pekerjan sebagai masukan. Kemudian, membuat jenis pekerjaan yang paling relevan dari database. Proses ini menghasilkan kandidat (item) jenis pekerjaan yang relevan bagi pengguna. Selanjutnya, sejumlah kecil item yang relevan bagi pengguna akan dianalisis untuk memutuskan jenis pekerjaan yang akan direkomendasikan. Disinilah jaringan peringkat atau ranking berperan. Proses pemeringkatan ini menggunakan skor di setiap jenis pekerjaan pengguna. Skor tertinggi akan direkomendasikan oleh pengguna. <br>


## Data Understanding
Dataset yang digunakan adalah dataset yang diambil dari Kaggle yakni [Linkedin Job Postings 2023](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings). Dataset dalam bentuk Format CSV yang terdiri dari 4 kategori yaitu
1. job_postings.csv
   - job_id: ID pekerjaan yang didefinisikan oleh situs LinkedIn
   - company_id: ID perusahan yang terkait posting pekerjaan (company_details/companies.csv dan company_details/employee_counts.csv)
   - title: Judul pekerjaan
   - description: deskripsi pekerjaan
   - max_salary: gaji maximum
   - med_salary: jadi rata-rata
   - min_salary: gaji minimum
   - pay_period: periode pembayaran gaji (Hourly, Monthly, Yearly)
   - formatted_work_type: Jenis pekerjaan (Fulltime, Parttime, Contract)
   - location: Lokasi pekerjaan
   - applies: jumlah pendaftar yang telah melakukan submit berkas
   - original_listed_time: Original time the job was listed
   - remote_allowed: apakah pekerjaan bersifat remote atau tidak
   - views: jumlah yang telah melihat postingan pekerjaan tersebut 
   - job_posting_url: URL to the job posting on a platform
   - application_url: URL where applications can be submitted
   - application_type: Jenis proses seleksi berkas pendaftar (offsite, complex/simple onsite)
   - expiry: Expiration date or time for the job listing
   - closed_time: Time to close job listing
   - formatted_experience_level: Job experience level (entry, associate, executive, etc)
   - skills_desc: Description detailing required skills for job
   - listed_time: Time when the job was listed
   - posting_domain: Domain of the website with application 
   - sponsored: Whether the job listing is sponsored or promoted.
   - work_type: Type of work associated with the job
   - currency: Currency in which the salary is provided.
   - compensation_type: Type of compensation for the job. <br>
2. job_details/benefits.csv
   - job_id
   - type: jenis manfaat yang disediakan oleh perusahaan seperti asuransi kesehatan, dan sebagainya
   - inferred: apakah manfaat ditag secara eksplisit atau melalui teks oleh linkedin <br>
3. company_details/companies.csv
   - company_id: The company ID as defined by LinkedIn
   - name: Company name
   - description: Company description
   - company_size: Company grouping based on number of employees (0 Smallest - 7 Largest)
   - country: Country of company headquarters.
   - state: State of company headquarters.
   - city: City of company headquarters
   - zip_code: ZIP code of company's headquarters.
   - address: Address of company's headquarters
   - url: Link to company's LinkedIn page <br>
4. company_details/employee_counts.csv
   - company_id: The company ID
   - employee_count: Number of employees at company
   - follower_count: Number of company followers on LinkedIn
   - time_recorded: Unix time of data collection <br>

Total kesuluruhan dataset adalah 33,000+ pekerjaan yang dipublikasi dan terdaftar selama 2 hari, terpisah beberapa bulan. Setiap postingan berisi 27 atribut berharga termasuk judul, deskripsi pekerjaan, gaji, lokasi, URL aplikasi, dan jenis pekerjaan (remote, kontrak, dll), di samping file terpisah yang berisi manfaat, keterampilan, dan industri yang terkait dengan setiap posting. Mayoritas pekerjaan juga ditautkan ke perusahaan, yang semuanya terdaftar dalam file csv lain yang berisi atribut seperti deskripsi perusahaan, lokasi kantor pusat, dan jumlah karyawan, dan jumlah pengikut.

Untuk memahami sebuah data dengan memiliki jumlah yang banyak akan lebih efisien jika kita menggunakan teknik yang disebut dengan exploratory data analysis. Dalam proyek ini, menggunakan beberapa visualisasi yang ada diikuti dengan pemeriksaan jenis data, missing values, data terduplikasi dan analisis statistik deskriptif. <br>

Visualisasi Wordcloud pada Job Title:<br>
![wordcloud job title](https://github.com/adinplb/ML-Terapan-Proyek-Kedua/assets/61041719/6e8909a8-28b8-415d-a173-8e0bf0c07325) <br>
Visualisasi Bar Chart pada Work Type:<br>
![work_type](https://github.com/adinplb/ML-Terapan-Proyek-Kedua/assets/61041719/e7c6448e-463d-4a7b-b922-2363378b2459) <br>
Univariate Analysis <br>
![univariate](https://github.com/adinplb/ML-Terapan-Proyek-Kedua/assets/61041719/f340e85f-cbce-47e5-ad7a-9caf56342bc4) <br>
Multivariate Analysis <br>
![multivariate](https://github.com/adinplb/ML-Terapan-Proyek-Kedua/assets/61041719/ae7a299a-cc44-4a88-99e2-58a447a7759c)


## Data Preparation
Pada tahap ini, lakukan data combination pada semua file csv dengan fungsi merge. Setelah digabung, pilih data dengan fungsi unique sehingga terhindari dari duplikasi. Data terpilih akan diubah ke dalam bentuk array untuk setiap atributnya. Kemudian, lakukan vektorisasi agar data menjadi bentuk matriks dan diakhiri dengan pembobotan TF-IDF. Berikut ini urutan pada Data Preparation yang akan digunakan dalam membangun model dengan metode CBF: <br>
- Menghilangkan Missing Value <br>
Sebelumnya kita melihat adanya Missing Value pada data kita jadi kita akan menghapusnya dengan fungsi dropna() <br>
- Menghapus Data Duplikat <br>
kita akan menghapusnya agar menjadi setiap jenis pekerjaan memiliki nilai yang berbeda. Cara yang kita gunakan adalah dengan drop_duplicates()
- Ubah data ke dalam bentuk list <br>
Pada tahap ini, kami mencoba untuk mengubah variable yang dibutuhkan yaitu tipe jenis pekerjaan dan jenis pekerjaan ke dalam sebuah list. Dengan tujuan untuk menjadikannya data dictionary setelah itu.
- Membuat Dictionary <br>
Kita membuat variable baru dengan nama Job_Title dengan isi Dictionary tiga atribute kita, di bantu dengan pd.DataFrame() dalam membuat Dictionary. Tujuan nya untuk menentukan key:value pada atrbiute dataset kita.


## Modelling
Tahap kali ini kita akan menggunakan Content Based Filltering yaitu, merekomendasikan item yang mirip dengan item yang disukai pengguna di masa lalu. Di bantu dengan teknik TF IDF dan Cosine Similarity untuk mencari korelasi antara judul film satu dengan yang lainnya berdasarkan genre. Dalam Cosine Similarity, objek data dalam kumpulan data diperlakukan sebagai vektor. Rumus untuk mencari persamaan kosinus antara dua vektor adalah,
Top-N Recommendation: 

| Job Title     | Work Type |
| ----------- | ----------- |
| Server-over 19 to serve alcohol preferred | Full-Time |
| HVAC Project Manager | Full-Time |
| Office Manager | Full-Time |
| Executive Chef - Stadium Operations | Full-Time |
| Manager, Engineering | Full-Time |
<br>

## Evaluation
Matrik yang kita gunakan untuk sistem rekomendasi Content Based Filtering adalah Matrik Precision, yaitu P = Hasil rekomendasi relevan/total rekomendasi. Berdasarkan hasil rekomendasi 5 jenis pekerjaan yang relevan maka presisi adalah 100%. Hal ini menunjukkan bahwa sebelumnya jenis pekerjaan yang berjenis tipe yang sama yaitu full time. Kemudian program kita mencoba memberi 5 rekomendasi jenis pekerjaan yang serupa kepada pengguna berdasarkan jenis tipe pekerjaan. Dan hasil yang di dapat adalah ke 5 rekomendasi sistem berhasil memberi 5 jenis pekerjaan dengan tipe pekerjaan yang sama/relevan kepada user. Dengan begitu kita tau bahwa hasil presisi dari sistem rekomendasi untuk Technical Specialist adalah 100%.
