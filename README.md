#  LinkedIn Profile Search Engine

یک موتور جستجوی ساده و حرفه‌ای برای پروفایل‌های لینکدین با استفاده از **Django** و **Elasticsearch** + **Docker**

---

##  معرفی پروژه

این پروژه یک وب‌اپلیکیشن جستجو است که امکان جستجو و فیلتر روی دیتاست ۳۳۶ پروفایل لینکدین را فراهم می‌کند.  
تمرکز اصلی پروژه روی **منطق جستجو**، **معماری تمیز بک‌اند** و **ارتباط صحیح فرانت‌اند و بک‌اند** است.

پروژه با استفاده از:
- **Elasticsearch** به عنوان موتور جستجوی اصلی
- **Django ORM** برای ذخیره‌سازی داده‌ها
- **Django REST Framework** برای پیاده‌سازی API
- **Docker** برای اجرای یکپارچه و آسان

---

##  تکنولوژی‌های استفاده شده

| بخش | تکنولوژی |
|-----|-----------|
| **Backend** | Django 4.2, Django REST Framework |
| **موتور جستجو** | Elasticsearch 7.17 |
| **پایگاه داده** | SQLite (برای توسعه) |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **Containerization** | Docker, Docker Compose |
| **کتابخانه‌های اصلی** | django-elasticsearch-dsl, elasticsearch-dsl |

---

##  ساختار پروژه

```
SearchEngineProject/
├── Dockerfile                 # فایل ساخت ایمیج جنگو
├── docker-compose.yml         # اجرای همزمان جنگو و Elasticsearch
├── .dockerignore              # فایل‌های نادیده گرفته شده در داکر
├── requirements.txt           # وابستگی‌های پایتون
├── manage.py
├── search/
│   ├── models.py              # مدل Profile با JSONField
│   ├── documents.py           # Document معادل برای Elasticsearch
│   ├── services.py            # منطق جستجو (مشترک بین API و فرانت)
│   ├── serializers.py         # سریالایزر برای خروجی JSON
│   ├── views/
│   │   ├── api.py             # SearchAPIView با صفحه‌بندی
│   │   └── web.py             # HomeView برای صفحه اصلی
│   ├── urls.py
│   ├── admin.py               # پنل ادمین سفارشی
│   ├── management/commands/
│   │   └── load_data.py       # بارگذاری دیتاست از CSV
│   └── templates/search/
│       └── index.html         # صفحه جستجوی زیبا و ریسپانسیو
└── data/
    └── linkedin_dataset.csv   # دیتاست ۳۳۶ پروفایل
```

---

##  نصب و اجرا

###  روش اول: اجرا با Docker (توصیه شده)

ساده‌ترین و سریع‌ترین روش اجرای پروژه:

```bash
# 1. کلون کردن پروژه
git clone https://github.com/your-username/SearchEngineProject.git
cd SearchEngineProject

# 2. اجرا با Docker Compose
docker-compose up --build
```

پس از اجرا، پروژه روی آدرس زیر در دسترس خواهد بود:

```
http://localhost:8000
```

API جستجو نیز در آدرس زیر قابل دسترس است:

```
http://localhost:8000/api/search/
```

---

###  روش دوم: اجرای محلی (بدون Docker)

اگر Docker ندارید یا ترجیح می‌دهید پروژه را به صورت محلی اجرا کنید:

#### ۱. نصب Elasticsearch

