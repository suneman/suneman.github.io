---
title: "Tracking Human Mobility using WiFi signals"
date: 2015-05-26 09:27:07
slug: "tracking-human-mobility-using-wifi-signals"
status: publish
author: "sunelehmann"
categories: ["Misc"]
original_url: "https://sunelehmann.com/2015/05/26/tracking-human-mobility-using-wifi-signals/"
images: ["/assets/20150526_tracking_human_mobility_using_wifi_signals/subsampling_curves.png"]
---

When I started working on understanding social systems, privacy really wasn't on my mind. (I generally want to write down equations, understand the universe and all that). But one of the central realizations arising from our [SensibleDTU experiment](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0095978) is that privacy needs to be an important part of this kind of research. I've written about this at length [elsewhere](http://sunelehmann.com/2014/12/11/some-thoughts-on-privacy-part-0/). One of the things we noticed while digging into terabytes of social data is that data-channels are highly correlated. Information "bleeds through" ... something which has serious implications for privacy. Case in point: My group has just released a new preprint ([get it here](http://arxiv.org/abs/1505.06311 "Link to paper")) that *shows how the WiFi information routinely collected by your smartphone can easily be converted to precise information about your location*. WiFi routers reveal where you live, work, and spend your leisure time. While your phone may have told you that WiFi helps “improve location accuracy”, it may come as a surprise that

- A majority of apps in the store have access to the list of routers around you (scanned every 20 seconds).
- Your Android smartphone by default scans for WiFi routers even if you disable WiFi.

Our research shows

- How to easily convert WiFi information into geographical position.
- That although it sounds like all WiFi scans might be a lot of data to process, your mobility can be described using just a few of access points. **And we have built an Android app** **which only requires WiFi data** to illustrate how this works for your own mobility: [Download here](https://play.google.com/store/apps/details?id=dk.dtu.compute.mywifiscanner "Check out the App!").
- That if someone knows these routers at some point in time, they will still know a lot about your mobility six months later.

Thus, while WiFi networks are intended for enabling connectivity, they are also a *de facto* location tracking infrastructure. More generally, our world is becoming more enclosed in a web infrastructures supporting communication, mobility, payments, and advertising. Logs from mobile phone networks (call detail records, CDRs) constitute a global database of human mobility and communication networks. Credit card records form high-resolution traces of our spending behaviors.
![The figure shows 48 hours of location data of one of the authors, with the four visited locations visited marked in blue: home, two offices, and a food market. Even though the author](/assets/20150526_tracking_human_mobility_using_wifi_signals/subsampling_curves.png)

The figure shows 48 hours of location data of one of the authors, with the four visited locations visited marked in blue: home, two offices, and a food market. Even though the author's phone has sensed 3,822 unique routers in this period, only a few are enough to describe the location more than 90% of time. (a) traces recorded with GPS; (b) traces reconstructed using all available data on WiFi routers locations - the transition traces are distorted, but all stop locations are visible and the location is known 97% of the time. (c) with 8 top routers it is still possible to discover stop locations in which the author spent 95% of the time. In this scenario transitions are lost. (d) timeseries showing when during 48 hours each of the top routers were seen. It can be assumed that AP 1 is home, as it's seen every night, while AP 2 and AP 3 are offices, as they are seen during working hours. The last row shows the combined 95% of time coverage provided by the top 8 routers.

It is already a well know fact, that the so-called “WiFi scanners” can be [used to track individuals](http://www.sciencedirect.com/science/article/pii/S1574119214001953 "An example paper"). This is done by cities, airports, shopping centers, and advertisers (and perhaps intelligence agencies). Some OS manufacturers (e.g. Apple and Chainfire) have recently responded to such tracking by frequently randomizing the unique identifier of each phone. Randomizing the phone identifier, however, *does not address the threat presented in our work*—where data is collected by an application on the phone, not by external devices. The privacy of WiFi scan results is often overlooked. In the Android ecosystem the WiFi scans are not considered as a location signal. WiFi information can be collected by applications without location permission, do not show up in the overview of applications using location data, and the WiFi permission is not considered sensitive. This makes it possible for 3rd party developers to collect high-resolution mobility data under the radar, circumventing the policy and the privacy model of the Android ecosystem. Any app with just the WiFi permission can track your position, although they don't necessary do (there are legitimate reasons for applications to ask for WiFi permission, although this permission seems to be requested more often than required). Last time we checked (February 2015), 17 out of 20 top games on Android Play Store required access to your WiFi data; in only 6 of those 17 cases their privacy policy provided reasons why this information is required. For more information, email the paper's first author Piotr ([pisa@dtu.dk](mailto:pisa@dtu.dk)), who collaborated on this post. Or me ([sljo@dtu.dk)](mailto:sljo@dtu.dk)). The [preprint is available on arXiv](http://arxiv.org/abs/1505.06311 "Link to Paper").

## Update June 3rd, 2015 (maybe-our-paper-played-a-role-in-this edition)

Yesterday, while scouring Google I/O for details on the updated permissions (and to see if anyone mentioned our work), we found that a Google engineer (Ben Poiesz) was asked about the issue of WiFi tracking during the session discussing the new permission model. The session took place on May 29th - the clip is here:
https://youtu.be/f17qe9vZ8RM?t=17m30s
In the video, the friendly Google engineer notes that that - under the new system - apps without the location permission will no longer be able to see the mac addresses of WiFi and Bluetooth devices around ... *because that’s that’s equivalent to location*.
No one is claiming (least of all us) that our work caused the change, but we would like to point out a couple of things about the way Google chose to announce it, which might indicate that the choice of fixing wifi is a recent decision on Google's part:

- The published source code [find it [**here**](https://android.googlesource.com/platform/packages/apps/Settings/+/android-m-preview/src/com/android/settings/applications/AppOpsState.java "Source Code")] (lines 99-114) and documentation [find it [**here**](https://developer.android.com/preview/features/runtime-permissions.html "Documentation")] *do not yet* indicate that WiFi information is to be treated as location.
- When you install the current Android M beta on your phone, our *"WiFi Watchdog"app still works* ... and WiFi is not treated as location. And a technical point: This it’s not just because of the “legacy mode” - according to the same presentation (<https://youtu.be/f17qe9vZ8RM?t=13m>): "WiFi Watchdog" should just receive empty data on Android M, but instead it continues to receive the same data as on Lollipop
- The announcement of this *arguably major change* (80% of apps on the market would potentially be affected) was not a part of the main presentation ... but an answer during the Q&A session.

Now, it is *probably just a coincidence*, and maybe a fix for the WiFi permissions has been in the works for months. But it’s quite striking that Google decided to fix wifi permissions 7 years after the existing scheme was introduced (and just days after we published our paper).
