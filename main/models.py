from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=5)
    is_active = models.BooleanField(default=True)
    brith_data = models.DateField(null=True, blank=True)

    Courses = models.ManyToManyField("main.Course", related_name="courses", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def courses_count(self):
        return self.courses_count()

    def __str__(self):
        return f"student: {self.name} - #{self.id}"
    
    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"
        ordering = ["id"]



class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    discount_type_choices = (
        ("flex", "Aniq summa"),
        ("percent", "Foizli")
    )
    discount_type = models.CharField(max_length=10, choices=discount_type_choices)
    discount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def final_price(self):
        if self.discount:
            if self.discount_type == "percent":
                return self.price - (self.price / 100 * self.discount)
            return self.price - self.discount

        return self.price
    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ["id"]