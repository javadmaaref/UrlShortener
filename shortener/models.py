from django.db import models
from django.utils import timezone
import string

characters = string.ascii_letters + string.digits

# این ایده از While و for بهتره چون اونا توی آخری ها خیلی تعداد محاسباتشون میره بالا
def base_conversion(num):
    if num == 0:
        return characters[0]
    arr = []
    base = len(characters)
    while num:
        rem = num % base
        num = num // base
        arr.append(characters[rem])
    arr.reverse()
    return ''.join(arr)


class URL(models.Model):
    original_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=5, unique=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    # این نیازه چون مثل While نیستش، با خود ID کار داره
    def save(self, *args, **kwargs):
        if not self.short_url:
            super().save(*args, **kwargs)  # اول ID بساز
            self.short_url = self.generate_short_url()
            # بعد لینک کوتاه رو اضافه کن
            kwargs['force_insert'] = False
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def generate_short_url(self):
        # حال ندارم عوضش کنم با اصلی
        return base_conversion(self.id)

    def __str__(self):
        return f"{self.short_url} -> {self.original_url}"
