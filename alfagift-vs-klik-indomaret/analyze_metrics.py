import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import textwrap

def generate_all_charts():
    alfamart_dir = r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\csv-alfamart"
    indomaret_dir = r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\csv-indomaret"
    output_dir = r"d:\UNSIA\review-analysis\alfagift-vs-klik-indomaret\images"
    os.makedirs(output_dir, exist_ok=True)
    
    # ------------------------------------------------------------------------
    # 1. LOAD AND AGGREGATE RAW MAPPING DATA FOR TIMELINE & TREND CHARTS
    # ------------------------------------------------------------------------
    print("[INFO] Loading Alfamart raw mapping data...")
    alfa_files = glob.glob(os.path.join(alfamart_dir, "alfamart_mapping_review_topic_all_final_*.csv"))
    df_alfa = pd.concat([pd.read_csv(f, usecols=['score', 'at', 'sentiment', 'business_category', 'reviewCreatedVersion']) for f in alfa_files], ignore_index=True)
    df_alfa['at'] = pd.to_datetime(df_alfa['at'])
    df_alfa['month_year'] = df_alfa['at'].dt.to_period('M')
    
    print("[INFO] Loading Indomaret raw mapping data...")
    indo_files = glob.glob(os.path.join(indomaret_dir, "indomaret_mapping_review_topic_all_final_*.csv"))
    df_indo = pd.concat([pd.read_csv(f, usecols=['score', 'at', 'sentiment', 'business_category', 'reviewCreatedVersion']) for f in indo_files], ignore_index=True)
    df_indo['at'] = pd.to_datetime(df_indo['at'])
    df_indo['month_year'] = df_indo['at'].dt.to_period('M')
    
    # ------------------------------------------------------------------------
    # GRAPHICS CONFIGURATION
    # ------------------------------------------------------------------------
    color_navy = '#1E293B'  # Primary
    
    # Brand Colors (Primary & Soft variants for Pos/Neg)
    color_alfa_pos = '#DC2626'  # Alfamart Red
    color_alfa_neg = '#FCA5A5'  # Soft Red
    color_indo_pos = '#1D4ED8'  # Klik Indomaret Blue
    color_indo_neg = '#93C5FD'  # Soft Blue
    
    color_teal = color_alfa_pos   # For backward compatibility
    color_amber = color_indo_pos  # For backward compatibility
    
    color_slate = '#475569' # Text/Muted
    color_light_gray = '#E2E8F0'
    color_orange = '#F59E0B' # Orange for neutral line metrics (e.g., delay)
    
    color_neg = '#E06F6F'
    color_net = '#F5D061'
    color_pos = '#52B788'
    
    plt.rcParams['font.sans-serif'] = 'Helvetica'
    plt.rcParams['axes.edgecolor'] = color_light_gray
    plt.rcParams['axes.linewidth'] = 0.8
    
    # ========================================================================
    # CHART 1: Sentiment Comparison (sentiment_comparison.png)
    # ========================================================================
    print("[INFO] Generating Chart 1: Sentiment Comparison...")
    # Alfagift: Positif 82.98%, Netral 2.23%, Negatif 14.78%
    # Klik Indomaret: Positif 56.90%, Netral 3.77%, Negatif 39.33%
    labels = ['Positif', 'Netral', 'Negatif']
    alfa_sent_pct = [82.98, 2.23, 14.78]
    indo_sent_pct = [56.90, 3.77, 39.33]
    
    x = np.arange(len(labels))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(6.5, 2.8))
    rects1 = ax.bar(x - width/2, alfa_sent_pct, width, label='Alfagift', color=color_teal)
    rects2 = ax.bar(x + width/2, indo_sent_pct, width, label='Klik Indomaret', color=color_amber)
    
    ax.set_ylabel('Persentase (%)', fontsize=8, color=color_slate)
    ax.set_title('Perbandingan Proporsi Sentimen Ulasan (2023–2026)', fontsize=10, fontweight='bold', color=color_navy, pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8, color=color_slate)
    ax.tick_params(axis='y', labelsize=8, colors=color_slate)
    ax.set_ylim(0, 110)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax.legend(fontsize=8, loc='upper right', framealpha=0.9, edgecolor=color_light_gray)
    
    ax.bar_label(rects1, fmt='%.2f%%', padding=3, fontsize=7.5, color=color_slate)
    ax.bar_label(rects2, fmt='%.2f%%', padding=3, fontsize=7.5, color=color_slate)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'sentiment_comparison.png'), dpi=300)
    plt.close()
    
    # ========================================================================
    # CHART 2: Rating Trend (rating_trend.png)
    # ========================================================================
    print("[INFO] Generating Chart 2: Rating Trend...")
    # Calculate monthly average rating
    alfa_rating_monthly = df_alfa.groupby('month_year')['score'].mean()
    indo_rating_monthly = df_indo.groupby('month_year')['score'].mean()
    
    # Align index
    all_months = sorted(list(set(alfa_rating_monthly.index.astype(str)) | set(indo_rating_monthly.index.astype(str))))
    
    fig, ax = plt.subplots(figsize=(6.5, 2.8))
    ax.plot(alfa_rating_monthly.index.astype(str), alfa_rating_monthly.values, color=color_teal, linewidth=1.5, marker='.', markersize=4, label='Alfagift')
    ax.plot(indo_rating_monthly.index.astype(str), indo_rating_monthly.values, color=color_amber, linewidth=1.5, marker='.', markersize=4, label='Klik Indomaret')
    
    ax.set_ylabel('Rating Rata-rata (Skala 1-5)', fontsize=8, color=color_slate)
    ax.set_title('Tren Pergerakan Rating Bulanan (2023–2026)', fontsize=10, fontweight='bold', color=color_navy, pad=10)
    ax.tick_params(axis='both', labelsize=7, colors=color_slate)
    
    # Show labels every 4 months to avoid clutter
    tick_positions = list(range(0, len(all_months), 4))
    ax.set_xticks(tick_positions)
    ax.set_xticklabels([all_months[i] for i in tick_positions], rotation=30, ha='right')
    ax.set_ylim(0.5, 5.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax.legend(fontsize=8, loc='lower left', framealpha=0.9, edgecolor=color_light_gray)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'rating_trend.png'), dpi=300)
    plt.close()
    
    # ========================================================================
    # CHART 3: Top Negative Categories (top_negative_categories.png)
    # ========================================================================
    print("[INFO] Generating Chart 3: Top Negative Categories...")
    # Group categories for comparison
    categories = ['Layanan Pengiriman', 'Performa & Stabilitas', 'Akses & Akun', 'UI/UX & Kualitas', 'Promo & Harga', 'Transaksi & Pembayaran']
    # Alfagift negative counts
    alfa_neg_counts = [5645, 1016 + 254, 2489 + 709 + 397, 209 + 77, 644 + 106 + 84, 422 + 67]
    # Indomaret negative counts
    indo_neg_counts = [4252, 6565 + 787 + 58, 650 + 536, 1613 + 71, 267, 189 + 64]
    
    y = np.arange(len(categories))
    height = 0.35
    
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    rects1 = ax.barh(y - height/2, alfa_neg_counts, height, label='Alfagift', color=color_teal)
    rects2 = ax.barh(y + height/2, indo_neg_counts, height, label='Klik Indomaret', color=color_amber)
    
    ax.set_xlabel('Jumlah Ulasan Negatif', fontsize=8, color=color_slate)
    ax.set_title('Perbandingan Volume Keluhan Negatif Per Kategori', fontsize=10, fontweight='bold', color=color_navy, pad=10)
    ax.set_yticks(y)
    ax.set_yticklabels(categories, fontsize=8, color=color_slate)
    ax.tick_params(axis='x', labelsize=8, colors=color_slate)
    ax.set_xlim(0, 9500)
    ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='x', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax.legend(fontsize=8, loc='lower right', framealpha=0.9, edgecolor=color_light_gray)
    
    ax.bar_label(rects1, padding=3, fontsize=7, color=color_slate)
    ax.bar_label(rects2, padding=3, fontsize=7, color=color_slate)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_negative_categories.png'), dpi=300)
    plt.close()
    
    # ========================================================================
    # CHART 4: Top Positive Categories (top_positive_categories.png)
    # ========================================================================
    print("[INFO] Generating Chart 4: Top Positive Categories...")
    pos_categories = ['Kepuasan Pengguna', 'Pengalaman Pengguna', 'Promo & Harga', 'Layanan Pengiriman', 'Layanan Pelanggan']
    # Alfagift positive counts
    alfa_pos_counts = [28416, 21085 + 3014 + 124, 16299 + 1456 + 156, 632 + 168, 1467 + 930]
    # Indomaret positive counts
    indo_pos_counts = [7581 + 531, 6984 + 79, 2313 + 521 + 170 + 25, 1309, 573]
    
    y = np.arange(len(pos_categories))
    height = 0.35
    
    fig, ax = plt.subplots(figsize=(6.5, 3.0))
    rects1 = ax.barh(y - height/2, alfa_pos_counts, height, label='Alfagift', color=color_teal)
    rects2 = ax.barh(y + height/2, indo_pos_counts, height, label='Klik Indomaret', color=color_amber)
    
    ax.set_xlabel('Jumlah Ulasan Positif', fontsize=8, color=color_slate)
    ax.set_title('Perbandingan Volume Ulasan Positif Per Kategori', fontsize=10, fontweight='bold', color=color_navy, pad=10)
    ax.set_yticks(y)
    ax.set_yticklabels(pos_categories, fontsize=8, color=color_slate)
    ax.tick_params(axis='x', labelsize=8, colors=color_slate)
    ax.set_xlim(0, 36000)
    ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='x', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax.legend(fontsize=8, loc='lower right', framealpha=0.9, edgecolor=color_light_gray)
    
    ax.bar_label(rects1, padding=3, fontsize=7, color=color_slate)
    ax.bar_label(rects2, padding=3, fontsize=7, color=color_slate)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_positive_categories.png'), dpi=300)
    plt.close()
    
    # ========================================================================
    # CHART 5: Promo & Value (promo_value.png)
    # ========================================================================
    print("[INFO] Generating Chart 5: Promo & Value...")
    promo_labels = ['Alfagift (Positif)', 'Alfagift (Negatif)', 'Klik Indomaret (Positif)', 'Klik Indomaret (Negatif)']
    # Alfagift Positive Promo: Layanan Pengiriman dan Promo (16299) + Harga dan Promosi (1456)
    # Alfagift Negative Promo: Promosi dan Loyalitas (644) + Manajemen Harga dan Promosi (106)
    # Indomaret Positive Promo: Promosi dan Penawaran (2313) + Promosi dan Diskon (521) + Harga dan Nilai (170)
    # Indomaret Negative Promo: Promosi dan Harga (267)
    promo_counts = [16299 + 1456, 644 + 106, 2313 + 521 + 170, 267]
    promo_colors = [color_alfa_pos, color_alfa_neg, color_indo_pos, color_indo_neg]
    
    fig, ax = plt.subplots(figsize=(6.5, 2.5))
    bars = ax.barh(promo_labels, promo_counts, color=promo_colors, height=0.5)
    
    ax.set_xlabel('Jumlah Ulasan', fontsize=8, color=color_slate)
    ax.set_title('Ulasan Terkait Promosi, Harga & Value (2023–2026)', fontsize=10, fontweight='bold', color=color_navy, pad=10)
    ax.tick_params(axis='both', labelsize=8, colors=color_slate)
    ax.set_xlim(0, 22000)
    ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='x', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax.bar_label(bars, padding=4, fontsize=7.5, color=color_slate)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'promo_value.png'), dpi=300)
    plt.close()
    
    # ========================================================================
    # CHART 6: Stock & Loyalty (stock_loyalty.png)
    # ========================================================================
    print("[INFO] Generating Chart 6: Stock & Loyalty...")
    labels_stock = ['Stok Kosong / Tidak Akurat', 'Kendala Poin / Loyalitas']
    alfa_stock_loyalty = [278, 644 + 201]  # Alfagift: Ketersediaan Produk (278), Promosi & Loyalitas (644) + Prog Loyalitas (201)
    indo_stock_loyalty = [123, 327]        # Indomaret: Manajemen Stok (123), Stok & Layanan Netral (327)
    
    x = np.arange(len(labels_stock))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(6.5, 2.5))
    rects1 = ax.bar(x - width/2, alfa_stock_loyalty, width, label='Alfagift', color=color_teal)
    rects2 = ax.bar(x + width/2, indo_stock_loyalty, width, label='Klik Indomaret', color=color_amber)
    
    ax.set_ylabel('Jumlah Ulasan', fontsize=8, color=color_slate)
    ax.set_title('Volume Keluhan Terkait Ketersediaan Stok & Loyalitas', fontsize=10, fontweight='bold', color=color_navy, pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(labels_stock, fontsize=8, color=color_slate)
    ax.tick_params(axis='y', labelsize=8, colors=color_slate)
    ax.set_ylim(0, 1100)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax.legend(fontsize=8, loc='upper right', framealpha=0.9, edgecolor=color_light_gray)
    
    ax.bar_label(rects1, padding=3, fontsize=7.5, color=color_slate)
    ax.bar_label(rects2, padding=3, fontsize=7.5, color=color_slate)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'stock_loyalty.png'), dpi=300)
    plt.close()
    
    # ========================================================================
    # CHART 7: Delivery & Omnichannel (delivery_omnichannel.png)
    # ========================================================================
    print("[INFO] Generating Chart 7: Delivery & Omnichannel...")
    labels_del = ['Pengiriman (Negatif)', 'Pengiriman (Positif)', 'Beda Harga Fisik vs App']
    alfa_del_omni = [5645, 632 + 168, 106]
    indo_del_omni = [4252, 1309, 267]
    
    x = np.arange(len(labels_del))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(6.5, 2.5))
    rects1 = ax.bar(x - width/2, alfa_del_omni, width, label='Alfagift', color=color_teal)
    rects2 = ax.bar(x + width/2, indo_del_omni, width, label='Klik Indomaret', color=color_amber)
    
    ax.set_ylabel('Jumlah Ulasan', fontsize=8, color=color_slate)
    ax.set_title('Perbandingan Kinerja Pengiriman & Integrasi Fisik', fontsize=10, fontweight='bold', color=color_navy, pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(labels_del, fontsize=8, color=color_slate)
    ax.tick_params(axis='y', labelsize=8, colors=color_slate)
    ax.set_ylim(0, 7500)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax.legend(fontsize=8, loc='upper right', framealpha=0.9, edgecolor=color_light_gray)
    
    ax.bar_label(rects1, padding=3, fontsize=7.5, color=color_slate)
    ax.bar_label(rects2, padding=3, fontsize=7.5, color=color_slate)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'delivery_omnichannel.png'), dpi=300)
    plt.close()
    
    # ========================================================================
    # CHART 8: Tech Issues & Security Detail (tech_issues.png)
    # ========================================================================
    print("[INFO] Generating Chart 8: Tech Issues...")
    labels_tech = ['Performa / Lemot', 'Stabilitas / Crash', 'Akses Akun / Login', 'Aksesibilitas / Daftar']
    alfa_tech = [1016, 254, 397, 709]
    indo_tech = [6565, 787 + 58, 650 + 536, 1613]
    
    x = np.arange(len(labels_tech))
    width = 0.35
    
    fig, (ax, ax_sec) = plt.subplots(1, 2, figsize=(7.2, 2.8), gridspec_kw={'width_ratios': [1.8, 1]})
    
    # Left Plot: Comparison
    rects1 = ax.bar(x - width/2, alfa_tech, width, label='Alfagift', color=color_teal)
    rects2 = ax.bar(x + width/2, indo_tech, width, label='Klik Indomaret', color=color_amber)
    ax.set_ylabel('Jumlah Keluhan', fontsize=7.5, color=color_slate)
    ax.set_title('Perbandingan Volume Keluhan Teknis', fontsize=8.5, fontweight='bold', color=color_navy, pad=8)
    ax.set_xticks(x)
    short_labels = [textwrap.fill(l, width=12) for l in labels_tech]
    ax.set_xticklabels(short_labels, fontsize=7, color=color_slate)
    ax.tick_params(axis='y', labelsize=7, colors=color_slate)
    ax.set_ylim(0, 9500)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax.legend(fontsize=7, loc='upper right', framealpha=0.9, edgecolor=color_light_gray)
    ax.bar_label(rects1, padding=2, fontsize=6.5, color=color_slate)
    ax.bar_label(rects2, padding=2, fontsize=6.5, color=color_slate)
    
    # Right Plot: Security Block Breakdown (Root / VPN detection)
    sec_labels = ['Deteksi Root /\nError 70007', 'OTP & Login\nLainnya']
    sec_counts = [114, 3222]
    rects_sec = ax_sec.bar(sec_labels, sec_counts, color=[color_alfa_neg, color_alfa_pos], width=0.45)
    ax_sec.set_ylabel('Jumlah Ulasan', fontsize=7.5, color=color_slate)
    ax_sec.set_title('Isu Keamanan Alfagift', fontsize=8.5, fontweight='bold', color=color_navy, pad=8)
    ax_sec.tick_params(axis='both', labelsize=7, colors=color_slate)
    ax_sec.set_ylim(0, 4200)
    ax_sec.spines['top'].set_visible(False)
    ax_sec.spines['right'].set_visible(False)
    ax_sec.grid(axis='y', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax_sec.bar_label(rects_sec, padding=2, fontsize=6.5, color=color_slate)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'tech_issues.png'), dpi=300)
    plt.close()
    
    # ========================================================================
    # CHART 9: CS Performance – Reply Rate & Delay (cs_performance_rr_delay.png)
    # ========================================================================
    print("[INFO] Generating Chart 9: CS Performance - Reply Rate & Delay...")
    apps = ['Alfagift CS', 'Klik Indomaret CS']
    reply_rates = [73.04, 43.22]
    reply_delays = [10.93, 0.33]
    
    fig, ax1 = plt.subplots(figsize=(6.5, 2.5))
    ax2 = ax1.twinx()
    
    rects1 = ax1.bar(apps, reply_rates, color=[color_alfa_pos, color_indo_pos], width=0.4, alpha=0.8)
    line = ax2.plot(apps, reply_delays, color=color_orange, marker='o', linewidth=2.0, markersize=6, label='Median Delay')
    
    ax1.set_ylabel('Rasio Balasan CS (%)', color=color_navy, fontsize=8, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor=color_navy, labelsize=8)
    ax1.set_ylim(0, 115)
    
    ax2.set_ylabel('Median Delay Tanggapan (Jam)', color=color_orange, fontsize=8, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor=color_orange, labelsize=8)
    ax2.set_ylim(-0.5, 16.5)
    
    ax1.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.grid(axis='y', linestyle=':', alpha=0.5, color='#CBD5E1')
    
    # Annotate bars INSIDE the bar to avoid overlap with line labels
    ax1.bar_label(rects1, fmt='%.2f%%', label_type='center', color='white', fontsize=8, fontweight='bold')
    
    # Annotate line (placed above the marker)
    for i, v in enumerate(reply_delays):
        ax2.text(i, v + 0.6, f"{v:.2f} jam", ha='center', fontsize=8, color=color_orange, fontweight='bold',
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=1))
                 
    # Combine legends and place in empty upper right space (above Indomaret's low values)
    patch_alfa = mpatches.Patch(color=color_alfa_pos, label='Reply Rate (Alfagift)')
    patch_indo = mpatches.Patch(color=color_indo_pos, label='Reply Rate (Indomaret)')
    ax1.legend([patch_alfa, patch_indo, line[0]], ['Reply Rate (Alfagift)', 'Reply Rate (Indomaret)', 'Median Delay Tanggapan'], loc='upper right', fontsize=8, framealpha=0.9, edgecolor=color_light_gray)
    
    plt.title('Kinerja Respon Layanan Pelanggan (CS) di Play Store', fontsize=10, fontweight='bold', color=color_navy, pad=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'cs_performance_rr_delay.png'), dpi=300)
    plt.close()
    
    # ========================================================================
    # CHART 10: CS Category Reply Rate (cs_category_rr.png)
    # ========================================================================
    print("[INFO] Generating Chart 10: CS Category Reply Rate...")
    # Compare reply rate of main negative categories
    cats = ['Layanan Pengiriman', 'Performa Aplikasi', 'Manajemen Akun', 'Transaksi / Bayar']
    alfa_rr = [74.61, 72.05, 74.45, 71.56]
    indo_rr = [37.02, 44.52, 41.38, 44.97]
    
    x = np.arange(len(cats))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(6.5, 2.5))
    rects1 = ax.bar(x - width/2, alfa_rr, width, label='Alfagift CS', color=color_teal)
    rects2 = ax.bar(x + width/2, indo_rr, width, label='Klik Indomaret CS', color=color_amber)
    
    ax.set_ylabel('Rasio Balasan (%)', fontsize=8, color=color_slate)
    ax.set_title('Rasio Balasan CS Per Kategori Keluhan Utama', fontsize=10, fontweight='bold', color=color_navy, pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=8, color=color_slate)
    ax.tick_params(axis='y', labelsize=8, colors=color_slate)
    ax.set_ylim(0, 110)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax.legend(fontsize=8, loc='upper right', framealpha=0.9, edgecolor=color_light_gray)
    
    ax.bar_label(rects1, fmt='%.1f%%', padding=2, fontsize=7.5, color=color_slate)
    ax.bar_label(rects2, fmt='%.1f%%', padding=2, fontsize=7.5, color=color_slate)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'cs_category_rr.png'), dpi=300)
    plt.close()
    
    # ========================================================================
    # CHART 11: CS Redirection Channels (cs_redirection_channels.png)
    # ========================================================================
    print("[INFO] Generating Chart 11: CS Redirection Channels...")
    channels_labels = ['Redirect ke WA / DM / Call Center (%)', 'Tetap di Play Store / Umum (%)']
    alfa_redirect = [45.17, 100 - 45.17]
    indo_redirect = [95.03, 100 - 95.03]
    
    x = np.arange(len(channels_labels))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(6.5, 2.5))
    rects1 = ax.bar(x - width/2, alfa_redirect, width, label='Alfagift CS', color=color_teal)
    rects2 = ax.bar(x + width/2, indo_redirect, width, label='Klik Indomaret CS', color=color_amber)
    
    ax.set_ylabel('Persentase (%)', fontsize=8, color=color_slate)
    ax.set_title('Saluran Penanganan Keluhan (Redirection Channel)', fontsize=10, fontweight='bold', color=color_navy, pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(channels_labels, fontsize=8, color=color_slate)
    ax.tick_params(axis='y', labelsize=8, colors=color_slate)
    ax.set_ylim(0, 130)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax.legend(fontsize=8, loc='upper right', framealpha=0.9, edgecolor=color_light_gray)
    
    ax.bar_label(rects1, fmt='%.2f%%', padding=3, fontsize=7.5, color=color_slate)
    ax.bar_label(rects2, fmt='%.2f%%', padding=3, fontsize=7.5, color=color_slate)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'cs_redirection_channels.png'), dpi=300)
    plt.close()
    
    # ========================================================================
    # CHART 12: Spike / Anomaly Timeline & Forced Ratings (spike_timeline.png)
    # ========================================================================
    print("[INFO] Generating Chart 12: Spike / Anomaly Timeline...")
    alfa_neg_monthly = df_alfa[df_alfa['sentiment'] == 'negatif'].groupby('month_year').size()
    indo_neg_monthly = df_indo[df_indo['sentiment'] == 'negatif'].groupby('month_year').size()
    
    all_months_neg = sorted(list(set(alfa_neg_monthly.index.astype(str)) | set(indo_neg_monthly.index.astype(str))))
    
    fig, (ax, ax_forced) = plt.subplots(1, 2, figsize=(7.2, 2.8), gridspec_kw={'width_ratios': [1.8, 1]})
    
    # Left Plot: Timeline
    ax.plot(alfa_neg_monthly.index.astype(str), alfa_neg_monthly.values, color=color_teal, linewidth=1.5, marker='.', markersize=4, label='Alfagift')
    ax.plot(indo_neg_monthly.index.astype(str), indo_neg_monthly.values, color=color_amber, linewidth=1.5, marker='.', markersize=4, label='Klik Indomaret')
    
    # Highlight Klik Indomaret Peak (Feb 2026: 2633)
    if '2026-02' in indo_neg_monthly.index.astype(str):
        idx = list(indo_neg_monthly.index.astype(str)).index('2026-02')
        val = indo_neg_monthly['2026-02']
        ax.scatter(idx, val, color='#EF4444', s=35, zorder=5)
        ax.annotate(f"Spike Feb 2026\n({val:,})", (idx, val), textcoords="offset points", 
                    xytext=(-10, 10), ha='center', fontsize=7, fontweight='bold', color=color_navy,
                    bbox=dict(facecolor='white', alpha=0.8, edgecolor=color_light_gray, pad=2))
                    
    # Highlight Alfagift Peak (Mar 2024: 556)
    if '2024-03' in alfa_neg_monthly.index.astype(str):
        idx = list(alfa_neg_monthly.index.astype(str)).index('2024-03')
        val = alfa_neg_monthly['2024-03']
        ax.scatter(idx, val, color='#EF4444', s=35, zorder=5)
        ax.annotate(f"Spike Mar 2024\n({val:,})", (idx, val), textcoords="offset points", 
                    xytext=(0, 10), ha='center', fontsize=7, fontweight='bold', color=color_navy,
                    bbox=dict(facecolor='white', alpha=0.8, edgecolor=color_light_gray, pad=2))
    
    ax.set_ylabel('Jumlah Keluhan Negatif', fontsize=7.5, color=color_slate)
    ax.set_title('Lini Masa Keluhan Negatif Bulanan & Spike', fontsize=8.5, fontweight='bold', color=color_navy, pad=8)
    ax.tick_params(axis='both', labelsize=7, colors=color_slate)
    tick_positions_neg = list(range(0, len(all_months_neg), 4))
    ax.set_xticks(tick_positions_neg)
    ax.set_xticklabels([all_months_neg[i] for i in tick_positions_neg], rotation=30, ha='right')
    ax.set_ylim(0, 3600)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax.legend(fontsize=7, loc='upper left', framealpha=0.9, edgecolor=color_light_gray)
    
    # Right Plot: Forced ratings per month (Jan 25: 1, Feb 25: 2, Oct 25: 1, Feb 26: 9, May 26: 1)
    forced_months = ['Jan\n25', 'Feb\n25', 'Okt\n25', 'Feb\n26', 'Mei\n26']
    forced_counts = [1, 2, 1, 9, 1]
    rects_forced = ax_forced.bar(forced_months, forced_counts, color=color_indo_pos, width=0.5)
    ax_forced.set_ylabel('Jumlah Ulasan', fontsize=7.5, color=color_slate)
    ax_forced.set_title('Ulasan Paksaan (Rating 5)', fontsize=8.5, fontweight='bold', color=color_navy, pad=8)
    ax_forced.tick_params(axis='both', labelsize=7, colors=color_slate)
    ax_forced.set_ylim(0, 12)
    ax_forced.spines['top'].set_visible(False)
    ax_forced.spines['right'].set_visible(False)
    ax_forced.grid(axis='y', linestyle=':', alpha=0.5, color='#CBD5E1')
    ax_forced.bar_label(rects_forced, padding=1, fontsize=7, color=color_slate)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'spike_timeline.png'), dpi=300)
    plt.close()
    
    print("[INFO] All 12 charts generated successfully!")

if __name__ == "__main__":
    generate_all_charts()
