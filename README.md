
## Running the Project Locally

First, clone the repository to your local machine by typing the command below in terminal:

```bash
git clone https://github.com/xxozmozxx2/scheduler.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

create super user with this command :

```bash
python manage.py createsuperuser
```

run the development server:

```bash
python manage.py runserver
```

create rooms in the admin panel. 
```bash
127.0.0.1:8000/admin
```

The project will be available at **127.0.0.1:8000**.
