# Accuknox Django Trainee Assignment

Solutions for the Django Signals questions and the Rectangle class task.
Answers with code snippets are also in `Accuknox_Django_Assignment_B_Aman_Ulla_Khan.pdf`.

## Setup

```
cd django_project
python -m venv venv
venv\Scripts\activate          # on Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

## Django Signals

Each question has its own model, receiver (in `signals_demo/signals.py`) and management command.

**Q1. Are signals synchronous or asynchronous?**
Synchronous. The receiver sleeps for 5 seconds and the caller's `save()` takes about 5 seconds to return.

```
python manage.py q1_sync
```

**Q2. Do signals run in the same thread as the caller?**
Yes. The caller and the receiver print the same thread id.

```
python manage.py q2_thread
```

**Q3. Do signals run in the same database transaction as the caller?**
Yes. Inside `transaction.atomic()` the receiver writes an `AuditLog` row, then the caller raises an error. After the rollback both rows are gone.

```
python manage.py q3_transaction
```

## Rectangle class

`signals_demo/rectangle.py` takes `length` and `width` as ints. Iterating over it gives `{'length': ...}` first and then `{'width': ...}`.

```
python manage.py rectangle_demo
```

Output:

```
{'length': 10}
{'width': 5}
```

## Project structure

```
django_project/
├── manage.py
├── requirements.txt
├── accuknox_assignment/      settings, urls
└── signals_demo/
    ├── models.py             Q1Record, Q2Record, Q3Record, AuditLog
    ├── signals.py            post_save receivers
    ├── apps.py               connects the receivers in ready()
    ├── rectangle.py          Rectangle class
    └── management/commands/  q1_sync, q2_thread, q3_transaction, rectangle_demo
```
