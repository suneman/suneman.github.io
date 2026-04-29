---
title: "Google's generosity goes to zero!"
date: 2011-10-07 08:51:17
slug: "googles-generosity-over-time"
status: publish
author: "sunelehmann"
categories: ["Misc"]
original_url: "https://sunelehmann.com/2011/10/07/googles-generosity-over-time/"
images: ["/assets/20111007_google_s_generosity_goes_to_zero/account_cost.png"]
---

According to the best of my calculations, the growth of Gmail storage is linear in time. Today, I recorded the amount of storage at two different times and found the rate of storage growth to be about 4.06541 bytes per second. This is consistent with [Wikipedia's report that, as of Jan 18th](http://en.wikipedia.org/wiki/Gmail#cite_ref-17), 2010 Gmail's storage was increasing at a rate of approximately 0.000004 MB per second. In other words, Google is giving away space at a constant rate.
Now, since the price of hard drive storage space seems to drop exponentially ([over the last 30 years, space per unit cost has doubled roughly every 14 months (increasing by an order of magnitude every 48 months](http://www.mkomo.com/cost-per-gigabyte "Hard drive prices")), this implies that Google is paying exponentially less for their new hard drive space [1]. The only reasonable conclusion is that***Google's generosity is rapidly approaching zero!***
Just to be extra silly, I actually plugged the growth-data from my own account and used the regression fit from the site above in order to estimate the cost per gmail account as a funtion of time.
[![](/assets/20111007_google_s_generosity_goes_to_zero/account_cost.png "account_cost")](http://sunelehmann.com/2011/10/07/googles-generosity-over-time/account_cost/)
Full disclosure: There are a number of problems with the approach of estimating the cost of an account as *current storage* multiplied by *current cost of storage.* And let me just mention some of them here for transparency. Firstly, my storage price is based on consumer hardware prices, and I'm betting that Google probably can probably get some kind of bulk deal. Secondly, I assume that Google has some kind of backup system in place, which increases the need for storage beyond the account size reported by Google. Finally and most importantly, the correct price for storage over time should probably be estimated as accumulated price paid for hardware at time *t* compared with the total amount of storage offered for free at time *t*.
And there's one final problem with the linear growth of storage. The issue becomes extra noticeable because all this cheap storage also applies to our personal computers ... and to the average attachment size, which is probably growing in proportion to the size of the hard drive it was sent from [2]. What this means is that we're likely to use up Gmail storage space at a rapid increasing rate.
I'm not saying that this is a violation of the "don't be evil" maxim. It's just that I'm running out of inbox space and don't want to pay for additional storage.

## Footnotes

[1] See also http://ns1758.ca/winch/winchest.html for more info on historical hard drive pricing. [2] I don't really have data to support this claim, but it sounds reasonable to me.
