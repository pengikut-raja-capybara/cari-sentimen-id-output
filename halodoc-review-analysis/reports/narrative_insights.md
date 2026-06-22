# Laporan Insight Analisis Ulasan — Halodoc: Dokter, Obat & Lab

> Dibuat otomatis pada 2026-06-22 23:42:22 menggunakan gemini-3.1-flash-lite
> Sumber data: output/json/eda_summary.json

---

Berikut adalah laporan analisis sentimen untuk aplikasi **Halodoc: Dokter, Obat & Lab** berdasarkan data periode 15 Juni 2023 hingga 15 Juni 2026.

---

## 1. Ringkasan Umum
Aplikasi ini memiliki basis pengguna yang sangat loyal dengan total **15.629 ulasan**. Distribusi sentimen sangat dominan ke arah **positif (88,76%)**, dengan rata-rata skor 4,94. Sebaliknya, sentimen negatif hanya menyumbang **9,78%**. 
*   **Distribusi Rating:** Terjadi polarisasi ekstrem di mana **83,65% (13.074)** ulasan memberikan rating bintang 5, sementara hanya 8,32% (1.300) yang memberikan bintang 1.
*   **Kepercayaan Data:** Model klasifikasi sentimen memiliki tingkat akurasi yang sangat solid dengan **overall_confident_rate sebesar 97,54%**, memberikan validitas tinggi pada temuan ini.

## 2. Analisis Sentimen Negatif & Korelasi Versi
Masalah utama yang mendasari kekecewaan pengguna (pain points) berfokus pada kegagalan teknis saat bertransaksi:
1.  **Kegagalan Sesi Konsultasi (371 ulasan):** Saldo terpotong tetapi akses konsultasi tidak terbuka.
2.  **Keterlambatan Pengiriman Obat (138 ulasan):** Masalah sistem pelacakan dan estimasi waktu kirim.
3.  **Ketidakresponsifan Dokter (137 ulasan):** Sesi hangus setelah pembayaran tanpa pengembalian dana (refund).

**Korelasi Versi:** Ulasan negatif tersebar di berbagai versi, namun versi **"Unknown"** menunjukkan persentase negatif tertinggi yaitu **16,22%** dengan rata-rata rating 4,28. Hal ini mengindikasikan adanya kelompok pengguna (kemungkinan pengguna lama atau perangkat tertentu) yang mengalami kendala teknis yang belum teridentifikasi versinya. Perlu diperhatikan juga versi **21.51** yang memiliki persentase negatif **7,84%**, lebih tinggi dibanding versi stabil seperti **22.6 (5,77%)**.

## 3. Analisis Temporal & Lonjakan (Spike Detection)
Tren sentimen bulanan menunjukkan stabilitas, namun terdapat fluktuasi pada Maret 2026 dengan jumlah ulasan negatif mencapai 39 ulasan.
**Spike Ulasan Negatif:**
*   **19 April 2024:** 6 ulasan negatif (rating 1,0). Topik utama: Ketidakjelasan status dokter (sibuk/tidak tersedia) setelah pembayaran berhasil.
*   **23 Juni 2023:** 5 ulasan negatif (rating 1,0). Topik utama: Kendala teknis login, OTP, dan fitur kalender menstruasi.
Lonjakan ini menunjukkan adanya "bug" sporadis atau gangguan pada sistem *gateway* pembayaran yang berinteraksi langsung dengan ketersediaan dokter.

## 4. Analisis Sentimen Positif
Pengguna sangat mengapresiasi kemudahan akses layanan kesehatan. Topik **"Membantu Sangat Sekali"** (2.679 ulasan) dan **"Good Ok Bagus"** (2.247 ulasan) menjadi pilar utama.
*   **Resonansi Sosial:** Topik **"Ramah Dan Dokter"** memiliki daya tarik yang sangat besar. Dengan **1.184 *thumbs up*** untuk 1.181 ulasan, rasio *likes*-nya mencapai **1,002x per ulasan**, menandakan bahwa keramahan dokter adalah *Unique Selling Point* yang paling divalidasi oleh sesama pengguna di kolom komentar.

## 5. Kinerja Customer Service
Performa CS sangat impresif dengan **avg_reply_rate 99,8%**.
*   **Kecepatan Respon:** Kategori **"Promosi dan Voucher"** adalah yang tercepat dengan median delay **0,16 jam**.
*   **Area Perbaikan:** Kategori **"Stabilitas Aplikasi"** memiliki *delay* respon terlama yakni **2,05 jam**. Meskipun tingkat redireksi ke WhatsApp sangat tinggi (99,67%), tim CS perlu memprioritaskan SLA untuk tiket terkait stabilitas aplikasi agar *user retention* tetap terjaga saat terjadi kendala teknis.

## 6. Rekomendasi Strategis
1.  **Perbaikan Produk (Payment-to-Service Sync):** Memperbaiki sinkronisasi antara *gateway* pembayaran dengan status sesi dokter. Jika pembayaran sukses namun dokter tidak merespons dalam X menit, sistem harus melakukan *auto-refund* atau pemindahan sesi ke dokter lain secara otomatis tanpa intervensi CS.
2.  **Optimasi Pengiriman:** Mengingat tingginya keluhan pengiriman, tingkatkan transparansi *tracking* *real-time* dan buat opsi pengiriman instan yang lebih terintegrasi.
3.  **Pengelolaan Versi:** Mewajibkan *tracking* versi aplikasi yang lebih akurat untuk ulasan agar tim pengembang dapat melakukan *rollback* segera jika versi terbaru (seperti varian "Unknown" yang negatifnya tinggi) menunjukkan anomali.
4.  **CS Automation:** Mengurangi beban tim CS dengan membuat *chatbot* khusus penanganan masalah "Saldo Terpotong" yang dapat memverifikasi status transaksi secara instan (self-service) agar CS bisa fokus pada masalah yang lebih kompleks.
5.  **Prioritas SLA:** Mengingat topik "Stabilitas Aplikasi" memiliki waktu respon terlama (2,05 jam), diperlukan peningkatan *buffer* tim teknis CS khusus untuk isu stabilitas guna mempercepat penyelesaian tiket yang berpotensi menyebabkan *churn*.
