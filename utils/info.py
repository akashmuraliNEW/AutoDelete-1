#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "20786733"))
API_HASH     = os.environ.get("API_HASH", "d8b4eae3db613c5bb4654f9cb2d73e83")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "6321385282:AAFwQI1LKr5RSa0M3r1xxskL1ZmYfZ0cJNs")
SESSION      = os.environ.get("SESSION", "AQE9Li0AnvCsI3V8xU5-8WKm95e8jrpabrRibgvs0_DzkN_odu4rex6LfKcMfryJWJnatzXlJ8gBP5JHPgE_gpUYPMyocDvISoiPgo6lb40BW_Z_tQWqN4Za1dJe5j09jOArkZNI7P67rd_s6h61umLYjpEPsYnNZUvaOzw3wvKrv8oH0iTAhRHqsgS7sy6_q6MFz47LKbXlDXR2UyiRmZW0QlX2toF2Xvem_lt8Lf1M1LfXmLE2q2aOfARBiKypzLy58piIMBgroiPb-iJT3fZ0vI7c_iaJo2NM9G9j0XAZvGWDc3bgx5DQ5M4aagAVkKgpcA6ymXpPfKFhlQVGRFyjmt6Y4QAAAAFM5OJNAA")
TIME         = int(os.environ.get("TIME", 10))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1001914144088 -1002153616127 -1002153616127").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://tg:tg@cluster0.3ntpyoc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT         = os.environ.get("PORT", "8080")
