from azure.storage.blob import (
    BlockBlobService
)
import pandas as pd
import io

output = io.StringIO()
head = ["col1", "col2", "col3"]
l = [[1, 2, 3], [4, 5, 6], [8, 7, 9]]
df = pd.DataFrame(l, columns=head)
print(df)
output = df.to_csv(index_label="idx", encoding="utf-8")
print(output)

accountName = "samtdaentcadl"
accountKey = "3DRT9Nrt9Ab8xKZNW8A4PDcf2H9gg4IyLpqD7j1SaSIzhhKSuqdgAmKH9xLE2PpPf/ALz8fWL4Vsmk3PC0NyXw=="
containerName = "dev-dl"
blobName = "test3.json"
blobService = BlockBlobService(account_name=accountName, account_key=accountKey)

blobService.create_blob_from_text(containerName, 'OutFilePy.csv', output)

# block_blob_service = BlockBlobService(account_name=accountName, account_key=accountKey)
# block_blob_service.create_blob_from_text(containerName, filename_with_path, encoding='utf-8', output)