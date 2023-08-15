#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import sklearn
import pandas as pd


# In[ ]:


# Data preprocessing
from collections import Counter
import re
import unicodedata
df = pd.read_excel('data.xlsx')
def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenization
    words = text.split()
    text = ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c))
    text = text.lower()
    return text

df['haber'] = df['haber'].apply(preprocess_text)
df['icerik'] = df['icerik'].apply(preprocess_text)
df.to_excel('processed_data.xlsx', index=False)


# In[ ]:


# Haberleri kategorize etme
import pandas as pd
def siniflandir(row):
    icerik = row['icerik']
    konu = row['konu']
    
    if pd.isnull(konu):
        if 'lojistik' in icerik.lower() or 'taşımacılık' in icerik.lower() or 'kargo' in icerik.lower() or 'teslimat' in icerik.lower():
            return 'Lojistik'
        elif 'yatırım' in icerik.lower():
            return 'Yatırım'
        elif 'e-ticaret' in icerik.lower() or 'online alışveriş' in icerik.lower():
            return 'E-Ticaret'
        elif 'güvenlik' in icerik.lower() or 'veri güvenliği' in icerik.lower() or 'KVKK' in icerik.lower() or 'siber' in icerik.lower() or 'hırsızlık' in icerik.lower():
            return 'Güvenlik/Veri Güvenliği'
        elif 'tarım' in icerik.lower() or 'sürdürülebilir' in icerik.lower() or 'sıfır atık' in icerik.lower() or 'sürdürülebilirlik' in icerik.lower() or 'geri dönüştürülebilir' in icerik.lower() or 'tamir' in icerik.lower() or 'karbon emisyonu' in icerik.lower() or 'çevre dostu' in icerik.lower() or 'engelli' in icerik.lower():
            return 'Tarımsal ve Toplumsal Sürdürülebilir Fayda'
        elif 'teknoloji' in icerik.lower() or 'inovasyon' in icerik.lower() or 'robotik' in icerik.lower() or 'metaverse' in icerik.lower() or 'yapay zeka' in icerik.lower() or 'NFT' in icerik.lower() or 'otonom' in icerik.lower() or 'sanal' in icerik.lower():
            return 'Teknoloji/İnovasyon'
        elif 'kazanç' in icerik.lower() or 'kar' in icerik.lower():
            return 'Finansal Üstünlük/Kaynak Yönetimi'
        elif 'müşteri' in icerik.lower() or 'tüketici' in icerik.lower() or 'rakip' in icerik.lower():
            return 'Müşteri ve Ticari Üstünlük'
    
    return konu  

df = pd.read_excel('data.xlsx')
df['konu'] = df.apply(siniflandir, axis=1)
df.to_excel('processed_data.xlsx', index=False)


def siniflandir(row):
    icerik = row['icerik']
    konu = row['konu']
    
    if pd.isnull(konu):  
        if 'lojistik' in icerik.lower() or 'taşımacılık' in icerik.lower() or 'kargo' in icerik.lower() or 'teslimat' in icerik.lower():
            return 'Lojistik'
        elif 'yatırım' in icerik.lower():
            return 'Yatırım'
        elif 'e-ticaret' in icerik.lower() or 'online alışveriş' in icerik.lower():
            return 'E-Ticaret'
        elif 'güvenlik' in icerik.lower() or 'veri güvenliği' in icerik.lower() or 'KVKK' in icerik.lower() or 'siber' in icerik.lower():
            return 'Güvenlik/Veri Güvenliği'
        elif 'tarım' in icerik.lower() or 'sürdürülebilir' in icerik.lower() or 'sıfır atık' in icerik.lower() or 'sürdürülebilirlik' in icerik.lower() or 'geri dönüştürülebilir' in icerik.lower() or 'tamir' in icerik.lower() or 'karbon emisyonu' in icerik.lower() or 'çevre dostu' in icerik.lower() or 'engelli' in icerik.lower():
            return 'Tarımsal ve Toplumsal Sürdürülebilir Fayda'
        elif 'teknoloji' in icerik.lower() or 'inovasyon' in icerik.lower() or 'robotik' in icerik.lower() or 'metaverse' in icerik.lower() or 'yapay zeka' in icerik.lower() or 'NFT' in icerik.lower() or 'otonom' in icerik.lower() or 'sanal' in icerik.lower() or 'dijital' in icerik.lower():
            return 'Teknoloji/İnovasyon'
        elif 'kazanç' in icerik.lower() or 'kar' in icerik.lower():
            return 'Finansal Üstünlük/Kaynak Yönetimi'
        elif 'müşteri' in icerik.lower() or 'tüketici' in icerik.lower() or 'rakip' in icerik.lower():
            return 'Müşteri ve Ticari Üstünlük'
        
    return konu 

