from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=100)



class Books(models.Model):
    title = models.CharField(max_length=200)
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    publish_date = models.DateField()


class Members(models.Model):
    name = models.CharField(max_length=100)
    join_date = models.DateField(null=False,blank=False)



class BorrowingRecords(models.Model):
    book_id = models.OneToOneField(Books, on_delete=models.CASCADE)
    member_id = models.OneToOneField(Members,on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()



