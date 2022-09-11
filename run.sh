echo "install python package";
pip install -r ./info/requirements.txt;
mkdir /result;

echo "start running python"
python -u ./code/crawler.py