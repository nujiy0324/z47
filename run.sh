echo "install python package";
pip3 install -r ./info/requirements.txt;
mkdir /result;

echo "start running python"
python -u ./code/crawler.py