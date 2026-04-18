# H1D024111-PraktikumKB-Pertemuan5

## Program

### 1. Knowledge Base (`basis_pengetahuan`)

```python
basis_pengetahuan = {
    "Tonsilitis": {
        "gejala": {"G37", "G12", "G5", "G27", "G6", "G21"},
        "penjelasan": "Peradangan pada tonsil (amandel) ..."
    },
    ...
}
```

Basis pengetahuan disimpan dalam **dictionary Python** dengan struktur:
- **Key** → Nama penyakit THT (string)
- **Value** → Dictionary berisi:
  - `gejala`: `set` berisi gejala (G1–G37)
  - `penjelasan`: keterangan tentang penyakit tersebut

Program mencakup **23 jenis penyakit THT**:

| No | Penyakit | Gejala |
|----|----------|--------|
| 1 | Tonsilitis | G37, G12, G5, G27, G6, G21 |
| 2 | Sinusitis Maksilaris | G37, G12, G27, G17, G33, G36, G29 |
| 3 | Sinusitis Frontalis | G37, G12, G27, G17, G33, G36, G21, G26 |
| 4 | Sinusitis Edmoidalis | G37, G12, G27, G17, G33, G36, G21, G30, G13, G26 |
| 5 | Sinusitis Sfenoidalis | G37, G12, G27, G17, G33, G36, G29, G7 |
| 6 | Abses Peritonsiler | G37, G12, G6, G15, G2, G29, G10 |
| 7 | Faringitis | G37, G5, G6, G7, G15 |
| 8 | Kanker Laring | G5, G27, G6, G15, G2, G19, G1 |
| 9 | Deviasi Septum | G37, G17, G20, G8, G18, G25 |
| 10 | Laringitis | G37, G5, G15, G16, G32 |
| 11 | Kanker Leher & Kepala | G5, G22, G8, G28, G3, G11 |
| 12 | Otitis Media Akut | G37, G20, G35, G31 |
| 13 | Contact Ulcers | G5, G2 |
| 14 | Abses Parafaringeal | G5, G16 |
| 15 | Barotitis Media | G12, G20 |
| 16 | Kanker Nafasoring | G17, G8 |
| 17 | Kanker Tonsil | G6, G29 |
| 18 | Neuronitis Vestibularis | G35, G24 |
| 19 | Meniere | G20, G35, G14, G4 |
| 20 | Tumor Syaraf Pendengaran | G12, G34, G23 |
| 21 | Kanker Leher Metastatik | G29 |
| 22 | Osteosklerosis | G34, G9 |
| 23 | Vertigo Postular | G24 |

---

### 2. Daftar Gejala (`daftar_gejala`)

```python
daftar_gejala = [
    ("G1", "Apakah Anda mengalami nafas abnormal?"),
    ("G2", "Apakah suara Anda serak?"),
    ...
]
```

List of tuple yang berisi pasangan `(kode_gejala, teks_pertanyaan)`. Terdapat **37 pertanyaan gejala** yang akan ditampilkan satu per satu kepada user.

| Kode | Gejala |
|------|--------|
| G1 | Nafas abnormal |
| G2 | Suara serak |
| G3 | Perubahan kulit |
| G4 | Telinga penuh |
| G5 | Nyeri bicara menelan |
| G6 | Nyeri tenggorokan |
| G7 | Nyeri leher |
| G8 | Pendarahan hidung |
| G9 | Telinga berdenging |
| G10 | Airliur menetes |
| G11 | Perubahan suara |
| G12 | Sakit kepala |
| G13 | Nyeri pinggir hidung |
| G14 | Serangan vertigo |
| G15 | Getah bening |
| G16 | Leher bengkak |
| G17 | Hidung tersumbat |
| G18 | Infeksi sinus |
| G19 | Beratbadan turun |
| G20 | Nyeri telinga |
| G21 | Selaput lendir merah |
| G22 | Benjolan leher |
| G23 | Tubuh tak seimbang |
| G24 | Bolamata bergerak |
| G25 | Nyeri wajah |
| G26 | Dahi sakit |
| G27 | Batuk |
| G28 | Tumbuh dimulut |
| G29 | Benjolan dileher |
| G30 | Nyeri antara mata |
| G31 | Radang gendang telinga |
| G32 | Tenggorokan gatal |
| G33 | Hidung meler |
| G34 | Tuli |
| G35 | Mual muntah |
| G36 | Letih lesu |
| G37 | Demam |

---

### 3. Mesin Inferensi (`mesin_inferensi`)

```python
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
```

