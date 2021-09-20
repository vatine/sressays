# When do you "know" a language?

People I know who work with computers often end up having to write
code, in one or more languauges. To do that, you need to have some
level of knowledge of the language, but there's also a mile-wide
difference between "being comfortable making small changes in existing
code" and "writing code from scratch".

At what level of knowledge can you say that you "know" a specific
language? This is an interesting question, and I suspect that the
answer differs from person to person. I also suspect that what the
answer is, reveals something about the person.

I will not try to tell you what you should consider the right level
for you. But, I will explore this question, for myself, to see where
this leads.

After that digression, I will try to summarise.

## Languages I definitely do not know

I don't know D. I don't know Rust. I know neither Haskell, nor OCaml.

I can say this, because I have never written a single line of them,
and I don't know that I could, without at least some level of
coaching.

I am compfortable answering "do you know X" for any of these with
"no".

## Languages I might know

### Prolog
I maybe know Prolog. I have not written any prolog for about 30 years,
and what I wrote was in "datavetenskap" class in the Swedish gymnasium
(using, if memory serves me right, Turbo Prolog). But, back then I
knew it well enough that not only did I solve teh exercises we were
supposed to solve, but also implemented a simlistic library for
derivation of polynomials. I also started looking at simplification of
the results, but, well, that didn't work.

### Java
I may know Java. I have now written syntactically correct Java code at
two work places, implementing features as envisioned. But, I feel less
confident writing Java than I do writing C++. I am also deeply
saddened every time I remember that a Java object is not its own green
thread that you can send messages to. One, if not the only, reasons
that I never picked Java up when it was new and shiny. I have mostly
managed to crib from existing code. None of the fetaures have been
very complicated. I am comfortable to say that I probbaly don't know
Java, but maybe I do.

### C++
I may know C++. I have written some C++, from scratch, at a previous
work-place. It re-implemeted two hard-coded decision makers for
"should I participate in leader election" as a generalised framework,
where deciders were now any class that fulfilled an interface, and you
could register them, either when you created the "should we
participate or not" container thing, or after the fact. The code
passed peer review, and actually netted me "C++ Readability"
(basically, it allowed me the privilege to say "this C++ looks
OK"). But, I never got to the point where writing C++ felt "fluid". I
needed not only library references at hand, but actual language
references, for any of teh code to actually become valid. To some
extent, I could crib off of existing code. I am comfortable saying
that maybe I know it, but I probably don't.

### C
I may know C. I know that I used to know C, but I have not used it in
anger for a decade or so (despite writing some benchmarking code in C,
only earlier this year, but those were all somple programs). It's been
long enough that I do stupid mistakes, like thinking that functions
need eithehr "func" or "def" to declare them, and sticking types in
the wrong place. I am comfotrable saying that I probably know C, but
maybe I don't.

## Languages I probably know

### Go

I have been writing Go at least every month since 2011 (OK, late
2011). I have left Go code in source repositories at all companies I
worked at, during taht time. OK, so at one place, it was just a simple
"get DNS response times" blackbox prober, but that counts, right?

I am comfortable writing Go code starting from not even a directory. I
frequently reference library documentation, especially if it's a
library I seldom use.

I have written patches for FOSS Go projects, some of which have even
been accepted and merged.

All in all, I am comfortabke with the language. I woudl say that I
know it, but I am not an expert. There are still the occasionaly
corner that surprise me.

### Python

I have been writing python longer than I have been writing
Go. Somewhere in the last N years, I have gone from writing
"python3-friendly python2.7" to "writing python3 code".

On the whole, I am happy writing Python code from scratch. There are
definitely corners of the language I have not explored, so I would not
say I have any mastery of the language, but on the whole I am
compfortable with saying that I know it.

### Shell

I have been writng shell scripts since, um, 1988 or so. I have
probably written less shell, as time has gone on. Mostly because other
languages have started picking up the slack.

I have reached the point where I try to write as little shell as
possible. It is, on the whole, not an excellent programing
languauge. Its strength lies more in being an excellent glue between
programs written in other languages.

I know enough shell to know what bits I should stay away from in
things committed to version control. There's a LOT of interesting
magic you can do, that is utterly unmaintainable if you use it.

I would say that I know shell, but I am not (and have no intention of
becoming) a master of it.

### Common Lisp

A language I use a lot less than I used to. Which, on the whole, is a
bit of a shame. I like the language. When I use it, I occasionally
have to go check the HyperSpec for some specifics around one of the
978 standard library symbols, but I can usually find that prety quick.

On the whole, I woudl say that I know Common Lisp, but I may entertain
the notion taht it is starting to slightly slip out of my grasp.

## In summary

For me, "knowing a language" seems to imply that I am comfortable
starting from scratch in the language. That I don't need to consult
references all the time. I would also go as far as saying taht I would
probably be happy to white-board-code in any of the languages that I
definitely consider myself to know.

Note that there are a bunch of languages that I have not mentioned
above, that probably would end up in the "might know" category (like,
say, APL, or Pascal, neither of which I have used in 20+ years).

What (programming) languagues do you know? What are your decision
criteria for the "defintely do not know", "might know", "probably
know" categories?
