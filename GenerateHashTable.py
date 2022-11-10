import hashlib
import json
import os


class GenerateCrackStation:
    def __init__(self):
        self.__string_list = [chr(x) for x in range(ord("a"), ord("z") + 1)]
        for i in range(0, 10):
            self.__string_list.append(str(i))
        self.__table_index = 0
        self.__table = {}
        self.__table_file = open(
            f"{os.path.dirname(os.path.realpath(__file__))}/table.json", "w+"
        )

    def __generate_sha256(self, __string):
        __sha256 = hashlib.sha256(__string.encode("utf-8")).hexdigest()
        self.__table.update({__sha256:__string})
        return __sha256

    def __generate_3bit(self):
        for bit1 in self.__string_list:
            for bit2 in self.__string_list:
                for bit3 in self.__string_list:
                    print(
                        str(bit1 + bit2 + bit3)
                        + ":"
                        + self.__generate_sha256(str(bit1 + bit2 + bit3))
                    )
                    self.__table_index += 1

    def __generate_2bit(self):
        for bit1 in self.__string_list:
            for bit2 in self.__string_list:
                print(str(bit1 + bit2) + ":" + self.__generate_sha256(str(bit1 + bit2)))
                self.__table_index += 1

    def __generate_1bit(self):
        for bit1 in self.__string_list:
            print(str(bit1) + ":" + self.__generate_sha256(str(bit1)))
            self.__table_index += 1

    def __create_file(self):
        json_object = json.dumps(self.__table, indent=4)
        with self.__table_file as file:
            file.write(json_object)

    def generate(self):
        self.__generate_1bit()
        self.__generate_2bit()
        self.__generate_3bit()
        self.__create_file()
        print(self.__table_index)
        print(self.__table)


if __name__ == "__main__":
    cs = GenerateCrackStation()
    cs.generate()
