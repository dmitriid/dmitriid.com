+++
date = "2016-09-24T10:42:02+02:00"
draft = true
title = "Javascript: Fatigue vs. Stockholm syndrome"
tags = ["javascript", "tools", "rants", "state of the world", "wtf", "musings"]
+++

Programmers are the worst. They will vehemently defend the tool of their choice even though it’s the worst tool in the universe. See any vs in the programming community. Tabs vs. spaces. Emacs vs. vim. C++ vs. PHP. You name it.
tl;dr: Javascript fatigue is real. If you deny it, you have a case of Stockholm syndrome. <!--more-->The problem isn’t new, see these two excelent blog posts: [http://blog.keithcirkel.co.uk/why-we-should-stop-using-grunt/](http://blog.keithcirkel.co.uk/why-we-should-stop-using-grunt) and [http://blog.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/](http://blog.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/) for a calmer discussion.

# A little true story
All joking aside, I think that Javascript programmers are even worse than the worst. Here’s a little true story that happened to me three weeks ago.

We have a project which started way before Webpack was in any useable shape or form. So, it uses Grunt. It’s all been fine, and Grunt has been chugging along quite happily (chugging, because, well, you need to *concat* all/some/some magic number of files before it can figure out what to do with them. Yes, concat. *Sigh*). Until we imported a small three-file component which was written in — wait for it — ES6.

ES6 is the next version of Javascript (erm, ECMAScript) which is supported in exactly zero browsers, and exactly zero versions of any of the Javascript virtual machines. Through the magic of *transpilers* it can be converted to a supported version of Javascript. Therefore half of the internet publishes their code in ES6 now.

Oh my. I know what we need! We need Babel! The best tool to convert pesky ES6 into shiny ESwhatever-the-version (I’m told it’s 5).

Install Babel. Run.

```
>> ParseError: ‘import’ and ‘export’ may appear only with ‘sourceType: module’
Warning: Error running grunt-browserify. Use — force to continue.
```

Ok. Bear with me. Babel, whose job 99% of the time consists of transforming ES6 code into ES5 code *no longer does this out of the box*. I have no idea if it does anything out of the box anymore.

But it comes with nice presets! One of them does the job! It’s even called, erm, *es-2015*. Whatever. Specify it in options, run grunt be happy.

```
>> ParseError: ‘import’ and ‘export’ may appear only with ‘sourceType: module’
Warning: Error running grunt-browserify. Use — force to continue.
```

Ok. Bear with me. A preset is an umbrella name that specifies a list of plugins Babel will apply to code. If these plugins are not present, Babel will fail silently.

Oh, it doesn’t fail in your particular setup? Oh, how so very nice to be you. The problem is: *there is exactly zero info on which of the moving parts of the entire system silently swallows the error*.

Let’s step back for a second, and consider:

- Grunt does not transform code, it’s a “task runner”
The task it runs is called *browserify*
- Well, the problem with the browserify *task* is that the *task* runner cannot run it. It needs a plugin called *grunt-browserify* to do that
- Oh, and browserify has to run babel on the source code before it can do anything with it.
- And the problem is that browserify cannot run babel directly. It needs *babelify* to work

All in all the whole toolchain to produce a Javascript file is *grunt -> grunt-browserify -> browserify -> babelify -> babel*. And someone in that chain decides that babel missing all of its specified plugins *is not a reason to throw an error, stop and report*.

Unwind. Relax. Breathe. Solve differential equations in your head. Install whatever’s needed for babel. Run grunt.

```
>> ParseError: ‘import’ and ‘export’ may appear only with ‘sourceType: module’
Warning: Error running grunt-browserify. Use — force to continue.
```

Oh, Jesus Christ on a pony! What now? Ok. I’m a smart developer. I can figure this out. I mean, if I cannot debug my own toolchain, what good am I?

So, grunt has a `-d` option which means *debug*. Awesome.

Ok. Bear with me. *The debug option passed to grunt does not propagate through the mess of twig and sticks called a toolchain*. *Grunt* does not pass the debug option to *grunt-browserify* does not pass the debug option to *browserify* does not pass the debug option to *babelify* does not pass the debug option to *babel*.

You have to provide separate debug options to every piece of the toolschain and pray to god that this piece provides such an option and does not ignore it.

Let’s add `debug: true` to babelify.

```
>> ParseError: ‘import’ and ‘export’ may appear only with ‘sourceType: module’
Warning: Error running grunt-browserify. Use — force to continue.
```

Exactly. Was the `debug: true` option ignored? Or is this *all* the debug info I can get? *I have no idea*.

Ok. Bear with me. Grunt has *a specific list of files and components it needs to process*. I can only assume that the broken ladder of crap called the toolchain gets this list from Grunt with instructions: “These are the files. Process them.”

Despite all that, *Babel by default does not process files from node_modules. Even when invoked from grunt-whatever-theplugin-is-i-dont-care will not process them, and will silently skip them*. You have to explicitly provide a separate `global: true` option to all places in grunt->grunt-broswerify->babelify config where you think that code from node_modules may be imported/invoked/whatever.

# No, it’s Stockholm syndrome

I’ve been told that [this](http://www.2ality.com/2016/02/js-fatigue-fatigue.html) article is a valid argument against “Javascript fatigue”.

It’s not. It’s Stockholm syndrome.

- *Don’t try to know everything*  
I’m not “using everything”. Only the absolute minimum I need to do my job. Going as far as rewriting or reimplementing things that are overy bloated
- *Wait for the critical mass.*  
How is Grunt, browserify, Babel not critical mass?
- *Do exploratory toy projects*  
Believe me, I do. It is nigh impossible to start a toy project these days, unless you blindly copy paste an umpteenth webpack-starter-kit-for-reals-this-time-works-I-promise and pray that it works for the current minor and major versions of all the moving parts involved. Unless you have your one config file, faithfully copy-pasted all over the place.
- *Diversify in life*  
I do kendo, aikido, contemporary dance, salsa, and amateur Russian theater. How’s that for diversification? How any of these can help me with the abomination in the first part of this post?
- *You can always go back to fundamentals*  
How very condescending of you. I wrote articles (albeit in Russian) on fundamentals.

Nothing can excuse the terrible horrible mess that the state of Javascript development is in right now. Step back, and *look* at your tools. Really *look* at them. There is a reason we have a million “webpack starter packs”. Because nothing works unless you invoke a number of semi-arcane incantations with increasingly inane combinations and versions of options.

```
loaders:[{
   test: /(\.css)/,
   loader: "css-loader?module&localIdentName=[path][name] — -[local] — -[hash:base64:5]"
}]
```

Really?!

I will not even go into how half of these tools don’t support recursing directories or globs. Or how another half of them doesn’t support monitoring the file system and recompiling stuff on the fly (what? recompiling on the fly with *dependency tracking* wat?).

Why are you supporting this?

# I’m not lazy. I don’t not want to learn

It’s been said that “Javascript fatigue” appears because developers are lazy.

It’s been said that “Javascript fatigue” is because developers don’t want to learn anything new.

These arguments are null and void. If you read the first part of the story, you’ve seen that:

- there’s nothing lazy in trying to make your build tool work
- there are exactly zero useful things to learn from that experience

The time I spent trying to figure out the exact motions of all the moving parts I could spend on learning something genuinely new.

Instead, I now have a build toolchain that I have exactly zero confidence in (because it will break unexpectedly at the very next update of any of the fourteen hundred moving parts in it).

And yes, I will be removing some of those moving parts. It doesn’t mean that I will enjoy it or learn anything remotely useful from it.

<em>(imgur style): send me your *-starter-packs :)</em>
