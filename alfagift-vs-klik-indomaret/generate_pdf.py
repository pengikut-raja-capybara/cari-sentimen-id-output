import os
import re
import pandas as pd
import numpy as np
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Image
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# ============================================================================
# CONSTANTS & COLOR PALETTE
# ============================================================================
PRINTABLE_WIDTH = 487.27
PRIMARY_COLOR = colors.HexColor("#1E293B")    # Slate 900
SECONDARY_COLOR = colors.HexColor("#B91C1C")  # Alfamart Red (Red 700)
TEXT_COLOR = colors.HexColor("#334155")       # Slate 700
LIGHT_BG = colors.HexColor("#F8FAFC")         # Slate 50
BORDER_COLOR = colors.HexColor("#E2E8F0")     # Slate 200
ACCENT_BLUE = colors.HexColor("#1D4ED8")      # Klik Indomaret Blue (Blue 700)

# ============================================================================
# NUMBERED CANVAS (header/footer)
# ============================================================================
class NumberedCanvas(canvas.Canvas):
    """ Canvas implementation for dynamic page footer numbers and headers """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return  # Skip cover page
            
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(PRIMARY_COLOR)
        
        # Header
        self.drawString(54, 800, "LAPORAN KOMPARATIF: ALFAGIFT VS KLIK INDOMARET (2023–2026)")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.75)
        self.line(54, 792, 541.27, 792)
        
        # Footer
        self.drawString(54, 40, "Alfiansah Tech Solution")
        page_text = f"Halaman {self._pageNumber} dari {page_count}"
        self.drawRightString(541.27, 40, page_text)
        self.line(54, 52, 541.27, 52)
        
        self.restoreState()

# ============================================================================
# COVER PAGE BACKGROUND
# ============================================================================
def draw_cover_background(canvas_obj, doc):
    """ Draw premium cover page background layout """
    canvas_obj.saveState()
    
    # 1. Full page Deep Slate Navy background
    canvas_obj.setFillColor(colors.HexColor("#0F172A"))
    canvas_obj.rect(0, 0, 595.27, 841.89, fill=True, stroke=False)
    
    # 2. Teal accent polygon bottom-right
    canvas_obj.setFillColor(SECONDARY_COLOR)
    p = canvas_obj.beginPath()
    p.moveTo(250, 0)
    p.lineTo(595.27, 0)
    p.lineTo(595.27, 450)
    p.close()
    canvas_obj.drawPath(p, fill=True, stroke=False)
    
    # 3. Second polygon in bottom-left
    canvas_obj.setFillColor(colors.HexColor("#1E293B"))
    p = canvas_obj.beginPath()
    p.moveTo(0, 0)
    p.lineTo(350, 0)
    p.lineTo(0, 350)
    p.close()
    canvas_obj.drawPath(p, fill=True, stroke=False)

    # 4. Bright blue accent stripe at the top
    canvas_obj.setFillColor(ACCENT_BLUE)
    canvas_obj.rect(54, 720, 80, 8, fill=True, stroke=False)
    
    # 5. Bottom accent line
    canvas_obj.rect(54, 54, PRINTABLE_WIDTH, 1.5, fill=True, stroke=False)

    canvas_obj.restoreState()

