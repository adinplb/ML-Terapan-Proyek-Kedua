# -*- coding: utf-8 -*-
"""Recommender_System_Jobs_Indonesia

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fQvVGeV-zwCVMf0Ibg43t0o42-Q_wR-8

# **Laporan Proyek Machine Learning (Job Recommender System)- Muhammad Adin Palimbani**

## **Project Overview**
Sejak pandemi COVID-19 terjadi di tahun 2020, sebagian besar negara mengahadapi masalah akut dalam menyediakan pekerjaan bagi kaum muda. Penurunan aktivitas ekonomi secara drastus membuat bisnis menjadi rapuh secara finansial yang menyebabkan banyak orang diberhentikan dari pekerjaan mereka. Kondisi ini juga membuat perusahaan tidak mampu memperkerjakan karyawan baru dan mempersulit para pencari kerja dalam mendapatkan pekerjaan mereka. <br>

Pada tahun 2020, Organisasi Perburuhan International menempatkan tingkat pengangguran kaum muda Indonesia sebagai tertinggi kedua di Asia Tenggara. Meskipun jumlah lulusan perguruan tinggi di Indonesia meningkat setiap tahun, angkat pengangguran di kalangan anak muda juga meningkat dan lebih tinggi setelah pandemi. Situasi ini menunjukkan bahwa sebagian besar pencari kerja muda dengan pendidikan tinggi mengalami kesulitan dalam mencari pekerjaan. Tidak hanya itu, menurut studi Willis Towers Watson terkait Talent Management and Rewards, 8 dari 10 perusahaan di Indonesia mengalami kesulitan menemukan lulusan perguruan tinggi dengan keterampilan yang dibutuhkan perusahaan mereka. Oleh karena itu, berdasarkan kedua permasalahan di atas, tingkat pengangguran kaum muda dapat dianggap sebagai salah satu masalah terbesar di Indonesia. <br>

Di era digital saat ini, baik pemberi kerja maupun pencari kerja dihadapkan pada data yang semakin melimpah dan proses rekrutmen yang memakan waktu. Profil kandidat sangat beragam sehingga sulit bagi perekrut untuk menemukan kompetensi yang relevan dengan kualifikasi yang dibutuhkan oleh perusahaan. Oleh karena itu, penting untuk mengidentifikasi fitur-fitur dari setiap kandidat yang relevan dengan kualifikasi atau keterampilan suatu perusahaan. Sistem rekomendasi pekerjaan adalah solusi teknologi Machine Learning yang mampu menyarankan pekerjaan atau kandidat yang relevan berdasarkan perilaku dan kebutuhan pencari kerja serta persyaratan suatu perusahaan. Dengan sistem rekomendasi ini, pelamar dapat menerima pekerjaan online yang dipersonalisasi dan perekrut diharapkan dapat menemukan kandidat yang paling relevan dengan keterampilan dan kualifikasi yang sesuai dengan kebutuhan mereka.

## **Business Understanding**
Proyek ini bertujuan untuk mengembangkan sistem rekomendasi pekerjaan yang dibuat untuk membantu para pencari kerja dalam menemukan pekerjaan yang sesuai dengan minat dan preferensi mereka. Selain itu, para pemberi kerja atau recruiter dari suatu perusahaan dapat menemukan target pekerja yang sesuai dengan kualifikasi dan keterampilan yang dibutuhkan suatu perusahaan. Dengan memanfaatkan model Machine Learning sistem rekomendasi, data user dan data perusahaan dari situs Job Posting yang telah diekstrak, diharapkan sistem ini dapat terus berkembang dan memberikan kemudahan bagi para pemberi kerja dan pencari kerja dalam mendapatkan perkerjaan dan pekerja yang sesuai dengan kriteria atau kualifasikasi yang relevan.

### **Problem Statements**
Berdasarkan uraian latar belakang masalah yang telah dijelaskan sebelumnya, berikut rumusan masalah dari proyek ini:
1. Bagaimana proses pembuatan sistem rekomendasi pekerjaan berdasarkan data historis dari pekerjaan yang ditawarkan, detail profil perusahaan, keterampilan user dan kualifikasi perusahaan?
2. Bagaimana proses pembuatan sistem rekomendasi pekerjaan berdasarkan data kolaboratif dari pengguna lain dengan kualifikasi yang dicari?

### **Goals**
1. Membuat sistem rekomendasi pekerjaan berdasarkan data historis
2. Membuat sistem rekomenasi pekerjaan berdasarkan data kolaboratif

### **Solution Startements**
Untuk mengembangkan sistem rekomendasi pekerjaan yang baik, pada proyek ini menggunakan 2 Algoritma sistem rekomendasi dengan personalisasi, yaitu Content-Based Filtering (CBF) dan Collaborative Filtering (CF). Pada kategori Collaborative filtering, terdapat beberapa teknik yaitu Memory Based; seperti user based dan item based, dan Model Based; seperti matrix factorization dan pendekatan deep learning.

## Data Understanding
Dataset yang digunakan adalah dataset yang diambil dari Kaggle yakni [Linkedin Job Postings 2023](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings). Dataset dalam bentuk Format CSV yang terdiri dari 4 kategori yaitu
1. job_postings.csv
2. job_details/benefits.csv
3. company_details/companies.csv
4. company_details/employee_counts.csv

## Data Preparation CBF

### Pre-Process job_details data
"""

