---
title: "Directions"
date: 2014-09-10 12:19:00
slug: "directions"
status: publish
author: "sunelehmann"
original_url: "https://sunelehmann.com/directions/"
images: ["/assets/20140910_directions/screenshot-2022-11-18-at-09.54.04.png"]
---

<style>
.journey{list-style:none;margin:1.5em 0 1.5em .5rem;padding:0;max-width:34rem}
.journey li{--c:var(--fg-muted);position:relative;margin:0;padding:.15em 0 .15em 1.6rem;border-left:4px solid var(--c)}
.journey li::before{content:"";position:absolute;box-sizing:border-box;left:-8px;top:.55em;width:12px;height:12px;border-radius:50%;background:var(--bg);border:3px solid var(--c)}
.journey .leg{padding:.6em 0 .6em 1.6rem;color:var(--fg-muted);font-size:.92em}
.journey .leg::before{display:none}
.journey .strain{--c:var(--accent-oxblood)}
.journey .tram{--c:var(--accent-olive)}
.journey .walk{--c:var(--accent-sienna);border-left-style:dashed}
.journey .change::before{box-shadow:0 0 0 3px var(--bg),0 0 0 6px var(--accent-oxblood)}
.journey .here{--c:var(--accent-sienna)}
.journey .here::before{width:14px;height:14px;left:-9px;top:.5em}
.journey .dest{--c:var(--accent-sienna);border-left-color:transparent}
.journey .minor{color:var(--fg-muted);font-size:.9em}
.dirtable{border-collapse:collapse;width:100%;font-size:.95em;margin:1em 0 1.5em}
.dirtable th,.dirtable td{text-align:left;padding:.45em .7em .45em 0;border-bottom:1px solid var(--rule);vertical-align:top}
.dirtable th{font-weight:600}
</style>

## DTU

My office is on the first floor of Building 321, room 126, on DTU's campus in Lyngby.

### From central Copenhagen, by train

1. **S-train to Lyngby.** From Nørreport (or København H, Østerport, wherever you are), take line **A** towards Hillerød or line **E** towards Holte and get off at **Lyngby St.** The ride takes about a quarter of an hour. On weekdays each line runs every ten minutes, so in practice there is a train roughly every five minutes. In the evenings and at weekends only line A runs: every ten minutes during the day, every twenty later on.
2. **Light rail to campus.** At Lyngby, a tunnel leads straight from the S-train platforms to the light rail stop. Take the light rail towards **Lundtofte**. It runs every five to eight minutes during the day on weekdays and Saturdays, every ten minutes in the evening and on Sundays. Three stops later you are at **Akademivej (DTU)**, the first of two stops on campus.[^1] Under ten minutes.
3. **Walk.** From the Akademivej stop, follow the tracks north for about 450 metres. Building 321 is on your left, just before the tracks bend east. Five or six minutes, depending on the weather and your attitude towards it.

<ol class="journey">
<li class="strain"><strong>Nørreport</strong> <span class="minor">(or any S-train station in town)</span></li>
<li class="leg strain">S-train, line A towards Hillerød or line E towards Holte. About 15 minutes.</li>
<li class="tram change"><strong>Lyngby St.</strong> – change to the light rail; the tunnel from the platforms takes you straight there.</li>
<li class="leg tram">Light rail towards Lundtofte. Under 10 minutes.</li>
<li class="tram minor">Lyngby Centrum</li>
<li class="tram minor">Fortunbyen</li>
<li class="tram here"><strong>Akademivej (DTU)</strong> – get off here.</li>
<li class="leg walk">On foot, north along the tracks. About 450 metres.</li>
<li class="dest"><strong>Building 321</strong>, first floor, room 126.</li>
</ol>

