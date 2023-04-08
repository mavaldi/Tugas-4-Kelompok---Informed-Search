from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):

    # Set untuk menyimpan node yang sudah dikunjungi
    visited = set()

    # PriorityQueue untuk menyimpan node yang akan dikunjungi selanjutnya
    queue = PriorityQueue()

    # Memasukkan node awal ke dalam PriorityQueue dengan cost 0
    queue.put((0, [start]))

    while not queue.empty():

        # Mengeluarkan / mengambil node dengan cost terkecil dari PriorityQueue
        current_cost, current_path = queue.get()

        # Mengambil node terakhir dari path saat ini
        current_node = current_path[-1]

        # Jika node saat ini merupakan node tujuan return ke current_path
        if current_node == goal:
            return current_path

        # Jika node saat ini belum dikunjungi
        if current_node not in visited:

            # Menandai node saat ini sebagai sudah dikunjungi
            visited.add(current_node)

            # For loop untuk setiap tetangga dari node saat ini
            for neighbor in graph[current_node]:

                # Kondisi if jika tetangga belum dikunjungi
                if neighbor not in visited:

                    distance = graph[current_node][neighbor]

                    # Cost total dari node awal ke tetangga
                    estimated_cost = current_cost + distance + heuristic[neighbor]

                    # Membuat path baru dengan menyalin path saat ini
                    new_path = list(current_path)

                    # Menambahkan tetangga ke path baru
                    new_path.append(neighbor)

                    # Memasukkan path baru ke dalam PriorityQueue dengan cost total
                    queue.put((estimated_cost, new_path))
    return None

# Graph yang merepresentasikan jarak setiap kota dengan tetangganya
graph = {
    'Magetan': {'Ngawi': 32, 'Madiun': 22, 'Ponorogo': 34},
    'Ngawi': {'Magetan': 32, 'Madiun': 30, 'Bojonegoro': 44},
    'Bojonegoro': {'Ngawi': 44, 'Nganjuk': 33, 'Jombang': 70, 'Lamongan': 42},
    'Lamongan': {'Bojonegoro': 42, 'Gresik': 14},
    'Gresik': {'Lamongan': 14, 'Surabaya': 12},
    'Ponorogo': {'Magetan': 34, 'Madiun': 29},
    'Madiun': {'Magetan': 22, 'Ngawi': 30, 'Ponorogo': 29, 'Nganjuk': 48},
    'Nganjuk': {'Madiun': 48, 'Bojonegoro': 33, 'Jombang': 40},
    'Jombang': {'Nganjuk': 40, 'Bojonegoro': 70, 'Surabaya': 72},
    'Surabaya': {'Gresik': 12, 'Jombang': 72, 'Bangkalan': 44, 'Sidoarjo': 25},
    'Bangkalan': {'Surabaya': 44, 'Sampang': 52},
    'Sampang': {'Bangkalan': 52, 'Pamekasan': 31},
    'Pamekasan': {'Sampang': 31, 'Sumenep': 54},
    'Sumenep': {'Pamekasan': 54},
    'Sidoarjo': {'Surabaya': 25, 'Probolinggo': 78},
    'Probolinggo': {'Sidoarjo': 78, 'Situbondo': 99},
    'Situbondo': {'Probolinggo': 99}
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

result = a_star_search(graph, start, goal, heuristic)
print(result)