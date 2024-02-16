import random
import time
import json

# 連想配列の定義
# items = {
#     "decide": "決める",
#     "understand": "理解する",
#     "mean": "意味する。",
#     "notice": "気づく",
#     "waste": "無駄にする",
#     "discover": "発見する",
#     "wake": "目覚める",
#     "invite": "招待する",
#     "pick": "つまむ",
#     "borrow": "借りる",
#     "introduce": "導入、紹介する",
#     "wonder": "不思議な",
#     "receive": "受け取る",
#     "reuse": "再利用する",
#     "degree": "程度",
#     "reduce": "減らす",
#     "garbage": "ゴミ",
#     "fuct": "事実",
#     "luck": "運",
#     "college": "大学",
#     "university": "大学",
#     "cafeteria": "食堂",
#     "stadium": "競技場",
#     "north": "北",
#     "east": "東",
#     "soush": "南",
#     "west": "西",
#     "trip": "移動、旅行",
#     "way": "道、方法",
#     "information": "情報",
#     "holiday": "休日",
#     "lake": "湖",
#     "language": "言語",
#     "pond": "池",
#     "grade": "学年",
#     "kind": "種類",
#     "glacier": "氷河",
#     "continent": "大陸",
#     "effect": "結果",
#     "shortage": "不足",
#     "Celsius(セルシアス)": "摂氏",
#     "Fahrenheit(ファーレンハイト)": "華氏",
#     "releace": "解放する。",
#     "fail": "失敗する",
#     "hold": "持つ、開催する",
#     "appear": "現れる",
#     "raise": "あげる、育てる",
#     "solve": "解決する",
#     "act": "行う",
#     "tour": "ツアー",
#     "farm": "農場",
#     "I'dont remember": "私は覚えていません",
#     "You can't smoke here": "ここではタバコは吸えません",
# }


def auto_extract_random():
    # JSONファイルのパス
    file_path = "items.json"
    # JSONファイルを読み込む
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    # 300部分の辞書を取得する
    dictionary_300 = data["300"]
    # 辞書内の各キーと値に対してループ処理を行う
    for key, value in dictionary_300.items():
        print(f"キー: {key}, 値: {value}")

    # 辞書のコピーを作成してイテレーションする
    items_copy = dict(dictionary_300)
    for key, value in items_copy.items():
        print("連想配列内の要素をランダムに抽出中...")
        time.sleep(2)  # 2秒待機（仮の処理として）
        # ランダムに要素を選択
        random_key, random_value = random.choice(list(dictionary_300.items()))
        print("抽出が完了しました。エンターキーを押して結果を表示します。")
        print(f"{random_key}: はなに")
        input()  # エンターキーを待機
        print(f"選択された要素: {random_key}: {random_value}")

        # 選択された要素を元の辞書から削除
        del dictionary_300[random_key]


# プログラムの実行
auto_extract_random()
