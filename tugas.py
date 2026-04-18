import tkinter as tk
from tkinter import messagebox

basis_pengetahuan = {
    "Tonsilitis": {
        "gejala": {"G37", "G12", "G5", "G27", "G6", "G21"},
        "penjelasan": "Peradangan pada tonsil (amandel) yang disebabkan oleh infeksi virus atau bakteri."
    },
    "Sinusitis Maksilaris": {
        "gejala": {"G37", "G12", "G27", "G17", "G33", "G36", "G29"},
        "penjelasan": "Peradangan pada sinus maksilaris yang menyebabkan nyeri di area pipi dan hidung tersumbat."
    },
    "Sinusitis Frontalis": {
        "gejala": {"G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"},
        "penjelasan": "Peradangan pada sinus frontalis di area dahi yang menyebabkan sakit kepala dan tekanan di dahi."
    },
    "Sinusitis Edmoidalis": {
        "gejala": {"G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"},
        "penjelasan": "Peradangan pada sinus etmoid yang menyebabkan nyeri antara mata dan hidung."
    },
    "Sinusitis Sfenoidalis": {
        "gejala": {"G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"},
        "penjelasan": "Peradangan pada sinus sfenoid yang terletak di belakang hidung."
    },
    "Abses Peritonsiler": {
        "gejala": {"G37", "G12", "G6", "G15", "G2", "G29", "G10"},
        "penjelasan": "Kumpulan nanah di sekitar tonsil akibat infeksi bakteri yang parah."
    },
    "Faringitis": {
        "gejala": {"G37", "G5", "G6", "G7", "G15"},
        "penjelasan": "Peradangan pada faring (tenggorokan) yang menyebabkan nyeri saat menelan."
    },
    "Kanker Laring": {
        "gejala": {"G5", "G27", "G6", "G15", "G2", "G19", "G1"},
        "penjelasan": "Pertumbuhan sel kanker di area laring (kotak suara)."
    },
    "Deviasi Septum": {
        "gejala": {"G37", "G17", "G20", "G8", "G18", "G25"},
        "penjelasan": "Penyimpangan dinding pemisah rongga hidung yang menyebabkan penyumbatan."
    },
    "Laringitis": {
        "gejala": {"G37", "G5", "G15", "G16", "G32"},
        "penjelasan": "Peradangan pada laring yang menyebabkan suara serak dan tenggorokan gatal."
    },
    "Kanker Leher & Kepala": {
        "gejala": {"G5", "G22", "G8", "G28", "G3", "G11"},
        "penjelasan": "Pertumbuhan sel kanker di area leher dan kepala."
    },
    "Otitis Media Akut": {
        "gejala": {"G37", "G20", "G35", "G31"},
        "penjelasan": "Infeksi akut pada telinga tengah yang menyebabkan nyeri telinga dan demam."
    },
    "Contact Ulcers": {
        "gejala": {"G5", "G2"},
        "penjelasan": "Luka pada pita suara akibat penggunaan suara berlebihan."
    },
    "Abses Parafaringeal": {
        "gejala": {"G5", "G16"},
        "penjelasan": "Kumpulan nanah di ruang parafaringeal yang menyebabkan nyeri dan bengkak leher."
    },
    "Barotitis Media": {
        "gejala": {"G12", "G20"},
        "penjelasan": "Kerusakan telinga akibat perubahan tekanan udara atau air."
    },
    "Kanker Nafasoring": {
        "gejala": {"G17", "G8"},
        "penjelasan": "Pertumbuhan sel kanker di area nasofaring (belakang hidung)."
    },
    "Kanker Tonsil": {
        "gejala": {"G6", "G29"},
        "penjelasan": "Pertumbuhan sel kanker pada tonsil (amandel)."
    },
    "Neuronitis Vestibularis": {
        "gejala": {"G35", "G24"},
        "penjelasan": "Peradangan saraf vestibular yang menyebabkan vertigo dan mual."
    },
    "Meniere": {
        "gejala": {"G20", "G35", "G14", "G4"},
        "penjelasan": "Gangguan telinga bagian dalam yang menyebabkan vertigo, tinitus, dan gangguan pendengaran."
    },
    "Tumor Syaraf Pendengaran": {
        "gejala": {"G12", "G34", "G23"},
        "penjelasan": "Pertumbuhan tumor jinak pada saraf pendengaran yang menyebabkan tuli dan ketidakseimbangan."
    },
    "Kanker Leher Metastatik": {
        "gejala": {"G29"},
        "penjelasan": "Penyebaran sel kanker ke kelenjar getah bening di leher."
    },
    "Osteosklerosis": {
        "gejala": {"G34", "G9"},
        "penjelasan": "Pertumbuhan tulang abnormal di telinga tengah yang menyebabkan tuli dan telinga berdenging."
    },
    "Vertigo Postular": {
        "gejala": {"G24"},
        "penjelasan": "Vertigo yang dipicu oleh perubahan posisi kepala secara tiba-tiba."
    }
}

