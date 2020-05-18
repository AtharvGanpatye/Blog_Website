In [1]: from blog.models import Post                                  

In [2]: from django.contrib.auth.models import User                   

In [3]: Post.objects.all()                                            
Out[3]: <QuerySet [<Post: Blog 1>]>

In [4]: user = User.objects.get(id=1)                                 

In [5]: user                                                          
Out[5]: <User: AtharvG>

In [6]: post_2 = Post(title="Blog 2", content='Second Post Content !',
   ...: author_id=user_id)                                            
----------------------------------------------------------------------
NameError                            Traceback (most recent call last)
<ipython-input-6-42e43f4f34d7> in <module>
----> 1 post_2 = Post(title="Blog 2", content='Second Post Content !',author_id=user_id)

NameError: name 'user_id' is not defined

In [7]: post_2 = Post(title="Blog 2", content='Second Post Content !',
   ...: author_id=user.id)                                            

In [8]: post_2.save()                                                 

In [9]: Post.objects.all()                                            
Out[9]: <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>

In [10]: post = Post.objects.first()                                  

In [11]: post.content                                                 
Out[11]: 'First Post Content !'

In [12]: post.date_posted                                             
Out[12]: datetime.datetime(2020, 5, 17, 13, 18, 39, 500019, tzinfo=<UTC>)

In [13]: post.author                                                  
Out[13]: <User: AtharvG>

In [14]: post.author_id                                               
Out[14]: 1

In [15]: post.author.email                                            
Out[15]: 'atharvganpatye@gmail.com'

In [16]: user                                                         
Out[16]: <User: AtharvG>

In [17]: user.post_set                                                
Out[17]: <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager at 0x7fc54bf858d0>

In [18]: user.post_set.all()                                          
Out[18]: <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>

In [19]: user.post_set.create(title='Blog 3', content='Third Post contentent')                                                        
Out[19]: <Post: Blog 3>

In [20]: Post.objects.all()                                           
Out[20]: <QuerySet [<Post: Blog 1>, <Post: Blog 2>, <Post: Blog 3>]>

In [21]: exit()
