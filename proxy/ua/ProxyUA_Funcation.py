# 从文件中获取UA以List返回,默认返回前20个
import sqlite3


def Enca_get_proxyUA(start_num=0, end_number=20):
    db = sqlite3.connect("./useragents.db")
    cursor = db.cursor().execute(f'select * from uas limit {start_num},{end_number}').fetchall()
    for ua in cursor:
        result_ualist = []
        for this_ua in ua[1:]:
            result_ualist.append(this_ua)
        # print('/'.join(result_ualist))
        return result_ualist


print(140 * 0.3)
