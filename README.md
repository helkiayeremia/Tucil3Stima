# Tucil3Stima

## Deskripsi

Program pencarian rute terpendek dari sebuah graph.Program ini dapat menerima sebuah file txt yang berisi N buah jumlah, node, pasangan nama node dan kooridnatnya beserta matriks ketetetangaan yang menyatakan keterhubungan node - node yang ada pada graph. Program akan menghitung rute terpendek dari node awal dan node akhir dengan menggunakan algoritma A*. Algoritma A* yang digunakan, menggunakan heuristik euclidean.

## Requirement

Python3
Anaconda
Jupyter Notebook
gmaps library

## Installation

Anaconda dapat didownload pada laman https://www.anaconda.com/products/individual
Kemudian install Jupyter Notebook melalui Anaconda
Setelah itu, Install library gmaps pada Anaconda prompt

```bash
conda install -c conda-forge gmaps
```

## Usage

Masukkan file map dengan ekstensi .txt
Format file sebagai berikut :
Baris pertama diisi sebuah bilangan integer N yang menandakan banyaknya nodes yang ingin diinput
Baris 2 sampai N+1 diisi dengan Nama node dan koordinat dipisahkan dengan spasi (nama_node x y)
Baris N+1 sampai 2N+1 diisi dengan adjecency matrix dengan format setiap baris dan kolom dipisahkan dengan spasi
Untuk lebih jelasnya dapat dilihat file - file yang sudah disediakan pada folder test

Buka folder src
Di dalam folder src akan ada file Graph.ipynb dan Gmap.ipynb.
Jika ingin menampilkan Graph saja gunakan Graph.ipynb dan gunakan Gmap.ipynb jika ingin menampilkan peta
Jalankan setiap cell pada kedua file
Pada cell di bawah markdown input, perlu melakukan input yang diminta kemudian menekan enter. setelah itu jalankan cell berikutnya
Program akan menampilkan gambar Graph/Map sesuai input

## Author

id Line :
helkiayeremia2
jordandj500
