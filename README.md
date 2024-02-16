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

Untuk memahami sebuah data dengan memiliki jumlah yang banyak akan lebih efisien jika kita menggunakan teknik yang disebut dengan exploratory data analysis. Dalam proyek ini, menggunakan beberapa visualisasi yang ada diikuti dengan pemeriksaan jenis data, missing values, data terduplikasi dan analisis statistik deskriptif.

![df info](https://github.com/adinplb/Belajar-Machien-Learning-Terapan-Dicoding/assets/61041719/34570f7b-7e16-414e-89f6-0599f85d0f78)
<br>
![df isna](https://github.com/adinplb/Belajar-Machien-Learning-Terapan-Dicoding/assets/61041719/e14838d5-5672-4119-95dd-fd14397d81d0)
<b>
![df duplicated](https://github.com/adinplb/Belajar-Machien-Learning-Terapan-Dicoding/assets/61041719/78819fb9-3ed0-47f7-97fa-da9328168a27)
<br>
![df describe](https://github.com/adinplb/Belajar-Machien-Learning-Terapan-Dicoding/assets/61041719/9b0f5c49-5927-4b31-adad-21dcd35e6f67)


## Data Preparation
At this stage, PCA feaures reduction, change target labelled type into binary integer, IQR Method, SMOTE and Feature Scalling are approriate techniques for this type of dataset. Moreover, the class contribution in dataset are indeed imbalanced; 357 Benign and 212 Malignant so SMOTE or Synthetic Minority Over-sampling Technique will be implemented. Removing outliers will be performed as well and followed by feature scaling or z-score normalization where they have a mean of 0 and a standard deviation of 1. The data size will be splitted into train set and test set with ratio 80:20. To understand deeply the ins and outs of data preparation is by looking at these several steps: <br>

1. Convert "Diagnosis" Feature "object" type into "binary integer" values 0 and 1.
>Why is it necessary for this technique to be carried out?
>>Answer: require input features to be numerical so the algorithms can be performed.
```ruby
df['diagnosis']=df['diagnosis'].map({'M':1,'B':0})
```
<img src="https://github.com/adinplb/Belajar-Machien-Learning-Terapan-Dicoding/assets/61041719/a29b20da-b0f5-4b34-b066-2c2ed1e285d9"/> <img src="https://github.com/adinplb/Belajar-Machien-Learning-Terapan-Dicoding/assets/61041719/89166fd5-dce2-499c-8a6d-3909cafa9db2"/> 

2. Remove outliers using IQR Method in all Features. Then, check data shape.
>Why is it necessary for this IQR Method to be carried out?
>>Answer: outliers can increase variance in the dataset and the Interquartile Range (IQR) method is a robust and commonly used technique for detecting and removing outliers as well. 
```ruby
Q1 = df_baru.quantile(0.25)
Q3 = df_baru.quantile(0.75)
IQR=Q3-Q1
df_baru=df_baru[~((df_baru<(Q1-1.5*IQR))|(df_baru>(Q3+1.5*IQR))).any(axis=1)]

# Check data shape after dropping outliers
df_baru.shape
```
![data shape after drop outliers](https://github.com/adinplb/Belajar-Machien-Learning-Terapan-Dicoding/assets/61041719/26534822-5f9f-451a-9efe-cbccc9b7c3eb) <br>
The dataset has been cleaned and has 398 samples

3. Reduce dimension of radius_mean, perimeter_mean, area_mean, radius_worst, perimeter_worst and area_worst feature using PCA
>Why is it necessary for reducing those features using PCA to be carried out?
>>Answer: The pairplot result shows those six features have a high correlation so they can be reduced using PCA which help to reduce noise and redundancy in dataset.
```ruby
from sklearn.decomposition import PCA
pca = PCA(n_components=1, random_state=123)
pca.fit(df_baru[['radius_mean', 'perimeter_mean', 'area_mean', 'radius_worst', 'perimeter_worst', 'area_worst']])
df_baru['dimension'] = pca.transform(df_baru.loc[:, ('radius_mean', 'perimeter_mean', 'area_mean', 'radius_worst', 'perimeter_worst', 'area_worst')]).flatten()
df_baru.drop(['radius_mean', 'perimeter_mean', 'area_mean', 'radius_worst', 'perimeter_worst', 'area_worst'], axis=1, inplace=True)
df_baru
```
![dimension](https://github.com/adinplb/Belajar-Machien-Learning-Terapan-Dicoding/assets/61041719/bf28fcf9-1c18-4ecd-8284-fd15c807384a)

4. Splitting Data into Train Set and Test Set + SMOTE For imbalanced data
>Why is it necessary for handling imbalanced data using SMOTE to be carried out?
>>Answer: To maximize overall accuracy and minimize MSE which can be misleading when classes are imbalanced and SMOTE (Synthetic Minority Over-sampling Technique) is one of the method used to address this issue.
```ruby
pip install imbalanced-learn
```
```ruby
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

# Assuming X contains your features and y contains the corresponding labels
# Perform train-test split

X = df.drop(["diagnosis"],axis =1)
y = df["diagnosis"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMOTE only on the training data
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Now, X_train_resampled and y_train_resampled contain the resampled data using SMOTE,
# while X_test and y_test remain unchanged

# Proceed with model training and evaluation using the resampled training data and the original test data

# Count the number of samples in each class before and after SMOTE
unique_train, counts_train = np.unique(y_train, return_counts=True)
unique_train_resampled, counts_train_resampled = np.unique(y_train_resampled, return_counts=True)

# Create a DataFrame to display the results
data = {
    'Class': unique_train,
    'Original Count': counts_train,
    'Resampled Count': counts_train_resampled
}

df_result = pd.DataFrame(data)
print("Before SMOTE:")
print(df_result)

# Visualize the distribution of classes after SMOTE
print("\nAfter SMOTE:")
print("Classes:", unique_train_resampled)
print("Counts:", counts_train_resampled)
```
![output smote](https://github.com/adinplb/Belajar-Machien-Learning-Terapan-Dicoding/assets/61041719/0c0b9474-ad9f-4f9a-9482-8648a8642ae4)

5. Feature Scalling using Z-Score Normalization
>Why is it necessary for feature scalling to be carried out?
>>Answer: To ensures all features have a similar scale, typically between 0 and 1 or around a mean of 0 with a standard deviation of 1. 
```ruby
scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()
X_train[numerical_features].describe().round(4)
```
![standarisation](https://github.com/adinplb/Belajar-Machien-Learning-Terapan-Dicoding/assets/61041719/ed2b1602-7ea1-4089-a6ed-c9d7c9037585)


## Modelling
To solve this Binary Classification of Medical Diagnosis issue, implementing Logistic Regression, Neural Network and Support Vector Machine Algorithms are the most appropriate model in classifying whether it is Benign (0) or Malignant (1) and having a great accuracy for predictions. The following is an explanation of each stage in each algorithms:
- [Logistic Regression Model:](https://medium.com/@akshayjain_757396/advantages-and-disadvantages-of-logistic-regression-in-machine-learning-a6a247e42b20) <br>
  Step 1. Import library <br>
  ```ruby
  from sklearn.linear_model import LogisticRegression
  from sklearn.metrics import classification_report, confusion_matrix
  from imblearn.over_sampling import SMOTE
  from sklearn.preprocessing import StandardScaler
  ```
  Step 2. Scale features (optional but often recommended)
  ```ruby
  scaler = StandardScaler()
  X_train_resampled_scaled = scaler.fit_transform(X_train_resampled)
  X_test_scaled = scaler.transform(X_test)
  ```
  Step 3. Initialize and train logistic regression model before SMOTE <br>
  ```ruby
  log_reg_before_smote = LogisticRegression()
  log_reg_before_smote.fit(X_train, y_train)
  ```
  Step 4. Make predictions on the test set before SMOTE <br>
  ```ruby
  y_pred_before_smote = log_reg_before_smote.predict(X_test)
  ```
  Step 5. Evaluate performance before SMOTE
  ```ruby
  print("Performance before SMOTE:")
  print(confusion_matrix(y_test, y_pred_before_smote))
  print(classification_report(y_test, y_pred_before_smote))
  ```

  ![LogReg_Before Smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/73a0b293-33a1-4855-ac9b-577a2adc33ac)

  Step 6. Initialize and train logistic regression model after SMOTE <br>
  ```ruby
  log_reg_after_smote = LogisticRegression()
  log_reg_after_smote.fit(X_train_resampled_scaled, y_train_resampled)
  ```
  Step 7. Make predictions on the test set after SMOTE
  ```ruby
  y_pred_after_smote = log_reg_after_smote.predict(X_test_scaled)
  ```
  Step 8. Evaluate performance after SMOTE
  ```ruby
  print("Performance after SMOTE:")
  print(confusion_matrix(y_test, y_pred_after_smote))
  print(classification_report(y_test, y_pred_after_smote))
  ```
  ![LogReg_After Smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/77ddc2a4-4a7c-43eb-8046-0a56a6caa393)

  Step 9. Plot Confusion Metrics Before and After SMOTE
  ```ruby
  # Compute confusion matrices before and after SMOTE
  confusion_matrix_before_smote = confusion_matrix(y_test, y_pred_before_smote)
  confusion_matrix_after_smote = confusion_matrix(y_test, y_pred_after_smote)

  # Plot confusion matrices
  fig, axes = plt.subplots(1, 2, figsize=(12, 6))

  # Plot confusion matrix before SMOTE
  axes[0].imshow(confusion_matrix_before_smote, cmap=plt.cm.Blues, interpolation='nearest')
  axes[0].set_title('Confusion Matrix Before SMOTE')
  axes[0].set_xticks([0, 1])
  axes[0].set_yticks([0, 1])
  axes[0].set_xlabel('Predicted Label')
  axes[0].set_ylabel('True Label')
  for i in range(2):
      for j in range(2):
          axes[0].text(j, i, str(confusion_matrix_before_smote[i, j]),
                       horizontalalignment='center', verticalalignment='center',   color='white')

  # Plot confusion matrix after SMOTE
  axes[1].imshow(confusion_matrix_after_smote, cmap=plt.cm.Blues, interpolation='nearest')
  axes[1].set_title('Confusion Matrix After SMOTE')
  axes[1].set_xticks([0, 1])
  axes[1].set_yticks([0, 1])
  axes[1].set_xlabel('Predicted Label')
  axes[1].set_ylabel('True Label')
  for i in range(2):
      for j in range(2):
          axes[1].text(j, i, str(confusion_matrix_after_smote[i, j]),
                       horizontalalignment='center', verticalalignment='center', color='white')

  plt.tight_layout()
  plt.show()
  ```

  ![LogReg Confusion Before and After smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/1d373926-f9db-4916-974a-127d1dd8c834)

  Step 10. Plot Accuracy Before and After SMOTE
  ```ruby
  # Get classification reports before and after SMOTE
  classification_report_before_smote = classification_report(y_test, y_pred_before_smote, output_dict=True)
  classification_report_after_smote = classification_report(y_test, y_pred_after_smote, output_dict=True)

  # Extract accuracy values
  accuracy_before_smote = classification_report_before_smote['accuracy']
  accuracy_after_smote = classification_report_after_smote['accuracy']

  # Plot accuracy before and after SMOTE
  labels = ['Before SMOTE', 'After SMOTE']
  accuracy_scores = [accuracy_before_smote, accuracy_after_smote]

  plt.bar(labels, accuracy_scores, color=['blue', 'green'])
  plt.xlabel('SMOTE')
  plt.ylabel('Accuracy')
  plt.title('Accuracy of Logistic Regression before and after SMOTE')
  plt.ylim(0, 1)  # Limit y-axis from 0 to 1 for accuracy range
  plt.show()
  ```
  ![LogReg_Accuracy_Before and after smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/63740f0e-86f4-433d-bc0c-3cb69da4c3bf)

  > Advantages: <br>
  >> - Logistic Regression performs well when the dataset is linearly separable <br>
  >> - Logistic Regression not only gives a measure of how relevant a predictor (coefficient size) is, but also its direction of association (positive or negative) <br>
  
  > Disadvantages: <br>
  >> - Main limitation of Logistic Regression is the assumption of linearity between the   dependent variable and the independent variables <br>
  >> - If the number of observations are lesser than the number of features, Logistic Regression should not be used, otherwise it may lead to overfit  <br>



- [Neural Network Model](https://subscription.packtpub.com/book/data/9781788397872/1/ch01lvl1sec27/pros-and-cons-of-neural-networks): <br>
  Step 1. Import library <br>
  ```ruby
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.layers import Dense
  ```
  Step 2. Scale features (optional but often recommended)
  ```ruby
  scaler = StandardScaler()
  X_train_resampled_scaled = scaler.fit_transform(X_train_resampled)
  X_test_scaled = scaler.transform(X_test)
  ```
  Step 3. Define the neural network model architecture before SMOTE <br>
  ```ruby
  lmodel_before_smote = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
  ])
  ```
  Step 4. Compile the model <br>
  ```ruby
  model_before_smote.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
  ```
  Step 5. Train the model before SMOTE
  ```ruby
  model_before_smote.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)
  ```
  Step 6. Make predictions on the test set before SMOTE <br>
  ```ruby
  y_pred_before_smote = (model_before_smote.predict(X_test) > 0.5).astype("int32")
  ```
  Step 7. Compute and print confusion matrix and classification report before SMOTE
  ```ruby
  print("Confusion Matrix and Classification Report before SMOTE:")
  print(confusion_matrix(y_test, y_pred_before_smote))
  print(classification_report(y_test, y_pred_before_smote))
  ```
  ![NN_Before Smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/b5dbe9b3-47b7-438a-bd50-7aa594a65a3e)

  Step 8. Define the neural network model architecture after SMOTE
  ```ruby
  model_after_smote = Sequential([
    Dense(128, activation='relu', input_shape=(X_train_resampled_scaled.shape[1],)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
  ])
  ```

  Step 9. Compile the model
  ```ruby
  model_after_smote.compile(optimizer='adam', loss='binary_crossentropy', metrics= ['accuracy'])
  ```

  Step 10. Train the model after SMOTE
  ```ruby
  history_smote = model_after_smote.fit(X_train_resampled_scaled, y_train_resampled, epochs=10, batch_size=32, verbose=1)
  ```

  Step 11. Make predictions on the test set after SMOTE
  ```ruby
  y_pred_after_smote = (model_after_smote.predict(X_test_scaled) > 0.5).astype("int32")
  ```

  Step 12. Compute and print confusion matrix and classification report after SMOTE
  ```ruby
  print("Confusion Matrix and Classification Report after SMOTE:")
  print(confusion_matrix(y_test, y_pred_after_smote))
  print(classification_report(y_test, y_pred_after_smote))
  ```

  ![NN After Smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/5dbf196c-9751-43e7-a87c-e7541b3d0b12)


  Step 13. Plot confusion matrix before and after SMOTE
  ```ruby
  # Plot confusion matrix before SMOTE
  axes[0].imshow(confusion_matrix_before_smote, cmap=plt.cm.Blues, interpolation='nearest')
  axes[0].set_title('Confusion Matrix Before SMOTE')
  axes[0].set_xticks([0, 1])
  axes[0].set_yticks([0, 1])
  axes[0].set_xlabel('Predicted Label')
  axes[0].set_ylabel('True Label')
  for i in range(2):
      for j in range(2):
          axes[0].text(j, i, str(confusion_matrix_before_smote[i, j]),
                       horizontalalignment='center', verticalalignment='center', color='white')

  # Plot confusion matrix after SMOTE
  axes[1].imshow(confusion_matrix_after_smote, cmap=plt.cm.Blues, interpolation='nearest')
  axes[1].set_title('Confusion Matrix After SMOTE')
  axes[1].set_xticks([0, 1])
  axes[1].set_yticks([0, 1])
  axes[1].set_xlabel('Predicted Label')
  axes[1].set_ylabel('True Label')
  for i in range(2):
      for j in range(2):
          axes[1].text(j, i, str(confusion_matrix_after_smote[i, j]),
                       horizontalalignment='center', verticalalignment='center', color='white')

  plt.tight_layout()
  plt.show()
  ```

  ![NN_ConfusionMetrics](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/436f2328-888d-4abd-8ed2-397e03db62ca)


  Step 14. Plot Accuracy Before and After SMOTE
  ```ruby
  # Plot accuracy before and after SMOTE
  plt.plot(history_original.history['accuracy'], label='Original Dataset')
  plt.plot(history_smote.history['accuracy'], label='After SMOTE')
  plt.xlabel('Epochs')
  plt.ylabel('Accuracy')
  plt.title('Accuracy of Neural Network before and after SMOTE')
  plt.legend()
  plt.show()
  ```
  | Plot Accuracy 1 | Plot Accuracy 2 | 
  | :---: | :---: | 
  | ![NN_Accuracy Before after smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/d88fa925-694f-47bf-a0f3-5edd86021790) | ![NN_Diagram Accuracy before after smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/d7b4fb46-431c-46a7-9e85-fcd8128b0999) | 

  > Advantages: <br>
  >> - Neural Network can be trained with any number of inputs and layers <br>
  >> - Neural networks work best with more data points
  >> - One trained, the predictions are pretty fast
  
  >  Disadvantages: <br>
  >> - Neural networks are black boxes, meaning we cannot know how each independent variable is influencing the dependent variables <br>
  >> - It is computationally very expensive and time consuming to train with traditional CPUs  <br>
  >> - Neural networks depend a lot on training data





- [Support Vector Machine Model:](https://scikit-learn.org/stable/modules/svm.html) <br>
  Step 1. Import library <br>
  ```ruby
  from sklearn.svm import SVC
  ```
  Step 2. Initialize SVM classifier before SMOTE
  ```ruby
  svm_classifier_before_smote = SVC(kernel='rbf', random_state=42)
  ```
  Step 3. Train SVM classifier before SMOTE <br>
  ```ruby
  svm_classifier_before_smote.fit(X_train, y_train)
  ```
  Step 4. Make predictions on the test set before SMOTE <br>
  ```ruby
  y_pred_before_smote = svm_classifier_before_smote.predict(X_test)
  ```
  Step 5. Compute and print confusion matrix and classification report before SMOTE
  ```ruby
  print("Confusion Matrix and Classification Report before SMOTE:")
  print(confusion_matrix(y_test, y_pred_before_smote))
  print(classification_report(y_test, y_pred_before_smote))
  ```

  ![SVM_Before smote Confusion](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/5ca15720-e31d-4c6c-a0be-6e59297cb226)


  Step 6. Train SVM classifier after SMOTE <br>
  ```ruby
  svm_classifier_after_smote.fit(X_train_resampled_scaled, y_train_resampled)
  ```
  Step 7. Make predictions on the test set after SMOTE
  ```ruby
  y_pred_after_smote = svm_classifier_after_smote.predict(X_test_scaled)
  ```
  Step 8. Compute and print confusion matrix and classification report after SMOTE
  ```ruby
  print("Confusion Matrix and Classification Report after SMOTE:")
  print(confusion_matrix(y_test, y_pred_after_smote))
  print(classification_report(y_test, y_pred_after_smote))
  ```
  
  ![SVM_After SMOTE Confusion](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/071e71d2-8392-41c2-9f1a-0f4938a903e1)

  Step 9. Plot Confusion Metrics Before and After SMOTE
  ```ruby
  # Plot confusion matrices
  fig, axes = plt.subplots(1, 2, figsize=(12, 6))

  # Plot confusion matrix before SMOTE
  axes[0].imshow(confusion_matrix_before_smote, cmap=plt.cm.Blues, interpolation='nearest')
  axes[0].set_title('Confusion Matrix Before SMOTE')
  axes[0].set_xticks([0, 1])
  axes[0].set_yticks([0, 1])
  axes[0].set_xlabel('Predicted Label')
  axes[0].set_ylabel('True Label')
  for i in range(2):
      for j in range(2):
          axes[0].text(j, i, str(confusion_matrix_before_smote[i, j]),
                       horizontalalignment='center', verticalalignment='center', color='white')

  # Plot confusion matrix after SMOTE
  axes[1].imshow(confusion_matrix_after_smote, cmap=plt.cm.Blues, interpolation='nearest')
  axes[1].set_title('Confusion Matrix After SMOTE')
  axes[1].set_xticks([0, 1])
  axes[1].set_yticks([0, 1])
  axes[1].set_xlabel('Predicted Label')
  axes[1].set_ylabel('True Label')
  for i in range(2):
      for j in range(2):
          axes[1].text(j, i, str(confusion_matrix_after_smote[i, j]),
                       horizontalalignment='center', verticalalignment='center', color='white')

  plt.tight_layout()
  plt.show()
  ```

  ![Plot confusion metric SVM](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/e5a86814-f223-45ea-892e-22bda98e9af1)


  Step 10. Plot Accuracy Before and After SMOTE
  ```ruby
  # Get classification reports before and after SMOTE
  classification_report_before_smote = classification_report(y_test, y_pred_before_smote,   output_dict=True)
  classification_report_after_smote = classification_report(y_test, y_pred_after_smote, output_dict=True)

  # Extract accuracy values
  accuracy_before_smote = classification_report_before_smote['accuracy']
  accuracy_after_smote = classification_report_after_smote['accuracy']

  # Plot accuracy before and after SMOTE
  labels = ['Before SMOTE', 'After SMOTE']
  accuracy_scores = [accuracy_before_smote, accuracy_after_smote]

  plt.bar(labels, accuracy_scores, color=['blue', 'green'])
  plt.xlabel('SMOTE')
  plt.ylabel('Accuracy')
  plt.title('Accuracy of SVM before and after SMOTE')
  plt.ylim(0, 1)  # Limit y-axis from 0 to 1 for accuracy range
  plt.show()
  ```
  ![SVM Accuracy Before adn After SVM](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/0cee870f-92b6-4a87-87f0-d3ada2d971e9)

  > Advantages: <br>
  >> - Effective in High Dimensional Spaces <br>
  >> - Still effective in cases where number of dimensions is greater than the number of samples
  >> - Uses a subset of training points in the decision function/support vectors, so it is also memory efficient
  >> - Versatile: different kernel functions can be specified for the decision function.

  > Disadvantages: <br>
  >> - If the number of features is much greater than the number of samples, avoid over-fitting in choosing kernel functions and regularization term is crucial <br>
  >> - SVM do not directly provide probability estimates, these are calculated using an expensive five fold cross validation<br>

- Which algorithm is best for prediction? <br>
  | Logistic Regression | Neural Network | Support Vector Machine |
  | :---: | :---: | :---: | 
  | ![LogReg_Accuracy_Before and after smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/051a8bc0-2c44-4e54-a377-18e6c0e9e5bb) | ![NN_Diagram Accuracy before after smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/635bc08d-d78f-4b57-b6c2-c71549879242) | ![SVM Accuracy Before adn After SVM](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/ac82d963-2026-4273-bcdc-2ed9f84a5033) | <br>

  The best algorithms for predicion Binary Integer Data in this case is ***Neural Network + SMOTE*** with accuracy 98%. Based on the plotting of accuracy results between NN Before and After SMOTE, Neural Network can automatically learn relevant features from raw data and have a flexibility in various architectures which enables them to capture different types of patterns and structures in the data, making them adaptable to diverse classification tasks across various domains. In this model, impelenting Activation RelU Function in input layer, hidden layer and Acitvation Sigmoid Function in Output layer are the main reason why Neural Network is the most appropriate algorithms for classifying Target Labelled into binary ineteger data. <br>

   ![NN_Accuracy Before after smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/6c8ead2e-918c-4eb4-ba1f-c364b1270279)

## Evaluation
- What metrics evaluation is used in this project and how it works? <br> 
The metrics evaluation used are [Confusion Metrics, Accuracy, Precision, Sensitivity(Recall), Specificity and F1-Score](https://medium.com/javarevisited/evaluating-the-logistic-regression-ae2decf42d61). Those performance metrics are commonly used to evaluate a Binary Classification Model. Let's define each metric and how they work below: <br>
1. Confusion Metric: <br>
   A Tabular summary of True/False and Positive/Negative prediction rates. It allows to compute various performance metrics. <br>

   ![Basic-Confusion-matrix](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/2fd76ef0-c24e-4ba3-ae8a-0959bf5b1e9a)
   
2. Accuracy: <br>
measures the ratio of correct predictions from all predicted results. <br>

   ![accurcay score measuring](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/dd2b037c-cb5d-4cbd-a49c-547d67154a16)

3. Precision: <br>
measures what proportion of the positive predictions is actually positive. The precision score is useful for the succes of prediction when classes are very imbalanced and when it's significantly cost-efficient to identify all positive examples without any false positive. <br>

   ![precision formula](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/8d654914-c0eb-4047-95f6-e72aa5e9efbb)

4. Sensitivity/Recall: <br>
represents the model’s ability to correctly predict the positives out of actual positives. The higher the recall score, the better the machine learning model is at identifying positives. <br>
   ![recall formula](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/8a47bebf-2e71-4b39-8147-8d90b0ff3673)

5. Specificity: <br>
represents the model’s ability to correctly predict the negatives out of actual negatives. The higher the specificity score, the better the machine learning model is at identifying negatives. <br>

   ![specificity](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/0a7141f5-3bf6-4c89-bfcf-51010985190a)

6. F1 Score: <br>
combine the precision and recall of the model, and it is the harmonic mean of the precision and recall. It’s used often when data is imbalanced. <br>

   ![f1 score](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/4a047010-c742-47c0-a375-015bf2b223c8)

 
- Explanation of The Metrics Evaluation Project Results! <br>
  | X | Logistic Regression | Neural Network |  Support Vector Machine | 
  | :---: | :---: | :---: | :---: | 
  | Plot Accuracy |  ![LogReg_Accuracy_Before and after smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/051a8bc0-2c44-4e54-a377-18e6c0e9e5bb) | ![NN_Diagram Accuracy before after smote](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/635bc08d-d78f-4b57-b6c2-c71549879242) | ![SVM Accuracy Before adn After SVM](https://github.com/adinplb/Belajar-Machine-Learning-Terapan-Dicoding/assets/61041719/ac82d963-2026-4273-bcdc-2ed9f84a5033) |


  |   | Accuracy  | Precision  |  Recall |  F1-Score |
  |---|---|---|---|---|
  | Logistic Regression  | 0.81  | 0.86  | 0.81  | 0.82  |
  |  Logistic Regression +SMOTE | 0.95  |  0.95 | 0.95  | 0.95  |
  |  Neural Network | 0.81  | 0.86  | 0.81  | 0.82  |
  | Neural Network + SMOTE  |  0.97 | 0.98  | 0.97  | 0.97  |
  |  SVM | 0.69  | 0.47  |  0.69 | 0.56  |
  |  SVM +SMOTE | 0.95  | 0.95  | 0.95 | 0.95  |

  To racap, on the comparison of confusion matrix and accuracy values plot results above, Neural Network with SMOTE has the highest accuracy score and great confusion matrics so this algorithms is the most  suitable and approriate model for predictiong Breast Tumor Diagnosis using Quantitative Cell-Nuclear Phenotypes Features. The flexibility of Neural Network Architectures makes enables to capture different types of patterns/structures in dataset and learn relevant numerical features to predict Binary Integer Data whether it is Benign (0) or Malignant (1).

## Conclusion 
1. Not all features have an impact to the algorithms in the model prediction.
2. Neural Network with handling imbalanced data using SMOTE, give the greatest accuracy so this algorithm is the best model for predicting Breast Tumor Diagnosis.
3. Yes, SMOTE influences the high accuracy of the model.