# ============================================================================
# PDF BUILDER
# ============================================================================
def build_report_pdf():
    pdf_path = r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\comparative_analysis_report.pdf"
    
    print("[INFO] Creating PDF template...")
    # Initialize Document Templates
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Paragraph Styles
    styles.add(ParagraphStyle(
        name='CoverBrand', fontName='Helvetica-Bold', fontSize=15, leading=19,
        textColor=ACCENT_BLUE, spaceAfter=10
    ))
    styles.add(ParagraphStyle(
        name='CoverTitle', fontName='Helvetica-Bold', fontSize=26, leading=32,
        textColor=colors.white, spaceAfter=18
    ))
    styles.add(ParagraphStyle(
        name='CoverSubtitle', fontName='Helvetica', fontSize=11, leading=16,
        textColor=colors.HexColor("#94A3B8"), spaceAfter=120
    ))
    styles.add(ParagraphStyle(
        name='CoverMetadata', fontName='Helvetica', fontSize=9.5, leading=15,
        textColor=colors.HexColor("#F1F5F9"),
    ))
    styles.add(ParagraphStyle(
        name='ReportH1', fontName='Helvetica-Bold', fontSize=13, leading=17,
        textColor=PRIMARY_COLOR, spaceBefore=10, spaceAfter=8, keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='ReportH2', fontName='Helvetica-Bold', fontSize=10.5, leading=14,
        textColor=SECONDARY_COLOR, spaceBefore=8, spaceAfter=5, keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='ReportBody', fontName='Helvetica', fontSize=9.0, leading=13.0,
        textColor=TEXT_COLOR, spaceAfter=8
    ))
    styles.add(ParagraphStyle(
        name='ReportBullet', fontName='Helvetica', fontSize=9.0, leading=13.0,
        leftIndent=15, firstLineIndent=-10, textColor=TEXT_COLOR, spaceAfter=4
    ))
    styles.add(ParagraphStyle(
        name='TableHeader', fontName='Helvetica-Bold', fontSize=8.0, leading=10,
        textColor=colors.white, alignment=1
    ))
    styles.add(ParagraphStyle(
        name='TableCell', fontName='Helvetica', fontSize=8.0, leading=10,
        textColor=TEXT_COLOR,
    ))
    styles.add(ParagraphStyle(
        name='TableCellBold', fontName='Helvetica-Bold', fontSize=8.0, leading=10,
        textColor=TEXT_COLOR,
    ))
    styles.add(ParagraphStyle(
        name='TableCellCenter', fontName='Helvetica', fontSize=8.0, leading=10,
        textColor=TEXT_COLOR, alignment=1
    ))
    
    flowables = []
    
    # ------------------------------------------------------------------------
    # PAGE 1: COVER PAGE
    # ------------------------------------------------------------------------
    flowables.append(Spacer(1, 75))
    flowables.append(Paragraph("CaRI Sentiment ID", styles['CoverBrand']))
    flowables.append(Paragraph(
        "LAPORAN ANALISIS KOMPARATIF<br/>ALFAGIFT VS KLIK INDOMARET", 
        styles['CoverTitle']))
    
    flowables.append(Paragraph(
        "Analisis Pengalaman Pengguna Ritel dan Efektivitas Layanan Digital<br/>"
        "Berbasis Ulasan Google Play Store (Rentang Data 2023–2026)", 
        styles['CoverSubtitle']))
    
    pub_date = datetime.now().strftime("%d %B %Y, %H:%M WIB")
    months_id = {
        'January': 'Januari', 'February': 'Februari', 'March': 'Maret', 'April': 'April',
        'May': 'Mei', 'June': 'Juni', 'July': 'Juli', 'August': 'Agustus',
        'September': 'September', 'October': 'Oktober', 'November': 'November', 'December': 'Desember'
    }
    for en, id_val in months_id.items():
        pub_date = pub_date.replace(en, id_val)
        
    metadata_text = f"""
    <font color="#94A3B8">Disiapkan untuk:</font><br/>
    <b>Publik</b><br/><br/>
    
    <font color="#94A3B8">Sumber Data:</font><br/>
    <b>Google Play Store Reviews (15 Juni 2023 – 14 Juni 2026)</b><br/><br/>

    <font color="#94A3B8">Metodologi:</font><br/>
    <b>NLP BERTopic + IndoBERT Embeddings + Cosine Centroid</b><br/><br/>
    
    <font color="#94A3B8">Dibuat:</font><br/>
    <b>{pub_date}</b>
    """
    flowables.append(Paragraph(metadata_text, styles['CoverMetadata']))
    flowables.append(PageBreak())
    
    # ------------------------------------------------------------------------
    # PAGE 2: Pendahuluan & Ringkasan KPI Retail Experience
    # ------------------------------------------------------------------------
    flowables.append(Paragraph("PENGANTAR METODOLOGI & KPI UTAMA RETAIL EXPERIENCE", styles['ReportH1']))
    flowables.append(Spacer(1, 4))
    
    flowables.append(Paragraph(
        "<b>Disclaimer Metodologi</b><br/>"
        "Laporan komparatif ini disusun menggunakan data ulasan pengguna aplikasi Alfagift dan Klik Indomaret yang dipublikasikan di Google Play Store selama periode tiga tahun, terhitung sejak 15 Juni 2023 hingga 14 Juni 2026. Klasifikasi kategori ulasan dan analisis sentimen dilakukan secara otomatis menggunakan pemodelan bahasa alami (NLP) berbasis algoritma BERTopic yang dikombinasikan dengan IndoBERT Embeddings dan pencocokan Cosine Centroid untuk memastikan pengelompokan topik yang akurat. Tingkat kepercayaan klasifikasi model divalidasi guna meminimalkan margin kesalahan klasifikasi ulasan pengguna.<br/><br/>"
        "Laporan publik ini memanfaatkan analisis otomatis berbasis AI. Hasilnya bersifat indikatif, dapat mengandung ketidakakuratan, dan tidak menggantikan verifikasi atau penilaian profesional masing-masing pihak.", 
        styles['ReportBody']))
    
    flowables.append(Paragraph(
        "<b>Tujuan Laporan</b><br/>"
        "Laporan ini bertujuan untuk memetakan secara objektif perbandingan pengalaman pengguna (retail experience) dan kinerja pelayanan digital (digital service response) dari kedua platform ritel modern tersebut. Fokus analisis diarahkan pada identifikasi pola ulasan positif, kategori keluhan negatif utama, serta respon dari masing-masing unit layanan pelanggan dalam menanggapi keluhan pengguna di Google Play Store tanpa menyertakan penilaian subjektif atau rekomendasi strategis.", 
        styles['ReportBody']))
    
    flowables.append(Spacer(1, 4))
    flowables.append(Paragraph("<b>Tabel KPI Retail Experience (2023–2026)</b>", styles['ReportH2']))
    
    kpi_data = [
        [Paragraph("Parameter Pengalaman Pengguna", styles['TableHeader']), 
         Paragraph("Aplikasi Alfagift", styles['TableHeader']), 
         Paragraph("Aplikasi Klik Indomaret", styles['TableHeader'])],
        
        [Paragraph("<b>Total Volume Ulasan</b>", styles['TableCellBold']), 
         Paragraph("93.649 ulasan", styles['TableCellCenter']), 
         Paragraph("39.993 ulasan", styles['TableCellCenter'])],
        
        [Paragraph("<b>Rata-rata Rating (Weighted)</b>", styles['TableCellBold']), 
         Paragraph("4,37 dari 5,00", styles['TableCellCenter']), 
         Paragraph("3,37 dari 5,00", styles['TableCellCenter'])],
        
        [Paragraph("<b>Proporsi Ulasan Positif</b>", styles['TableCellBold']), 
         Paragraph("77.713 ulasan (82,98%)", styles['TableCellCenter']), 
         Paragraph("22.757 ulasan (56,90%)", styles['TableCellCenter'])],
        
        [Paragraph("<b>Proporsi Ulasan Netral</b>", styles['TableCellBold']), 
         Paragraph("2.092 ulasan (2,23%)", styles['TableCellCenter']), 
         Paragraph("1.506 ulasan (3,77%)", styles['TableCellCenter'])],
        
        [Paragraph("<b>Proporsi Ulasan Negatif</b>", styles['TableCellBold']), 
         Paragraph("13.844 ulasan (14,78%)", styles['TableCellCenter']), 
         Paragraph("15.730 ulasan (39,33%)", styles['TableCellCenter'])]
    ]
    
    col_widths_kpi = [207.27, 140, 140]
    t_kpi = Table(kpi_data, colWidths=col_widths_kpi)
    t_kpi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY_COLOR),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
    ]))
    flowables.append(t_kpi)
    flowables.append(Spacer(1, 10))
    
    flowables.append(Paragraph(
        "<b>Analisis Rating &amp; Sentimen Umum</b><br/>"
        "Berdasarkan data akumulasi ulasan selama periode 2023–2026, Alfagift mencatat volume ulasan yang lebih tinggi dengan indeks kepuasan pengguna yang tecermin dari rata-rata rating 4,37 serta dominasi sentimen positif mencapai 82,98%. Sebaliknya, Klik Indomaret mencatat total ulasan sebanyak 39.993 dengan rata-rata rating berada pada angka 3,37. Selisih kepuasan tersebut dipengaruhi oleh proporsi sentimen negatif pada Klik Indomaret yang mencatat angka 39,33%, lebih tinggi dibandingkan proporsi sentimen negatif Alfagift yang berada pada angka 14,78%.", 
        styles['ReportBody']))
    
    flowables.append(PageBreak())
    
    # ------------------------------------------------------------------------
    # PAGE 3: Tren Sentimen & Rating
    # ------------------------------------------------------------------------
    flowables.append(Paragraph("1. Retail experience: tren sentimen &amp; rating", styles['ReportH1']))
    flowables.append(Spacer(1, 4))
    
    flowables.append(Paragraph(
        "Berikut adalah ulasan perbandingan tren sentimen tahunan serta pergerakan rata-rata rating dari aplikasi Alfagift dan Klik Indomaret selama periode analisis 2023–2026. Data ini menggambarkan fluktuasi kepuasan pengguna dari tahun ke tahun yang dipengaruhi oleh kinerja operasional ritel dan kestabilan sistem aplikasi masing-masing platform.", 
        styles['ReportBody']))
    flowables.append(Spacer(1, 10))
    
    img1 = Image(r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images\sentiment_comparison.png", width=420, height=180)
    img1.hAlign = 'CENTER'
    flowables.append(img1)
    
    flowables.append(Spacer(1, 15))
    
    img2 = Image(r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images\rating_trend.png", width=420, height=180)
    img2.hAlign = 'CENTER'
    flowables.append(img2)
    
    flowables.append(PageBreak())
    
    # ------------------------------------------------------------------------
    # PAGE 4: Masalah Utama (Ulasan Negatif)
    # ------------------------------------------------------------------------
    flowables.append(Paragraph("1. Retail experience: masalah utama (negatif)", styles['ReportH1']))
    flowables.append(Spacer(1, 4))
    
    flowables.append(Paragraph(
        "Analisis ulasan negatif menunjukkan perbedaan karakteristik masalah utama antara kedua aplikasi. Klik Indomaret didominasi oleh kendala teknis sistem internal, sedangkan Alfagift lebih banyak dikeluhkan terkait layanan fisik pengiriman.", 
        styles['ReportBody']))
    
    flowables.append(Paragraph("<b>Kategori Keluhan Terbanyak</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Alfagift:</b> Didominasi kendala operasional pada Layanan Pengiriman (5.645 ulasan) dan Manajemen Akun (2.489 ulasan).", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Klik Indomaret:</b> Didominasi masalah teknis pada Performa Aplikasi (6.565 ulasan) dan Layanan Pengiriman (4.252 ulasan).", styles['ReportBullet']))
    
    flowables.append(Paragraph("<b>Kategori dengan Rating Terendah (Skala 5,00)</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Alfagift:</b> Kualitas Aplikasi (1,07) serta Program Promosi &amp; Cashback (1,07).", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Klik Indomaret:</b> Pengalaman Pengguna/UI-UX (1,01) dan Kepuasan Pelanggan umum (1,03).", styles['ReportBullet']))
    
    flowables.append(Spacer(1, 10))
    img3 = Image(r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images\top_negative_categories.png", width=440, height=210)
    img3.hAlign = 'CENTER'
    flowables.append(img3)
    
    flowables.append(PageBreak())
    
    # ------------------------------------------------------------------------
    # PAGE 5: Kekuatan Utama (Ulasan Positif)
    # ------------------------------------------------------------------------
    flowables.append(Paragraph("1. Retail experience: kekuatan utama (positif)", styles['ReportH1']))
    flowables.append(Spacer(1, 4))
    
    flowables.append(Paragraph(
        "Apresiasi positif pengguna mencerminkan keunggulan operasional ritel yang dirasakan langsung. Kedua platform memiliki pendorong sentimen positif yang sama, yaitu kenyamanan dan efisiensi belanja online dari rumah.", 
        styles['ReportBody']))
    
    flowables.append(Paragraph("<b>Pilar Utama Ulasan Positif</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Alfagift:</b> Kategori Kepuasan Pengguna (28.416 ulasan) dan Pengalaman Pengguna belanja online (21.085 ulasan) mendominasi secara signifikan.", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Klik Indomaret:</b> Didominasi oleh Kepuasan Pengguna (7.581 ulasan) dan Pengalaman Pengguna (6.984 ulasan).", styles['ReportBullet']))
    
    flowables.append(Paragraph("<b>Perbandingan Volume &amp; Skala Kepuasan</b>", styles['ReportH2']))
    flowables.append(Paragraph("• Volume apresiasi Alfagift jauh melampaui Klik Indomaret. Layanan Pengiriman &amp; Promo Alfagift menyumbang 16.299 ulasan positif dengan rating rata-rata 4,99.", styles['ReportBullet']))
    flowables.append(Paragraph("• Klik Indomaret mencatat ulasan positif pada Promosi &amp; Penawaran (2.313 ulasan; rating 4,98) serta Layanan Pengiriman (1.309 ulasan; rating 4,97).", styles['ReportBullet']))
    
    flowables.append(Spacer(1, 10))
    img4 = Image(r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images\top_positive_categories.png", width=440, height=200)
    img4.hAlign = 'CENTER'
    flowables.append(img4)
    
    flowables.append(PageBreak())
    
    # ------------------------------------------------------------------------
    # PAGE 6: Promo, Harga & Value
    # ------------------------------------------------------------------------
    flowables.append(Paragraph("1. Retail experience: promo, harga &amp; value", styles['ReportH1']))
    flowables.append(Spacer(1, 4))
    
    flowables.append(Paragraph(
        "Respon pengguna terhadap program promosi dan kebijakan harga memperlihatkan kontras yang signifikan antara kedua platform ritel.", 
        styles['ReportBody']))
    
    flowables.append(Paragraph("<b>Evaluasi Promo &amp; Harga Alfagift</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Sentimen Positif:</b> Sangat tinggi pada Layanan Pengiriman &amp; Promo (16.299 ulasan) serta Harga &amp; Promosi (1.456 ulasan; rating 5,00), didorong oleh gratis ongkir tanpa syarat ketat dan diskon langsung.", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Sentimen Negatif:</b> Tercatat keluhan minor terkait voucher atau poin tidak berfungsi pada kategori Promosi &amp; Loyalitas (644 ulasan).", styles['ReportBullet']))
    
    flowables.append(Paragraph("<b>Evaluasi Promo &amp; Harga Klik Indomaret</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Sentimen Positif:</b> Terkonsentrasi pada Promosi &amp; Penawaran (2.313 ulasan) dan Promosi &amp; Diskon (521 ulasan).", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Sentimen Negatif:</b> Keluhan menonjol pada Promosi &amp; Harga (267 ulasan; rating 1,13) akibat ketidaksesuaian harga katalog vs toko fisik, serta tidak munculnya fitur tebus murah setelah update.", styles['ReportBullet']))
    
    flowables.append(Spacer(1, 10))
    img5 = Image(r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images\promo_value.png", width=440, height=170)
    img5.hAlign = 'CENTER'
    flowables.append(img5)
    
    flowables.append(PageBreak())
    
    # ------------------------------------------------------------------------
    # PAGE 7: Stok, Fulfillment & Loyalty
    # ------------------------------------------------------------------------
    flowables.append(Paragraph("1. Retail experience: stok, fulfillment &amp; loyalty", styles['ReportH1']))
    flowables.append(Spacer(1, 4))
    
    flowables.append(Paragraph(
        "Pemenuhan pesanan dan program loyalitas pelanggan menjadi indikator penting dalam menjaga retensi pengguna di kedua aplikasi.", 
        styles['ReportBody']))
    
    flowables.append(Paragraph("<b>Manajemen Stok &amp; Ketersediaan Produk</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Alfagift:</b> Keluhan Ketersediaan Produk (278 ulasan negatif; rating 1,16) berfokus pada stok kosong item promo tebus murah dan persediaan air galon.", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Klik Indomaret:</b> Keluhan Manajemen Stok (123 ulasan negatif; rating 1,20) berpusat pada ketidaksesuaian stok aplikasi vs gerai fisik, yang memicu pembatalan pesanan sepihak oleh sistem tanpa konfirmasi.", styles['ReportBullet']))
    
    flowables.append(Paragraph("<b>Program Loyalitas &amp; Poin Reward</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Alfagift:</b> Keluhan poin error/gagal tukar voucher tercatat di kategori Promosi &amp; Loyalitas (644 ulasan) dan Program Loyalitas (201 ulasan; rating 1,14). Namun, ulasan positif loyalitas merek (Brand Loyalty) terkumpul 84 ulasan dengan rating 5,00.", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Klik Indomaret:</b> Tidak memiliki kategori loyalitas khusus; keluhan poin hilang menyatu dalam isu umum operasional pasca update aplikasi.", styles['ReportBullet']))
    
    flowables.append(Spacer(1, 10))
    img6 = Image(r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images\stock_loyalty.png", width=440, height=170)
    img6.hAlign = 'CENTER'
    flowables.append(img6)
    
    flowables.append(PageBreak())
    
    # ------------------------------------------------------------------------
    # PAGE 8: Pengiriman & Omnichannel
    # ------------------------------------------------------------------------
    flowables.append(Paragraph("1. Retail experience: pengiriman &amp; omnichannel", styles['ReportH1']))
    flowables.append(Spacer(1, 4))
    
    flowables.append(Paragraph(
        "Layanan logistik pengiriman dan integrasi online-to-offline (omnichannel) merupakan titik temu vital bagi kepuasan pelanggan e-grocery.", 
        styles['ReportBody']))
    
    flowables.append(Paragraph("<b>Performa Layanan Pengiriman (Logistik)</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Alfagift:</b> Kategori Layanan Pengiriman mengumpulkan 5.645 ulasan negatif (rating 1,16) akibat keterlambatan dan status pelacakan tidak akurat. Namun, terdapat 632 ulasan positif (rating 4,99) yang mengapresiasi keandalan kurir.", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Klik Indomaret:</b> Layanan Pengiriman mencatat 4.252 ulasan negatif (rating 1,11) karena keterlambatan pengiriman, diimbangi 1.309 ulasan positif (rating 4,97) yang memuji keramahan kurir gerai.", styles['ReportBullet']))
    
    flowables.append(Paragraph("<b>Tantangan Integrasi Omnichannel</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Disparitas Harga:</b> Isu ketidaksesuaian harga antara katalog aplikasi dan toko fisik dikeluhkan pengguna Klik Indomaret (267 ulasan) serta Alfagift (106 ulasan).", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Cakupan Layanan &amp; Staf:</b> Alfagift mencatat 160 keluhan terkait area pengiriman terbatas. Klik Indomaret menerima 21 ulasan negatif terkait perilaku staf toko atau kurir.", styles['ReportBullet']))
    
    flowables.append(Spacer(1, 10))
    img7 = Image(r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images\delivery_omnichannel.png", width=440, height=170)
    img7.hAlign = 'CENTER'
    flowables.append(img7)
    
    flowables.append(PageBreak())
    
    # ------------------------------------------------------------------------
    # PAGE 9: KPI Kinerja Digital Service & Response
    # ------------------------------------------------------------------------
    flowables.append(Paragraph("2. Digital service &amp; response: KPI", styles['ReportH1']))
    flowables.append(Spacer(1, 4))
    
    # Table KPI Digital Service & Response
    cs_kpi_data = [
        [Paragraph("Parameter Layanan Digital", styles['TableHeader']), 
         Paragraph("Aplikasi Alfagift", styles['TableHeader']), 
         Paragraph("Aplikasi Klik Indomaret", styles['TableHeader'])],
        
        [Paragraph("<b>Volume Ulasan Negatif Teranalisis</b>", styles['TableCellBold']), 
         Paragraph("13.844 ulasan", styles['TableCellCenter']), 
         Paragraph("15.730 ulasan", styles['TableCellCenter'])],
        
        [Paragraph("<b>Rasio Balasan Admin CS</b>", styles['TableCellBold']), 
         Paragraph("10.111 ulasan (73,04%)", styles['TableCellCenter']), 
         Paragraph("6.798 ulasan (43,22%)", styles['TableCellCenter'])],
        
        [Paragraph("<b>Median Waktu Tunda Tanggapan</b>", styles['TableCellBold']), 
         Paragraph("10,93 jam", styles['TableCellCenter']), 
         Paragraph("0,33 jam (20 menit)", styles['TableCellCenter'])],
        
        [Paragraph("<b>Rasio Pengalihan Kanal Eksternal</b>", styles['TableCellBold']), 
         Paragraph("45,17% dari total balasan", styles['TableCellCenter']), 
         Paragraph("95,03% dari total balasan", styles['TableCellCenter'])],
        
        [Paragraph("<b>Isu Teknis Utama Pengguna</b>", styles['TableCellBold']), 
         Paragraph("Performa Aplikasi (1.016 ulasan)<br/>Aksesibilitas Aplikasi (709 ulasan)", styles['TableCell']), 
         Paragraph("Performa Aplikasi (6.565 ulasan)<br/>Kualitas Aplikasi (787 ulasan)", styles['TableCell'])]
    ]
    
    t_cs_kpi = Table(cs_kpi_data, colWidths=[207.27, 140, 140])
    t_cs_kpi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY_COLOR),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
    ]))
    flowables.append(t_cs_kpi)
    flowables.append(Spacer(1, 8))
    
    flowables.append(Paragraph(
        "Keluhan teknis memuncak setelah rilis pembaruan versi aplikasi (APK) di Google Play Store, yang sering mengganggu fungsi login, verifikasi OTP, dan integrasi metode pembayaran.", 
        styles['ReportBody']))
    
    flowables.append(Paragraph("<b>Kategori Kendala Teknis Utama</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Alfagift:</b> Berpusat pada Performa Aplikasi (1.016 ulasan negatif; rating 1,13) dan Aksesibilitas Aplikasi (709 ulasan negatif; rating 1,18) akibat respon lambat dan kegagalan memuat katalog.", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Klik Indomaret:</b> Mengalami kendala performa lebih masif pada Performa Aplikasi (6.565 ulasan negatif; rating 1,12) dan Kualitas Aplikasi (787 ulasan negatif; rating 1,06) berupa lag berat dan kegagalan sistem pembayaran.", styles['ReportBullet']))
    
    flowables.append(Paragraph("<b>Isu Keamanan &amp; Akses Aplikasi (Alfagift)</b>", styles['ReportH2']))
    flowables.append(Paragraph("Berdasarkan kumpulan ulasan pengguna, pembaruan keamanan Alfagift dinilai semakin sensitif dalam mendeteksi kondisi perangkat dan memunculkan pesan kesalahan Error 70007 pada sebagian pengguna. Keluhan yang muncul menyebut bahwa perangkat dianggap ter-root atau tidak aman meskipun pengguna merasa tidak pernah melakukan root, dan beberapa di antaranya mengaitkan kejadian ini dengan penggunaan VPN, pengaktifan USB debugging, atau aplikasi utilitas tertentu. Akibat pesan kesalahan tersebut, aplikasi tidak dapat digunakan sebagaimana mestinya pada perangkat yang terdampak, sehingga pengguna kehilangan akses ke layanan Alfagift meskipun aplikasi sudah terpasang: <i>'Mendeteksi root, jls tidak root ponsel saya. Meski vpn tunnel sdh di force close, usb debug nonaktif'</i>.", styles['ReportBody']))
    
    flowables.append(Spacer(1, 4))
    img8 = Image(r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images\tech_issues.png", width=440, height=170)
    img8.hAlign = 'CENTER'
    flowables.append(img8)
    
    flowables.append(PageBreak())
    
    # ------------------------------------------------------------------------
    # PAGE 10: Kinerja Respons Layanan Pelanggan (CS)
    # ------------------------------------------------------------------------
    flowables.append(Paragraph("2. Digital service: respons CS di Play Store", styles['ReportH1']))
    flowables.append(Spacer(1, 4))
    
    flowables.append(Paragraph(
        "Strategi respon layanan pelanggan (CS) dari kedua ritel menunjukkan perbedaan mendasar dalam penanganan keluhan publik.", 
        styles['ReportBody']))
    
    flowables.append(Paragraph("<b>Perbandingan Rasio &amp; Kecepatan Respon</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Alfagift:</b> Merespon hingga 73,04% ulasan negatif (10.111 ulasan dibalas), namun dengan median waktu tunda respon yang cukup lama (10,93 jam).", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Klik Indomaret:</b> Hanya membalas 43,22% keluhan (6.798 ulasan dibalas), tetapi mencatat waktu respon sangat cepat dengan median 0,33 jam (20 menit).", styles['ReportBullet']))
    
    flowables.append(Paragraph("<b>Alur Resolusi &amp; Kanal Pengalihan</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Alfagift:</b> Mengarahkan 45,17% keluhan ke asisten virtual 'Shalma' via DM Instagram resmi. CS menyertakan kode tiket unik (contoh: <b>#3896583</b>) langsung pada balasan untuk mempermudah pelacakan tanpa pengulangan informasi.", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Klik Indomaret:</b> Mengarahkan 95,03% keluhan secara generik ke saluran telepon resmi (021-1500-280) atau email (customercare@klikindomaret.com) tanpa disertai nomor tiket pelacakan.", styles['ReportBullet']))
    
    flowables.append(Spacer(1, 10))
    img9 = Image(r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images\cs_performance_rr_delay.png", width=440, height=170)
    img9.hAlign = 'CENTER'
    flowables.append(img9)
    
    flowables.append(PageBreak())
    
    # ------------------------------------------------------------------------
    # PAGE 11: Distribusi Respons CS Berdasarkan Kategori & Kanal
    # ------------------------------------------------------------------------
    flowables.append(Paragraph("2. Digital service: detil kanal &amp; respons CS", styles['ReportH1']))
    flowables.append(Spacer(1, 4))
    
    flowables.append(Paragraph(
        "Analisis detail mengenai efektivitas respon layanan pelanggan mencakup persentase ulasan negatif yang dibalas untuk masing-masing kategori bisnis ritel serta identifikasi pola pengalihan komunikasi dari platform publik Google Play Store menuju kanal penanganan keluhan pelanggan yang bersifat privat.", 
        styles['ReportBody']))
    flowables.append(Spacer(1, 10))
    
    img10 = Image(r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images\cs_category_rr.png", width=420, height=170)
    img10.hAlign = 'CENTER'
    flowables.append(img10)
    
    flowables.append(Spacer(1, 15))
    
    img11 = Image(r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images\cs_redirection_channels.png", width=420, height=170)
    img11.hAlign = 'CENTER'
    flowables.append(img11)
    
    flowables.append(PageBreak())
    
    # ------------------------------------------------------------------------
    # PAGE 12: Dampak Pembaruan APK, Anomali Bulanan, & Ringkasan
    # ------------------------------------------------------------------------
    flowables.append(Paragraph("2. Digital service: APK, anomali &amp; ringkasan", styles['ReportH1']))
    flowables.append(Spacer(1, 4))
    
    flowables.append(Paragraph("<b>Versi APK dengan Keluhan Tertinggi</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Alfagift:</b> Keluhan terpusat pada versi <b>4.37.0</b> (652 ulasan), <b>4.27.1</b> (622 ulasan), dan <b>4.47.1</b> (569 ulasan).", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Klik Indomaret:</b> Ulasan negatif menumpuk pada rilis versi <b>2512100</b> (1.240 ulasan) dan <b>2501210</b> (674 ulasan).", styles['ReportBullet']))
    
    flowables.append(Paragraph("<b>Analisis Spike / Anomali Lini Masa</b>", styles['ReportH2']))
    flowables.append(Paragraph("• <b>Alfagift:</b> Lonjakan keluhan pada April-Mei terkait pendaftaran event 'Alfamart Run' akibat server lumpuh saat <i>war tiket</i>: <i>'Aplikasi lemot daftar alfamart Run aja, kaga jelas sistem nya jelek'</i>.", styles['ReportBullet']))
    flowables.append(Paragraph("• <b>Klik Indomaret:</b> Spike ekstrem pada Februari 2026 (2.633 keluhan) terkait rilis versi baru, serta kelumpuhan berkala saat event Harbolnas (9.9, 12.12): <i>'Saat event harbolnas selalu macet nih aplikasi'</i>.", styles['ReportBullet']))
    
    flowables.append(Spacer(1, 2))
    img12 = Image(r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images\spike_timeline.png", width=360, height=135)
    img12.hAlign = 'CENTER'
    flowables.append(img12)
    flowables.append(Spacer(1, 4))
    
    flowables.append(Paragraph("<b>Anomali Rating Bintang 5 Paksaan (Klik Indomaret)</b>", styles['ReportH2']))
    flowables.append(Paragraph("Berdasarkan salah satu ulasan pengguna, terdapat rating bintang 5 yang isi teksnya justru berisi keluhan teknis dan menyebut adanya instruksi dari atasan agar karyawan memberikan rating tinggi. Ulasan tersebut menuliskan bahwa rating bintang 5 diberikan bukan karena kepuasan, melainkan karena tekanan internal, dan mengkritik praktik tersebut sebagai bentuk manipulasi ulasan: <i>'Terpaksa kasih bintang 5 karna dipaksa atasan... kalau mau rating bagus perbaiki sistem bukan manipulasi review'</i>.", styles['ReportBody']))
    
    flowables.append(Paragraph("<b>Ringkasan Komparatif</b>", styles['ReportH2']))
    flowables.append(Paragraph("Alfagift unggul secara volume dan kepuasan umum (rating 4,37) dengan CS yang responsif (rasio balasan 73,04%) namun lambat tanggap (delay 10,93 jam). Sebaliknya, Klik Indomaret (rating 3,37) menghadapi kendala stabilitas aplikasi yang tinggi, dengan CS berasio rendah (43,22%) namun sangat cepat membalas (delay 20 menit) menggunakan pengalihan generik.", styles['ReportBody']))
    
    print("[INFO] Building PDF document...")
    # Build Document
    doc.build(flowables, onFirstPage=draw_cover_background, canvasmaker=NumberedCanvas)
    print(f"[INFO] PDF generated successfully at '{pdf_path}'!")

if __name__ == "__main__":
    build_report_pdf()
