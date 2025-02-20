from rich.console import Console
from rich.table import Table

console = Console()

def read_expenses(expenses):
    table = Table()
    table.add_column("No", justify="left", style="white")
    table.add_column("Tanggal", justify="center", style="cyan")
    table.add_column("Jumlah", justify="center", style="magenta")
    table.add_column("Kategori", justify="center", style="green")
    table.add_column("Deskripsi", justify="left",  style="green")

    for expense in expenses:
        table.add_row(
            expense['no'], 
            expense['tanggal'], 
            "Rp " + str(expense['jumlah']), 
            expense['kategori'], 
            expense['deskripsi']
        )

    console.print(table)