df = pd.read_excel('data1.xlsx')
df['konu'] = df.apply(siniflandir, axis=1)
df.to_excel('processed_data1.xlsx', index=False)



# In[ ]:


import openpyxl
from nltk.tokenize import word_tokenize

def count_words_in_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    total_words = 0

    for column in sheet.iter_cols():
        for cell in column:
            if cell.value is not None:
                words = word_tokenize(str(cell.value))
                total_words += len(words)

    return total_words

file1_path = "processed_data.xlsx"
file2_path = "processed_data1.xlsx"

total_words_file1 = count_words_in_excel(file1_path)
total_words_file2 = count_words_in_excel(file2_path)

print("Toplam kelime sayısı (processed_data.xlsx):", total_words_file1)
print("Toplam kelime sayısı (processed_data1.xlsx):", total_words_file2)


# In[ ]:


import pandas as pd

df = pd.read_excel('processed_data.xlsx')
content = df.iloc[1, 1]  
total_words = len(content.split())

word_counts = pd.Series(content.split()).value_counts()
top_10_words = word_counts.head(10)

print("Toplam kelime sayısı:", total_words)
print("En sık kullanılan 10 kelime:")
print(top_10_words)



# In[ ]:


# X kelimesinden kaç tane vardır
filtered_df = df[df['icerik'].str.contains('perakende', case=False)]
count = len(filtered_df)
print("Toplam {} adet 'perakende' kelimesi bulundu.".format(count))


# In[ ]:


import pandas as pd
from collections import Counter

df = pd.read_excel('processed_data.xlsx')
all_words = ' '.join(df['icerik'].astype(str))
word_counts = Counter(all_words.split())
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(word, count)


# In[ ]:


import pandas as pd
import re
from collections import Counter

df = pd.read_excel('processed_data.xlsx')
text = ' '.join(df['icerik'].astype(str))
words = re.findall(r'\b\w+\b', text.lower())
word_counts = Counter(words)
word_variations = {}
for word in word_counts:
    base_word = re.sub(r'(ler|lar|in|nın|nin|den|dan|ci|ciler|cı|cılar|ecek|acak|cilerin|cıların|lerin|ların|li|lı|cilerden|cılardan|cilerinden|cılarından)$', '', word)
    if base_word not in word_variations:
        word_variations[base_word] = []
    word_variations[base_word].append(word)

word_total_counts = {}
for base_word, variations in word_variations.items():
    total_count = sum(word_counts[word] for word in variations)
    word_total_counts[base_word] = total_count

top_100_words = sorted(word_total_counts.items(), key=lambda x: x[1], reverse=True)[:100]

for word, count in top_100_words:
    if word in word_variations:
        variations = word_variations[word]
    else:
        variations = "No variations found"
    print(f'{word} ({count})-{variations}')


# In[ ]:


import pandas as pd
pd.set_option('display.max_colwidth', None)
df = pd.read_excel('processed_data.xlsx')
filtered_data = df[df['icerik'].str.contains('yemek|satış', case=False)]
print(filtered_data[['haber', 'icerik', 'bb_no']])


