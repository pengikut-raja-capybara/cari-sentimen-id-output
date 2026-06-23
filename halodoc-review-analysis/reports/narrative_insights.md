# Laporan Insight Analisis Ulasan — Halodoc: Dokter, Obat & Lab

> Dibuat otomatis pada 2026-06-23 09:06:30 menggunakan gemini-3.1-flash-lite
> Sumber data: output/json/eda_summary.json

---

Berikut adalah laporan analisis data sentimen untuk aplikasi "Halodoc: Dokter, Obat & Lab" berdasarkan data periode 15 Juni 2023 hingga 15 Juni 2026.

---

## 1. Ringkasan Umum
Aplikasi Halodoc memiliki basis pengguna yang sangat loyal dengan total **15.629 ulasan**. Distribusi sentimen menunjukkan dominasi **sentimen positif sebesar 88,76%** (13.873 ulasan), diikuti sentimen negatif (9,78%) dan netral (1,46%).
*   **Polarisasi Rating:** Terdapat polarisasi yang sangat tajam di mana **83,6%** dari total ulasan memberikan rating bintang 5 (13.074 ulasan). Hal ini menunjukkan *brand advocacy* yang sangat kuat.
*   **Kepercayaan Data:** Model klasifikasi sentimen memiliki tingkat keyakinan (*confidence rate*) yang sangat tinggi, mencapai **97,34%**, sehingga data ini sangat valid untuk dijadikan dasar pengambilan keputusan.

## 2. Analisis Sentimen Negatif & Korelasi Versi
Masalah utama yang memicu frustrasi pengguna adalah kegagalan sistem transaksi dan aksesibilitas.
*   **Pain Point Utama:** Kegagalan akses ruang chat setelah pembayaran (552 ulasan) dan saldo terpotong namun sesi chat tidak tersedia (152 ulasan) menjadi kategori "Layanan Konsultasi Medis" yang paling krusial. Kata kunci seperti **"konsultasi"**, **"ribet"**, dan **"saldo"** mendominasi keluhan.
*   **Korelasi Versi:** Ulasan dengan versi **"Unknown"** menyumbang persentase negatif tertinggi sebesar **16,22%** dengan rata-rata rating rendah (4,28). Sementara itu, versi **21.9** yang memiliki 297 ulasan mencatat tingkat negatif **9,76%**. Ini mengindikasikan perlunya pembenahan pada *tracking* versi aplikasi agar kendala teknis lebih mudah teridentifikasi.

## 3. Analisis Temporal & Lonjakan (Spike Detection)
Tren bulanan menunjukkan stabilitas dengan rasio sentimen bersih rata-rata di atas 0,75. Namun, data *spike* menunjukkan adanya titik kritis:
*   **2024-04-19:** Terjadi lonjakan keluhan (6 ulasan negatif) dengan rata-rata rating sangat rendah (1,0) yang dipicu oleh kegagalan akses chat dan keterlambatan pengiriman obat.
*   **2023-06-20:** Lonjakan keluhan (5 ulasan negatif, rating 1,0) akibat bug teknis aplikasi.
Pola ini menunjukkan bahwa lonjakan negatif sangat berkorelasi dengan **kegagalan fungsionalitas inti** (transaksi/akses chat), bukan isu minor.

## 4. Analisis Sentimen Positif
Pengguna sangat mengapresiasi kemudahan akses kesehatan.
*   **Topik Utama:** "Membantu Sangat Sekali" (2.775 ulasan) dan "Good Ok Bagus" (2.228 ulasan) menjadi bukti kepuasan fungsional aplikasi. Kata kunci **"bagus"** dan **"membantu"** muncul secara konsisten.
*   **Resonansi Tinggi:** Topik "Halodoc Dokter Kasih" mencatat **992 total_thumbs_up** dari 902 ulasan, memberikan rasio *likes* per ulasan sebesar **1,1x**, yang menunjukkan bahwa narasi kemudahan konsultasi dengan dokter sangat disukai oleh komunitas.

## 5. Kinerja Customer Service
Performa CS sangat impresif dengan *average reply rate* mencapai **99,8%**.
*   **Responsivitas:** Kategori "Pengalaman Pengguna" memiliki respons tercepat dengan median delay hanya **0,36 jam**. Sebaliknya, kategori "Lain-lain / Noise" menjadi yang paling lambat (0,94 jam).
*   **Redireksi WA:** Hampir seluruh keluhan (99,67%) diarahkan ke WhatsApp, yang menunjukkan bahwa CS lebih memilih penyelesaian masalah secara personal dan real-time daripada melalui sistem *in-app chat* yang mungkin sedang bermasalah.

## 6. Rekomendasi Strategis
1.  **Perbaikan Backend Transaksi:** Prioritaskan perbaikan *callback system* antara *payment gateway* dan ruang chat. Keluhan "saldo terpotong tapi chat tidak ada" adalah *critical point* yang harus dihilangkan untuk menjaga kepercayaan pengguna.
2.  **Audit Versi Aplikasi:** Segera identifikasi 2.479 ulasan dengan versi "Unknown". Lakukan *mandatory update* atau pengetatan deteksi versi agar data *crash* lebih akurat.
3.  **Mekanisme Refund Otomatis:** Mengingat tingginya keluhan terkait pembayaran, buatlah sistem *self-service refund* di aplikasi untuk sesi chat yang gagal, guna mengurangi beban tim CS.
4.  **Optimasi SLA Respons:** Fokuskan penambahan SDM/Automasi untuk kategori "Layanan Pelanggan" yang memiliki *reply rate* terendah (98,41%).
5.  **Stabilisasi Pengiriman Obat:** Untuk masalah pengiriman obat, tingkatkan integrasi dengan API kurir pihak ketiga untuk memberikan *tracking* yang lebih transparan kepada pengguna, guna menekan keluhan terkait "keterlambatan pengiriman".
