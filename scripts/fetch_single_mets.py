import os
import pandas as pd
from tqdm import tqdm
from transkribus_utils.transkribus_utils import ACDHTranskribusUtils

user = os.environ.get("TR_USER")
pw = os.environ.get("TR_PW")
col_id = os.environ.get("colId")
doc_id = os.environ.get("docId")


mets_dir = os.path.join(".", "mets", col_id)
print(mets_dir)
transkribus_client = ACDHTranskribusUtils(
    user=user, password=pw, transkribus_base_url="https://transkribus.eu/TrpServer/rest"
)
mets_file = transkribus_client.save_mets_to_file(doc_id, col_id, file_path=mets_dir)

print(mets_file)