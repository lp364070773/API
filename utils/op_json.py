
class operationJson(object):
    def __init__(self, file_path="../test_data/login.json"):
        self.file_path = file_path
        self.data = self.get_data()
 
    def get_data(self):
        with open(self.file_path) as f:
            data = json.load(f)
            return data
 
    def get_key_words(self, key=None):
        if key:
            return self.data[key]
        else:
            return self.data
 
 
if __name__ == '__main__':
    print(operationJson().get_key_words())
    print(operationJson().get_key_words("login"))
    print(operationJson().get_key_words("login")['username'])