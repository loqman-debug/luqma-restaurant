---
name: shadcn-ui
description: Design and develop clean, accessible, and themeable web applications and dashboards using shadcn/ui, Radix UI, Tailwind CSS, and Lucide Icons. Use this skill whenever the user asks for dashboards, admin panels, form validation, dialogs, drawers, or data tables.
---

# shadcn/ui

Build high-performance, fully customizable React / Next.js interfaces with shadcn/ui.

## Setup & Initialization

```bash
npx shadcn@latest init
```

Choose style, base color, and CSS variables.

## Adding Key Components

```bash
npx shadcn@latest add button card dialog drawer table dropdown-menu badge
```

## Dashboard / Admin Pattern

```tsx
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";

export function OrderCard({ orderId, customer, total, status }: any) {
  return (
    <Card className="border-border/40 bg-card/60 backdrop-blur-md">
      <CardHeader className="flex flex-row items-center justify-between pb-2">
        <CardTitle className="text-sm font-medium">طلب #{orderId}</CardTitle>
        <Badge variant={status === 'completed' ? 'default' : 'secondary'}>
          {status === 'completed' ? 'مكتمل' : 'قيد التجهيز'}
        </Badge>
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{total} ر.ي</div>
        <p className="text-xs text-muted-foreground mt-1">العميل: {customer}</p>
        <Button size="sm" className="w-full mt-4" variant="outline">
          إرسال عبر واتساب
        </Button>
      </CardContent>
    </Card>
  );
}
```

## Arabic RTL Integration
- Ensure `dir="rtl"` is applied on root layout.
- Radix UI primitives like `Dialog`, `DropdownMenu`, and `Drawer` respect logical flex direction and RTL placement.
- Use `lucide-react` icons and flip directional icons (arrows, chevrons) where appropriate.
