from django.db import models
from django.contrib.auth.models import User


class SocialAccount(models.Model):
    PLATFORM_CHOICES = [
        ("facebook", "Facebook"),
        ("twitter", "Twitter / X"),
        ("instagram", "Instagram"),
        ("tiktok", "TikTok"),
        ("linkedin", "LinkedIn"),
        ("youtube", "YouTube"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="social_accounts",
    )
    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES,
    )
    account_name = models.CharField(
        max_length=150,
        help_text="اسم الحساب كما يظهر في المنصة.",
    )
    account_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="المعرّف الداخلي للحساب في منصة السوشيال ميديا (إن وُجد).",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="هل ما زال الحساب متصلاً وصالحًا للاستخدام؟",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Social Account"
        verbose_name_plural = "Social Accounts"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.platform} - {self.account_name}"
