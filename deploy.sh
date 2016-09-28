DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Running in $DIR"

echo "::: Building site" && \
~/.go/bin/hugo --theme=freja -v && \
echo "::: Site built" && \
echo "::: Remove old social cards" && \
rm -rf $DIR/public/assets/img/cards && \
echo "::: Rebuild social cards" && \
python $DIR/utils.py --public=$DIR/public --font=/Users/dmitriid/Downloads/Merriweather/Merriweather-Regular.ttf
echo "::: Done"




