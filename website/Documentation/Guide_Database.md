# Using django for ParlimentAIry database -Guide
Currently this project contains a database in the db.sqlite3 file. This means
the database information will exist locally and for updates to databases, you
will need to pull for updated versions.

## Database plan
A database contains data objects, instances that contain information from the
website. Our parlimentAIry project contains one such database. A database can
contain multiple **tables**. Each table lists a different type of object.

### Included tables
For now, only a Question table is created. In django, tables are created through
**models** and are constructed similarly to a python class in the file called
models.py. In this project, you can find the file in the following directory:

```
website/q_answering/models.py
```

### Planned tables
Later, we plan to add a table for:
* **old questions**
* **articles**


## Creating a database table
Creating a database table is done in the following way:
* Add a new data object model to models.py
* Compile the code to update the database structure

### Creating a model
For the exact syntax for the django models, I will refer you to the [django
documentation](https://docs.djangoproject.com/en/2.1/ref/models/fields/)

**Pointer: always include a \_\_str\_\_ function to make the object
representation human readable.**

### Compile model to update table

After having written the code in models.py we can now make a migration:
```
python manage.py makemigrations q_answering
```

We can check the newest migration edits when we open the following folder in
our editor:
```
website/q_answering/migrations/
```

When happy with all the migrations, we can 'build' the new table. This is when
python uses sql to update our database structure:
```
python manage.py migrate
```

## Accessing information from database
Accessing information from the database is now straightforward as we are using
django, and can be done directly in python. It is somewhat similar to using
python classes. Here I shall demonstrate how to work with database information
using the already implemented Question model.

### Accessing a table
This works similarly to importing local python files. This is necessary if you
wish to have any sort of access to the table.
```
from q_answering.models import Question
```

### Accessing rows from a table
We can query the database table through python, and ask the table to return
a list with specific rows (objects) from a table.

**Select all:**

All question objects in table are returned in an iterable QuerySet
```
Question.objects.all()
```

**Select with filter:**

All question objects in table where the field 'status' has the value 'IP'
are returned in an iterable QuerySet.
```
Question.objects.filter(status='IP')
```

**Get a specific object:**

If you want to retrieve a specific object from the table, and know for sure that
your query will return exactly one object (e.g. because you query the primary
key id), you can use the get method to return the object immediately:
```
Question.objects.get(pk=1)
```

## Updating the database
**Change field value**

You can simply change the value of a field by assigning the new (valid) value to
the attribute:
```
q = Question.objects.get(pk=1)
q.description = "hello world"
```

**Add to table**

To update this to the actual database, save it like so:
```
q.save()
```

**Delete from table**

To delete the entire entry from the database, delete it like so:
```
q.delete()
```
