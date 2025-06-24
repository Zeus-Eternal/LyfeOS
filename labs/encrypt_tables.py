import os
import duckdb

DB_PATH = os.environ.get("DUCKDB_PATH", "/data/lyfe.duckdb")
KEY_HEX = os.environ.get("LYFE_KEY_HEX")

SQL_SETUP = """
INSTALL crypto;
LOAD crypto;
"""

def encrypt_reflections():
    if not KEY_HEX:
        raise RuntimeError("LYFE_KEY_HEX env var not set")
    conn = duckdb.connect(DB_PATH)
    conn.execute(SQL_SETUP)
    conn.execute(f"CREATE SECRET KEY lyfe_key USING 'xchacha20' KEY_HEX '{KEY_HEX}';")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS reflections_encrypted AS\n"
        "SELECT encrypt(lyfe_key, reflection_text) AS blob, timestamp\n"
        "FROM reflections_plain;"
    )
    conn.close()

if __name__ == "__main__":
    encrypt_reflections()