- نسخه `7.17.25` را از [سایت رسمی Elastic](https://www.elastic.co/downloads/elasticsearch) دانلود کنید.
- فایل را Extract کرده و به پوشه `bin` بروید.
- فایل `elasticsearch.yml` را در پوشه `config` ویرایش کرده و این خط را اضافه کنید:
  ```yaml
  xpack.security.enabled: false
  ```
- فایل `elasticsearch.bat` (ویندوز) یا `elasticsearch` (لینوکس/مک) را اجرا کنید.
- از صحت اجرا با باز کردن `http://localhost:9200` در مرورگر مطمئن شوید.

#### ۲. نصب وابستگی‌های پایتون

```bash
# ایجاد و فعال‌سازی محیط مجازی
python -m venv venv
source venv/bin/activate   # در ویندوز: venv\Scripts\activate

# نصب وابستگی‌ها
pip install -r requirements.txt
```

#### ۳. تنظیمات و بارگذاری داده

```bash
# اعمال مایگریشن‌ها
python manage.py migrate

# بارگذاری دیتاست
python manage.py load_data

# ایندکس کردن داده‌ها در Elasticsearch
python manage.py search_index --rebuild -f
```

#### ۴. اجرای سرور

```bash
python manage.py runserver
```

حالا می‌توانید در مرورگر خود به `http://localhost:8000` بروید.

---

##  نحوه استفاده

### صفحه اصلی (فرانت‌اند)


- **کلمه کلیدی**: جستجو در نام، عنوان شغلی، مهارت‌ها و خلاصه
- **مهارت**: فیلتر بر اساس مهارت‌ها
- **عنوان شغلی**: فیلتر بر اساس عنوان شغلی
- **کشور**: فیلتر بر اساس کشور
- **صنعت**: فیلتر بر اساس صنعت شرکت

نتایج به صورت **کارت‌های زیبا** با صفحه‌بندی (۱۰ آیتم در هر صفحه) نمایش داده می‌شوند.

---

### API جستجو

**اندپوینت:**
```
GET /api/search/
```

**پارامترها (همگی اختیاری):**

| پارامتر | توضیح | مثال |
|---------|-------|------|
| `q` | کلمه کلیدی | `?q=manager` |
| `skill` | فیلتر مهارت | `&skill=recruiting` |
| `title` | فیلتر عنوان شغلی | `&title=human_resources` |
| `country` | فیلتر کشور | `&country=united%20states` |
| `industry` | فیلتر صنعت | `&industry=civil%20engineering` |
| `page` | شماره صفحه (پیش‌فرض: ۱) | `&page=2` |
| `page_size` | تعداد آیتم در هر صفحه (پیش‌فرض: ۱۰) | `&page_size=20` |

**مثال درخواست:**
```
GET /api/search/?q=manager&skill=recruiting&title=manager&page=1
```

**پاسخ نمونه:**
```json
{
    "count": 336,
    "next": "http://localhost:8000/api/search/?page=2&q=manager&skill=recruiting&title=manager",
    "previous": null,
    "results": [
        {
            "full_name": "joseph holland",
            "job_title": "recruiting manager",
            "skills": ["recruiting", "leadership", "human resources"],
            "summary": "Celebrating its 100th year, Garver is...",
            "location_name": "denton, texas, united states",
            "linkedin_url": "https://linkedin.com/in/joeyholland"
        }
    ]
}
```

---

##  منطق جستجو و فیلترها

### جستجوی کلمه کلیدی

با استفاده از `multi_match` در Elasticsearch، جستجو به صورت همزمان روی فیلدهای زیر انجام می‌شود:
- `full_name`
- `job_title`
- `skills`
- `summary`

همچنین با فعال کردن `fuzziness='AUTO'`، جستجو **غلط‌های املایی** را نیز تشخیص می‌دهد (مثلاً `pythn` → `python`).

### فیلترها

فیلترها با استفاده از `filter` در Elasticsearch پیاده‌سازی شده‌اند تا:
- **سرعت بالاتر**: فیلترها کش می‌شوند
- **امتیازدهی تحت تأثیر قرار نگیرد**: نتایج مرتب‌سازی بر اساس جستجوی کلمه کلیدی انجام می‌شود

---

##  Docker

### فایل‌های داکر

**`Dockerfile`**:
- مبتنی بر `python:3.9-slim`
- نصب وابستگی‌های سیستمی و پایتون
- کپی پروژه و اجرای سرور

**`docker-compose.yml`**:
- سرویس `elasticsearch`: نسخه `7.17.25` با امنیت غیرفعال
- سرویس `web`: جنگو با خودکارسازی مایگریشن، ایندکس‌سازی و اجرا

### متغیرهای محیطی

| متغیر | توضیح | مقدار پیش‌فرض |
|-------|-------|---------------|
| `ELASTICSEARCH_HOST` | آدرس Elasticsearch در داکر | `http://elasticsearch:9200` |

---

##  دیتاست

دیتاست شامل ۳۳۶ پروفایل لینکدین با فیلدهای زیر است:

- **اطلاعات هویتی**: نام، نام‌خانوادگی، جنسیت، آدرس لینکدین
- **اطلاعات شغلی**: عنوان شغلی، نقش، شرکت، صنعت
- **مهارت‌ها**: لیستی از مهارت‌ها (به صورت JSON)
- **سوابق شغلی و تحصیلی**: لیستی از دیکشنری‌ها (به صورت JSON)
- **اطلاعات تکمیلی**: خلاصه، موقعیت مکانی، سال‌های تجربه

---

##  ویژگی‌های برجسته

-  جستجوی **Full-Text** با **Elasticsearch**
-  صفحه‌بندی (Pagination) با قابلیت تنظیم `page_size`
-  سریالایزر برای خروجی JSON **تمیز و کنترل‌شده**
-  **5 فیلتر** (کلمه کلیدی، مهارت، عنوان شغلی، کشور، صنعت)
-  فرانت‌اند **ریسپانسیو** و **زیبا** با جاوااسکریپت خالص
-  پنل ادمین **سفارشی** با نمایش زیبای JSON
-  **Dockerized** برای اجرای یکپارچه
-  **مدیریت خطا** و نمایش پیام‌های مناسب

---

##  تست با curl

```bash
# جستجوی ساده
curl "http://localhost:8000/api/search/?q=manager"

# جستجو با فیلترهای ترکیبی
curl "http://localhost:8000/api/search/?q=engineer&skill=python&country=united%20states"
```

---

##  نکات مهم برای توسعه‌دهندگان

### بارگذاری دیتاست

برای بارگذاری مجدد دیتاست (مثلاً بعد از تغییر مدل):

```bash
python manage.py load_data
```

### بازسازی ایندکس Elasticsearch

```bash
python manage.py search_index --rebuild -f
```








---



##  ارتباط با توسعه‌دهنده

- **نام**: محمد متین پورجواد
- **ایمیل**: matinpourjavad@gmail.com

---


---

**ساخته شده با   Django + Elasticsearch**

---

