import numpy as np
from PIL import Image
from os import path
import pandas as pd
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
from src.numToString import NumToString
from src.wordCloudCH1 import channel1
from src.wordCloudCH34 import channel34


text=NumToString(1000)

channel1(imgPath="img/ataturk.png",savePath="img/ataturk1.png",text=text,format="png")

channel34(imgPath="img/h9.jpg",savePath="img/wine1.png",format="png",text=text)