# In[ ]:


import pandas as pd
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import re
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def generate_word_counts(filename):
    df = pd.read_excel(filename)
    text = ' '.join(df['icerik'].astype(str))
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('turkish'))
    filtered_words = [word for word in words if word not in stop_words and len(word) > 1 and not word.isdigit()]

    # Lemmatization işlemi
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for word, tag in pos_tag(filtered_words):
        if tag.startswith('NN'):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos='n'))
        elif tag.startswith('VB'):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos='v'))
        elif tag.startswith('JJ'):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos='a'))
        elif tag.startswith('R'):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos='r'))
        else:
            lemmatized_words.append(lemmatizer.lemmatize(word))

    word_counts = Counter(lemmatized_words)

    word_variations = {}
    for word in word_counts:
        base_word = re.sub(r'(ler|lar|in|nın|nin|den|dan|ci|ciler|cı|cılar|ecek|acak|cilerin|cıların|leri|ları|lere|lara|lerin|ların|li|lı|cilerden|cılardan|cilerinden|cılarından)$', '', word)
        if base_word not in word_variations:
            word_variations[base_word] = []
        word_variations[base_word].append(word)

    word_total_counts = {}
    for base_word, variations in word_variations.items():
        total_count = sum(word_counts[word] for word in variations)
        word_total_counts[base_word] = total_count

    top_200_words = sorted(word_total_counts.items(), key=lambda x: x[1], reverse=True)[:200]

    output_data = []
    for word, count in top_200_words:
        if word in word_variations:
            variations = word_variations[word]
        else:
            variations = "No variations found"
        output_data.append({'Word': word, 'Count': count, 'Variations': variations})

    return pd.DataFrame(output_data)

def generate_output_image(output_df, filename):
    image_width = 800
    image_height = 1050
    image = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 10)  
    text_position = (10, 10) 
    text_color = (71, 60, 139)  
    line_height = 10 

    for i, row in output_df.iterrows():
        word = row['Word']
        count = row['Count']
        variations = row['Variations']

        line = f"Word: {word}, Count: {count}, Variations: {variations}"
        draw.text(text_position, line, font=font, fill=text_color)
        text_position = (text_position[0], text_position[1] + line_height)

    image.save(f'output_{filename}.png')
    print(f"Çıktı image formatında 'output_{filename}.png' olarak kaydedildi.")


output1 = generate_word_counts('processed_data.xlsx')
output1.to_excel('output_processed_data.xlsx', index=False)
generate_output_image(output1, 'processed_data')

output2 = generate_word_counts('processed_data1.xlsx')
output2.to_excel('output_processed_data1.xlsx', index=False)
generate_output_image(output2, 'data1')




# In[ ]:


import pandas as pd
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from PIL import Image, ImageDraw, ImageFont

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def generate_word_counts(filename):
    df = pd.read_excel(filename)
    text = ' '.join(df['icerik'].astype(str))
    text += ' '.join(df['haber'].astype(str)) 
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('turkish'))
    filtered_words = [word for word in words if word not in stop_words and len(word) > 1 and not word.isdigit()]

    # Lemmatization işlemi
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for word, tag in pos_tag(filtered_words):
        if tag.startswith('NN'):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos='n'))
        elif tag.startswith('VB'):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos='v'))
        elif tag.startswith('JJ'):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos='a'))
        elif tag.startswith('R'):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos='r'))
        else:
            lemmatized_words.append(lemmatizer.lemmatize(word))

    word_counts = Counter(lemmatized_words)

    word_variations = {}
    for word in word_counts:
        base_word = re.sub(r'(ler|lar|in|nın|nin|den|dan|ci|ciler|cı|cılar|ecek|acak|cilerin|cıların|leri|ları|lere|lara|lerin|ların|li|lı|cilerden|cılardan|cilerinden|cılarından)$', '', word)
        if base_word not in word_variations:
            word_variations[base_word] = []
        word_variations[base_word].append(word)

    word_total_counts = {}
    for base_word, variations in word_variations.items():
        total_count = sum(word_counts[word] for word in variations)
        word_total_counts[base_word] = total_count

    top_100_words = sorted(word_total_counts.items(), key=lambda x: x[1], reverse=True)[:100]

    output = ""
    for word, count in top_100_words:
        if word in word_variations:
            variations = word_variations[word]
        else:
            variations = "No variations found"
        output += f'{word} ({count}) - Varyasyonlar: {variations}\n'

    return output


