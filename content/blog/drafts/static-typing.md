+++
date = "2016-09-21T13:38:57+02:00"
draft = true
title = "Static Typing"
+++

If you want to read many rambling words about my views on static typing, read on.
If you want to use static typing to solve a small-ish real-world problem (and prove that static typing is up to the task), read here.

<!--more-->

# Intro, or It's a Fundamental Problem With Claims

Time and again I find myself either reading or participating in various discussions and arguments regarding static typing. Time and again I read the same tired old arguments for and against. And now I find myself tired and old :)

> First, let me be perfectly clear: I'm neither for nor against static typing. Static typing is a tool. As any tool it has its uses and limitations. I am against the bold, sweeping, and largely unsubstantiated claims made by proponents of static typing.

The problem with IT as it exists now is total lack of and disregard for the scientific method. We routinely believe in claims by anyone who makes a claim first, or shouts the most, or gets more people to their side. This ranges from benchmarks run on laptops to code styles, from tooling to language design.

# Claims, or What People Swear By

Same applies to the great static vs. dynamic debate. All of the following widely accepted and believed claims have very few, if any, solid proofs beside hearsay, anecdotes, and personal preferences:

- If a program compiles, it's correct. Or, more recently rephrased as "the compiler provides guarantees for a program's correctness"
- Types are self-documenting. Or, types make it easier to reason about a program.
- Types eliminate many or most errors that a programmer makes
- Types eliminate many or most runtime errors
- Types significantly reduce the amount of bugs in a program
- Types help deal with changing requirements (e.g. because it's easier to refactor code with types)

**TODO : review/rewrite/add. Also see what was said on RSDN**

Rule of the thumb: if you say "well, obviously" to any of the above, you need to think again. Cognitive biases, personal preferences, bad or good experience and the ever-present Dunning-Kruger *require* you to provide solid proof for any "well, obviously".

# You Are Wrong, or No, You Are Wrong

In recent times I've seen a few people question the validity of the above claims. A part from the "well, obviously" proponents of static typing usually resort to exactly two types of counter-arguments:

## The "strawman"

Whatever example you can come up with showing that types are inadequate in certain scenarios, it will be dismissed as strawman, artificial, not existing in practice etc. This "counter argument" is so blatantly wrong on so many levels, it's not even funny. And I'm surprised so many people get baffled by it.

**TODO: Popper, falsification. A theory is as good as it's ability to explain phenomena. If counter-examples appear, theory has to be accommodated or changed, or thrown out entirely.**

## Your type system is wrong

The most common manifestation is, of course, "By types I don't mean Java". However, even Haskell (ever a static typing  darling) is not immune to this argument. Since very few people know enough Haskell (or use enough Haskell in production) to argue, you rarely see this in the wild, but it's there. "Why, of course you need dependent types for this, or liquid type for that, or whatever is type word _du jour_ is. Oh, too bad Haskell doesn't have it, but trust me, types easily solve whatever little problem you may think you've come up with".

Again. Wrong on an all levels. If your theory only works for some theoretical yet-to-be invented programming language, you are not really allowed to make bold sweeping claims.

# The Evidence, or The Hard Truth

**TODO: Add types research applicable to programming. Shorter more expressive code beats types hands down. Only 10% caught by static types etc.**

# Your Documentation is Only as Good as Your APIs

"Types autodocumenting code".


Consider this function: `trans_asses_to_asses(assessments :: AssessmentList) -> None`. It's a real function form a real-life code base.

From the fact that it exists in a `assessments` module/package you can deduce that it means "transform transactional assessments to assessments". Whoopty doo. This does not help in the least. You need specific domain knowledge and a lot of digging around the code to understand what the hell is going on. And pray that the libraries called from this function have their sources. Otherwise you'll be stuck with only function signatures.


It gets worse as the code base grows, thrid-party libraries are pulled in, or if the number of people working on the code base increases.