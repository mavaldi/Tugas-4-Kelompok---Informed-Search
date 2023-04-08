# Tugas-4-Kelompok---Informed-Search

| Nama | NRP |
| --- | --- |
| Andrian Tambunan | 5025211018 |
| Mavaldi Rizqy Hazdi | 5025211086 |
| Schaquille Devlin Aristano | 5025211211 |

## Greedy Best-First Search ```greedybfs.py```
  Greedy Best-First Search adalah sebuah algoritma pencarian jalur dalam graph yang mengutamakan node yang memiliki estimasi cost paling rendah untuk mencapai goal node. Algoritma ini digunakan untuk menyelesaikan masalah yang tidak memerlukan optimalitas yang mutlak dan dapat mengabaikan beberapa solusi yang lebih baik secara keseluruhan untuk mencapai solusi yang lebih cepat.
  
  Pada implementasi kode di atas, algoritma Greedy Best-First Search digunakan untuk mencari jalur terpendek dari kota "Magetan" ke kota "Surabaya" dalam graph yang telah didefinisikan. Algoritma ini menggunakan PriorityQueue untuk mengurutkan node-node berdasarkan estimasi cost terkecil untuk mencapai goal node. 
  
  Estimasi cost dihitung menggunakan heuristic, yaitu jarak lurus dari masing-masing kota ke kota "Surabaya". Dalam setiap iterasi, algoritma akan mengambil jalur dengan estimasi cost terkecil pada queue, kemudian memeriksa apakah node terakhir pada jalur sama dengan goal node. Jika ya, jalur akan ditambahkan ke list paths. Jika tidak, algoritma akan menambahkan node yang belum dikunjungi ke set visited dan menambahkan jalur baru ke queue dengan cost estimated_cost. Setelah semua jalur telah diperiksa, list paths yang memenuhi kriteria akan dikembalikan.

### Langkah-langkah algoritma Greedy Best-First Search adalah sebagai berikut:
1. Inisialisasi set visited untuk menampung node yang sudah dikunjungi.
2. Inisialisasi queue dengan PriorityQueue dan memasukkan start node.
3. Buat list paths untuk menampung jalur yang memenuhi kriteria.
4. Selama queue tidak kosong, lakukan langkah-langkah berikut:
   * Ambil node/jalur dengan cost terkecil pada queue.
   * Ambil node terakhir pada jalur.
   * Jika node terakhir sama dengan goal, tambahkan jalur ke list paths.
   * Jika node belum dikunjungi, tambahkan ke set visited.
   * Looping untuk setiap node tetangga.    
   * Jika tetangga belum dikunjungi, hitung estimated cost dari tetangga menggunakan heuristic.
   * Buat jalur baru dengan menambahkan tetangga pada akhir jalur saat ini.
   * Tambahkan jalur baru ke queue dengan cost estimated_cost.
5. Return list paths yang memenuhi kriteria.

## A* Search ```astar.py```
  A* search adalah algoritma pencarian graf yang digunakan untuk menemukan jalur terpendek antara dua titik dalam graf. Algoritma ini memanfaatkan heuristik untuk mempercepat pencarian jalur terpendek dengan menggunakan pendekatan Best-First Search dan menggabungkannya dengan nilai biaya aktual dari node awal ke node tujuan. 
  
  A* search mempertimbangkan biaya dari node saat ini dan perkiraan biaya sisa (disebut fungsi heuristik) untuk mencapai tujuan saat menentukan langkah selanjutnya dalam pencarian. Dengan demikian, A* search menemukan jalur terpendek dengan efisien dan optimal dalam ruang pencarian besar.

### Langkah-langkah algoritma A* Search adalah sebagai berikut:
1. Inisialisasi set visited untuk menampung node yang sudah dikunjungi.
2. Inisialisasi queue dengan PriorityQueue dan memasukkan start node.
3. Buat list paths untuk menampung jalur yang memenuhi kriteria.
4. Selama queue tidak kosong, lakukan langkah-langkah berikut:
    * Mengeluarkan node dengan cost terkecil dari PriorityQueue
    * Mengambil node terakhir dari path saat ini
    * Jika node saat ini merupakan node tujuan return ke current_path
    * Jika node saat ini belum dikunjungi
    * Menandai node saat ini sebagai sudah dikunjungi
    * Looping untuk setiap tetangga dari node saat ini
    * Jika tetangga belum dikunjungi
       * Membuat path baru dengan menyalin path saat ini
       * Menambahkan tetangga ke path baru
       * Memasukkan path baru ke dalam PriorityQueue dengan cost total
5. Return list paths yang memenuhi kriteria.

## Analisis Perbandingan Hasil Solusi / Output
Setelah melakukan running pada kedua algoritma A* Search dan Greedy Best-First Search, didapatkan hasil seperti berikut :
- Greedy Best-First Search
```sh
['Magetan', 'Madiun', 'Nganjuk', 'Jombang', 'Surabaya']
```
- A* Search
```sh
['Magetan', 'Ngawi', 'Bojonegoro', 'Lamongan', 'Gresik', 'Surabaya']
```
![image](https://user-images.githubusercontent.com/107263770/230710759-5af9a3a2-3e9e-4a32-861e-b858f729fdb7.png)

Dengan membandingkan kedua hasil dari algoritma search tersebut dapat dilihat jika, path yang dihasilkan oleh A* Search lebih baik dari Greedy Best-First Search karena jarak yang harus ditempuh dari hasil A* Search lebih singkat dengan perbandingan :
```sh
Greedy Best-First Search = 182 : A* Search = 144
```
Perbedaan hasil tersebut disebabkan oleh algoritma Greedy Best-First Search yang hanya memakai heuristic value atau straight line distance sebagai perbandingan yang memiliki kecenderungan salah yang lebih besar dari pada A* Search yang memakai jarak antar kota dan heuristic sebagai perbandingan sehingga hasil yang didapatkan lebih baik.






