# Laporan Insight Analisis Ulasan — EdLink

> Dibuat otomatis pada 2026-06-23 15:20:58 menggunakan gemini-3.1-flash-lite
> Sumber data: output/json/eda_summary.json

---

Berikut adalah laporan analisis data sentimen untuk aplikasi **EdLink**:

## 1. Ringkasan Umum
Analisis ini mencakup **2.667 ulasan** yang dikumpulkan antara **23 Februari 2017 hingga 15 Juni 2026**. Distribusi sentimen menunjukkan polarisasi yang tajam: **47,17% positif** (1.258 ulasan) dan **42,56% negatif** (1.135 ulasan), dengan sisanya netral. Terdapat polarisasi ekstrem pada rating; pengguna cenderung memberikan rating **5 bintang (1.014 ulasan)** atau **1 bintang (875 ulasan)**, yang mengindikasikan pengalaman pengguna yang sangat kontras antara kepuasan tinggi dan frustrasi mendalam. Model klasifikasi sentimen memiliki tingkat kepercayaan yang sangat tinggi dengan **overall_confident_rate sebesar 98,54%**.

## 2. Analisis Sentimen Negatif & Korelasi Versi
Pengguna melaporkan beberapa *pain point* utama yang didominasi oleh kata kunci seperti *"eror"*, *"tugas"*, dan *"mohon"*:
1. **Gagal mengunggah tugas dan file tidak terbaca** (143 ulasan).
2. **Aplikasi sering mengalami error dan tidak stabil** (117 ulasan).
3. **Loading aplikasi lambat meskipun koneksi internet stabil** (93 ulasan).
4. **Pengguna tidak bisa masuk atau login ke aplikasi** (92 ulasan).

Korelasi terhadap performa teknis terlihat jelas pada versi aplikasi. **Versi 4.5.5** menjadi titik terendah dengan rata-rata rating hanya **2,62** dan persentase ulasan negatif mencapai **57,48%**. Hal ini berbanding terbalik dengan **Versi 4.5.2** yang lebih stabil dengan rating **3,6** dan tingkat negatif yang lebih rendah di angka **29,57%**.

## 3. Analisis Temporal & Lonjakan (Spike Detection)
Tren sentimen bulanan selama 2026 menunjukkan performa yang cenderung stagnan di sisi negatif, di mana rasio sentimen bersih selalu berada di angka negatif (terendah di **-0,4167 pada Juni 2026**). Analisis lonjakan menemukan beberapa insiden kritis:
* **17 Maret 2021**: Terdapat **25 ulasan negatif** (rata-rata skor 1,32). Keluhan utama berpusat pada *kegagalan unggah tugas*, *aplikasi yang tidak stabil*, serta *data hilang setelah pembaruan*.
* **15 Oktober 2021**: Terdapat **19 ulasan negatif** (rata-rata skor 1,11). Fokus keluhan adalah pada *kegagalan unggah tugas* dan *kualitas aplikasi secara umum*.

## 4. Analisis Sentimen Positif
Pengguna yang puas sangat mengapresiasi fungsi inti aplikasi dengan kata kunci seperti *"bagus"*, *"good"*, dan *"nice"*.
* Topik utama adalah **aplikasi membantu proses perkuliahan dan pengecekan nilai** dengan **709 ulasan**. Topik ini memiliki resonansi yang sangat kuat, dibuktikan dengan **808 total thumbs up** (tertinggi di antara semua topik), yang menunjukkan validasi sosial dari komunitas mahasiswa.
* Pengguna juga menyukai kemudahan penggunaan secara umum (**87 ulasan**).

## 5. Kinerja Customer Service
Tim Customer Service memiliki komitmen tinggi dengan **avg_reply_rate 97,97%**.
* **Kategori Terbaik**: *Stabilitas Sistem* memiliki reply rate sempurna (**100%**).
* **Kategori Terlambat**: Respon untuk *gagal mengunggah tugas* memakan waktu **142,79 jam** (median delay), yang merupakan angka tertinggi, berbanding terbalik dengan kategori *Performa Aplikasi* yang memiliki respon tercepat dalam **40 jam**.
* **Redireksi WhatsApp**: Terdapat kecenderungan tinggi untuk mengarahkan pengguna ke WhatsApp (**61,15%**), terutama pada isu *gagal unggah tugas* (66,83%).


