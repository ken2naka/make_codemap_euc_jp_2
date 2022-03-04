# make_codemap_euc_jp_2
Generate codemap in EUC character code.

目的：
- euc_jp の2バイトコード（全角漢字）のエリアマップの漢字部分を標準出力に出力（utf-8）する。
- 同時に "euc_code_table2.text" というファイルにも出力する。
- その際、「JIS X 0208 (1990) to Unicode 漢字コード表」に
- 存在しないコード部分は 0xfff0efbfbd （'�'）で埋める。

備考：
- xyzzy やサクラエディタでは 0xfff0efbfbd （'�'）は正しく表示されず、別の文字で置き換えられている。
- メモ帳では正しく表示される。vs code のターミナルでも正しく表示される。
- unicode の対応状況がこれらのソフトでは異なるためか？
