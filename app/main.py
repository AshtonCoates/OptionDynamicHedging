from app.hedge import Hedge
from app.get_option import GetOption

if __name__ == "__main__":

    tk = input('Enter a ticker symbol: ')
    exp = input('Enter an expiration date in the format MM/DD/YYYY: ')
    buy = input('Enter a date of purchase in the format MM/DD/YYYY: ')
    freq = input('Enter a frequency of adjustment, either "hour", "day", "month", or "year": ')
