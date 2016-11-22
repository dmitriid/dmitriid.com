+++
date = "2016-10-19T13:38:57+02:00"
Lastmod = "2016-11-16T13:38:57+02:00"
draft = false
title = "Javascript Tools: A Story in Disgrace"
summary = "We're told: move fast and break things. For once, just for once, I would like to stop breaking things and stick to something that works."
tags = ["javascript", "dx"]
+++

# Why am I even writing about this?

## Building JavaScript apps is overly complex right now

Among other things [The State of JS 2016](http://stateofjs.com/2016/opinions/) asked developers if they disagreed (1), were neutral (3), or agreed (5) with the following statement: *Building JavaScript apps is overly complex right now*

<figure class="fullimage"><div>
<svg viewBox="0 0 1097 400" version="1.1"><g class="recharts-layer recharts-x-axis"><g class="recharts-layer recharts-cartesian-axis"><line class="recharts-cartesian-axis-line" width="1097" height="30" x="0" y="370" stroke="#5ec6cc" fill="none" x1="0" y1="370" x2="1097" y2="370"></line><g class="recharts-cartesian-axis-ticks"><g class="recharts-cartesian-axis-tick"><text dy="15" text-anchor="middle" width="1097" height="30" x="109.7" y="376" stroke="none" fill="#666" class="recharts-cartesian-axis-tick-value">1</text></g><g class="recharts-cartesian-axis-tick"><text dy="15" text-anchor="middle" width="1097" height="30" x="329.1" y="376" stroke="none" fill="#666" class="recharts-cartesian-axis-tick-value">2</text></g><g class="recharts-cartesian-axis-tick"><text dy="15" text-anchor="middle" width="1097" height="30" x="548.5" y="376" stroke="none" fill="#666" class="recharts-cartesian-axis-tick-value">3</text></g><g class="recharts-cartesian-axis-tick"><text dy="15" text-anchor="middle" width="1097" height="30" x="767.9000000000001" y="376" stroke="none" fill="#666" class="recharts-cartesian-axis-tick-value">4</text></g><g class="recharts-cartesian-axis-tick"><text dy="15" text-anchor="middle" width="1097" height="30" x="987.3000000000001" y="376" stroke="none" fill="#666" class="recharts-cartesian-axis-tick-value">5</text></g></g></g></g><g class="recharts-layer recharts-bar-graphical"><g class="recharts-layer recharts-bar"><g class="recharts-layer recharts-bar-rectangles"><g style="transform-origin: 50% 100%;"><path fill="url(#cfwue)" x="65.82" y="317.3379714390333" width="87" height="52.66202856096669" stroke="none" stroke-width="1" stroke-dasharray="none" class="recharts-rectangle recharts-bar-rectangle" d="M 65.82,317.3379714390333 h 87 v 52.66202856096669 h -87 Z"></path></g><g style="transform-origin: 50% 100%;"><path fill="url(#cfwue)" x="285.22" y="249.36287074331747" width="87" height="120.63712925668253" stroke="none" stroke-width="1" stroke-dasharray="none" class="recharts-rectangle recharts-bar-rectangle" d="M 285.22,249.36287074331747 h 87 v 120.63712925668253 h -87 Z"></path></g><g style="transform-origin: 50% 100%;"><path fill="url(#cfwue)" x="504.62" y="62.61808861222994" width="87" height="307.38191138777006" stroke="none" stroke-width="1" stroke-dasharray="none" class="recharts-rectangle recharts-bar-rectangle" d="M 504.62,62.61808861222994 h 87 v 307.38191138777006 h -87 Z"></path></g><g style="transform-origin: 50% 100%;"><path fill="url(#cfwue)" x="724.02" y="41.827169534968846" width="87" height="328.17283046503115" stroke="none" stroke-width="1" stroke-dasharray="none" class="recharts-rectangle recharts-bar-rectangle" d="M 724.02,41.827169534968846 h 87 v 328.17283046503115 h -87 Z"></path></g><g style="transform-origin: 50% 100%;"><path fill="url(#cfwue)" x="943.4200000000001" y="30" width="87" height="340" stroke="none" stroke-width="1" stroke-dasharray="none" class="recharts-rectangle recharts-bar-rectangle" d="M 943.4200000000001,30 h 87 v 340 h -87 Z"></path></g></g><g class="recharts-layer recharts-bar-rectangle-labels"><g class="recharts-layer recharts-bar-labels"><text class="label" x="109.32" y="312.3379714390333" text-anchor="middle">5%</text><text class="label" x="328.72" y="244.36287074331747" text-anchor="middle">11%</text><text class="label" x="548.12" y="57.61808861222994" text-anchor="middle">27%</text><text class="label" x="767.52" y="36.827169534968846" text-anchor="middle">29%</text><text class="label" x="986.9200000000001" y="25" text-anchor="middle">30%</text></g></g></g></g><defs><pattern id="cfwue" patternUnits="userSpaceOnUse" width="10" height="10"><path d="M 0,10 l 10,-10 M -2.5,2.5 l 5,-5 M 7.5,12.5 l 5,-5" stroke-width="6" shape-rendering="auto" stroke="#5ec6cc" stroke-linecap="square"></path></pattern></defs></svg></div></figure>

**A full 59% of developers agree that <em>Building JavaScript apps is overly complex right now</em>. Only 16% disagree.**

Javascript fatigue is real, no matter how hard some people try to shrug it off (see [this](http://www.2ality.com/2016/02/js-fatigue-fatigue.html) for an example).

We're told: move fast and break things. For once, just for once, I would like to stop breaking things and stick to something that works. Half of the issues here is something I've encountered in the _past two weeks alone_, when trying to create a project from scratch.

## Developer Experience

Developer Experience is not a lost art. It's an art that has never been discovered. It was briefly discussed a few years ago and then forgotten. These days if you ever hear it mentioned, it's usually in the context of APIs.

However (emphasis mine):

{{% quote link="https://blog.opsee.com/let-s-talk-about-developer-experience-dx-design-f62ee4c2ee05#.n2x4gr3cn" author="Steve Boak" %}}As software consumes the world around us, good design in our tools is a growing competitive advantage

 Our tools shape our work, and great tools change the shape of our industry.
 
 **We talk a lot about the importance of a strong engineering team, but not enough about the design of our tools and the impact it has on the quality of the products we build**. We should be talking about DX more, and it’s not enough to talk about UX alone.
 {{%/ quote %}}


Javascript tools are quite literally death by a thousand cuts. The whole experience of working with and building for Javascript is, at the very least, an excercise in frustration. The landscape is utterly hostile to developers. With experience you learn to navigate it, somewhat safely. Is it an experience you need, though?

## Falsehoods programmers believe about Javascript tools

1. Tools work when you run them
1. Tools can be configured
14. In JSON
15. In Javascript
16. Can be pointed to different config file
17. Don't use hidden/special files like `.something.rc`
1. Tools fail if their config is incorrect
2. Tools warn you about invalid values in configs
3. Tools ignore invalid values in config
4. Tools use defaults instead of invalid values in config
5. Tools **don't** ignore valid values in config
6. Well, at least tools report non-config errors
7. At least fatal errors?
8. Tools propagate errors from their plugins or sub-tools
9. At least fatal errors? I asked that one already, didn't I?
10. You can tell if an error originated in the tool, in a plugin or in a sub-tool
11. At least, errors are clearly stated on screen/in logs
12. At least, with reasonable and relevant information
18. Tools can be invoked from command line
19. Tools can be run on a list of files
20. With glob patterns
21. Minor versions of tools, or their plugins, or their sub-parts keep backwards compatibility
22. Tools fail if none of their requirements are satisfied
23. Tools fail if some of their requirements are not satisfied
24. Errors or warnings if this happens
25. There is only one way to do things
26. There is more than one way to do things
27. These many ways lead to the same result
28. Your tool will be relevant 5 years from now
29. Ok, a year from now

So, let's talk tools.


# npm

`npm` is the ubiquitous javascript tool. You may still run into bower occasionally, but that battle seems to [have been lost](https://www.quora.com/Why-use-Bower-when-there-is-npm/answer/Mattias-Petter-Johansson).

`npm` is:

- a package manager
- a dependency tracker
- a build tool (node.js's `make`, if you will)
- a task runner

It probably does other tasks, but these are the most important ones. It does its job quite well, and I cannot recommend [this post](https://www.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/) highly enough. Still, there are gotchas.

## Run whatever I think you want, not what you want

This is relatively a minor WTF, but it's [there](https://docs.npmjs.com/misc/config) nonetheless:

{{% quote %}}
If the specified configuration param resolves unambiguously to a known configuration parameter, then it is expanded to that configuration parameter. For example:

```
npm ls --par
# same as:
npm ls --parseable
```

{{%/ quote %}}

In the example above `--par` is an *invalid* parameter. `npm` will not silently ignore it (which would be bad). `npm` will silently expand it to whatever parameter or combination of parameters it fuzzy matched.

`npm` has been notoriously bad at detecting actual errors. For example, until version 3.x (!) it would not fail if its configuration file [was](https://github.com/npm/npm/issues/12155) [invalid](https://github.com/npm/npm/pull/12406).

## Depend on whatever I you think you want, not what you want

Let's consider `npm install --save`. This installs a dependency and adds it to the dependency list in your project's `package.json`. And by *saving* I mean *"take the list of dependencies, sort it alphabetically, and write it back to disk"*.

This would not be a problem, save for this:

{{% quote author="Yarn: A new package manager for JavaScript" link="https://code.facebook.com/posts/1840075619545360" %}}
The `npm` client installs dependencies into the `node_modules` directory non-deterministically. This means that based on the order dependencies are installed, the structure of a `node_modules` directory could be different from one person to another. These differences can cause “works on my machine” bugs that take a long time to hunt down.
{{%/ quote %}}

Brilliant, isn't it?

## Remove all the things

Well, you know/remember this one: [Rage-quit: Coder unpublished 17 lines of JavaScript and “broke the Internet”](http://arstechnica.com/information-technology/2016/03/rage-quit-coder-unpublished-17-lines-of-javascript-and-broke-the-internet/)

Many were quick to attribute the problem to the horrible programmer culture of JavaScript, where people have [forgotten how to program](http://www.haneycodes.net/npm-left-pad-have-we-forgotten-how-to-program/). It's not the case. JavaScript community has whole-heartedly adopted Unix's philosophy of "one package has to do one thing, and do it well", but may have taken it to extremes.

The problem, or rather problems (plural) are all laid out here: https://github.com/npm/npm/issues/12045, so I'm not going to re-iterate.

npm and *npm's registry* are essential to developers and to developer experience. The way some/many of arising issues are handled by npm's organisation are clearly detrimental to developer experience.

## Your package name doesn't matter. Until it matters

First, [this story](https://medium.com/@3rdeden/an-attack-on-publisher-freedom-271013ff33c5#.jotoz8m8w).

{{% quote author="Arnout Kazemier" link="https://medium.com/@3rdeden/an-attack-on-publisher-freedom-271013ff33c5#.jotoz8m8w" %}}
So after a search for various of keywords I found out that the module name npmjs was still available in the registry. In the four years that the registry existed nobody took the effort in registering it. This module was and is a perfect fit for my module.

On the 22th I received an email from Isaac, the CEO of npm Inc (which recently raised more than 2M in funding for his company) and creator of npm with a question:

> Can you please choose another name for this module? It’s extremely confusing. Thanks.

...

It didn’t even matter what how right or wrong I was for using npmjs as a module name Isaac had clearly already decided to destroy the module as he stated there wasn’t any negotiation and that it would be deleted no matter what.
{{%/ quote %}}

Sounds bad, doesn't it? Ok, what about [this story](http://status.npmjs.org/incidents/dw8cr1lwxkcr) then (emphasis mine)?

{{% quote author="Incident Report for npm, Inc." link="http://status.npmjs.org/incidents/dw8cr1lwxkcr" %}}
For a few minutes today the package "fs" was unpublished from the registry in response to a user report that it was spam. It has been restored. 

More detail: the "fs" package is a non-functional package. It simply logs the word "I am fs" and exits. There is no reason it should be included in any modules. **However, something like 1000 packages *do* mistakenly depend on "fs", probably because they were trying to use a built-in node module called "fs".**
{{%/ quote %}}

1. Should you even allow publishing a module that has the same name as an intenal one?
2. If `npmjs` is confusing, how is `fs` *not* confusing?
3. If thousands of packages depend on it, how can you remove it considering the SNAFU you had just several months prior?

## Can we even trust our core tools?

This all leads to rather horrible questions:

- Can we trust our core tools?
- What are the guarantees that anything we install and run installs and runs in the intended way?

Also, [see the rationale](https://code.facebook.com/posts/1840075619545360) behind [Yarn](https://yarnpkg.com), Facebook's alternative package manager.

# Build tools

The number of build tools (subsets and supersets of Makefiles and npm, or combination of all of the above) for Javascript is simply staggering.

Grunt, Gulp, Broccoli, Brunch, Jake, Mimosa, Webpack, Bower...

They are all broken in more ways than one. Let me just quote from my own experience (read the whole article for more than just this one snippet):

{{% quote author="Javascript: Fatigue vs. Stockholm syndrome" link="https://medium.com/@dmitriid/javascript-fatigue-vs-stockholm-syndrome-631d4f524008" %}}
Let’s step back for a second, and consider:

- Grunt does not transform code, it’s a “task runner”
The task it runs is called *browserify*
- Well, the problem with the browserify *task* is that the *task* runner cannot run it. It needs a plugin called *grunt-browserify* to do that
- Oh, and browserify has to run babel on the source code before it can do anything with it.
- And the problem is that browserify cannot run babel directly. It needs *babelify* to work

All in all the whole toolchain to produce a Javascript file is *grunt -> grunt-browserify -> browserify -> babelify -> babel*. And someone in that chain decides that babel missing all of its specified plugins *is not a reason to throw an error, stop and report*.
{{%/ quote %}}

Are these problems fixed now? I don't know. I no longer even care if they are fixed or not. I got myself new shiny better toys to play with. Or did I?

# webpack

[Webpack](https://webpack.github.io) is almost the latest and greatest in a web-developer's life (there's a more latest now, called [Rollup](http://rollupjs.org/)).

On the surface it does the following: take all the modules that your app has, figure out dependencies between them, bundle them up in a single file that you can serve to your website.

All webpack understands is ES5 and some common module structures: CommonJS, AMD etc. It can invoke so-called loaders  whose job is to take a file and produce an ES5 output which Webpack will then take and bundle.

As a result, you can somewhat easily depend on anything: modules written in ES6, or in TypeScript, or in Coffeescript, or... You can even depend on CSS files or PNGs. If there's a loader for that type of file, Webpack can bundle it.

## Boilerplates

Also as a result, Webpack's configuration is *inane*. And I don't say it lightly.

Search github for "boilerplate", and you will come away with easily hundreds of "this is configuration you need to get you started" because it is very nearly impossible to configure webpack.

Webpack is not alone to blame for this. It's also the fractured tools, the fractured libraries etc.


```javascript
loaders:[{
   test: /(\.css)/,
   loader: "css-loader?module&localIdentName=[path][name]--[local]--[hash:base64:5]"
}]
```

Yes, the above is configuration for [css-loader](https://github.com/webpack/css-loader). Yes, it is a string that contains URL-like structure where parameters you pass in are, well, URL query parameters. Because reasons.

There's a reason for that, obviously. There always is.

First, you can pipe loaders for a file type:

```javascript
loaders:[{
   test: /(\.css)/,
   loader: "style-loader!css-loader?importLoaders=1!autoprefixer-loader"
}]
```

This configuration pipes a `.css` file through `style-loader` then `css-loader` with options then `autoprefixer-loader`.

Second, you can do the same thing from within your code because why the fuck would you not want to do that?

```javascript
require("style-loader!css-loader?importLoaders=1!autoprefixer-loader!...")
```

Did you know you could exclude things from a loader, if, well, there's such an option?

```javascript
loaders:[{
   test: /(\.css)/,
   loader: ExtractTextPlugin.extract('style', 'css?-autoprefixer!postcss')
}]
```

This is a plugin. Acting as a loader. It has a pre-loader, `style`. And a loader. Which is a combination of two loaders, `css` and `postcss`. Oh, and we exclude `autoprefixer` (plugin? feature?) from the `css loader`.

{{< image src="https://cdn.meme.am/instances/400x400/57997219.jpg" />}}

Yes, if there's just one loader, you can provide its parameters as a regular JSON structure (feast your eyes on the [query parameters](http://webpack.github.io/docs/using-loaders.html#query-parameters) section). However, this is yet another impendancy mismatch you have to deal with when trying to figure out what, where and how to configure all the moving parts.

You go an look for docs on a `*-loader`, and you run into anything: config as strings, config as objects, a mix of it. And if something goes wrong, you are left alone, there's [no way to know what failed](https://github.com/webpack/extract-text-webpack-plugin/issues/118).

But honsetly. How much time do you have to spend to come up with this: `ExtractTextPlugin.extract('style', 'css?-autoprefixer!postcss')`?

## Learn to love the stacktrace

Let's pretend you are a C++ developer. You use a `Makefile` to invoke the `gcc` compiler on your source code. If there is an error in your source code, you will see the relevant error.

**For some reason you will never see the stacktraces from either the make tool or from gcc**

Not so in Javascript. Because internal stacktraces from the build tools are the bread and butter of everyday JS development.

Enjoy.

```
> webpack --config webpack.config.js --progress --colors -w -d

Hash: 6f816ab5f143490174a0
Version: webpack 1.13.2
Time: 3176ms
     Asset     Size  Chunks             Chunk Names
    app.js  1.11 MB       0  [emitted]  main
app.js.map  1.25 MB       0  [emitted]  main
   [0] multi main 28 bytes {0} [built]
    + 226 hidden modules

ERROR in ./js/app/fsm/payment-flow-fsm.ts
Module parse failed: /Users/dmitriid/Projects/project/node_modules/awesome-typescript-loader/dist/entry.js!/Users/dmitriid/Projects/project/js/app/fsm/payment-flow-fsm.ts Unexpected token (3:18)
You may need an appropriate loader to handle this file type.
SyntaxError: Unexpected token (3:18)
    at Parser.pp$4.raise (/Users/dmitriid/Projects/project/node_modules/webpack/node_modules/acorn/dist/acorn.js:2221:15)
    at Parser.pp.unexpected (/Users/dmitriid/Projects/project/node_modules/webpack/node_modules/acorn/dist/acorn.js:603:10)
    at Parser.pp$3.parseExprAtom (/Users/dmitriid/Projects/project/node_modules/webpack/node_modules/acorn/dist/acorn.js:1822:12)
    at Parser.pp$3.parseExprSubscripts (/Users/dmitriid/Projects/project/node_modules/webpack/node_modules/acorn/dist/acorn.js:1715:21)
    at Parser.pp$3.parseMaybeUnary (/Users/dmitriid/Projects/project/node_modules/webpack/node_modules/acorn/dist/acorn.js:1692:19)
	<...skip 20 or so lines...>
    at Parser.parse (/Users/dmitriid/Projects/project/node_modules/webpack/node_modules/acorn/dist/acorn.js:516:17)
    at Object.parse (/Users/dmitriid/Projects/project/node_modules/webpack/node_modules/acorn/dist/acorn.js:3098:39)
	<...skip another 20 or so lines...>
    at nextLoader (/Users/dmitriid/Projects/project/node_modules/webpack/node_modules/webpack-core/lib/NormalModuleMixin.js:290:3)
    at /Users/dmitriid/Projects/project/node_modules/webpack/node_modules/webpack-core/lib/NormalModuleMixin.js:259:5
    at Storage.finished (/Users/dmitriid/Projects/project/node_modules/webpack/node_modules/enhanced-resolve/lib/CachedInputFileSystem.js:38:16)
    at /Users/dmitriid/Projects/project/node_modules/webpack/node_modules/enhanced-resolve/node_modules/graceful-fs/graceful-fs.js:78:16
    at FSReqWrap.readFileAfterClose [as oncomplete] (fs.js:380:3)
 @ ./js/app/index.tsx 9:25-58

ERROR in [default] /Users/dmitriid/Projects/project/js/app/fsm/payment-flow-fsm.ts:3:15
Expression expected.

```

The relevant ticket for this is [webpack/webpack#1245](https://github.com/webpack/webpack/issues/1245). Note no one even asks the most obvious question: "why in the seven hells would I need internal stacktraces if I'm not a webpack/plugin developer?" Well, not until yours truly came along.

## Can you understand what actually failed?

So, I'm running this:

```
> webpack --config webpack.config.js --progress --colors "-w" "-d"

Hash: 578f6adad579fede3e98
Version: webpack 1.9.6
Time: 3224ms
     Asset     Size  Chunks             Chunk Names
    app.js  1.12 MB       0  [emitted]  main
app.js.map  1.27 MB       0  [emitted]  main
   [0] multi main 28 bytes {0} [built]
    + 227 hidden modules

ERROR in ./js/app/fsm/state-manager.ts
Module not found: Error: Cannot resolve module 'machina' in /Users/dmitriid/Projects/js/app/fsm
 @ ./js/app/fsm/state-manager.ts 2:14-32
```

Can you immediately tell me if it's `webpack` or `typescript` failing?

Ok, how about this:

```
> webpack --config webpack.config.js --progress --colors "-w" "-d"

Hash: ab8d7ccc3d611479ca81
Version: webpack 1.9.6
Time: 4464ms
     Asset     Size  Chunks             Chunk Names
    app.js   2.4 MB       0  [emitted]  main
app.js.map  2.77 MB       0  [emitted]  main
   [0] multi main 28 bytes {0} [built]
    + 341 hidden modules

ERROR in [default] /Users/dmitriid/Projects/js/app/fsm/state-manager.ts:1:25
Cannot find module 'machina'.

```

As you can *clearly* see, the first one is a webpack error. The second one is TypeScript error. Relevant issue: [webpack/webpack#2878](https://github.com/webpack/webpack/issues/2878) (there are probably others).

## All your options are belong to us

Specifically, the [`watch` option](https://webpack.github.io/docs/configuration.html#watch). Could be others. I don't know and don't care at this point.

So, if you provide `watch: true` in Webpack configuration, Webpack will:

{{< quote author="Webpack documetation" link="https://webpack.github.io/docs/configuration.html#watch">}}Enter watch mode, which rebuilds on file change.{{</ quote >}}

This is, unsurprisingly, not entirely correct. See, if you ever decide to create your own build script, and invoke webpack trough its [node.js](https://webpack.github.io/docs/node.js-api.html) API, you will see that:

- webpack provides to separate APIs: `run` and `watch`
- they are both really identical:
  - you create a `compiler` object by invoking `webpack` with webpack config 
  - you invoke the API
  - you provide a callback which accepts to parameters `err` and `state`

**Except**

- `run` *ignores* the `watch` option of `config`
- `watch` expects a first parameter with options that are already there in the `config`, really

Because, I guess, reasons. And, surprisingly, the "short" version with `webpack(config, callback)` works as expected. Who'd a thunk it.


# Nothing works out of the box anymore

Install and run? Sane defaults? These things are becoming a rare beast in the Javascript world. It seems that *nothing* works out of the box anymore.

In JS world, sadly, going through hoops and withholding crucial information from the developer is now the accepted norm.

## Babel

The only job that Babel does is compiling a next version of JavaScript to the current version of Javascript.

I mean this is what says on its site:

{{% quote link="https://babeljs.io" author="https://babeljs.io" %}}
**Babel is a JavaScript compiler.**

Use next generation JavaScript, today.

Babel transforms your JavaScript

You put JavaScript in

```js
[1,2,3].map(n => n + 1);
```

And get JavaScript out

```js
[1,2,3].map(function(n) {
  return n + 1;
});
```

{{%/ quote %}}

**THIS IS A LIE.** A lie so blatant that the next line on the site says it's a lie:

{{% quote link="https://babeljs.io" author="https://babeljs.io" %}}

Start by installing the Babel CLI and a preset

```
npm install --save-dev babel-cli babel-preset-latest
```

Create a .babelrc file in your project (or use your package.json)

```js
{
  "presets": ["latest"]
}
```

{{%/ quote %}}

Understand this: out of the box the javascript compiler **does not do a single thing**. You have to install a number of plugins/presets before it even does anything.

Moreover, if there are no presets and no plugins installed, babel will not even complain about it. It will just ... do nothing.

Given this `index.js` file:

```js
[1, 2, 3].map(n => n + 1);
```

Running freshly installed babel will *not even warn you, and will do nothing*:

```js
> node_modules/.bin/babel index.js
[1, 2, 3].map(n => n + 1);
```

Only if you install a preset and specify it, you get back what you need.

Babel has the ["latest" preset](http://babeljs.io/docs/plugins/preset-latest/) which is:

{{< quote >}}
This is a special preset that will contain all yearly presets so user’s won’t need to specify each one individually.
{{</quote >}}

- Does this sound like a good sane default to you? Why isn't it the default?
- Does it seem that having no presets or plugins should at least raise a warning or something?

The answer is yes in any world other than Javascript.

# Typescript

I've decided to talk about Typescript, because why not. More often than not Javascript is only used as a target language. Multiple other languages exist that compile/transpile into Javascript while promising nicer features, syntax, tools and so on and so forth. 

[Typescript](http://www.typescriptlang.org) is a superset of Javascript developed by Microsoft. It introduces type checks and various niceties into the language.

It includes a nice fast compiler which removes the need for Babel, but, obviously, it introduces a whole host of other problems.

## Loaders

Not a typescript issue per se, but still.

When invoking from Webpack, you will deal with either [ts-loader](https://github.com/TypeStrong/ts-loader) or [awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader).

The former one is recommended in typescript docs. The latter one is used in 99% of Webpack boilerplates. Good luck figuring out how they are different, what features they support or don't support etc.

I haven't had much experience with ts-loader (yet?), but I've alredy run into the following with `awesome-typescript-loader`.

### Who cares about your configs. Part I

Project from scratch. Forgot to create `tsconfig.json`. No errors whatsoever, obvously. Webpack fails because it cannot parse the non-processed `.ts` file. 

Why did `.ts` compilation fail? Was it due to a missing `tsconfig.json`. Wouldn't it be just so nice if the tools involved could report this?

### Who cares about your configs. Part II

When trying to clean up configs I decided to move `tsconfig.json` to a `config` directory. Provided path to this file as `tsconfig` option as per [README](https://github.com/s-panferov/awesome-typescript-loader/blob/master/README.md).

Provided the following invalid option to the compiler in the `tsconfig`: 

```
{
  "compilerOptions": {
    "target": "absdefg",
  }
}
```

The config above was accepted, and silently ignored. Everything got compiled. Was the config file even picked up? Well, webpack didn't fail, so probably it was (see Part I). Who ignored the error? TS compiler? awesome-config-loader? No one knows, and it is impossible to find out.

## Third-party modules, do you speak it? (upd. 2016-11-16)

Sooner or later you will have to import modules written in or transpiled to Javascript. Unless you develop a library with no external dependencies (quite possible) or something that only depends on other libraries written in Typescript (highly unlikely).

So, you will find yourself typing something like this into your Typescript code:

```typescript
import machina from 'machina';
```

Which will fail:

```
[default] ...app/src/fsm/state-manager.ts:1:25
Cannot find module 'machina'.
```

See, Typescript needs type definitions describing the stuff your import. And here's a type definition that will work just fine:

```typescript
declare module machina;
```
You will ask however, "Is that it?". Yes, that is *it*.

- Typescript knows where the module resides, because it knows how to import stuff from `node_modules`
- Typescript does not need a single type definition to work with such a module
- *Obviously, it will not import such a module unless you provide it with a usless unnecessary stub it could've generated automatically*.

**Edit (Nov 16):** This will finally be fixed in [TypeScript 2.1.3](https://github.com/Microsoft/TypeScript/issues/11106#issuecomment-261012601)

Because reasons. Go ahead and try to make sense of the [ambient modules](https://www.typescriptlang.org/docs/handbook/modules.html#working-with-other-javascript-libraries) section in the docs.

## Types, types everywhere

Libraries are developed in whatever language authors prefer. To provide proper static type checking Typescript needs more than the stub module definitions. It needs actual type definitions for libraries.

Thanks to countless contributors to [DefinitelyTyped](http://definitelytyped.org) there are quite a few definitions Typescript can use.

Well,...for some definition of "can".

```
> npm install @types/superagent

[default] /Users/dmitriid/Projects/keyflow/keyflow-website/app/node_modules/@types/superagent/index.d.ts:83:30
Cannot find name 'Promise'.
```
{{< image src="https://pbs.twimg.com/media/CtgwTouWgAAv5Bc.jpg:large" />}}

See, despite the fact that this is not a single isolated problem, there are no solutions to this.

Well, except one: maybe try a newer version of `npm`, namely npm 3.x.

I personally have a problem with this. node.js has this thing called Node LTS, Long Term Support. And at the time of this writing it was:

```
> node -v
v4.6.0
> npm -v
2.15.9
```

I know, I know. I probably shouldn't run cutting edge stuff on non-cutting-edge platforms, yada yada.

The problem is there, the problem exists. And, obviously, it exists for some modules, and for others (`@types/react` works, `@types/superagent` doesn't, *ad nauseam*). Because reasons.

# Wrapping up

I'm not sure this warrants a conclusion. I've stopped detailing my experience as I was approaching the 4000 word mark. However, there are so many more things that break, run amok, break in unpredictable ways, etc. etc. etc.

I'll leave you with these quotes:

{{% quote author="Alastair Maw" link="https://medium.com/@herebebeasties/your-sentiments-are-admirable-but-never-have-i-worked-in-an-ecosystem-where-the-knowledge-attained-1b7b1ebee617#.85tt4pn8u" %}}

...never have I worked in an ecosystem where the knowledge attained while becoming a master of the craft goes out of date so rapidly, or where solutions are quite so brittle.

The JS world’s obsession with small tools mean that they combine in endless permutations, causing endless issues to debug.

...

When the tower of abstractions falls down in a steaming pile and you need to figure out what’s gone wrong and fix it, you then end up sinking hours and hours into it (all the more because you don’t really understand what’s going on, because you didn’t set it up from scratch).

Or you waste a month figuring out how to plug all the tools together. If I have a complex project I know full well I’m going to want code coverage, a proper module system, minification, etc. etc. The initial time investment to investigate the options here and get it all working is faintly ridiculous compared to ecosystems like Java or .NET (or even C++, for that matter).

I’m not even going to talk about the cavalier attitude various popular parts of the ecosystem (e.g. react-router) have towards API stability.

It’s deeply irksome, at best.

{{%/ quote %}}

{{% quote author="Daniel Ruoso" link="https://medium.com/@ruoso/i-think-the-point-youre-missing-is-that-no-you-re-not-getting-around-to-it-because-the-f62c00d96c72#.exzln83fo" %}}
...the JavaScript community suffers from a very serious case of NIH syndrome, compounded by a neglect for long term sustainability of software projects.

Don’t get me wrong, every single language in the 20 or so years of web development has gone through the framework phase, where people would experiment with solutions for every one of those problems.

The difference is that every one of those languages very quickly converged into good solutions and then made those good solutions into effective tools to get things done.

...

The JavaScript community, otoh, doesn’t seem to get to the converging part...
{{%/ quote %}}

{{% quote author="Yours truly" link="https://medium.com/@dmitriid/javascript-fatigue-vs-stockholm-syndrome-631d4f524008" %}}
It’s been said that “Javascript fatigue” appears because developers are lazy.

It’s been said that “Javascript fatigue” is because developers don’t want to learn anything new.

These arguments are null and void...

- there’s nothing lazy in trying to make your build tool work
- there are exactly zero useful things to learn from that experience

The time I spent trying to figure out the exact motions of all the moving parts I could spend on learning something genuinely new.

Instead, I now have a build toolchain that I have exactly zero confidence in (because it will break unexpectedly at the very next update of any of the fourteen hundred moving parts in it).
{{%/ quote %}}
