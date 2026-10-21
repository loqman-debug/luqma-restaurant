---
name: scrollytelling-arabic
description: Build scroll-driven (scrollytelling) websites with GSAP ScrollTrigger and Lenis, with full Arabic and RTL support. Use this skill whenever the user asks for a scroll animation website, scrollytelling, parallax landing page, restaurant or food website with animation, or an animated infographic page, especially if the content is in Arabic, even if they do not say "scrollytelling" explicitly.
---

# Scrollytelling Arabic (RTL)

Build cinematic, fast, accessible scroll-driven websites. Arabic and RTL are first-class, not an afterthought.

## Default stack

- **Plain HTML + CSS + JS** for a single landing page; **Next.js + Tailwind** if the user asks for a full app.
- **GSAP + ScrollTrigger** for all scroll animation.
- **Lenis** for smooth scrolling, synced with ScrollTrigger.
- **Scrollama** only when the story is data/chart driven (sticky graphic + text steps).
- **Three.js / Spline** only if the user explicitly wants 3D.

Install with npm (`npm install gsap lenis`) or pinned CDN versions. Never use unpinned `@latest` URLs.

## Workflow

1. Confirm the story: what is the goal, how many scenes (default 5 to 7), what is the call to action.
2. Write one line per scene: what the visitor sees, what moves, what text appears.
3. Build the static layout first (no animation), check RTL and mobile.
4. Add animation scene by scene.
5. Test performance and reduced motion before finishing.

## RTL and Arabic rules

- Set `<html lang="ar" dir="rtl">`.
- Use **logical CSS properties**: `margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `text-align: start`. Avoid `left` and `right`.
- Horizontal animations must be mirrored: content that enters from the "start" side enters from the right in RTL. Compute direction from `document.dir`, never hardcode `x: -100`.
- Fonts: **Cairo**, **Tajawal**, **IBM Plex Sans Arabic**, or **Noto Kufi Arabic** from Google Fonts, always with a fallback stack (`system-ui, sans-serif`).
- Line height 1.7 or more for Arabic body text. Do not use letter-spacing on Arabic (it breaks letter joining).
- **Never split Arabic text into individual letters** (SplitType by chars, etc.). It breaks letter connections. Animate by **word or line** only.
- Use Arabic-Indic numerals only if the brand wants them; otherwise keep Western digits consistent.
- Mixed Arabic/English: wrap English fragments in `<span dir="ltr">`.
- Carousels, progress bars, and timelines must also flow right to left.

## Animation patterns

**Smooth scroll + ScrollTrigger sync**
```js
gsap.registerPlugin(ScrollTrigger);
const lenis = new Lenis();
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((t) => lenis.raf(t * 1000));
gsap.ticker.lagSmoothing(0);
```

**Pinned scene with scrub**
```js
gsap.timeline({
  scrollTrigger: { trigger: '.scene', start: 'top top', end: '+=150%', scrub: true, pin: true }
}).from('.scene .title', { y: 60, opacity: 0 })
  .from('.scene .image', { scale: 1.2 }, '<');
```

**Direction-aware reveal (RTL safe)**
```js
const dir = document.dir === 'rtl' ? 1 : -1;
gsap.from('.card', { x: 80 * dir, opacity: 0, scrollTrigger: { trigger: '.card', start: 'top 80%' } });
```

Prefer animating `transform` and `opacity` only. Do not animate `width`, `height`, `top`, or `left`.

## Scene structure (typical restaurant or product story)

1. **Hero**: large hero image or short looping video, title, subtle slow zoom.
2. **Story**: pinned section, text lines fade in as the user scrolls.
3. **Hero dish/product**: image scales or rotates with scroll (use transparent PNG/WebP cutout).
4. **Menu/gallery**: horizontal scroll section or staggered grid reveal.
5. **Social proof**: reviews or numbers counting up.
6. **Call to action**: order, book, or contact button, sticky on mobile.

## Images and media

- Use **WebP or AVIF**, target under 200 KB per image, same aspect ratio across a gallery.
- `loading="lazy"` for everything below the first screen; preload only the hero image.
- Always write a meaningful Arabic `alt` text.
- Videos: MP4/WebM, muted, `playsinline`, under 5 MB, with a poster image.
- For scroll-scrubbed image sequences, use a canvas and keep frames under about 120 at reduced resolution.
- Only use images the user owns or that have a license allowing commercial use. Say so when unsure.

## Performance and accessibility (required)

- Respect reduced motion:
```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
if (reduce) { /* skip pin, scrub, parallax; show final states */ }
```
- Use `ScrollTrigger.matchMedia` or `gsap.matchMedia()` to simplify or disable heavy effects on mobile.
- Test at 375px width. No horizontal page scroll. Touch targets at least 44px.
- Contrast ratio of 4.5:1 or more for text over images (add a gradient overlay).
- Keep the page usable without JavaScript (content visible, animation as enhancement).
- Target Lighthouse mobile of 85 or more.
- Call `ScrollTrigger.refresh()` after images and fonts load.
- Clean up triggers on unmount in React (`ctx.revert()`).

## Common mistakes to avoid

- Hardcoded `left/right` values that break in RTL.
- Splitting Arabic text by character.
- Too many simultaneous animations; use one or two motions per scene.
- Pinning long sections on mobile without testing.
- Huge unoptimized images or autoplay videos with sound.
- Using external scripts from unknown CDNs.

## Final checklist before delivering

- [ ] RTL layout verified, fonts load, no broken letter joining
- [ ] Every scene animates correctly scrolling down and back up
- [ ] Reduced-motion fallback works
- [ ] Mobile layout checked
- [ ] Images compressed with alt text
- [ ] Short README explaining how to change text, images, and colors
