DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Running in $DIR"

echo "::: SASS" && \
sass --watch themes/freja/static/assets/sass/freja.scss:themes/freja/static/assets/css/freja.css & \
echo "::: Hugo server" && \
~/.go/bin/hugo server --buildDrafts --theme=freja -v
