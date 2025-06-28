# Export DB
import csv, sqlite3, json

def export_to_csv(db_name):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

    with open("passwords_export.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(data)

    print(f">>> Data export to \"passwords_export.csv\"")

def export_to_json(db_name):
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        data = [dict(row) for row in cursor.fetchall()]

    with open('passwords_export.json', 'w', encoding='utf-8') as f:
        json.dump(str(data), f, indent=2, ensure_ascii=False)

    print(f">>> Data export to \"passwords_export.json\"")

def export_to_sql(db_name):
    with sqlite3.connect(db_name) as conn:
        with open('passwords_export.sql', 'w', encoding='utf-8') as f:
            for line in conn.iterdump():
                f.write(f"{line}\n")

    print(f">>> Data export to \"passwords_export.sql\"")



