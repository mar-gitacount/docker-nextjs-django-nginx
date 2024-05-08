from selenium import webdriver
import os
import json
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime
from selenium import webdriver
import re
import math
from datetime import datetime
from openpyxl import Workbook, load_workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import glob
import csv


def model_validete_imput(text):
    models = [
        "デイトジャスト",
        "オイスター",
        "コスモグラフ",
        "シードゥエラー",
        "エクスプローラー",
        "GMTマスター",
        "GMTマスターII",
        "サブマリーナー",
        "ヨットマスター",
        "スカイドゥエラー",
        "エクスプローラーII",
        "エアキング",
    ]
    print("関数内のテキスト", text)
    pattern = r"\b\s+(\S+)\s+\b"
    # beltpattern = r"\[(.*?)\]|\((.*?)\)"
    beltpattern = r"\[(?:.*?)\]|\((?:.*?)\)"

    # ベルトと文字盤を抽出する。
    beltmatches = re.findall(beltpattern, text)
    # モデル名を抽出する。
    model = re.sub(beltpattern, "", text)
    print("モデル名", model)
    # [],()を正規表現で抽出する。
    items = {"model": model, "beltmatches": beltmatches}
    return items

def main():
    # 現在の日付を取得 
    today_date = datetime.now().date()
    # 現在のディレクトリを格納する。
    path = os.getcwd()
    rowdata = []
    insertdata = []
    # CSVファイル作成
    # ファイルを取得し、利用おわったら済みフォルダに移動する。
    ref_pattern = r"\b(?:\d{4,6})(?:[a-zA-Z]+)?\s\b"
    gram_pattern = r"\b\d+.*?g\b"
    box_pattern = r"\b(BOX|ｹｰｽ)+\b"
    box_pattern = r"(BOX|ｹｰｽ|コマ)+"

    # ref_pattern = r"\b(?:\d{4,6})(?:[a-zA-Z]+)*\s\b"

    # カレントディレクトリのCSVファイルを検索
    csv_files = glob.glob('csv/*.csv')


   # 検出されたCSVファイルのリストを表示
    for file_name in csv_files:
    #    print(file_name)
       use_csvfile = os.path.join(path,file_name)
           
    # 了するcsvfile最後はdoneに移動する。
  

    with open(use_csvfile, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            print(row)  
            filtered_items = [item for item in row if item not in [None, '', ' ']]
            rowdata.append(row)
        # print(rowdata)
        for items in rowdata:
            itemdatas = []
        
            for item in items:
               if item is None or item == '' or item == ' ':
                  itemdatas.append(item)
                  continue
                
               refmatches = re.findall(ref_pattern,item,flags=re.UNICODE)
               boxmatches = re.findall(box_pattern,item,flags=re.UNICODE)
               grammatches = re.findall(gram_pattern,item,flags=re.UNICODE)

   
               
               if boxmatches:
                   #    いらないやつ
                   itemdatas = []
                   break
               
                   
                
               if refmatches:
                  parts = item.split()
                  ref = parts[0]
                  itemdatas.append(ref)
                  # 他のデータ
                  another_datil = item.replace(ref,"")
                #   print(ref)
                # itemdatas.append("")
                  itemdatas.append(another_datil)
               else:
                #  itemdatas.append("")
                 itemdatas.append(item)
                # print(ref)
            # print(itemdatas)

            if itemdatas:
                insertdata.append(itemdatas)




        # ファイル名をコピーする。
        if not os.path.exists(use_csvfile):
            print(f"{use_csvfile}ある")
        else:
            print(f"{use_csvfile}はない。作る")
            # 元のファイルを取得する。
            make_csv_filename = os.path.basename(use_csvfile)
            # csvファイル作成する。
            with open(make_csv_filename,mode='w',newline='') as newfile:
                writer = csv.writer(newfile)
                writer.writerow(['会場', '開催日', '箱番号','番号','レーン名','品名','ブランド名','枠','脇石','重量','品番','','ランク','スタート価格','予想時刻','オークション結果','落札価格'])
                writer.writerows(insertdata)

        




# mainメソッドを呼び出す
if __name__ == "__main__":
    main()