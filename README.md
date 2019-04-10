# UAS Bahasa Pemrograman 1

## Fork
* lakukan fork pada repository dengan mengklik tombol fork pada https://github.com/abuazzam/uaspy

![github](https://github.com/Marinska/uaspy/blob/master/1.PNG)

## Clone
*  Silahkan clone repository yang sudah anda fork, pada repository local

![github](https://github.com/Marinska/uaspy/blob/master/2.PNG)


## Melakukan konfigurasi Virtual Environment pada Pycharm
*  Pada menu editor PyCharm, silahkan buka Setting kemudian pada project interpreter, tambahkan pengaturan baru sesuai direktori repository anda

![github](https://github.com/Marinska/uaspy/blob/master/3.PNG)

![github](https://github.com/Marinska/uaspy/blob/master/4.PNG)

*  Setelah itu Instal pip pygame pada PyCharm, tunggu kemudian check versi dari pip

![github](https://github.com/Marinska/uaspy/blob/master/5.PNG)


## Membuat Class App pada main.py
*  Pertama import terlebih dahulu class baseapp pada baseapp.py 
*  Setelah itu buat class dengan nama App berdasarkan BaseApp
```
from core.baseapp import BaseApp

class App(BaseApp):
    pass


if __name__ == "__main__":
         theApp = App()
         theApp.run()
```

![github](https://github.com/Marinska/uaspy/blob/master/7.PNG)

## Menjalankan Program
*  Jalankan program dengan me-RUN program

![github](https://github.com/Marinska/uaspy/blob/master/6.PNG)