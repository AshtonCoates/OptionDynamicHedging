import yahoo_fin as yf
from yahoo_fin import options
import pandas as pd

chain = yf.options.get_options_chain('nflx')