# SM_APP – Backend (Django + DRF + JWT)

هذا المستودع يحتوي على الباك‑إند لمنصّة **محور سوشال** ضمن مظلّة **آفاق ديجيتال**.  
يقدّم API لإدارة حسابات السوشال، الألبومات، والمنشورات، مع مصادقة JWT وربط بواجهة React.

## المكوّنات الرئيسية

- Django + Django REST Framework لبناء الـ API.
- djangorestframework-simplejwt للمصادقة عبر JWT (access + refresh token).
- Postgres كقاعدة بيانات في بيئة الإنتاج (Railway)، و SQLite افتراضيًا محليًا.
- تطبيقات:
  - `accounts` لإدارة حسابات السوشال (SocialAccount).
  - `mahwar_social` لإدارة الألبومات والمنشورات والإحصاءات الخاصة بالداشبورد.
- إعداد CORS للسماح بالوصول من:
  - الواجهة المحلية `http://localhost:3000`.
  - واجهة GitHub Pages: `https://Ihsan76.github.io/afaq-frontend`.

## تشغيل المشروع محليًا

من داخل مجلد المشروع:

cd D:\Projects\python\SM_APP

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser # أول مرة فقط
python manage.py runserver


ثم افتح في المتصفح:

- لوحة الإدارة: <http://127.0.0.1:8000/admin/>
- API الداشبورد: <http://127.0.0.1:8000/api/mahwar/dashboard/>

## نقاط الـ API المهمة

- مصادقة JWT:

  - `POST /api/auth/token/`  
    يرسل JSON: `{"username": "...", "password": "..."}`  
    ويعيد: `access`, `refresh`.

- لوحة الداشبورد:

  - `GET /api/mahwar/dashboard/`  
    يتطلب هيدر: `Authorization: Bearer <access_token>`  
    ويعيد بيانات من نوع:

    - `stats`: أعداد المسودات، المجدولة، المنشورة.
    - `recent_posts`: قائمة بأحدث المنشورات (مع الحالة والمحتوى).
    - `social_accounts`: قائمة بحسابات السوشال المرتبطة.

(يمكن لاحقًا إضافة توثيق مفصل لكل endpoint عند بناء CRUD كامل للحسابات والمنشورات.)

## النشر الحالي

- الإنتاج حاليًا على **Railway** (خطة تجريبية/مدفوعة خفيفة):
  - Django + Postgres ضمن خدمة واحدة.
  - النشر يتم تلقائيًا من فرع `main` في هذا المستودع.
- إعدادات مهمة في `settings.py`:
  - متغيرات البيئة: `SECRET_KEY`, إعدادات Postgres, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`.
  - `CORS_ALLOWED_ORIGINS` يتضمّن نطاق GitHub Pages.

## الارتباط بالفرونت‑إند

واجهة React (في مستودع `afaq-frontend`) تتصل بهذا الباك‑إند عبر:

- محليًا: `http://127.0.0.1:8000`
- في الإنتاج: رابط Railway مثل: `https://sm-app.up.railway.app`

ويتم تحديد العنوان من خلال `API_BASE_URL` في واجهة React.
