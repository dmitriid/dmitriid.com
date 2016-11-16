+++
title = "Why I'm not using closure compiler"
draft = true
date = "2016-11-01T13:18:53+01:00"

+++

# The question

**tl;dr**: Closure compiler makes little to no sense outside of Google's ecosystem. 

Nolan Lawson conducted a very nice research on how various Javasctip tools bundle/compile Javascript. I highly recommend it: [The cost of small modules](https://nolanlawson.com/2016/08/15/the-cost-of-small-modules/).

This article has made several rounds on Twitter and many people have asked: *Why aren't more people using Closure*? There are many reasons for that.

Considering the [dire](/blog/2016/10/javascript-tools/) [state](https://medium.com/@dmitriid/javascript-fatigue-vs-stockholm-syndrome-631d4f524008) of Javascript tools today, Google's Closure compiler is yet another cryptic, badly configured, half-baked tool to through into the ever-groing pile of twigs and sticks called Javascript infrastructure.

# Documentation

There's basically none.

The [Quickstart](https://developers.google.com/closure/compiler/docs/gettingstarted_app) shows how to create a page that contains basically exactly one line of Javascript code. Instead of showing you how to do more, the next step is [Advanced compilation](https://developers.google.com/closure/compiler/docs/api-tutorial3) which is basically Javascript one-liners interspersed with Python code to invoke the compiler service.

- How do I set up a project to compile my application?
- How do I properly process the multiple modules my application has?
- How do I include/process third-party modules?
- How do I bundle stuff?
- etc.

All these are unanswered.

Let's download the app then. There could me more info.

## To run this you need a library you don't need

The README for the compiler has this nugget:

{{% quote %}}
If you're using globs or many files, you may start to run into
problems with managing dependencies between scripts. In this case, you should use the [Closure Library](https://developers.google.com/closure/library/). It contains functions for enforcing dependencies between scripts, and Closure Compiler will re-order the inputs automatically.
{{%/ quote %}}

If you follow the link, this is the page you land on:

{{% quote %}}
The Closure Library is a broad, well-tested, modular, and cross-browser JavaScript library. You can pull just what you need from a large set of reusable UI widgets and controls, and from lower-level utilities for DOM manipulation, server communication, animation, data structures, unit testing, rich-text editing, and more.
{{%/ quote %}}

WAT?

I want to handle my dependencies, not have a UI library. Maybe they refer to [ClosureBuilder](https://developers.google.com/closure/library/docs/closurebuilder)? I have no idea.

# Let's maybe run it?

I have some code in my app that consists of multiple modules, relies on some third-library code (`node_modules`) etc. The entry point is `index.js`

How do I run it so that it generates code I need to run my app in the browser?

However you run it, it only produces some minified code that:

- Doesn't include any dependencies (except those directly in the folder)
- Generates code that throws a `require is not defined` error in the browser

At this point I'm ready to give up because, well, I already have my sweet set up that handles everything, transpiles, and compiles, and minifies, and bundles all code.

Switching to `ADVANCED` compilation modules may pollute your console output with mutiple warnings or errors that are also not helpful in the least.

# In (small) conclusion

Google's Closure compiler makes no sense outside Gogole infrastructure. When you have set up everything the Google way and there are people to help you along as you run into problems, you're ok.

When you're alone (as most devs are), you will either spend an unknown number of hours going through error-messages, disassembling the setups of other projects (ClojureScript, Angular 2)...

Or just use the tools which you kinda sorta can setup without going insane
