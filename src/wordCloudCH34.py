import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud,ImageColorGenerator
def channel34(text,imgPath,savePath,format):

    img=np.array(Image.open(imgPath))
    wordcloud=WordCloud(background_color="white", max_words=3000, mask=img,mode="RGBA").generate(text)    
    img_color=ImageColorGenerator(img)
    plt.imshow(wordcloud.recolor(color_func=img_color), interpolation='bilinear')
    plt.axis("off")
    plt.savefig(savePath,format=format)
    plt.show()