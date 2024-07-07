from django.db import models

class Exercise(models.Model):
    MUSCLE_GROUP_CHOICES = [
        ('Chest', 'Chest'),
        ('Back', 'Back'),
        ('Legs', 'Legs'),
        ('Arms', 'Arms'),
        ('Shoulders', 'Shoulders'),
        ('Core', 'Core'),
    ]

    EQUIPMENT_CHOICES = [
        ('None', 'None'),
        ('Dumbbells', 'Dumbbells'),
        ('Barbell', 'Barbell'),
        ('Machine', 'Machine'),
        ('Bands', 'Bands'),
        ('Kettlebells', 'Kettlebells'),
    ]

    DIFFICULTY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=50, choices=MUSCLE_GROUP_CHOICES)
    equipment = models.CharField(max_length=50, choices=EQUIPMENT_CHOICES)
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    video_url = models.URLField(blank=True, null=True)
    steps = models.TextField()

    def __str__(self):
        return self.name
    
    