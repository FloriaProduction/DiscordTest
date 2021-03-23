from pypresence import Presence
from time import time
 
RPC = Presence("823747051257856020")
btns = [
    {
        "label": "VK",
        "url": "https://vk.com/neforelove"
    },
    {
        "label": "Telegram",
        "url": "https://t.me/neforelove"
    }
]
 
RPC.connect()
RPC.update(
    details="Чай с лимоном",
    start=time(),
    buttons=btns,
    large_image="download",
    large_text="Тоже хочёшь чай? Держи ^-^",
)
 
input() # Чтобы программа резко не закрывалась.