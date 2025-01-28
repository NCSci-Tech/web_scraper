echo "[*]#### This bash file is for the proprietary"
echo "[*]#### setup and use of my web scraper tool"
echo "[*]#### on ubuntu using a python environment."

apt install python3.12-venv

python3 -m venv myenv

source myenv/bin/activate

pip install beautifulsoup4
pip install requests

echo "[*]#### Setup Complete..."
echo "[*]#### Starting program..."

python3 scraper.py

find / -type d -name "myenv" -exec rm -rf {} +