All in all, something like half an hour from Nørreport. For live departures, [rejseplanen.dk](https://www.rejseplanen.dk) knows everything, and [dinletbane.dk](https://dinletbane.dk/) has the light rail timetable.

### How often things run

<table class="dirtable">
<thead><tr><th>Leg</th><th>Weekdays, daytime</th><th>Evenings and weekends</th></tr></thead>
<tbody>
<tr><td>S-train, Nørreport to Lyngby</td><td>About every 5 minutes (lines A and E, every 10 minutes each)</td><td>Line A only: every 10 minutes during the day, every 20 in the evening</td></tr>
<tr><td>Light rail, Lyngby to Akademivej (DTU)</td><td>Every 5–8 minutes</td><td>Every 10 minutes in the evening and on Sundays; Saturday daytime as on weekdays</td></tr>
</tbody>
</table>

### The last 450 metres

<!-- dirmap:start -->
<svg class="dirmap" xmlns="http://www.w3.org/2000/svg" viewBox="-270 -330 970 950" role="img" aria-labelledby="dirmap-title dirmap-desc">
<title id="dirmap-title">Map of DTU Lyngby Campus with the light rail and the walk to Building 321</title>
<desc id="dirmap-desc">The light rail enters campus from the south along Lundtoftegårdsvej, runs west along Akademivej, north up Koppels Allé and east along Anker Engelunds Vej before leaving towards Rævehøjvej and Lundtofte. From the Akademivej stop it is about 450 metres north on foot to Building 321.</desc>
<style>
.dirmap{width:100%;height:auto;display:block;margin:1.5em 0;font-family:Inter,system-ui,sans-serif}
.dirmap .paper{fill:var(--surface-card,#f1f0ea)}
.dirmap .bld{fill:var(--bg,#fbfbf8);stroke:var(--fg-muted,#666);stroke-width:.8;stroke-opacity:.6}
.dirmap .rd{fill:none;stroke:var(--fg-muted,#666);stroke-linecap:round;stroke-linejoin:round}
.dirmap .rd-mw{stroke-width:7;stroke-opacity:.22}
.dirmap .rd-major{stroke-width:4.5;stroke-opacity:.3}
.dirmap .rd-minor{stroke-width:2.5;stroke-opacity:.25}
.dirmap .rd-path{stroke-width:1;stroke-opacity:.22}
.dirmap .tram{fill:none;stroke:var(--accent-olive,#7e8d20);stroke-width:6;stroke-linecap:round;stroke-linejoin:round}
.dirmap .tram-core{fill:none;stroke:var(--bg,#fbfbf8);stroke-width:1.5;stroke-dasharray:9 9;stroke-opacity:.9}
.dirmap .walk{fill:none;stroke:var(--accent-sienna,#b8451e);stroke-width:6;stroke-dasharray:10 9;stroke-linecap:round;stroke-linejoin:round}
.dirmap .stop{fill:var(--bg,#fbfbf8);stroke:var(--accent-olive,#7e8d20);stroke-width:4}
.dirmap .stop-here{stroke:var(--accent-sienna,#b8451e)}
.dirmap .b321{fill:var(--accent-sienna,#b8451e);stroke:none}
.dirmap .bus{fill:var(--accent-oxblood,#992c44)}
.dirmap text{fill:var(--fg,#0e0e10);font-size:17px}
.dirmap .lbl-stop{font-weight:600;font-size:19px}
.dirmap .lbl-stop tspan.sub{font-weight:400;font-size:15px;fill:var(--fg-muted,#666)}
.dirmap .lbl-road{font-size:15px;fill:var(--fg-muted,#666);letter-spacing:.06em}
.dirmap .lbl-here{font-weight:600;font-size:19px;fill:var(--accent-sienna,#b8451e)}
.dirmap .lbl-muted{fill:var(--fg-muted,#666);font-size:15px}
.dirmap .halo{stroke:var(--surface-card,#f1f0ea);stroke-width:5;stroke-linejoin:round;paint-order:stroke}
.dirmap .scale{stroke:var(--fg,#0e0e10);stroke-width:2}
.dirmap .arrow{fill:var(--fg,#0e0e10)}
@media (max-width:600px){
  .dirmap text{font-size:24px} .dirmap .lbl-stop{font-size:26px} .dirmap .lbl-stop tspan.sub{font-size:20px}
  .dirmap .lbl-road{font-size:21px} .dirmap .lbl-here{font-size:26px} .dirmap .lbl-muted{font-size:21px}
}
</style>
<defs><path id="lp-aev" d="M-219,-174 L-196,-172 L-157,-164 L34,-104 L48,-100 L91,-94 L121,-86 L318,-23 L388,-1 L399,1" fill="none"/><path id="lp-ak" d="M-121,509 L-108,509 L-91,504 L-79,505 L109,563" fill="none"/><path id="lp-lg" d="M285,541 L358,202" fill="none"/><path id="lp-mw" d="M519,-49 L570,-291 L648,-651" fill="none"/></defs>
<rect class="paper" x="-270" y="-330" width="970" height="950" rx="6"/>
<g class="roads">
<path class="rd rd-path" d="M-213,36 L-186,44 L-164,42 L-94,64 M22,653 L79,633 M-170,318 L-234,299 L-218,245 L-300,219 L-305,226 M-207,307 L-194,264 L-221,256 M48,-56 L-4,108 L2,110 L-11,150 L-27,205 L-35,222 L-51,282 L-120,503 M-124,559 L-131,581 L-127,582 L-122,567 L-106,572 M-133,566 L-124,559 L-97,568 M-112,129 L-152,117 L-161,118 L-168,116 M-286,570 L-282,566 L-276,566 L-277,538 L-263,535 L-261,528 M81,53 L188,86 L192,82 M-131,581 L-142,578 L-144,585 L-278,544 M-239,657 L-276,558 M-251,624 L-235,612 M-44,87 L-1,99 M-36,430 L-25,434 L-17,449 L-3,447 L10,448 L18,452 L20,460 L36,462 M-273,99 L-267,96 L-251,102 L-257,96 L-277,84 L-288,70 L-293,69 M-145,329 L-106,337 L-104,341 L-80,349 L-83,355 L-79,357 M-131,537 L-126,523 L-69,541 L-83,591 L-88,589 M-98,183 L-91,170 L-83,143 M-128,173 L-101,88 L-87,93 M-81,529 L-85,529 L-97,568 M-31,204 L-29,198 L-31,195 L-24,167 L-19,148 L-14,139 L-9,118 M-24,167 L-49,166 L-60,150 L-83,143 M-53,163 L-66,160 L-72,162 L-87,157 M-83,143 L-69,98 L-87,93 M-80,349 L-77,339 L-84,337 L-83,333 M-172,160 L-175,156 L-230,137 M-117,177 L-115,169 L-106,172 L-103,163 M-278,544 L-293,526 L-289,518 M64,354 L47,349 L40,342 L29,344 L-6,334 M-66,601 L-65,597 L-54,596 L-47,590 L-40,587 L-36,582 L-30,583 L-21,578 L-14,578 M-235,169 L-242,191 M-258,177 L-242,182 L-239,170 L-236,171 M-238,178 L-220,186 L-219,184 L-195,193 L-194,190 L-182,194 M64,354 L104,366 M58,393 L70,356 M84,411 L99,365 M-97,568 L-85,572 L-89,583 M-98,573 L-106,597 L-100,599 L-110,626 L-107,631 L-89,642 L-55,649 L-46,646 L-38,631 M-126,523 L-125,517 L-85,529 M-125,517 L-194,495 M-106,513 L-100,519 L103,583 M-98,546 L-123,538 M-234,299 L-240,319 L-245,325 M-300,-128 L-288,-132 L-269,-133 L-259,-136 L-243,-134 L-235,-135 L-220,-141 M-59,503 L87,36 L115,-63 M79,633 L170,602 M-23,328 L-51,319 M-51,282 L5,298 M-66,81 L-41,1 M-24,614 L-66,601 M180,335 L10,281 M38,131 L75,143 L76,139 M-152,249 L-51,282 M12,60 L-10,53 L-8,48 M74,75 L35,62 M8,53 L31,60 M-235,612 L-253,565 L-262,558 L-279,551 L-309,522 M-251,102 L-173,128 M-223,134 L-230,155 M-83,81 L-69,37 M-71,-8 L-97,75 L-67,85 L-66,81 M201,585 L173,588 L121,575 L118,586 L125,600 L124,603 L100,612 L83,624 L42,639 L34,638 L-13,656 L-34,657 M-157,370 L-192,487 M-221,478 L-184,362 M63,110 L105,123 L107,117 M29,220 L51,227 L53,220 M179,337 L9,284 M7,293 L176,346 M38,193 L75,205 M-281,465 L-109,517 L-101,517 L-90,509 L-84,509 L-62,514 M-59,503 L45,536 L93,548 L105,549 L112,537 M-283,453 L-120,503 L-83,497 L-59,503 M-65,514 L155,582 L177,581 L253,550 L270,549 L274,556 L274,564 L259,619 L253,652 M381,22 L385,28 L386,32 L280,526 L240,540 L190,565 L178,569 L162,570 L-77,500 L-92,500 L-118,505 L-191,484 L-198,485 M-221,478 L-222,473 L-283,454 M-180,126 L-172,104 L-176,100 L-167,66 L-188,59 L-224,70 L-235,83 L-245,86 L-251,102 M404,566 L413,572 L416,581 L401,651 M262,575 L260,595 M302,563 L288,583 M265,574 L292,566 M292,566 L333,554 L364,557 M364,557 L404,566 M615,-304 L606,-286 L451,438 L449,535 L429,654 M245,124 L257,124 L368,159 M238,428 L245,426 L265,432 M256,472 L228,463 M180,526 L200,461 L198,455 M309,431 L164,386 M229,515 L248,513 L265,432 L273,419 M265,60 L299,69 L307,67 M306,140 L294,181 L280,201 L274,230 L265,237 L254,276 L260,292 L255,308 L259,321 L258,325 L237,363 L219,422 M118,534 L159,540 L188,533 L193,527 M718,413 L703,410 L708,421 L698,475 L689,491 L668,498 M259,321 L277,328 L279,325 M280,203 L259,197 M269,234 L289,239 L290,235 M675,582 L659,632 L664,634 M285,110 L279,131 M295,113 L302,88 M253,100 L331,124 M254,276 L233,271 M278,172 L309,182 M222,363 L247,370 M337,73 L381,90 M310,80 L263,66 M601,83 L583,166 L583,171 L590,186 L591,192 L578,251 L580,260 L608,298 L605,331 L608,338 L692,399 L695,404 M695,404 L702,392 L712,383 L724,378 L739,376 M733,234 L732,223 L727,216 L722,196 L708,177 L708,154 L699,133 L686,113 L683,103 L689,96 L703,89 L724,87 M702,392 L728,273 L733,234 M566,106 L595,113 L610,109 L644,113 L650,110 L657,98 L668,87 L718,66 L725,54 L736,44 L738,38 L737,31 L718,3 L717,-5 L718,-9 L730,-20 L736,-32 M637,630 L656,635 L659,632 M629,655 L648,596 L660,596 L672,591 M177,157 L196,94 L188,86 M266,653 L280,602 M201,593 L265,574 M170,602 L193,595 M271,501 L293,506 M280,602 L260,595 M280,602 L293,542 L285,541 M294,637 L285,647 L275,651 M211,658 L211,645 L206,637 L197,631 L183,625 L169,626 L122,643 M412,603 L420,588 L427,557 L418,555 M380,25 L371,46 L370,62 L360,80 L358,93 L359,111 L352,124 L349,137 L351,155 L336,208 L336,218 L329,233 L324,257 L319,299 L272,493 L270,512 L275,527 M269,550 L263,558 L242,566 L201,585 M693,77 L683,73 L681,69 L679,63 L680,59 L719,43 L730,20 M181,647 L183,625 M208,641 L201,647 L193,649 L181,647 L175,656 L135,659 M197,396 L210,367 M251,413 L260,383 M601,83 L631,-54 L635,-58 L668,-71 L674,-92 M99,310 L171,81 M248,513 L270,512 M275,527 L254,533 L214,553 L178,567 L169,569 L160,569 L126,558 L121,556 L119,549 L289,2 L292,-1 L299,-2 L380,25 M219,97 L227,99 L239,109 L254,113 M263,596 L254,628 L251,651 M280,526 L274,556 M718,66 L739,71 M734,167 L724,154 L725,137 M695,404 L647,569 L620,652 M314,59 L314,59 M193,649 L195,660 L175,656 M-96,-364 L-128,-341 L-140,-311 M5,-311 L10,-318 L25,-365 L24,-367 M87,-149 L363,-64 L369,-64 M-84,33 L-110,25 L-111,27 L-126,23 L-125,21 L-198,-2 M-66,-80 L-55,-111 M-60,-44 L-30,-35 M-10,53 L-53,40 M-285,48 L-275,36 L-261,9 M52,25 L98,39 M-269,-332 L-281,-327 L-292,-319 L-300,-304 L-310,-308 M-88,-293 L-83,-309 L-75,-307 L-70,-304 L-67,-298 L-72,-286 M-67,-299 L-47,-301 L-44,-308 M-94,-295 L-87,-293 L-78,-294 L-68,-301 M-298,-21 L-292,-44 L-270,-79 L-267,-88 M-274,-133 L-274,-122 L-267,-118 L-262,-110 L-267,-88 M-56,-71 L-52,-70 L-58,-51 M-53,40 L-84,33 M58,-80 L55,-78 L48,-56 M-53,-227 L-68,-183 M-101,-242 L-53,-227 L-34,-288 M-101,-242 L-105,-228 L-58,-213 M-38,-276 L-8,-267 M-49,-240 L-19,-231 M-125,-190 L-123,-195 L-107,-190 L-105,-198 L72,-143 M-43,-261 L95,-218 L72,-143 M72,-143 L69,-132 L-39,-166 M69,-132 L61,-104 M-219,-182 L-224,-197 L-231,-202 L-241,-217 L-225,-245 L-219,-263 L-209,-279 L-205,-298 L-196,-309 L-189,-330 L-161,-363 M-92,-82 L-99,-60 M-97,-60 L-100,-60 L-125,21 M-294,-35 L-270,-27 M-264,-62 L-246,-57 L-226,-58 M-276,-69 L-264,-64 L-265,-57 L-281,-62 M-307,-71 L-285,-57 M-112,-319 L-121,-326 L-117,-335 M-121,-348 L-117,-335 L-110,-330 L-114,-302 M-248,-326 L-229,-316 M-254,-176 L-259,-181 L-263,-194 L-261,-220 L-255,-240 L-248,-257 L-209,-318 M-305,-141 L-218,-157 L-188,-158 L-167,-154 L37,-91 L56,-84 L87,-69 L393,26 M388,-1 L384,-5 L103,-94 L56,-103 L-173,-174 L-210,-180 L-231,-180 L-254,-176 M-218,-154 L-219,-182 M-25,-272 L-20,-262 L-19,-254 M-8,-267 L-3,-283 L104,-248 L95,-218 M-140,-311 L-149,-287 L-170,-294 M-48,-245 L-146,-276 M98,-228 L-10,-261 M-52,35 L-5,49 M-31,-32 L-20,-66 M-122,10 L-81,22 M-147,-13 L-142,-30 L-145,-32 L-158,-36 L-164,-20 L-146,-14 M-156,-38 L-149,-61 M-61,-154 L-58,-158 L-64,-165 L-63,-170 L-58,-173 L-58,-176 M-58,-173 L-50,-163 L-38,-170 M-79,-147 L-66,-155 L-61,-154 L-55,-145 L-47,-140 M-237,-210 L-248,-198 L-257,-181 M-85,37 L-193,4 M288,-40 L211,-62 L102,-97 L65,-103 L-47,-137 M58,-80 L89,-65 L275,-9 L278,-5 M58,-80 L-144,-144 L-179,-154 L-201,-156 L-218,-154 L-301,-139 M14,53 L-5,47 L-5,49 M-93,-58 L-95,-59 L-88,-81 M-100,-59 L-177,-82 M-92,-82 L-56,-71 L-53,-81 L-28,-73 L-27,-77 M-47,-137 L-181,-179 L-216,-182 L-255,-179 L-258,-184 M-9,-221 L12,-214 M-32,-176 L-18,-223 M65,-174 L45,-180 M-204,-10 L-210,9 L-215,17 L-219,18 L-257,6 M-238,12 L-239,-5 L-236,-14 L-238,-17 M-27,-77 L-10,-71 L-9,-75 M46,-50 L-12,-68 L-20,-66 M-254,-176 L-306,-167 M-17,-341 L-10,-368 L23,-358 M94,-190 L123,-284 L118,-291 L72,-305 L73,-311 M130,-305 L137,-326 L70,-347 L71,-351 M20,-6 L-25,-22 M-21,-36 L25,-22 M-105,-198 L-103,-204 L-119,-209 L-118,-213 M-47,-137 L-37,-173 M-304,-170 L-279,-175 L-278,-214 L-272,-241 L-262,-263 L-218,-334 M-216,-333 L-268,-246 L-275,-223 L-276,-175 L-279,-171 M-257,-181 L-278,-177 M-192,27 L-197,26 L-192,11 L-200,8 M-34,-288 L-22,-326 M-60,-44 L-71,-8 M-41,1 L-31,-32 M436,-171 L398,-179 L361,-190 L359,-182 M340,-224 L374,-333 M592,-316 L595,-316 L601,-324 L607,-324 L613,-315 L615,-304 M154,-113 L134,-119 M440,-369 L423,-317 M424,-116 L381,-125 M615,-304 L621,-304 L613,-342 L617,-363 M360,-240 L388,-231 L393,-225 L401,-222 L405,-212 L398,-179 L349,-19 M717,-295 L734,-313 L737,-313 M454,-284 L464,-331 L472,-334 M444,-308 L344,-342 M469,-281 L426,-291 M465,-304 L460,-307 L446,-305 L353,-235 L346,-222 M446,-305 L456,-293 L463,-295 M203,-340 L168,-350 M237,-169 L308,-147 L301,-123 L233,-144 L240,-168 M451,-367 L441,-327 L446,-305 L444,-297 L433,-284 L428,-258 L421,-240 L420,-228 L423,-217 L414,-166 L406,-132 L398,-121 L386,-68 L383,-65 M324,-229 L357,-338 M615,-304 L591,-305 L591,-308 M626,-102 L710,-84 M674,-92 L688,-149 L702,-161 L736,-173 M601,-353 L600,-341 L591,-314 M346,-356 L347,-361 L322,-367 M203,-340 L209,-344 L225,-346 L346,-309 L353,-310 L390,-298 L426,-291 M423,-317 L408,-277 M672,-148 L674,-155 L671,-182 L659,-200 L657,-209 L659,-226 L658,-234 L642,-255 L632,-272 L624,-275 L621,-280 L618,-291 M371,46 L346,34 L336,32 L323,23 L315,23 L286,10 M115,-63 L121,-86 M386,-68 L416,-78 M717,-7 L702,-18 L699,-25 M669,-366 L655,-352 L646,-339 L619,-315 M604,-0 L667,13 M674,-155 L691,-141 L687,-114 L711,-88 M121,-86 L134,-119 M506,-275 L476,-283 L469,-281 M375,-33 L383,-14 L390,-9 M297,-68 L288,-40 M344,-217 L351,-215 L342,-187 M175,-248 L337,-197 L334,-189 M390,-9 L393,-12 L410,-8 M378,-54 L375,-33 M323,23 L322,45 M390,-9 L380,25 M390,-7 L313,-30 L306,-34 M313,-30 L304,-0 M195,-63 L187,-35 M130,-305 L123,-281"/>
<path class="rd rd-minor" d="M-265,650 L-270,612 L-276,587 L-286,570 L-304,551 M-308,229 L-305,226 M-245,325 L-284,457 M36,659 L45,653 L70,650 L72,648 M-287,484 L-251,495 M-292,501 L-256,512 M-244,470 L-261,528 M-247,481 L-283,470 L-297,515 L-261,528 M-41,322 L74,-46 L92,-41 L-23,328 M-175,333 L-149,342 M-184,362 L-157,370 M-179,348 L-153,356 M-184,362 L-170,317 L-144,325 L-157,370 M-301,163 L-290,129 L-281,123 L-273,99 M15,142 L33,147 M42,55 L60,61 M-75,431 L-57,436 M-51,354 L-34,360 M-152,249 L-128,173 M-216,237 L-195,235 M48,526 L84,411 L55,402 L14,533 M-176,173 L-132,187 M-191,222 L-147,235 M-185,205 L-142,218 M-181,189 L-137,203 M-195,235 L-172,160 M109,563 L103,583 L83,624 M19,517 L48,526 M24,501 L53,510 M39,452 L68,461 M29,485 L58,494 M44,437 L73,446 M49,420 L78,429 M34,469 L63,478 M-163,276 L-163,276 M-83,355 L-125,490 L-130,493 L-188,474 M89,403 L89,403 M-274,348 L-254,355 M-160,483 L-149,450 M-221,478 L-305,451 M-57,436 L-74,490 L-91,485 L-41,322 M-8,641 L6,641 L73,617 L85,619 M-8,641 L-92,614 L-94,609 L-88,589 M-192,487 L-195,498 L-224,489 L-221,478 M109,563 L-79,505 L-91,504 L-108,509 L-121,509 M-121,509 L-198,485 M-63,234 L-81,233 L-113,221 L-107,208 L-91,214 L-60,235 L-58,230 L-76,190 M-90,230 L-97,251 M-308,229 L-295,235 M11,291 L117,324 M-110,245 L-104,225 M-72,233 L-80,258 M-9,285 L7,290 M7,290 L11,291 M79,633 L72,648 M-18,248 L1,253 M-301,163 L-258,177 M83,624 L79,633 M18,557 L-8,641 M-28,280 L-9,285 M-23,328 L-57,436 M-199,-165 L-208,-120 L-96,-85 L-67,-77 L-66,-80 L-20,-66 L-16,-59 L46,-39 L-0,109 M-195,235 L-152,249 M-172,160 L-27,205 M-298,460 L-284,457 M-198,485 L-221,478 M-279,459 L-283,470 M170,155 L230,174 M120,139 L170,155 M272,539 L257,541 L186,572 L165,578 L148,576 L109,563 M209,419 L198,455 M233,445 L214,439 M217,519 L214,511 L238,428 L159,403 M253,100 L192,82 M117,324 L170,155 M126,507 L189,527 L229,515 M214,224 L234,230 M261,75 L308,89 M155,150 L110,297 M104,366 L164,386 M192,82 L218,-1 L263,13 L238,96 M199,164 L221,91 M128,237 L105,230 M587,79 L634,-137 L638,-146 L644,-152 L673,-163 M587,79 L567,171 L570,192 M587,79 L637,89 M591,61 L577,59 L554,162 L558,165 L568,167 M145,147 L167,79 M110,297 L124,301 M101,523 L119,529 M307,657 L317,622 M311,641 L294,637 M117,324 L178,342 M285,541 L272,539 M287,-10 L109,563 M198,164 L193,181 M139,253 L168,262 L186,206 M131,281 L158,289 L155,300 M122,447 L143,453 M-304,-4 L-210,25 L-203,2 M-235,-342 L-248,-326 L-279,-271 L-306,-213 M-294,-354 L-290,-355 L-215,-321 M-295,-278 L-253,-259 M-244,-273 L-234,-267 L-188,-253 L-182,-258 L-170,-294 L-164,-302 L-158,-307 L-140,-311 L-102,-298 M25,-365 L143,-330 M75,-110 L143,-330 M-156,-209 L-68,-181 L-81,-140 M94,-111 L94,-111 M-68,-353 L-77,-347 L-93,-352 M-309,-214 L-298,-210 L-295,-207 L-295,-188 M-261,9 L-241,-12 L-231,-33 L-218,-88 M-203,2 L-181,-76 L-218,-88 M132,-294 L16,-328 M-37,-173 L-8,-267 M-17,-232 L-17,-232 M-182,-71 L-104,-47 M-218,-88 L-208,-120 M-210,25 L-213,36 M-37,-173 L-68,-183 L-68,-181 M-81,-140 L-83,-133 M-304,-4 L-298,-21 M589,-299 L518,-300 M518,-300 L465,-304 M556,-334 L544,-289 L531,-262 L514,-180 L501,-33 M349,-53 L206,-97 M302,-50 L295,-30 M717,-295 L717,-289 M717,-295 L589,-299 M202,-257 L202,-257 M519,-49 L539,-110 L571,-244 L582,-308 L588,-326 M192,-370 L210,-364 M180,-264 L145,-275 M145,-156 L111,-166 M180,-264 L244,-246 M669,-134 L649,-139 L636,-77 M621,-80 L655,-74 L672,-148 M589,-292 L717,-289 M463,-295 L518,-293 M518,-293 L589,-292 M625,-113 L628,-112 M589,-43 L599,-41 L619,-138 M599,-41 L591,-5 L581,-8 M630,-162 L622,-153 L619,-141 M659,-158 L653,-161 L623,-162 L611,-153 M735,-88 L712,-93 L708,-74 M511,-273 L493,-194 L484,-188 L438,-182 M738,-54 L739,-48 L735,-17 L739,2 M595,40 L576,36 M295,-30 L287,-10 M134,-119 L210,-364 M285,-72 L281,-80 L225,-97 L213,-94 M544,-289 L519,-172 L512,-166 M96,-99 L96,-99 M154,-113 L149,-97 L201,-81 M201,-81 L344,-37 L349,-53 M307,-66 L302,-50 M206,-97 L154,-113 M111,-166 L94,-172 M611,-153 L589,-43 M581,-8 L587,-40 L596,-46 L610,-116 L625,-113"/>
<path class="rd rd-major" d="M273,599 L266,637 M388,54 L358,202 M358,202 L285,541 M285,541 L273,599 M60,-85 L75,-77 L115,-63 L394,22 M-219,-174 L-245,-172 L-266,-167 M-264,-156 L-226,-163 L-199,-165 M-267,-174 L-269,-205 L-268,-222 L-263,-239 L-253,-259 L-210,-330 M-297,-161 L-310,-160 M-304,-149 L-264,-156 M-266,-167 L-264,-156 M399,1 L121,-86 L91,-94 L34,-104 L-157,-164 L-196,-172 L-219,-174 M-266,-167 L-297,-161 M-266,-167 L-267,-174 M46,-93 L60,-85 M-199,-165 L-175,-161 L-148,-154 L46,-93 M463,-295 L399,1 M472,-334 L463,-295 M399,1 L394,22 M394,22 L388,54"/>
<path class="rd rd-mw" d="M452,199 L372,574 M501,-33 L452,199 M411,464 L519,-49 M519,-49 L570,-291"/>
</g>
<path class="bld" d="M-195,25 L-195,25Z M-51,45 L-51,45Z M-68,103 L-68,103Z M-229,132 L-229,132Z M115,142 L115,142Z M92,247 L92,247Z M22,327 L22,327Z M136,400 L136,400Z M-250,362 L-250,362Z M20,605 L20,605Z M-295,155 L-295,155Z M-80,138 L-80,138Z M-91,173 L-91,173Z M-240,167 L-240,167Z M-250,203 L-250,203Z M-32,468 L-32,468Z M-21,433 L-21,433Z M-9,396 L-9,396Z M52,534 L52,534Z M95,60 L95,60Z M53,195 L53,195Z M27,279 L27,279Z M-135,317 L-135,317Z M-238,325 L-238,325Z M-179,266 L-179,266Z M-231,45 L-231,45Z M-48,79 L-48,79Z M37,674 L37,674Z M48,673 L48,673Z M-265,312 L-265,312Z M-326,373 L-326,373Z M-236,169 L-236,169Z M-166,103 L-166,103Z M-108,421 L-108,421Z M-300,172 L-300,172Z M-99,90 L-99,90Z M-344,554 L-344,554Z M-363,602 L-363,602Z M-343,662 L-343,662Z M-287,398 L-287,398Z M70,289 L70,289Z M62,286 L62,286Z M75,243 L75,243Z M68,195 L68,195Z M82,150 L82,150Z M94,113 L94,113Z M-132,318 L-132,318Z M-182,370 L-182,370Z M-241,113 L-241,113Z M-100,374 L-100,374Z M-233,327 L-233,327Z M-138,356 L-138,356Z M-122,442 L-122,442Z M-98,368 L-98,368Z M-272,432 L-272,432Z M-151,275 L-151,275Z M-121,305 L-121,305Z M-44,505 L-44,505Z M-366,347 L-366,347Z M-266,268 L-266,268Z M-312,42 L-312,42Z M55,293 L55,293Z M-244,669 L-244,669Z M-178,64 L-178,64Z M-290,397 L-290,397Z M-108,421 L-108,421Z M136,72 L136,72Z M302,60 L302,60Z M174,59 L174,59Z M245,60 L245,60Z M204,98 L204,98Z M224,104 L224,104Z M251,429 L251,429Z M212,455 L212,455Z M242,470 L242,470Z M177,202 L177,202Z M182,419 L182,419Z M148,527 L148,527Z M127,73 L127,73Z M182,549 L182,549Z M309,130 L309,130Z M193,97 L193,97Z M241,261 L241,261Z M246,293 L246,293Z M269,309 L269,309Z M272,342 L272,342Z M229,350 L229,350Z M249,357 L249,357Z M285,252 L285,252Z M260,213 L260,213Z M282,188 L282,188Z M302,195 L302,195Z M273,65 L273,65Z M292,70 L292,70Z M582,641 L582,641Z M665,23 L665,23Z M646,599 L646,599Z M642,608 L642,608Z M614,644 L614,644Z M289,707 L289,707Z M112,628 L112,628Z M724,174 L724,174Z M717,169 L717,169Z M723,163 L723,163Z M729,168 L729,168Z M232,603 L232,603Z M235,249 L235,249Z M216,50 L216,50Z M239,58 L239,58Z M137,138 L137,138Z M218,478 L218,478Z M214,492 L214,492Z M209,507 L209,507Z M202,520 L202,520Z M-61,-404 L-61,-404Z M18,-337 L18,-337Z M-5,-261 L-5,-261Z M-36,-162 L-36,-162Z M-41,-276 L-41,-276Z M-61,-211 L-61,-211Z M-179,-190 L-179,-190Z M-207,-97 L-207,-97Z M-88,-76 L-88,-76Z M-59,-90 L-59,-90Z M103,-380 L103,-380Z M-49,-69 L-49,-69Z M-194,38 L-194,38Z M-217,-10 L-217,-10Z M-104,-301 L-104,-301Z M-61,-52 L-61,-52Z M-196,38 L-196,38Z M-331,-217 L-331,-217Z M-327,-330 L-327,-330Z M-279,-370 L-279,-370Z M-319,-361 L-319,-361Z M-140,-264 L-140,-264Z M-8,-362 L-8,-362Z M-103,-403 L-103,-403Z M-166,-245 L-166,-245Z M-126,-190 L-126,-190Z M-2,-301 L-2,-301Z M-273,-89 L-273,-89Z M-285,-12 L-285,-12Z M-263,-66 L-263,-66Z M-154,-56 L-154,-56Z M93,-408 L93,-408Z M-295,-65 L-295,-65Z M-264,-59 L-264,-59Z M-287,-34 L-287,-34Z M-307,-49 L-307,-49Z M-199,-78 L-199,-78Z M-127,14 L-127,14Z M-177,-248 L-177,-248Z M77,-291 L77,-291Z M-236,1 L-236,1Z M4,-166 L4,-166Z M29,-158 L29,-158Z M30,-250 L30,-250Z M55,-243 L55,-243Z M-137,-200 L-137,-200Z M-20,-391 L-20,-391Z M377,-444 L377,-444Z M365,-191 L365,-191Z M742,-403 L742,-403Z M341,-332 L341,-332Z M353,-196 L353,-196Z M415,-388 L415,-388Z M213,0 L213,0Z M701,-346 L701,-346Z M712,-420 L712,-420Z M608,-380 L608,-380Z M305,-354 L305,-354Z M688,-344 L688,-344Z M754,-311 L754,-311Z M735,-314 L735,-314Z M575,29 L575,29Z M621,-43 L621,-43Z M618,-30 L618,-30Z M616,-17 L616,-17Z M609,13 L609,13Z M606,26 L606,26Z M604,38 L604,38Z M400,-393 L400,-393Z M206,-118 L206,-118Z M298,-89 L298,-89Z"/>
<path class="b321" d="M-80,138 L-25,156 L-21,143 L-76,126 L-80,138Z"/>
<path class="tram" d="M548,-442 L546,-427 L542,-379 L532,-316 L498,-156 L483,-104 L460,-34 L451,-17 L438,-3 L427,4 L417,7 L390,7 L90,-85 L82,-86 L74,-84 L69,-81 L63,-74 L33,13 L-0,131 L-110,485 L-110,495 L-108,504 L-102,511 L-95,515 L199,606 L217,616 L230,631 L235,647 L236,655 L233,671 L216,711 M212,739 L240,676 L245,662 L245,649 L242,635 L237,626 L229,616 L219,609 L206,604 L-89,512 L-100,505 L-103,500 L-105,489 L-104,479 L9,116 L31,36 L46,-14 L62,-60 L67,-70 L73,-76 L81,-80 L97,-79 L391,12 L406,14 L422,11 L430,9 L441,2 L454,-11 L463,-28 L500,-149 L539,-329 L554,-449"/>
<path class="tram-core" d="M548,-442 L546,-427 L542,-379 L532,-316 L498,-156 L483,-104 L460,-34 L451,-17 L438,-3 L427,4 L417,7 L390,7 L90,-85 L82,-86 L74,-84 L69,-81 L63,-74 L33,13 L-0,131 L-110,485 L-110,495 L-108,504 L-102,511 L-95,515 L199,606 L217,616 L230,631 L235,647 L236,655 L233,671 L216,711 M212,739 L240,676 L245,662 L245,649 L242,635 L237,626 L229,616 L219,609 L206,604 L-89,512 L-100,505 L-103,500 L-105,489 L-104,479 L9,116 L31,36 L46,-14 L62,-60 L67,-70 L73,-76 L81,-80 L97,-79 L391,12 L406,14 L422,11 L430,9 L441,2 L454,-11 L463,-28 L500,-149 L539,-329 L554,-449"/>
<path class="walk" d="M-33,532 L-53,518 L-105,508 L-120,470 L-18,140 L-22,140"/>

<circle class="stop stop-here" cx="-33" cy="532" r="9"/>
<circle class="stop" cx="165" cy="-60" r="9"/>
<circle class="stop" cx="519" cy="-244" r="9"/>
<rect class="bus" x="437" y="-245" width="12" height="12" rx="2"/>
<rect class="bus" x="609" y="-293" width="12" height="12" rx="2"/>
<text class="lbl-stop halo" x="-17" y="560">Akademivej (DTU) <tspan class="sub">get off here</tspan></text>
<text class="lbl-stop halo" x="149" y="-78" text-anchor="end">Anker Engelunds Vej (DTU)</text>
<text class="lbl-stop halo" x="503" y="-260" text-anchor="end">Rævehøjvej</text>
<text class="lbl-muted halo" x="615" y="-263" text-anchor="middle">bus 150S</text>
<text class="lbl-here halo" x="-78" y="136" text-anchor="end">Building 321</text>
<text class="lbl-muted halo" x="-78" y="156" text-anchor="end">my office, 1st floor</text>
<text class="lbl-road" dy="-9"><textPath href="#lp-aev" startOffset="62%">Anker Engelunds Vej</textPath></text>
<text class="lbl-road" dy="-9"><textPath href="#lp-ak" startOffset="30%">Akademivej</textPath></text>
<text class="lbl-road" dy="-9"><textPath href="#lp-lg" startOffset="55%">Lundtoftegårdsvej</textPath></text>
<text class="lbl-road" dy="-10"><textPath href="#lp-mw" startOffset="72%">Helsingørmotorvejen</textPath></text>
<text class="lbl-muted halo" x="245" y="612">to Lyngby St. ↓</text>
<text class="lbl-muted halo" x="523" y="-307" text-anchor="end">↑ to Lundtofte</text>
<line class="scale" x1="-240" y1="590" x2="-40" y2="590"/><line class="scale" x1="-240" y1="584" x2="-240" y2="596"/><line class="scale" x1="-40" y1="584" x2="-40" y2="596"/><text class="lbl-muted" x="-140" y="580" text-anchor="middle">200 m</text>
<path class="arrow" d="M660,524 L651,556 L660,548 L669,556 Z"/><text x="660" y="574" text-anchor="middle" class="lbl-muted">N</text>
</svg>
<!-- dirmap:end -->

If the map is being uncooperative, here is [the same walk in Google Maps](https://www.google.com/maps/dir/?api=1&origin=55.78022,12.51948&destination=Matematiktorvet,+2800+Kgs.+Lyngby&travelmode=walking).

### The bus, for traditionalists

Bus **150S** (and its express sibling 15E) still runs from Nørreport up the motorway and drops you at **Rævehøjvej, DTU** in 25 minutes or so, traffic permitting. From there it is a 15-minute walk across campus to Building 321 – or, and I find this delightful, you can hop on the light rail right at the bus stop and ride a single stop to Anker Engelunds Vej (DTU), which leaves you a 500-metre walk.

## University of Copenhagen

Our University of Copenhagen offices are part of CSS on [Øster Farimagsgade](https://samf.ku.dk/kontakt/findvej/). SODAS is the part right under the fancy dome. And our space is at the very end of the SODAS hallway - see helpful illustration below.

![](/assets/20140910_directions/screenshot-2022-11-18-at-09.54.04.png)

Go through into the left gate as indicated by "Enter here" in the illustration above and walk up the stairs immediately to the left. They'll take you to the space in front of the bookstore. Proceed though that room to the central stairs (there's an elevator in the middle of the stairwell) and head to the top floor. Once at the top of the stairs, walk through the glass door and you can see the office. The room number is is 7.2.48.


[^1]: The next stop, Anker Engelunds Vej (DTU), by the main building, works almost as well. It is a coin toss, really – about 500 metres either way – but Akademivej comes first, and I am a man of simple heuristics.
