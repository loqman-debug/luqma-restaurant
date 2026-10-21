---
name: bsmnt-scrollytelling
description: Build declarative, cinema-grade scroll-driven animations in React and Next.js using Basement Studio's Scrollytelling library (@bsmnt/scrollytelling), GSAP, and Lenis. Use this skill whenever the user asks for cinematic scrollytelling in React/Next.js, pinned story scenes, scroll-scrubbed layers, or animated landing pages.
---

# BSMNT Scrollytelling

Build cinematic, scroll-bound web experiences in React / Next.js with `@bsmnt/scrollytelling`, GSAP ScrollTrigger, and Lenis.

## Core Packages

```bash
npm install @bsmnt/scrollytelling gsap lenis
```

## Architecture & Concepts

BSMNT Scrollytelling decomposes scroll experiences into three core components:
1. **`Root`**: Provides the scroll context and coordinates GSAP ScrollTrigger with Lenis smooth scrolling.
2. **`Pin`**: Pins a container in the viewport for a specified duration (`amount` or pixel height).
3. **`Animation`**: Declarative tweens that scrub with the scroll position inside a pinned section.

## Basic Implementation Pattern

```tsx
import { Root, Pin, Animation } from '@bsmnt/scrollytelling';

export default function ScrollyExperience() {
  return (
    <Root start="top top" end="bottom bottom" debug={false}>
      <Pin childHeight="100vh" pinSpacerHeight="300vh" top={0}>
        <div className="relative w-full h-screen overflow-hidden flex items-center justify-center">
          <Animation
            tween={{
              start: 0,
              end: 50,
              from: { opacity: 0, y: 100, scale: 0.8 },
              to: { opacity: 1, y: 0, scale: 1 },
              ease: 'power2.out'
            }}
          >
            <h1 className="text-6xl font-bold text-white">المشهد الأول</h1>
          </Animation>

          <Animation
            tween={{
              start: 50,
              end: 100,
              from: { opacity: 0, y: 100 },
              to: { opacity: 1, y: 0 },
              ease: 'power2.out'
            }}
          >
            <div className="text-3xl text-amber-400">المشهد الثاني</div>
          </Animation>
        </div>
      </Pin>
    </Root>
  );
}
```

## RTL Guidelines for Arabic
- Always wrap text and coordinate animations using logical offsets (`dir="rtl"`).
- Invert horizontal transforms (`x: 100 * (isRTL ? -1 : 1)`).
- Ensure line heights are at least 1.7 for Arabic fonts (Cairo, Tajawal).
- Never split Arabic words into characters.
