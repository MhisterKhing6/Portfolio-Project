class Common:
    def to_dict(self):
        temp = self.__dict__.copy()
        if "_sa_instance_state" in temp:
            del temp["_sa_instance_state"]
        return temp
