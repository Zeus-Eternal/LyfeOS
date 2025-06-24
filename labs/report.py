import duckdb
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table
import os

DB_PATH = os.environ.get("DUCKDB_PATH", "/data/lyfe.duckdb")

console = Console()

def weekly_summary():
    conn = duckdb.connect(DB_PATH)
    df = conn.execute("SELECT date(timestamp) d, count(*) c FROM reflections_plain GROUP BY d ORDER BY d DESC LIMIT 7").fetchdf()
    conn.close()
    table = Table(title="Reflections Last 7 Days")
    table.add_column("Date")
    table.add_column("Count")
    for _, row in df.iterrows():
        table.add_row(str(row['d']), str(row['c']))
    console.print(table)
    plt.figure(figsize=(6,3))
    plt.bar(df['d'], df['c'])
    plt.title('Reflections per Day')
    plt.tight_layout()
    plt.savefig('/data/report.png')

if __name__ == '__main__':
    weekly_summary()
