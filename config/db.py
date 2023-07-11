import os


MYSQL_AZURE={
  'default':{
  'ENGINE':'django.db.backends.mysql',
  'NAME':os.environ.get("DBNAME"), #nombre de la base de datos
  'USER':os.environ.get("DBUSER"),
  'PASSWORD':os.environ.get("DBPASS"),
  'HOST':os.environ.get("DBHOST"), #servidor local o también puede ser 'localhost'
  'PORT':'3306'
  }
}
MYSQL_LOCAL={
  'default':{
  'ENGINE':'django.db.backends.mysql',
  'NAME':'juegossena', #nombre de la base de datos
  'USER':'root',
  'PASSWORD':'root',
  'HOST':'127.0.0.1', #servidor local o también puede ser 'localhost'
  'PORT':'3306'
  }
}