def calc_variance(penjualan_A, penjualan_B):
    # Fungsi untuk menghitung rata-rata
    def calc_mean(penjualan_A, penjualan_B):
        return (sum(penjualan_A) + sum(penjualan_B)) / (len(penjualan_A) + len(penjualan_B))
    
    mean = calc_mean(penjualan_A, penjualan_B)
    print(f"Mean: {mean}")  # Menampilkan mean untuk debugging
    
    # Kuadrat selisih antara setiap nilai data dengan rata-rata
    squared_diff = []
    for x in penjualan_A + penjualan_B:
        squared_diff_per_x = (x - mean)**2
        squared_diff.append(squared_diff_per_x)
    
    print(f"Squared Differences: {squared_diff}")  # Menampilkan daftar squared differences
    
    # Jumlah kuadrat selisih antara setiap nilai data dengan rata-rata, kemudian dibagi dengan jumlah total data
    variance = sum(squared_diff) / (len(penjualan_A) + len(penjualan_B))
    
    print(f"Variansi: {sum(squared_diff)} / {len(penjualan_A) + len(penjualan_B)} = {variance}")
    return variance

# Contoh pemanggilan fungsi
penjualan_A = [10, 20, 30]
penjualan_B = [15, 25, 35]

calc_variance(penjualan_A, penjualan_B)
