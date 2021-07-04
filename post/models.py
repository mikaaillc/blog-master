from django.db import models
from django.urls import reverse
from django.utils.text import slugify #slug oluştumak için



class post(models.Model):
    user=models.ForeignKey('auth.User',verbose_name='Yazar',on_delete=models.CASCADE,related_name='posts')
    baslik = models.CharField(max_length=120,verbose_name='Başlık')#mmutak max uzunluk belirt
    metin= models.TextField(verbose_name='İçerik')
    yayin=models.DateTimeField(verbose_name='Yayınlanma Tarihi',auto_now_add=True)
    image=models.ImageField(null= True ,blank=True)
    slug=models.SlugField(unique=True,editable=False,max_length=130)

    #FileField ile hetr uzantıda dosya yüklenebilir

    def __str__(self):
        return self.baslik
    def get_absolute_url(self):
       # return "/post/{}".format(self.id)
        return reverse('post:detail',kwargs={'slug':self.slug})
    def guncel(self):
       # return "/post/{}".format(self.id)
        return reverse('post:update',kwargs={'slug':self.slug})
    def sil(self):
       # return "/post/{}".format(self.id)
        return reverse('post:delete',kwargs={'slug':self.slug})
    def olustur(self):
        return reverse('post:create')

    def get_unique_slug(self): # eşsiz slug oluşturmak için
        slug=slugify(self.baslik.replace('ı','i'))
        uniq_slug=slug
        counter=1
        while post.objects.filter(slug =uniq_slug).exists():
            uniq_slug='{}-{}'.format(slug,counter)
            counter+=1
        return uniq_slug

    def save(self, *args,**kwargs):#save modeli eziliyor override
        self.slug=self.get_unique_slug()     #eşsiz slug oluşuyor
        return super(post,self).save(*args,**kwargs)
    class Meta:
        ordering=['-yayin', 'slug']

class Comment(models.Model):
    post=models.ForeignKey('post.post',related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(verbose_name='İsim',max_length=200)
    yorum=models.TextField(verbose_name='Yorum')
    creat_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-creat_date']