import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt # for plotting nice charts
from functools import reduce # module which helps in merging multiple dataframes
from wordcloud import WordCloud # module to print word cloud
import seaborn as sns

!unzip /content/drive/MyDrive/pengembangan-ML-dicoding/recommender_system/linkedinjobsposting.zip

df_job_postings = pd.read_csv("/content/job_postings.csv")
df_job_postings.info()
# check missing values and duplication
print ('Jummlah job_id yang Terduplikasi Sebanyak:', df_job_postings['job_id'].duplicated().sum())
print ('Jummlah missing values di job_id sebanyak:', df_job_postings['job_id'].isnull().sum())

df_job_postings.describe()

# Visualization 1: Creating a word cloud from job titles
job_titles_text = ' '.join(df_job_postings['title'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(job_titles_text)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Job Title Word Cloud')
plt.axis('off')
plt.tight_layout()
plt.show()

# Visualization 3: Job Type Breakdown (Bar Chart)
job_type_counts = df_job_postings['work_type'].value_counts()
plt.figure(figsize=(10, 6))
job_type_counts.plot(kind='bar', color='lightblue')
plt.title('Job Type Breakdown')
plt.xlabel('Job Type')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

df_job_postings.hist(bins=50, figsize=(20,15))
plt.show()

# Mengamati hubungan antar fitur numerik dengan fungsi pairplot()
sns.pairplot(df_job_postings, diag_kind = 'kde')

"""dapat disumpulkan bahwa pada atribut job_id di dataframe job postings tidak ada yang terduplikasi maupun missing values"""

df_job_benefits = pd.read_csv("/content/job_details/benefits.csv")
df_job_benefits.info()
df_job_benefits = df_job_benefits.drop('inferred', axis=1) # remove 'inferred' column
df_job_benefits = df_job_benefits.groupby('job_id')['type'].agg(lambda x: ', '.join(x)).reset_index() # aggregate same job benefits

df_job_postings = df_job_postings.merge(df_job_benefits, on="job_id", how="left")
df_job_postings

# merge duplicate job_id on job_skills.csv
df_job_skills = pd.read_csv("/content/job_details/job_skills.csv")
df_job_skills = df_job_skills.groupby('job_id')['skill_abr'].agg(lambda x: ', '.join(x)).reset_index() # aggregate same job skills

df_job_postings= df_job_postings.merge(df_job_skills, on="job_id", how="left")
df_job_postings

"""job_details data is DONE!

### Pre-Process company_details data
"""

df_companies = pd.read_csv("/content/company_details/companies.csv")

df_company_industries = pd.read_csv("/content/company_details/company_industries.csv")
df_company_industries = df_company_industries.groupby('company_id')['industry'].agg(lambda x: ', '.join(x)).reset_index() # aggregate same company industries

df_company_specialities = pd.read_csv("/content/company_details/company_specialities.csv")
df_company_specialities = df_company_specialities.groupby('company_id')['speciality'].agg(lambda x: ', '.join(x)).reset_index() # aggregate same company specialities

df_employee_counts = pd.read_csv("/content/company_details/employee_counts.csv")
df_employee_counts = df_employee_counts.groupby('company_id')['time_recorded'].max().reset_index() # get newest data based on 'time_recorded' column

df_companies = df_companies.merge(df_company_industries, on="company_id", how="left")
df_companies = df_companies.merge(df_company_specialities, on="company_id", how="left")
df_companies = df_companies.merge(df_employee_counts, on="company_id", how="left")
df_companies

"""### Merge job_details dan company_details"""

merged_data = df_job_postings.merge(df_companies, on="company_id", how="left")
merged_data

# Check Missing Values
merged_data.isnull().sum()

"""### Eleminate Certain Column to Use for Recomennder System and Rename the column for better understanding"""

selected_column = ['job_id','company_id','title','name','description_x','skills_desc', 'formatted_work_type','location','description_y','company_size','industry']
merged_data = merged_data[selected_column]
merged_data



update_column_name = {'title': 'job_title', 'name': 'company_name', 'description_x': 'job_description',
               'formatted_work_type': 'work_type','description_y': 'company_description'}
data = merged_data.rename(columns=update_column_name)
data = data.dropna()
data

data.isnull().sum()

# mengurutkan company berdasarkan company_id kemudian dimasukkan ke dalam variabel fix_company
fix_company = data.sort_values('company_id', ascending=True)
fix_company

# Mengecek berapa jumlah fix_company
len(fix_company.company_id.unique())

# Mengecek kategori job_tittle
fix_company.job_title.unique()

preparation = fix_company
preparation.sort_values('company_id')

# Membuang data duplikat pada variabel preparation
preparation = preparation.drop_duplicates('company_id')
preparation

# Mengonversi data series ‘company_id’ menjadi dalam bentuk list
company_id = preparation['company_id'].tolist()

# Mengonversi data series ‘Name’ menjadi dalam bentuk list
company_name= preparation['company_name'].tolist()

# Mengonversi data series ‘Name’ menjadi dalam bentuk list
company_size= preparation['company_size'].tolist()

# Mengonversi data series ‘Name’ menjadi dalam bentuk list
job_title= preparation['job_title'].tolist()

# Mengonversi data series ‘Rcuisine’ menjadi dalam bentuk list
work_type = preparation['work_type'].tolist()

print(len(company_id))
print(len(company_name))
print(len(company_size))
print(len(job_title))
print(len(work_type))

# Membuat dictionary untuk data ‘resto_id’, ‘resto_name’, dan ‘cuisine’
company_new = pd.DataFrame({
    'id': company_id,
    'name': company_name,
    'size': company_size,
    'job_title': job_title,
    'work_type': work_type
})
company_new

"""### TF-Vectorizer"""

data = company_new
data.sample(10)

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data cuisine
tf.fit(data['work_type'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(data['work_type'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

"""nilai 10095 ukuran data dan 8 adalah matriks kategori work_type"""

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan jenis masakan
# Baris diisi dengan nama resto

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=data.job_title
).sample(4, axis=1).sample(10, axis=0) # 8 itu worktypenya dan 2 itu job_title nya

from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama resto
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['job_title'], columns=data['job_title'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap resto
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""## Modelling CBF

### Dapatkan Rekomendasi berupa TOP N RECOMMENDATION
"""

def jobs_recommendations(job_title, similarity_data=cosine_sim_df, items=data[['job_title', 'work_type']], k=5):
    """
    Rekomendasi Resto berdasarkan kemiripan dataframe

    Parameter:
    ---
    nama_resto : tipe data string (str)
                Nama Restoran (index kemiripan dataframe)
    similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan resto sebagai
                      indeks dan kolom
    items : tipe data pd.DataFrame (object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
    k : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
    ---


    Pada index ini, kita mengambil k dengan nilai similarity terbesar
    pada index matrix yang diberikan (i).
    """


    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,job_title].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama_resto agar nama resto yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(job_title, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

# menemukan rekomendasi pekerjaan yang punya work_type sejenis
data[data.job_title.eq('Lead DevOps Engineer')]

# Mendapatkan rekomendasi pekerjaan yang work_typenya mirip dengan Lead DevOps Engineer
jobs_recommendations('Technical Specialist')