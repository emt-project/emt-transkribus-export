# emt-transkribus-export
Repo for exporting data from Transkribus

* GH-Action `download_collections` downloads METS from Transkribus-Collections listed in `col_ids.csv` and applies page2tei to create generic XML/TEI files which are stored in `alltei`.
* Those generic XML/TEIs can be further processed with `python scripts/create_templates.py` into semantically enriched XML/TEIs 