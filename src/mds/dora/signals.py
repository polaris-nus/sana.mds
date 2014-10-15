from django.db.models.signals import post_save

def my_callback(sender, **kwargs):
    print('Changed!')
    
post_save.connect(my_callback)