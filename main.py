import streamlit as st
import random
import time

# Configuration Page
st.set_page_config(
    page_title="The Great Snail Race 🐌",
    page_icon="🐌",
    layout="wide"
)

st.title("🐌 The Great Snail Race (SpongeBob Style)")
st.subheader("Siapakah yang akan memenangkan piala bergengsi ini?")

# Default Names dari Episode SpongeBob
default_names = ["Snellie (Squidward)", "Gary (SpongeBob)", "Rocky (Patrick)", "Larry the Snail"]

# Sidebar Settings
st.sidebar.header("⚙️ Pengaturan Balapan")

num_snails = st.sidebar.number_input(
    "Jumlah Siput (2 - 8):",
    min_value=2,
    max_value=8,
    value=3,
    step=1
)

st.sidebar.write("---")
st.sidebar.write("### 📝 Nama Siput:")

snail_names = []
for i in range(int(num_snails)):
    default_val = default_names[i] if i < len(default_names) else f"Siput #{i+1}"
    name = st.sidebar.text_input(f"Nama Siput {i+1}:", value=default_val, key=f"snail_{i}")
    snail_names.append(name)

# Jarak lintasan (100 langkah = ~10-12 detik)
finish_line = 100 

st.write("---")

# Tombol Mulai
if st.button("🏁 MULAI BALAPAN!", type="primary"):
    # Penampung utama: Mengosongkan status & status bar
    status_container = st.empty()
    
    # --- PERBAIKAN DI SINI ---
    # Penampung tunggal untuk SELURUH area balapan agar tidak bertumpuk kebawah
    race_area = st.empty()
    
    positions = [0] * int(num_snails)
    winner = None
    
    status_container.info("🟢 *Ready... Set... GOOO!* 🏁")
    time.sleep(1)

    # Loop Animasi Balapan
    while True:
        finished = False
        
        # 1. Update Posisi Siput
        for i in range(int(num_snails)):
            step = random.randint(0, 3)
            positions[i] += step
            
            if positions[i] >= finish_line:
                positions[i] = finish_line
                if winner is None:
                    winner = snail_names[i]
                finished = True

        # 2. Gambar Ulang Seluruh Area Balapan di dalam 'race_area'
        with race_area.container():
            for i in range(int(num_snails)):
                # Membuat baris kolom baru untuk frame ini (posisi tetap sejajar)
                col_name, col_start, col_track, col_finish = st.columns([2.5, 0.4, 7, 0.4])
                
                pos = positions[i]
                
                # Hitung proporsi posisi siput dalam bentuk spasi monospaced
                # Menggunakan skala relatif agar muat rapi di layar
                display_pos = int((pos / finish_line) * 45)
                track_before = " " * display_pos
                track_after = " " * (45 - display_pos)
                
                # Tampilkan di kolom masing-masing
                col_name.markdown(f"**{snail_names[i]}**")
                col_start.markdown("🚨")  # Garis Start
                col_track.markdown(f"`{track_before}🐌{track_after}`") # Lintasan
                col_finish.markdown("🏁") # Garis Finish
            
            # Tambahkan sedikit pemisah antar siput
            st.write("")

        # 3. Kontrol Loop
        if finished:
            break
            
        time.sleep(0.15)

    # Pengumuman Pemenang
    status_container.success(f"🎉 **SELAMAT!** Pemenangnya adalah **{winner}**! 🏆")
    st.balloons()
