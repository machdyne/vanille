# first do: pip install -r requirements.txt
python3 csvtocsv.py > pinout.csv
kipart -b pinout.csv -o ecp5-12-tg144.lib --overwrite
