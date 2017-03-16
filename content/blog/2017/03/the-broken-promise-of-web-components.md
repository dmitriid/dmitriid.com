+++
date = "2017-03-14T23:57:58+02:00"
Lastmod = "2017-03-16T09:52:00+02:00"
draft = false
title = "The broken promise of Web Components"
summary = "Web Components are the promise of a bright new future, aren't they?"
banner = "https://farm6.staticflickr.com/5592/29946893014_d6fbdbe1ff_k_d.jpg"
tags = ["javascript", "dx", "web"]
+++

Disclaimer: I talk a lot about React here, but you can substitute your favorite library: Inferno, Preact, Vue, snabbdom, virtual-dom (or non-js libraries and frameworks like Elm, Om, etc.). Similarly, replace Polymer with Vaadin, or X-Tag, or...

_Also, read Rob Dodson's excellent response to this article: [https://robdodson.me/regarding-the-broken-promise-of-web-components/](https://robdodson.me/regarding-the-broken-promise-of-web-components/)_

# Brief, incomplete, and mostly incorrect history of Web Components

## Ancient times

By 2011 Internet had grown. It had Facebooks and Gmails, and Twitters, and Asanas, and Google Docs, and countless other online _things_ that could no longer be called sites, or Single Page Applications. They were, for all intents and puposes, applications. As simple as that.

And woe was to the devs who were developing them.

