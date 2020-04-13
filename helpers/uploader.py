from youtube_upload.auth import GoogleAuth
from youtube_upload.youtube import Youtube

from config import Config

from translations import Messages as tr

import os
import time
import traceback

class Uploader:

    def __init__(self, file, title=None):
        
        self.file = file
        
        self.title = title


    async def start(self, progress=None, *args):
        self.progress = progress
        self.args = args

        await self._upload()

        return self.status, self.message


    async def _upload(self):
        try:

            auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)
            
            if not os.path.isfile(Config.CRED_FILE):
                self.status = False
                
                self.message = "Upload failed because you did not authenticate me."
                
                return

            auth.LoadCredentialsFile(Config.CRED_FILE)

            google = auth.authorize()

            properties = dict(
                title = self.title if self.title else os.path.basename(self.file),
                description = 'ezel part 54, ezel part 55, ezel part 56, ezel part 57, ezel part 58, ezel part 59 ezel part 60, ezel part 61, ezel part 62, ezel part 63, ezeldrama part 45, ezel drama part 48, ezel drama, new part ezel drama, new part ezel, ezel drama amharic, kana tv, kanatelevision ezel, ezel, e zel drama part 45, ezel kana tv drama, ezel kana tv, ezel turkish drama, ezel turkishseries, ezel film, ezel part 44 kana tv, ezel part 50, ezel part 44, Kana TV, firdegnochu, ferdegnochu, ende enat, buzu tube, yalaleke fikir, ezal, ezele, ኢዘል ክፋል 45, ኢዘል ክፋል 46, ኢዘል ክፋል, 4 7, ኢዘል ክፋል 48, ኢዘል ክፋል 49, ኢዘል ክፋል 50,, ezel part 55, ezel amharic, ezel amharic part 66 ezel amharic part 67,ezel amharic part 58,ezel amharic part 63, ezel amharic part 61,ezel amharic part 62, ezel amharic part 64,ezel amharic part 65, ezel amharic part 57, ezel amharic part 63,ezel amharic part 60, ezel amharic part 59, ezel amharic part 65,ፍርደኞቹ ምእራፍ 2 ክፍል 100 ፍርደኞቹ ምእራፍ 2 ክፍል 101, ፍርደኞቹ ምእራፍ 2 ክፍል 10, ፍርደኞቹ ምእራፍ 2 ክፍል 99, ፍርደኞቹ ምእራፍ 2 ክፍል 103, ፍርደኞቹ ምእራፍ 2 ክፍል 104,ፍርደኞቹ ምእራፍ 2 ክፍል 105, feredenochu part 97, feredenochu part 98, feredenochu part 99, feredenochu part 100, feredenochu part 101, ፍርደኞቹ ምእራፍ 2 ክፍል 93, ፍርደኞቹ ምእራፍ 2 ክፍል 92, ፍርደኞቹ ምእራፍ 2 ክፍል 91, ፍርደኞቹ ምእራፍ 2 ክፍል 94, feredenochu part 85, feredenochu part 86, feredenochu part 87, feredenochu part 88, feredenochu part 89, feredenochu part 90, feredenochu part 91,ፍርደኞቹ part 93,feredenochu, feredenochu 90,, feredenochu season 2 part 97– kana tv amharic drama, feredenochu kana tv, feredenochu part 89– kana tv amharic drama, feredenochu season 2 part 95, feredenochu season 2 part 94, feredenochu season 2 part 93, feredenochu season 2 part 92, feredenochu season 2 part 91, feredenochu season 2, feredenochu season 2 part 90– kana tv amharic drama, feredenochu season 2 part 96, feredenochu part 2– kana tv,feredenochu kana tv part 101, feredenochu kana tv part 102, feredenochu kana tv part 100, feredenochu kana tv part 99, feredenochu kana tv part 103, feredenochu kana tv part 104,feredenochu kana tv part 98, feredenochu kana tv part 105, feredenochu kana tv part 106, feredenochu kana tv part 97,feredenochu kana tv part 99, feredenochu kana tv part 100, feredenochu kana tv part 101, feredenochu kana tv part 102, feredenochu kana tv part 103, feredenochu kana tv part 104, feredenochu kana tv part 105, feredenochu kana tv part 106, feredenochu kana tv part 107,feredenochu kana tv part 108,feredenochu, kana tv part 109, feredenochu kana tv part 110, feredenochu kana tv part 111, feredenochu kana tv part 91, kana tv, feredenochu season 2, feredenochu part2
',
                category = 27,
                privacyStatus = 'public'
            )

            youtube = Youtube(google)

            self.start_time = time.time()
            self.last_time = self.start_time

            r = await youtube.upload_video(video = self.file, properties = properties)

            self.status = True
            self.message = f"https://youtu.be/{r['id']}"
        except Exception as e:
            traceback.print_exc()
            self.status = False
            self.message = f"Error occuered during upload.\nError details: {e}"
        return

