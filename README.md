<p align="center">
  <img src="assets/banner.png" alt="مهارت‌های فارسی Cursor — Persian Writing Skills for Cursor" width="100%" />
</p>

<h1 align="center">Skillهای فارسی حرفه‌ای برای Cursor</h1>

<p align="center">
  دو Skill قابل‌حمل برای نوشتن، ویرایش و طبیعی‌سازی متن فارسی در Cursor
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Cursor-Skills-0d9488?style=flat-square" alt="Cursor Skills" />
  <img src="https://img.shields.io/badge/Language-Persian%20%2F%20فارسی-115e59?style=flat-square" alt="Persian" />
  <img src="https://img.shields.io/badge/Focus-Natural%20Writing-334155?style=flat-square" alt="Natural Writing" />
</p>

---

دو Skill قابل‌حمل برای نوشتن، ویرایش و طبیعی‌سازی متن فارسی در Cursor.

| پوشه | نقش |
|------|-----|
| [`persian-writing-mastery`](persian-writing-mastery/) | نویسندگی و تولید فارسی صحیح، روان و متناسب با لحن |
| [`natural-persian-text-editor`](natural-persian-text-editor/) | تحلیل و ویرایش متن موجود در ۵ حالت خروجی |

هدف: کیفیت واقعی نوشتار فارسی — نه دور زدن ابزارهای تشخیص AI.

## نصب در یک پروژه

1. پوشه‌های `persian-writing-mastery` و `natural-persian-text-editor` را کپی کن به:

```text
your-project/.cursor/skills/
```

ساختار نهایی:

```text
your-project/
└── .cursor/
    └── skills/
        ├── persian-writing-mastery/
        │   └── SKILL.md
        └── natural-persian-text-editor/
            └── SKILL.md
```

2. در چت Agent بگو مثلاً:

> Skillهای فارسی داخل `.cursor/skills` را بخوان و از این به بعد برای متن فارسی از آن‌ها استفاده کن.

یا برای یک کار مشخص:

> با `persian-writing-mastery` یک README فارسی برای این پروژه بنویس.
> با `natural-persian-text-editor` این متن را طبیعی‌سازی کن.

## چه زمانی کدام Skill؟

- **تولید یا بازنویسی از صفر** → `persian-writing-mastery`
- **تحلیل / ویرایش / طبیعی‌سازی متن موجود** → `natural-persian-text-editor`

Skill دوم برای قواعد پایه نگارشی به قواعد Skill اول تکیه می‌کند (یا چک‌لیست فشرده داخل خودش).

## تست سریع

نمونه‌ها در [`tests/samples/`](tests/samples/):

```bash
# بررسی ساختاری بسته‌ها و خروجی‌های مرجع
python3 tests/validate_skills.py

# Skill 1 — تولید: به Agent بده tests/samples/skill1-prompt.md
# Skill 2 — طبیعی‌سازی: به Agent بده tests/samples/skill2-input.md
```

نتایج مرجع: [`tests/expected/`](tests/expected/)  
نتایج اجرای زنده: [`tests/live-results/`](tests/live-results/)

## محدودیت‌ها

- منبع، نقل‌قول یا تجربه شخصی جعلی نمی‌سازد.
- معنا را بدون دلیل تغییر نمی‌دهد و ادعای تأییدنشده اضافه نمی‌کند.
- غلط املایی یا شلختگی عمدی ایجاد نمی‌کند.
- عبور از AI Detector را تضمین نمی‌کند و هدفش فریب آشکارساز نیست.

## انتشار بعدی روی GitHub

همین پوشه را می‌توانی به‌عنوان ریپو عمومی منتشر کنی تا دیگران همان ساختار را در `.cursor/skills` کپی کنند.
# persian-skills
