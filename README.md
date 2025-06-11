# 🔗 URL Extractor & Status Checker from `.docx` Files

This Python script extracts **all URLs** from a Microsoft Word `.docx` document—including from **paragraphs**, **tables**, **headers**, **footers**, and **footnotes**—and checks the HTTP status of each URL. The results are saved into an Excel report for further review.

---

## 📌 Features

* 📄 Extracts URLs from:

  * Body paragraphs
  * Table cells
  * Headers and footers
  * Footnotes (via raw XML parsing)
* 🌐 Checks the HTTP status of each URL
* 📊 Generates a clean Excel report showing:

  * URL
  * Status Code
  * Human-readable Status Description
* ❌ Handles errors gracefully (e.g. network issues or invalid URLs)

---

## 🖥️ Sample Output (Excel)

| URL                                                | Status Code | Description          |
| -------------------------------------------------- | ----------- | -------------------- |
| [https://example.com](https://example.com)         | 200         | Working              |
| [https://nonexistent.org](https://nonexistent.org) | 404         | Not Found            |
| [http://timeout-site.com](http://timeout-site.com) | Error       | Connection Timed Out |

---

## ⚙️ Requirements

Install the required Python libraries:

```bash
pip install python-docx lxml pandas openpyxl requests
```

---

## 📂 File Structure

```
project-folder/
│
├── main.py       # This script
├── example.docx                # Your input Word document
├── url_status_report.xlsx      # Generated output
```

---

## 🚀 How to Use

### 🔧 Option 1: With file path

```python
docx_file = 'example.docx'  # Provide the path to your Word file
```

### 🔧 Option 2: With file bytes

```python
with open('example.docx', 'rb') as f:
    docx_file = f.read()
```

### ▶️ Run the script

```bash
python main.py
```

### ✅ Output

The script will:

1. Extract all URLs from the `.docx` file.
2. Check their status using HTTP requests.
3. Export the results to `url_status_report.xlsx`.

---

## 🛡️ Error Handling

The script gracefully handles:

* Connection timeouts
* Invalid URLs
* Unknown status codes

All exceptions are recorded in the Excel report for traceability.

---

## 📚 Functions Overview

| Function                                      | Description                                                                 |
| --------------------------------------------- | --------------------------------------------------------------------------- |
| `extract_urls_from_docx(docx_file)`           | Extracts all URLs from paragraphs, tables, headers, footers, and footnotes. |
| `check_urls_and_create_excel(urls, filename)` | Sends HTTP requests and generates an Excel file with status info.           |
| `get_status_description(status_code)`         | Maps common HTTP status codes to human-readable strings.                    |

---

## 📃 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Wolfie Crypto**
Built with ❤️ using Python, `docx`, and `pandas`
