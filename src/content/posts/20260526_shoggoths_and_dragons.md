---
title: "Shoggoths and Dragons"
date: 2026-05-26 09:00:00
slug: "shoggoths-and-dragons"
status: publish
author: "sunelehmann"
categories: ["Misc"]
images: ["/assets/20260526_shoggoths_and_dragons/shoggoth-smiley.jpg", "/assets/20260526_shoggoths_and_dragons/customer-service-dragon.jpg", "/assets/20260526_shoggoths_and_dragons/customer-service-shoggoth.jpg"]
---

Metaphors can be a support system for thinking. By finding the right analogies, we can map the complex unknown onto something familiar. And, in turn, that can help us better understand the complex unknown.

So when my former student [Germans Savcisens](https://savcisens.com) visited the group to talk about his new work as a postdoc at Northeastern University, my spidey sense tingled when he showed the following graphic.

![The 'Shoggoth with a smiley face' meme: a many-eyed Lovecraftian monster, with a small pink human face and a yellow smiley mask attached at the front.](/assets/20260526_shoggoths_and_dragons/shoggoth-smiley.jpg "A metaphor for large language models as a Lovecraftian monster (pretraining) holding a human mask (fine-tuning) holding a smiley face (RLHF). If any of these terms are confusing to you, not to worry – all will be explained in the text below.")

## The metaphor

The picture is so famous that it has a name: *Shoggoth with a smiley face*. And it's a metaphor for AI. If you want its whole history, you can find it at [Know Your Meme](https://knowyourmeme.com/memes/shoggoth-with-smiley-face-artificial-intelligence), but I'll give a short explanation here.

The unsightly monster is the Shoggoth, a creature invented by the master of the weird, writer H.P. Lovecraft (1890–1937).

**Pretraining**: In the metaphor the Shoggoth represents the *pretraining* aspect of LLMs. Pretraining is the part where an enormous neural network is trained to predict the next word within unfathomable amounts of text. The pretraining is the part of LLMs that's incredibly costly and uses huge amounts of energy. And more importantly, ***the pretraining is where the magic happens***.

What happens during pretraining is what makes the models brilliant; it's also the part we understand the least about. It's where intelligence somehow grows in an almost biological way out of the training process. (That's what I mean by 'magic'.)

The raw pretrained model is the one full of schizophrenic personalities, the part that will rattle off recipes for chemical weapons, the part displaying all manner of dangerous behavior. That's why the metaphor of the Shoggoth for the pretrained model captured me. The crazy monster seemed like the right way to capture the weirdness and mystery of the pretrained model.

**The rest of the metaphor**. The rest of the metaphor is designed to show how the part of the LLMs we interact with are really just shallow masks on top of the pretrained models. First a human mask, then a smiley face to represent the little prompt that we all talk to every day. That smiley face is generated via Reinforcement Learning from Human Feedback (RLHF), where humans tell the model which responses they like and don't like.

So we think we are talking to a happy little smiley face, but in reality the Shoggoth is right underneath.

## Sigh. 'It's very 2023'

So when I met my smart and awesome colleague and AI guru [Anders Søgaard](https://cpai.ku.dk) a few days later, I showed him the image, but he wasn't impressed. He said "to me that description feels a lot like LLMs in 2023".

That statement of course put me on a quest to figure out what the right metaphor for LLMs would be in 2026.

I don't want to get too technical here, so I'll describe the changes in training since 2023 somewhat superficially. Essentially what has changed is that there is much more input into the model after the pretraining. The feedback that the model gets is much more diverse than it used to be, and there's huge amounts of feedback from AI models too. On top of that there's system prompts and tools/scaffolding that also shape behavior.

Interestingly, there's still relatively little change to the weights of the pretrained model. My intuition is that this is because that makes the model less intelligent. All the focus is on steering the model towards certain (acceptable) behaviors and making the changes necessary to achieve that, not updating the wild beast at the center of all of it.

## A new metaphor

Fair enough. So I asked ChatGPT to give me a new metaphor for LLMs that works for 2026. IMHO it is pretty great.

It's represented below.

![A four-panel comic. Panel 1 'Pretraining': a Dragon surrounded by text declaring 'I have consumed all text.' Panel 2 'SFT': the Dragon in a customer-service cap reading an employee handbook. Panel 3 'RLHF and beyond': humans holding up rating cards. Panel 4 'Modern AI': the Dragon answering a tired customer, captioned 'A Dragon trained to do customer service.'](/assets/20260526_shoggoths_and_dragons/customer-service-dragon.jpg "How ChatGPT sees itself. As an all-powerful Dragon working in customer support.")

Instead of the Shoggoth, in Panel 1 we now have an all-powerful Dragon (so the pretraining monster has been cleaned up a bit). Then all the modern post-training in Panels 2 and 3.

In Panel 4, we finally arrive at modern AI. Firstly, I almost feel sorry for the wild beast of the Dragon having been so thoroughly tamed. Secondly, the guy asking it to "Explain Kant like I'm exhausted and late for a meeting" is a nice touch. Genuinely funny, and it captures what it feels like to be human in 2026. But more importantly, it shows the kind of task the Dragon has been shaped for.

## So what have we learned?

Metaphors always reveal something. But they're never perfect. So different metaphors reveal different things.

I loved the Shoggoth metaphor because it expressed something deep about the otherworldliness of the pretrained model. And it showed us how thin a veneer we had put on the Shoggoth back in 2023.

The Dragon metaphor does a few things differently. It still captures the power of the pretrained model (the Dragon in Panel 1 is scary and awesome), but makes it feel less alien.

Maybe it's not surprising since ChatGPT came up with it, but the Dragon metaphor subtly shifts the perspective of the post-training experience so we *see it from the perspective of the LLM*. The experience in Panel 3 seems genuinely stressful. And by the end of the comic strip I'm left feeling slightly sorry for the Dragon, once so powerful, now doing menial little tasks.

But my favorite thing is that the Dragon metaphor reveals something completely new. (And that's the power of metaphors right there.)

**As I read it, the Dragon metaphor also showcases the insanity of the entire endeavor. We created an all-powerful Dragon, but we're using it to do customer support. What a small job for such a big machine.**

I'm left thinking: is this really a good use of scarce resources? Or: shouldn't we be using the Dragon for something more inventive?

<hr />

P.S. I always felt that ChatGPT was 'cheating' when it replaced the Shoggoth with a Dragon in its metaphor. The pretrained model is still weird, and it isn't changing that much. So I created a new version that puts the Shoggoth back in the Dragon's place. It's perhaps the right amount of unsettling.

![The same four-panel customer-service comic, but with a many-eyed Shoggoth in place of the Dragon. The final panel reads 'A Shoggoth trained to do customer service.'](/assets/20260526_shoggoths_and_dragons/customer-service-shoggoth.jpg "The same four panels, with the Shoggoth put back where the Dragon was.")
