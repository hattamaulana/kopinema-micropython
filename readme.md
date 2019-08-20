<h1 align="center"> Smart Coffee Brewing </h1>

### Guide Started
Open this project location in terminal

Install esptool.py globally
```bash
$ pip3 install esptool
```

Setup PATH
```bash
$ echo "export $PATH=$PATH:/home/<user>/.local/bin" >> ~/.profile
$ source ~/.profile
```

Flashing NodeMCU, [download file binary](http://micropython.org/download#esp8266)
```bash
$ esptool.py --port /dev/ttyUSB0 erase_flash
$ esptool.py \
    --port /dev/ttyUSB0 \
    --baud 460800 \
    write_flash \
    --flash_size=detect \
    -fm dio 0 \
    esp8266-20190529-v1.11.bin
``` 

Create Virtual Environment
```bash
$ virtualenv venv
```

Activate Virtual Environment
```bash
$ source venv/bin/activate 
```

Install all requirements
```bash
(venv) $ pip3 install -r requirements.txt
```

### Upload / Run
Open this project location in terminal


Upload file ke root
```bash
(venv) $ ampy --port /dev/ttyUSB0 --baud 115200 put file.py 
```

Upload file ke directory
```bash
(venv) $ ampy --port /dev/ttyUSB0 --baud 115200 mkdir usocketio
(venv) $ ampy --port /dev/ttyUSB0 --baud 115200 put usocketio/__init__.py uscoketio/__init__.py
```

Run file
```bash
(venv) $ ampy --port /dev/ttyUSB0 --baud 115200 run file.py 
```

Others Command 
```bash
(venv) $ ampy --help 
```


### Reference
[Micropython Docs](https://docs.micropython.org/en/latest/index.html)