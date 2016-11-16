+++
title = "why mobx"
draft = true
date = "2016-11-16T16:51:56+01:00"

+++

My thinking would be like:

What if we create a todo list?

In redux you need:

- a store
- an action type (strings!) per each user action
- propagate state down from parent element (I’m guessing, have no idea what redux does these days)
make all moving parts aware of actions
- etc.?

In MobX you can treat your data as a black box with an API:

- create a store with `@observable` and `@computed` properties
- `@action` for complex data manipulation
- Basically all your components can be stateless components within an @observer


Also:

- mobx isn’t react-only. It’s pretty trivial to add it to anything, see virtual-dom: https://medium.com/@botverse/enjoying-mobx-jsx-and-virtual-dom-621dcc2a2bd5#.x00dl3vwv I’ve started using it with snabbdom
- with React and Mobx React Dev Tools you see full overview of how your system behaves and where the data goes

One thing to say for Redux though is that it forces “a strict unidirectional data flow.” (a quote from their website). E.g. cycle.js builds around the same concept (but bases itself on reactive streams)

MobX doesn’t care what approach you choose. You can be as sloppy or as good as you want

However, when all data is in an `@observable` in a store/stores, MobX makes the “unidirectional data flow” trivial.
