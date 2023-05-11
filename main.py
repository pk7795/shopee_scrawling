from getItems import getItems
import multiprocessing

if __name__ == "__main__":
    p1 =multiprocessing.Process(target=getItems, args=(20000, 30000))
    p2 = multiprocessing.Process(target=getItems, args=(40000, 50000))
    p3 = multiprocessing.Process(target=getItems, args=(50190, 60000))
    p4 = multiprocessing.Process(target=getItems, args=(30000, 40000))


    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("done")
