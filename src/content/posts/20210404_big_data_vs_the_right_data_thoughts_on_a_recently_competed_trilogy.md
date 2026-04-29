---
title: "Big data vs the right data: Thoughts on a recently competed trilogy"
date: 2021-04-04 16:36:41
slug: "big-data-and-predicting-how-fast-you-can-run-100m"
status: publish
author: "sunelehmann"
categories: ["Misc"]
original_url: "https://sunelehmann.com/2021/04/04/big-data-and-predicting-how-fast-you-can-run-100m/"
images: ["/assets/20210404_big_data_vs_the_right_data_thoughts_on_a_recently_competed_trilogy/boot_loading.jpg", "/assets/20210404_big_data_vs_the_right_data_thoughts_on_a_recently_competed_trilogy/screen-shot-2021-04-04-at-14.51.45.png"]
---

Along with a superb group of coauthors ([Andreas Bjerre-Nielsen](https://abjer.github.io/), [Valentin Kassarnig](https://www.linkedin.com/in/valentin-kassarnig-5330a3124/), and [David Dreyer Lassen](https://daviddlassen.github.io/)), I recently published *[Task-specific information outperforms surveillance-style big data in predictive analytics](https://www.pnas.org/content/118/14/e2020258118)* in PNAS.

I am very excited about this paper, which is the conclusion to our trilogy of "learning analytics" papers, based on the [Copenhagen Networks Study (CNS) dataset](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0095978). And in my own humble opinion, it's a fine series conclusion [1]. What we found was deeply surprising to us and while focused on predicting academic performance, the paper makes a couple of important general points, which I discuss below. Plus it's short! The two first papers in the trilogy are:

- **Part 1**: [Class attendance, peer similarity, and academic performance in a large field study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0187078) (PLOS One, 2017). In this first part of the trilogy, we develop methods for measuring class attendance using behavioral data and quantify how attending class impacts our predictions of academic performance.
- **Part 2**: [Academic performance and behavioral patterns](https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-018-0138-8) (EPJ Data Science, 2018). In the follow-up, we use class attendance - and all the other rich data we collected about students during the CNS project face-to-face contacts, online social networks, telecommunication, mobility, demographics, personality, etc) to predict academic performance. On of the key results from that paper was that, based on these rich data, we could predict performance on the level of state-of-the-art within learning analytics (=quite well).

![](/assets/20210404_big_data_vs_the_right_data_thoughts_on_a_recently_competed_trilogy/boot_loading.jpg)

**Figure 1.** Flashing custom software on the smartphones used for the CNS study back in 2013. We did that for 1000 phones!

For the conclusion of the trilogy we wanted to do something special. So we moved the features from the CNS study to [Statistics Denmark](https://www.dst.dk/en) (DST) [3] in order to see ***how much* more accurately *we could predict outcomes if we merged the highly detailed CNS data with the comprehensive registry data from DST***.

We expected the combination of behavioral data and registry data to yield even better results than the behavioral data alone. And that is indeed what we found.

But what completely took us by surprise is that ***the behavioral data basically didn't add anything to the prediction***. You can see this in Figure 2 (Fig 1A in the paper) below.

![](/assets/20210404_big_data_vs_the_right_data_thoughts_on_a_recently_competed_trilogy/screen-shot-2021-04-04-at-14.51.45.png)

**Figure 2:** Predictive performance of the various data-types considered individually and together. The *x*-axis shows the balanced accuracy, with the vertical dashed line indicating the baseline of random guessing. "Big data" is all the detailed behavioral data we had collected from the CNS study and written about in Part 1 and 2 of the trilogy. "Administrative data" is the registry data which contains information about past grades as well as sociodemographic information about parents.

The top line of the figure (red violin) shows the performance of behavioral data alone, the second line (blue violin) shows administrative data alone, and the bottom line shows performance when both data-types are combined. As is clear from the plot: When comparing behavioral data with the registry data head-to-head, we clearly get the best prediction from the administrative alone. And when we combine the two, the behavioral data does not add any additional information!

(And at this stage I remind the reader that in Part 2 two of the trilogy, we showed that the behavioral data is absolutely on par with state-of-the-art in terms of predicting actual performance).

## What's going on!?

In the paper itself, we dig deeper and show that the thing that really matters in terms of making accurate predictions, is how well students did academically before starting university. And that finding helps us make sense of the (surprising) result above.

What matters for accurate prediction is access to a measure of ***task-specific performance***. If you what to know how well a student is going to fare at an exam, then information about their performance at a previous exam will be highly valuable. As we show in that paper, that information is much more relevant that information about your social network, friendship circle, personality, and so on.

The analogy that I like use is the 100*m* sprint. Let's say you find a person and want to predict how long it will take them to run 100 meters.

As I see it, the [surveillance capitalism/](https://www.theguardian.com/books/2019/oct/04/shoshana-zuboff-surveillance-capitalism-assault-human-automomy-digital-privacy)data exhaust/digital breadcrumbs approach is similar to sending a person to the gym and measuring how much weight they can lift in bench press, squat, dead lift, and so on. Perhaps also measure their BMI, body fat percentage, VO2max, and take some of blood panels.

This kind of rich information tells us a lot about a person's general fitness. And based on this type of data, we can make many very different (but mediocre) predictions. We could probably do a reasonable job predicting their lifespan, guessing their age, estimating how many pull-ups they could do, what kind of diet they eat, etc

Based on these data, we could probably also do an acceptable job at predicting how fast that person can run 100*m*.

But my bet is that ***information about how fast their most recent time running 100m would be a much more valuable piece of information***. That's what we mean by "task-specific information" in the paper. And I think that's why we find that the most useful information in the case of academic performance ... is past academic performance!

## What does this mean for data science?

The first implication for data science (which we also mention in the paper) is that our finding provides yet another argument that for every practical application, we should carefully consider, if we really need to collect all that data in the first place.

In the case of learning analytics specifically, we make the point that it might not be necessary to install an app on every single student's phone and monitor their every move in order to identify the students in need of extra help or support. One could simply take a look at high-school transcripts (submitted during the application procedure) - or simply ask the students!

The more general version of this is expressed beautifully in the paper (formulated by co-author David Dreyer Lassen), so I'll just quote it here:

*The privacy–utility tradeoff ( ... ) posits that predictive ability from personal data is inversely related to privacy preservation. While generally true within a given dataset, this approach neglects the possibility that other data, possibly from different sources, on the same set of individuals may have a superior predictive ability for a given, or even more favorable, level of privacy. We argue—following the logic of prediction contests, where **new candidate models are compared against the best possible alternative rather than a benchmark of zero predictive ability**—that we should compare the predictive ability of different datasets, with different levels of granularity and potential privacy implications, to make more-informed choices about prediction/privacy tradeoffs. This insight is particularly important for characteristics or behaviors that are more stable over time and for outcomes where past task-specific information is available.* [my emphasis]

The second implication is a bit more fuzzy. A sharp formulation of the exact issue is still not really clear in my mind yet. But somehow this feels to me like a new kind of frontier among the many complex issues related to Big Data (e.g. among privacy, biases, transparency, security, and so on).

The best way I can express it, is that the issue is related to something we could call *"relevantness"*. Big datasets can be used to predict many different things about the people in those datasets. And it is true that sometimes we can wring surprising insights out of behavioral data. Famously, for example, we know that it is possible to estimate political leanings, personality and more, based on [Facebook likes](https://www.pnas.org/content/110/15/5802).

But what we argue in our new paper, is that there's also a limit to these big datasets. It's not magic, and there are things we cannot learn just because we have access to large scale behavioral data. We can't necessarily estimate your risk of heart disease based reading habits, and so on.

Here, I think coming back to the analogy of physiological measurements is useful. The big behavioral datasets allow us provide mediocre answers many different questions, but for each specific question we have, there are better ways of getting accurate answers. And that's the new trade off we need to also think about: Is the information we're interested even available within the surveillance-style datasets we're collecting? Stated borrowing some terms from linear algebra: Is it even possible to express direction we're interested in based on the basis vectors spanned by our surveillance data set? Or something like that.

That last part got a big rambling, but if you're still here, let me know if this makes sense to you. I'll be thinking more about this in the future and hopefully my thoughts on this last aspect will get clearer with time :)

## Notes

[1] I honestly think that it's "Avengers Endgame"-level. By this I don't mean that the paper is as good as *Avengers Endgame*. I just mean that *Avengers Endgame* was a satisfying end to the Avengers quadrilogy [2] - and in the same way this paper is a satisfying end to our paper trilogy.

[2] And yes, I am using the word "quadrilogy" to describe a 4 part series even though I think it is a ridiculous word. A better term for a four part series is "quartet" (e.g. as in Lawrence Durrell's *Alexandria Quartet*), but that's clearly too pretentious for the Avengers Series. And I'm not a fan of the term tetralogy.

[3] Statistics Denmark is the central authority on Danish statistics. Their mission is to collect, compile and publish statistics on the Danish society - and so they have an amazing dataset on all Danes, including lifelong academic performance, income, health, you name it.
