# 1. Impor modul Flask dan render_template
#    - Flask: untuk membuat aplikasi web
#    - render_template: untuk menghubungkan Python ke file HTML
from flask import Flask, render_template

# 2. Inisialisasi aplikasi Flask
app = Flask(__name__)

# 3. Buat data sederhana (database sementara)
siswa_db = {
    '1': {
        'nama': 'Irfan Syahfutra', 
        'hobi': 'Badminton', 
        'cita_cita': 'Programmer',
        'foto': 'irfan.jpg',
        'instagram': 'irfansyftra' # irfansyftra
    },
    '2': {
        'nama': 'Satria Cahaya Mulia', 
        'hobi': '-', 
        'cita_cita': '-',
        'instagram': '-',
        'foto': '-'
    },
    '3': {
        'nama': 'AMALYA RAMADHANTI', 
        'hobi': '-', 
        'cita_cita': '-',
        'foto': '-'
    },
    '4': {
        'nama': 'VANNISYA RAHMA HALIZA', 
        'hobi': 'Nonton', 
        'cita_cita': 'CEO',
        'foto': 'vanni.jpeg',
        'instagram': 'vnnirh' # vnnirh
    },
    '5': {
        'nama': 'Nanda Gadis Supriadi', 
        'hobi': 'Bernyanyi', 
        'cita_cita': 'Sutradara',
        'foto': '-',
        'instagram': 'yondapple' # yondapple
    }
}

# 4. Halaman Utama (Dashboard)
@app.route('/')
def dashboard():
    # Mengirim data 'siswa_db' ke file 'dashboard.html'
    return render_template('dashboard.html', siswa_list=siswa_db)

# 5. Halaman Profil Siswa (Dinamis berdasarkan ID)
@app.route('/siswa/<id_siswa>')
def profil(id_siswa):
    # Mencari data siswa berdasarkan ID yang diklik
    siswa = siswa_db.get(id_siswa)
    return render_template('profil.html', siswa=siswa)

# 6. Jalankan server lokal jika file ini dieksekusi
if __name__ == '__main__':
    app.run(debug=True)