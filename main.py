from GUIComponents.UserInitComponent import UserInit
from logger import logging


logger = logging.getLogger('Office Application')
if __name__ == "__main__":
    try:
        logger.info("____________________________________________________________________________________________")
        logger.info("Starting Application.")
        newUser = UserInit()
        newUser.initUserWindow()
    except Exception as error:
        logger.error(f"Error while starting.{error}")
