from MyLogger import MyLogger
import os


if __name__ == '__main__':
    print('Program begin!')
    logger = MyLogger("TaglotJsonMaker").logger
    logger.info(f'Program Start!')
    logger.info(f'Program End!')
    print('Program End!')
