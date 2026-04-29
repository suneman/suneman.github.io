---
title: "How to write a Master's Thesis"
date: 2016-01-24 23:24:57
slug: "how-to-write-a-masters-thesis"
status: publish
author: "sunelehmann"
original_url: "https://sunelehmann.com/how-to-write-a-masters-thesis/"
---

Well, ok. The title should probably be "How to write a Master's Thesis *in my group*"*,* but's who's counting? Below, I've collected some notes on tips and tricks - it's a long doc, but I hope it's useful.

Let me know if something could be better/clearer and I will update it. If you're currently writing a thesis, in my group, I recommend you read it once in a while.

Also - this is **not** the place for answers regarding any admin questions. BUT don't worry. If you're at DTU, [this magical and comprehensive page, will answer all your questions](https://www.inside.dtu.dk/en/undervisning/regler/afsluttende-projekter/kandidatspeciale?fs=1). Not kidding. This is where you'll find all the rules about extensions, exams, etc.

## What is a good thesis?

The point of writing a thesis is to have a written record that demonstrates (to me and the external examiner):

- What you're able to do.
- What you have learned.

The point, in a bit more detail, is that the thesis should show how you're able to apply all the things you've learned during your reading, simulations, and research in general to solve a problem - perhaps even show how you've generated a bit of new knowledge yourself.

But there are many aspects to this. Below, I've put together my top 10 tips for writing an **excellent thesis.**

## Tips and tricks

### Tip 1: Reproducibility

I'll repeat the most important thing from above one more time and expand a little bit just to make sure that we all remember this fundamental part.

> The point of your thesis is to **report your research process***.*

Tell us about the methods you have used. Do that accurately and precisely. Think ***reproducibility*** when you're writing (also when thinking about how much math & methods to include) - someone else should be able to pick up your report and redo the work.

This also means that it is crucial justify the choices you have made (why you chose method X over method Y, why made choice Z in the preparation of data) - that way we can evaluate, not just your results, but the entire process you have used to arrive at those results (so even if you did something wrong, you can still get credit for having thought about the problem the right way).

### Tip 2: Take notes

For the rest of your life, no-one will care about the things you've tried that didn't work. They will just want you to write down the parts that work and forget about everything else.

*That's not the case for your Master's thesis.*

The point of the thesis is to spend 5-6 months researching a topic, getting to know the literature, attacking the issue from different angles, and figuring out something for yourself. See "What is a good thesis" above for more details.

Your thesis should clean the research process up a little bit (as explained elsewhere in this post), but for the Master's project, we truly want to know about all the things you've tried and learned. That means that negative results (e.g. something doesn't work) are just as important as new findings. Why? Because the process (and not the result) is the important thing.

All of that means that taking notes is crucial!

Let me say that again: **Taking notes is super important.**

Writing a thesis takes five-six months, and there's no way that you will be able to remember the details of the methods you used in month one, when you get around to writing the thesis.

I'm not saying you should write detailed text about your results (since you won't know what's important in the beginning), just note down the important findings, parameter settings, that kind of thing. Below are some examples.

- Example 1: Take notes for every paper you need, and add them to the *Literature Review*section in your .tex document (and add the according entry to your .bib file).
- Example 2: Save the most important figures (including plot titles and nicely labeled axes) and write a few words of caption for each one to help you remember the important results. *Perhaps even add them to the appropriate section in your LaTeX file!*
- Example 3: You can usually write large parts of the methods section early, why not do that? Maybe even as you're reading up on theory?
- Example 4: Make sure your code is marginally readable because you will probably have to redo some of your calculations/simulations/predictions/analyses.

### Tip 3: Create a good list of references (and - in the process - also a good literature review)

Almost all M.Sc. theses will rely heavily on one, two, or three central papers. That's how it (usually) works. But you need to have a much bigger list of references to show that you're aware of the research-world surrounding those papers. I'd say somewhere between 20 and 50 is a good number. If you can find more than 50 good references, you'll really impress the external examiner.

*Which papers are important?* When you're trying to figure out which papers are the central ones, a good trick is to look at their citation count (for example in Google Scholar). Highly cited papers are usually important in their field. You can also look at the authors. Authors of good papers are usually good scientists with lots of good papers.

*Expanding the list of relevant papers.*Your can expand the world of your 1-3 central papersby looking at the papers that those central papers are citing. The cited papers contain the work that inspired those, so that's probably going to be interesting to your research. And you can expand further by looking at the papers that your new set of papers are citing and so on.

You can also expand your search by checking which papers *are citing your papers*. Or central papers in the field. Try a keyword search in Google Scholar.

Sometimes wikipedia articles will cite papers. It's better to cite those papers than the wikipedia article.

### Tip 4: The research process is confusing and that's OK

How you think Science works is wrong. The video below explains how it really works. Watch it - and it will make you feel better.

https://www.youtube.com/watch?v=F1U26PLiXjM

There's more on the same topic in [this article](https://dl.dropboxusercontent.com/u/153071/teaching/importance_of_stupidity.pdf).

The page is not about the *topic* of your thesis - it's not about the *research process*. And about all of the stuff surrounding that research. How to write, what should be included, that kind of thing.

### Tip 5: How to structure of your Thesis

There are many ways to structure a thesis, but I personally like a kind of story-telling format.

- You start with an **Introduction** that introduces the topic of your project.
- The you include a **Literature review**, that give an overview of the work what other people have done related to your topic.
- If you have an interesting dataset, then it's natural to have a **Data** section that explains your dataset + provides basic stats about it.
- Then, when you start your analysis, you devote a chapter to each part of your analysis (that can be a single chapter or many, depending on your particular thesis). Each part should have the following structure
  - Introduce the problem/challenge you're trying to solve
  - Introduce the theory needed to tackle this challenge
  - Analyze your data using the theory
  - Present your results / findings.
- Once you're done your wrap everything up with a **Conclusion**. The conclusion should summarize your most important findings. It should comment on your results, explain what those results mean, interpret the results in a wider context. You may also indicate which results were expected or unexpected, and provide an explanation for the unexpected results. It's also a good idea to have a sub-part that deal with limitations, outlook, etc.

If you don't like the organization above, you can consider a more traditional structure.

- *Introduction*
- *Literature review*
- *Dataset*
- *Methods* (Describe the tools you've used)
- *Results* (Tell us what you have found)
- *Discussion*
- *Conclusion*

If you want to read more about structuring your report this way, I think [this page](https://student.unsw.edu.au/thesis-structure) is pretty good.

### Tip 6: Use the structure of Academic Writing

Unless you’re a great writer (in which case you don’t have to follow any rules), the structure of academic text is the following:

- First you tell your readers what you’re about to tell them.
- Then you tell the readers the thing you want to tell them.
- Finally you tell them what you’ve just told them.

This structure works on a number of levels in a thesis.

On the level of the entire thesis, the introduction tells the reader what’s going to happen in the text and the conclusion summarizes what just happened, while the chapters in between contain the actual work.

But for each chapter, you should also put an introduction and conclusion around the content, and similarly for each section. Even within each subsection, it might be good idea to start with a introductory sentence or two (setting the stage) and wrapping up. You have to stop before it gets too pedantic, but I hope the point gets across. It’s not exactly fractal, but almost.

### Tip 7: Figure captions

Figure captions are important. They should ***not*** just be a short string describing the figure (e.g. "Distribution of X."). Each caption should - at a minimum - describe in words what you see in the figure and (even) perhaps also what the reader should notice about the figure, what they can learn from the figure. It's OK to have some overlap between the main text and the figure (in case you also describe some of these things in the text).

For examples of great figure captions, check out this [PhD Thesis](http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/5124/pdf/imm5124.pdf).

### Tip 8: Active versus Passive Voice

Former teachers may have instructed you to use passive voice. That is wrong.

Use [active voice](http://www.biomedicaleditor.com/active-voice.html).

### Tip 9: Use a relatively formal tone

You should aim for clarity when you're writing, and make sure you keep the tone more formal than I do in this blog post. Use "do not" instead of "don't", "we are" instead of "we're" and so one. Take a look at examples of other scientific writing (papers) to get a sense of the right tone.

### Tip 10: Use LaTeX and BibTeX

I don't want to dictate what tools you should use to write your thesis, but you should probably use LaTeX for writing and BibTeX for your bibliography. Why, you ask?

*LaTeX*: The main reason to use LaTex is that it works really well for large documents with many figures and equations. MS Word, Pages, or OpenOffice probably work great for short documents, but when you get beyond 40 pages with lots of figures, things can get shaky. Not with LaTeX. LaTeX helps you structure your work, it handles references to other parts of the thesis as well as citations in a beautiful way. And also the typesetting is professional grade. Read more [here](http://www.andy-roberts.net/writing/latex/benefits).

I learned how to use LaTeX from *[The not so short introduction to LaTeX](http://tug.ctan.org/info/lshort/english/lshort.pdf)*, but there might be better options out there these days.

*[BibTeX](http://www.bibtex.org/)*: You also have to organize all the papers you've read while writing your thesis. BibTeX is how LaTeX manages references. It will seem cumbersome at first, but compared to typing in each single reference manually with the right formatting, BibTeX is easy to use. Start finding a BibTeX entry for all the papers you read (you can [get them via Google Scholar](http://texblog.org/2014/04/22/using-google-scholar-to-download-bibtex-citations/)) and adding them to your .bib file. You will thank me later.

*Exercise*: Find your own BibTeX tutorial (I can't remember how I learned it).

## Putting this together

So how do we combine these 10 tips into a coherent whole? Typically we evaluate theses according to the quality of the following aspects of the thesis.

- Scope and goals
- Command of the overall topic
- Methods
- Conclusion
- Presentation and language

Below, I explain what a good thesis does for each of these aspects, so you have something to aim for.

### An overview

In an excellent thesis, you should aim to show your:

**Scope & goals.** Early in the thesis (e.g. in the introduction), define your research scope (what are you setting out to do, what are you not setting out to do). Present those goals clearly. They should be attainable but high. Important trick: Once you're all done with your research, go back to the introduction and make sure scope still fits with the work you actually did :)

**Command of the overall topic.** You will need to show that you understand how your work fits into the bigger picture.  
Make sure that the papers you cite have been selected not only appropriately but critically (e.g. don't site random web page as a reference for your machine learning). And cite more than a just few papers. A good list of references contains your key papers as well as the important papers in the field (more on this below).

When evaluating a thesis, we want you to show us that you can read scientific papers and find the relevant ones for the topic you're studying.

Oh, and the papers should not just be relevant, they should also be the right ones: from high-quality scientific publications (journals or other refereed forums), not the scribblings of a crazy hermit with twitter handle @theconspiracyistrue. One good trick is that good papers typically have a lot of citations on Google Scholar. And do consider how your results fit into prior research and theories on the topic. That way you can show that you have a deep understanding of the research topic.

**Methods.** When you write about the techniques you use, the overall goal here is to demonstrate command of the relevant research methods. Specifically argue why the methods you are using are right for your problem. Do that by explaining your reasons for using those those methods.

As I stated above, remember that the point of a thesis is to report the research process including the methods you have used accurately and precisely. An important part of that is to justify the choices you have made.

A good way to think about the level of detail is that someone else should be able to pick up your thesis and reproduce your work.

**Conclusion.** When you get beyond the methods, and you have some results, make sure that the line of reasoning behind the conclusions is clear, accurate and critical and supports the points you're making. This is how we can see that you have gained a deep understanding of the topic.

**Presentation and language.** The appearance, presentation and language of the thesis should be impeccable.

Presentation is the easy part, which ANYONE can do. So take great care that this is in order. Make sure everything is spelled correctly and formatted nicely.

Nothing signals poor work more strongly that if you couldn't even make the effort to present stuff nicely. Even if your scientific work is Nobel-prize level, you'll be starting out at a serious disadvantage in the mind of the external examiner (and me) if the presentation is sloppily done.

And if you're not good at english, find a friend who can help you. And start looking early - it can be difficult to find someone last-minute.)

**Contribution to overall scientific knowledge.** It is not necessary for the thesis to contribute to new scientific knowledge. So don't worry if you don't produce an amazing new scientific result.

## And when you get to the exam

You should read [this friendly how-to on taking M.Sc. Exams in my group](http://sunelehmann.com/masters-defence-notes/).
