import azure.core.exceptions
import requests
import json
import io
import shutil
from os import listdir
from os.path import isfile, join
import os
import pathlib
from pathlib import Path
from datetime import datetime
# from azure.storage.blob import BlobService
from azure.storage.blob import (BlobServiceClient, BlobClient, ContainerClient, ContentSettings)

jv_token = "ec16ae05-276a-4f63-a17c-59c0458c0901"
bearer_token = f'Bearer {jv_token}'.replace('"', '')

# gtin = ['062600963383']
gtin = ['062600964960'  # '00062600964328', '062600246165',
        #         '062600338990',
        #         '062600963086','062600965035',
        #         '062600443052', '62600964328', '62600230706', '62600964410', '62600964960', '62600278920', '62600262509',
        # '62600965240', '62600239402', '62600245526', '62600246103', '62600291981', '62600263001', '62600284952',
        # '62600271440', '62600262974', '62600262950', '62600315434', '62600338853', '62600306845', '62600283542',
        # '62600306869', '62600306876', '62600306890', '62600338921', '62600338938', '62600306043', '62600338945',
        # '62600338952', '62600338969', '62600338976', '62600338983', '62600338990', '62600351241', '62600375865',
        # '62600365385', '62600386267', '62600309280', '62600380159', '62600380227', '62600385338', '62600380562',
        # '62600380081', '62600380197', '62600380203', '62600380210', '62600365392', '62600380326', '62600380548',
        # '62600380555', '62600380579', '62600381132', '62600381149', '62600381156', '62600381170', '62600381187',
        # '62600381200', '62600381217', '62600381224', '62600400031', '62600400031', '62600400055', '62600444837',
        # '62600452931', '62600433787', '62600443052', '62600475527', '62600475534', '62600479013', '62600479020',
        # '62600479372', '62600479389', '62600621474', '62600475541', '62600415592', '62600415608', '62600415615',
        # '62600415622', '62600433848', '62600629678', '62600624376', '62600629685', '62600200211', '62600632616',
        # '62600492364', '62600492371', '62600501202', '62600501219', '62600501226', '62600514776', '62600514783',
        # '62600514790', '62600621368', '62600621740', '62600621757', '62600621764', '62600621771', '62600631497',
        # '62600635242', '62600430205', '62600451002', '62600460011', '62600470027'
        ]
baseGln = '0062600000019'

path_working_gs1 = ''

connection_string = "DefaultEndpointsProtocol=https;AccountName=samtdaentcadl;AccountKey=3DRT9Nrt9Ab8xKZNW8A4PDcf2H9gg4IyLpqD7j1SaSIzhhKSuqdgAmKH9xLE2PpPf/ALz8fWL4Vsmk3PC0NyXw==;EndpointSuffix=core.windows.net"
container_name = '$web'
"""https://agitt.medium.com/update-all-files-in-azure-blob-storage-or-change-content-types-with-python-script-83a14dabc5fc"""


def change_content_type_blob(connection_string, container):
    # Change this to the file extension you want to search for
    SEARCH_FILE_EXTENSION = [x.upper() for x in ['jpg', 'jpeg', 'tif']]
    # If not equal with this
    ORIGINAL_CONTENT_TYPE = "application/octet-stream"
    # Change with this.
    TO_CHANGE_CONTENT_TYPE = "image/jpeg"
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            conn_str=connection_string)

        blobs = blob_service_client.get_container_client(container).list_blobs()
        for blob in blobs:
            # If blob content type not is pdf then change
            extension = blob.name.split('.')[-1]
            # print(f"blob.name :: {blob.name}")
            if extension.upper() in SEARCH_FILE_EXTENSION:
                blob_client = blob_service_client.get_blob_client(container=container, blob=blob.name)
                blob.content_settings.content_type = TO_CHANGE_CONTENT_TYPE
                blob_client.set_http_headers(blob.content_settings)
                # print(f"content type ::: {blob_client.get_blob_properties().content_settings.content_type}")
                # print(f'URL: {blob_client.url}')

    except Exception as e:
        print(e)


