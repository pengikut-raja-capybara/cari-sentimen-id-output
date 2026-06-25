# Laporan Insight Analisis Ulasan — Vidio: Sports, Movies, Series

> Dibuat otomatis pada 2026-06-23 21:28:32 menggunakan gemini-3.1-flash-lite
> Sumber data: output/json/eda_summary.json

---

Berikut adalah laporan analisis data sentimen untuk aplikasi **Vidio: Sports, Movies, Series** berdasarkan data periode 15 Juni 2023 hingga 15 Juni 2026.

---

## 1. Ringkasan Umum
Aplikasi Vidio mencatatkan total **37.661 ulasan** dengan distribusi sentimen yang cenderung negatif, di mana **51,03% (19.220 ulasan)** bersifat negatif, **41,46% (15.613 ulasan)** positif, dan **7,51% (2.828 ulasan)** netral. 

Terdapat polarisasi ekstrem pada rating: bintang 1 mendominasi dengan **16.177 ulasan**, diikuti oleh bintang 5 sebanyak **13.051 ulasan**. Model klasifikasi sentimen memiliki tingkat kepercayaan yang sangat tinggi dengan **overall_confident_rate sebesar 0,97**, memastikan data yang dianalisis memiliki validitas yang kuat.

## 2. Analisis Sentimen Negatif & Korelasi Versi
Pengguna menghadapi hambatan utama pada pengalaman bertransaksi dan kualitas teknis aplikasi dengan kata kunci dominan: **menonton, beli, paket, bayar,** dan **iklan**. Berikut *pain point* utamanya:
*   **Paket langganan tidak aktif atau tidak terbaca sistem**: 10.539 ulasan (kategori: Masalah Langganan dan Akses).
*   **Kualitas aplikasi secara umum dinilai buruk**: 4.154 ulasan (kategori: Kualitas Aplikasi).
*   **Frekuensi iklan yang terlalu banyak dan mengganggu**: 1.675 ulasan (kategori: Pengalaman Pengguna).

**Korelasi Versi:** Versi **6.26.10-d1d18a1dc7** menunjukkan performa yang cukup mengkhawatirkan dengan rata-rata rating hanya **2,45** dan persentase ulasan negatif mencapai **60,05%**. Sebaliknya, versi **6.42.11-d5e79fc404** lebih stabil dengan rating **4,18** dan persentase negatif yang jauh lebih rendah, yakni **16,06%**. Hal ini mengindikasikan adanya regresi kualitas pada update tertentu.

## 3. Analisis Temporal & Lonjakan (Spike Detection)
Tren sentimen bulanan selama semester pertama 2026 menunjukkan kondisi **net-negatif** yang konsisten, di mana volume ulasan negatif selalu lebih tinggi dibandingkan ulasan positif.

Dua lonjakan (*spike*) negatif terbesar terjadi pada:
*   **22 Juni 2024**: Terjadi **158 ulasan negatif** dengan rata-rata rating **1,06**. Topik utamanya adalah paket langganan tidak aktif, kualitas aplikasi buruk, dan loading yang lama.
*   **31 Januari 2026**: Terdapat **132 ulasan negatif** dengan rata-rata rating **1,02**. Topik utamanya adalah kualitas aplikasi buruk, ketidaksesuaian akses konten berbayar untuk siaran bola, dan paket langganan tidak terbaca sistem.

## 4. Analisis Sentimen Positif
Pengguna memberikan apresiasi tinggi pada kemudahan akses konten dengan kata kunci seperti **seru, bagus, film,** dan **ok**.
*   **Ulasan positif umum mengenai aplikasi**: 9.063 ulasan.
*   **Kemudahan akses menonton film dan siaran langsung**: 4.072 ulasan (kategori: Pengalaman Menonton).

Terdapat fenomena resonansi tinggi pada topik "Kemudahan akses menonton film dan siaran langsung" yang mendapatkan total **9.125 *thumbs up***. Jika dibandingkan dengan jumlah ulasannya, topik ini memiliki rasio keterlibatan yang sangat kuat, menunjukkan bahwa kepuasan akan kemudahan akses konten merupakan *value proposition* utama yang paling dirasakan pengguna.

## 5. Kinerja Customer Service
Layanan pelanggan menunjukkan dedikasi tinggi dengan **avg_reply_rate mencapai 99,03%**. 
*   **Efisiensi Respon**: Median waktu respon tercepat berada pada kategori "Lain-lain / Noise" (**0,98 jam**), sementara respon paling lambat terjadi pada kategori "Kepuasan Pengguna" (**1,42 jam**). 
*   **Variasi Kinerja**: Kategori "Kepuasan Pengguna" menjadi yang paling responsif dalam hal kuantitas (**100% reply rate**), namun kategori "Kualitas Aplikasi" memiliki *reply rate* terendah di angka **97,88%**.
*   **Redireksi WhatsApp**: Tingkat redireksi ke WhatsApp sangat tinggi pada kategori "Masalah Langganan dan Akses" (**87,64%**), yang menunjukkan bahwa tim pendukung sadar masalah teknis akses memerlukan penanganan personal melalui kanal privat dibandingkan di kolom ulasan publik.
