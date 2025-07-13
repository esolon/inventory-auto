import pandas as pd
from datetime import datetime
import os

def generate_html_table(df, title):
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h2 {{
            text-align: center;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid #ccc;
            padding: 8px;
            text-align: center;
        }}
        th {{
            background-color: #f2f2f2;
        }}
    </style>
    <!-- DataTables CDN -->
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
</head>
<body>

<h2>{title} (Searchable)</h2>
<p><strong>Last updated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

<table id="data-table">
    <thead>
        <tr>"""

    for col in df.columns:
        html += f"<th>{col}</th>"
    html += "</tr></thead><tbody>"

    for _, row in df.iterrows():
        html += "<tr>"
        for col in df.columns:
            html += f"<td>{row[col]}</td>"
        html += "</tr>"

    html += """
    </tbody>
</table>

<!-- DataTables JS -->
<script src="https://code.jquery.com/jquery-3.7.0.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
<script>
    $(document).ready(function () {
        $('#data-table').DataTable();
    });
</script>

</body>
</html>"""
    return html

def update_html_table(xlsx_path, html_path, title):
    # Read Excel and skip the timestamp row
    df = pd.read_excel(xlsx_path, skiprows=1)

    # 🔍 Debug: Print headers and row count
    print(f"\n📄 {title} HEADERS: {list(df.columns)}")
    print(f"🔢 {title} ROW COUNT: {len(df)}")

    # Generate and save HTML
    html_content = generate_html_table(df, title)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Updated: {html_path}")

# === Update both Inventory and PO Status HTML ===

update_html_table(
    r"C:\Users\esolon\OneDrive - Boston Semi Equipment LLC\Github Projects\Inventory\inventory.xlsx",
    r"C:\Users\esolon\OneDrive - Boston Semi Equipment LLC\Github Projects\Inventory\index.html",
    "Inventory"
)

update_html_table(
    r"C:\Users\esolon\OneDrive - Boston Semi Equipment LLC\Github Projects\PO_Status\po-status.xlsx",
    r"C:\Users\esolon\OneDrive - Boston Semi Equipment LLC\Github Projects\PO_Status\index.html",
    "PO Status"
)