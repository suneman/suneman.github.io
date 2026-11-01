---
title: "New paper: the adaptive cut, sixteen years in the making"
date: 2026-11-01 14:00:00
slug: "adaptive-cut"
status: publish
author: "sunelehmann"
categories: ["Misc"]
images: ["/assets/20261101_adaptive_cut/adaptive_cut_final_hd.png"]
ai_assisted: true
---

I'm excited to announce a new paper in *PNAS Nexus*. The first author is the brilliant [Louis Boucherie](https://louisboucherie.com) and we wrote it with [Yong-Yeol Ahn](http://yongyeol.com/). It's called "Adaptive cut reveals multiscale complexity in networks" [1].

Back in 2010, YY, Jim Bagrow and I published a paper (in *Nature*, no big deal) called "Link communities reveal multiscale complexity in networks" [2]. The idea there was that communities in networks could be defined as groups of related *links*, rather than groups of nodes. You belong to many communities: family, workplace, old college friends, all at once. But your relationship to any one person mostly belongs to just one of those. So if you cluster links instead of people, you find beautiful overlapping communities. 

The paper uses hierarchical clustering of links: compute the similarity between every pair of neighboring links, build a dendrogram, and cut the tree at the level that maximizes a quality measure we called partition density.

The thing we noticed almost immediately after the paper came out was that a *single level* didn't necessarily look like the best way to cut a dendrogram. Real networks have both dense and sparse parts. The communities in dense regions of the network merge near the leaves of the tree and the sparse ones close to the root. When that is the case, no single horizontal line can do them all justice. 

Cut near the leaves and the sparse communities shatter into fragments. Cut near the root and the dense part of the network becomes one big community. So what if the cut could bend? 

We agreed that this was obviously the next thing to do, and then we didn't do it. For sixteen years.[^1]

What finally happened was that Louis visited YY during his PhD exchange, and we thought it would be fun to actually build the thing. It was. We call the result the *adaptive cut*.

## Cutting at more than one height

The adaptive cut lets every branch of the dendrogram be cut at its own height, so the cut can be low where a community is dense and high where it is sparse. 

The problem (as always) is combinatoric. The number of possible multi-level cuts of a tree grows doubly exponentially with its depth. We solve that problem via search. We start from the best single cut (that way the answer can only get better), pick a group at random, and propose a small change: merge it with its sibling branch, or split it further. Changes that increase the partition density are kept. Changes that lower it are sometimes kept anyway, with a probability set by a temperature that cools over the run, we can get out of small local optima.[^2]

![Final frame of the adaptive-cut animation: a block-diagonal adjacency matrix colored by community on the left, a dendrogram with each branch cut at its own height in the middle, and the partition density climbing past the best single cut along the MCMC run at the bottom.](/assets/20261101_adaptive_cut/adaptive_cut_final_hd.png "The adaptive cut on a toy network with communities of varying density. Left: the adjacency matrix, one square per link, colored by community. Right: the link dendrogram, with every branch cut at its own height. Bottom: partition density along the Markov chain, against the best single cut (dashed) and the best adaptive cut we found (dotted). Animation by Louis Boucherie.")

On the toy network above, the best single cut reaches a partition density of 0.29 and the adaptive cut 0.39. On a balanced network, where every community is equally dense, there is nothing to gain, because the best single cut was already the best cut. Which raises the obvious question: can you tell in advance whether your network needs adaptive cuts?

## Balancedness

To answer that, we go back to the thing about networks with regions of different density. We quantify that using a new score we call *balancedness*. At every height of the dendrogram, the branches divide the leaves into groups, and the Shannon entropy of the group size distribution tells you how even that division is. Normalize using the *most even* split possible and the *least even* split, average over all heights, and you get a number between 0 for a caterpillar tree (every split peels off a single leaf) and 1 for a perfectly balanced tree.

We computed the balancedness for 202 real networks. We find that most real dendrograms are unbalanced, and larger networks tend to be more unbalanced than smaller ones. 

The upshot of that is that the single cut we recommended in 2010 was leaving something on the table for most networks. Across the 202 networks, the adaptive cut improves partition density on 195 of them, by 34 percent on average (the median is 21 percent), and the lower the balancedness, the bigger the gain. In that sense, balancedness is a prediction, not just a diagnosis: compute it first (it's not computationally expensive), and you have a decent idea whether the adaptive cut (much more computationally expensive) is worth the trouble.

## And it's actually a general thing

We started from link clustering, but none of what we find is specific to link clustering. Adaptive cuts can be useful in many other places. 

For example we also use an adaptive cut for the Louvain algorithm [3], where it improves modularity, and for plain hierarchical clustering of points, where it manages the classic two-concentric-circles dataset that a single cut cannot separate. Our approach works for anything that produces a dendrogram and has an objective function.

The paper is open access, the code is on [GitHub](https://github.com/LCB0B/adaptive_cut), and Louis has written two interactive posts where you can drag the cut yourself and watch the chain run: one on the [adaptive cut](https://louisboucherie.com/blog/adaptive_cut/) and one on [balancedness](https://louisboucherie.com/blog/balancedness/). 

It may have taken 16 years to get here – but it's still a super exciting paper!


## Notes

[^1]: In our defense, 2010 was a busy year. So, it turns out, were the fifteen that followed.

[^2]: For the connoisseurs: because a move changes the number of clusters, the sampler is a reversible-jump Markov chain Monte Carlo with an asymmetric proposal, and the paper proves detailed balance and ergodicity for it. 

**References**

[1] L. Boucherie, Y.-Y. Ahn and S. Lehmann, "Adaptive cut reveals multiscale complexity in networks," *PNAS Nexus*, pgag344 (2026). <https://doi.org/10.1093/pnasnexus/pgag344>. Preprint: <https://arxiv.org/abs/2512.08741>.

[2] Y.-Y. Ahn, J. P. Bagrow and S. Lehmann, "Link communities reveal multiscale complexity in networks," *Nature* **466**, 761–764 (2010). <https://doi.org/10.1038/nature09182>

[3] V. D. Blondel, J.-L. Guillaume, R. Lambiotte and E. Lefebvre, "Fast unfolding of communities in large networks," *Journal of Statistical Mechanics: Theory and Experiment* **2008**, P10008 (2008). <https://doi.org/10.1088/1742-5468/2008/10/P10008>
