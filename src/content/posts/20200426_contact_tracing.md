---
title: "Contact Tracing"
date: 2020-04-26 11:56:33
slug: "contact-tracing"
status: publish
author: "sunelehmann"
categories: ["Misc"]
original_url: "https://sunelehmann.com/2020/04/26/contact-tracing/"
images: ["/assets/20200426_contact_tracing/screenshot-2020-04-26-11.24.21.png", "/assets/20200426_contact_tracing/screenshot-2020-04-26-11.17.33.png"]
---

**Update May 23rd**. Final update for this post. I'm happy to report that the Danish government - in part based on input from our advisory board - has decided to base the Danish contact tracing app on the DP-3T (as implemented by Google and Apple) framework. Details here https://www.sum.dk/Aktuelt/Nyheder/Coronavirus/2020/Maj/Politisk-aftale-om-frivillig-smittesporingsapp-for-covid-19.aspx

**Update May 1st**. Here's another update. It also turns out the advisory board wasn't officially announced until today. I hope the unintended embargo-breaking below won't have any serious consequences. Here's the official press release: <https://digst.dk/nyheder/nyhedsarkiv/2020/maj/nyt-advisory-board-skal-raadgive-myndighederne-om-den-kommende-danske-smittestops-app/> see also [here](http://sum.dk/Aktuelt/Nyheder/Coronavirus/2020/Maj/Smittestop-app.aspx).

**Update: April 27th, 2020.** *Well, it turns out I was wrong about Reason 1 below. And that I have lousy timing in writing blogposts with declarations in them.*

*Pretty much right after finishing the post below (original post was written on April 26th), I was invited to be a member of a newly established Advisory Board for the officialDanish Contact Tracing App. The goal of the advisory board is to provide advice/feedback for the Agency for Digitization and the Ministry of Health regarding the App.*

*Since I care a lot about doing digital contact tracing in the right way (with respect to privacy & epidemiological relevance), I accepted the offer to join. Clearly that changes some aspects of what I've written below.*

Over the past few weeks, I've commented on contact tracing in the Danish press. But starting today, I am going to stop chiming in on this topic.

Reason 1 is that I don't feel like I'm making much of an impact in terms of where the official app is going (which was my main reason to start speaking about this in the first place). Reason 2 is that the news on this topic are moving fast and staying updated is exhausting. Reason 3 is that engagement in this topic is drawing me away from the deep & long-term work that I want to be focusing on. And finally, Reason 4 is that contact tracing connects deeply to projects I did years ago, so it feels a bit removed from my current core scientific work of network science and mobility modeling. Thus, I'll be doing my best to pipe down from now on.

If you want updated info about contact tracing in Denmark, I recommend checking out [Henrik Moltke's twitter feed](https://twitter.com/moltke). For the overall (epidemiology and privacy) view on contact tracing, I personally follow [Marcel Salathe at EPFL](https://twitter.com/marcelsalathe).

Here are my two key points on contact tracing:

- A decentralized protocol (such as DP-3T) is the best way to do things.
- Contact tracing is not necessarily the best way to counteract spread of COVID-19. (For example: Re-focusing all the resources we're currently using on building apps towards getting everyone to wear masks, might very well be a better strategy.)

Below, I provide some context on each of these points, referring back to what I've already said in the press.

## Privacy preserving contact tracing

In the beginning of the epidemic, I supported (and made a small contribution to) the PEPP-PT initiative, which was then more of an umbrella organization, also including DP-3T. See [this press release](https://www.dtu.dk/english/news/2020/04/ny-app-skal-afdaekke-smittekaeder?id=4eaab1c6-ccc5-4c29-ac99-22e126d4555c) from DTU. At some point there was an internal argument (which I know nothing about), resulting in a split into a centralized (still privacy preserving) paradigm embodied by PEPP-PT and a decentralized paradigm represented by DP-3T and also incorporated in the Apple/Google solution to contact tracing.

I have provided continuous updates on my attitude towards this issue via Twitter. See below

![](/assets/20200426_contact_tracing/screenshot-2020-04-26-11.24.21.png)

I'm placing an image instead of embedding the tweets because I can't figure out how to display the thread. Link here <https://twitter.com/suneman/status/1251101267956502531>

![](/assets/20200426_contact_tracing/screenshot-2020-04-26-11.17.33.png)

Again, I'm putting an image here instead of an imbed - since I can't figure out how to embed the thread. But you can find it here: <https://twitter.com/karmel80/status/1253256268283891713>

Here's a [link to a nice report on issues with centralized solution used in PEPP-PT](https://github.com/DP-3T/documents/blob/master/Security%20analysis/PEPP-PT_%20Data%20Protection%20Architechture%20-%20Security%20and%20privacy%20analysis.pdf). This report, written by members of the DP-3Tproject, came out shortly after PEPP-PT finally provided open source code.

## Is contact tracing using cellphones even a good idea?

An important point to make when it comes to contact tracing is that it might not be a very good solution. Many of the issues are discussed in [this Twitter thread](https://twitter.com/vedransekara/status/1251160367801094144) by UNICEF Machine Learning Lead & Principal Researcher Vedran Sekara.

I've also talked about these issues in the Danish Press.

- *Version2* (April 20th, 2020): [DTU-professor advarer: Lad være at forvente for meget af corona-apps](https://www.version2.dk/artikel/dtu-professor-advarer-lad-vaere-at-forvente-meget-corona-apps-1090441). This article provides has details on potential technical issues related to how we convert info on Bluetooth scans to an understanding of epidemiological interactions.
- *Information* (April 18th, 2020): [Apple og Google lancerer værktøj, som vil kunne spore spredning af COVID-19](http://Eksperter er ikke specielt bekymrede for vores privatliv https://www.information.dk/indland/2020/04/apple-google-lancerer-vaerktoej-spore-spredning-covid-19-eksperter-specielt-bekymrede-vores-privatliv). Here, I discuss the Google/Apple solution and how we leak data in many different contexts.
- *Weekendavisen* (April 3rd, 2020): [Fagre nye færden](https://www.weekendavisen.dk/2020-14/samfund/fagre-nye-faerden). Talks about surveillance more generally.
