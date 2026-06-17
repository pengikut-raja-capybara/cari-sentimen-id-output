# 📊 Alfagift vs Klik Indomaret: Analisis Komparatif Ulasan Play Store (2023–2026)

Proyek ini menyajikan analisis komparatif pengalaman pengguna (retail experience) dan kinerja layanan digital dari dua aplikasi e-grocery/ritel modern terbesar di Indonesia, yaitu **Alfagift (Alfamart)** dan **Klik Indomaret (Indomaret)** untuk periode data **15 Juni 2023 hingga 14 Juni 2026**.

Analisis dan pemrosesan data dalam proyek ini merupakan hasil dari **[CaRI Sentimen ID](https://github.com/pengikut-raja-capybara/cari-sentimen-id)**.

### 🤖 Tentang CaRI Sentimen ID
**[CaRI Sentimen ID](https://github.com/pengikut-raja-capybara/cari-sentimen-id)** adalah tools untuk menganalisis ulasan aplikasi berbahasa Indonesia. Engine ini melakukan scraping ulasan, pemisahan sentimen, pemodelan topik dengan BERTopic + IndoBERT, pelabelan topik otomatis dengan LLM, dan menghasilkan ringkasan kategori bisnis yang siap dipakai untuk analisis BI dan evaluasi kinerja layanan.

Laporan hasil analisis disajikan dalam bentuk file laporan PDF setebal 12 halaman yang dirancang menggunakan pustaka `ReportLab` serta versi web HTML interaktif.

---

## 📌 Ringkasan KPI Utama (2023–2026)

| Parameter Pengalaman Pengguna | Aplikasi Alfagift | Aplikasi Klik Indomaret |
| :--- | :---: | :---: |
| **Total Volume Ulasan** | 93.649 ulasan | 39.993 ulasan |
| **Rata-rata Rating (Weighted)** | 4,37 dari 5,00 | 3,37 dari 5,00 |
| **Proporsi Ulasan Positif** | 77.713 ulasan (82,98%) | 22.757 ulasan (56,90%) |
| **Proporsi Ulasan Netral** | 2.092 ulasan (2,23%) | 1.506 ulasan (3,77%) |
| **Proporsi Ulasan Negatif** | 13.844 ulasan (14,78%) | 15.730 ulasan (39,33%) |

> [!NOTE]
> Klasifikasi topik dan analisis sentimen otomatis ini dibangun menggunakan arsitektur **NLP BERTopic** + **IndoBERT Embeddings** + pencocokan **Cosine Centroid**.

---

## 📁 Struktur Repositori

```text
├── csv-alfamart/          # Data CSV hasil mapping ulasan Alfagift per topik & sentimen
├── csv-indomaret/         # Data CSV hasil mapping ulasan Klik Indomaret per topik & sentimen
├── images/                # Output 12 visualisasi grafik analisis (.png)
│   ├── sentiment_comparison.png
│   ├── rating_trend.png
│   ├── top_negative_categories.png
│   ├── top_positive_categories.png
│   ├── promo_value.png
│   ├── stock_loyalty.png
│   ├── delivery_omnichannel.png
│   ├── tech_issues.png
│   ├── cs_performance_rr_delay.png
│   ├── cs_category_rr.png
│   ├── cs_redirection_channels.png
│   └── spike_timeline.png
├── analyze_metrics.py     # Script Python untuk membaca CSV, memproses metrik, dan membuat grafik
├── generate_pdf.py        # Script Python untuk merancang dan merender laporan PDF 12 halaman
├── comparative_analysis_report.md   # Laporan lengkap versi Markdown (Bahasa Indonesia)
├── comparative_analysis_report.pdf  # Laporan akhir versi PDF terkompilasi
└── README.md              # Dokumentasi proyek (file ini)
```

---

## 🛠️ Instalasi & Persyaratan

Pastikan Anda telah menginstal Python (minimal versi 3.8) pada sistem Anda. 

### 1. Kloning Repositori
```bash
git clone https://github.com/pengikut-raja-capybara/cari-sentimen-id-output.git
cd cari-sentimen-id-output/alfagift-vs-klik-indomaret
```

### 2. Instalasi Library Dependensi
Instal pustaka-pustaka Python yang diperlukan:
```bash
pip install pandas numpy matplotlib reportlab
```

---

## 🚀 Cara Menjalankan Proyek

Proyek ini terbagi menjadi dua langkah eksekusi utama:

### Langkah 1: Regenerasi Visualisasi Grafik
Jalankan script analisis metrik untuk membaca database ulasan dan memperbarui 12 grafik visualisasi di dalam folder `images/`:
```bash
python analyze_metrics.py
```

### Langkah 2: Pembuatan Laporan PDF
Jalankan script ReportLab untuk merender dokumen PDF laporan komparatif 12 halaman dengan layout terstruktur, tabel KPI, bagan grafik, dan konten analisis:
```bash
python generate_pdf.py
```
Setelah script selesai berjalan, file laporan baru akan diperbarui di [comparative_analysis_report.pdf](comparative_analysis_report.pdf).

---

## 🔍 Sorotan Analisis Utama

* **Karakteristik Keluhan**: Ulasan negatif **Alfagift** didominasi masalah operasional fisik (**Layanan Pengiriman** sebanyak 5.645 ulasan), sedangkan **Klik Indomaret** didominasi kendala stabilitas teknologi (**Performa Aplikasi** sebanyak 6.565 ulasan).
* **Isu Keamanan Alfagift**: Terdeteksi anomali error **Error 70007 (Root Detection)** yang sangat sensitif pasca pembaruan sistem keamanan, sehingga memblokir akses pengguna non-root yang mengaktifkan opsi debugging USB atau utilitas backend.
* **Kecepatan & Rasio Layanan CS**: 
  * Admin **Alfagift CS** membalas **73,04%** keluhan dengan median waktu tunda **10,93 jam**, serta menyertakan tiket pelacakan terintegrasi ke asisten virtual *Shalma*.
  * Admin **Klik Indomaret CS** merespons sangat cepat dengan median waktu **20 menit**, namun rasio tanggapannya rendah (**43,22%**) dan menggunakan template pengalihan generik ke call center / email.
* **Anomali Rating Bintang 5 Paksaan**: Ditemukan bukti ulasan tidak organik di Play Store Klik Indomaret yang dipaksa oleh manajemen internal/atasan toko agar staf internal memberikan rating bintang 5 meskipun isi ulasannya berupa keluhan teknis aplikasi.
