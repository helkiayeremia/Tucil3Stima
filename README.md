# Tucil3Stima

## Deskripsi

Program pencarian rute terpendek dari sebuah graph.Program ini dapat menerima sebuah file txt yang berisi N buah jumlah, node, pasangan nama node dan kooridnatnya beserta matriks ketetetangaan yang menyatakan keterhubungan node - node yang ada pada graph. Program akan menghitung rute terpendek dari node awal dan node akhir dengan menggunakan algoritma A*. Algoritma A* yang digunakan, menggunakan heuristik euclidean.

## Requirement

Python3
Anaconda
Jupyter Notebook
gmaps library

## Installation

Anaconda dapat didownload pada laman https://www.anaconda.com/products/individual <br>
Kemudian install Jupyter Notebook melalui Anaconda <br>
Setelah itu, Install library gmaps pada Anaconda prompt <br>

```bash
conda install -c conda-forge gmaps
```

## Usage

Masukkan file map dengan ekstensi .txt <br>
Format file sebagai berikut : <br>
Baris pertama diisi sebuah bilangan integer N yang menandakan banyaknya nodes yang ingin diinput <br>
Baris 2 sampai N+1 diisi dengan Nama node dan koordinat dipisahkan dengan spasi (nama_node x y) <br>
Baris N+1 sampai 2N+1 diisi dengan adjecency matrix dengan format setiap baris dan kolom dipisahkan dengan spasi <br>
Untuk lebih jelasnya dapat dilihat file - file yang sudah disediakan pada folder test <br> <br>

Buka folder src <br>
Di dalam folder src akan ada file Graph.ipynb dan Gmap.ipynb. <br>
Jika ingin menampilkan Graph saja gunakan Graph.ipynb dan gunakan Gmap.ipynb jika ingin menampilkan peta <br>
Jalankan setiap cell pada kedua file <br>
Pada cell di bawah markdown input, perlu melakukan input yang diminta kemudian menekan enter. setelah itu jalankan cell berikutnya <br>
Program akan menampilkan gambar Graph/Map sesuai input <br>

## Author

id Line : <br>
helkiayeremia2 <br>
jordandj500 <br>
