---
title: "Worlds Colliding"
date: 2010-03-23 16:18:48
slug: "worlds_colliding"
status: publish
author: "sunelehmann"
categories: ["Misc"]
original_url: "https://sunelehmann.com/2010/03/23/worlds_colliding/"
images: ["/assets/20100323_worlds_colliding/google_vs_real.jpg"]
---

During a [press conference at last week's SxSW conference](http://lifehacker.com/5493475/what-the-gmail-team-is-working-on), product manager of Google's gmail team, Todd Jackson, revealed an interesting bit of information about the company's [problem-ridden](http://news.bbc.co.uk/2/hi/technology/8517613.stm) new service [Google Buzz](http://www.google.com/buzz):
> Jackson told the crowd, as he's previously said to reporters, that too much was assumed about how Buzz would work best and be received based on Google's internal testing. Google employees didn't have a strong use case for "muting" their fellow Google employees, and the people they'd want to follow and be followed by closely matched up to their contact lists. In general, too, Jackson suggested that Google underestimated the impact of "having a social, public service appear inside ... what is a very private thing (email) for some people [[1]](http://lifehacker.com/5493475/what-the-gmail-team-is-working-on).

So by testing their social service inside a single context (Google employees only), the developers failed to notice that in real life, people participate in *multiple* contexts (family, work, friends, etc) that they work actively to keep separate. The reasons for wanting to keep these groups separate can range from wanting to keep an illicit affair secret from your spouse to political activists in oppressive regimes wanting to keep certain connections secret from the government [[2]](http://news.bbc.co.uk/2/hi/technology/8517613.stm). Another important reason to keep our communities separate, is that we often play different roles - and communicate differently - in different contexts, as illustrated beautifully in the following clip from TV's Seinfeld:

<iframe src="https://www.youtube.com/embed/SxuYdzs4SS8" width="560" height="315" frameborder="0" allowfullscreen></iframe>

So, ironically, the key problem for Buzz, Google's *social network* service was that the engineers at the Googleplex had failed to understand an essential property of real-world social networks. Figure 1 illustrates the problem:![google_vs_real](/assets/20100323_worlds_colliding/google_vs_real.jpg)Figure 1A shows a cartoon version of Google's internal testing situation. It's clear that in this situation, since an individual (the gray node) only belongs to a single social context, sharing contact information with his neighbors reveals no new information to his social network. However, an ego-centered network in the wild looks more like the situation depicted in Figure 1B. Here, the gray node is a member of several communities (nodes with different colors) with very little communication between communities. Now, because people typically manage all of their 'worlds' from their email inbox, what Google did when they created Buzz' automatic friends-lists, was to implicitly link people's worlds, revealing the precisely the information that people work to supress. Sometimes with [serious implications](http://techcrunch.com/2010/02/12/google-buzz-privacy/).
It is interesting to consider what the structure displayed in Figure 1B implies for the full graph. For an individual, the world breaks neatly into a small set of social contexts, but when every single node is in this situation, then the resulting total structure becomes very different from many of the model networks that are currently in use. In my own corner of the complex networks world, this has serious implications for rapidly growing field of *community detection* [3]. Currently, most algorithms are designed to search for densely connected sets of nodes that are weakly connected to the rest of the network, and while some methods do include the possibility of community overlap, most break down if the overlap constitutes more than a small fraction of the number of nodes. If Figure 1B is correct and overlap is present for all nodes, then the idea of communities as weakly connected to the remainder of the network is false -- since communities will have many more links to the outside world than to the inside.
I hope to see more research investigating this problem!
Oh - and [George Costanza](http://en.wikipedia.org/wiki/George_Costanza) gets to have the last word...

<iframe src="https://www.youtube.com/embed/uPG3YMcSvzo" width="560" height="315" frameborder="0" allowfullscreen></iframe>

Update April 3rd, 2010
I've just become aware of a few excellent blog posts that discuss problems related to buzz, drawing on ideas very similar to what I present above. Fred Stutzman writes eloquently about buzz and colliding worlds inspired by Erving Goffman [here](http://fstutzman.com/2010/02/16/what-google-could-learn-from-goffman/). That post sparked [additional 'world-colliding' thoughts](http://) from David Truss (via [this post](http://www.elearnspace.org/blog/2010/02/18/what-google-could-learn-from-goffman/) from George Siemens).
**Note**: This post was originally posted back in 2010 at the now defunct *Complexity and Social Networks Blog* (which was hosted here https://blogs.iq.harvard.edu).
References

- [1] http://lifehacker.com/5493475/what-the-gmail-team-is-working-on
- [2] http://news.bbc.co.uk/2/hi/technology/8517613.stm
- [3] Santo Fortunato. Community detection in graphs. *Physics Reports* **486**:75-174 (2010).
