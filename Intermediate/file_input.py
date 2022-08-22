def read():
    try:
        data = []
        with open("./archivos/PyDjangoEnv1.txt","r",encoding="utf-8") as f:
            for line in f:
                data.append(str(line))
        print(data)
    except:
        pass
    finally:
        f.close()

def write():
    try:
        data = ["numpy==1.23.2","pandas==1.4.3","python-dateutil==2.8.2","pytz==2022.2.1","six==1.16.0"]
        with open("./archivos/PyDjangoEnv1.txt","w",encoding="utf-8") as f:
            for line in data:
                f.write(line + "\n")
    except:
        pass
    finally:
        f.close()

def write_no_del():
    try:
        data = ["numpy==1.23.2","pandas==1.4.3","python-dateutil==2.8.2","pytz==2022.2.1","six==1.16.0"]
        with open("./archivos/PyDjangoEnv1.txt","a",encoding="utf-8") as f:
            for line in data:
                f.write(line + "\n")
    except:
        pass
    finally:
        f.close()


def run():
    write_no_del()

if __name__ == '__main__':
    run()