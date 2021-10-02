import pytest
from register import *
from login import *
from project import *
# ------------------------testing-----------------
@pytest.fixture
def username():

    usernameR_entry=StringVar
    return [usernameR_entry]


@pytest.fixture
def name():
    name_entry = "nabin khanal"
    return [name_entry]

@pytest.fixture
def adress():
    adress_entry="kirtipur"
    return [adress_entry]
@pytest.fixture
def no():
    phoneno_entry="20-01-2000"
    return [DOB_entry]

@pytest.fixture
def password():
    password_entry="nabin"
    return [password_entry]



def test1(username):
    x="nabin"
    assert username  [0]==x


def test2(name):
    y="nabin khanal"
    assert name [0]==y


def test3(adress):
    z = "lalitpur"
    assert adress[0] == z

def test4(no):
    c= 9861447181
    assert no[0]==c

def test5(password):
    d="nabin"
    assert password[0]==d

# ---------------------------------login page testing-----------------------
@pytest.fixture
def l_username():

    username_entry="nabin"
    return [username_entry]

@pytest.fixture
def l_password():
    password_entry="nabin"
    return [password_entry]


def test6(l_username):
    e="nabin"
    assert l_username  [0]==e


def test7(l_password):
    f="nabin"
    assert l_password[0]==f

# ---------------------------#---------project testing-----------------------------------------


def website():

    website_entry=StringVar
    return [website_entry]


def test8(l_password):
    f=StringVar
    assert l_password[0]==f
