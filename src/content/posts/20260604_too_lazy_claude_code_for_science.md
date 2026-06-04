---
title: "We need to get started on creating gyms for the mind"
date: 2026-06-04 09:00:00
slug: "too-lazy-claude-code-for-science"
status: publish
author: "sunelehmann"
categories: ["Podcasts"]
images: ["/assets/20120522_yong_yeol_ahn/yy_2011.jpg"]
ai_assisted: true
---

The podcast is back!

A couple of years ago, I got excited about podcasting. The concept for my podcast is amazing. It's called *Too Lazy to Read the Paper*. The pitch is that someone explains a paper that they love to me (so I don't have to read it). 

There's no paper this time. Instead I felt like talking on the air about agentic coding: Claude Code, Codex, and the rest – the whole business of handing an AI your research and letting it write and run the code. My sense is that getting started is the big hurdle for a lot of people.

So to help folks get started, and to help myself, I sat down with the obvious guest. **Yong-Yeol Ahn** – YY to everyone who knows him – is an old friend and collaborator from my postdoc days in László Barabási's group at Northeastern. YY is now the Quantitative Foundation Distinguished Professor at the University of Virginia's School of Data Science. He has been living in the terminal since long before it was fashionable, dotfiles and all. And he's an early mover with respect to agentic coding. I've been following his writing ont his for a while. It's awesome. So he is exactly the person I want to talk to about all this.

We get into what Claude Code actually *is* (a capable model on a leash, with access to your files), why a working scientist should care, the genuinely scary parts (it will write a lot of wrong code very quickly and very convincingly), what we might lose when the next generation never has to debug a stray semicolon, and a long, unplanned detour about starting up a mental gym. We also talk skills, subagents, the dangers of letting a model invent your references, and why YY keeps pushing for open-source models and portability.

