# Laporan Insight Analisis Ulasan — Halodoc: Dokter, Obat & Lab

> Dibuat otomatis pada 2026-06-23 20:53:56 menggunakan gemini-3.1-flash-lite
> Sumber data: output/json/eda_summary.json

---

Berikut adalah laporan analisis data sentimen untuk aplikasi **Halodoc: Dokter, Obat & Lab**.

---

## 1. Ringkasan Umum
Data mencakup **15.629 ulasan** yang dikumpulkan selama periode **15 Juni 2023 hingga 15 Juni 2026**. Distribusi sentimen menunjukkan dominasi positif yang sangat kuat sebesar **88,76% (13.873 ulasan)**, diikuti sentimen negatif **9,78% (1.528 ulasan)** dan netral **1,46% (228 ulasan)**. 

Terjadi polarisasi ekstrem pada distribusi rating: **83,65% (13.074)** dari total ulasan memberikan rating **bintang 5**, yang mengindikasikan loyalitas pengguna sangat tinggi. Tingkat kepercayaan klasifikasi model secara keseluruhan mencapai **0,9734**, mencerminkan akurasi tinggi dalam kategorisasi data.

## 2. Analisis Sentimen Negatif & Korelasi Versi
Pengguna yang memberikan ulasan negatif sering menggunakan kata kunci seperti **"konsultasi"**, **"ribet"**, dan **"saldo"**. Berikut adalah 3 *pain point* utama:
1. **Kegagalan akses ruang chat setelah pembayaran berhasil** (552 ulasan): Merupakan isu krusial yang paling banyak dikeluhkan.
2. **Saldo terpotong namun sesi chat tidak tersedia** (152 ulasan): Isu sistemik pada integrasi pembayaran.
3. **Bug aplikasi dan kendala akses fitur utama** (117 ulasan).

**Korelasi Versi:**
Versi aplikasi yang belum teridentifikasi (**Unknown**) menyumbang persentase negatif tertinggi sebesar **16,22%** dengan rata-rata rating **4,28**. Sementara itu, versi **21.51** memiliki persentase negatif **7,84%** dengan rating **4,61**, menunjukkan perlunya pembaruan stabilitas pada versi *legacy* atau tidak teridentifikasi untuk menekan angka kegagalan akses.

## 3. Analisis Temporal & Lonjakan (Spike Detection)
Tren sentimen bulanan menunjukkan stabilitas dengan *net sentiment ratio* rata-rata di kisaran 0,74 hingga 0,83. 
Dua lonjakan (*spike*) negatif signifikan yang terdeteksi:
* **19 April 2024**: Terjadi 6 ulasan negatif (rating rata-rata **1,0**), didominasi oleh keluhan terkait **kegagalan akses ruang chat setelah pembayaran berhasil** dan **keterlambatan pengiriman obat instan**.
* **3 Januari 2024**: Terjadi 6 ulasan negatif (rating rata-rata **1,33**), terutama mengenai **keterlambatan pengiriman obat instan** dan **kegagalan akses ruang chat**.

## 4. Analisis Sentimen Positif
Pengguna sangat mengapresiasi kemudahan aplikasi dengan kata kunci **"bagus"**, **"membantu"**, dan **"bermanfaat"**. Topik positif teratas meliputi:
1. **Ulasan positif mengenai manfaat aplikasi secara umum** (2.775 ulasan).
2. **Ulasan positif singkat mengenai kualitas layanan** (2.228 ulasan).
3. **Kemudahan akses konsultasi dokter secara daring** (1.395 ulasan).

Terdapat poin resonansi tinggi pada topik **apresiasi terhadap dokter dan kemudahan konsultasi**, yang memperoleh **992 *thumbs up*** (total *likes*). Jika dibandingkan dengan rata-rata *thumbs up* topik lain, topik ini memiliki daya tarik atau validasi komunitas yang sangat kuat.

## 5. Kinerja Customer Service
Secara umum, performa *Customer Service* (CS) sangat impresif dengan *avg reply rate* **99,8%** dan median waktu respon **0,62 jam**.
* **Responsivitas Terbaik:** Kategori **Promosi dan Voucher** mencatat waktu respon tercepat yaitu **0,21 jam**.
* **Responsivitas Terlambat:** Kategori **Lain-lain / Noise** memiliki waktu respon terlambat yaitu **0,94 jam**.
* **Tingkat Respon:** Kategori **Layanan Konsultasi Medis** menjadi yang paling responsif dengan *reply rate* **100%**, sedangkan **Layanan Pelanggan** memiliki *reply rate* terendah di angka **98,41%**, yang menunjukkan area untuk perbaikan komunikasi bagi tim CS.

Redireksi ke WhatsApp telah diimplementasikan dengan sangat baik, dengan tingkat redireksi mencapai **99,67%**, memastikan pengguna mendapatkan bantuan personal setelah kendala terdeteksi.
