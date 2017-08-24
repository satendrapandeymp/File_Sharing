from cx_Freeze import setup,Executable

MIMENAMES = [
    'audio',
    'base',
    'image',
    'message',
    'multipart',
    'nonmultipart',
    'text',
    ]

email_includes = ['email.mime.' + x for x in MIMENAMES]

includes = []

includes.extend(email_includes)

bin_includes = [
        'libcrypto.so.1.0.0',
        'libcrypto.so.10',
        'libgssapi_krb5.so.2',
        'libk5crypto.so.3',
        'libkeyutils.so.1',
        'libssl.so.1.0.1e',
        'libssl.so.10'
    ]

excludes = ['Tkinter']
packages = ['markupsafe', 'flask', 'click', 'werkzeug', 'itsdangerous' ]

setup(
    name = 'myapp',
    version = '0.1',
    description = 'A general enhancement utility',
    author = 'lenin',
    author_email = 'le...@null.com',
    options = {'build_exe': {'packages':packages,'includes':includes,'excludes':excludes,'bin_includes':bin_includes}}, 
    executables = [Executable('main.py')]
)
