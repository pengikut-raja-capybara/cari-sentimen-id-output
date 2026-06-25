# Laporan Insight Analisis Ulasan — JMO (Jamsostek Mobile)

> Dibuat otomatis pada 2026-06-25 11:40:56 menggunakan gemini-3.1-flash-lite
> Sumber data: output/json/eda_summary.json
> ⚠️ **Catatan Cakupan Data:** Analisis ini hanya mencakup ulasan yang memiliki teks komentar. Ulasan dengan rating tanpa komentar tidak diikutsertakan, sehingga distribusi sentimen mencerminkan pengguna yang aktif memberikan pendapat dan dapat condong ke arah negatif dibanding populasi pengguna keseluruhan.

---

Berikut adalah laporan analisis data sentimen untuk aplikasi **JMO (Jamsostek Mobile)** berdasarkan data periode 15 Juni 2025 hingga 15 Juni 2026.

---

## 1. Ringkasan Umum

Aplikasi JMO menerima total **80.637 ulasan** dalam setahun terakhir. Distribusi sentimen menunjukkan dominasi **sentimen positif sebesar 75,09% (60.550 ulasan)**, diikuti oleh **sentimen negatif 20,3% (16.369 ulasan)**, dan **sentimen netral 4,61% (3.718 ulasan)**.

Distribusi rating menunjukkan polarisasi yang kuat dengan **68,02% ulasan memberikan rating bintang 5 (54.854 ulasan)**. Sebaliknya, terdapat pula akumulasi rating bintang 1 yang signifikan sebanyak **16,62% (13.402 ulasan)**, menunjukkan adanya segmen pengguna yang sangat loyal berhadapan dengan kelompok yang mengalami kendala teknis krusial. Secara keseluruhan, model klasifikasi memiliki tingkat kepercayaan (**confidence rate**) yang sangat tinggi di angka **97,7%**.

---

## 2. Analisis Sentimen Negatif & Korelasi Versi

Masalah utama yang mendominasi keluhan pengguna berkaitan erat dengan stabilitas sistem pasca-pembaruan. Berikut adalah _pain points_ utama:

- **Pengguna gagal masuk ke aplikasi setelah melakukan pembaruan**: 5.701 ulasan.
- **Aplikasi tidak dapat dibuka setelah proses pembaruan selesai**: 4.659 ulasan.
- **Aplikasi terus menerus meminta pembaruan secara berulang**: 1.070 ulasan.

Kata kunci seperti **"dibuka"**, **"update"**, **"buka"**, **"tolong"**, dan **"login"** mendominasi keluhan, mencerminkan frustrasi pengguna yang terhambat aksesnya.
**Korelasi Versi:** Versi **4.15.5** menjadi versi paling bermasalah dengan **25,18% ulasan negatif** dan rata-rata rating hanya **3,85**. Sebagai perbandingan, versi **4.15.14** jauh lebih stabil dengan persentase ulasan negatif yang jauh lebih rendah, yakni **11,97%**, dan rating rata-rata **4,41**.

---

## 3. Analisis Temporal & Lonjakan (Spike Detection)

Tren bulanan menunjukkan fluktuasi stabilitas, di mana rasio sentimen bersih (net sentiment) anjlok ke titik terendah pada **Mei 2026 (0,3881)**, bertepatan dengan kenaikan tajam ulasan negatif.

**Lonjakan ulasan negatif signifikan terjadi pada:**

- **24 Juni 2025:** Terdapat **318 ulasan negatif** dengan rata-rata rating **1,17**. Isu utama adalah kegagalan masuk dan aplikasi yang tidak bisa dibuka setelah _update_.
- **29 Mei 2026:** Terjadi lonjakan serupa sebanyak **318 ulasan negatif** dengan rata-rata rating **1,21**, didominasi oleh kendala akses aplikasi pasca-pembaruan.

---

## 4. Analisis Sentimen Positif

Pengguna sangat mengapresiasi efisiensi yang ditawarkan JMO. Topik positif yang paling disukai adalah:

- **Ulasan positif umum mengenai pengalaman pengguna**: 23.776 ulasan.
- **Aplikasi dianggap sangat membantu dan bermanfaat**: 7.288 ulasan.
- **Ulasan positif mengenai kualitas aplikasi**: 6.694 ulasan.

Kata kunci seperti **"ok"**, **"keren"**, **"bagus"**, dan **"memuaskan"** sering muncul. Khusus untuk topik **"Kendala biometrik dan ketidaksesuaian data klaim JHT"**, meskipun kategorinya teknis, ia memiliki **7.674 total thumbs_up**. Mengingat jumlah ulasannya 978, topik ini memiliki rasio _thumbs_up_ per ulasan yang sangat tinggi (sekitar **7,8x lebih banyak** dibanding rata-rata ulasan lainnya), menandakan isu ini sangat krusial bagi komunitas pengguna.

---

## 5. Kinerja Customer Service

Performa CS mencatatkan _reply rate_ rata-rata sebesar **47,09%** dengan waktu respon median **24,74 jam**. Tingkat redireksi ke kanal bantuan lain sangat tinggi, yakni **74,26%**.

- **Reply Rate:** Kategori **Keluhan Layanan Pengguna** memiliki _reply rate_ tertinggi (**53,15%**), sementara kategori **Masalah Stabilitas Aplikasi** memiliki _reply rate_ terendah di antara kategori utama (**41,35%**).
- **Waktu Respon:** Respon tercepat diberikan pada kategori **Stabilitas Aplikasi** (median **13,63 jam**), sedangkan respon paling lambat terjadi pada kategori **Verifikasi Identitas** (median **88,97 jam**).

**Rekomendasi:** CS perlu mempercepat waktu respon untuk isu verifikasi identitas dan meningkatkan konsistensi reply rate pada topik teknis (stabilitas aplikasi) guna menurunkan volume ulasan negatif yang berulang.
