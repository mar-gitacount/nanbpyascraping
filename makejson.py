import json
import os


# 新しいアイテムを追加する関数
def add_item(items, item_id, data):
    items[item_id] = data


# 既存のJSONファイルのパス
file_path = "items.json"

# 既存のJSONファイルが存在するか確認し、辞書として読み込む
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        items = json.load(file)
else:
    # 既存のJSONファイルが存在しない場合は空の辞書を作成する
    items = {}

# 新しいアイテムを追加
new_item_id = 300
new_item_data = {
    "decide": "決める",
    "understand": "理解する",
    "mean": "意味する。",
    "notice": "気づく",
    "waste": "無駄にする",
    "discover": "発見する",
    "wake": "目覚める",
    "invite": "招待する",
    "pick": "つまむ",
    "borrow": "借りる",
    "introduce": "導入、紹介する",
    "wonder": "不思議な",
    "receive": "受け取る",
    "reuse": "再利用する",
    "degree": "程度",
    "reduce": "減らす",
    "garbage": "ゴミ",
    "fuct": "事実",
    "luck": "運",
    "college": "大学",
    "university": "大学",
    "cafeteria": "食堂",
    "stadium": "競技場",
    "north": "北",
    "east": "東",
    "soush": "南",
    "west": "西",
    "trip": "移動、旅行",
    "way": "道、方法",
    "information": "情報",
    "holiday": "休日",
    "lake": "湖",
    "language": "言語",
    "pond": "池",
    "grade": "学年",
    "kind": "種類",
    "glacier": "氷河",
    "continent": "大陸",
    "effect": "結果",
    "shortage": "不足",
    "Celsius(セルシアス)": "摂氏",
    "Fahrenheit(ファーレンハイト)": "華氏",
    "releace": "解放する。",
    "fail": "失敗する",
    "hold": "持つ、開催する",
    "appear": "現れる",
    "raise": "あげる、育てる",
    "solve": "解決する",
    "act": "行う",
    "tour": "ツアー",
    "farm": "農場",
    "I'dont remember": "私は覚えていません",
    "You can't smoke here": "ここではタバコは吸えません",
}

add_item(items, new_item_id, new_item_data)

# 更新された辞書をJSONファイルに書き込む
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(items, file, indent=4, ensure_ascii=False)

print(f"新しいアイテムを {file_path} に追加しました。")
