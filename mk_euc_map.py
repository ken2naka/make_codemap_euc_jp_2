
# -*- coding: utf-8 -*-
"""

更新：
  2019-02-01 type annotation を追加。pycodestyle で引っかかった箇所を修正。
  2018-09-24
作成：2018-09-13
目的：
　　・euc_jp の2バイトコード（全角漢字）のエリアマップの漢字部分
　　　を "euc_code_table.txt" に出力（utf-8）する。
　　・その際、「JIS X 0208 (1990) to Unicode 漢字コード表」に
　　　存在しないコード部分は 0xfff0efbfbd （'�'）で埋める。
備考：xyzzy やサクラエディタでは 0xfff0efbfbd （'�'）は正しく
　　　表示されず、別の文字で置き換えられている。メモ帳では正しく
　　　表示される。vs code のターミナルでも正しく表示される。unicode
　　　の対応状況がこれらのソフトでは異なるためか？

入力ファイル：なし
引数：なし
対象：python3
実行方法：python mk_euc_map.py

参考：
　　・文字コード表 日本語EUC(euc-jp) http://charset.7jp.net/euc.html
"""
# ------------------

# import os
# import binascii
import sys
import codecs
import io

# type annotation
from typing import IO

# 以下の行が無いと git bash で実行した時、unicodeEncodeError となる。それを防止する。
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# --------------------
# main()
# --------------------
def main():
    import struct

    out_path: str = "euc_code_table2.text"
    fout: IO[str] = codecs.open(out_path, 'w', 'utf-8')

    # 横のアドレス：下位8bit
    fout.write("  |")
    print("  |", end="")
    for n in range(0xa1, 0xff):
        print("%02x" % n, end="")
        fout.write("%02x" % n)
    print('\n', end="")

    # 横線
    fout.write("\n--|")
    for n in range(0xa1, 0xff):
        fout.write("--")

    for up in range(0xb0, 0xf5):
        for down in range(0xa1, 0xff):
            if (down == 0xa1):
                print("\n%02x|" % up, end="")
                fout.write("\n%02x|" % up)
            if ((up >= 0xf4) and (down >= 0xa7)):
                print("�", end="")
                fout.write("�")
                continue
            elif ((up == 0xcf) and ((down >= 0xd4) and (down <= 0xfe))):
                print("�", end="")
                fout.write("�")
                continue
            else:
                val = up * 256 + down
                chars = struct.pack('!H', val)
                print(chars.decode('euc_jp'), end="")
                fout.write(chars.decode('euc_jp'))

    fout.close()


# --------------------
if __name__ == '__main__':
    main()
