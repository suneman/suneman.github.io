---
title: "Featured publications"
slug: "featured-publications"
status: publish
---

You can find all my publications on my [Google Scholar profile](https://scholar.google.com/citations?user=wvkUbiUAAAAJ). The handful below is shorter and more selective — papers I'm particularly proud of, with a few words on what they're about and why they ended up mattering.

---

### Using sequences of life-events to predict human lives

**Savcisens, Eliassi-Rad, Hansen, Mortensen, Lilleholt, Rogers, Zettler, Lehmann.** *Nature Computational Science*, 2024.
[life2vec.dk](https://life2vec.dk/) · [Nature Computational Science](https://www.nature.com/natcomputsci/)

We took the sequence of events in a Danish person's life — every job, hospital visit, change of address, relationship — and treated it as something like a sentence in a language model. A transformer trained on these sequences learned representations of human lives that capture deep structure: relationships between education, health, employment, and many other dimensions, and the ability to predict future events. The work was led by my brilliant PhD student Germans Savcisens. It also generated the largest wave of press I've ever experienced — much of it sensationalising the model as a "death predictor," which it is not. We built [life2vec.dk](https://life2vec.dk/) to set the record straight. The paper is about the deep structure of human experience; the boundary between *understanding* and *surveillance* is a line I care a great deal about getting right.

---

### Task-specific information outperforms surveillance-style big data in predictive analytics

**Bjerre-Nielsen, Kassarnig, Lassen, Lehmann.** *PNAS*, 2021.
[doi.org/10.1073/pnas.2020258118](https://doi.org/10.1073/pnas.2020258118)

We had spent years collecting fine-grained behavioural data from a thousand DTU students — Bluetooth proximity, communication, mobility, app use — and we wanted to know: does all of this help predict academic performance better than a transcript? It does not. Past grades, the dullest possible feature, beat the rich behavioural signal across every model we tried. The lesson, which I find deeply important, is that for a great many practical applications we should think carefully about whether we actually need to collect this kind of data at all. Right data beats big data. It's an argument for privacy, for parsimony, and for being honest about what we're learning.

---

### The scales of human mobility

**Alessandretti, Aslak, Lehmann.** *Nature*, 2020.
[doi.org/10.1038/s41586-020-2909-1](https://doi.org/10.1038/s41586-020-2909-1)

Where do you go in a typical week? In a typical year? With Laura Alessandretti and Ulf Aslak, we showed that human mobility is organised as a clean nested hierarchy of spatial scales — from the daily neighbourhood routine up through the city, the region, and long-distance travel — and that this structure is remarkably consistent across individuals and datasets. The hierarchy is universal even though the *content* of any one person's mobility is unique. There's something satisfying about discovering that the way you and I move through the world has the same mathematical skeleton, even when our days look nothing alike.

---

### Accelerating dynamics of collective attention

**Lorenz-Spreen, Mønsted, Hövel, Lehmann.** *Nature Communications*, 2019.
[doi.org/10.1038/s41467-019-09311-w](https://doi.org/10.1038/s41467-019-09311-w)

Many people feel that the world is moving faster — that things go viral and disappear before you've even heard about them. We measured it. Across Twitter hashtags, Google Books, movie ticket sales, Reddit, citations, and more, the window of collective attention has been shrinking for decades. Topics rise faster, peak higher, and fall away sooner. Chaucer's nine-day wonder is now a six-hour wonder. The paper later got swept into the public conversation around Johann Hari's *Stolen Focus* — a useful lesson in the difference between careful academic findings and the shape they take once they're loose in the discourse. The result still holds, and I still think it tells us something important about the information systems we have built.

---

### Evidence for a conserved quantity in human mobility

**Alessandretti, Sapiezynski, Sekara, Lehmann, Baronchelli.** *Nature Human Behaviour*, 2018.
[doi.org/10.1038/s41562-018-0364-x](https://doi.org/10.1038/s41562-018-0364-x)

People maintain a roughly constant number of regularly visited places — about 25 — across their lives. When you adopt a new gym, café, or favourite bar, you tend to drop an old one. The set churns, but the size doesn't grow. It's a kind of Dunbar's number for places: a finite social-spatial capacity that we manage rather than expand. I find this one quietly striking. We assume our relationship to place accumulates over time; in fact, it reshuffles.

---

### The chaperone effect in scientific publishing

**Sekara, Deville, Ahnert, Barabási, Sinatra, Lehmann.** *PNAS*, 2018.
[doi.org/10.1073/pnas.1800471115](https://doi.org/10.1073/pnas.1800471115)

How does a young scientist break into a top journal for the first time? Almost always, with an experienced co-author who has already published there. We named this the "chaperone effect" and traced its outline across millions of papers. It points to a mentorship structure quietly embedded in the publication system — usually invisible, occasionally exclusionary, sometimes generative. As someone who has now chaperoned a fair number of first papers myself, I find it equal parts fascinating and humbling.

---

### Evidence of complex contagion of information in social media: an experiment using Twitter bots

**Mønsted, Sapieżyński, Ferrara, Lehmann.** *PLOS One*, 2017.
[doi.org/10.1371/journal.pone.0184148](https://doi.org/10.1371/journal.pone.0184148)

Information was long modelled as a kind of disease: one exposure is enough to "infect" you. Social influence, it turns out, is more interesting than that. With Bjarke Mønsted and collaborators, we deployed Twitter bots in a carefully controlled experiment, varying how many independent sources each user heard a piece of content from. People were significantly more likely to share when they'd heard about something from multiple sources — a clean experimental demonstration of complex contagion in the wild. The paper won the IC2S2 best-paper award in 2018 and remains one of the cleaner field experiments on social influence.

---

### The fundamental structures of dynamic social networks

**Sekara, Stopczynski, Lehmann.** *PNAS*, 2016.
[doi.org/10.1073/pnas.1602803113](https://doi.org/10.1073/pnas.1602803113)

What does a social network actually look like when you measure it minute by minute, instead of as a static snapshot of friends? Drawing on the high-resolution Bluetooth and proximity data from the Copenhagen Networks Study, we showed that human social interaction is organised around a small number of stable "gatherings" — recurring meetings of the same people in the same configurations — superimposed on a churn of more transient encounters. The gatherings are the load-bearing structure of a social life. The transient stuff is where most of the noise lives.

---

### Measuring large-scale social networks with high resolution

**Stopczynski, Sekara, Sapiezynski, Cuttone, Larsen, Lehmann.** *PLOS One*, 2014.
[doi.org/10.1371/journal.pone.0095978](https://doi.org/10.1371/journal.pone.0095978)

The methodological paper behind the Copenhagen Networks Study. We equipped over a thousand DTU students with instrumented smartphones recording Bluetooth proximity, communication, GPS traces, and more — at five-minute resolution, for years at a time. The paper documents how we did it: the hardware, the data pipeline, the privacy architecture, the ethics review. Flashing custom firmware onto a thousand phones in the basement of DTU in 2013 remains one of my fondest, most exhausting memories. The dataset has since underpinned dozens of papers across the group on friendship, mobility, sleep, and contagion. None of it would exist without this paper.

---

### Link communities reveal multiscale complexity in networks

**Ahn, Bagrow, Lehmann.** *Nature*, 2010.
[doi.org/10.1038/nature09182](https://doi.org/10.1038/nature09182)

The paper that put me on the map. With Yong-Yeol Ahn and Jim Bagrow, we proposed an inversion of how community detection had been framed: instead of asking which group each node belongs to, ask which group each *link* belongs to. The shift turns out to be enormous. Real people belong to many overlapping communities — family, work, college friends, neighbours — and a node-based clustering forces you to choose. A link-based clustering doesn't. Your relationship with your sister sits in "family"; your relationship with your colleague sits in "work"; *you* sit at the intersection. The method has been applied across biology, social science, and information science, and I think the reason it stuck is that it captures something true about how the social world is actually organised.
