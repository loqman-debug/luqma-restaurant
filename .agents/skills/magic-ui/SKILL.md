---
name: magic-ui
description: Build high-conversion, futuristic landing pages and web apps using Magic UI components, animated backgrounds, shaders, bento grids, and shimmer effects. Use this skill whenever the user asks for Magic UI, luxury tech landing pages, animated grids, marquee logos, or interactive particle backgrounds.
---

# Magic UI

Integrate luxury, modern UI components, background animations, and interactive elements inspired by Magic UI (`magicui.design`).

## Core Technologies
- React / Next.js
- Tailwind CSS
- Lucide React
- Framer Motion / Motion

## Recommended Installation

```bash
npx shadcn@latest init
npx shadcn@latest add @magicui/marquee
npx shadcn@latest add @magicui/bento-grid
npx shadcn@latest add @magicui/retro-grid
npx shadcn@latest add @magicui/particles
npx shadcn@latest add @magicui/shimmer-button
```

## Signature Components

### 1. Marquee (Continuous Loop)
Ideal for customer reviews, partners, or product highlights in Arabic RTL:
```tsx
import Marquee from "@/components/magicui/marquee";

export function ReviewsMarquee() {
  return (
    <Marquee pauseOnHover reverse className="[--duration:25s]" dir="rtl">
      {reviews.map((rev) => (
        <ReviewCard key={rev.id} {...rev} />
      ))}
    </Marquee>
  );
}
```

### 2. Bento Grid
Structured showcase for product features with hover glow:
```tsx
import { BentoCard, BentoGrid } from "@/components/magicui/bento-grid";

export function FeatureGrid() {
  return (
    <BentoGrid className="max-w-5xl mx-auto">
      {features.map((feature) => (
        <BentoCard key={feature.name} {...feature} />
      ))}
    </BentoGrid>
  );
}
```

### 3. Shimmer Button & Particle Canvas
High-converting CTA buttons with moving border gradients and interactive particle canvas backgrounds.
