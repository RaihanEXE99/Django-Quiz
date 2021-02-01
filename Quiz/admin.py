from django.contrib import admin
from .models import CustomizeQuiz,Tquestion,Myself,Slide,Department_or_branch
# Register your models here.
admin.site.register(CustomizeQuiz)
admin.site.register(Tquestion)
admin.site.register(Myself)
admin.site.register(Slide)
admin.site.register(Department_or_branch)


# class SlideImageAdmin(admin.StackedInline):
#     model = SlideImage

# @admin.register(Slide)
# class SlideAdmin(admin.ModelAdmin):
#     inlines = [SlideImageAdmin]

#     class Meta:
#         model = Slide
        
# @admin.register(SlideImage)
# class SlideImageAdmin(admin.ModelAdmin):
#     pass
