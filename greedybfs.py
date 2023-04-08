from queue import PriorityQueue

# Implementasi fungsi Greedy Best-First Search
def greedy_best_first_search(graph, start, goal, heuristic):

    # Set untuk menampung node yang sudah dikunjungi
    visited = set()

    # Inisialisasi queue dengan PriorityQueue dan memasukkan start node
    queue = PriorityQueue()
    queue.put((0, [start]))

    # List untuk menampung jalur yang memenuhi kriteria
    paths = []

    while not queue.empty():

        # Mengambil jalur dengan cost terkecil pada queue
        current_cost, current_path = queue.get()

        # Mengambil node terakhir pada jalur
        current_node = current_path[-1]

        # Jika node terakhir sama dengan goal, tambahkan jalur ke list paths
        if current_node == goal:
            paths.append(current_path)

        # Jika node belum dikunjungi, tambahkan ke set visited
        if current_node not in visited:
            visited.add(current_node)

            # Looping untuk setiap node tetangga
            for neighbor in graph[current_node]:

                # Jika tetangga belum dikunjungi
                if neighbor not in visited:

                    # Hitung estimated cost dari tetangga menggunakan heuristic
                    estimated_cost = heuristic[neighbor]

                    # Buat jalur baru dengan menambahkan tetangga pada akhir jalur saat ini
                    new_path = list(current_path)
                    new_path.append(neighbor)

                    # Tambahkan jalur baru ke queue dengan cost estimated_cost
                    queue.put((estimated_cost, new_path))

    # Return list paths yang memenuhi kriteria
    return paths

# Graph yang merepresentasikan tetangga-tetangga dari setiap kota
graph = {
    'Magetan': {'Ngawi', 'Madiun', 'Ponorogo'},
    'Ngawi': {'Magetan', 'Madiun', 'Bojonegoro'},
    'Bojonegoro': {'Ngawi', 'Nganjuk', 'Jombang', 'Lamongan'},
    'Lamongan': {'Bojonegoro', 'Gresik'},
    'Gresik': {'Lamongan', 'Surabaya'},
    'Ponorogo': {'Magetan', 'Madiun'},
    'Madiun': {'Magetan', 'Ngawi', 'Ponorogo', 'Nganjuk'},
    'Nganjuk': {'Madiun', 'Bojonegoro', 'Jombang'},
    'Jombang': {'Nganjuk', 'Bojonegoro', 'Surabaya'},
    'Surabaya': {'Gresik', 'Jombang', 'Bangkalan', 'Sidoarjo'},
    'Bangkalan': {'Surabaya', 'Sampang'},
    'Sampang': {'Bangkalan', 'Pamekasan'},
    'Pamekasan': {'Sampang', 'Sumenep'},
    'Sumenep': {'Pamekasan'},
    'Sidoarjo': {'Surabaya', 'Probolinggo'},
    'Probolinggo': {'Sidoarjo', 'Situbondo'},
    'Situbondo': {'Probolinggo'}
}

# Heuristic value dari setiap kota (straight line distance dari setiap kota ke surabaya)
heuristic = {
    'Magetan': 162,
    'Surabaya': 0,
    'Ngawi': 130,
    'Ponorogo': 128,
    'Madiun': 126,
    'Bojonegoro': 60,
    'Nganjuk': 70,
    'Jombang': 36,
    'Lamongan': 36,
    'Gresik': 12,
    'Sidoarjo': 22,
    'Probolinggo': 70,
    'Situbondo': 146,
    'Bangkalan': 140,
    'Sampang': 90,
    'Pamekasan': 104,
    'Sumenep': 150
}

start = "Magetan"
goal = "Surabaya"

result = greedy_best_first_search(graph, start, goal, heuristic)
print(result)
