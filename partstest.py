import os
import json
import csv
from bs4 import BeautifulSoup
import requests
import re
import sys
from openpyxl import Workbook, load_workbook
from datetime import datetime

# 新しいCSVファイルのパス
csv_file_path = "新しいファイル.csv"
current_directory = os.getcwd()
html_relative_path = "load.html"
urlcsv_relative_path = "url.csv"
# HTMLファイルの絶対パスを生成
html_file_path = os.path.join(current_directory, html_relative_path)
item_name = {0: ""}
csv_input_data = []
# CHFの正規表現パターン
chf_pattern = re.compile(r"\bCHF\b")
testcheck_pattern = re.compile(r"\b未使用品\b")
brbproducts_list_array = []
brbproducts_list_array_index = 0
brbproduct = ""
single_rowdata = []

# !エクセルデータ設定
# エクセルのヘッダ－データ
data = ["製品名", "リファレンスNO", "最高価格", "最安価格", "ブレスレット", "その他"]
# ファイル名に日付を組み込む
# 現在の日付を取得
today_date = datetime.now().strftime("%Y%m%d")
file_name = f"output_{today_date}.xlsx"
if not os.path.exists(file_name):
    # Excelブックの作成
    wb = Workbook()
    ws = wb.active
    # ヘッダー行を追加
    ws.append(["製品名", "リファレンスNO", "未使用品", "中古品"])
else:
    # ファイルが存在する場合は既存のファイルを読み込み
    wb = load_workbook(file_name)
    ws = wb.active

# !エクセルデータ設定ここまで

with open(html_file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
    brbproducts_list = soup.find_all(class_="MarketSearch2_itemDiv")  # クラス名を修正
    brbproducts_list = soup.find_all(class_="MarketSearch2_item")  # クラス名を修正

    page_array_index = 0
    index = 0
    for item in brbproducts_list:
        # テキストを走査
        input_text = item.text
        text = input_text.splitlines()
        row_item = []
        index += 1

        text = list(filter(None, text))
        # print(text)
        # print("---------------")
        for item in text:
            print(item)
            row_item.append(item)
            # !以下でエクセルファイルに入稿する。
            # ws.append(itemmatches)
            #     if not item.strip():
            #         continue
            #     else:
            #         brbproduct += brbproduct + "\n" + item

            chf_match = testcheck_pattern.search(item)
            if chf_match:
                #             brbproducts_list_array.append(brbproduct)
                #             print(brbproducts_list_array[brbproducts_list_array_index])
                #             brbproducts_list_array_index += 1
                #             brbproduct = ""
                print("----------------")
        ws.append(row_item)
        print("-------ここでエクセルファイルに入稿する---------")

wb.save(file_name)
