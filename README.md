# shopping

## 1 - About us

Our website application is an e-commerce platform that provides users with personalized and intelligent shopping experiences. The project was designed and developed with a modular approach, including product, product_csv, order, user, and product_admin modules. We selected the Amazon sales dataset from https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset and designed a database that includes product, review, user, shopping cart, and order tables using sqlite3 and managed it with Navicat. The website has a front-end and a back-end, and different user levels with corresponding permissions.


## 2 - Main features

* View the summary of disaster data
* Public navigation bar, About Us section, and search function
* User registration, login, and logout
* Home page with recommended products and links to product detail pages
* Product list page with filters by category
* Product detail page with product information, user reviews, and recommendations for similar products
* Shopping cart page to add, delete, and checkout products
* My Orders page for logged-in users to view their orders
* Login and logout for administrators and different user levels with permissions
* Order management, user management, and dashboard with graphs for administrators

## 3 - Database overview

![](https://github.com/wangleiz166/studyInAberdeen/blob/main/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230505205725.png?raw=true)

## 4 - Installation

### 4.1 If you are using Codio:

#### 4.1.1 Create a virtual environment and activate it in the terminal of Codio
``` shell
    python3 -m venv .venv 
```

``` shell
    source .venv/bin/activate 
```

#### 4.1.2 Clone the repository or pull the code from Github
``` shell
    git clone git@github.com:wangleiz166/cs551q-solo-assignment.git
```
Or if you have cloned before

``` shell
    git pull origin main
```

#### 4.1.3 Changed the site details in **ALLOWED_HOSTS** of ```shop/setting.py```

For example:

``` shell
    ALLOWED_HOSTS = ['*']
    CSRF_TRUSTED_ORIGINS = ['https://aprilpicnic-bronzefilm-8000.codio-box.uk','https://cs551q-solo-assignment.onrender.com']
```

#### 4.1.4 Install Django and Plotly in terminal

As for the Django installation

``` shell
    pip install django
```

As for the Plotly in terminal

``` shell
    pip install plotly
```

#### 4.1.5 Run the website application

``` shell
    python3 manage.py runserver 0.0.0.0:8000
```

P.S **8000** is decided by what did you input in 3.1.3

### 4.2 If you are using a local editor, such as Visual Studio Code, or Mac Terminal:

#### 4.2.1 Create a virtual environment and activate it in the terminal
``` shell
    python3 -m venv .venv 
```

``` shell
    source .venv/bin/activate 
```

#### 4.2.2 Clone the repository or pull the code from Github
``` shell
    git clone git@github.com:wangleiz166/cs551q-solo-assignment.git
```
Or if you have cloned before

``` shell
    git pull origin main
```

#### 4.2.3 Changed the site details in **ALLOWED_HOSTS** of ```shop/setting.py```

For example:

``` shell
    ALLOWED_HOSTS = ['*']
    CSRF_TRUSTED_ORIGINS = ['https://aprilpicnic-bronzefilm-8000.codio-box.uk','https://cs551q-solo-assignment.onrender.com']
```

#### 4.2.4 Install Django and Plotly in terminal

As for the Django installation

``` shell
    pip install django
```

As for the Plotly in terminal

``` shell
    pip install plotly
```

#### 4.2.5 Run the website application

``` shell
    python3 manage.py runserver
```

## 5 - Test
To use Behave for testing in a Django project, you will need to follow these steps:

1.Install Behave and Django-Behave-Runner::

```
pip install behave django-behave
```

2.In the `settings.py` file of your Django project, add `'django_behave.runner.djangotestrunner'` to your test runner, and INSTALLED_APPS: `

```python
INSTALLED_APPS = [
     ...
    'behave_django'.
]

TEST_RUNNER = 'behave_django.runner.BehaviorDrivenTestRunner'
```
3. Create a directory called `features` in parallel with your Django manage.py that will contain your feature files and step definitions.
The directory structure is as follows:
```
    features/
        steps/
            __init__.py
            myapp_steps.py
        myapp.feature
        environment.py
```
4. Write a feature file (`.feature`). Feature files are written in the Gherkin language and describe the expected behaviour of the application. For example, in `myapp.feature`:
5. Write the corresponding step definitions. In the ``myapp/features/steps/myapp_steps.py`` file, you need to define the Python functions that match the steps described in the features file.
6. Run the test in the root directory (the directory where manage.py is located).

![](https://github.com/wangleiz166/studyInAberdeen/blob/main/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20230505125939.png?raw=true)

## 6 - Details of deploying the website application

The website application has been deployed to Render, here is its URL: https://cs551q-solo-assignment.onrender.com.

Build command:

``` shell
    pip install --upgrade pip && pip install -r requirements.txt
```

Start command:

``` shell
    gunicorn mysite.shop:application
```