daftar_gejala = [
    ("G1", "Apakah Anda mengalami nafas abnormal?"),
    ("G2", "Apakah suara Anda serak?"),
    ("G3", "Apakah Anda mengalami perubahan kulit?"),
    ("G4", "Apakah telinga Anda terasa penuh?"),
    ("G5", "Apakah Anda merasa nyeri saat bicara atau menelan?"),
    ("G6", "Apakah Anda mengalami nyeri tenggorokan?"),
    ("G7", "Apakah Anda mengalami nyeri leher?"),
    ("G8", "Apakah Anda mengalami pendarahan hidung?"),
    ("G9", "Apakah telinga Anda berdenging?"),
    ("G10", "Apakah air liur Anda menetes terus?"),
    ("G11", "Apakah Anda mengalami perubahan suara?"),
    ("G12", "Apakah Anda mengalami sakit kepala?"),
    ("G13", "Apakah Anda mengalami nyeri di pinggir hidung?"),
    ("G14", "Apakah Anda mengalami serangan vertigo?"),
    ("G15", "Apakah terdapat getah bening yang membesar?"),
    ("G16", "Apakah leher Anda bengkak?"),
    ("G17", "Apakah hidung Anda tersumbat?"),
    ("G18", "Apakah Anda mengalami infeksi sinus?"),
    ("G19", "Apakah berat badan Anda turun?"),
    ("G20", "Apakah Anda mengalami nyeri telinga?"),
    ("G21", "Apakah selaput lendir Anda merah?"),
    ("G22", "Apakah terdapat benjolan di leher?"),
    ("G23", "Apakah tubuh Anda terasa tidak seimbang?"),
    ("G24", "Apakah bola mata Anda bergerak sendiri?"),
    ("G25", "Apakah Anda mengalami nyeri wajah?"),
    ("G26", "Apakah dahi Anda terasa sakit?"),
    ("G27", "Apakah Anda mengalami batuk?"),
    ("G28", "Apakah ada tumbuh sesuatu di mulut Anda?"),
    ("G29", "Apakah terdapat benjolan di leher?"),
    ("G30", "Apakah Anda mengalami nyeri antara mata?"),
    ("G31", "Apakah Anda mengalami radang gendang telinga?"),
    ("G32", "Apakah tenggorokan Anda gatal?"),
    ("G33", "Apakah hidung Anda meler?"),
    ("G34", "Apakah Anda mengalami gangguan pendengaran (tuli)?"),
    ("G35", "Apakah Anda mengalami mual atau muntah?"),
    ("G36", "Apakah Anda merasa letih dan lesu?"),
    ("G37", "Apakah Anda mengalami demam?")
]

def mesin_inferensi(gejala_input):
    hasil = []
    gejala_set = set(gejala_input)
    for penyakit, data in basis_pengetahuan.items():
        gejala_cocok = data["gejala"].intersection(gejala_set)
        if len(gejala_cocok) >= len(data["gejala"]):
            tingkat = 100.0
            hasil.append((penyakit, data["penjelasan"], tingkat))
        elif len(gejala_cocok) >= 2:
            tingkat = len(gejala_cocok) / len(data["gejala"]) * 100
            hasil.append((penyakit, data["penjelasan"], tingkat))
    hasil.sort(key=lambda x: x[2], reverse=True)
    return hasil

class AplikasiDiagnosa:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Penyakit THT")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        self.label_judul = tk.Label(root, text="Sistem Pakar Diagnosa\nPenyakit THT", font=("Arial", 14, "bold"))
        self.label_judul.pack(pady=15)

        self.label_tanya = tk.Label(root, text="Tekan tombol di bawah untuk memulai diagnosa.", font=("Arial", 11), wraplength=420)
        self.label_tanya.pack(pady=20)

        self.label_counter = tk.Label(root, text="", font=("Arial", 9))
        self.label_counter.pack()

        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", font=("Arial", 10), command=self.mulai_tanya)
        self.btn_mulai.pack(pady=10)

        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_jawaban, text="YA", width=12, font=("Arial", 10), command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_jawaban, text="TIDAK", width=12, font=("Arial", 10), command=lambda: self.jawab('t'))
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=15)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(daftar_gejala):
            kode, teks = daftar_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=f"[{kode}] {teks}")
            self.label_counter.config(text=f"Pertanyaan {self.index_pertanyaan + 1} dari {len(daftar_gejala)}")
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == 'y':
            kode = daftar_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)
        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    def proses_hasil(self):
        hasil = mesin_inferensi(self.gejala_terpilih)

        if hasil:
            teks_hasil = ""
            for i, (penyakit, penjelasan, tingkat) in enumerate(hasil, 1):
                teks_hasil += f"[{i}] {penyakit}\n"
                teks_hasil += f"     Kesesuaian: {tingkat:.0f}%\n"
                teks_hasil += f"     Keterangan: {penjelasan}\n\n"
        else:
            teks_hasil = "Tidak ditemukan penyakit THT yang cocok dengan gejala yang Anda masukkan.\n\nSilakan konsultasi langsung ke dokter spesialis THT."

        messagebox.showinfo("Hasil Diagnosa", teks_hasil)

        self.frame_jawaban.pack_forget()
        self.label_counter.config(text="")
        self.label_tanya.config(text="Diagnosa selesai. Ingin mengulang?")
        self.btn_mulai.config(text="Ulang Diagnosa")
        self.btn_mulai.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")
    app = AplikasiDiagnosa(root)
    root.mainloop()
