# Laporan Insight Analisis Ulasan — Vidio: Sports, Movies, Series

> Dibuat otomatis pada 2026-06-24 23:13:07 menggunakan openai/gpt-oss-120b:free
> Sumber data: output/json/eda_summary.json

---

## 1. Ringkasan Umum
- **Total ulasan**: 37.661 (periode 15‑Jun‑2023 sd 15‑Jun‑2026).  
- **Distribusi sentimen**  
  - Positif: 15.613 ulasan (**41,46 %**, rata‑rata skor 4,84)  
  - Negatif: 19.220 ulasan (**51,03 %**, rata‑rata skor 1,16)  
  - Netral: 2.828 ulasan (**7,51 %**, rata‑rata skor 3,0)  
- **Distribusi rating bintang**  
  - 1★ = 16.177 (43 %)  
  - 2★ = 3.043 (8 %)  
  - 3★ = 2.828 (8 %)  
  - 4★ = 2.562 (7 %)  
  - 5★ = 13.051 (35 %)  

  **Polarisasi** terlihat jelas: 43 % ulasan berada pada rating 1★, sementara hanya 35 % pada 5★. Ini menandakan kecenderungan kuat ke arah kepuasan rendah.  

- **Kepercayaan klasifikasi**  
  - Overall confidence = 97,2 %  
  - Positif = 95,2 % | Negatif = 98,7 % | Netral = 98,2 %  

  Tingkat kepercayaan tinggi memberikan keyakinan pada interpretasi sentimen di atas.

---

## 2. Analisis Sentimen Negatif & Korelasi Versi  
### Pain point utama (berdasarkan sub_issue)

| Peringkat | Sub‑issue (keluhan)                | Jumlah ulasan | Persentase dari total negatif |
|-----------|------------------------------------|---------------|------------------------------|
| 1 | **Tidak dapat menonton meski sudah berlangganan** | 4.959 | 25,8 % |
| 2 | **Tidak dapat menonton konten berbayar** (akses konten) | 1.730 | 9,0 % |
| 3 | **Aplikasi dianggap buruk/jelek** (kualitas aplikasi) | 1.784 | 9,3 % |
| 4 | **Tidak dapat menonton liga setelah bayar** (streaming bola) | 2.066 | 10,8 % |
| 5 | **Iklan terlalu lama/berlebih pada film** (iklan pada film) | 1.408 | 7,3 % |

**Kata kunci negatif** yang muncul paling sering: **“paket”, “menonton”, “saldo”, “iklan”, “bagus”**. Misalnya, kata *paket* dan *menonton* muncul di lebih dari 6.600 ulasan gabungan, menegaskan bahwa masalah langganan & akses konten adalah inti keluhan.

### Hubungan dengan versi aplikasi
- **Versi 6.26.10‑d1d18a1dc7**  
  - Review: 801 ulasan, **avg score 2,45**, **negatif = 60,05 %**.  
  - Keluhan paling dominan pada versi ini adalah **“Tidak dapat menonton meski sudah berlangganan”** (≈ 45 % dari negatif pada versi ini) dan **“Aplikasi dianggap buruk/jelek”**.  

- **Versi 6.42.11‑d5e79fc404**  
  - Review: 1.295 ulasan, **avg score 4,18**, **negatif = 16,06 %**.  
  - Pada versi ini, persentase keluhan “Tidak dapat menonton liga setelah bayar” turun drastis menjadi < 5 % serta laporan iklan berlebih berkurang signifikan, menandakan perbaikan pada modul pembayaran dan iklan.

**Insight**: Versi lama (6.26.10) menunjukkan tingkat keluhan langganan dan kualitas aplikasi yang sangat tinggi, sedangkan perbaikan pada versi 6.42.11 berhasil menurunkan proporsi ulasan negatif sampai di bawah 20 %.

---

## 3. Analisis Temporal & Lonjakan (Spike Detection)

### Tren bulanan (Jan‑Jun 2026)
- **Negatif** tetap mendominasi tiap bulan (≈ 55‑70 % dari total).  
- **Positif** menurun secara konsisten dari 319 (Jan) menjadi 133 (Jun).  
- **Net Sentiment Ratio** (positif‑negatif)/(total) berkisar **‑0,20 – ‑0,24**, menandakan sentimen negatif secara konsisten lebih kuat.

