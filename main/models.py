from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=5)
    is_active = models.BooleanField(default=True)
    brith_data = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    


    def __str__(self):
        return f"dtudent: {self.name} - #{self.id}"
    
    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"
        ordering = ["id"]