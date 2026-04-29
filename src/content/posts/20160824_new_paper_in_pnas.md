---
title: "New paper in PNAS!"
date: 2016-08-24 21:55:15
slug: "new-paper-in-pnas"
status: publish
author: "sunelehmann"
categories: ["Misc"]
original_url: "https://sunelehmann.com/2016/08/24/new-paper-in-pnas/"
images: ["/assets/20160824_new_paper_in_pnas/screenshot-2016-09-06-19-43-09.png", "/assets/20160824_new_paper_in_pnas/screenshot-2016-08-25-12-59-19.png", "/assets/20160824_new_paper_in_pnas/wikipedia-svg.png", "/assets/20160824_new_paper_in_pnas/screenshot-2016-08-24-14-29-48.png", "/assets/20160824_new_paper_in_pnas/screenshot-2016-08-24-14-33-59.png", "/assets/20160824_new_paper_in_pnas/screenshot-2016-08-24-21-25-11.png", "/assets/20160824_new_paper_in_pnas/screenshot-2016-08-25-09-21-56.png", "/assets/20160824_new_paper_in_pnas/screenshot-2016-08-25-09-22-13.png"]
---

I'm super excited to announce that we recently had a new paper published in PNAS. And by 'we' I mean my former PhD Student [Vedran Sekara](https://vedransekara.github.io/) (first author), my former PostDoc [Arek Stopczynski](https://stopczynski.com/), along with yours truly.
![screenshot-2016-09-06-19-43-09](/assets/20160824_new_paper_in_pnas/screenshot-2016-09-06-19-43-09.png)

Figure 0: [Update Sept 6th, 2016] Extra excited that we made the cover of the printed version!