### Spike ulasan negatif
| Tanggal (YYYY‑MM‑DD) | Negatif (ulasan) | Avg score | Sub‑issue utama (keluhan) |
|----------------------|------------------|----------|---------------------------|
| **2024‑06‑22** | 158 | 1,06 | • Tidak dapat menonton meski sudah berlangganan  <br>• Aplikasi dianggap buruk/jelek  <br>• Aplikasi dianggap sampah |
| **2026‑01‑31** | 132 | 1,02 | • Aplikasi dianggap buruk/jelek  <br>• Tidak dapat menonton liga setelah bayar  <br>• Ingin uninstall karena iklan |

Kedua spike terjadi bersamaan dengan lonjakan keluhan “tidak dapat menonton” dan “iklan berlebihan”, yang cocok dengan kata kunci **“iklan”** dan **“menonton”** dalam analisis keyword.

---

## 4. Analisis Sentimen Positif
### Apa yang disukai pengguna
| Peringkat | Sub‑issue (apresiasi)                     | Jumlah ulasan | Rata‑rata skor |
|-----------|-------------------------------------------|---------------|----------------|
| 1 | **Pujian kualitas aplikasi** (Ulasan Umum Positif) | 3.047 | 4,89 |
| 2 | **Ekspresi kepuasan tinggi** (Ulasan Umum Positif) | 1.677 | 4,92 |
| 3 | **Kualitas film dan streaming** (Konten Film) | 1.150 | 4,85 |
| 4 | **Pujian aplikasi secara umum** (Ulasan Umum Positif) | 968 | 4,90 |
| 5 | **Kualitas TV / kanal** (Konten TV) | 830 | 4,65 |

**Kata kunci positif** yang menonjol: **“bagus”, “ok”, “oke”, “seru”, “top”**. Misalnya, kata *bagus* muncul di 5.432 ulasan positif, menegaskan bahwa kualitas visual & konten dianggap memuaskan.

### Resonansi tinggi
- Topik **“Kualitas film dan streaming”** memiliki **total_thumbs_up = 1.875** dengan **1.150 ulasan**, menghasilkan **rasio ~1,63 thumbs‑up per ulasan** (lebih dari satu like per komentar).  
- Topik **“Tidak dapat menonton / error playback”** pada kategori negatif (meski negatif) memiliki **total_thumbs_up = 16.442** dengan **1.004 ulasan**, yaitu **≈ 16,4 thumbs‑up per ulasan**, menandakan keluhan ini mendapatkan perhatian sangat tinggi dari komunitas.

---

## 5. Kinerja Customer Service
- **Reply rate keseluruhan**: 99,03 % (19.034/19.220 ulasan negatif).  
- **Median reply delay**: 1,22 jam (respons sangat cepat).  
- **Redirect ke WhatsApp**: 82,43 % (pengguna dialihkan ke WA untuk penyelesaian).

### Kategori dengan performa terbaik
| Kategori | Reply rate | Median delay (jam) | WA‑redirect |
|----------|------------|--------------------|-------------|
| **Login** (best rate) | 100,0 % | — | — |
| **Langganan Tidak Aktif** | 99,68 % | 1,26 | 88,71 % |
| **Kualitas Aplikasi** | 97,32 % | 1,17 | 85,51 % |

### Kategori dengan tantangan terbesar
| Kategori | Reply rate | Median delay (jam) | WA‑redirect |
|----------|------------|--------------------|-------------|
| **Konten Siaran** (worst rate) | 95,05 % | — | — |
| **Umum Positif** (slowest reply) | — | 1,55 | — |
| **Iklan pada Film** (lowest WA‑redirect) | 99,29 % | 1,00 | 61,95 % |

**Insight**: Meskipun hampir semua ulasan negatif mendapat balasan, variasi pada **waktu respons** (0,88 jam pada kategori “Tampilan” vs 1,55 jam pada “Umum Positif”) dan **tingkat redirect ke WA** (lebih tinggi pada masalah langganan vs rendah pada iklan film) dapat memengaruhi persepsi pengguna. Pengurangan delay, khususnya pada kategori “Umum Positif”, serta peningkatan redirect pada kasus iklan dapat meningkatkan kepuasan layanan.
