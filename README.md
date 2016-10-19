# What

Code and content for [http://dmitriid.com](http://dmitriid.com).

Uses [Hugo static site generator](https://gohugo.io) and a custom theme

Content is [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). The theme is [MIT](https://opensource.org/licenses/MIT).

# How

You can use the theme to your liking. See `themes/freja`.

- Run `hugo server --theme=freja --buildDrafts`
- Open [http://localhost:1313/blog/beta/all-elements/](http://localhost:1313/blog/beta/all-elements/) to see all elements in action and how to use them
- See `themes/freja/shortcodes` for available shortcodes
- See `config.toml.example` to see how to config your site

## Facebook graph and Twitter Cards

Run `utils.py` to automatically generate images required by FB OpenGraph and Twitter Cards. See `deploy.sh` to see how the script needs to be invoked.

The script will use the `banner` you specify in page front matter or an empty image with text and your transparent `static/assets/img/logo.png`.