for gtn in gtin:

    def process_media_download_detail(gtin=gtn, baseGln=baseGln):
        headers = {"Authorization": f"{bearer_token}", 'content-type': 'application/json'}

        url = "https://demo-api-contentdistribution.gs1ca.org/api/products/%s?baseGln=%s" % (
            gtin, baseGln)
        response = requests.get(
            url,
            headers=headers,
        )
        dataJsonMedia = response.json()
        dataJsonMedia = dict(dataJsonMedia)
        if response.status_code == 200:
            # print(response.status_code)
            # print(type(dataJsonMedia))
            for key, value in dataJsonMedia.items():
                ims = key
                if key == 'ecommerceContent':
                    # print(f"key: {key}, value: {value}")
                    # path
                    for i in range(len(dataJsonMedia['ecommerceContent'][0]['imageGroup'])):
                        formatFile = dataJsonMedia['ecommerceContent'][0]['imageGroup'][i]['format']
                        fileName = dataJsonMedia['ecommerceContent'][0]['imageGroup'][i]['gdti']
                        # print(f"{key}:{fileName}:{formatFile}")
                        # uploadToBlobStorage
                        uploadToBlobStorage(fileName=fileName, formatFile=formatFile, ims=ims, gtin=gtin)

                        # # append url image here to description
                        # # print(f"{key}, date: {datetime.now().date()}, gtin: {gtin}, type: {formatFile}, fileName: {fileName}.{formatFile}")
                        # url_from_azure_blob = f""" https://samtdaentcadl.z9.web.core.windows.net/api=media/content={key}/date={datetime.now().date()}/gtin={gtin}/type={formatFile}/{fileName}.{formatFile} """
                        # url_dict_add = dataJsonMedia['ecommerceContent'][0]['imageGroup'][i]
                        #
                        # url_dict_add.update({'url': url_from_azure_blob})
                        # print("Updated Dict is:", url_dict_add)

                if key == 'planoContent':
                    # path
                    for i in range(len(dataJsonMedia['planoContent'][0]['digitalAssetPlanogram'])):
                        # print(dataJsonMedia['planoContent'][0]['digitalAssetPlanogram'][i])
                        # get format and fileName
                        formatFile = dataJsonMedia['planoContent'][0]['digitalAssetPlanogram'][i][
                            'digitalAssetFormatPlanogram']
                        fileName = dataJsonMedia['planoContent'][0]['digitalAssetPlanogram'][i][
                            'digitalAssetGDTIPlanogram']
                        # print(f"{key}:{fileName}:{formatFile}")
                        # uploadToBlobStorage
                        uploadToBlobStorage(fileName=fileName, formatFile=formatFile, ims=ims, gtin=gtin)

                        # append url image here to description
                        url_file = f""" https://samtdaentcadl.z9.web.core.windows.net/api=media/content={key}/date={datetime.now().date()}/gtin={gtin}/type={formatFile}/{fileName}.{formatFile} """
                        # print(url_file)

                if key == 'marketingContent':
                    for i in range(len(dataJsonMedia['marketingContent'][0]['digitalAssetMarketing'])):
                        # print(dataJsonMedia['marketingContent'][0]['digitalAssetMarketing'][i])
                        # get format and fileName
                        formatFile = dataJsonMedia['marketingContent'][0]['digitalAssetMarketing'][i][
                            'digitalAssetFormatMarketing']
                        fileName = dataJsonMedia['marketingContent'][0]['digitalAssetMarketing'][i][
                            'digitalAssetGDTIMarketing']
                        print(f"{key}:{fileName}:{formatFile}")
                        # uploadToBlobStorage
                        uploadToBlobStorage(fileName=fileName, formatFile=formatFile, ims=ims, gtin=gtin)

            # print(json.dumps(dataJsonMedia['ecommerceContent'][0]['imageGroup']))
            # print(json.dumps(dataJsonMedia['planoContent'][0]))
        else:
            print(response.status_code)


    def uploadToBlobStorage(fileName, formatFile, ims, gtin):
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        headers = {"Authorization": f"{bearer_token}", 'Accept': 'image/jpeg', "content-type": "application/json", }
        url = "https://demo-api-contentdistribution.gs1ca.org/api/images/%s.%s" % (fileName, formatFile)
        response = requests.get(
            url,
            headers=headers, allow_redirects=True
        )
        # print(response.content)
        # destination blob
        destination_blob = f"api=media/content={ims}/date={datetime.now().date()}/gtin={gtin}/type={formatFile}/{fileName}.{formatFile}"
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=f'{destination_blob}')
        input_stream = io.BytesIO(response.content)

        # container = ContainerClient.from_connection_string(conn_str=connection_string, container_name=container_name,
        #                                                    )
        # blob_list = container.list_blobs()
        # file_count = 0
        # for blob in blob_list:
        #     # print(blob.name + '\n')
        #     if ".JPG" in blob.name:
        #         # Print file name and current content type to monitor progress
        #         print(f"For file {blob.name}  current type is {blob.content_settings.content_type}")
        #         # Note that in addition to content_type, you can also set the following values,
        #         # content_encoding, content_language, content_disposition, cache_control and content_md5
        #         blob.content_settings.content_type = "image/jpeg"
        #         #blob_service_client.get_blob_client(blob).set_http_headers(blob.content_settings)
        #         blob_client.set_http_headers(content_settings=cnt_settings)
        #         file_count += 1
        #
        # print(f"changing content type completed. Processed {file_count} files")

        try:
            blob_client.upload_blob(input_stream, blob_type="BlockBlob", overwrite=True)
            # print(f"blob_client.url::: {blob_client.url}")

        except azure.core.exceptions.ResourceExistsError as error:
            # print(f"blob_client.url::: {blob_client.url}")
            """Get url image example """
            """https://samtdaentcadl.z9.web.core.windows.net/api=media/content=planoContent/date=2023-07-31/gtin=062600230706/type=JPG/754000000015800000000265613280.JPG"""
            # print(error)
            pass


    process_media_download_detail(gtin=gtn, baseGln=baseGln)

change_content_type_blob(connection_string=connection_string, container=container_name)

print("finsh")
