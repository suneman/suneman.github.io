---
title: "Pervasive Overlap"
date: 2010-06-29 15:07:08
slug: "pervasive-overlap"
status: publish
author: "sunelehmann"
categories: ["Complexity and Social Networks Blog", "Work"]
original_url: "https://sunelehmann.com/2010/06/29/pervasive-overlap/"
---

Just recently, I came across the following video showing [LinkedIn](http://www.linkedin.com/) chief scientist [DJ Patil](http://www.linkedin.com/in/dpatil) explaining the egocentric networks (networks consisting of an individual and their immediate friends) for a few individuals based on their LinkedIn connections.

<iframe src="https://www.youtube.com/embed/se2u5RyGaNE" width="560" height="315" frameborder="0" allowfullscreen></iframe>

Although the individuals in the center of these egocentric networks are unusual (in the sense that they have many more LinkedIn connections than the average user), the video clearly shows that each person is a member of *multiple communities* where the communities are dense and almost fully connected, while there are fewer connections between the communities. (If any of this sounds familiar, it's because [I wrote about this subject](http://www.iq.harvard.edu/blog/netgov/2010/03/worlds_colliding.html) a couple of months ago on the [Complexity and Social Networks Blog](http://www.iq.harvard.edu/blog/netgov/)).
This notion of social structure implies that -- seen from the perspective of a single node -- everything is relatively simple: the world breaks neatly into easily recognizable parts (e.g. family,  co-workers, and friends). There are few or no links between the communities because we actively work to keep them separate ([more here, on why this is the case](http://www.iq.harvard.edu/blog/netgov/2010/03/worlds_colliding.html)).
I've been thinking about the consequences of this local structure for a while, and recently coauthored a paper this subject with [YY Ahn](http://yongyeol.com/) and [Jim Bagrow](http://bagrow.com/) [1]. Here, and in an upcoming blog post, I'll be writing about some insights from that work.
The idea I hope to explore here has to do with the *global structure* that arises when all nodes in a network have multiple community affiliations, when there is pervasive overlap. In the follow up, I'll explore how a single hierarchical organization of the network can exist in the presence of pervasive overlap.

### Untangling the hairball

In the standard view of communities in networks, the global structure is modular [2]. This situation is shown below (left), where the communities are labeled using different colors (image from [gephi.org](http://gephi.org/)). Modular structure on the global level implies, however, that individual nodes can have only a single community affiliation!

|  |  |
| --- | --- |
|  |  |

If every node is a member of more than one community -- and this is clearly the case in the LinkedIn example, as well as in real social networks -- *then the global structure of the network is not at all modular. Rather, the network will be a dense mess with no visually discernible structure. The network will look like ball of yarn ... or a hairball (*above, right). In fact, this is precisely the type of structure which has recently been discovered in empirical investigations of a comprehensive set of large networks (social and otherwise) [2, 3].
So the question becomes: *How do we find network communities in the hairball?* This is the question YY, Jim and I answer in Ref [1]. The trick is that although *nodes* have many community memberships, each *link* is mostly uniquely defined. For example, the link you have to one coworker is similar to the link you have to other coworkers. Thus, by formulating community detection as a question of categorizing links rather than nodes, we are able to detect communities in networks with pervasive overlap.
Using our algorithm, for example, we show that dense hairball-networks, such as the [word association network](http://web.usf.edu/FreeAssociation/) (which is what is pictured above, right) contain highly organized internal structure with well defined and pervasively overlapping communities. We're hoping that our algorithm will help reveal new insights about some of the many highly overlapping social networks, such as the LinkedIn data shown above.
Code for our algorithm may be downloaded [here](http://barabasilab.neu.edu/projects/linkcommunities/); that site also features a neat interactive visualization of the link clustering algorithm.
**Note**: This entry was originally posted on the [Complexity and Social Networks Blog](http://www.iq.harvard.edu/blog/netgov/2010/04/).

## References

- [1] Yong-Yeol Ahn, James P. Bagrow and Sune Lehmann. [Link clustering reveals multiscale complexity in network](http://www.nature.com/nature/journal/vaop/ncurrent/abs/nature09182.html). *Nature.* doi:10.1038/nature09182 (2010).
- [2] Santo Fortunato. [Community detection in graphs](http://sites.google.com/site/santofortunato/review_comm.pdf?attredirects=0). *Physics Reports* **486**, 75-174 (2010).
- [3] J. Leskovec, K. Lang, A. Dasgupta, M. Mahoney. [Statistical Properties of Community Structure in Large Social and Information Networks](http://cs.stanford.edu/people/jure/pubs/ncp-www08.pdf) *International World Wide Web Conference (WWW)* (2008).
- [4] J. Leskovec, K. Lang, A. Dasgupta, M. Mahoney. [Community Structure in Large Networks: Natural Cluster Sizes and the Absence of Large Well-Defined Clusters](http://arxiv.org/abs/0810.1355). *arXiv:0810.1355v1* (2008).
