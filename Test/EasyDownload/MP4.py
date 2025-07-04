# 23.06.24

# Fix import
import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(src_path)



# Import
from StreamingCommunity.Util.message import start_message
from StreamingCommunity.Util.os import os_summary
os_summary.get_system_summary()
from StreamingCommunity.Util.logger import Logger
from StreamingCommunity.Lib.Downloader import MP4_downloader


start_message()
logger = Logger()
path, kill_handler = MP4_downloader(
    url="https://148-251-75-109.top/Getintopc.com/IDA_Pro_2020.mp4",
    path=r".\\Video\\undefined.mp4"
)

thereIsError = path is None
print(thereIsError)