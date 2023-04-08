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

## A* Search ```astar.py```
  A* search adalah algoritma pencarian graf yang digunakan untuk menemukan jalur terpendek antara dua titik dalam graf. Algoritma ini memanfaatkan heuristik untuk mempercepat pencarian jalur terpendek dengan menggunakan pendekatan Best-First Search dan menggabungkannya dengan nilai biaya aktual dari node awal ke node tujuan. 
  
  A* search mempertimbangkan biaya dari node saat ini dan perkiraan biaya sisa (disebut fungsi heuristik) untuk mencapai tujuan saat menentukan langkah selanjutnya dalam pencarian. Dengan demikian, A* search menemukan jalur terpendek dengan efisien dan optimal dalam ruang pencarian besar.

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






