# Tugas-4-Kelompok---Informed-Search

| Nama | NRP |
| --- | --- |
| Andrian Tambunan | 5025211018 |
| Mavaldi Rizqy Hazdi | 5025211086 |
| Schaquille Devlin Aristano | 5025211211 |

## Greedy Best-First Search
  Greedy Best-First Search adalah sebuah algoritma pencarian jalur dalam graph yang mengutamakan node yang memiliki estimasi cost paling rendah untuk mencapai goal node. Algoritma ini digunakan untuk menyelesaikan masalah yang tidak memerlukan optimalitas yang mutlak dan dapat mengabaikan beberapa solusi yang lebih baik secara keseluruhan untuk mencapai solusi yang lebih cepat.
  Pada implementasi kode di atas, algoritma Greedy Best-First Search digunakan untuk mencari jalur terpendek dari kota "Magetan" ke kota "Surabaya" dalam graph yang telah didefinisikan. Algoritma ini menggunakan PriorityQueue untuk mengurutkan node-node berdasarkan estimasi cost terkecil untuk mencapai goal node. 
  Estimasi cost dihitung menggunakan heuristic, yaitu jarak lurus dari masing-masing kota ke kota "Surabaya". Dalam setiap iterasi, algoritma akan mengambil jalur dengan estimasi cost terkecil pada queue, kemudian memeriksa apakah node terakhir pada jalur sama dengan goal node. Jika ya, jalur akan ditambahkan ke list paths. Jika tidak, algoritma akan menambahkan node yang belum dikunjungi ke set visited dan menambahkan jalur baru ke queue dengan cost estimated_cost. Setelah semua jalur telah diperiksa, list paths yang memenuhi kriteria akan dikembalikan.