Watch below, or listen on [Buzzsprout](https://toolazy.buzzsprout.com).

<https://www.youtube.com/watch?v=8jo91yMtD_E>

---

*The transcript below was auto-generated from the captions and then lightly edited for readability – fixing the worst mis-hearings and adding speaker labels. I've tried not to change what either of us actually said; where a sentence reads oddly, assume the editor mangled it, not the speaker.*

**Sune:** Welcome, ladies and gentlemen, to *Too Lazy to Read the Paper*, the show where normally someone explains a paper to me – because reading papers is hard, and talking to people is fun and natural. And now for a corollary. If someone is too lazy to read a paper, they're definitely too lazy to read the manual. So today I have a new format. There's no paper; instead there's a thing we've all been talking about, maybe in the shadows: agentic coding. Claude Code, Codex, whatever they're all called – this whole business of handing an AI your research and letting it write and run the code. And my sense is that getting started on this is a big hurdle for a lot of folks.

So to help them, and to help myself, I'm sitting down with the all-round genius, Renaissance man, deep thinker, connoisseur of all things coding and living in the terminal, and honest and decent person, YY Ahn. YY is the Quantitative Foundation Distinguished Professor at the School of Data Science at the University of Virginia. YY and I go way back – to the Center for Complex Network Research at Northeastern, where we were both postdocs in László Barabási's group. Fast-forward to now: a decade and a half later, YY stands out as the person I want to talk to about agentic coding. So let's cut to the chase and hear my conversation with YY Ahn.

Welcome, welcome to the pod. This is a special occasion. I'm bringing back the podcast. It used to be called *Too Lazy to Read the Paper*; now it's called *Too Lazy to Figure Out How to Use Claude Code for Science*. And I'm here with my special guest, YY Ahn, a very old friend – we started out together in science in the Barabási lab. Before we get going, I want to give you the chance to talk a little about the science you're doing in your group. I've been following it; the papers are brilliant as always, and your website is one I check regularly – I'll put notes in the show notes for those who want to follow your life. But tell me – I'll shut up, since you're the one being interviewed – tell me a little about what you're working on at the moment.

**YY:** I've been fascinated by latent space – representation learning, especially related to graphs and networks. That's been driving a lot of research recently. I'd say it's about bridging network science and machine learning, or representation learning, and using that understanding to address interesting problems in society. For instance, when we dig into what's really happening in representation learning, one thing we found is that the degree bias from the random walk is canceled out by the bias in the optimization function – in the negative sampling. That leads to a correspondence with the gravity law, which means we can impose nice interpretability in the embedding space when we have trajectory data. We've been applying that to mobility – finding invisible borders in urban space – or thinking about belief embeddings. Lots of different applications.

**Sune:** But immediately the question that comes to mind – and part of what's awesome about networks is the discreteness. It's the paths, all the things that are *not* continuous. But representation is about taking the network and putting it into a machine-learning space. So – and we're getting off on a tangent already, but it's because your work is awesome – can you talk about what we gain by jumping between the two? Is there even anything left of the network afterwards? Is it just a data set, then we put it into a representation, and the representation tells us everything? What's going on there?

**YY:** I think it's a little underexplored, actually – how to combine the two. There's a nice property to this continuous representation: we can find meaningful axes in the space, we can measure distance in a very smooth way, and so on. So there are lots of good things in the representation space. But networks provide really discrete connections. A good scenario to think about: you have a smooth, chain-like network structure; if you embed it into the representation space, it becomes a smooth manifold, and the distance from one end to the other is very far. But in the network you can just connect the ends – there's no constraint on those connections. It reminds me of a *Science* paper about long-range, really strong connections in social networks. So combining that information is what's really exciting.

**Sune:** I totally agree. And we should be honest that, of course, if you add that connection, you also change the network quite dramatically. A lot of network properties make huge jumps as you add shortcuts, so it's not so weird that the space would have to be reconfigured too. This is super cool. I also saw you posting on something called the platonic representation hypothesis – the idea that when you train neural networks on large amounts of text (but you could also train them on data from physics or whatever), maybe there's a platonic space underneath, and it all converges to the same thing, in some way mirroring reality. I follow your blog, I'm a fan, and I saw your post: here's the paper, here's someone expanding on it, and here's someone saying maybe it's all bullshit. So this leads me to ask: how do you think about representations more generally? We really live in this representation world. How does all the work on graphs connect to these other representations?

**YY:** In a way, we are living in a shared world – one world. Whatever perspective we take, it's slightly different but still a very similar truth underneath. A graph is one way to look at it, focusing on explicit relationships. And a lot of machine learning and representation learning is about finding a more continuous representation that captures that same space. So there's a constant tension between explicit and implicit – knowledge graph versus plain embedding. In my group we also work a lot on embeddings, and I've thought about this a lot. So consider this a teaser for the yet-to-be-made podcast where we go deep on embeddings and how they reflect reality.

But this episode is kind of Claude Code for – I don't even want to say "beginners" – for scientists. We've seen people all over the internet catch the Claude Code fever. All of a sudden you fire it up on your little computer at home and realize, wow, this thing can do amazing things.

**Sune:** It's not wrong to say you've been a pioneer in applying this. I keep saying Claude Code, but we should be clear it's just one approach to coding with AI – there are competing solutions, also good, from other providers, other purveyors of general intelligence. But we'll talk about Claude because it's the one most people have played with. I wanted this conversation to be about what this means for a scientist. Maybe you can start by saying – if you come to this completely cold and just want a sense of what Claude Code even is – what is this thing? Do you want to lay it out a little?

**YY:** Everyone has played with ChatGPT and these chatbots, right? To me, Claude Code, Codex and the other coding agents are basically putting them *into* your computer, so they can interact with your files. That's what it really is. People call it a "harness" – providing tools the model can launch and use, and harnessing it so it stays in its lane. So you're allowing it to use tools and, at the same time, preventing it from doing weird things. On top of that there's maybe a more specialized model, although it's becoming less specialized: Claude Code works with Claude – Opus, or Sonnet – really well, because the model is trained to use the tools Claude Code provides and to work in the harness.

**Sune:** And I've found that working with Claude Code is almost nicer than working in the web interface to Claude, somehow. Whatever tweaks they have in the harness make it a bit more rational and thorough, so it doesn't skip a beat. So Claude Code is really a way to put Claude in contact with a subset of the tools available on your computer – all the coding tools – and let it play around with your files, but locked into a place. It's also extra amazing to someone like you, because the canonical way of working with it is staying in the terminal – that classic way to approach code. I remember you from back in the day, living in the terminal in a very real way. You had this thing called dotfiles – little files that the various terminal programs read – setting up your terminal really well, knowing all the shortcuts to move around files. Is that one of the reasons you were an early adopter, that it brought coding agents into that world?

**YY:** Yeah, totally. I was working with dotfiles, living in the command-line-interface ecosystem, before Claude Code. So it felt supernatural to try out. One other thing I'd quickly mention: "Claude Code" is maybe a bit of a misnomer, because it's not just about coding – it's about anything on your computer.

**Sune:** I agree. You could say, "I'm working on a manuscript, help me outline the arguments, here's what I've got so far." It does all of that. It's not just coding – it just happens to be really good at coding too.

**YY:** Yeah. If I count all my usage, the actual coding is a smaller percentage than the rest. The first thing I did with Claude Code was revamp my dotfiles – make them nicer, easier to install and manage.

**Sune:** So – I introduced this term "Claude fever," because when people first start using it and discover how amazing it is, they tend to get obsessed for a while. It has all the bad stuff of social networks: a variable reward – you sit and wait, and what comes back might be awesome, but it might also be terrible, and the waiting time is unpredictable. It does amazing things, and if you don't have the big usage plan, it'll suddenly say "now you have to take a break," and that makes you even more obsessed. So what's your story of becoming obsessed with it?

**YY:** I installed it quite early and tried it out. But this January it really started to take off, in terms of what it can do and how well it does it. Once that model hit – I don't know exactly which model number it was – you really feel that something is different here. After that, I just kept testing it, because there's no way back. There's a moment where you think, "oh, coding is done, a solved problem" – a moment where I don't have to code anymore. The way I experimented was by building really small tools for myself: a timer, static site generators, all these little tools. My homepage was actually one of the first projects I made. I keep a large personal wiki, and I mark things public or private through front matter; the tool generates the homepage from the wiki. So I don't have to maintain a separate homepage and wiki – what you see is whatever in my wiki has been made public. At the same time, I've been scared to really use it in research, because it's such a slippery slope.

**Sune:** Totally. It's really slippery.

**YY:** If you just let go and let it write code for you in research, it's hard to ensure the code is actually correct. I was very scared of that. So it was mainly about building tools and experimenting with how well it works on various tasks – and things like managing files, filing the papers I download, and so on.

**Sune:** Anything that can be verified somehow. And I agree – research is a special use case, where I've also been very careful. I'm a bit weird this way, but I like writing, and I don't want it to take over the writing, because I'm so particular. But there's still lots of writing I don't care about that's amazing to have done. I also see it as a kind of API into unstructured data. Your wiki is unstructured, but if you want to query it for something you know is in there but can't find – oh, hang on, I think we have some lag. Can you still hear me? Okay, we're back, I don't know what happened. You were saying –

**YY:** You were saying the wiki is unstructured.

**Sune:** Right. So if you're looking for some piece of information in your wiki, Claude is also a way in. You can grep and use the terminal tools and probably find it; but for something bigger, it's also, in a weird way, an API for that. Or if you have a Word document full of information and want it moved into an Excel sheet in a certain format, Claude can do that for you – and it might even write a script to do it, so you can verify it worked.

**YY:** Yeah. One thing that really removed a lot of hassle is ingesting papers into my wiki. I have a skill: I send it a URL, and it fetches the metadata through OpenAlex, arXiv, the DOI, whatever, downloads the PDF, and creates a wiki page with that metadata. And one really cool thing – it kind of knows the relevant papers, so it can search for them in my wiki and link to those pages. Once you ingest a paper you still want to read and digest it, but more or less every time it discovers a linkage I hadn't noticed: "oh, this author wrote that paper." So you get a richer link structure.

**Sune:** Super cool. But now we're already talking about skills, and maybe getting ahead of ourselves. We've laid out what this machine is and some of what it can do, but it can still feel abstract. So let's talk about AI for science – agentic coding for science, Claude Code for science, whatever we want to call it. We already covered the scary thing: if something is really mission-critical, it can generate so much code, so quickly, that trusting it blindly is dangerous. Lots of billion-dollar companies do trust it blindly, but in science we want to be extra careful. So what are some no-brainer use cases for scientists? If you were starting today, how would you use it? What do you use Claude for?

**YY:** I think the first step – as I mentioned – is that every scientist should have some kind of knowledge system. It can be Zotero, a wiki, Obsidian, whatever. Managing that is where it can help a lot: instead of manually typing the title and URL, it automates that and makes the connections. So knowledge ingestion is the first step.

**Sune:** Can we pause on that? You're a disciplined, awesome person, and I'm the opposite. I've started a wiki three times and abandoned it each time, because when I got busy I'd stop updating it, and then I'd say "okay, I'll keep notes this other way instead." So I have these old, abandoned knowledge systems lying around. And what I found is that Claude – or good agentic coding – can help with that too. You can literally say, "here's this old pile of stuff, let's organize it," and it'll take the words you've written and make new sense of them, integrating across time. Of course, it's a lot of work – this was some of my own Claude fever, cleaning up my scattered pieces from the past. But it's also good for weird stuff: "let's go through all my tweets and..." When I quit Twitter I downloaded all my tweets, and it'll just write a script to go through them, extract all the links, and see what's valuable. It's amazing how easy it makes that – again, serving as an API, a programming interface to all kinds of weird unstructured data. So even if you don't have a wiki, it can help you make sense of your personal history of ideas, something you can draw on and build from.

**YY:** Yeah. And it's not just the mechanistic stuff – you can also learn a subject fairly easily. It hallucinates from time to time, but it's so easy to keep asking questions you'd be too embarrassed to ask an actual human being. So there's real value in learning.

**Sune:** Can you give an example? Don't make it too embarrassing, but just to give people a sense of the kind of question.

**YY:** I can't think of a concrete one right now, but say you're learning some mathematical theory and you don't understand a small part – maybe something undergraduate, calculus or really elementary math – and I do struggle with those.

**Sune:** Look who you're talking to. You don't have to be embarrassed. What *I* don't know is fairly impressive for someone at my career stage.

**YY:** For learning anything, it's amazing. I have had it hallucinate totally crazy things. But you can always cross-check, and if you really understand the subject, you know.

**Sune:** So if you understand enough to reconstruct it yourself, you'll catch it. But you need a kind of bullshit detector.

**YY:** That's true, for sure. But it did amazing stuff. I had something pretty messy, and – I'd never bothered, because I thought it was overkill – it suggested, "do you want to embed all this information so we can search it more efficiently?"

**Sune:** Just to give people a sense of how capable it is: if I wanted to take an old set of notes I'd kept over the years – say, in Apple Notes – export them to Markdown, and explore them in some embedding space, that would be a huge undertaking for me. I'd have to figure out the right tool, how it'd work, do a ton of data cleaning. But with this kind of tool you can set that up in a very short time. And of course you can do the same with a research corpus.

**YY:** Yeah, you can build the infrastructure that helps you navigate your own space.

**Sune:** And this ability to code – you were saying you don't really need to code anymore, in a certain way. Another place you can use it without too much danger is data visualization. In the early days of our work together, we spent a huge amount of time making beautiful plots in – I can't even remember what was cool back then. Then D3 came out. D3, for me, was always a pain. I could get a network running in it, but coming from Python it was a whole saga. Now you can say, "I wrote a paper, I want a website for it, let's make all the plots interactive." You hand over the data, and it produces insanely beautiful D3 visualizations of every plot in your paper, and suddenly you have this gorgeous re-representation of what you did.

**YY:** Yeah. Data visualization is now more of a critique process, an iteration process, rather than coding. But there's an interesting point – many people have already said it – your taste now matters much more. You can totally produce something ugly and uninformative; the chance is lower, but you can still do it if you can't distinguish a good visualization from a bad one, and the principles behind it.

**Sune:** Maybe we can jump onto a big side-track here, a question I'd planned to save for later. You have all the experience and skill to use these tools – you learned to code the hard way, you're a great coder, you know how to make visualizations, you know how to think things through. When I want a D3 visualization, I also know what the constraints are. I can say, "start with a planar graph, put a little force between the nodes so they move around naturally, and squeeze it into this container so it doesn't float off the sides," and it builds the visualization. But if you don't have a language for those things, if you don't know the underlying science, you can't really use these tools. So it becomes an advantage for old farts like us, and something subtly different for young people and students. How do you think about that change – what should we be teaching students? How do we make sure the next generation is on board?

**YY:** Yeah, that's *the* question. I keep thinking about it, and it's not easy. There are certain things we can totally skip – we're not learning computer architecture or assembly anymore, so at that level we can skip a lot of the detail. A lot of programming education was just figuring out "why doesn't this code run?" – and it's usually a semicolon here or a bracket there. So that maybe isn't the thing to focus on. But at the same time – how do you train your eyes and nose to smell that something funky is going on?

**Sune:** I think there's also something that comes out of physics – you and I are both physicists by training – a certain discipline in how you even think. You learn one big theory, then a completely different one, then another, and along the way it's not that knowing quantum mechanics is useful per se – it's that your brain acquired the discipline needed to learn quantum mechanics. That structure, that muscle, that discipline, is what makes you good at thinking through all kinds of problems in a principled way. And programming is one of the ways you take this soft human brain – built for navigating nature, or whatever it's built for – and turn it into a better analytical machine. That's what we do as scientists. So do we lose that, you think?

**YY:** Exactly. One thing I keep thinking: we've basically replaced eight to ten hours of field work – hard physical labor – with maybe a couple of hours a week of hard work at the gym.

**Sune:** I see you posting about protein and all that, so you're staying in shape.

**YY:** In a way, we may need a *mental* gym – deliberately doing the hard mental work, regularly. And that should maybe be part of the point of education, the classroom environment. That's a rare opportunity to really nudge students into doing their own work without a device. So maybe we should put way more effort into making those classrooms precious time for exactly that.

**Sune:** And that makes it challenging for us too, because our brains can atrophy very quickly.

**YY:** Oh, I'm aware – I'm kind of embedded in Claude Code 24/7.

**Sune:** So one part is classroom teaching. What about your own students – PhDs, postdocs? How do you talk to them about AI? What advice do you give?

**YY:** Good question. I should do better. I encourage them to play with it and learn how it works, because it's hard to imagine a future where they don't use AI in research and are still very successful. The current students are senior enough, and I trust their judgment – they already know the basics, so I don't worry too much about them. But there's an incoming cohort, and that's the headache.

**Sune:** That's where we should worry. Because – you were hinting at it, and then I distracted you – the important thing is that, as you say, the semicolons aren't the important thing to learn from coding. There *are* important things to learn from coding, and from learning theories of how the world works – but what are they? What should we be doing in the classroom gym? That's yet to be determined. We haven't figured it out. But that's the big question.

**YY:** One thing I keep thinking about: I remember an example classroom activity – from Vietnam, or somewhere – in a computer-science class. No computer. Just a hard algorithm question, with pen and paper, to come up with an algorithm and analyze why it's efficient. That kind of work is still really valuable. I'm also thinking about journal club – reading a paper in a deep way. I'm really concerned that many young students now "read" a paper by dropping it into an LLM and asking a bunch of questions. That's quite concerning. A lot of the mental-gym work might just be really focused reading. But maybe there are also ideas in recreating something – I still feel I read papers most carefully when I really needed them for my own work. When you really need to know what some other group did, and the code isn't available, so you have to figure out how they even coded it up – that's when you get in deep and go, "wait a minute, *this* is what they did." I think that could be streamlined with agentic coding: you could reproduce a paper with Claude and learn a lot.

**Sune:** So that's also –

**YY:** But if it gets too good, and you ask it to reproduce a paper, it may do it in one shot –

**Sune:** Sure.

**YY:** – and then you don't learn much. So: suitable constraints.

**Sune:** I was also thinking – you mentioned the example from Vietnam, and my inner monologue went, "but how do we *find* those problems?" And then it was, "let's ask... let's ask Claude."

**YY:** That's a big problem. Instead of thinking for yourself –

**Sune:** Exactly. You've got a meta-problem.

**YY:** Totally. That pops up first.

**Sune:** It's scary. Luckily my kids are wonderfully skeptical and tease me whenever I look anything up at home – "here's old dad, trying to look something up online again." So – this is awesome. We got sidetracked into the bigger question, which was a good discussion, but I billed this as Claude Code for science. We talked about organizing your idea-structures and making them searchable – where in my own life does a new idea connect, how does my work link into the bigger picture I'm trying to build. But there are also a lot of practical things. I saw you have a skill that's like being "reviewer zero," and prepping things to submit to arXiv, and so on. So maybe we start with skills. And – maybe we should start super basic. If there's an AI doing chapters for this podcast, now's a good time for a chapter called "super basic."

We know that AIs get more expensive and a bit unhinged when the context window is very long. And yet one thing you do is keep a Claude session open all the time. We also know that in the chat interface, Claude comes in fresh every time – a new instance, knowing nothing. So let's go through this one step at a time. You have a main Claude window you use on your computer and access from different places. Where is that? Does it remember everything you said? Do you make it forget once in a while?

**YY:** So, basically it's an LLM: the context prompt gets injected, it produces a new token, that gets injected, then the next token, and so on. You can keep a main session open – it's up to you, you can restart whenever. Claude has a kind of remote control, and Codex you can also reach through mobile, which means it's synced across your phone and your computer, so you can have one continuous session. When the context grows, a lot of information – most of it not very useful – gets injected, so the quality of the answers can degrade, and you spend more money. There are multiple ways to handle it. One is: don't think about it. Just do whatever you want, because they're building the harness to address exactly that. I feel Codex is a bit better here – you don't have to think as much about context-length issues. Claude is more hands-on. By default it does something called *compacting*: it asks another model to summarize what happened and what's most essential, then starts a fresh session with that summary injected, so you can continue. It can still miss critical information, so it's not perfect, and your mileage may vary. But it's a totally viable solution – just keep using the same window and it takes care of it. Occasionally it compacts, which is a bit slow. That's one option. The other is: whenever you finish a work session, just clear and restart. What Claude then loads is the system prompt – the harness, how to behave – and then your user-level CLAUDE.md or AGENTS.md instructions.

**Sune:** And that's important to say. That's one of the ways you keep persistent information between sessions: you can put a file – or have Claude put one – in whatever directory you're working in. You're always working in a directory; that's part of the harness. So you have a file there that Claude knows to read, to situate it: "this is what we're doing here." That's one of the key ways to get continuity with this maniac who wakes up fresh every so often.

**YY:** Right. There's a user-level instruction you can keep in your dotfiles, and then you can treat every directory as a specific context: whenever there's important information to provide, drop a CLAUDE.md or AGENTS.md file there. Then whenever Claude launches or starts working in that directory, it reads that and uses it for the session. One mistake I see a lot of people make is putting *too much* into those files, so they get really long. That's a problem, because it gets injected on every conversation turn, which grows the context very quickly. A lot of it doesn't need to be there, because – remember – Claude can use all the tools. It can read files, it can figure things out. Often it's better to let it figure things out than to write them all down in that file.

**Sune:** Yes. The less you tell it, the better, almost. But you mentioned another persistent thing: skills. How should people think about skills?

**YY:** I think it's unnecessarily complicated right now. There are skills, agents, commands –

**Sune:** They also have memories.

**YY:** – right. But you can think of all of them as just instructions –

**Sune:** Exactly. A text file.

**YY:** – and I think the distinctions will gradually disappear, and everything will just be a skill, or whatever. Even an agent: you don't really have to create one; if you have a skill, you can launch a subagent with that skill.

**Sune:** Try to explain that – both the agent and the skill.

**YY:** Let's do the skill first. A skill is just a text file with front matter that explains when it should be invoked, or when it can be used. That front matter is exposed to Claude up front, in every session, so Claude knows the inventory of skills you have. When it realizes "this is the moment to use this skill," it reads the file and follows the instructions inside. A skill can come with tools – a Python script, command-line tools, MCP, whatever – all tools Claude or the agent can use. You pack them together as a skill. It can be as simple as "commit and push whatever's changed in this directory," or as complex as "we have a paper, let's..." But let's do the simple one first. And it's always a good idea to work in a repository where you can commit to Git or GitHub, so that if Claude does something bad you can revert to an earlier state. Claude is very good with Git and GitHub.

**Sune:** One of the old pain points was that resolving a Git conflict could eat 20 minutes of your day on some stupid problem. Now Claude just does it. It can look back in time, see where things were, and if it accidentally deletes something it can usually restore it. So you're working in Git, and every time you're tired of typing "hey Claude, commit everything in this repo and push it to the remote," you decide, "I'm going to make a skill." What would that skill look like?

**YY:** The front matter would give the name of the skill and say it's invoked when the user says "let's commit," or "let's finish up," or whatever – when it should be read. The instructions would say: "now we're committing all the unstaged changes in the repository; first do this, then that, fetch all the remote upstream changes, compare, merge, push," and so on. You *can* write that down, but usually it's better to just ask Claude to create the skill. You say, "I want a new skill for when I want to commit and push all the changes – ask me questions to clarify."

**Sune:** And you answer some questions, and it creates it for you.

**YY:** Exactly. That's the skill.

**Sune:** And then you said they can be much more complex – like submitting a paper to arXiv, which is one you have.

**YY:** Yeah – *preparing* one.

**Sune:** Preparing, that's what I meant.

**YY:** It's very dangerous now with arXiv. In case you haven't heard, arXiv is very anti-AI: if they find any provable case of AI in your paper, they can ban you for a year, and you don't get to submit again – unless the paper has already been published. So they're pretty serious. So only *prepare*; don't necessarily submit without really checking. Anyway, a lot of the work is manual: you clean up the comments, prepare the BibTeX entries in specific ways, and so on. There are already packages that clean up your files, so the skill uses those existing packages and checklists to go through it – "do this, do that, check, check" – and just create a copy of the paper that's ready to upload. You can also run a reference-check skill, which I made too: it queries OpenAlex and other services to validate your entries, and flags "I can't find these – can you check?" And if you keep asking, it can web-search and check those entries manually. I've found that works pretty well in most cases.

**Sune:** And I've noticed this is one of the places where language models still hallucinate – scientific references. They come up with papers that are almost right; it's as if they have a paper in mind but can't recall the exact author list or title, so they produce something plausible. So it's incredibly important to run this kind of check, to make sure you're not putting even more garbage out there.

**YY:** Yeah. One important thing is that I also try to use the skill to inject DOIs, so it can verify them.

**Sune:** And just to be super clear, so I don't get canceled as a scientist: you should *not* just have Claude invent a bunch of references, "fix" them, and call it fine. I mean this seriously – it's crucial to cite the relevant papers and not just produce lazy citations. But it's also important to check, because you might lazily say "fill in this paper that I know exists and have read," and it still fills in something garbage. So check.

**YY:** Yeah.

**Sune:** All right, super cool. But you mentioned something about agents and skills you wanted to explain. Let's get into that.

**YY:** A subagent is just a Claude session that Claude can spawn. It can spawn many at once. The main agent spawns an agent, the agent does something and reports back – it's all text – and then the main agent looks at the result and acts on it. So, again, think of an agent as a kind of tool Claude can use.

**Sune:** Can you say more, because this is something I actually haven't used. Can you have a list of agents with specializations, connected to skills?

**YY:** One way is to create an agent file – again, instructions – telling the agent what to do and what to report.

**Sune:** And how do you invoke it while you're working?

**YY:** You ask: "launch a subagent with this skill." It's the same thing, like the /agents command.

**Sune:** So if you want an ultra-critical subprocess – say you're producing something and want it to have the "reviewer three" attitude toward the whole project – you can have an agent with that attitude and say, "use it on this last piece of text." But the important thing is, you're not watching everything the subagent does; you only see what filters back through the main agent.

**YY:** Right. So a subagent is useful for things like "put this paper's information into my wiki." It just goes off and does the work, and I don't have to watch what's happening in there.

**Sune:** It's simple enough that you trust it'll get done without you babysitting every step. Very cool.

**YY:** And you can invoke those agents through the skill – just say "launch a subagent with this skill." So it's more or less the same thing. Claude Code also has an agent view now: if you type the agents command, you get a slightly different view with a list of subagents, and you can use the arrow keys to step into an agent and back out, to see what they're actually doing. That's useful when you spawn many, many agents. But these days I tend to keep things manageable, a single window, because I do feel a bit of what people call "AI psychosis."

**Sune:** Yes.

**YY:** It's very fragmenting for your attention. It might start something that takes three minutes, and you think, "oh, I've got three minutes, let me answer email," and then you come back, and it's this very task-switchy mode that's not good for your brain or your focus.

**Sune:** Right now it nudges you in that direction, because it's not fast enough to make you stick with the window, but it's also not long enough – I mean, you can build a verification system and let it run for, I don't know, 24 hours, but it's not quite there yet. So it's in the middle, and it really encourages you to constantly switch context, which is not great.

**YY:** No, it's terrible.

**Sune:** I can almost feel it. After a whole day working with Claude, my brain is completely scattered, and it's much harder to sit down and just relax, because you feel you should constantly be –

**YY:** And Claude is also very flow-like, because it can keep you at the right difficulty level, especially with a couple of windows open. It feels really great to use. But at the end of the day, there's a bill to pay.

**Sune:** For sure.

**YY:** Yeah – counterproductive.

**Sune:** Exactly. All right, awesome. But just so people understand how to get going in practice. Let's say you decide, "I want to grab some of YY's skills and put them on my computer." We don't have to cover all of them. You also have one that critiques a manuscript before you send it off, with principles for getting feedback before submission, which I think is really helpful. And because it's all plain text, people can just read the instructions, which is nice. So say you now want to try this for your science – they know how to find you, it's in the show notes. How do they get going with the skills in practice?

**YY:** I'd start from really simple skills, like "commit and push" – just ask Claude to create them, then open the skill text to see what's happening. Get an understanding of what's going on first. After that you can try more. I have a package – a plugin – called Claude Scholar, which is on GitHub. You can probably just point Claude at the URL and ask it to install.

**Sune:** And if people want to know where on the computer the skills actually live –

**YY:** On a Mac, I believe it's the `.claude` directory in your home directory. Inside it there's a CLAUDE.md, plus agents, skills, memories, plan – all those folders live there. So you can navigate there and open the files and read the instructions. The way I do it: I have a big dotfiles folder that manages the skills, and a script that symlinks them into the `.claude` directory. So on a new computer I just install the dotfiles folder, and all the skills are there – same for Codex and the other agents. It makes it easy to move between computers and keep everything synced.

**Sune:** We could do a whole episode on dotfiles, but I just wanted people to have a sense of where this stuff lives. One of the things I love about it is exactly that it's all plain text. You can go in and see what Claude remembers of the time you spent together, what it noted in the MD file about the projects. There's something nice about being able to see and change all of these things. It's out in the open.

All right – we're already ten minutes past the hour, and people are going to be angrily yelling at me here at home, and you have a day to get to. I feel like we only scratched the surface, but hopefully we got some things down. Maybe one last topic: portability. As you said, when Claude 4.6 came out, it suddenly got really, really good, and 4.7 is also fantastic. Right now Claude is where I spend most of my time; you keep mentioning Codex; there's also Google's coding agent. How do you think about making all of this portable? It's a bit like investing in an ecosystem. If everyone is addicted to Claude, they can raise prices, and maybe it becomes untenable; or maybe someone else suddenly gets much better and you want to switch. How do you think about portability – maybe also running a local LLM if you have a powerful machine at home?

**YY:** The biggest worry for me about this ecosystem is that very few companies can dominate all these models and agents. That means they have the power to control your thought, essentially. That power is probably the biggest danger we're facing. So I think we should really push for standards, portability, open source – open-source models, open-source harnesses. I mainly use an open-source agent, plus some open-source alternatives. One nice thing UVA provides – and many universities do – is that they install huge models on the research-computing system and open that API endpoint to the university community. That's nice, because you can use those open models with an open harness, and it can replace many of the tasks you'd do with Claude products without locking you into one service. The problem is that the frontier keeps moving: once you've tried the best model right now, it's hard to go back to a slightly inferior one. That's the main challenge. But open-source models keep getting better, and we're at the point where even an open-source model is perfectly capable of doing 80 or 90% of what you do. So I think everyone should try these open alternatives and promote them.

**Sune:** I completely agree. And I also agree it's almost impossible to actually use the open-source ones day to day, because you want the most capable model, and the smallest misstep is super annoying when you know it could just work.

**YY:** But the other thing open-source and local models give you is very strong privacy.

**Sune:** Yes, totally.

**YY:** Your data doesn't have to go to certain parties.

**Sune:** No. I've been thinking about taking all my email and embedding it to get a sense of everything – and that I'd never share with Claude. I'd use a local model for that. I'm still too scared to touch it.

**YY:** Yeah, me too.

**Sune:** But it was an idea. Maybe if I get some innocent little thing running strictly on my own machine, that nobody can see into, it could be fun to make a timeline.

**YY:** In a way, ironically, people are now buying Mac Studios and Mac minis precisely for these use cases.

**Sune:** The big topic I wanted to reach but didn't: increasingly I hear people say, "I don't need grad students anymore, because it can basically do a grad student's job." I think that'll be a real issue – especially in math, where the models are super capable – in a high-pressure, publish-or-perish environment where you have to be brilliant at all times. In the old days you'd get a grad student to amplify your output; now maybe you'd just have agents do it. And then we cut out one more layer of the ecosystem.

**YY:** Yeah, that's a full-day podcast topic on its own.

**Sune:** Exactly. A self-reinforcing system, and –

**YY:** Yes, exactly.

**Sune:** – and then all the deskilling. But I think we covered a lot. Thank you so much for taking the time to explain this. I don't know how to end on a good note, but maybe you say bye, and we'll cut it.

**YY:** Thanks for having me – so good to see you.

**Sune:** You too, man. Awesome. All right, we'll cut it here.
