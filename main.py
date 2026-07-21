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

finish_line = 40  # Jarak garis finish (panjang lintasan)

st.write("---")

# Tombol Mulai
if st.button("🏁 MULAI BALAPAN!", type="primary"):
    # Penampung UI animasi & status
    status_container = st.empty()
    progress_containers = [st.empty() for _ in range(int(num_snails))]
    
    # Inisialisasi Posisi Siput
    positions = [0] * int(num_snails)
    winner = None
    
    status_container.info("🟢 *Ready... Set... GOOO!* 🏁")
    time.sleep(1)

    # Loop Animasi Balapan
    while True:
        finished = False
        
        for i in range(int(num_snails)):
            # Pergerakan acak (pure random speed)
            # Setiap step, siput maju antara 0 sampai 3 langkah
            step = random.randint(0, 3)
            positions[i] += step
            
            # Cek jika sudah menyentuh atau melewati garis finish
            if positions[i] >= finish_line:
                positions[i] = finish_line
                if winner is None:
                    winner = snail_names[i]
                finished = True

        # Render Visual Lintasan
        for i in range(int(num_snails)):
            pos = positions[i]
            # Menghitung spasi jalan & sisa lintasan
            track_before = " " * pos
            track_after = " " * (finish_line - pos)
            
            # Visualiasi: Nama | Spasi + Siput + Sisa Track | Finish
            line_display = f"**{snail_names[i]:<20}** | `{track_before}🐌{track_after}` | 🏁"
            progress_containers[i].markdown(line_display)

        # Hentikan loop jika ada yang finish
        if finished:
            break
            
        time.sleep(0.15)  # Delay frame animasi

    # Pengumuman Pemenang
    status_container.success(f"🎉 **SELAMAT!** Pemenangnya adalah **{winner}**! 🏆")
    st.balloons()
