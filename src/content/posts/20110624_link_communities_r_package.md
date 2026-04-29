---
title: "Link communities R package"
date: 2011-06-24 12:48:28
slug: "link-communities-r-package"
status: publish
author: "sunelehmann"
categories: ["Misc"]
original_url: "https://sunelehmann.com/2011/06/24/link-communities-r-package/"
images: ["/assets/20110624_link_communities_r_package/screen-shot-2011-06-22-at-8-24-53-pm.png", "/assets/20110624_link_communities_r_package/screen-shot-2011-06-24-at-6-20-06-pm.png"]
---

A while ago, I [wrote](http://sunelehmann.com/2010/11/03/visualizing-link-communities/) about Rob Spencer over at [Scaled Innovation](http://scaledinnovation.com/)'s implementation of the algorithm for detecting link communities. Today, I am happy to report on another exciting development for the alorithm. Alex Kalinka from the [Tomancak lab](http://www.mpi-cbg.de/research/research-groups/pavel-tomancak.html "mpi") at the Max Plank Institute (MPI-CBG) has written a great implementation in *R*, called *linkcomm*. It is now up on CRAN:
<http://cran.r-project.org/web/packages/linkcomm/index.html>
While everything is excellent, the graphics are particularly beautiful - much prettier than our own visualizations - check out the colored link dendrogram plot (from the [CRAN website](http://cran.r-project.org/web/packages/linkcomm/vignettes/linkcomm.pdf "image source"))

[![](/assets/20110624_link_communities_r_package/screen-shot-2011-06-22-at-8-24-53-pm.png "Link dendrogram")](http://sunelehmann.com/2011/06/24/link-communities-r-package/screen-shot-2011-06-22-at-8-24-53-pm/)

And the spatial network layout options are great as well; the various community visualizations are simple, elegant, and very pretty:
![](/assets/20110624_link_communities_r_package/screen-shot-2011-06-24-at-6-20-06-pm.png)
In addition, there are many neat features. For example, *linkcomm* allows you to visualize sub-communities by themselves. Alex has also published an Application Note in Bioinformatics about the implementation, so take a look if you're interested:
<http://bioinformatics.oxfordjournals.org/content/early/2011/05/19/bioinformatics.btr311.abstract> (open access).
We also link to the package from our [link communities download page](http://barabasilab.neu.edu/projects/linkcommunities/).
