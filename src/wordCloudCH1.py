import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
def channel1(text,imgPath,savePath,format):
        

    img=np.array(Image.open(imgPath))
    if len(img.shape)>2:
        img=img[:,:,0]
    def transform_format(val):
        if val == 0:
            return 255
        else:
            return val

    transformed_wine_mask = np.ndarray((img.shape[0],img.shape[1]), np.int32)

    for i in range(len(img)):
        transformed_wine_mask[i] = list(map(transform_format, img[i]))

    wordcloud=WordCloud(background_color="white", max_words=3000, mask=transformed_wine_mask,contour_width=3,contour_color='firebrick').generate(text)    
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(savePath,format=format)
    plt.show()