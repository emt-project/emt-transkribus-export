import glob
import jinja2
import pandas as pd
import os
from acdh_tei_pyutils.tei import TeiReader
from dateutil.parser import parse, ParserError
from datetime import date
import tqdm
import lxml.etree as ET


templateLoader = jinja2.FileSystemLoader(searchpath="./scripts/templates")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template('tei_template.xml')

df = pd.read_csv('gesamtliste_enriched.csv')
files = glob.glob('./alltei/*.xml')

file_mapper = {}
header = ['file', 'exception']
failed = []
for x in files:
    _, tail = os.path.split(x)
    try:
        doc = TeiReader(x)
    except Exception as e:
        failed.append([tail, e])
        continue
    title = doc.any_xpath('.//tei:title[@type="main"]/text()')[0]
    file_mapper[title] = x

no_match = []
for gr, df in tqdm.tqdm(df.groupby('folder')):
    try:
        doc_id = file_mapper[gr]
    except KeyError:
        no_match.append(gr)
        continue
    file_name = f"./data/editions/{gr}.xml"
    doc = TeiReader(doc_id)
    with open(file_name, 'w') as f:
        row = df.iloc[0]
        item = {}
        item['settlement'] = "München"
        item['repositor'] = "some archive in munich"
        item['id'] = gr.lower()
        item['file_name'] = f"{gr}.xml".lower()
        item['title'] = f"{row['weranwen']}, {row['Ort']} am {row['Datum']}"
        try:
            item['sender'] = row['weranwen'].split(' an ')[0]
        except:
            item['sender'] = row['weranwen']
        try:
            item['receiver'] = row['weranwen'].split(' an ')[-1]
        except:
            item['receiver'] = row['weranwen']
        item['place'] = row['Ort']
        item['writte_date'] = row['Datum']
        item['current_date'] = f"{date.today()}"
        body = doc.any_xpath('.//tei:body')[0]
        item["body_string"] = ET.tostring(body, encoding='utf-8', pretty_print=True).decode('utf-8')
        try:
            item['parsed_date'] = parse(item['writte_date'])
        except (ParserError, TypeError):
            item['parsed_date'] = None
        item['pages'] = []
        f.write(template.render(**item))
print(len(no_match))