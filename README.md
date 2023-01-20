# sk_practice
## Overview
このパッケージは機械学習による機能をまとめている

## Description
### このパッケージの機能

- 名前からの性別判断
 

## Usage

|Communication|Name|Type|Request|Result|
| :---: | :---: | :---: | :---: | :---: |
| Service | /gender_jg | [StringToString](https://github.com/KIT-Happy-Robot/happymimi_voice/blob/master/happymimi_voice_msgs/srv/StringToString.srv) | string型： `req` | string型： `result_date` , bool型: `result` |

## サーバの起動

`$ rosrun sk_practice server_gender_jg.py `
（make_list.py から import して使っているので server_gender_jg.py と同じところに置いとかないとnot fond errorになると思う）

## クライアントのプログラム例
```
  4 import rospy
  5 from happymimi_voice_msgs.srv import StringToString
  6 # from happymimi_voice_msgs.srv import StringToStringResponse
  7 
  8 req = "Liam"                                                                
  9 ge = rospy.ServiceProxy('/gender_jg',StringToString)
 10 x = ge(req)
 11 if x.result:
 12     print(x.result_data)
```

## 使っている名前のデータ
- [yob2021.txt](https://www.ssa.gov/oact/babynames/limits.html)

