from time import sleep


class TrafficLight:
    __color = 1

    def ruhhing(self):
        while True:
            if self.__color == 1:
                print("\033[31mred")
                sleep(7)
                self.__color = 2
            elif self.__color == 2:
                print("\033[33myellow")
                sleep(2)
                self.__color = 3
            elif self.__color == 3:
                print("\033[32mgreen")
                sleep(7)
                self.__color = 4
            else:
                print("\033[33myellow")
                sleep(2)
                self.__color = 1


run = TrafficLight()
run.ruhhing()
