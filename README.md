<div dir="rtl">

<p align="center">
  <img src="assets/banner.png" alt="مهارت‌های فارسی Cursor — Persian Writing Skills for Cursor" width="100%" />
</p>

<h1 align="center">اسکیل‌های فارسی حرفه‌ای برای Cursor</h1>

<p align="center">
  دو اسکیل قابل‌حمل برای نوشتن، ویرایش و طبیعی‌سازی متن فارسی در Cursor
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Cursor-Skills-0d9488?style=flat-square" alt="Cursor Skills" />
  <img src="https://img.shields.io/badge/Language-Persian%20%2F%20فارسی-115e59?style=flat-square" alt="Persian" />
  <img src="https://img.shields.io/badge/Focus-Natural%20Writing-334155?style=flat-square" alt="Natural Writing" />
</p>

---

دو اسکیل قابل‌حمل برای نوشتن، ویرایش و طبیعی‌سازی متن فارسی در Cursor.

| پوشه | نقش |
|------|-----|
| <span dir="ltr">[`persian-writing-mastery`](persian-writing-mastery/)</span> | نویسندگی و تولید فارسی صحیح، روان و متناسب با لحن |
| <span dir="ltr">[`natural-persian-text-editor`](natural-persian-text-editor/)</span> | تحلیل و ویرایش متن موجود در ۵ حالت خروجی |

هدف: کیفیت واقعی نوشتار فارسی — نه دور زدن ابزارهای تشخیص هوش مصنوعی.

## نصب در یک پروژه

۱. پوشه‌های <span dir="ltr">`persian-writing-mastery`</span> و <span dir="ltr">`natural-persian-text-editor`</span> را کپی کن به:

</div>

<div dir="ltr">

```text
your-project/.cursor/skills/
```

</div>

<div dir="rtl">

ساختار نهایی:

</div>

<div dir="ltr">

```text
your-project/
└── .cursor/
    └── skills/
        ├── persian-writing-mastery/
        │   └── SKILL.md
        └── natural-persian-text-editor/
            └── SKILL.md
```

</div>

<div dir="rtl">

۲. در چت Agent بگو مثلاً:

> اسکیل‌های فارسی داخل <span dir="ltr">`.cursor/skills`</span> را بخوان و از این به بعد برای متن فارسی از آن‌ها استفاده کن.

یا برای یک کار مشخص:

> با <span dir="ltr">`persian-writing-mastery`</span> یک README فارسی برای این پروژه بنویس.
> با <span dir="ltr">`natural-persian-text-editor`</span> این متن را طبیعی‌سازی کن.

## چه زمانی کدام اسکیل؟

- **تولید یا بازنویسی از صفر** ← <span dir="ltr">`persian-writing-mastery`</span>
- **تحلیل / ویرایش / طبیعی‌سازی متن موجود** ← <span dir="ltr">`natural-persian-text-editor`</span>

اسکیل دوم برای قواعد پایهٔ نگارشی به قواعد اسکیل اول تکیه می‌کند (یا چک‌لیست فشرده داخل خودش).

## تست سریع

نمونه‌ها در <span dir="ltr">[`tests/samples/`](tests/samples/)</span>:

</div>

<div dir="ltr">

```bash
# بررسی ساختاری بسته‌ها و خروجی‌های مرجع
python3 tests/validate_skills.py

# Skill 1 — تولید: به Agent بده tests/samples/skill1-prompt.md
# Skill 2 — طبیعی‌سازی: به Agent بده tests/samples/skill2-input.md
```

</div>

<div dir="rtl">

نتایج مرجع: <span dir="ltr">[`tests/expected/`](tests/expected/)</span>  
نتایج اجرای زنده: <span dir="ltr">[`tests/live-results/`](tests/live-results/)</span>

## محدودیت‌ها

- منبع، نقل‌قول یا تجربهٔ شخصی جعلی نمی‌سازد.
- معنا را بدون دلیل تغییر نمی‌دهد و ادعای تأییدنشده اضافه نمی‌کند.
- غلط املایی یا شلختگی عمدی ایجاد نمی‌کند.
- عبور از آشکارساز متن هوش مصنوعی را تضمین نمی‌کند و هدفش فریب آشکارساز نیست.

## انتشار روی GitHub

همین پوشه را می‌توانی به‌عنوان ریپو عمومی منتشر کنی تا دیگران همان ساختار را در <span dir="ltr">`.cursor/skills`</span> کپی کنند.

</div>
