
## Running the Project Locally

First, clone the repository to your local machine by typing the command below in terminal:

```bash
git clone https://github.com/xxozmozxx2/scheduler.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Make migrations:

```bash
python manage.py makemigrations
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