# In[ ]:


import pandas as pd
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def generate_word_counts(filename):
    df = pd.read_excel(filename)
    text = ' '.join(df['icerik'].astype(str))
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('turkish'))
    filtered_words = [word for word in words if word not in stop_words and len(word) > 1 and not word.isdigit()]

    # Lemmatization işlemi
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for word, tag in nltk.pos_tag(filtered_words):
        if tag.startswith('NN'):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos='n'))
        elif tag.startswith('VB'):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos='v'))
        elif tag.startswith('JJ'):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos='a'))
        elif tag.startswith('R'):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos='r'))
        else:
            lemmatized_words.append(lemmatizer.lemmatize(word))

    word_counts = Counter(lemmatized_words)

    word_variations = {}
    for word in word_counts:
        base_word = re.sub(r'(ler|lar|in|nın|nin|den|dan|ci|ciler|cı|cılar|ecek|acak|cilerin|cıların|leri|ları|lere|lara|lerin|ların|li|lı|cilerden|cılardan|cilerinden|cılarından)$', '', word)
        if base_word not in word_variations:
            word_variations[base_word] = []
        word_variations[base_word].append(word)

    word_total_counts = {}
    for base_word, variations in word_variations.items():
        total_count = sum(word_counts[word] for word in variations)
        word_total_counts[base_word] = total_count

    top_100_words = sorted(word_total_counts.items(), key=lambda x: x[1], reverse=True)[:100]

    output = ""
    for word, count in top_100_words:
        if word in word_variations:
            variations = word_variations[word]
        else:
            variations = "No variations found"
        output += f'{word} ({count})-{variations}\n'

    return output

output1 = generate_word_counts('processed_data.xlsx')
print(output1)

output2 = generate_word_counts('processed_data1.xlsx')
print(output2)


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import PathPatch
from matplotlib.path import Path

df1 = pd.read_excel("processed_data.xlsx")
df2 = pd.read_excel("processed_data1.xlsx")
content1 = " ".join(df1["icerik"].astype(str))
content2 = " ".join(df2["icerik"].astype(str))
word_counts1 = {
    "müşteri": content1.count("müşteri"),
    "ürün": content1.count("ürün"),
    "şirket": content1.count("şirket") + content1.count("şirketi"),
    "marka": content1.count("marka"),
    "perakende": content1.count("perakende"),
    "mağaza": content1.count("mağaza"),
    "ödeme": content1.count("ödeme"),
    "alışveriş": content1.count("alışveriş"),
    "yatırım": content1.count("yatırım"),
    "hizmet": content1.count("hizmet"),
    "market": content1.count("market"),
    "satış": content1.count("satış"),
    "kart": content1.count("kart")
}
word_counts2 = {
    "müşteri": content2.count("müşteri"),
    "ürün": content2.count("ürün"),
    "şirket": content2.count("şirket") + content2.count("şirketi"),
    "marka": content2.count("marka"),
    "perakende": content2.count("perakende"),
    "mağaza": content2.count("mağaza"),
    "ödeme": content2.count("ödeme"),
    "alışveriş": content2.count("alışveriş"),
    "yatırım": content2.count("yatırım"),
    "hizmet": content2.count("hizmet"),
    "market": content2.count("market"),
    "satış": content2.count("satış"),
    "kart": content2.count("kart")
}
words = list(word_counts1.keys())
counts1 = list(word_counts1.values())
counts2 = list(word_counts2.values())
percentage_change = [(count1 - count2) / count2 * 100 for count1, count2 in zip(counts1, counts2)]

