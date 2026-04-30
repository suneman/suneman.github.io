---
title: "Mood, twitter, and the new shape of America"
date: 2010-07-13 15:21:35
slug: "mood-twitter-and-the-new-shape-of-america"
status: publish
author: "sunelehmann"
categories: ["Misc", "Work"]
tags: ["visualization"]
original_url: "https://sunelehmann.com/2010/07/13/mood-twitter-and-the-new-shape-of-america/"
---

Twitter is a gigantic repository for our collective state of mind.
Every second, thousands of tweets reveal what everybody [and their mother](http://tweepml.org/Mothers/) [had for lunch](http://twitter.com/Mickey__Rourke/status/18348383163), what [Justin Bieber](http://en.wikipedia.org/wiki/Justin_Bieber) is up to, or what [magnificent link you should be checking out](http://twitter.com/suneman) right now. Individually, each tweet is mostly interesting to friends/fans of the tweeter, but taken together they add up to something more.
In analogy to individual neurons firing together to add up to the human consciousness, the billions of tweets have meaningful macro-states that contain information about the whole system rather than the individual tweeters. But we need to do a little data mining to extract meaningful information about these states, to expose our collective states of mind.
As a proof-of-concept we've1 been studying the mood2 of all of the public tweets. While there are many services that will allow you to study the [mood of your own tweets](http://tweetmood.info/) ([and also an neat little DIY project to show you the global average of twitter](http://www.instructables.com/id/Twitter-Mood-Light-The-Worlds-Mood-in-a-Box/)), much less effort has gone into studying how the mood breaks down according to geography. Below, I show a brand new video displaying the pulsating 24-hour twitter mood cycle of the United States (I'll explain just what you're looking at, in the following).

<div class="embed embed--youtube"><iframe src="https://www.youtube.com/embed/ujcrJZRSGkg" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>

In the video, green corresponds to a happy mood and red corresponds to a grumpier state of mind. The area of each state is scaled according to the number of tweets originating in that state. Note how the East Coast is consistently 3 hours ahead of the West Coast, so when we're sleeping in Boston, the Californians are tweeting away. It's also interesting that better weather seems to make you happier (or rather, that better weather is correlated with happier tweets): Florida and California seems to be consistently in a better mood than the remaining US. Also note how New Mexico and Delaware behave very differently from their neighbors. Full results, individual maps, and a high-res poster can be found on the dedicated [Twitter Mood website](http://www.ccs.neu.edu/home/amislove/twittermood/).

### How to construct the mood map

Since many twitter users list their location, we've assigned every tweet in our (massive) database to a US county and extracted their mood. This allows us to average over tweets and plot the mood of the US as a function of geography (and time). However, since the US is unevenly populated, the resulting maps are boring since only a few counties (the centers of cities) contain most of the tweets (not too many tweets in [Ellsworth, Nebraska](http://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=nebraska&sll=41.6725,-70.3514&sspn=0.009761,0.017166&ie=UTF8&hq=&hnear=Nebraska&ll=42.057737,-102.277608&spn=0.019405,0.034332&z=15) yet).
Luckily, brilliant people have come up with a cool way of solving this problem using a technique called [density equalizing maps](http://www.pnas.org/content/101/20/7499.abstract)3. (or [cartograms](http://en.wikipedia.org/wiki/Cartogram)) The idea here is simple: warp the map in such a way that certain features of shape are conserved, but in such a way that the (population) density becomes the same everywhere. The resulting maps look like something from an alternate universe and allow us to show the US mood much more clearly.

### Notes

1. The twittermood project members are [Alan Mislove](http://www.ccs.neu.edu/home/amislove/), [YY Ahn](http://yongyeol.com/), [JP Onnela](http://jponnela.com/), Niels Rosenquist, and undersigned.
2. For a deeper explanation of how we evaluate the mood of tweets, see the [Twitter Mood website](http://www.ccs.neu.edu/home/amislove/twittermood/).
3. An easily accessible explanation of the density equalizing maps, is posted on the [Twitter Mood website](http://www.ccs.neu.edu/home/amislove/twittermood/).
