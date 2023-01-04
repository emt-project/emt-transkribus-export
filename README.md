# emt-transkribus-export
Repo for exporting data from Transkribus

* GH-Action `download_collections` downloads METS from Transkribus-Collections listed in `col_ids.csv` and applies [page2tei](https://github.com/dariok/page2tei) (by [@dariok](https://github.com/dariok)) to create generic XML/TEI files which are stored in `alltei`.
* Those generic XML/TEIs can be further processed with `python scripts/create_templates.py` into semantically enriched XML/TEIs


## iiif access

https://viewer.acdh.oeaw.ac.at/viewer/image/Kasten_blau_44_10_0004/
-> https://viewer.acdh.oeaw.ac.at/viewer/api/v1/records/Kasten_blau_44_10_0004/files/images/Kasten_blau_44_10_0004.jpg/info.json
