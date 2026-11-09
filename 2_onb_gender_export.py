import csv
import xml.etree.ElementTree as ET

INPUT_FILE = "/Users/lisateichmann/Desktop/ONB_gender/onb_extract/LT_131026_onb_request_before2013_xmlresults.xml"
OUTPUT_FILE = "/Users/lisateichmann/Desktop/ONB_gender/LT_131026_onb_request_before2013_xmlresults.csv"

# MARCXML namespace
ns = {
    "m": "http://www.loc.gov/MARC21/slim"
}

tree = ET.parse(INPUT_FILE)
root = tree.getroot()


def get_subfields(record, tag, code):
    """
    Return all matching MARC subfield values from one record.
    Example: get_subfields(record, "020", "a") returns all ISBNs.
    """
    values = []

    for datafield in record.findall(f"m:datafield[@tag='{tag}']", ns):
        for subfield in datafield.findall(f"m:subfield[@code='{code}']", ns):
            if subfield.text:
                values.append(subfield.text.strip())

    return values


with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)

    writer.writerow([
        "record_id",
        "author",
        "author_id",
        "title",
        "publication_date",
        "language",
        "isbns"
    ])

    for record in root.findall("m:record", ns):

        # Optional: MARC control number 001, useful for identifying each record
        record_id = record.findtext(
            "m:controlfield[@tag='001']",
            default="",
            namespaces=ns
        ).strip()

        # 100$a: main author
        authors = get_subfields(record, "100", "a")

        # 100$0: authority/author ID
        author_ids = [
    author_id.replace("(DE-588)", "").strip()
    for author_id in get_subfields(record, "100", "0")
]

        # 245$a: title
        title_parts = get_subfields(record, "245", "a")

        # 245$b: subtitle, if it exists
        subtitle_parts = get_subfields(record, "245", "b")

        # 264$c: publication date
        dates = get_subfields(record, "264", "c")

        # 041$a: language code(s)
        languages = get_subfields(record, "041", "a")

        # 020$a: ISBN(s)
        isbns = get_subfields(record, "020", "a")

        # Combine main title and subtitle
        title = " : ".join(title_parts + subtitle_parts)

        # Use " | " when a record has multiple values
        writer.writerow([
            record_id,
            " | ".join(authors),
            " | ".join(author_ids),
            title,
            " | ".join(dates),
            " | ".join(languages),
            " | ".join(isbns)
        ])

print(f"CSV file created: {OUTPUT_FILE}")