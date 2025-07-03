# openjtalk-user-dict

### このリポジトリについて

openjtalk用の辞書置き場です


詳しい情報については[wiki](https://github.com/WariHima/openjtalk-user-dict/wiki)をお読みください。

## アピールポイント  
  
世界最大規模の日本語オブジェクト（複合名詞）単位形態素解析辞書  
日本語最大規模のアクセントつき辞書  
日本語最大規模の形態素解析機向け医療用語辞書  
日本語最大規模の形態素解析機向け人名辞書  

#### src以下フォルダの説明  
csv_1gram 漢字1gram（1文字）の辞書  
csv_2gram 漢字2gram（2文字）の辞書  
csv_3gram 漢字3gram（3文字）の辞書  
csv_4_5gram 漢字4-5gram（4-5文字）の辞書  
csv_ngram 漢字6-ngram（6-n文字）の辞書  
csv_hiragana すべてひらがなでできた単語の辞書  
csv_katakana すべてカタカナでできた単語の辞書  
csv_eigo アルファベットのみでできた単語の辞書  
csv_name 人名辞書  
csv_medical 医療用辞書  
csv_game ゲーム用語辞書  
csv_history　歴史用語に関連する辞書  

#### 使い方
```
# 仮想環境の作成
task run install

# pyopenjtalk ユーザー辞書をビルド
task run build_dictionary
```