Cara kerja mesin inferensi:
1. Mengubah input gejala pengguna menjadi `set`
2. Untuk setiap penyakit, menghitung **irisan (intersection)** antara gejala input dengan gejala pada knowledge base
3. Jika **semua gejala cocok**, tingkat kesesuaian langsung ditetapkan **100%**
4. Jika ada **minimal 2 gejala yang cocok** (tapi belum semua), tingkat kesesuaian dihitung: `(gejala_cocok / total_gejala_penyakit) x 100`
5. Mengurutkan hasil dari tingkat kesesuaian tertinggi ke terendah

---

### 4. Kelas GUI (`AplikasiDiagnosa`)

Kelas menampilkan interface menggunakan **Tkinter**.

```python
class AplikasiDiagnosa:
    def __init__(self, root): ...   
    def mulai_tanya(self): ...      
    def tampilkan_pertanyaan(self): 
    def jawab(self, respon): ...    
    def proses_hasil(self): ...     
```

---

## Alur Kerja Program

```
[Mulai]
   │
   ▼
User klik "Mulai Diagnosa"
   │
   ▼
Pertanyaan gejala ditampilkan satu per satu
   │
   ├ Jawab YA  → gejala ditambahkan ke gejala_terpilih
   ├ Jawab TIDAK → lanjut ke pertanyaan berikutnya
   │
   ▼
Semua pertanyaan selesai → proses_hasil() dipanggil
   │
   ▼
mesin_inferensi(gejala_terpilih) dijalankan
   │
   ├ Semua gejala cocok (100%)
   │       → Tampilkan nama penyakit, kesesuaian 100%, dan keterangan
   │
   ├ Sebagian gejala cocok (≥2 gejala match)
   │       → Tampilkan nama penyakit, kesesuaian %, dan keterangan
   │
   ├ Tidak ada yang cocok
           → Tampilkan pesan konsultasi ke dokter spesialis THT
   │
   ▼
Pengguna bisa "Ulang Diagnosa"
```

### Penjelasan Kode dari Alur Kerja

#### Langkah 1 - Memulai Diagnosa
```python
def mulai_tanya(self):
    self.gejala_terpilih = []   
    self.index_pertanyaan = 0   
    self.btn_mulai.pack_forget()
    self.frame_jawaban.pack(pady=15)
    self.tampilkan_pertanyaan()  
```
Saat tombol "Mulai Diagnosa" ditekan, semua state direset dan proses tanya jawab dimulai. List `gejala_terpilih` dikosongkan untuk diagnosa baru dimulai dari awal.

#### Langkah 2 - Menampilkan Pertanyaan
```python
def tampilkan_pertanyaan(self):
    if self.index_pertanyaan < len(daftar_gejala):
        kode, teks = daftar_gejala[self.index_pertanyaan]
        self.label_tanya.config(text=f"[{kode}] {teks}")
        self.label_counter.config(text=f"Pertanyaan {self.index_pertanyaan + 1} dari {len(daftar_gejala)}")
    else:
        self.proses_hasil()  # Semua pertanyaan selesai
```
Setiap pertanyaan ditampilkan berurutan (contoh: `[G6] Apakah Anda mengalami nyeri tenggorokan?`). Label counter menunjukkan progres pertanyaan ke berapa dari total 37. Ketika `index_pertanyaan` melebihi jumlah gejala, proses inferensi dijalankan.

#### Langkah 3 - Jawaban
```python
def jawab(self, respon):
    if respon == 'y':
        kode = daftar_gejala[self.index_pertanyaan][0]
        self.gejala_terpilih.append(kode)
    self.index_pertanyaan += 1
    self.tampilkan_pertanyaan()  
```
Jika pengguna menjawab YA, kode gejala disimpan ke list `gejala_terpilih`. Jika TIDAK, langsung lanjut tanpa menyimpan apapun. Index pertanyaan selalu bertambah 1.

#### Langkah 4 - Proses Inferensi & Tampilkan Hasil
```python
def proses_hasil(self):
    hasil = mesin_inferensi(self.gejala_terpilih)
    if hasil:
        teks_hasil = ""
        for i, (penyakit, penjelasan, tingkat) in enumerate(hasil, 1):
            teks_hasil += f"[{i}] {penyakit}\n"
            teks_hasil += f"     Kesesuaian: {tingkat:.0f}%\n"
            teks_hasil += f"     Keterangan: {penjelasan}\n\n"
    else:
        teks_hasil = "Tidak ditemukan penyakit THT yang cocok ..."
    messagebox.showinfo("Hasil Diagnosa", teks_hasil)
```
Setelah semua 37 pertanyaan dijawab, fungsi `mesin_inferensi()` dipanggil. Hasil diagnosa ditampilkan dalam messagebox berisi daftar penyakit yang terdeteksi dan persentase kesesuaian serta keterangan penyakit. Jika tidak ada penyakit yang cocok, ditampilkan pesan untuk konsultasi ke dokter spesialis THT.