# Sort the words and counts in descending order
sorted_indices = sorted(range(len(counts1)), key=lambda k: counts1[k], reverse=True)
words = [words[i] for i in sorted_indices]
counts1 = [counts1[i] for i in sorted_indices]
counts2 = [counts2[i] for i in sorted_indices]
percentage_change = [percentage_change[i] for i in sorted_indices]

bar_width = 0.75
fig, ax = plt.subplots(figsize=(10, 6), facecolor="white")
ax.barh(words, counts1, bar_width, label="2022", linewidth=0.5, color="#ffc1c1", capstyle='round')
ax.barh(words, [-count for count in counts2], bar_width, label="2002", linewidth=0.5, color="#00CDCD",  capstyle='round')
ax.set_title("2002 ve 2022 Yıllarında En Sık Kullanılan Ortak Kelimeler")
for i, v in enumerate(percentage_change):
    ax.text(counts1[i] + 10, i, f"{v:.2f}%", color='black', fontweight='bold')
ax.legend()
ax.set_xticks(counts1)
ax.set_xticklabels(counts1)
ax.tick_params(axis='y', labelsize=14) 
ax.spines['right'].set_color('white')
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('processed_data.xlsx')
icerik = data['icerik']
kelimeler = ['sanal', 'dijital', 'teknoloji', 'teslimat', 'e-ticaret', 'online', 'çevrimiçi', 'sipariş', 'girişim', 'metaverse', 'uygulama', 'uygulaması']
kelime_sayilari = [icerik.str.contains(kelime, case=False).sum() for kelime in kelimeler]

online_index = kelimeler.index('online')
kelime_sayilari[online_index] += kelime_sayilari[kelimeler.index('çevrimiçi')]
kelime_sayilari.pop(kelimeler.index('çevrimiçi'))
kelimeler.pop(kelimeler.index('çevrimiçi'))

uygulama_index = kelimeler.index('uygulama')
kelime_sayilari[uygulama_index] += kelime_sayilari[kelimeler.index('uygulaması')]
kelime_sayilari.pop(kelimeler.index('uygulaması'))
kelimeler.pop(kelimeler.index('uygulaması'))

kelime_sayilari, kelimeler = zip(*sorted(zip(kelime_sayilari, kelimeler), reverse=True))
plt.figure(figsize=(7, 4))
plt.bar(kelimeler, kelime_sayilari, color='#ffc1c1', width=0.7)
plt.xticks(rotation=45, fontsize=12)
plt.title('2022 Yılında En Sık Kullanılan Kelimeler')
plt.tight_layout()
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('processed_data1.xlsx')
icerik = data['icerik']
kelimeler = ['avrupa', 'süpermarket', 'araştırma', 'araştırmaya', 'gıda', 'indirim', 'gida', 'aile', 'otomobil', 'çalışan', 'cep', 'ödeme']
kelime_sayilari = [icerik.str.contains(kelime, case=False).sum() for kelime in kelimeler]

araştırma_index = kelimeler.index('araştırma')
araştırmaya_index = kelimeler.index('araştırmaya')
kelime_sayilari[araştırma_index] += kelime_sayilari[araştırmaya_index]
del kelimeler[araştırmaya_index]
del kelime_sayilari[araştırmaya_index]

gida_index = kelimeler.index('gida')
gıda_index = kelimeler.index('gıda')
kelime_sayilari[gıda_index] += kelime_sayilari[gida_index]
del kelimeler[gida_index]
del kelime_sayilari[gida_index]
kelime_sayilari, kelimeler = zip(*sorted(zip(kelime_sayilari, kelimeler), reverse=True))

