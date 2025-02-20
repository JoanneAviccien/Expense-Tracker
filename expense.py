from datetime import datetime

def load_expenses(filename="expenses.csv"):
    expenses = []
    with open(filename, "r") as file:
        for line in file:
            no, tanggal, jumlah, kategori, deskripsi = line.strip().split(",")
            expenses.append({
                "no": no,
                "tanggal": tanggal,
                "jumlah": int(jumlah),
                "kategori": kategori,
                "deskripsi": deskripsi
            })
    return expenses

def save_expenses(expenses, filename="expenses.csv"):
    expenses.sort(key=lambda x: datetime.strptime(x["tanggal"], "%Y-%m-%d"))
    for i, expense in enumerate(expenses, start=1):
        expense["no"] = str(i)
    with open(filename, "w") as file:
        for expense in expenses:
            file.write(f"{expense['no']},{expense['tanggal']},{expense['jumlah']},{expense['kategori']},{expense['deskripsi']}\n")