State of the art for Web GUIs at the time was probably a templating language glued together by some serverside logic and/or a client-side library. [Backbone](http://backbonejs.org) if you were lucky. [jQuery UI](http://jqueryui.com) or [Sencha/ExtJs](https://www.sencha.com/products/extjs/) if you were enterprise enough.

This was cumbersome. This was limiting. You could not prototype easily and quickly. You could not easily escape the limitations of UI libraries. etc. etc. etc.

And you were limited to the same set of HTML elements as ever: `div`s, `p`s, `forms`s...

In 2011 Alex Russel proposed [a vision of the future](https://fronteers.nl/congres/2011/sessions/web-components-and-model-driven-views-alex-russell) (emphasis mine):

{{% quote %}}
I think we're stuck today in a little bit of a rut of extensibility. We wind up leaning on JavaScript to get things, because it is the Turing complete language in our environment. It is the only thing that can give us an answer when CSS and HTML fail us. So we wind up piling ourselves into the JavaScript boat. We keep piling into the JavaScript boat.

Bruce yesterday brought up the great example of an empty body tag, and sort of this pathological case of piling yourself into the JavaScript boat, where you wind up then having to go recreate all of the stuff that the browser was going to do more or less for you if you'd sent markup down the wire in order to get back to the same value that was going to be provided to you if you'd done it in markup. But you did it for a good reason. Gmail has an empty body tag, not because it's stupid. Gmail does that because that's how you can actually deliver the functionality of Gmail in a way that's both meaningful and reliable and maintainable. You wind up putting all of your bets, all of your eggs, into the JavaScript basket.
 
...

It takes browsers time to implement stuff. We have to get it out to users, now users have to start using it, and then we have to look at our deployed population and go, "OK, now I can use this feature, I can target this feature."

So as developers, this is the sort of things we thrive on. The faster that this crank turns, the more chances we get to see new features enter the market that we can start to target. "OK, well, this is good."

...

<strong>So we wind up with this unspoken tension between deep pragmatism and the Platonic ideal of where we would like to be.</strong> But we don't have a really good model for thinking about it.

...

The more of this behavior [behavior agreed-upon, known to devs, and implemented in the browser] that we take into ourselves, the more we do in JavaScript, the more we get away from the idea of shared ambiguity, which is what makes the world work.

...

<strong>We want to feed this process of progress.</strong> I think we get stuck in a place where we consider HTML5, we're done.
{{%/ quote %}}

And then he goes on to introduce and demo Web Components, which  at the time were three different things: Scoped CSS, Shadow DOM and Web Components. (I also highly recommend his talk in general)

But then [W3C](https://www.w3.org) happened. In true w3c fashion it went ahead and spent another 5 years defining the Platonic ideal and never feeding the progress as a result.

## Cue in Facebook

Facebook application is complex. It might not look like it, but it is. Those little boxes everywhere on the page have surprisingly complex layouts _which have to be repeated, and/or customized, and/or adjusted_ in various contexts. A developer would naturally want to do the following: take this `box` element, and put it _here_, and apply these random styles to it without disturbing anything on the page.

And it has to be reasonably fast. Because, well, DOM updates are notoriously slow, and there are countless articles detailing how you _absolutely must_ reduce the number of times you access the DOM.

It's so bad that `innerHTML`, a sign of horrible smelly code, is [on par with _or faster_](http://andrew.hedges.name/experiments/innerhtml/) than DOM manipulation.

So, what did Facebook do? Oh, simple, they basically wrote their own implementation of Web Components entirely in Javascript. With an XML-based DSL to boot. They called it [React](https://facebook.github.io/react/) and unleashed it unto the world in 2013.

React provides you with following:

- a way to define your own custom elements
- place them on the page with HTML-like syntax
- provides a fast virtual DOM implementation that minimizes changes to the actual DOM
- has very few limitations on what you can do with or within components because it's Javascript all the way down (the DSL is a thin wrapper on top of a small number of functions)

No wonder React took the world by storm. Those who weren't writing it were surely talking about it. It spawned several competitiors that are aiming for the same feature set ([Inferno](https://infernojs.org), [Preact](https://preactjs.com)) or various subsets, most notably Virtual DOM ([Snabbdom](https://github.com/snabbdom/snabbdom), [virtual-dom](https://github.com/Matt-Esch/virtual-dom) etc.).

## 2017

In 2017 React fulfills all the promises of Web Components: it lets you write performant reusable self-contained components. It can run on almost any Javascript-enabled browser (React doesn't support IE < 9).

As the ecosystem blossomed, it went far beyond the scope of Web Components. If I'm not mistaken, [CSS Modules](https://github.com/css-modules/css-modules) proposal appeared because it was first implemented in, and for, React.

In 2017 Web Components [are in development](http://caniuse.com/#search=web%20compo) despite already spawning two versions each of two of underlying standards.

At the time of this writing the situation for Web Components looks like this:

{{< fullimage src="/assets/img/blog/web-components-support.png" >}}


# So what's this broken promise I hear about?

Well, the main failure is obvious: they are nowhere to be seen. The promise of "feeding the process of progress" is unfulfilled. By their 6<sup>th</sup> year they spawned a total of 6 standards. Two of them are already deprecated. Only one major browser is commited to supporting them (sorry, Opera, you're no longer a major browser, _and_ you run on top of Chrome these days).

The other broken promise is the one bandied about in the Internets these days: interoperable custom components without vendor lock-ins.

And this is the one that got me writing this overly long piece of thinking out loud.

Because there's [Polymer](https://www.polymer-project.org).

Polymer is Google's attempt at creating a Web Components-compliant implementation:

{{< quote >}}
<strong>Unlock the Power of Web Components.</strong> Polymer is a JavaScript library that helps you create custom reusable HTML elements, and use them to build performant, maintainable apps.
{{</ quote >}}

Polymer shows the main problem with Web Components: they are DOM.

## The DOM

Consider the following code in React:

```
<MyComponent style={{border: '1px solid gray'}}>
  {
     ['Hello', 'world'].map((text) => <p>{text}</p>)
  }
</MyComponent>
```

This is a custom component. Its style is defined by a JavaScript object. Its children are defined by `map`ing over an array of values and producing another component. In this case it's a `<p>`, but it could be anything. This component's children is the current array value.

This XML-like DSL is directly [translated into JavaScript](http://bit.ly/2nC6fdu):

```js
React.createElement(
  MyComponent,
  { style: { border: '1px solid gray' } },
  ['Hello', 'world'].map(text => React.createElement(
    'p',
    null,
    text
  ))
);
```

A similar feat in WebComponents would be ... well...

If you go for HTML as a counterexample for React's DSL, it's impossible:

```xml
<my-component style="only strings are allowed in attributes">
  ... nothing here ... 
  only other components or text allowed here
</my-component>
```

What about JS APIs? Remember I told you Web Components is DOM?

```js
const MyComponent = document.createElement('my-component')
MyComponent.style.border = '1px solid gray'

['Hello', 'world'].forEach(('text') => {
	const p = document.createElement('p')
	p.textContent(text)
	
	MyComponent.appendChild(p)
})
```

This gets progressively worse as your components grow in complexity. Imagine adding a `span` around the `text` in `p`?

React? Easy-peasy. Just add it:

```
     ['Hello', 'world'].map((text) => {
       return <p><span>{text}</span></p>
     })
```

Web Components? Well, it's DOM:

```
['Hello', 'world'].forEach(('text') => {
	const p = document.createElement('p')
	const span = document.createElement('span')
	span.textContent(text)
	p.appendChild(span)
	
	MyComponent.appendChild(p)
})
```

_Ad infinitum_.


## Let's break compatibility

I assume the limitations described above were the immediate problem that Polymer faced. How do you work around this? Well, you invent your own not-really-JavaScript-but-kinda-Javascript kinda-templating-kinda-scripting kinda-language. That can only exist in strings.

Work your way through Polymer's [data system](https://www.polymer-project.org/2.0/docs/devguide/data-system) for a full overview. Below are just some examples.

_Note: none of these `[[]]`, `{{}}`, `$=` etc. are in the Web Component spec_

```
<template>
  <div>[[name.first]] [[name.last]]</div>
</template>

<my-input value="{{name}}"></my-input>

static get properties() {
  return {
    active: {
      type: Boolean,
      observer: 'userListChanged(users.*, filter)'
    }
  }
}

<div>[[_formatName(first, last, title)]]</div>

<a href$="{{hostProperty}}">
```

etc. etc. etc.

And my favorite [one](https://www.polymer-project.org/2.0/docs/devguide/data-binding#annotated-computed): 

{{% quote %}}
**Commas in literal strings**: Any comma occurring in a string literal **must** be escaped using a backslash (\\).

```xml
<dom-module id="x-custom">
  <template>
    <span>{{translate('Hello\, nice to meet you', first, last)}}</span>
  </template>
</dom-module>
```

{{%/ quote %}}

I mean, [wat](https://www.destroyallsoftware.com/talks/wat).

# Seriously, y'all

In all seriousness though. Web Components ended up delivering hardly anything from their original promises (or have hardly answered any of the originally raised questions):

- Their specs depend on JavaScript to work:
  - Custom Elements are a part of [scripting](https://html.spec.whatwg.org/multipage/scripting.html#custom-elements)
  - HTML Templates exist only to be [manipulated by scripts](https://html.spec.whatwg.org/multipage/scripting.html#the-template-element)
  - I don't even know if [Shadow DOM](https://www.w3.org/TR/shadow-dom/) can be used without JavaScript
  - And only [HTML imports](http://w3c.github.io/webcomponents/spec/imports/) don't need JavaScript
- They are DOM. So:
	- [attributes](https://html.spec.whatwg.org/#attributes) are strings
	- [content models](https://html.spec.whatwg.org/#kinds-of-content) are strange (we'll have to wait and see how they end up [interacting](https://html.spec.whatwg.org/multipage/scripting.html#custom-elements-autonomous-drawbacks) in deeply nested structures)
- To work around limitations (such as string attributes) libraries will (and have) come up with incompatible ways to pass data
	- is Polymer's `attr$='{{user.name}}'` better than Vaadin's `item-label-path="name.first"` or Angular's `<div *ngFor="let hero of heroes">{{hero.name}}</div>` or more compatible with others?
	- What, where, and how should I import the entirety of a library X to deal with their weird ways of dealing with DOM limitations if I deal with multiple nested components?
	- DOM APIs are horrible, cumbersome, awkward and clunky. Polymer and others are bravely trying to use DOM APIs only, but even they resort to `innerHTML` anywhere they don't have to put on a show ([tests](https://github.com/Polymer/polymer/search?utf8=✓&q=innerHTML), for example). When Web Components take root, the web will be flooded with less performant `innerHTML`s and possibly re-implementations of snabbdoms and virtual-doms (obviously incompatible)
	- how will this help with interoperability and vendor lock-ins if everyone will chose their own ways of dealing with this?
- Scoped CSS...
  - CSS Modules. Need I say more?

These are just a few warts I could come up wth off the top of my head. I haven't seen them really truly discussed anywhere. 

React team went as far as to [say](https://docs.google.com/document/d/1QZxArgMwidgCrAbuSikcB2iBxkffH6w0YB0C1qCsuH0/edit)

{{% quote %}}
We’re not going to use it at all at Facebook.  We’re not going to build React on it because there’s a strong model difference -- imperative in Web Components to declarative in React.  Web Components doesn’t have an idiomatic way to define things like where events go.  How do you pass data when everything is a string?  We see it more as an interop layer that lets various frameworks talk to each other.
{{%/ quote %}}

Nowadays React lets you have them as the [leaf nodes](https://www.youtube.com/watch?t=124&v=g0TD0efcwVg) in the component tree because React assumes any component name that starts with a lowercase to be a DOM element. 

To [quote Pete Hunt](https://www.youtube.com/watch?time_continue=176&v=MC376f3QWYw):

{{% quote %}}
There's a lot of stuff in Web Components spec that is nice. Being able to customize how select work for example (like dropdowns). So there's a lot of great stuff in Web Components, but it's not gonna be the way you structure your applications. and that's what React tries to solve: how do you structure your application, manipulate the DOM.

Web Components are more of the same regular DOM API. What I like to think of it is: it standardized the worst practices. 
{{%/ quote %}}

There are very very few discussions about these issues except for comments on Twitter or on [various articles](http://www.2ality.com/2015/08/web-component-status.html). The consensus seems to be "Web Components is the glorious interoparable fast performant future".

Is it?

_Rob Dodson posted excellent response to this article: [https://robdodson.me/regarding-the-broken-promise-of-web-components/](https://robdodson.me/regarding-the-broken-promise-of-web-components/). I highly recommend it._

# Credits

- Image: [Nobody Home Yet](https://www.flickr.com/photos/yoorock/29946893014/in/photolist-MCiDXC-fCXhFm-7mUqAr-rjo2tE-efLtJk-9kt8ut-pHizLn-rtRryk-qNtRbo-rs9wfQ-b4uEDP-n6ehKp-8B2g2b-pbNJRv-ggn9D4-rRDzJx-rianKH-q99pSr-dWkdFk-qskyPz-fPj1CE-quEQJb-ncm3w5-eLESPz-e9Vvnd-qLHL4n-rcWNaj-gfR9gS-dWvGBg-e3naF7-q6u4ng-mAhi34-dZx5qo-qV7GRy-dGvcTV-dZPw7d-egk2QP-fjuGKk-egLqSQ-e1SKBD-qwWjgJ-fdN2B3-dWRvrG-eY5gfm-r96KKY-efWUty-egTh1R-r8yZ93-fd3kv4-dWB3HA) by Rich Herrmann, [CC BY-NC-ND 2.0](https://creativecommons.org/licenses/by-nc-nd/2.0/)
- Links to some of the material were found in [this blog post](http://www.2ality.com/2015/08/web-component-status.html) by Dr. Axel Rauschmayer 