You can download the whole thing by [clicking right here](http://www.pnas.org/content/early/2016/08/22/1602803113.abstract). In addition to the paper itself, PNAS published a nice commentary on the paper [written by Renaud Lambiotte](http://www.pnas.org/content/early/2016/08/22/1612364113.extract) [although that one is behind a paywall].
I'm very proud of the work we've done, and somehow we got away with giving the paper the not-so-humble title *Fundamental Structures of Dynamic Social Networks.*The cool thing is that even though the title is perhaps ostentatious, I actually think that we're on to something fundamental here. I've attempted to write a non-technical explanation below.

## Prologue: The connection to communities

Community detection is a big deal in network science. Just look at this plot I created that shows the number of papers about [community detection](https://en.wikipedia.org/wiki/Community_structure) per year.
![Screenshot 2016-08-25 12.59.19](/assets/20160824_new_paper_in_pnas/screenshot-2016-08-25-12-59-19.png)

Figure 1: Number of papers of community detection published per year, based on data from Google Scholar [1].

There are literally ***thousands of papers*** that address the topic of finding communities in networks published every single year, so in my world this is an important topic. Detecting communities in complex networks is usually all about finding groups of nodes with many links between then - and only few links to the rest of the network. The typical example network in a community detection paper looks something like this:
![wikipedia.svg](/assets/20160824_new_paper_in_pnas/wikipedia-svg.png)

Figure 2: A sketch of the communities world-view that YY, Jim, and I argued against in our 2010 paper in Nature. Illustration from wikipedia [2]

Back in 2010, [YY Ahn](http://yongyeol.com), [Jim Bagrow](http://bagrow.com) and I [wrote a paper](http://www.nature.com/nature/journal/v466/n7307/abs/nature09182.html) where we argue that there's something fundamentally wrong with this idea of communities. The problem is that the illustration above assumes that each node is a member of only *one single community*. In that paper we argue that this assumption is often wrong. In most networks, each node is a member of more than one community. In social networks, for example, we are in communities of friends, family, co-workers, sports buddies, etc.
When each node is a member of many communities, the global picture gets more messy. The network doesn't fall apart into neat chunks as above, rather it looks like a mess of a hairball. [I've written a popular explanation of those findings [here](https://sunelehmann.com/2010/03/23/worlds_colliding/) plus a follow-up [here](https://sunelehmann.com/2010/06/29/pervasive-overlap/).] The hairball below shows a real social network from the PNAS paper.
![Screenshot 2016-08-24 14.29.48](/assets/20160824_new_paper_in_pnas/screenshot-2016-08-24-14-29-48.png)

Figure 3: The hairball.

Back then, we did not have access to temporal information, but as part of trying to wrap our brains around how this hairball arises, Jim, YY, and I came up with the picture below (Jim actually drew it and impressively figured out how to do the perspective). This illustration - as we shall see below - turned out to be quite prophetic.
![Screenshot 2016-08-24 14.33.59.png](/assets/20160824_new_paper_in_pnas/screenshot-2016-08-24-14-33-59.png)

Figure 4: An early sketch Jim, YY, and I came up with in order to understand how the hairball arises from simple, but overlapping communities.

The illustration shows that when single individuals (marked in green and turquoise) participate in multiple communities the underlying simplicity is obscured in the aggregated network.

## Gatherings

I had forgotten all about communities when my graduate student Vedran and I started looking at the incredible detailed data my group had just started collecting as part of the [Copenhagen Networks Study](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0095978) (CNS). CNS contains 2.5 years of data collected by handing out 1000 smartphones to nearly all the DTU freshman students, collecting physical proximity data (using Bluetooth to measure the distance between pairs of individuals), phone calls, text messages, Facebook interactions, as well as GPS data. All of this with high temporal resolution (e.g. we recorded face-to-face meetings every 5 minutes)
Working as lead hacker-in-residence on top of his data science duties, Arek used a mix of 26-hour days & what I can only describe as pure black magic to start almost from scratch and orchestrate the software infrastructure needed to collect and store all of these data sources in something like six months.With CNS we finally had access to the temporal networks dataset needed to dig deeper.
When we looked at the physical proximity data we noticed that, as we considered finer and finer time resolution, the hair-ball (beautifully) dissolved into meaningful structures.
![Screenshot 2016-08-24 21.25.11](/assets/20160824_new_paper_in_pnas/screenshot-2016-08-24-21-25-11.png)

Figure 5: At the right temporal resolution (blue network), we can observe communities directly, no community detection needed. The green network shows interactions aggregated over one day. The orange network shows interactions aggregated over 1 hour, and the blue network is a single 5-minute timeslice.

The green hairball shows everyone who has spent time together across an entire day. The orange network shows physical contacts aggregated over an hour, and the blue network shows the interactions for a five-minute time slice. The exciting thing is that in the blue network, ***we can directly observe the groups of people hanging out together***. No community detection necessary - we had solved that question those thousands of papers in Figure 1 are addressing, simply by changing the temporal resolution [3]. Said differently we've just identified a case where understanding the network got ***easier by adding more data (***That's why Renaud's commentary is called "Rich Gets Simpler").
Usually it's the opposite. Things usually get a lot more complex when we have to account for more data. Just check any paper on temporal networks (for example take a look at [this excellent review](http://www.sciencedirect.com/science/article/pii/S0370157312000841)). I take the fact that more data has simplified the problem to mean that we're on to something: that we're looking at the network represented at the right temporal resolution.
Anyway. We'd just found out how to identify all of the little communities in a timeslice. Now we needed to put the pieces together again. But since we'd figured out the underlying simple principle, we began to study how meetings between people develop over time - simply by matching up groups between neighboring timeslices.
The result is ***gatherings***- the temporal representation of a meeting between a group of individuals that can last anywhere from 15 mins to several hours.
We have [a great visualization](https://ulfaslak.com/portfolio/Visualisation/) (with accompanying explainer-video, embedded below) that beautifully describes what gatherings are and how they work. Check out the video, it's only 90 seconds long.
https://www.youtube.com/watch?v=YpBkH\_0jq2g
The visualization was created by Ulf Aslak Jensen, a newly started PhD student in my group. *And it is officially awesome*: earlier this year it won *Science* Magazine's [Data Stories Competition](http://www.sciencemag.org/projects/data-stories/winners)!

## Cores

But, while they're already great and exciting,  gatherings are only the beginning of the story. If a group of people have a real social connection, they meet again and again. We call gatherings that occur repeatedly, ***cores**.*It is the cores that are the 'fundamental structures' that organize/simplify the dynamics we observe on the network. Let's dig deeper.
First, let's think about what the network looks like from the perspective of a single node. Below, we show an example from a real (and representative) individual.
![Screenshot 2016-08-25 09.21.56](/assets/20160824_new_paper_in_pnas/screenshot-2016-08-25-09-21-56.png)

Figure 6: The cores in which a single node participates. Each cores is highlighted using a brightly colored background. Note how cores can be overlapping and nested.

## 

Instead of modeling each and every interaction in the network, we now have a framework that allows us to think about a node's social activity in a different way. We are able to think about the node as participating in a *sequence of gatherings*, where each gathering is an instance of a core.
The node pictured above is a member of 9 cores, each of which has gathered multiple times. If we plot *when in time* each core is active, it looks like this:
![Screenshot 2016-08-25 09.22.13](/assets/20160824_new_paper_in_pnas/screenshot-2016-08-25-09-22-13.png)

Figure 7: How the central, red node from Figure 6 participates in gatherings over time. The x-axis shows time, with light-gray vertical bars corresponding to weekends and dark-gray vertical bars shows holidays. Each horizontal row corresponds to a core, and each time that core is active, we highlight the corresponding timeslot. Colors match Figure 6.

We call this pattern of interactions a person's *social trajectory*, because we can think of the person's journey through the network as jumping from core to core - from social context to social context.
It is a massive simplification of the hairball from Figure 3. And it is this simplification - the fact that we are now able to think about dynamic social network in terms of cores and their activations - that I think is the paper's main contribution.
(Plus, having seen how the cores work, I hope it's clear why I said that Figure 4 turned out to be a nice representation of what's actually happening in real networks. )

## Applications

In the paper we also spend quite a bit of time showing how this simplification is, in fact, useful for a number of purposes. But since this post is probably already a bit **tl;dr** I'll save a detailed description of those results for another day. But I'll summarize them here.
**Firstly**, we show that we can use cores to predict where people will be in the future. The idea is simple. A core is a 'real' object in the network in the sense that when we see a gathering, *all of its members must be present.* This means that observing a part of a core is a signal that soon we'll soon see the remaining members.
In the paper we look at cores of size three and show how a sighting of two core members signals the arrival of the third group member.
**Secondly**, we realized that social trajectories have a lot in common with spatial trajectories. Spatial trajectories describe how we move from location to location. From 'home' to 'work 'to 'supermarket', etc.
The fact that we move through social contexts (cores) just like we move through physical space opens an interesting connection to work on human mobility. Specifically, we connect the work on cores to a seminal paper on *[Limits of Predictability in Human Mobility](http://science.sciencemag.org/content/327/5968/1018),*which showed that for most people, given a sequence of past locations, the next location can be predicted with high accuracy [4].
We find a similar level of predictability given social trajectories, as well as an interesting interplay between the social and geo-spatial predictability (when people are highly unpredictable wrt. their location, they tend to be highly predictable wrt. their social context).

## Rounding up

There is much more in the actual paper. For example, we talk about how the cores leave traces in other communication channels. And the paper also contains the technical details (although a lot of them are contained in the massive Supporting Information document). I will write more about the predictability results in a later post (since those findings are actually pretty cool as well).
In summary, I hope that I've managed to give you a sense of the paper's central contribution - and perhaps also provided a bit more of an explicit link to the literature (including my own past research) than is readily available from the paper.

## Notes

[1] The data was retrieved using the following Google Scholar search query: (“complex network” OR “complex networks” OR “network data”) AND (“community detection” OR “community assignment” OR “network community” OR “network communities” OR “community finding”). The idea for that query comes form Conrad Lee.
[2] I grabbed this illustration from wikipedia. It's by j\_ham3 - Own work. Licensed under Creative Commonse BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=17125894.
[3] I'm exaggerating a little bit for effect here. The approach we're discussing only works for systems where people are actually meeting face-to-face. Community detection in phone call networks or Facebook is a different story.
[4] It's a little bit confusing because we're talking about two distinct kinds of predictability. The predictability related to a sequence of location/social contexts has to do with to the amount of routine in someone's behavior.
