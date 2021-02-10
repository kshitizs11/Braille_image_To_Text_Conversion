#!/usr/bin/env python
# coding: utf-8

# In[4]:


from keras.models import Model,load_model
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2
# from gtts import gTTS
# from playsound import playsound
# import IPython


# In[5]:


# test_img = Image.open("test/AI and machine learning.png")
# test_img = test_img.convert("RGB")
# total_width,height = test_img.size
# n_chars = int(total_width/height/0.78)

# width_ind = total_width/n_chars
# # print(n_chars)
# # print(total_width,height)
# # print(width_ind)


# In[6]:


# plt.imshow(npimg1[:,:,:])
# plt.show()


# In[7]:


model = load_model("best_model1.h5")


# In[8]:


dicti ={'a': 0,
 'apostrophe': 1,
 'b': 2,
 'c': 3,
 'capitalize': 4,
 'colon': 5,
 'comma': 6,
 'd': 7,
 'e': 8,
 'exclamation mark': 9,
 'f': 10,
 'g': 11,
 'h': 12,
 'hyphen': 13,
 'i': 14,
 'j': 15,
 'k': 16,
 'l': 17,
 'm': 18,
 'n': 19,
 'number': 20,
 'o': 21,
 'p': 22,
 'period or decimal point': 23,
 'q': 24,
 'question mark': 25,
 'r': 26,
 's': 27,
 'semicolon': 28,
 'space': 29,
 't': 30,
 'u': 31,
 'v': 32,
 'w': 33,
 'x': 34,
 'y': 35,
 'z': 36}


# In[9]:


rev_dic = {0: 'a',
 1: 'apostrophe',
 2: 'b',
 3: 'c',
 4: 'capitalize',
 5: 'colon',
 6: 'comma',
 7: 'd',
 8: 'e',
 9: 'exclamation mark',
 10: 'f',
 11: 'g',
 12: 'h',
 13: 'hyphen',
 14: 'i',
 15: 'j',
 16: 'k',
 17: 'l',
 18: 'm',
 19: 'n',
 20: 'number',
 21: 'o',
 22: 'p',
 23: 'period or decimal point',
 24: 'q',
 25: 'question mark',
 26: 'r',
 27: 's',
 28: 'semicolon',
 29: 'space',
 30: 't',
 31: 'u',
 32: 'v',
 33: 'w',
 34: 'x',
 35: 'y',
 36: 'z'}

# In[15]:


def braille_text(path):
    test_img = Image.open(path)
    test_img = test_img.convert("RGB")
    total_width,height = test_img.size
    n_chars = int(total_width/height/0.78)
    width_ind = total_width/n_chars
    npimg1 = np.array(test_img)
    text = ""
    num = False
    capital = False
    for i in range(0,int(n_chars)):
        cropped = test_img.crop((i*width_ind,0,(i+1)*width_ind,height))
        cropped = np.array(cropped)
        cropped = cv2.resize(cropped,(50,50))
        cropped = cropped.astype(np.float32) / 255.0
        cropped = cropped.reshape(1,50,50,3)
        current = rev_dic[model.predict_classes(cropped)[0]]
        if num == True:
            if current == "period or decimal point":
                current = "."
                text+=current
            elif current == "semicolon":
                current = ";"
                text+=current
            elif current == "question mark":
                current = "?"
                text+=current
            elif current == "hyphen":
                current = "-"
                text+=current
            elif current == "exclamation mark":
                current = "!"
                text+=current
            elif current == "comma":
                current = ","
                text+=current
            elif capital==True:
                current = current.upper()
                capital = False
            elif current == "colon":
                current = ":"
                text+=current
            elif current == "apostrophe":
                current = "′"
                text+=current
            elif current == "space":
                current = " "
                text+=current
                num = False
            elif current == "number":
                current = ""
                text+=current
                continue
            elif current == "capitalize":
                capital = True
                current = ""
                continue
            elif capital == True:
                current = current.upper()
                capital = False
            if ord(current) in range(97,106):
                text+=chr(ord(current)-48)
            elif ord(current) == 106:
                text+=chr(48) 
            if current!=" ":
                continue
        if current=="capitalize":
            capital = True
            current = ""
        elif current=="space":
            current = " "
        elif capital==True:
            current = current.upper()
            capital = False
        elif current == "period or decimal point":
            current = "."
        elif current == "semicolon":
            current = ";"
        elif current == "question mark":
            current = "?"
        elif current == "hyphen":
            current = "-"
        elif current == "exclamation mark":
            current = "!"
        elif current == "comma":
            current = ","
        elif current == "colon":
            current = ":"
        elif current == "apostrophe":
            current = "′"
        elif current == "number":
            num =True
            current=""
        text+=current
    return text


# In[16]:


# braille_text("test/AI and machine learning.png")


# In[1]:


# start_text = "Braille Prediction output is"
# Full_text = start_text+" "+text
# tts = gTTS(Full_text,lang='en', slow=False)
# file_name ="./Braille_prediction2.wav" 
# tts.save(file_name)
# sound_file = file_name
# IPython.display.Audio(sound_file,autoplay=True)


# In[ ]:




