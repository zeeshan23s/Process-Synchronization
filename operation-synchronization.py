from time import sleep
from threading import *

rw_mutex = Semaphore(1)
mutex = Semaphore(1)
read_count = 0

class writerProcess(Thread):
    def run(self):
        rw_mutex.acquire()

        # writing is performed 
        print("Writing....")
        file = open("file.txt","a+")
        author = input("Enter Your Name: ")
        text = input("Enter Text You Like To Save: ")
        file.write(text + " - " + author + "\n")
        file.close
        print("Complete Writing....")

        rw_mutex.release()
        return
        

class readerProcess(Thread):
    def run(self):
        mutex.acquire()
        global read_count 
        read_count = read_count + 1
        if(read_count == 1):
            rw_mutex.acquire()
        mutex.release()
        
        # reading is performed 
        print("Reading....")
        try:
            file = open("file.txt", 'r')
            display = file.read()
            print(display[:-1])
            sleep(10)
            file.close()
        except:
            print("FILE DON'T EXISTS.")
        print("Complete Reading....")

        mutex.acquire()
        read_count = read_count - 1
        if(read_count == 0):
            rw_mutex.release()
        mutex.release()
        
        

def main():
    _read = readerProcess()
    _read.start()
    _write = writerProcess()
    _write.start()


if __name__ == "__main__":
    main()
