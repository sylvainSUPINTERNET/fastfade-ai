from fastapi import UploadFile
from app.services.firebase_conf import FirebaseConf
from firebase_admin import storage
import logging

class UploadService():

    def __init__(self, firebase_conf:FirebaseConf) -> None:
        self.chunk_size = 1024 * 1024  # 1 MB per chunk
        self.firebase_conf = firebase_conf

    def process_file(self, media:UploadFile):
        logging.info(f"Processing file ... {media}")
        
        # bucket = storage.bucket() # storage bucket
        # blob = bucket.blob("audio.mp3")
        # blob.upload_from_filename(r"D:\Dev\workspace\fastfade-ai\audio.mp3", content_type="audio/mp3")


        # print("Processing file")
        # print(media.file)
        # print(self.firebase_conf.firebase_storage_bucket)

        # try:
        #     while ( chunk := media.file.read(self.chunk_size) ):
        #         print(chunk)
        # except Exception as e:
        #     print(e)
        # finally:
        #     media.file.close()

