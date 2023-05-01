from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=260)
    picture = models.ImageField(upload_to='books')
    writer_name = models.CharField(max_length=260)
    regular_price = models.IntegerField()
    discount_price = models.IntegerField(default=regular_price,blank=True, null=True)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='category_pic')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    

class Languege(models.Model):
    languege_name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.languege_name
    
class Skill_Level(models.Model):
    level_name = models.CharField(max_length=120)


    def __str__(self) -> str:
        return self.level_name


class Course(models.Model):
    course_image = models.ImageField(upload_to='course_image', null=True)
    course_video = models.CharField(max_length=650, null=True)
    title_1 = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=300)
    languege = models.ForeignKey(Languege, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    description= models.TextField()
    price = models.IntegerField(null=True, default=0)
    discount = models.IntegerField(null=True)
    skill_level = models.ForeignKey(Skill_Level, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)
    deadline = models.DateField(null=True, blank=True)
    certificate = models.CharField(max_length=20)
    publish_satatus = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Course.objects.filter(slug=slug).order_by('-id')
    exsist = qs.exists()

    if exsist:
        new_slug = "%s-%s" % (slug, qs.filter().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
def pre_save_post_receive(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receive, Course)


    
class Lesson(models.Model):
    name = models.CharField(max_length=260)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='crs')


    def __str__(self) -> str:
        return self.name
    

class Video(models.Model):
    serial_number = models.IntegerField(null=True)
    thumbnail = models.ImageField(upload_to='video_Thumbnail')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='cls_video')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='video_leson')
    title = models.CharField(max_length=200)
    youtube_id = models.CharField(max_length=200)
    time_duration = models.IntegerField()
    preview = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title



class Whats_learn(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    pont1 = models.CharField(max_length=190, blank=True, null=True)
    pont2 = models.CharField(max_length=190, blank=True, null=True, default='')
    pont3 = models.CharField(max_length=190, blank=True, null=True)
    pont4 = models.CharField(max_length=190, blank=True, null=True)
    pont5 = models.CharField(max_length=190, blank=True, null=True)
    pont6 = models.CharField(max_length=190, blank=True, null=True)
    pont7 = models.CharField(max_length=190, blank=True, null=True)

    def __str__(self):
        return str(self.course.title_1)
    

class Requierment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    point_1 = models.CharField(max_length=260,null=True, blank=True)
    point_2 = models.CharField(max_length=260,null=True, blank=True)
    point_3 = models.CharField(max_length=260,null=True, blank=True)


    def __str__(self):
        return str(self.course.title_1)