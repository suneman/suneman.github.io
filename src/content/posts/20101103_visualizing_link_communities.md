---
title: "Visualizing Link Communities"
date: 2010-11-03 05:10:43
slug: "visualizing-link-communities"
status: publish
author: "sunelehmann"
categories: ["Complexity and Social Networks Blog", "Work"]
original_url: "https://sunelehmann.com/2010/11/03/visualizing-link-communities/"
---

When [YY Ahn](http://yongyeol.com/), [Jim Bagrow](http://bagrow.com/), and I published our [paper on communities of links in complex networks](http://www.nature.com/nature/journal/v466/n7307/abs/nature09182.html), we did share the [code](http://barabasilab.neu.edu/projects/linkcommunities/) for the algorithm, but one of the essentials missing from our package was a good way to visualize the highly overlapping link communities.

[![Link-communities Visualization](http://dl.dropbox.com/u/153071/website/link-viz.png)](http://scaledinnovation.com/analytics/communities/comlinks.html)

Thus, I'm delighted to report that Rob Spencer over at [Scaled Innovation](http://scaledinnovation.com/) has done a great job of [visualizing the detected link communities](http://scaledinnovation.com/analytics/communities/comlinks.html) (including a new client-side implementation, I might add). The technical details are interesting and available.

The example displayed above is lifted from Scaled Innovation and shows the network of characters in *The Wizard of Oz*. In addition to the central visualization reproduced above (see below for details),  the page also shows the full link dendrogram and many other treats; everything is beautifully crafted. Note the community assignment matrix on the right, which is a neat way of probing the issue of nested communities. On the page, Rob has a number of interesting observations regarding visualization of the link communities and explains the layout above in further detail. I quote:

> The good news is that the ABL method is powerful and flexible. The challenge is that the communities it reveals are of links, not nodes, and therefore not as obvious to portray and interpret. So far the literature method is to use a traditional force-based network diagram and color the lines between the dots, rather than color the dots. Not bad, but this has the limitations of force-directed network diagrams have always had: a big "wow factor" but of limited practical interpretive use because of the spaghetti of crossing lines. So here you'll find outright experiments, and that means that some will be different!
>
> In the upper circular graph the dots are the nodes and the polygons show community membership of those nodes (the colors match the table and dendrogram); line crossing is minimized by working around in cluster-joining order (same as the ROYGBIV color order). Communities are equally distributed around the circle with anchor points shown as black-centered dots; each node is placed as the weighted sum of its coordinates of each anchor to which it belongs, plus some random jitter to separate nodes with single community membership. The community ordering and coloring has an interesting result: the diagram gets simpler to see as the number of communities is increased, even far above the partition density "optimum".
> The method is fast because it's completely deterministic and drawn in one pass, i.e. it's not an iterative force-relaxation method.

### Pervasive overlap and visualizations

While Rob's visualization shows tremendous progress on a number of fronts (just compare it to [our own - primitive - first stab at visualizing](http://barabasilab.neu.edu/projects/linkcommunities/LinkClusteringFlex.swf) the network of characters in *Les Miserables*), I still think that node based visualizations of the link communities work best when we study ego-networks (a single person and her neighbors).

As we point out in the paper, we can visualize the ego-network precisely because the central node's communities are largely non-overlapping. So in the example above, Dorothy is the Ego, placed in the center of the visualization, while the various non-overlapping story lines appear as communities surrounding her.

One of the consequences of [pervasive overlap](http://sunelehmann.com/2010/06/29/pervasive-overlap/) (when every node is a member of multiple communities), is that we can no longer display the communities as block structures in the network adjacency matrix. Roughly speaking, to form a block structure, we need a single block per node. Some overlap is possible within the framework of block modeling, but when we can have more communities than nodes, this approach breaks down.

A similar problem arises in visualization. My guess is that any strategy for visualizing pervasive overlap where *nodes* are the basis of the visualization will ultimately turn out to be problematic for a full network. One possible solution is to follow the example of [CFinder](http://cfinder.org/) and construct a visualization based on the *network of communities* but with the ability to zoom into each community. At the local level, Rob's visualization would be perfect.

Comments/ideas are welcome. Note - this post can also be found at the [Complexity and Social Networks Blog](http://www.iq.harvard.edu/blog/netgov/2010/11/visualizing_link_communities.html).
