DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Running in $DIR"

echo "::: Hugo server" && \
hugo server --buildDrafts --theme=freja -v
