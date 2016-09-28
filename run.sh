DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Running in $DIR"

echo "::: Hugo server" && \
~/.go/bin/hugo server --buildDrafts --theme=freja -v
