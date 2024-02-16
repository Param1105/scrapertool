
# Scraper Tool

A brief description of what this project does and who it's for


## Deployment

To deploy this project run

```bash
    python scrapertool/manage.py makemigrations

    python scrapertool/manage.py migrate

    python scrapertool/manage.py runserver

    cd scrapertool/

    celery -A scrapertool worker -l info

    celery -A scrapertool beat -l info
```