plt.figure(figsize=(7, 4)) 
plt.bar(kelimeler, kelime_sayilari, color='#00CDCD', width=0.7)
plt.xticks(rotation=45, fontsize=12)
plt.title('2002 Yılında En Sık Kullanılan Kelimeler')
plt.tight_layout()
plt.show()


# In[ ]:


# En çok haberi yapılan şirketlerin grafiği
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('processed_data.xlsx')
top_10_sirketler = df[df['sirket'] != 'Araştırma']['sirket'].value_counts().head(10)

# Sort 'sirket' column in descending order
top_10_sirketler = top_10_sirketler.sort_values(ascending=False)

plt.figure(figsize=(13, 2.5))
top_10_sirketler.plot(kind='bar', color='#ffc1c1')
plt.title('2022 Yılındaki Haberlerin Şirketlere Göre Dağılımı', fontsize=14)
plt.xticks(fontsize=13)
plt.yticks(fontsize=12)
plt.show()




import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('processed_data1.xlsx')
top_10_sirketler = df[(df['sirket'] != 'Araştırma') & (df['sirket'] != 'AB')]['sirket'].value_counts().head(10)

plt.figure(figsize=(13, 2.5))
top_10_sirketler.plot(kind='bar', color='#00CDCD')
plt.title('2002 Yılındaki Haberlerin Şirketlere Göre Dağılımı', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_excel('processed_data1.xlsx')
df2 = pd.read_excel('processed_data.xlsx')

filtered_df1 = df1[df1['sirket'] == 'Araştırma']
filtered_df2 = df2[df2['sirket'] == 'Araştırma']
konu_counts1 = filtered_df1['konu'].value_counts(normalize=True)
konu_counts2 = filtered_df2['konu'].value_counts(normalize=True)
common_topics = set(konu_counts1.index).intersection(konu_counts2.index)

konu_counts1_common = konu_counts1[konu_counts1.index.isin(common_topics)]
konu_counts2_common = konu_counts2[konu_counts2.index.isin(common_topics)]

fig, ax = plt.subplots(figsize=(8, 6))
width = 0.35
x = np.arange(len(common_topics))

bars1 = ax.bar(x, konu_counts1_common, width, label='processed_data1.xlsx', color='#00C5CD')
bars2 = ax.bar(x + width, konu_counts2_common, width, label='processed_data.xlsx', color='#FFAEB9')

ax.set_title('Araştırma Haberlerinin Konu Dağılımı')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(common_topics, rotation=90)
ax.legend(['2022', '2002'])

plt.tight_layout()
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('processed_data.xlsx')
keywords = ['yapay zeka', 'nft', 'metaverse', 'teknoloji', 'blockchain', 'fintech']
filtered_df = df[df['icerik'].str.contains('|'.join(keywords), case=False)]
filtered_df = filtered_df[~filtered_df['sirket'].str.contains('Araştırma', case=False)]  # Remove rows containing 'Araştırma' in the 'sirket' column
companies = filtered_df['sirket'].unique()

plt.figure(figsize=(4, 9))
colors = ['#FF8247', '#20B2AA', '#FFE4E1', '#B0E0E6', '#FFF68F', '#F08080', '#DC143C', '#458B74', '#DB7093', '#43CD80', '#FFEC8B', '#FF7256', '#4BA123', '#5F9EA0']

for i, company in enumerate(companies):
    company_data = filtered_df[filtered_df['sirket'] == company]
    color = colors[i % len(colors)]
    plt.plot(company_data['bb_no'], company_data['sirket'], marker='o', linestyle='', label=company, color=color, markersize=8)

plt.xlabel('Bilgi Bülteni')
plt.gca().set_facecolor('#F2F2F2')

plt.legend(ncol=1.5, bbox_to_anchor=(1, 1))
plt.show()

df2 = pd.read_excel('data1.xlsx')
filtered_df2 = df2[df2['icerik'].str.contains('|'.join(keywords), case=False)]
filtered_df2 = filtered_df2[~filtered_df2['sirket'].str.contains('Araştırma', case=False)] 
companies2 = filtered_df2['sirket'].unique()

plt.figure(figsize=(4, 4))

for i, company in enumerate(companies2):
    company_data2 = filtered_df2[filtered_df2['sirket'] == company]
    color = colors[i % len(colors)]
    plt.plot(company_data2['bb_no'], company_data2['sirket'], marker='o', linestyle='', label=company, color=color, markersize=8)

plt.xlabel('Bilgi Bülteni')
plt.gca().set_facecolor('#F2F2F2')

plt.legend(bbox_to_anchor=(1, 1))
plt.show()


# In[ ]:


#Her iki yılda da en fazla haberi yapılan şirketlerin grafikleri
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('processed_data.xlsx')
df2 = pd.read_excel('data1.xlsx')

companies = ['Tesco', 'Sainsbury', 'Walmart', 'Aldi']
colors = ['#79CDCD', '#F4A460', '#6CA6CD', '#FFDE66']

company_df = df[df['sirket'].isin(companies)]
company_df2 = df2[df2['sirket'].isin(companies)]

fig, axs = plt.subplots(2, 1, figsize=(8, 5))

for company, color in zip(companies, colors):
    company_data = company_df[company_df['sirket'] == company]
    company_data2 = company_df2[company_df2['sirket'] == company]
    axs[0].plot(company_data['bb_no'], company_data['sirket'], marker='o', linestyle='', label=company + ' - 2022', color=color)
    axs[1].plot(company_data2['bb_no'], company_data2['sirket'], marker='o', linestyle='', label=company + ' - 2002', color=color)

axs[0].set_title('2022 Yılı')
axs[1].set_title('2002 Yılı')

axs[0].legend(fontsize='small')
axs[1].legend(fontsize='small')

plt.tight_layout()
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('processed_data.xlsx')
top_10_words = df[df['sirket'] != 'Araştırma']['sirket'].value_counts().head(10).index.tolist()
word_counts = df[df['sirket'].isin(top_10_words)].groupby(['bb_no', 'sirket']).size().unstack().fillna(0)

plt.figure(figsize=(7, 2))  
for word in word_counts.columns:
    plt.scatter(word_counts.index, word_counts[word], label=word)

plt.xlabel('Bilgi Bülteni')
plt.ylabel('Haber Sayısı')
plt.title('Top 10 Şirketin Haber Sayısı')
plt.yticks(range(int(word_counts.values.min()), int(word_counts.values.max())+1))
plt.ylim(bottom=0.5)
plt.legend(ncol=2, bbox_to_anchor=(1, 1))
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_excel('processed_data1.xlsx')
df2 = pd.read_excel('processed_data.xlsx')

filtered_df1 = df1[df1['sirket'] == 'Araştırma']
filtered_df2 = df2[df2['sirket'] == 'Araştırma']

konu_counts1 = filtered_df1['konu'].value_counts()
konu_counts2 = filtered_df2['konu'].value_counts()
common_topics = set(konu_counts1.index).intersection(konu_counts2.index)

konu_counts1_common = konu_counts1[konu_counts1.index.isin(common_topics)]
konu_counts2_common = konu_counts2[konu_counts2.index.isin(common_topics)]

fig, ax = plt.subplots(figsize=(8, 6))
width = 0.35
x = np.arange(len(common_topics))

bars1 = ax.bar(x, konu_counts1_common, width, label='processed_data1.xlsx', color='#00C5CD')
bars2 = ax.bar(x + width, konu_counts2_common, width, label='processed_data.xlsx', color='#FFAEB9')

ax.set_xlabel('Konu')
ax.set_ylabel('Haber Sayısı')
ax.set_title('Araştırma Haberlerinin Konu Dağılımı')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(common_topics, rotation=90)
ax.legend(['2022', '2002'])

ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

plt.tight_layout()
plt.show()

