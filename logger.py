import datetime
import logging
logging.getLogger('PIL.PngImagePlugin').setLevel(logging.WARNING)
logging.getLogger('PIL.Image').setLevel(logging.WARNING)

today=datetime.datetime.today().strftime('%d-%m-%Y')
logging.basicConfig(filename=f"Logs/{today}",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
