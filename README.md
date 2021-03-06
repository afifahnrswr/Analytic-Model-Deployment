# Analytic-Model-Deployment

*Model Deployment* merupakan metode dalam pengintegrasian model *machine learning* yang merupakan salah satu tahap terakhir setelah mendapatkan model yang telah dioptimasi. Beberapa cara dalam mengimplementasikan model *machine learning* yaitu dengan menggunakan :
1. Rewriting (menulis ulang kembali model yang telah dibuat)
2. API / Application Programming Interface (antarmuka yang berupa sekumpulan fungsi yang dapat dijalankan menggunakan program lain)

Pada umumnya dalam melakukan *Model Deployment* dapat digambarkan sebagai berikut.
![image1](https://github.com/afifahnrswr/Analytic-Model-Deployment/blob/master/image/img1.JPG)

Pada Repository kali ini, akan membahas bagaimana membangun suatu model optimum *(Model Deployment)* yang telah diperoleh pada analisis Credit Scoring yang sudah pernah dilakukan. Hasil analisis yang sudah pernah dilakukan dapat diakses pada link berikut [Analisis Credit Scoring](https://github.com/afifahnrswr/Credit-Scoring/blob/master/19.09.04_Credit%20Scoring.ipynb). Berdasarkan hasil analisis, dapat diperoleh bahwa model terbaik yang dihasilkan dalam memprediksi apakah pelanggan kartu kredit beresiko terlambat atau tidak terlambat bayar pada bulan Mei dapat menggunakan pemodelan menggunakan **Random Forest**. Melakukan *Model Deployment* yang akan dilakukan pada Repository ini yaitu dengan membangun model menggunakan Web Framework API menggunakan Flask. Model dapat dijalankan menggunakan Aplikasi Postman.

Terdapat beberapa File pada Repository, diantaranya yaitu terdiri dari code dan dataset untuk melakukan Model Deployment di Python Anywhere dan Tes di Postman dan Folder Image sebagi pendukung.

# Outline 
1. Credit Scoring Model
2. Model Deployment
3. Test Model

## *Credit Scoring Model (Export to Pickle File)*
Setelah mendapatkan model terbaik, maka dapat melakukan *export* model menggunakan package "joblib". Untuk syntax dapat dilihat pada file "model.py". Menggunakan ![syntax](https://github.com/afifahnrswr/Analytic-Model-Deployment/blob/master/image/img2.JPG) maka akan diperoleh file Pickle "Model_RF.pkl" secara otomatis.

## *Model Deployment (PythonAnywhere)*
Jika ingin melakukan *Model Deployment* pada PythonAnywhere, maka dapat melakukan langkah-langkah sebagai berikut.
1. Melakukan *Sign Up* untuk Membuat Akun Baru
![image3](https://github.com/afifahnrswr/Analytic-Model-Deployment/blob/master/image/img3.JPG)
2. Menambahkan Web App *(Add a new web app)*
![image4](https://github.com/afifahnrswr/Analytic-Model-Deployment/blob/master/image/img4.JPG)
3. Install dependencies
![image5](https://github.com/afifahnrswr/Analytic-Model-Deployment/blob/master/image/img5.JPG)
4. Uplod File ("request.py", "server.py", "Model_RF.pkl") pada File "mysite"
![image6](https://github.com/afifahnrswr/Analytic-Model-Deployment/blob/master/image/img6.JPG)
5. MelakukanReload pada Web App
![image7](https://github.com/afifahnrswr/Analytic-Model-Deployment/blob/master/image/img7.JPG)

maka selanjutnya akan didapatkan Web untuk menggunakan model yang dapat diakses menggunakan Postman.

## *Test Model (Postman)* 
Setelah mendapatkan Web, maka dapat menjalankan model menggunakan Postman, untuk langkah-langkah dapat dilakukan sebagai berikut.
1. Membuka Aplikasi Postman [Postman](https://www.getpostman.com/). Mengganti *request method* menjadi POST dan input link API http://afifahnrswr11.pythonanywhere.com/api
![image8](https://github.com/afifahnrswr/Analytic-Model-Deployment/blob/master/image/img8.JPG)
2. Melakukan input data testing pada bagian Body - Row. Dan input data yang diinginkan pada laman tersebut.
![image9](https://github.com/afifahnrswr/Analytic-Model-Deployment/blob/master/image/img9.JPG)
3. Maka akan diperoleh hasil prediksi pada pemodelan Data Astra Credit Scoring menggunakan Pemodelan Random Forest. Untuk menghasilkan kode 1 maka akan diprediksi akan terlambat bayar dan sebaliknya, jika kode 0 maka akan diprediksi tidak terlambat bayar.
![image10](https://github.com/afifahnrswr/Analytic-Model-Deployment/blob/master/image/img10.JPG)

Selamat mencoba :)
